"""
Amalgam Maker Coin
Victory print / keyring featuring Logo 10 (octagonal nut + A)

A simple "I built an Amalgam" badge.
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

# Coin dimensions
DIAMETER = 40 * MM          # Across flats (not vertices)
THICKNESS = 5 * MM          # Coin thickness
SIDES = 8                   # Octagonal (matches Logo 10)

# Logo "A" parameters (sized to match Logo 10 proportions)
# The "A" should nearly fill the octagon with minimal negative space
A_FONT_SIZE = 28            # Font size for the "A" (~70% of diameter)
A_FONT = "Arial Black"      # Bold, clean font
EMBOSS_DEPTH = 1.5 * MM     # How deep to cut the "A"

# Keyring hole
HOLE_DIAMETER = 4 * MM      # Keyring hole size
HOLE_INSET = 5 * MM         # Distance from edge to hole center

# Edge treatment
CHAMFER_SIZE = 0.8 * MM     # Chamfer on top/bottom edges
SMALL_FILLET = 0.4 * MM     # Small fillet on internal edges

# =============================================================================
# Build the Maker Coin
# =============================================================================

def make_amalgam_coin(
    diameter: float = DIAMETER,
    thickness: float = THICKNESS,
    sides: int = SIDES,
    a_font_size: float = A_FONT_SIZE,
    a_font: str = A_FONT,
    emboss_depth: float = EMBOSS_DEPTH,
    hole_diameter: float = HOLE_DIAMETER,
    hole_inset: float = HOLE_INSET,
    chamfer_size: float = CHAMFER_SIZE,
) -> Part:
    """
    Create the Amalgam maker coin with Logo 10 design.

    The coin is an octagonal "nut" shape with a bold "A" embossed
    on the top face and a keyring hole at one vertex.

    Args:
        diameter: Across-flats diameter of the octagon
        thickness: Coin thickness
        sides: Number of sides (8 for octagon)
        a_font_size: Size of the "A" letter
        a_font: Font family for the "A"
        emboss_depth: Depth of the embossed "A"
        hole_diameter: Keyring hole diameter
        hole_inset: Distance from edge to hole center
        chamfer_size: Size of edge chamfers

    Returns:
        The completed maker coin Part
    """

    # Calculate the circumradius (center to vertex) from the inradius (center to flat)
    # For a regular polygon: circumradius = inradius / cos(π/n)
    import math
    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / sides)

    with BuildPart() as coin:
        # --- Base octagonal shape ---
        with BuildSketch(Plane.XY) as base:
            RegularPolygon(radius=circumradius, side_count=sides, align=(Align.CENTER, Align.CENTER))
        extrude(amount=thickness)

        # --- Emboss the "A" on top face ---
        with BuildSketch(Plane.XY.offset(thickness)) as logo:
            Text("A", font_size=a_font_size, font=a_font, align=(Align.CENTER, Align.CENTER))
        extrude(amount=-emboss_depth, mode=Mode.SUBTRACT)

        # --- Keyring hole at top vertex ---
        # Place hole at the top vertex (pointing up in Y direction)
        # The top vertex of the octagon is at (0, circumradius)
        hole_y = circumradius - hole_inset
        with BuildSketch(Plane.XY.offset(thickness / 2)):
            with Locations([(0, hole_y)]):
                Circle(radius=hole_diameter / 2)
        extrude(amount=thickness, both=True, mode=Mode.SUBTRACT)

        # --- Optional: Fillet outer edges ---
        # Note: Filleting after boolean operations can be tricky.
        # Uncomment below to add edge fillets (may need tuning)
        # try:
        #     perimeter_edges = coin.edges().filter_by(Axis.Z)
        #     fillet(perimeter_edges, radius=chamfer_size * 0.5)
        # except Exception as e:
        #     print(f"Note: Edge fillet skipped ({e})")

    return coin.part


def main():
    """Generate the maker coin and optionally display/export it."""

    print("=" * 50)
    print("Amalgam Maker Coin Generator")
    print("=" * 50)
    print(f"Diameter (across flats): {DIAMETER}mm")
    print(f"Thickness: {THICKNESS}mm")
    print(f"Sides: {SIDES} (octagonal)")
    print(f"Emboss depth: {EMBOSS_DEPTH}mm")
    print(f"Hole diameter: {HOLE_DIAMETER}mm")
    print()

    # Generate the coin
    coin = make_amalgam_coin()

    print("Coin generated successfully!")

    # Export to STL
    stl_path = "../stl/amalgam_maker_coin.stl"
    try:
        export_stl(coin, stl_path)
        print(f"Exported: {stl_path}")
    except Exception as e:
        print(f"Could not export STL: {e}")
        print("(Run from cad/parts/ directory for correct path)")

    # Show in viewer if available
    if HAS_VIEWER:
        print("Displaying in viewer...")
        show(coin)
    else:
        print("(Install ocp_vscode for interactive viewing)")

    return coin


# =============================================================================
# Entry point
# =============================================================================

if __name__ == "__main__":
    main()
