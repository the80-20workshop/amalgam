"""
Amalgam Anvil Victory Print
A miniature anvil with Logo 10 embossed on the side.

The "I built an Amalgam" trophy.
"""

from build123d import *

# Try to import show for interactive viewing
try:
    from ocp_vscode import show
    HAS_VIEWER = True
except ImportError:
    HAS_VIEWER = False

# =============================================================================
# Parameters
# =============================================================================

# Overall anvil size
ANVIL_LENGTH = 60 * MM      # Total length (horn tip to heel)
ANVIL_HEIGHT = 35 * MM      # Total height
ANVIL_WIDTH = 25 * MM       # Body width

# Face (top working surface)
FACE_LENGTH = 30 * MM       # Length of flat top surface
FACE_WIDTH = 20 * MM        # Width of flat top surface

# Horn (pointed end)
HORN_LENGTH = 18 * MM       # Length of the horn
HORN_TIP_DIAMETER = 6 * MM  # Diameter at horn tip

# Heel (back end)
HEEL_LENGTH = 12 * MM       # Length of heel extension
HEEL_DROP = 5 * MM          # How much lower the heel is

# Base (feet)
BASE_HEIGHT = 12 * MM       # Height of the base/feet
BASE_TAPER = 3 * MM         # How much the base tapers inward

# Waist (narrowing under the face)
WAIST_DEPTH = 5 * MM        # How deep the waist cuts in

# Logo parameters
LOGO_SIZE = 12 * MM         # Size of the octagonal logo
LOGO_DEPTH = 1.5 * MM       # Emboss depth
LOGO_FONT_SIZE = 7          # Font size for "A" in logo

# Fillets
EDGE_FILLET = 1.5 * MM      # Fillet on main edges

# =============================================================================
# Build the Anvil
# =============================================================================

