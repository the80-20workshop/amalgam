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

# Logo parameters (matching Logo 10 - same approach as maker coin)
LOGO_A_FONT_SIZE = 18           # Font size for the raised solid "A"
LOGO_A_CUTOUT_SIZE = 16         # Font size for the A-shaped cutout (with rounded corners)
LOGO_CIRCLE_DIAMETER = 14 * MM  # Circle that creates the curved sides
LOGO_CIRCLE_Y_OFFSET = -1.5 * MM  # Offset circle down (negative = down)
LOGO_DEPTH = 1.2 * MM           # Depth of recess
LOGO_CUTOUT_FILLET = 1.4 * MM   # Radius for rounding the cutout A corners
LOGO_ROTATION = 22.5            # Rotate octagon head to align with logo

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
    logo_a_font_size: float = LOGO_A_FONT_SIZE,
    logo_a_cutout_size: float = LOGO_A_CUTOUT_SIZE,
    logo_circle_diameter: float = LOGO_CIRCLE_DIAMETER,
    logo_circle_y_offset: float = LOGO_CIRCLE_Y_OFFSET,
    logo_depth: float = LOGO_DEPTH,
    logo_cutout_fillet: float = LOGO_CUTOUT_FILLET,
    logo_rotation: float = LOGO_ROTATION,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Create the bolt with octagonal head and Logo 10.

    Logo 10 design (same as maker coin):
    - Cut circle (creates bulging sides)
    - Cut larger A with rounded corners
    - Add smaller sharp A back on top
    """

    # Calculate circumradius from inradius (across-flats to across-corners)
    head_inradius = head_diameter / 2
    head_circumradius = head_inradius / math.cos(math.pi / head_sides)

    with BuildPart() as bolt:
        # --- Bolt head (octagonal, rotated to align with logo) ---
        with BuildSketch(Plane.XY) as head_sketch:
            RegularPolygon(radius=head_circumradius, side_count=head_sides,
                          rotation=logo_rotation)
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

        # Add external thread grooves - simple ring cuts for reliable FDM printing
        thread_depth = thread_pitch * 0.35
        thread_bottom_z = -shank_length - thread_length
        num_threads = int(thread_length / thread_pitch)

        # Cut V-grooves at each thread position
        for i in range(num_threads):
            groove_z = thread_bottom_z + thread_pitch * (i + 0.5)
            # Create a V-groove ring by revolving a triangle
            with BuildSketch(Plane.XZ) as groove_profile:
                with Locations([(thread_diameter / 2, groove_z)]):
                    # Small triangle pointing inward
                    Polygon(
                        (0, -thread_pitch * 0.3),
                        (-thread_depth, 0),
                        (0, thread_pitch * 0.3),
                        align=None
                    )
            revolve(axis=Axis.Z, mode=Mode.SUBTRACT)

        # --- Logo 10 on top of head (same approach as maker coin) ---
        # Step 1: Cut the circle (creates bulging sides, offset down)
        with BuildSketch(Plane.XY.offset(head_height)) as circle_cut:
            with Locations([(0, logo_circle_y_offset)]):
                Circle(radius=logo_circle_diameter / 2)
        extrude(amount=-logo_depth, mode=Mode.SUBTRACT)

        # Step 2: Cut the larger A with rounded corners
        with BuildSketch(Plane.XY.offset(head_height)) as a_cutout:
            Text("A", font_size=logo_a_cutout_size, font="Arial Black",
                 align=(Align.CENTER, Align.CENTER))
            offset(amount=logo_cutout_fillet, kind=Kind.ARC)
        extrude(amount=-logo_depth, mode=Mode.SUBTRACT)

        # Step 3: Add the raised sharp A back on top
        with BuildSketch(Plane.XY.offset(head_height - logo_depth)) as raised_a:
            Text("A", font_size=logo_a_font_size, font="Arial Black",
                 align=(Align.CENTER, Align.CENTER))
        extrude(amount=logo_depth, mode=Mode.ADD)

    # --- Apply edge treatments outside BuildPart for better control ---
    result = bolt.part
    shank_length = 3 * MM  # Match the value used above
    head_outer_radius = (head_diameter / 2) * 0.8

    # Fillet vertical edges of the bolt head (the 8 octagon corners)
    try:
        vertical_edges = result.edges().filter_by(
            lambda e: (
                abs(e.length - head_height) < head_height * 0.2 and  # Approximately head height
                e.center().Z > 0 and  # In the head region (above Z=0)
                math.sqrt(e.center().X**2 + e.center().Y**2) > head_outer_radius  # On outer perimeter
            )
        )
        if vertical_edges:
            result = fillet(vertical_edges, radius=chamfer_size)
    except Exception as ex:
        print(f"Bolt head vertical fillet failed: {ex}")

    # Chamfer top edges of bolt head (outer octagon edges, not logo edges)
    # Filter for straight LINE edges on outer perimeter at the top
    min_edge_length = head_diameter * 0.25  # Octagon edges are ~0.41 * diameter
    try:
        top_edges = result.edges().filter_by(GeomType.LINE).filter_by(
            lambda e: (
                abs(e.center().Z - head_height) < 1.0 and  # At top (within 1mm)
                math.sqrt(e.center().X**2 + e.center().Y**2) > head_outer_radius and
                e.length > min_edge_length
            )
        )
        if top_edges:
            result = chamfer(top_edges, length=chamfer_size * 0.6)  # Smaller chamfer after fillets
        else:
            print("No top edges found for chamfer")
    except Exception as ex:
        print(f"Bolt head top chamfer failed: {ex}")

    # Chamfer bottom edges of bolt head (outer octagon edges at Z=0, not the shank circle)
    min_edge_length = head_diameter * 0.3  # Filter out the circular shank edge
    try:
        bottom_head_edges = result.edges().filter_by(
            lambda e: (
                abs(e.center().Z) < 0.5 and  # At Z ≈ 0
                math.sqrt(e.center().X**2 + e.center().Y**2) > head_outer_radius and
                e.length > min_edge_length  # Only straight octagon edges
            )
        )
        if bottom_head_edges:
            result = chamfer(bottom_head_edges, length=chamfer_size * 0.8)
    except Exception as ex:
        print(f"Bolt head bottom chamfer failed: {ex}")

    # Chamfer the thread tip
    try:
        thread_tip_z = -shank_length - thread_length
        tip_edges = result.edges().filter_by(
            lambda e: abs(e.center().Z - thread_tip_z) < 1.0
        )
        if tip_edges:
            result = chamfer(tip_edges, length=chamfer_size * 0.5)
    except Exception as ex:
        pass  # May fail on thread geometry

    return result


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
    nut_rotation: float = LOGO_ROTATION,  # Match bolt head rotation
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
        # --- Nut body (octagonal, rotated to match bolt head) ---
        with BuildSketch(Plane.XY) as nut_sketch:
            RegularPolygon(radius=nut_circumradius, side_count=nut_sides,
                          rotation=nut_rotation)
        extrude(amount=nut_height)

        # --- Central hole ---
        with BuildSketch(Plane.XY) as hole_sketch:
            Circle(radius=internal_diameter / 2)
        extrude(amount=nut_height, mode=Mode.SUBTRACT)

        # --- Internal thread ridges - simple rings for reliable FDM printing ---
        thread_depth = thread_pitch * 0.35
        num_threads = int(nut_height / thread_pitch)

        # Add V-ridges at each thread position (project into the hole)
        for i in range(num_threads):
            ridge_z = thread_pitch * (i + 0.5)
            if ridge_z < nut_height - thread_pitch * 0.3:  # Leave margin at top
                # Create a V-ridge ring by revolving a triangle
                with BuildSketch(Plane.XZ) as ridge_profile:
                    with Locations([(internal_diameter / 2, ridge_z)]):
                        # Small triangle pointing inward (into the hole)
                        Polygon(
                            (0, -thread_pitch * 0.3),
                            (-thread_depth, 0),
                            (0, thread_pitch * 0.3),
                            align=None
                        )
                revolve(axis=Axis.Z, mode=Mode.ADD)

    # Apply edge treatments outside BuildPart for better control
    result = nut.part

    # Fillet vertical edges (the 8 outer corners) first
    try:
        outer_radius = (nut_diameter / 2) * 0.8
        vertical_edges = result.edges().filter_by(
            lambda e: (
                abs(e.length - nut_height) < nut_height * 0.15 and
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius
            )
        )
        if vertical_edges:
            result = fillet(vertical_edges, radius=chamfer_size)
    except Exception as ex:
        print(f"Nut vertical fillet failed: {ex}")

    # Chamfer top outer edges (LINE edges only, smaller size after fillets)
    try:
        top_edges = result.edges().filter_by(GeomType.LINE).filter_by(
            lambda e: (
                abs(e.center().Z - nut_height) < 1.0 and
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius
            )
        )
        if top_edges:
            result = chamfer(top_edges, length=chamfer_size * 0.5)
    except Exception as ex:
        print(f"Nut top chamfer failed: {ex}")

    # Chamfer bottom outer edges (LINE edges only)
    try:
        bottom_edges = result.edges().filter_by(GeomType.LINE).filter_by(
            lambda e: (
                abs(e.center().Z) < 1.0 and
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius
            )
        )
        if bottom_edges:
            result = chamfer(bottom_edges, length=chamfer_size * 0.5)
    except Exception as ex:
        print(f"Nut bottom chamfer failed: {ex}")

    # Chamfer internal hole edges (top and bottom circles only)
    try:
        internal_edges = result.edges().filter_by(GeomType.CIRCLE).filter_by(
            lambda e: abs(e.center().Z) < 1.0 or abs(e.center().Z - nut_height) < 1.0
        )
        if internal_edges:
            result = chamfer(internal_edges, length=chamfer_size * 0.3)
    except Exception as ex:
        print(f"Nut internal chamfer failed: {ex}")

    return result


# =============================================================================
# Simplified Version (if threads are problematic)
# =============================================================================

def make_simple_bolt(
    thread_diameter: float = THREAD_DIAMETER,
    thread_length: float = THREAD_LENGTH,
    head_diameter: float = HEAD_DIAMETER,
    head_height: float = HEAD_HEIGHT,
    head_sides: int = HEAD_SIDES,
    logo_a_font_size: float = LOGO_A_FONT_SIZE,
    logo_a_cutout_size: float = LOGO_A_CUTOUT_SIZE,
    logo_circle_diameter: float = LOGO_CIRCLE_DIAMETER,
    logo_depth: float = LOGO_DEPTH,
    logo_cutout_fillet: float = LOGO_CUTOUT_FILLET,
    logo_rotation: float = LOGO_ROTATION,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Simplified bolt without complex thread geometry.
    Smooth shank - for display or to add threads in slicer.
    """

    head_circumradius = (head_diameter / 2) / math.cos(math.pi / head_sides)

    with BuildPart() as bolt:
        # --- Bolt head (octagonal) ---
        with BuildSketch(Plane.XY) as head_sketch:
            RegularPolygon(radius=head_circumradius, side_count=head_sides,
                          rotation=logo_rotation)
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

        # --- Logo 10 on top (same approach as maker coin) ---
        # Step 1: Cut the circle
        with BuildSketch(Plane.XY.offset(head_height)) as circle_cut:
            Circle(radius=logo_circle_diameter / 2)
        extrude(amount=-logo_depth, mode=Mode.SUBTRACT)

        # Step 2: Cut the larger A with rounded corners
        with BuildSketch(Plane.XY.offset(head_height)) as a_cutout:
            Text("A", font_size=logo_a_cutout_size, font="Arial Black",
                 align=(Align.CENTER, Align.CENTER))
            offset(amount=logo_cutout_fillet, kind=Kind.ARC)
        extrude(amount=-logo_depth, mode=Mode.SUBTRACT)

        # Step 3: Add the raised sharp A back on top
        with BuildSketch(Plane.XY.offset(head_height - logo_depth)) as raised_a:
            Text("A", font_size=logo_a_font_size, font="Arial Black",
                 align=(Align.CENTER, Align.CENTER))
        extrude(amount=logo_depth, mode=Mode.ADD)

    return bolt.part


