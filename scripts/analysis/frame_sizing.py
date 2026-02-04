"""
Frame Sizing Calculator for Amalgam

Calculates required frame dimensions based on bed size and
component clearances. Helps builders understand the relationship
between heat bed size and frame requirements.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FrameSizeResult:
    """Result of frame size calculation."""

    bed_x: float  # mm
    bed_y: float  # mm
    build_z: float  # mm

    # Calculated frame dimensions
    frame_x: float  # mm (internal)
    frame_y: float  # mm (internal)
    frame_z: float  # mm (internal)

    # Rod lengths needed
    rod_x_length: float  # mm
    rod_y_length: float  # mm
    rod_z_length: float  # mm

    # Smooth rod spans
    x_span: float  # mm (unsupported span for X gantry)
    y_span: float  # mm (unsupported span for Y rods)

    notes: list[str]


# Standard clearances (mm)
CLEARANCES = {
    # X-axis clearances
    "x_motor": 60,  # Space for X motor
    "x_endstop": 20,  # Space for X endstop
    "x_belt_path": 40,  # Belt tensioner and routing
    "x_extruder_overhang": 35,  # Pitan extruder overhang (50 for Wade)

    # Y-axis clearances
    "y_motor": 60,  # Space for Y motor
    "y_carriage": 50,  # Y carriage travel beyond bed
    "y_belt_path": 40,  # Belt tensioner and routing

    # Z-axis clearances
    "z_motor_coupler": 70,  # Z motor + coupler height
    "z_top_bracket": 50,  # Top bracket clearance
    "z_bed_clearance": 25,  # Bed to bottom frame

    # Frame corner overhead
    "corner_size": 50,  # Size of printed corner brackets
}


def calculate_frame_size(
    bed_x: float,
    bed_y: float,
    build_z: float,
    extruder_type: str = "PITAN",
    triple_z: bool = True,
) -> FrameSizeResult:
    """
    Calculate required frame dimensions from bed size.

    Args:
        bed_x: Heated bed X dimension in mm (e.g., 235)
        bed_y: Heated bed Y dimension in mm (e.g., 235)
        build_z: Desired Z build height in mm (e.g., 250)
        extruder_type: Extruder type for overhang calculation
        triple_z: Whether using Triple-Z (affects Z motor placement)

    Returns:
        FrameSizeResult with all calculated dimensions
    """
    notes = []

    # Extruder overhang based on type
    extruder_overhangs = {
        "PITAN": 35,
        "WADE": 50,
        "MK8": 25,
        "SHERPA": 25,
    }
    x_overhang = extruder_overhangs.get(extruder_type.upper(), 35)

    # Calculate internal frame dimensions
    frame_x = (
        bed_x
        + CLEARANCES["x_motor"]
        + CLEARANCES["x_endstop"]
        + x_overhang
    )

    frame_y = (
        bed_y
        + CLEARANCES["y_motor"]
        + CLEARANCES["y_carriage"]
    )

    frame_z = (
        build_z
        + CLEARANCES["z_motor_coupler"]
        + CLEARANCES["z_top_bracket"]
    )

    # Calculate rod lengths (add corner size for overlap)
    rod_x_length = frame_x + CLEARANCES["corner_size"]
    rod_y_length = frame_y + CLEARANCES["corner_size"]
    rod_z_length = frame_z + CLEARANCES["corner_size"]

    # Calculate smooth rod spans
    # X span is roughly bed width + motor clearance
    x_span = bed_x + CLEARANCES["x_motor"]

    # Y span is bed depth + carriage travel
    y_span = bed_y + CLEARANCES["y_carriage"]

    # Add notes about the configuration
    if extruder_type.upper() == "WADE":
        notes.append("Wade extruder requires larger X overhang (50mm)")

    if triple_z:
        notes.append("Triple-Z: Z motors at front corners + back center")
    else:
        notes.append("Belted-Z: Single motor, belt drives all Z points")

    # Standard rod length recommendations
    if rod_x_length <= 500 and rod_y_length <= 500 and rod_z_length <= 500:
        notes.append("All rods can be cut from 1m stock (cut in half)")
    else:
        notes.append("Some rods require longer stock than 500mm")

    # Span warnings
    if x_span > 300:
        notes.append(f"WARNING: X span ({x_span}mm) is long - consider M10 rods")
    if y_span > 350:
        notes.append(f"WARNING: Y span ({y_span}mm) is long - verify rod stiffness")

    return FrameSizeResult(
        bed_x=bed_x,
        bed_y=bed_y,
        build_z=build_z,
        frame_x=frame_x,
        frame_y=frame_y,
        frame_z=frame_z,
        rod_x_length=rod_x_length,
        rod_y_length=rod_y_length,
        rod_z_length=rod_z_length,
        x_span=x_span,
        y_span=y_span,
        notes=notes,
    )


# Common bed sizes
COMMON_BEDS = {
    "ender3": (235, 235, "Ender 3 / CR-10 Mini"),
    "prusa_mk3": (250, 210, "Prusa MK3/MK3S"),
    "mk3_dual": (200, 200, "MK3 Dual (recommended for M8 rods)"),
    "ender5": (220, 220, "Ender 5"),
    "voron_v0": (120, 120, "Voron V0"),
    "custom_300": (300, 300, "Large custom"),
}


def suggest_bed_for_rods(
    rod_diameter: float,
    max_acceptable_sag: float = 0.035,
) -> list[tuple[str, float, float, str]]:
    """
    Suggest appropriate bed sizes for a given rod diameter.

    Args:
        rod_diameter: Smooth rod diameter in mm
        max_acceptable_sag: Maximum acceptable deflection in mm

    Returns:
        List of (bed_name, x, y, description) tuples that work with this rod
    """
    from .rod_sag import calculate_rod_sag, get_extruder_mass

    suitable = []
    pitan_mass = get_extruder_mass("PITAN")

    for name, (x, y, desc) in COMMON_BEDS.items():
        # Calculate frame size to get span
        frame = calculate_frame_size(x, y, 250)

        # Check rod sag at this span
        sag = calculate_rod_sag(rod_diameter, frame.x_span, pitan_mass)

        if sag.deflection <= max_acceptable_sag:
            suitable.append((name, x, y, desc))

    return suitable


if __name__ == "__main__":
    # Example usage
    print("Frame Sizing Example")
    print("=" * 50)

    # Calculate for Ender 3 bed with Pitan
    result = calculate_frame_size(
        bed_x=235,
        bed_y=235,
        build_z=250,
        extruder_type="PITAN",
        triple_z=True,
    )

    print(f"\nBed size: {result.bed_x} x {result.bed_y} mm")
    print(f"Build height: {result.build_z} mm")
    print(f"\nFrame dimensions (internal):")
    print(f"  X: {result.frame_x} mm")
    print(f"  Y: {result.frame_y} mm")
    print(f"  Z: {result.frame_z} mm")
    print(f"\nRod lengths needed:")
    print(f"  X rods: {result.rod_x_length} mm")
    print(f"  Y rods: {result.rod_y_length} mm")
    print(f"  Z rods: {result.rod_z_length} mm")
    print(f"\nSmooth rod spans:")
    print(f"  X span: {result.x_span} mm")
    print(f"  Y span: {result.y_span} mm")
    print(f"\nNotes:")
    for note in result.notes:
        print(f"  - {note}")
