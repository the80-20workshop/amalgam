"""
Bed Registry for Amalgam

Defines common bed sizes and heating specifications.
Used by wizard to determine frame sizing and power requirements.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class BedSpec:
    """Specification for a heated bed."""

    id: str                     # Internal identifier
    name: str                   # Display name
    size_x: int                 # X dimension in mm
    size_y: int                 # Y dimension in mm

    # Heating
    heater_power: int           # Watts
    voltage: int                # 12V or 24V

    # Physical
    mass_grams: int             # Bed + heater mass
    material: str               # Aluminum, PCB, etc.

    # Sourcing
    donor_source: str           # Common donor printer, or "purchase"
    typical_price_aud: float

    # Frame implications
    notes: list[str]


# =============================================================================
# COMMON BED SIZES (quick lookup for wizard)
# =============================================================================

COMMON_BED_SIZES = {
    "ender3": (235, 235, "Ender 3 / CR-10 Mini"),
    "prusa_mk3": (250, 210, "Prusa MK3"),
    "cr10": (300, 300, "CR-10 / Ender 3 Max"),
    "ender5": (220, 220, "Ender 5"),
    "voron_v0": (120, 120, "Voron V0"),
    "custom": (0, 0, "Custom dimensions"),
}


# =============================================================================
# BED DEFINITIONS
# =============================================================================

BEDS = {
    # -------------------------------------------------------------------------
    # Donor beds (common sources)
    # -------------------------------------------------------------------------
    "ENDER3_BED": BedSpec(
        id="ENDER3_BED",
        name="Ender 3 Bed (235x235)",
        size_x=235,
        size_y=235,
        heater_power=200,
        voltage=24,
        mass_grams=800,
        material="Aluminum + PCB heater",
        donor_source="Ender 3, Ender 3 Pro, Ender 3 V2",
        typical_price_aud=0,
        notes=[
            "REFERENCE SPEC: Most common donor bed",
            "24V, 200W heater",
            "Good size/power balance",
        ],
    ),

    "PRUSA_MK3_BED": BedSpec(
        id="PRUSA_MK3_BED",
        name="Prusa MK3 Bed (250x210)",
        size_x=250,
        size_y=210,
        heater_power=180,
        voltage=24,
        mass_grams=750,
        material="PCB heater on aluminum",
        donor_source="Prusa MK3/MK3S",
        typical_price_aud=0,
        notes=[
            "Slightly larger X, smaller Y than Ender 3",
            "Excellent quality heater",
        ],
    ),

    "CR10_BED": BedSpec(
        id="CR10_BED",
        name="CR-10 Bed (300x300)",
        size_x=300,
        size_y=300,
        heater_power=350,
        voltage=24,
        mass_grams=1200,
        material="Aluminum + silicone heater",
        donor_source="CR-10, Ender 3 Max",
        typical_price_aud=0,
        notes=[
            "Large bed requires longer frame",
            "May need higher-power PSU",
            "Heavier = lower acceleration limits",
        ],
    ),

    # -------------------------------------------------------------------------
    # Purchase options
    # -------------------------------------------------------------------------
    "GENERIC_200": BedSpec(
        id="GENERIC_200",
        name="Generic 200x200 Bed",
        size_x=200,
        size_y=200,
        heater_power=150,
        voltage=24,
        mass_grams=600,
        material="Aluminum + PCB heater",
        donor_source="purchase",
        typical_price_aud=30,
        notes=[
            "Smaller bed = more rigid frame",
            "Good for learning/experimenting",
        ],
    ),

    "GENERIC_300": BedSpec(
        id="GENERIC_300",
        name="Generic 300x300 Bed",
        size_x=300,
        size_y=300,
        heater_power=300,
        voltage=24,
        mass_grams=1000,
        material="Aluminum + silicone heater",
        donor_source="purchase",
        typical_price_aud=50,
        notes=[
            "Large bed for bigger prints",
            "Requires substantial PSU (30A+)",
        ],
    ),

    "KEENOVO_235": BedSpec(
        id="KEENOVO_235",
        name="Keenovo 235x235 Silicone",
        size_x=235,
        size_y=235,
        heater_power=400,
        voltage=24,
        mass_grams=700,
        material="Cast aluminum + silicone heater",
        donor_source="purchase",
        typical_price_aud=80,
        notes=[
            "High-quality silicone heater",
            "Fast heat-up, even temperature",
            "Recommended upgrade from PCB heater",
        ],
    ),
}


def get_bed(bed_id: str) -> Optional[BedSpec]:
    """Get a bed specification by ID."""
    return BEDS.get(bed_id)


def get_bed_by_size(x: int, y: int, tolerance: int = 10) -> Optional[BedSpec]:
    """Find a bed matching the given dimensions (within tolerance)."""
    for bed in BEDS.values():
        if abs(bed.size_x - x) <= tolerance and abs(bed.size_y - y) <= tolerance:
            return bed
    return None


def get_donor_beds() -> list[BedSpec]:
    """Get beds commonly available from donor printers."""
    return [bed for bed in BEDS.values() if bed.donor_source != "purchase"]


def estimate_psu_requirement(bed: BedSpec, hotend_watts: int = 50) -> int:
    """
    Estimate PSU amperage requirement.

    Args:
        bed: Bed specification
        hotend_watts: Hotend power (typically 40-60W)

    Returns:
        Recommended PSU amperage at bed voltage
    """
    total_watts = bed.heater_power + hotend_watts + 50  # 50W for motors/electronics
    amps = total_watts / bed.voltage
    # Round up to common PSU sizes
    if amps <= 15:
        return 15
    elif amps <= 20:
        return 20
    elif amps <= 30:
        return 30
    else:
        return 40