def make_simple_nut(
    thread_diameter: float = THREAD_DIAMETER,
    thread_clearance: float = THREAD_CLEARANCE,
    nut_diameter: float = NUT_DIAMETER,
    nut_height: float = NUT_HEIGHT,
    nut_sides: int = NUT_SIDES,
    nut_rotation: float = LOGO_ROTATION,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Simplified nut with plain hole (no internal threads).
    For display/fidget without working threads.
    """

    nut_circumradius = (nut_diameter / 2) / math.cos(math.pi / nut_sides)
    internal_diameter = thread_diameter + thread_clearance * 2

    with BuildPart() as nut:
        # --- Nut body (rotated to match bolt) ---
        with BuildSketch(Plane.XY) as nut_sketch:
            RegularPolygon(radius=nut_circumradius, side_count=nut_sides,
                          rotation=nut_rotation)
            Circle(radius=internal_diameter / 2, mode=Mode.SUBTRACT)
        extrude(amount=nut_height)

    # Apply edge treatments outside BuildPart
    result = nut.part
    outer_radius = (nut_diameter / 2) * 0.8

    # Fillet vertical edges
    try:
        vertical_edges = result.edges().filter_by(
            lambda e: (
                abs(e.length - nut_height) < nut_height * 0.15 and
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius
            )
        )
        if vertical_edges:
            result = fillet(vertical_edges, radius=chamfer_size)
    except:
        pass

    # Chamfer top/bottom outer edges
    try:
        top_edges = result.edges().filter_by(
            lambda e: abs(e.center().Z - nut_height) < nut_height * 0.1 and
                      math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius
        )
        if top_edges:
            result = chamfer(top_edges, length=chamfer_size * 0.8)
    except:
        pass

    try:
        bottom_edges = result.edges().filter_by(
            lambda e: abs(e.center().Z) < nut_height * 0.1 and
                      math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius
        )
        if bottom_edges:
            result = chamfer(bottom_edges, length=chamfer_size * 0.8)
    except:
        pass

    # Chamfer internal hole edges
    try:
        internal_edges = result.edges().filter_by(GeomType.CIRCLE)
        if internal_edges:
            result = chamfer(internal_edges, length=chamfer_size * 0.5)
    except:
        pass

    return result


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
