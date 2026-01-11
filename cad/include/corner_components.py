"""
Shared build123d components for Neo-Darwin corners

This module contains reusable components used by multiple corner types
"""

from build123d import *


def create_corner_base(corner_size):
    """Create basic corner cube for subtraction"""
    return Box(corner_size, corner_size, corner_size)


def create_m12_rod_hole(diameter, height):
    """Create M12 rod channel hole"""
    return Circle(diameter / 2)


def create_nema17_motor_mount(
    mount_depth, plate_width=42.0, plate_height=42.0, bolt_spacing=31.0
):
    """
    Create NEMA17 motor mount plate with bolt holes

    Args:
        mount_depth: Depth of mount from rod center
        plate_width: Width of mounting plate (default 42mm)
        plate_height: Height of mounting plate (default 42mm)
        bolt_spacing: Distance between bolt holes (default 31mm NEMA17)

    Returns:
        build123d Part object for motor mount
    """
    motor_plate = Rectangle(plate_width, plate_height)

    # NEMA17 bolt holes (4 corners)
    bolt_pattern = [
        (-bolt_spacing / 2, bolt_spacing / 2),
        (bolt_spacing / 2, bolt_spacing / 2),
        (bolt_spacing / 2, -bolt_spacing / 2),
        (bolt_spacing / 2, -bolt_spacing / 2),
    ]

    motor_mount = extrude(motor_plate, amount=mount_depth)

    # Add bolt holes
    for bolt_x, bolt_y in bolt_pattern:
        with BuildSketch(motor_mount.faces(">X")):
            Location((bolt_x, bolt_y, 0)).circle(3.0).extrude(amount=10)

    return motor_mount


def create_rod_clamp(rod_diameter, wall_thickness=5.0, clamp_length=40.0):
    """
    Create M12 rod clamp component

    Args:
        rod_diameter: Diameter of rod to clamp
        wall_thickness: Wall thickness of clamp
        clamp_length: Length of clamp along rod

    Returns:
        build123d Part object for rod clamp
    """
    # Clamp body
    outer_dia = rod_diameter + (wall_thickness * 2)
    clamp = Box(outer_dia, outer_dia, clamp_length)

    # Rod hole
    rod_hole = Cylinder(rod_diameter / 2, clamp_length)

    return clamp - rod_hole


def create_jam_nut_access(diameter=20.0, wall_thickness=5.0):
    """
    Create jam nut access hole

    Args:
        diameter: Access hole diameter
        wall_thickness: Wall thickness

    Returns:
        build123d Part object for jam nut access
    """
    return Circle(diameter / 2)


def make_motorized_corner(
    location="front_left",
    mirror=False,
    m12_fit_dia=12.5,
    wall_thickness=5.0,
    motor_bolt_spacing=31.0,
    motor_mount_depth=25.0,
    leadscrew_clearance=15.0,
    cable_channel_depth=6.0,
    cable_channel_width=12.0,
    motor_plate_width=42.0,
    motor_plate_height=42.0,
):
    """
    Generate motorized corner with shared components

    Args:
        location: "front_left", "front_right", "back_left", "back_right"
        mirror: Flip X axis (for mirrored corners)
        m12_fit_dia: M12 rod diameter with lumpy factor
        wall_thickness: Wall thickness
        motor_bolt_spacing: NEMA17 bolt spacing (31mm)
        motor_mount_depth: Depth of motor mount
        leadscrew_clearance: Clearance for leadscrew path
        cable_channel_depth: Depth of cable routing channel
        cable_channel_width: Width of cable routing channel
        motor_plate_width: Motor mounting plate width
        motor_plate_height: Motor mounting plate height

    Returns:
        build123d Part object for corner
    """
