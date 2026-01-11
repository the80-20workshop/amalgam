"""
Neo-Darwin Motorized Corner (Front-Left or Front-Right)

Single Python file for both front motorized corners using CLI parameter
Usage: python corner_motorized.py [LOCATION] [ORIENTATION]
  LOCATION: front_left or front_right
  ORIENTATION: default (as designed) or mirror (flip X axis)
"""

import sys

sys.path.insert(0, "..")

# --- IMPORTS ---
try:
    from build123d import *

    BUILD123D_AVAILABLE = True
except ImportError:
    BUILD123D_AVAILABLE = False
    print("Error: build123d not available. Run: pip install build123d")

from config import *


# --- HELPER FUNCTION FOR EXPORTING STL ---
def export_stl(part, filename):
    """Export part to STL file"""
    try:
        from build123d import export_stl as export_stl_func

        export_stl_func(part, filename)
        print(f"Exported: {filename}")
    except ImportError:
        print(f"Warning: export_stl not available, skipping file export")


# --- PARAMETERS FROM CONFIG ---
m12_fit_dia = M12_FIT_DIA
wall_thickness = 5.0
motor_bolt_spacing = 31.0
motor_mount_depth = 25.0
leadscrew_clearance = 15.0
cable_channel_depth = 6.0
cable_channel_width = 12.0
motor_plate_width = 42.0
motor_plate_height = 42.0

# --- CALCULATED DIMENSIONS ---
corner_size = m12_fit_dia + (wall_thickness * 2)
jam_nut_dia = 20.0
jam_nut_offset = wall_thickness / 2
leadscrew_path_dia = 10.0


def make_motorized_corner(location="front_left", mirror=False):
    """
    Generate motorized corner with optional mirroring

    Args:
        location: "front_left" or "front_right"
        mirror: False (default) or True (flip X axis)

    Returns:
        build123d Part object for corner
    """

    # Determine motor position based on location
    if location == "front_left":
        motor_x_offset = corner_size / 2
        print(f"Location: {location}")
        print(f"Motor: Z1 integrated")
    elif location == "front_right":
        motor_x_offset = corner_size / 2
        print(f"Location: {location}")
        print(f"Motor: Z2 integrated")
    else:
        print(f"Error: Invalid location '{location}'")
        print("Use: front_left or front_right")
        return None

    # Apply mirror transformation if requested
    if mirror:
        print("Orientation: Mirrored (X-axis flip)")
    else:
        print("Orientation: Default (no mirror)")

    # --- BUILD THE PART ---
    with BuildPart() as corner:
        # 1. Create corner base block
        corner_base = Box(corner_size, corner_size, corner_size)

        # 2. Create M12 vertical rod channel (Front-Left or Front-Right)
        with BuildSketch(corner_base.faces(">Z")):
            Circle(m12_fit_dia / 2).extrude(amount=corner_size)

        # 3. Create M12 vertical rod channel (Front-Center)
        with BuildSketch(corner_base.faces(">Z")):
            Location((corner_size * 0.3, corner_size * 0.3, 0)).circle(
                m12_fit_dia / 2
            ).extrude(amount=corner_size * 0.4)

        # 4. Create M12 horizontal rod channel (Front-Left or Front-Right)
        with BuildSketch(corner_base.faces(">Y")):
            Location((0, m12_fit_dia / 2, 0)).circle(m12_fit_dia / 2).extrude(
                amount=corner_size
            )

        # 5. Create leadscrew vertical path clearance
        leadscrew_path_dia = 10.0
        with BuildSketch(corner_base.faces(">X")):
            Location(
                (motor_mount_depth + leadscrew_clearance, corner_size / 2, 0)
            ).circle(leadscrew_path_dia / 2).extrude(amount=wall_thickness * 2)

        # 6. Create motor mount plate (Z1 or Z2)
        with BuildSketch(corner_base.faces(">X")):
            motor_face = Rectangle(motor_plate_width, motor_plate_height)
            motor_face = extrude(motor_face, amount=motor_mount_depth)

            # NEMA17 motor bolt holes (4 corners of face)
            bolt_pattern = [
                (-motor_bolt_spacing / 2, motor_bolt_spacing / 2),
                (motor_bolt_spacing / 2, motor_bolt_spacing / 2),
                (motor_bolt_spacing / 2, -motor_bolt_spacing / 2),
                (motor_bolt_spacing / 2, -motor_bolt_spacing / 2),
            ]

            for bolt_x, bolt_y in bolt_pattern:
                with BuildSketch(motor_face.faces(">X")):
                    Location((bolt_x, bolt_y, 0)).circle(3.0).extrude(
                        amount=wall_thickness
                    )

        # 7. Create cable routing channels
        with BuildSketch(corner_base.faces(">Z")):
            channel_rect = Rectangle(cable_channel_width, cable_channel_height)
            channel_rect = extrude(channel_rect, amount=motor_mount_depth)

        # 8. Create jam nut access holes (2 per rod clamp)
        with BuildSketch(corner_base.faces(">X")):
            Location(
                (
                    corner_size / 2,
                    m12_fit_dia + wall_thickness / 2 + jam_nut_offset,
                    wall_thickness / 2,
                )
            ).circle(jam_nut_dia / 2).extrude(amount=wall_thickness)

        with BuildSketch(corner_base.faces(">Y")):
            Location(
                (wall_thickness / 2 + jam_nut_offset, corner_size / 2, corner_size / 2)
            ).circle(jam_nut_dia / 2).extrude(amount=wall_thickness)

        # 9. Add fillets (rounded edges for strength)
        edges_to_fillet = [
            corner_base.edges("|X and >Y"),
            corner_base.edges("|Y and >Z"),
            corner_base.edges("|Z and >X"),
        ]
        fillet(edges_to_fillet, radius=3.0)

        # 10. Label
        corner.label = f"Corner-{location.upper()}-Zmotorized"

        # Position for label placement
        corner.label_location = (-corner_size / 2, -corner_size / 2, corner_size)

    return corner


def main():
    # Parse command line arguments
    location = "front_left"
    mirror = False

    for arg in sys.argv[1:]:
        if arg.lower() == "front_left":
            location = "front_left"
        elif arg.lower() == "front_right":
            location = "front_right"
        elif arg.lower() == "mirror":
            mirror = True
        elif arg.lower() in ["-h", "--help"]:
            print("Usage: python corner_motorized.py [LOCATION] [ORIENTATION]")
            print("")
            print("Arguments:")
            print("  LOCATION    front_left or front_right")
            print("  ORIENTATION  mirror (optional)")
            print("")
            print("Examples:")
            print("  python corner_motorized.py front_left")
            print("  python corner_motorized.py front_right")
            print("  python corner_motorized.py front_left mirror")
            return
        else:
            print(f"Unknown argument: {arg}")
            print("Use -h for help")
            return

    print(f"Generating motorized corner: {location}")
    print(f"Mirror: {mirror}")

    corner = make_motorized_corner(location, mirror)

    if corner is None:
        return

    stl_name = f"corner_{location}.stl"
    export_stl(corner, stl_name)

    print(f"M12 rod diameter: {m12_fit_dia}mm")
    print(f"Motor: NEMA17 (Z1 or Z2 based on location)")
    print(f"Bolt spacing: {motor_bolt_spacing}mm (standard)")
    print(f"Export: {stl_name}")
    print("Corner complete!")

    return corner


if __name__ == "__main__":
    main()
