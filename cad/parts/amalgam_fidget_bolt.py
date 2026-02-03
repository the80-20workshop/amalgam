"""
Amalgam Fidget Bolt
A working nut and bolt with Logo 10 on the bolt head.

Both nut and bolt are octagonal, matching the Amalgam logo.
Designed with printable threads - a fidget toy that also tests calibration.
"""

from build123d import *
import math

# Try to import show for interactive viewing
try:
    from ocp_vscode import show
    HAS_VIEWER = True
except ImportError:
    HAS_VIEWER = False

# =============================================================================
# Parameters
# =============================================================================

# Thread parameters (optimized for FDM printing)
THREAD_DIAMETER = 12 * MM       # Nominal thread diameter (M12-ish)
THREAD_PITCH = 2.5 * MM         # Coarse pitch for easy printing
THREAD_LENGTH = 20 * MM         # Length of threaded section
THREAD_CLEARANCE = 0.3 * MM     # Clearance for nut (adjust for printer)

# Bolt head parameters
HEAD_DIAMETER = 24 * MM         # Across flats
HEAD_HEIGHT = 8 * MM            # Height of bolt head
HEAD_SIDES = 8                  # Octagonal (matches Logo 10)

# Nut parameters
NUT_DIAMETER = 24 * MM          # Across flats (same as head)
NUT_HEIGHT = 10 * MM            # Nut thickness
NUT_SIDES = 8                   # Octagonal

# Logo parameters
LOGO_SIZE = 16 * MM             # Logo octagon size on bolt head
LOGO_DEPTH = 1.2 * MM           # Emboss depth
LOGO_FONT_SIZE = 10             # Font size for "A"

# Edge treatment
CHAMFER_SIZE = 1.0 * MM         # Chamfer on head/nut edges

# Thread profile (trapezoidal for better printing)
THREAD_ANGLE = 30               # Thread flank angle (degrees)
THREAD_DEPTH = THREAD_PITCH * 0.5  # Thread depth


# =============================================================================
# Thread Helpers
# =============================================================================

def make_thread_profile(
    pitch: float,
    depth: float,
    angle: float,
    external: bool = True,
) -> Sketch:
    """
    Create a trapezoidal thread profile for FDM printing.

    Trapezoidal threads are more forgiving than ISO metric threads
    and print better on FDM printers.
    """
    # Calculate profile points
    half_angle = math.radians(angle)
    flat_width = pitch * 0.25  # Flat at root and crest

    if external:
        # External thread (bolt) - starts at major diameter
        points = [
            (0, 0),
            (flat_width / 2, 0),
            (pitch / 2 - flat_width / 2, -depth),
            (pitch / 2 + flat_width / 2, -depth),
            (pitch - flat_width / 2, 0),
            (pitch, 0),
        ]
    else:
        # Internal thread (nut) - starts at minor diameter
        points = [
            (0, 0),
            (flat_width / 2, 0),
            (pitch / 2 - flat_width / 2, depth),
            (pitch / 2 + flat_width / 2, depth),
            (pitch - flat_width / 2, 0),
            (pitch, 0),
        ]

    return points


# =============================================================================
# Build the Bolt
# =============================================================================

