from build123d import *
from ocp_vscode import show

SCALE = 1.0

BODY_LENGTH = 70 * SCALE
BODY_WIDTH = 35 * SCALE
BODY_HEIGHT = 15 * SCALE

CAB_LENGTH = 25 * SCALE
CAB_WIDTH = 30 * SCALE
CAB_HEIGHT = 20 * SCALE

WHEEL_RADIUS = 10 * SCALE
WHEEL_WIDTH = 8 * SCALE

EXHAUST_RADIUS = 1.5 * SCALE
EXHAUST_HEIGHT = 30 * SCALE

HOOD_DEPTH = 20 * SCALE
HOOD_SLOPE_HEIGHT = 12 * SCALE

TREAD_COUNT = 4
TREAD_DEPTH = 1.0 * SCALE

HITCH_WIDTH = 6 * SCALE
HITCH_HEIGHT = 8 * SCALE
HITCH_DEPTH = 12 * SCALE

GRILLE_WIDTH = 1.5 * SCALE
GRILLE_HEIGHT = 12 * SCALE
GRILLE_SPACING = 3 * SCALE


def make_body():
    with BuildPart() as body:
        Box(
            BODY_LENGTH,
            BODY_WIDTH,
            BODY_HEIGHT,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
    return body


def make_hood_slope():
    sloped_part = Solid.make_box(HOOD_DEPTH, BODY_WIDTH, HOOD_SLOPE_HEIGHT)
    sloped_part = sloped_part.rotate(Axis.Y, -45)
    sloped_part = sloped_part.moved(
        Location((BODY_LENGTH / 2 - HOOD_DEPTH / 2, 0, BODY_HEIGHT))
    )
    return sloped_part


def make_cab():
    with BuildPart() as cab:
        Box(
            CAB_LENGTH,
            CAB_WIDTH,
            CAB_HEIGHT,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        # Front window
        with BuildSketch(Plane.XY.offset(BODY_HEIGHT + CAB_HEIGHT - 5)) as s:
            Rectangle(CAB_LENGTH - 8, CAB_HEIGHT - 8)
        cut = extrude(s.sketch, amount=-5)
        add(cut, mode=Mode.SUBTRACT)
        # Side windows
        with BuildSketch(Plane.YZ.offset(CAB_LENGTH / 2 - 5)) as s:
            Rectangle(CAB_WIDTH - 6, CAB_HEIGHT - 6)
        cut = extrude(s.sketch, amount=5)
        add(cut, mode=Mode.SUBTRACT)
        with BuildSketch(Plane.YZ.offset(-CAB_LENGTH / 2 + 5)) as s:
            Rectangle(CAB_WIDTH - 6, CAB_HEIGHT - 6)
        cut = extrude(s.sketch, amount=-5)
        add(cut, mode=Mode.SUBTRACT)
    return cab


def make_wheel():
    with BuildPart() as wheel:
        Cylinder(
            WHEEL_RADIUS, WHEEL_WIDTH, align=(Align.CENTER, Align.CENTER, Align.MIN)
        )
    wheel = wheel.part.rotate(Axis.X, 90)

    for i in range(TREAD_COUNT):
        tread_radius = WHEEL_RADIUS - (i + 1) * (WHEEL_RADIUS - TREAD_DEPTH) / (
            TREAD_COUNT + 1
        )
        with BuildSketch(Plane.YZ) as s:
            Circle(tread_radius)
        tread = extrude(s.sketch, amount=WHEEL_WIDTH + TREAD_DEPTH * 2)
        tread = tread.moved(Location((WHEEL_WIDTH / 2, 0, 0)))
        wheel += tread

    return wheel


def make_exhaust():
    with BuildPart() as exhaust:
        Cylinder(
            EXHAUST_RADIUS,
            EXHAUST_HEIGHT,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
    return exhaust


def make_grille():
    with BuildPart() as grille:
        slot_count = 5
        for i in range(slot_count):
            offset_y = (i - slot_count / 2) * GRILLE_SPACING
            with BuildSketch(Plane.YZ.offset(BODY_LENGTH / 2 + 1)) as s:
                Rectangle(GRILLE_WIDTH, GRILLE_HEIGHT)
                offset((0, offset_y, BODY_HEIGHT / 2))
            cut = extrude(s.sketch, amount=3)
            add(cut, mode=Mode.SUBTRACT)
    return grille


def make_hitch():
    with BuildPart() as hitch:
        Box(
            HITCH_WIDTH,
            HITCH_DEPTH,
            HITCH_HEIGHT,
            align=(Align.CENTER, Align.MIN, Align.CENTER),
        )
        # Pin
        Cylinder(
            1.0 * SCALE, 4 * SCALE, align=(Align.CENTER, Align.CENTER, Align.CENTER)
        )
    return hitch


with BuildPart() as tractor:
    body = make_body()
    add(body.part)

    hood = make_hood_slope()
    add(hood, mode=Mode.SUBTRACT)

    cab_x = -BODY_LENGTH / 4
    cab = make_cab()
    add(cab.part.moved(Location((cab_x, 0, BODY_HEIGHT))))

    wheel_positions = [
        (BODY_LENGTH / 2 - WHEEL_RADIUS, BODY_WIDTH / 2 + WHEEL_WIDTH / 2),
        (BODY_LENGTH / 2 - WHEEL_RADIUS, -BODY_WIDTH / 2 - WHEEL_WIDTH / 2),
        (-BODY_LENGTH / 2 + WHEEL_RADIUS, BODY_WIDTH / 2 + WHEEL_WIDTH / 2),
        (-BODY_LENGTH / 2 + WHEEL_RADIUS, -BODY_WIDTH / 2 - WHEEL_WIDTH / 2),
    ]

    for x, y in wheel_positions:
        wheel = make_wheel()
        add(wheel.moved(Location((x, y, WHEEL_RADIUS))))

    exhaust_x = BODY_LENGTH / 2 - 15 * SCALE
    exhaust_y = -BODY_WIDTH / 2 - 3 * SCALE
    exhaust = make_exhaust()
    add(exhaust.part.moved(Location((exhaust_x, exhaust_y, BODY_HEIGHT))))

    hitch_x = -BODY_LENGTH / 2 - HITCH_DEPTH / 2
    hitch = make_hitch()
    add(hitch.part.moved(Location((hitch_x, 0, HITCH_HEIGHT / 2))))

show(tractor)
