"""
Extruder Registry for Amalgam

Defines supported extruder types with their mechanical and performance properties.
Critical for engineering analysis (rod sag, acceleration limits).
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ExtruderSpec:
    """Specification for an extruder type."""

    id: str                     # Internal identifier
    name: str                   # Display name
    drive_type: str             # "single" or "dual"
    gear_ratio: str             # e.g., "3:1", "7.5:1", "direct"

    # Physical properties (critical for analysis)
    mass_grams: int             # Total toolhead mass with motor
    motor_type: str             # "NEMA17", "NEMA14", "pancake"

    # Performance characteristics
    max_flow_mm3s: float        # Approximate max volumetric flow
    filament_support: list[str] # Supported filament types

    # Sourcing
    printable: bool             # Can be 3D printed
    typical_price_aud: float    # Approximate cost (excluding motor)

    # Documentation
    docs_folder: str            # Folder name in docs/extruders/
    stl_folder: str             # Folder in cad/parts/ for STLs

    # Compatibility notes
    notes: list[str]
    warnings: list[str]         # Conditions that trigger warnings

    # Rod compatibility (for analysis warnings)
    min_rod_diameter: int       # Minimum recommended smooth rod (mm)


# =============================================================================
# EXTRUDER DEFINITIONS
# =============================================================================

EXTRUDERS = {
    # -------------------------------------------------------------------------
    # Reference Spec
    # -------------------------------------------------------------------------
    "PITAN": ExtruderSpec(
        id="PITAN",
        name="Pitan (Printable Titan)",
        drive_type="single",
        gear_ratio="3:1",
        mass_grams=280,
        motor_type="NEMA17",
        max_flow_mm3s=12.0,
        filament_support=["PLA", "PETG", "ABS", "TPU"],
        printable=True,
        typical_price_aud=8,  # Bearings + hardware only
        docs_folder="pitan",
        stl_folder="extruder/pitan",
        notes=[
            "REFERENCE SPEC: Single-drive, no gear mesh artifacts",
            "Uses standard NEMA17 from donor printer",
            "3:1 reduction provides excellent torque",
            "Open-source design, easy to modify",
        ],
        warnings=[
            "NEMA14 motor reduces torque - PLA/PETG only",
            "Pancake NEMA17 works but less torque headroom",
        ],
        min_rod_diameter=8,
    ),

    # -------------------------------------------------------------------------
    # Alternatives
    # -------------------------------------------------------------------------
    "WADE": ExtruderSpec(
        id="WADE",
        name="Greg's Wade Extruder",
        drive_type="single",
        gear_ratio="39:11",  # ~3.5:1
        mass_grams=450,
        motor_type="NEMA17",
        max_flow_mm3s=10.0,
        filament_support=["PLA", "PETG", "ABS"],
        printable=True,
        typical_price_aud=5,
        docs_folder="wade",
        stl_folder="extruder/wade",
        notes=[
            "Classic RepRap design, proven reliable",
            "Heavier than modern alternatives",
            "Large gear provides high torque",
        ],
        warnings=[
            "Heavy mass (450g) limits acceleration",
            "Recommend M10+ rods with Wade",
        ],
        min_rod_diameter=10,
    ),

    "ORBITER_V2": ExtruderSpec(
        id="ORBITER_V2",
        name="Orbiter V2",
        drive_type="dual",
        gear_ratio="7.5:1",
        mass_grams=140,  # With pancake motor
        motor_type="pancake",
        max_flow_mm3s=15.0,
        filament_support=["PLA", "PETG", "ABS", "TPU", "PA"],
        printable=False,
        typical_price_aud=90,
        docs_folder="orbiter",
        stl_folder="extruder/orbiter",
        notes=[
            "Lightweight, high-performance option",
            "Dual-drive with planetary gears",
            "Requires purchase (not printable)",
        ],
        warnings=[
            "Expensive for Amalgam philosophy",
            "Dual-drive may show gear mesh artifacts",
        ],
        min_rod_diameter=8,
    ),

    "MK8": ExtruderSpec(
        id="MK8",
        name="MK8 Direct Drive",
        drive_type="single",
        gear_ratio="direct",
        mass_grams=180,
        motor_type="NEMA17",
        max_flow_mm3s=8.0,
        filament_support=["PLA", "PETG"],
        printable=False,
        typical_price_aud=15,
        docs_folder="mk8",
        stl_folder="extruder/mk8",
        notes=[
            "Simple, cheap, direct-drive",
            "Common in budget printers",
            "Lower flow rate than geared options",
        ],
        warnings=[
            "Direct drive = low torque at motor",
            "May struggle with harder filaments",
        ],
        min_rod_diameter=8,
    ),

    "BMG": ExtruderSpec(
        id="BMG",
        name="BMG Clone",
        drive_type="dual",
        gear_ratio="3:1",
        mass_grams=200,
        motor_type="NEMA17",
        max_flow_mm3s=14.0,
        filament_support=["PLA", "PETG", "ABS", "TPU", "PA"],
        printable=False,
        typical_price_aud=25,
        docs_folder="bmg",
        stl_folder="extruder/bmg",
        notes=[
            "Popular dual-drive, widely cloned",
            "Good balance of weight and performance",
        ],
        warnings=[
            "Dual-drive = potential gear mesh artifacts",
            "Clone quality varies significantly",
        ],
        min_rod_diameter=8,
    ),
}


def get_extruder(extruder_id: str) -> Optional[ExtruderSpec]:
    """Get an extruder specification by ID."""
    return EXTRUDERS.get(extruder_id)


def get_extruder_mass(extruder_id: str) -> int:
    """Get extruder mass in grams. Returns 280 (Pitan) if not found."""
    ext = EXTRUDERS.get(extruder_id)
    return ext.mass_grams if ext else 280


def get_printable_extruders() -> list[ExtruderSpec]:
    """Get extruders that can be 3D printed."""
    return [ext for ext in EXTRUDERS.values() if ext.printable]


def get_extruders_for_rod(rod_diameter: float) -> list[ExtruderSpec]:
    """Get extruders compatible with a given rod diameter."""
    return [
        ext for ext in EXTRUDERS.values()
        if ext.min_rod_diameter <= rod_diameter
    ]