def make_amalgam_bolt(
    thread_diameter: float = THREAD_DIAMETER,
    thread_pitch: float = THREAD_PITCH,
    thread_length: float = THREAD_LENGTH,
    head_diameter: float = HEAD_DIAMETER,
    head_height: float = HEAD_HEIGHT,
    head_sides: int = HEAD_SIDES,
    logo_size: float = LOGO_SIZE,
    logo_depth: float = LOGO_DEPTH,
    logo_font_size: float = LOGO_FONT_SIZE,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Create the bolt with octagonal head and Logo 10.
    """

    # Calculate circumradius from inradius (across-flats to across-corners)
    head_inradius = head_diameter / 2
    head_circumradius = head_inradius / math.cos(math.pi / head_sides)

    logo_inradius = logo_size / 2
    logo_circumradius = logo_inradius / math.cos(math.pi / 8)

    with BuildPart() as bolt:
        # --- Bolt head (octagonal) ---
        with BuildSketch(Plane.XY) as head_sketch:
            RegularPolygon(radius=head_circumradius, side_count=head_sides)
        extrude(amount=head_height)

        # --- Shank (smooth section under head) ---
        shank_length = 3 * MM  # Short smooth section
        with BuildSketch(Plane.XY.offset(-shank_length)) as shank_sketch:
            Circle(radius=thread_diameter / 2)
        extrude(amount=shank_length)

        # --- Threaded section ---
        # Use TrapezoidalThread or create with helix
        # For simplicity, using metric thread approximation
        with BuildSketch(Plane.XY.offset(-shank_length - thread_length)) as thread_base:
            Circle(radius=thread_diameter / 2)
        extrude(amount=thread_length)

        # Add thread using helix
        thread_helix = Helix(
            pitch=thread_pitch,
            height=thread_length,
            radius=thread_diameter / 2,
            center=(0, 0, -shank_length - thread_length),
            direction=(0, 0, 1),
        )

        # Thread profile
        thread_depth = thread_pitch * 0.4
        with BuildSketch(Plane(thread_helix @ 0, z_dir=thread_helix % 0)) as thread_profile:
            with Locations([(thread_diameter / 2, 0)]):
                Polygon(
                    (0, 0),
                    (-thread_depth, thread_pitch * 0.25),
                    (-thread_depth, thread_pitch * 0.75),
                    (0, thread_pitch),
                    align=None
                )
                make_face()

        sweep(path=thread_helix)

        # --- Chamfer bolt head edges ---
        top_face = bolt.faces().sort_by(Axis.Z)[-1]
        top_edges = top_face.edges()
        chamfer(top_edges, length=chamfer_size)

        # --- Chamfer thread end ---
        bottom_edges = bolt.faces().sort_by(Axis.Z)[0].edges()
        try:
            chamfer(bottom_edges, length=chamfer_size * 0.5)
        except:
            pass  # May fail on thread geometry

        # --- Emboss Logo 10 on top of head ---
        with BuildSketch(Plane.XY.offset(head_height)) as logo:
            # Octagonal outline
            RegularPolygon(radius=logo_circumradius, side_count=8)
            # Cut out the "A"
            Text("A", font_size=logo_font_size, font="Arial Black",
                 align=(Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)
        extrude(amount=-logo_depth, mode=Mode.SUBTRACT)

    return bolt.part


# =============================================================================
# Build the Nut
# =============================================================================

def make_amalgam_nut(
    thread_diameter: float = THREAD_DIAMETER,
    thread_pitch: float = THREAD_PITCH,
    thread_clearance: float = THREAD_CLEARANCE,
    nut_diameter: float = NUT_DIAMETER,
    nut_height: float = NUT_HEIGHT,
    nut_sides: int = NUT_SIDES,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Create the matching octagonal nut with internal threads.
    """

    # Calculate circumradius
    nut_inradius = nut_diameter / 2
    nut_circumradius = nut_inradius / math.cos(math.pi / nut_sides)

    # Internal thread diameter (with clearance)
    internal_diameter = thread_diameter + thread_clearance * 2

    with BuildPart() as nut:
        # --- Nut body (octagonal) ---
        with BuildSketch(Plane.XY) as nut_sketch:
            RegularPolygon(radius=nut_circumradius, side_count=nut_sides)
        extrude(amount=nut_height)

        # --- Central hole ---
        with BuildSketch(Plane.XY) as hole_sketch:
            Circle(radius=internal_diameter / 2)
        extrude(amount=nut_height, mode=Mode.SUBTRACT)

        # --- Internal threads ---
        thread_helix = Helix(
            pitch=thread_pitch,
            height=nut_height,
            radius=internal_diameter / 2,
            center=(0, 0, 0),
            direction=(0, 0, 1),
        )

        # Thread profile (internal - cuts inward)
        thread_depth = thread_pitch * 0.4
        with BuildSketch(Plane(thread_helix @ 0, z_dir=thread_helix % 0)) as thread_profile:
            with Locations([(internal_diameter / 2, 0)]):
                Polygon(
                    (0, 0),
                    (thread_depth, thread_pitch * 0.25),
                    (thread_depth, thread_pitch * 0.75),
                    (0, thread_pitch),
                    align=None
                )
                make_face()

        sweep(path=thread_helix, mode=Mode.SUBTRACT)

        # --- Chamfer top and bottom edges ---
        top_edges = nut.faces().sort_by(Axis.Z)[-1].edges().filter_by(
            lambda e: e.length > nut_diameter * 0.3  # Only outer edges
        )
        bottom_edges = nut.faces().sort_by(Axis.Z)[0].edges().filter_by(
            lambda e: e.length > nut_diameter * 0.3
        )

        try:
            chamfer(top_edges, length=chamfer_size)
            chamfer(bottom_edges, length=chamfer_size)
        except:
            pass  # May fail on complex geometry

        # --- Chamfer internal hole edges ---
        try:
            # Find circular edges at top and bottom of hole
            internal_top = nut.edges().filter_by(GeomType.CIRCLE).sort_by(Axis.Z)[-1]
            internal_bottom = nut.edges().filter_by(GeomType.CIRCLE).sort_by(Axis.Z)[0]
            chamfer([internal_top, internal_bottom], length=chamfer_size * 0.5)
        except:
            pass

    return nut.part


# =============================================================================
# Simplified Version (if threads are problematic)
# =============================================================================

def make_simple_bolt(
    thread_diameter: float = THREAD_DIAMETER,
    thread_length: float = THREAD_LENGTH,
    head_diameter: float = HEAD_DIAMETER,
    head_height: float = HEAD_HEIGHT,
    head_sides: int = HEAD_SIDES,
    logo_size: float = LOGO_SIZE,
    logo_depth: float = LOGO_DEPTH,
    logo_font_size: float = LOGO_FONT_SIZE,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Simplified bolt without complex thread geometry.
    Uses cosmetic thread grooves instead of full helix.
    """

    head_circumradius = (head_diameter / 2) / math.cos(math.pi / head_sides)
    logo_circumradius = (logo_size / 2) / math.cos(math.pi / 8)

    with BuildPart() as bolt:
        # --- Bolt head (octagonal) ---
        with BuildSketch(Plane.XY) as head_sketch:
            RegularPolygon(radius=head_circumradius, side_count=head_sides)
        extrude(amount=head_height)

        # --- Shank + thread section ---
        total_shank = thread_length + 3  # 3mm smooth section
        with BuildSketch(Plane.XY.offset(-total_shank)) as shank_sketch:
            Circle(radius=thread_diameter / 2)
        extrude(amount=total_shank)

        # --- Chamfer edges ---
        top_edges = bolt.faces().sort_by(Axis.Z)[-1].edges()
        chamfer(top_edges, length=chamfer_size)

        # Chamfer bottom (thread end)
        bottom_edges = bolt.faces().sort_by(Axis.Z)[0].edges()
        chamfer(bottom_edges, length=thread_diameter * 0.15)

        # --- Logo on top ---
        with BuildSketch(Plane.XY.offset(head_height)) as logo:
            RegularPolygon(radius=logo_circumradius, side_count=8)
            Text("A", font_size=logo_font_size, font="Arial Black",
                 align=(Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)
        extrude(amount=-logo_depth, mode=Mode.SUBTRACT)

    return bolt.part


def make_simple_nut(
    thread_diameter: float = THREAD_DIAMETER,
    thread_clearance: float = THREAD_CLEARANCE,
    nut_diameter: float = NUT_DIAMETER,
    nut_height: float = NUT_HEIGHT,
    nut_sides: int = NUT_SIDES,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Simplified nut with plain hole (no internal threads).
    For display/fidget without working threads.
    """

    nut_circumradius = (nut_diameter / 2) / math.cos(math.pi / nut_sides)
    internal_diameter = thread_diameter + thread_clearance * 2

    with BuildPart() as nut:
        # --- Nut body ---
        with BuildSketch(Plane.XY) as nut_sketch:
            RegularPolygon(radius=nut_circumradius, side_count=nut_sides)
            Circle(radius=internal_diameter / 2, mode=Mode.SUBTRACT)
        extrude(amount=nut_height)

        # --- Chamfer edges ---
        all_edges = nut.edges().filter_by(Axis.Z)
        chamfer(all_edges, length=chamfer_size)

    return nut.part


# =============================================================================
# Main
# =============================================================================

def main():
    """Generate the fidget bolt and nut."""

    print("=" * 50)
    print("Amalgam Fidget Bolt Generator")
    print("=" * 50)
    print(f"Thread diameter: {THREAD_DIAMETER}mm")
    print(f"Thread pitch: {THREAD_PITCH}mm")
    print(f"Thread length: {THREAD_LENGTH}mm")
    print(f"Head/Nut diameter: {HEAD_DIAMETER}mm across flats")
    print(f"Sides: {HEAD_SIDES} (octagonal)")
    print()

    # Try full threaded version first, fall back to simple
    try:
        print("Generating threaded bolt...")
        bolt = make_amalgam_bolt()
        print("Threaded bolt generated!")
    except Exception as e:
        print(f"Threaded bolt failed ({e}), using simple version...")
        bolt = make_simple_bolt()
        print("Simple bolt generated!")

    try:
        print("Generating threaded nut...")
        nut = make_amalgam_nut()
        print("Threaded nut generated!")
    except Exception as e:
        print(f"Threaded nut failed ({e}), using simple version...")
        nut = make_simple_nut()
        print("Simple nut generated!")

    # Export to STL
    try:
        export_stl(bolt, "../stl/amalgam_fidget_bolt.stl")
        print("Exported: ../stl/amalgam_fidget_bolt.stl")

        export_stl(nut, "../stl/amalgam_fidget_nut.stl")
        print("Exported: ../stl/amalgam_fidget_nut.stl")
    except Exception as e:
        print(f"Could not export STL: {e}")

    # Show in viewer
    if HAS_VIEWER:
        print("Displaying in viewer...")
        # Position nut next to bolt for display
        nut_display = nut.move(Location((HEAD_DIAMETER * 1.5, 0, 0)))
        show(bolt, nut_display)

    return bolt, nut


# =============================================================================
# Entry point
# =============================================================================

if __name__ == "__main__":
    main()
