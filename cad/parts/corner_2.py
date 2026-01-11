"""
Neo-Darwin Corner 2: Front-Right with Integrated Z2 Motor Mount

Mirror of Corner 1 - Front-Right corner with Z2 motor integrated
into corner bracket design.

Location: Front-Right corner
Z-Motor: Z2 (integrated)
Rod Clamps: Vertical Front-Right, Vertical Front-Center-Right, Horizontal Front-Right
"""

from build123d import *


def make_corner_front_right_z2():
    """
    Generate Front-Right corner with integrated Z2 motor mount

    Frame connections:
    - Vertical rod: Front-Right (VFR)
    - Vertical rod: Front-Center-Right (FCR)
    - Horizontal rod: Front-Right (FR)

    Features:
    - Integrated NEMA17 Z2 motor mount
    - M12 rod clamps (2 vertical + 1 horizontal)
    - Leadscrew vertical path clearance
    - Jam nut access points (2 per rod)
    - Cable routing channels for Z-motor

    Returns:
        build123d Part object for corner
    """

    # --- PARAMETERS FROM CONFIG ---
    m12_fit_dia = M12_FIT_DIA
    wall_thickness = 5.0
    motor_bolt_spacing = 31.0
    motor_mount_depth = 25.0
    leadscrew_clearance = 15.0
    cable_channel_depth = 6.0
    cable_channel_width = 12.0

    # --- BUILD THE PART ---
    with BuildPart() as corner:
        # 1. Create corner base block
        corner_size = m12_fit_dia + (wall_thickness * 2)

        corner_base = Box(corner_size, corner_size, corner_size)

        # 2. Create M12 vertical rod channel (Front-Right)
        with BuildSketch(corner_base.faces(">Z")):
            Circle(m12_fit_dia / 2).extrude(amount=corner_size)

        # 3. Create M12 vertical rod channel (Front-Center-Right)
        with BuildSketch(corner_base.faces(">Z")):
            Location((corner_size * 0.7, corner_size * 0.3, 0)).circle(
                m12_fit_dia / 2
            ).extrude(amount=corner_size * 0.4)

        # 4. Create M12 horizontal rod channel (Front-Right)
        with BuildSketch(corner_base.faces(">Y")):
            Location((-corner_size, m12_fit_dia / 2, 0)).circle(
                m12_fit_dia / 2
            ).extrude(amount=corner_size)

        # 5. Create leadscrew vertical path clearance
        leadscrew_path_dia = 10.0
        with BuildSketch(corner_base.faces(">X")):
            Location(
                (
                    corner_size - motor_mount_depth - leadscrew_clearance,
                    corner_size / 2,
                    0,
                )
            ).circle(leadscrew_path_dia / 2).extrude(amount=wall_thickness * 2)

        # 6. Create motor mount plate (Z2)
        with BuildSketch(corner_base.faces(">X")):
            motor_face = Rectangle(motor_plate_width, motor_plate_height)
            motor_face = extrude(motor_face, amount=motor_mount_depth)

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
            channel_rect = extrude(channel_rect, amount=motor_plate_depth)

        # 8. Create jam nut access holes
        jam_nut_dia = 20.0
        jam_nut_offset = wall_thickness / 2

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

        # 9. Add fillets
        edges_to_fillet = [
            corner_base.edges("|X and >Y"),
            corner_base.edges("|Y and >Z"),
            corner_base.edges("|Z and >X"),
        ]
        fillet(edges_to_fillet, radius=3.0)

        # 10. Label
        corner.label = "Corner-2-FrontRight-Z2"
        corner.label_location = (corner_size / 2, -corner_size / 2, corner_size)

    return corner


def main():
    print("Generating Corner 2: Front-Right with integrated Z2 motor mount...")

    corner_2 = make_corner_front_right_z2()

    export_stl(corner_2, "corner_2_front_right_z2.stl")

    print(f"  M12 rod diameter: {M12_FIT_DIA}mm")
    print(f"  Motor: NEMA17 (Z2)")
    print(f"  Mirror of Corner 1")
    print(f"  Export: corner_2_front_right_z2.stl")
    print("Corner 2 complete!")

    return corner_2


if __name__ == "__main__":
    main()