def make_amalgam_anvil(
    anvil_length: float = ANVIL_LENGTH,
    anvil_height: float = ANVIL_HEIGHT,
    anvil_width: float = ANVIL_WIDTH,
    face_length: float = FACE_LENGTH,
    face_width: float = FACE_WIDTH,
    horn_length: float = HORN_LENGTH,
    horn_tip_diameter: float = HORN_TIP_DIAMETER,
    heel_length: float = HEEL_LENGTH,
    heel_drop: float = HEEL_DROP,
    base_height: float = BASE_HEIGHT,
    base_taper: float = BASE_TAPER,
    waist_depth: float = WAIST_DEPTH,
    logo_size: float = LOGO_SIZE,
    logo_depth: float = LOGO_DEPTH,
    logo_font_size: float = LOGO_FONT_SIZE,
    edge_fillet: float = EDGE_FILLET,
) -> Part:
    """
    Create a miniature anvil with Logo 10 embossed on the side.

    The anvil is built from several operations:
    1. Main body block
    2. Horn (conical extension)
    3. Waist cutout (under the face)
    4. Base/feet shaping
    5. Logo embossing

    Returns:
        The completed anvil Part
    """
    import math

    with BuildPart() as anvil:
        # --- Main body ---
        # Start with a rectangular block for the body (excluding horn)
        body_length = face_length + heel_length

        with BuildSketch(Plane.XY) as body_profile:
            # Body rectangle, centered on X, starting at Y=0
            Rectangle(anvil_width, body_length, align=(Align.CENTER, Align.MIN))
        extrude(amount=anvil_height)

        # --- Add the horn ---
        # Horn extends from the front of the body, tapers to a point
        # Position at front of body (Y = body_length)
        horn_start_width = face_width * 0.8
        horn_start_height = anvil_height * 0.4

        with BuildSketch(Plane.XZ.offset(body_length)) as horn_base:
            # Elliptical base for horn
            Ellipse(horn_start_width / 2, horn_start_height / 2)
            # Position it at the right height (upper portion of body)
            with Locations([(0, anvil_height - horn_start_height / 2 - 2)]):
                pass

        # Create horn using loft from ellipse to small circle
        horn_base_plane = Plane.XZ.offset(body_length)
        horn_base_plane = horn_base_plane.shift((0, anvil_height - horn_start_height / 2 - 2, 0))

        horn_tip_plane = horn_base_plane.shift((0, 0, horn_length))

        with BuildSketch(horn_base_plane) as horn_start:
            Ellipse(horn_start_width / 2, horn_start_height / 2)

        with BuildSketch(horn_tip_plane) as horn_end:
            Circle(horn_tip_diameter / 2)

        loft([horn_start.sketch, horn_end.sketch])

        # --- Waist cutout (the curved section under the face) ---
        # Cut material from the sides to create the classic anvil waist
        waist_height = anvil_height - base_height - 5

        with BuildSketch(Plane.XZ.offset(body_length / 2)) as waist_cut_left:
            with Locations([(-anvil_width / 2 - waist_depth / 2, base_height + waist_height / 2)]):
                Ellipse(waist_depth, waist_height / 2)

        extrude(amount=body_length * 0.7, both=True, mode=Mode.SUBTRACT)

        with BuildSketch(Plane.XZ.offset(body_length / 2)) as waist_cut_right:
            with Locations([(anvil_width / 2 + waist_depth / 2, base_height + waist_height / 2)]):
                Ellipse(waist_depth, waist_height / 2)

        extrude(amount=body_length * 0.7, both=True, mode=Mode.SUBTRACT)

        # --- Heel drop (back of anvil is lower) ---
        with BuildSketch(Plane.XY.offset(anvil_height - heel_drop)) as heel_cut:
            with Locations([(0, -heel_length / 2)]):
                Rectangle(anvil_width + 10, heel_length + 5)

        extrude(amount=heel_drop + 5, mode=Mode.SUBTRACT)

        # --- Base taper (feet are narrower than body) ---
        # Cut angled sides at the bottom to create tapered feet
        with BuildSketch(Plane.YZ.offset(anvil_width / 2)) as base_taper_right:
            Polygon(
                (0, 0),
                (body_length, 0),
                (body_length, base_height),
                (0, base_height),
                (0, 0),
            )
            with Locations([(body_length / 2, base_height / 2)]):
                Rectangle(body_length - 10, base_height * 0.6, mode=Mode.SUBTRACT)

        extrude(amount=base_taper, mode=Mode.SUBTRACT)

        with BuildSketch(Plane.YZ.offset(-anvil_width / 2)) as base_taper_left:
            Polygon(
                (0, 0),
                (body_length, 0),
                (body_length, base_height),
                (0, base_height),
                (0, 0),
            )
            with Locations([(body_length / 2, base_height / 2)]):
                Rectangle(body_length - 10, base_height * 0.6, mode=Mode.SUBTRACT)

        extrude(amount=-base_taper, mode=Mode.SUBTRACT)

        # --- Fillet main edges ---
        try:
            # Fillet the top edges of the face
            top_edges = anvil.edges().filter_by(Plane.XY.offset(anvil_height))
            fillet(top_edges, radius=edge_fillet)
        except Exception:
            pass  # Some edges may not be fillettable

        # --- Emboss Logo 10 on the side ---
        # Logo goes on the right side face, centered
        logo_y = body_length / 2  # Center along length
        logo_z = (base_height + anvil_height) / 2  # Center vertically

        # Create the logo: octagon with "A" cut out
        circumradius = logo_size / 2 / math.cos(math.pi / 8)

        # Create logo sketch on the side face
        logo_plane = Plane.YZ.offset(anvil_width / 2)
        logo_plane = logo_plane.shift((logo_y, logo_z, 0))

        with BuildSketch(logo_plane) as logo_sketch:
            # Octagonal outline
            RegularPolygon(radius=circumradius, side_count=8)
            # Cut out the "A"
            Text("A", font_size=logo_font_size, font="Arial Black",
                 align=(Align.CENTER, Align.CENTER), mode=Mode.SUBTRACT)

        # Emboss the logo into the side
        extrude(amount=-logo_depth, mode=Mode.SUBTRACT)

    return anvil.part


def main():
    """Generate the anvil and optionally display/export it."""

    print("=" * 50)
    print("Amalgam Anvil Victory Print Generator")
    print("=" * 50)
    print(f"Length: {ANVIL_LENGTH}mm")
    print(f"Height: {ANVIL_HEIGHT}mm")
    print(f"Width: {ANVIL_WIDTH}mm")
    print(f"Logo size: {LOGO_SIZE}mm")
    print()

    # Generate the anvil
    anvil = make_amalgam_anvil()

    print("Anvil generated successfully!")

    # Export to STL
    stl_path = "../stl/amalgam_anvil.stl"
    try:
        export_stl(anvil, stl_path)
        print(f"Exported: {stl_path}")
    except Exception as e:
        print(f"Could not export STL: {e}")
        print("(Run from cad/parts/ directory for correct path)")

    # Show in viewer if available
    if HAS_VIEWER:
        print("Displaying in viewer...")
        show(anvil)
    else:
        print("(Install ocp_vscode for interactive viewing)")

    return anvil


# =============================================================================
# Entry point
# =============================================================================

if __name__ == "__main__":
    main()
