"""
Compatibility Rules for Amalgam

Determines tier eligibility, checks component compatibility,
and generates warnings for edge cases.

This is the "brain" of the wizard - it takes inventory and produces
tier recommendations with explanations.
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

from .boards import BOARDS, BoardSpec, boards_can_combine_for_drivers
from .extruders import EXTRUDERS, ExtruderSpec
from .motors import get_motor_count_for_tier, get_driver_count_for_tier


class Severity(Enum):
    """Severity level for compatibility issues."""
    INFO = "info"           # FYI, no action needed
    WARNING = "warning"     # Works but suboptimal
    ERROR = "error"         # Will not work, must resolve


@dataclass
class CompatibilityIssue:
    """A single compatibility issue or note."""
    severity: Severity
    message: str
    suggestion: Optional[str] = None


@dataclass
class TierRequirements:
    """Requirements to qualify for a tier."""
    tier: int
    name: str
    description: str
    min_motors: int
    min_drivers: int
    z_type: str             # "belt" or "triple"
    requires_host: bool     # Needs separate Klipper host
    notes: list[str]


@dataclass
class CompatibilityResult:
    """Result of compatibility analysis."""
    recommended_tier: int
    max_possible_tier: int
    issues: list[CompatibilityIssue] = field(default_factory=list)
    tier_breakdown: dict = field(default_factory=dict)


# =============================================================================
# TIER DEFINITIONS
# =============================================================================

TIER_REQUIREMENTS = {
    0: TierRequirements(
        tier=0,
        name="Klipper Only",
        description="Just upgrade firmware, no Amalgam build",
        min_motors=0,
        min_drivers=0,
        z_type="existing",
        requires_host=True,
        notes=["Not a Amalgam build", "Flash Klipper on existing printer"],
    ),
    1: TierRequirements(
        tier=1,
        name="Single Donor",
        description="One donor printer, belt-driven Z",
        min_motors=4,
        min_drivers=4,
        z_type="belt",
        requires_host=True,
        notes=[
            "Uses single Z motor with belt to drive both Z rods",
            "Simplest build, good for learning",
            "Needs Klipper host (Pi, CB1, or old laptop)",
        ],
    ),
    2: TierRequirements(
        tier=2,
        name="Dual Donor",
        description="Two donor printers, Triple-Z, multi-MCU",
        min_motors=6,
        min_drivers=6,
        z_type="triple",
        requires_host=True,
        notes=[
            "Triple independent Z for bed leveling",
            "May need multi-MCU (two boards) for 6+ drivers",
            "Needs Klipper host",
        ],
    ),
    3: TierRequirements(
        tier=3,
        name="Reference Spec",
        description="MKS SKIPR, Triple-Z, integrated host",
        min_motors=6,
        min_drivers=6,
        z_type="triple",
        requires_host=False,  # SKIPR has integrated host
        notes=[
            "REFERENCE SPECIFICATION",
            "MKS SKIPR: 6 drivers + integrated Klipper host",
            "No separate Pi/CB1 needed",
            "Buy SKIPR, scavenge everything else",
        ],
    ),
}


def get_tier_requirements(tier: int) -> Optional[TierRequirements]:
    """Get requirements for a specific tier."""
    return TIER_REQUIREMENTS.get(tier)


def determine_tier(
    motor_count: int,
    driver_count: int,
    board_ids: list[str],
    has_separate_host: bool = False,
    prefer_integrated: bool = True,
) -> CompatibilityResult:
    """
    Determine the recommended tier based on available components.

    Args:
        motor_count: Number of stepper motors available
        driver_count: Number of stepper drivers available
        board_ids: List of board IDs being used
        has_separate_host: Whether a separate Klipper host exists (Pi, etc.)
        prefer_integrated: Whether to prefer integrated solutions (SKIPR)

    Returns:
        CompatibilityResult with tier recommendation and issues
    """
    issues = []
    tier_breakdown = {}

    # Check each tier from highest to lowest
    for tier in [3, 2, 1, 0]:
        reqs = TIER_REQUIREMENTS[tier]
        can_achieve = True
        tier_issues = []

        # Motor check
        if motor_count < reqs.min_motors:
            can_achieve = False
            tier_issues.append(f"Need {reqs.min_motors} motors, have {motor_count}")

        # Driver check
        if driver_count < reqs.min_drivers:
            can_achieve = False
            tier_issues.append(f"Need {reqs.min_drivers} drivers, have {driver_count}")

        # Host check
        if reqs.requires_host and not has_separate_host:
            # Check if any board has integrated host
            has_integrated = any(
                BOARDS.get(bid, BoardSpec("", "", "", 0, False, False, 0, "", 0, False, "", [], 0, 0)).integrated_host
                for bid in board_ids
            )
            if not has_integrated:
                can_achieve = False
                tier_issues.append("Needs Klipper host (Pi/CB1/laptop)")

        # Tier 3 specific: must use SKIPR or equivalent
        if tier == 3:
            has_skipr = "MKS_SKIPR" in board_ids
            if not has_skipr:
                if prefer_integrated:
                    can_achieve = False
                    tier_issues.append("Tier 3 requires MKS SKIPR (or equivalent 6-driver integrated board)")
                else:
                    tier_issues.append("Tier 3 typically uses MKS SKIPR for integrated host")

        tier_breakdown[tier] = {
            "achievable": can_achieve,
            "issues": tier_issues,
            "requirements": reqs,
        }

    # Find highest achievable tier
    max_tier = 0
    for tier in [3, 2, 1, 0]:
        if tier_breakdown[tier]["achievable"]:
            max_tier = tier
            break

    # Recommended tier (may be lower than max for practical reasons)
    recommended = max_tier

    # Add issues for gaps between current and higher tiers
    if max_tier < 3:
        for tier in range(max_tier + 1, 4):
            for issue_msg in tier_breakdown[tier]["issues"]:
                issues.append(CompatibilityIssue(
                    severity=Severity.INFO,
                    message=f"Tier {tier}: {issue_msg}",
                    suggestion=f"To reach Tier {tier}, address this requirement",
                ))

    return CompatibilityResult(
        recommended_tier=recommended,
        max_possible_tier=max_tier,
        issues=issues,
        tier_breakdown=tier_breakdown,
    )


def check_compatibility(
    extruder_id: str,
    motor_type: str,
    rod_diameter: float,
    bed_size_x: int,
    bed_size_y: int,
) -> list[CompatibilityIssue]:
    """
    Check component compatibility and generate warnings.

    This is where edge cases get caught:
    - NEMA14 with Pitan: PLA only warning
    - Heavy extruder with M8 rods: strong warning
    - Large bed with light rods: warning

    Args:
        extruder_id: Extruder type ID
        motor_type: Motor type for extruder
        rod_diameter: Smooth rod diameter in mm
        bed_size_x: Bed X dimension
        bed_size_y: Bed Y dimension

    Returns:
        List of compatibility issues
    """
    issues = []

    extruder = EXTRUDERS.get(extruder_id)
    if not extruder:
        issues.append(CompatibilityIssue(
            severity=Severity.WARNING,
            message=f"Unknown extruder: {extruder_id}",
            suggestion="Using default Pitan values for analysis",
        ))
        return issues

    # Check extruder motor compatibility
    if "NEMA14" in motor_type:
        issues.append(CompatibilityIssue(
            severity=Severity.WARNING,
            message="NEMA14 motor with Pitan has significantly reduced torque",
            suggestion="Run analysis tool. May be limited to PLA/PETG only. Consider NEMA17 pancake instead.",
        ))

    if "pancake" in motor_type.lower() or "42x25" in motor_type or "42x20" in motor_type:
        issues.append(CompatibilityIssue(
            severity=Severity.INFO,
            message="Pancake motor detected - reduced torque headroom",
            suggestion="Works fine for most filaments. Run analysis to verify.",
        ))

    # Check rod compatibility
    if rod_diameter < extruder.min_rod_diameter:
        issues.append(CompatibilityIssue(
            severity=Severity.WARNING,
            message=f"{extruder.name} ({extruder.mass_grams}g) may cause excessive sag on M{int(rod_diameter)} rods",
            suggestion=f"Consider M{extruder.min_rod_diameter}+ rods or lighter extruder",
        ))

    # Check bed/rod combination
    max_span = max(bed_size_x, bed_size_y) + 100  # Approximate X gantry span

    if rod_diameter == 8.0 and max_span > 300:
        issues.append(CompatibilityIssue(
            severity=Severity.WARNING,
            message=f"M8 rods with {max_span}mm span may have excessive deflection",
            suggestion="Upgrade to M10 rods for larger beds",
        ))

    if rod_diameter == 8.0 and extruder.mass_grams > 300:
        issues.append(CompatibilityIssue(
            severity=Severity.ERROR,
            message=f"Heavy extruder ({extruder.mass_grams}g) on M8 rods will cause print quality issues",
            suggestion="Use M10+ rods or switch to lighter extruder (Pitan: 280g)",
        ))

    # Large bed power warning
    if bed_size_x >= 300 or bed_size_y >= 300:
        issues.append(CompatibilityIssue(
            severity=Severity.INFO,
            message="Large bed (300mm+) requires higher-power PSU",
            suggestion="Plan for 30A+ PSU at 24V",
        ))

    return issues


def check_board_driver_count(board_ids: list[str], tier: int) -> list[CompatibilityIssue]:
    """
    Check if boards provide enough drivers for the tier.

    Args:
        board_ids: List of board IDs
        tier: Target tier

    Returns:
        List of issues related to driver count
    """
    issues = []
    required = get_driver_count_for_tier(tier)

    total_drivers = sum(
        BOARDS.get(bid, BoardSpec("", "", "", 0, False, False, 0, "", 0, False, "", [], 0, 0)).stepper_drivers
        for bid in board_ids
    )

    if total_drivers < required:
        deficit = required - total_drivers
        issues.append(CompatibilityIssue(
            severity=Severity.ERROR,
            message=f"Need {required} drivers for Tier {tier}, have {total_drivers} ({deficit} short)",
            suggestion="Add another board or upgrade to board with more drivers",
        ))
    elif total_drivers == required:
        issues.append(CompatibilityIssue(
            severity=Severity.INFO,
            message=f"Exactly {total_drivers} drivers for Tier {tier} - no expansion room",
            suggestion="Consider board with extra drivers for future flexibility",
        ))

    # Multi-MCU warning
    if len(board_ids) > 1:
        issues.append(CompatibilityIssue(
            severity=Severity.INFO,
            message="Multi-MCU configuration detected",
            suggestion="Requires USB connection between boards and Klipper multi-MCU setup",
        ))

    return issues
