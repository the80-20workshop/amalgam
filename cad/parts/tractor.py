from build123d import *
from ocp_vscode import show

# =========================================================
# Configuration
# =========================================================

SCALE = 1.0

BODY_LENGTH = 60 * SCALE
BODY_WIDTH = 32 * SCALE
BODY_HEIGHT = 18 * SCALE

CAB_LENGTH = 22 * SCALE
CAB_WIDTH = 28 * SCALE
CAB_HEIGHT = 22 * SCALE

WHEEL_RADIUS = 9 * SCALE
WHEEL_WIDTH = 6 * SCALE

EXHAUST_RADIUS = 1.2 * SCALE
EXHAUST_HEIGHT = 25 * SCALE

GRILLE_SLOT_WIDTH = 1.0 * SCALE
GRILLE_SLOT_HEIGHT = 14 * SCALE
GRILLE_SLOT_SPACING = 2.2 * SCALE

FILLET_RADIUS = 1.0 * SCALE  # safe radius


# =========================================================
# Feature Functions
# =========================================================


def make_body():
    """Create the main tractor body with fillets."""
    b = Box(
        BODY_LENGTH,
        BODY_WIDTH,
        BODY_HEIGHT,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )
    fillet(b.edges(), radius=FILLET_RADIUS)


def cut_hood_slope():
    """Cut a sloped hood for overhang calibration."""
    with BuildSketch(
        Plane(origin=(BODY_LENGTH / 2 - 10 * SCALE, 0, BODY_HEIGHT), z_dir=(1, 0, 1))
    ) as s:
        Rectangle(40 * SCALE, 40 * SCALE)
    add(extrude(s.sketch, amount=40 * SCALE), mode=Mode.SUBTRACT)


def make_cab():
    """Create the cab with windows for bridging test."""
    with BuildPart() as cab:
        Box(
            CAB_LENGTH,
            CAB_WIDTH,
            CAB_HEIGHT,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        # Window cut
        with BuildSketch(Plane.YZ.offset(CAB_LENGTH / 2)) as s:
            Rectangle(12 * SCALE, 10 * SCALE)
        add(extrude(s.sketch, amount=4 * SCALE), mode=Mode.SUBTRACT)
    add(
        cab.part.moved(
            Location((-BODY_LENGTH / 2 + CAB_LENGTH / 2 + 5 * SCALE, 0, BODY_HEIGHT))
        )
    )


def add_wheels():
    """Add four wheels as cylinders for circular accuracy testing."""
    wheel_positions = [
        (BODY_LENGTH / 2 - 12 * SCALE, BODY_WIDTH / 2 + WHEEL_WIDTH / 2),
        (BODY_LENGTH / 2 - 12 * SCALE, -BODY_WIDTH / 2 - WHEEL_WIDTH / 2),
        (-BODY_LENGTH / 2 + 12 * SCALE, BODY_WIDTH / 2 + WHEEL_WIDTH / 2),
        (-BODY_LENGTH / 2 + 12 * SCALE, -BODY_WIDTH / 2 - WHEEL_WIDTH / 2),
    ]
    for x, y in wheel_positions:
        wheel = Cylinder(
            WHEEL_RADIUS,
            WHEEL_WIDTH,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        wheel = wheel.rotate(Axis.X, 90)
        add(wheel.moved(Location((x, y, 0))))


def add_exhaust():
    """Add the exhaust stack for cooling and retraction test."""
    exhaust = Cylinder(
        EXHAUST_RADIUS,
        EXHAUST_HEIGHT,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )
    add(
        exhaust.moved(
            Location(
                (BODY_LENGTH / 2 - 18 * SCALE, -BODY_WIDTH / 2 + 4 * SCALE, BODY_HEIGHT)
            )
        )
    )


def cut_grille():
    """Cut fine grille lines to test small feature resolution."""
    grille_x = BODY_LENGTH / 2 - 1 * SCALE
    for i in range(-3, 4):
        with BuildSketch(Plane.YZ.offset(grille_x)) as s:
            Rectangle(GRILLE_SLOT_WIDTH, GRILLE_SLOT_HEIGHT)
        cut = extrude(s.sketch, amount=3 * SCALE).moved(
            Location((0, i * GRILLE_SLOT_SPACING, BODY_HEIGHT / 2))
        )
        add(cut, mode=Mode.SUBTRACT)


def add_hitch():
    """Add a rear hitch for tiny feature accuracy."""
    hitch = Cylinder(
        1.2 * SCALE,
        6 * SCALE,
        align=(Align.CENTER, Align.CENTER, Align.CENTER),
    )
    add(hitch.moved(Location((-BODY_LENGTH / 2 - 2 * SCALE, 0, 6 * SCALE))))


# =========================================================
# Tractor Assembly (Single Solid)
# =========================================================

with BuildPart() as tractor:
    make_body()  # base
    cut_hood_slope()  # overhang
    make_cab()  # cab with windows
    add_wheels()  # wheels
    add_exhaust()  # exhaust stack
    cut_grille()  # grille slots
    add_hitch()  # rear hitch

# =========================================================
# Display
# =========================================================

show(tractor)
