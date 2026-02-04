"""
Motor Registry for Amalgam

Defines motor types and counts needed for each tier.
Motors are typically scavenged from donor printers, so this registry
focuses on what builders can expect to find and how to use them.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MotorSpec:
    """Specification for a stepper motor type."""

    id: str                     # Internal identifier
    name: str                   # Display name
    frame_size: str             # NEMA17, NEMA14, etc.
    length_mm: int              # Body length (not including shaft)

    # Performance
    holding_torque_ncm: int     # Holding torque in N·cm
    rated_current_a: float      # Rated current in Amps

    # Physical
    mass_grams: int
    shaft_diameter: float       # mm

    # Common sources
    typical_source: str

    # Compatibility
    suitable_for: list[str]     # Which uses: "X", "Y", "Z", "E"
    notes: list[str]
    warnings: list[str]


# =============================================================================
# MOTOR SOURCES (where motors come from)
# =============================================================================

MOTOR_SOURCES = {
    "ender3": {
        "name": "Ender 3 / Ender 3 Pro",
        "motor_count": 4,
        "motor_types": ["NEMA17_42x34"],  # Standard 34mm body
        "notes": "All 4 motors are identical 42-34 steppers",
    },
    "ender3_v2": {
        "name": "Ender 3 V2",
        "motor_count": 4,
        "motor_types": ["NEMA17_42x34"],
        "notes": "Same motors as Ender 3, dual-Z uses single motor + belt",
    },
    "cr10": {
        "name": "CR-10 / CR-10S",
        "motor_count": 5,
        "motor_types": ["NEMA17_42x40", "NEMA17_42x34"],
        "notes": "5 motors: Z may have longer motor",
    },
    "prusa_mk3": {
        "name": "Prusa MK3/MK3S",
        "motor_count": 4,
        "motor_types": ["NEMA17_42x25", "NEMA17_42x40"],  # Pancake E, regular XYZ
        "notes": "Extruder uses pancake motor, XYZ are standard",
    },
    "ender5": {
        "name": "Ender 5 / Ender 5 Pro",
        "motor_count": 4,
        "motor_types": ["NEMA17_42x34", "NEMA17_42x40"],
        "notes": "CoreXY donor - may have larger Z motor",
    },
}


# =============================================================================
# MOTOR DEFINITIONS
# =============================================================================

MOTORS = {
    # -------------------------------------------------------------------------
    # Standard NEMA17 (most common)
    # -------------------------------------------------------------------------
    "NEMA17_42x34": MotorSpec(
        id="NEMA17_42x34",
        name="NEMA17 42x34mm (Standard)",
        frame_size="NEMA17",
        length_mm=34,
        holding_torque_ncm=40,
        rated_current_a=1.5,
        mass_grams=280,
        shaft_diameter=5.0,
        typical_source="Ender 3, Ender 3 V2, most budget printers",
        suitable_for=["X", "Y", "Z", "E"],
        notes=[
            "Most common stepper in donor printers",
            "Good balance of torque and size",
            "Works for all Amalgam axes",
        ],
        warnings=[],
    ),

    "NEMA17_42x40": MotorSpec(
        id="NEMA17_42x40",
        name="NEMA17 42x40mm (Long)",
        frame_size="NEMA17",
        length_mm=40,
        holding_torque_ncm=55,
        rated_current_a=1.7,
        mass_grams=350,
        shaft_diameter=5.0,
        typical_source="CR-10, some Ender 5, Z axes",
        suitable_for=["X", "Y", "Z"],
        notes=[
            "Higher torque than standard",
            "Often found on Z axis of larger printers",
            "Heavier - best for non-moving axes",
        ],
        warnings=[
            "Too heavy for direct-drive extruder",
        ],
    ),

    # -------------------------------------------------------------------------
    # Pancake motors (short)
    # -------------------------------------------------------------------------
    "NEMA17_42x25": MotorSpec(
        id="NEMA17_42x25",
        name="NEMA17 42x25mm (Pancake)",
        frame_size="NEMA17",
        length_mm=25,
        holding_torque_ncm=25,
        rated_current_a=1.0,
        mass_grams=180,
        shaft_diameter=5.0,
        typical_source="Prusa MK3 extruder, Orbiter kits",
        suitable_for=["E"],
        notes=[
            "Lightweight - good for direct drive",
            "Lower torque than standard",
            "Requires geared extruder (Pitan, Orbiter)",
        ],
        warnings=[
            "Reduced torque - verify with analysis tool",
            "May struggle with high-flow printing",
        ],
    ),

    "NEMA17_42x20": MotorSpec(
        id="NEMA17_42x20",
        name="NEMA17 42x20mm (Ultra-Pancake)",
        frame_size="NEMA17",
        length_mm=20,
        holding_torque_ncm=18,
        rated_current_a=0.8,
        mass_grams=140,
        shaft_diameter=5.0,
        typical_source="Purchase (LDO, Moons)",
        suitable_for=["E"],
        notes=[
            "Very lightweight for extruder",
            "Significant torque reduction",
        ],
        warnings=[
            "Low torque - PLA/PETG only recommended",
            "Run analysis to verify viability",
        ],
    ),

    # -------------------------------------------------------------------------
    # NEMA14 (smaller frame)
    # -------------------------------------------------------------------------
    "NEMA14_36x20": MotorSpec(
        id="NEMA14_36x20",
        name="NEMA14 36x20mm",
        frame_size="NEMA14",
        length_mm=20,
        holding_torque_ncm=14,
        rated_current_a=0.8,
        mass_grams=100,
        shaft_diameter=5.0,
        typical_source="Purchase (specialized)",
        suitable_for=["E"],
        notes=[
            "Smallest practical motor for extruder",
            "Requires high-ratio gearbox",
        ],
        warnings=[
            "NEMA14 with Pitan: PLA only, run analysis",
            "Limited torque - experimental configuration",
            "Consider NEMA17 pancake instead",
        ],
    ),
}


def get_motor(motor_id: str) -> Optional[MotorSpec]:
    """Get a motor specification by ID."""
    return MOTORS.get(motor_id)


def get_motor_count_for_tier(tier: int) -> int:
    """
    Get the minimum number of motors required for a tier.

    Tier 1: 4 motors (X, Y, Z-belt, E)
    Tier 2: 6 motors (X, Y, Z×3, E)
    Tier 3: 6 motors (X, Y, Z×3, E)
    """
    if tier <= 1:
        return 4
    else:
        return 6


def get_driver_count_for_tier(tier: int) -> int:
    """
    Get the minimum number of stepper drivers required for a tier.

    Same as motor count - each motor needs a driver.
    """
    return get_motor_count_for_tier(tier)


def can_motors_support_tier(motor_count: int, tier: int) -> bool:
    """Check if the available motor count supports the target tier."""
    required = get_motor_count_for_tier(tier)
    return motor_count >= required


def get_motors_from_donor(donor_type: str) -> dict:
    """Get motor information for a donor printer type."""
    return MOTOR_SOURCES.get(donor_type, {
        "name": "Unknown",
        "motor_count": 0,
        "motor_types": [],
        "notes": "Unknown donor type",
    })
