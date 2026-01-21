from build123d import *
from ocp_vscode import show

SCALE = 1.0

TIRE_RADIUS = 12 * SCALE
TIRE_WIDTH = 10 * SCALE
TREAD_DEPTH = 2.5 * SCALE
TREAD_WIDTH = 5 * SCALE
TREAD_SPACING = 8 * SCALE
TREAD_COUNT = 6
SIDE_TREAD_COUNT = 4

RIM_RADIUS = 5 * SCALE
RIM_WIDTH = 6 * SCALE


def make_tread_block():
    with BuildSketch(Plane.YZ) as s:
        # Create a knobby tread shape with rounded top
        with Locations((0, TREAD_DEPTH / 2)):
            Circle(TREAD_WIDTH / 2)
        # Square off the bottom
        Rectangle(TREAD_WIDTH, TREAD_DEPTH, align=(Align.CENTER, Align.MIN))
    tread = extrude(s.sketch, amount=TIRE_WIDTH, both=True)

    # Add chamfer to outer circular edge for realistic tire appearance
    with BuildPart() as chamfered:
        add(tread)
        # Chamfer the outer circular edges only
        outer_edges = chamfered.edges().group_by(Axis.X)[-1]  # Outer circular edges
        chamfer(outer_edges, length=0.5 * SCALE)

    return chamfered.part


def make_side_tread():
    with BuildSketch(Plane.YZ) as s:
        Rectangle(3 * SCALE, TREAD_DEPTH * 0.8, align=(Align.CENTER, Align.CENTER))
    tread = extrude(s.sketch, amount=2 * SCALE)
    return tread


def make_tire():
    major_radius = RIM_RADIUS + TIRE_RADIUS  # Distance from center to tire center

    with BuildPart() as tire:
        # Main tire body - revolve around Z axis creates proper wheel shape
        with BuildSketch(Plane.XY) as sketch:
            with Locations((0, major_radius)):
                Circle(TIRE_RADIUS)
            with Locations((0, major_radius)):
                Circle(RIM_RADIUS, mode=Mode.SUBTRACT)
        revolve(sketch.sketch, axis=Axis.Z, revolution_arc=360)

        # Add center treads on OUTER surface (at Y = major_radius + TIRE_RADIUS)
        outer_radius = major_radius + TIRE_RADIUS
        inner_radius = major_radius + RIM_RADIUS

        for i in range(TREAD_COUNT):
            angle = i * (360 / TREAD_COUNT)
            tread = make_tread_block()
            tread = tread.rotate(Axis.Z, angle)
            tread = tread.moved(Location((0, outer_radius, 0)))
            add(tread, mode=Mode.ADD)

        # Add smaller side treads between main treads for realism
        for i in range(SIDE_TREAD_COUNT):
            angle = i * (360 / SIDE_TREAD_COUNT) + (180 / SIDE_TREAD_COUNT)
            tread = make_side_tread()
            tread = tread.rotate(Axis.Z, angle)
            tread = tread.moved(Location((0, major_radius + 0.6 * TIRE_RADIUS, 0)))
            add(tread, mode=Mode.ADD)

    return tire


def make_wheel_assembly():
    tire = make_tire()

    # Add inner rim - positioned at center (where donut hole would be)
    with BuildPart() as rim:
        Cylinder(
            RIM_RADIUS, RIM_WIDTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)
        )

    rim_part = rim.part

    # Combine
    wheel = tire.part + rim_part

    return wheel


wheel = make_wheel_assembly()
show(wheel)
