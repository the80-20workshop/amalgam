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
DIAMETER = 38 * MM          # Across flats (not vertices)
THICKNESS = 5 * MM          # Coin thickness
SIDES = 8                   # Octagonal (matches Logo 10)
OCTAGON_ROTATION = 22.5     # Rotation in degrees (22.5 = edge at top, 0 = vertex at top)

# Logo parameters (matching Logo 10)
A_FONT_SIZE = 26           # Font size for the raised solid "A"
A_CUTOUT_FONT_SIZE = 26   # Font size for the A-shaped cutout (larger)
A_FONT = "Arial Black"      # Bold, clean font
RECESS_DEPTH = 1.5 * MM     # How deep to recess

# Circle creates the bulging sides
CIRCLE_DIAMETER = 23 * MM   # Circle that creates the curved sides
CIRCLE_Y_OFFSET = -2 * MM   # Offset circle down (negative = down)

# Rounded corners on the cutout A
CUTOUT_FILLET = 1.5 * MM    # Radius for rounding the cutout A corners (larger = more rounded)

# Lanyard hole
HOLE_ENABLED = False         # Set to False to disable lanyard hole
HOLE_DIAMETER = 4 * MM      # Lanyard hole diameter
HOLE_INSET = 5 * MM         # Distance from edge to hole center

# Bottom text (frame path + date, or tagline)
# If empty, a random tagline is selected
BOTTOM_TEXT = ""            # e.g., "Scaffold 2026-02" or leave empty for random tagline
BOTTOM_TEXT_LINE2 = ""      # Optional second line (e.g., date)
BOTTOM_FONT_SIZE = 7        # Font size for bottom text
BOTTOM_TEXT_DEPTH = 0.4 * MM  # How deep to engrave
BOTTOM_LINE_SPACING = 1.5   # Multiplier for line spacing

# Taglines for random selection (when BOTTOM_TEXT is empty)
# Format: (line1, line2) - line2 can be empty
TAGLINES = [
    ("Scavenger", "Built"),
    ("2 Donors", "1 Printer"),
    ("Built Not", "Bought"),
    ("RepRap", "Reborn"),
]

# Minimum recommended coin diameter for readable text
MIN_COIN_DIAMETER = 35 * MM  # Minimum for legible bottom text

# Edge treatment
OUTER_FILLET = 1.0 * MM     # Fillet on outer vertical edges
EDGE_CHAMFER = 0.8 * MM     # Chamfer on top and bottom horizontal edges
RECESS_FILLET = 0.4 * MM    # Fillet on internal recess edges (bottom of cutout)


# =============================================================================
# Build the Maker Coin
# =============================================================================

def make_amalgam_coin(
    diameter: float = DIAMETER,
    thickness: float = THICKNESS,
    sides: int = SIDES,
    octagon_rotation: float = OCTAGON_ROTATION,
    a_font_size: float = A_FONT_SIZE,
    a_cutout_font_size: float = A_CUTOUT_FONT_SIZE,
    a_font: str = A_FONT,
    recess_depth: float = RECESS_DEPTH,
    circle_diameter: float = CIRCLE_DIAMETER,
    circle_y_offset: float = CIRCLE_Y_OFFSET,
    cutout_fillet: float = CUTOUT_FILLET,
    hole_enabled: bool = HOLE_ENABLED,
    hole_diameter: float = HOLE_DIAMETER,
    hole_inset: float = HOLE_INSET,
    bottom_text: str = BOTTOM_TEXT,
    bottom_text_line2: str = BOTTOM_TEXT_LINE2,
    bottom_font_size: float = BOTTOM_FONT_SIZE,
    bottom_text_depth: float = BOTTOM_TEXT_DEPTH,
    bottom_line_spacing: float = BOTTOM_LINE_SPACING,
    outer_fillet: float = OUTER_FILLET,
    edge_chamfer: float = EDGE_CHAMFER,
    recess_fillet: float = RECESS_FILLET,
) -> Part:
    """
    Create the Amalgam maker coin with Logo 10 design.

    The coin is an octagonal "nut" shape with Logo 10 on top:
    - Octagonal base
    - Circle cutout (creates bulging curves on sides)
    - Larger A cutout with rounded corners (extends beyond circle)
    - Raised sharp A added back on top (smaller, creates the letter)
    - The visible recess is the gap between cutout and raised A

    Args:
        diameter: Across-flats diameter of the octagon
        thickness: Coin thickness
        sides: Number of sides (8 for octagon)
        octagon_rotation: Rotation in degrees (22.5 = edge at top, 0 = vertex at top)
        a_font_size: Size of the raised solid "A"
        a_cutout_font_size: Size of the A-shaped cutout (larger)
        a_font: Font family for the "A"
        recess_depth: Depth of the recess
        circle_diameter: Diameter of the circle cutout
        circle_y_offset: Vertical offset for circle (negative = down)
        cutout_fillet: Radius for rounding cutout corners
        hole_enabled: Whether to add the lanyard hole
        hole_diameter: Lanyard hole diameter
        hole_inset: Distance from edge to hole center
        outer_fillet: Fillet radius on outer vertical edges
        edge_chamfer: Chamfer on top and bottom horizontal edges
        recess_fillet: Fillet radius on internal recess edges

    Returns:
        The completed maker coin Part
    """

    # Calculate the circumradius (center to vertex) from the inradius (center to flat)
    # For a regular polygon: circumradius = inradius / cos(π/n)
    import math
    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / sides)

    with BuildPart() as coin:
        # --- Base octagonal shape (full thickness) ---
        with BuildSketch(Plane.XY) as base:
            RegularPolygon(radius=circumradius, side_count=sides,
                          rotation=octagon_rotation, align=(Align.CENTER, Align.CENTER))
        extrude(amount=thickness)

        # --- Step 1: Cut the circle (creates bulging sides) ---
        with BuildSketch(Plane.XY.offset(thickness)) as circle_cut:
            with Locations([(0, circle_y_offset)]):
                Circle(radius=circle_diameter / 2)
        extrude(amount=-recess_depth, mode=Mode.SUBTRACT)

        # --- Step 2: Cut the larger A with rounded corners ---
        # This extends beyond the circle at top and bottom
        with BuildSketch(Plane.XY.offset(thickness)) as a_cutout:
            Text("A", font_size=a_cutout_font_size, font=a_font,
                 align=(Align.CENTER, Align.CENTER))
            # Offset outward to round external vertices and expand the shape
            offset(amount=cutout_fillet, kind=Kind.ARC)
        extrude(amount=-recess_depth, mode=Mode.SUBTRACT)

        # --- Fillet the internal recess edges (bottom of cutout) ---
        try:
            # Find edges at the recess floor level
            recess_z = thickness - recess_depth
            recess_edges = coin.edges().filter_by(
                lambda e: abs(e.center().Z - recess_z) < 0.1
            )
            if recess_edges:
                fillet(recess_edges, radius=recess_fillet)
        except Exception:
            pass  # May fail on complex geometry

        # --- Step 3: Add the raised sharp A back on top ---
        # Smaller than the cutout, centered, creates the visible letter
        with BuildSketch(Plane.XY.offset(thickness - recess_depth)) as raised_a:
            Text("A", font_size=a_font_size, font=a_font,
                 align=(Align.CENTER, Align.CENTER))
        extrude(amount=recess_depth, mode=Mode.ADD)

        # --- Lanyard hole at top edge (optional) ---
        if hole_enabled:
            hole_y = inradius - hole_inset
            with BuildSketch(Plane.XY.offset(thickness / 2)):
                with Locations([(0, hole_y)]):
                    Circle(radius=hole_diameter / 2)
            extrude(amount=thickness, both=True, mode=Mode.SUBTRACT)

        # --- Bottom text (frame path + date, or random tagline) ---
        import random
        line1 = bottom_text
        line2 = bottom_text_line2

        # If no text specified, pick a random tagline
        if not line1:
            tagline = random.choice(TAGLINES)
            line1, line2 = tagline

        # Calculate line positions for two-line text
        line_height = bottom_font_size * bottom_line_spacing
        if line2:
            y1 = line_height / 2   # Top line
            y2 = -line_height / 2  # Bottom line
        else:
            y1 = 0  # Single line centered
            y2 = None

        # Engrave on bottom face - use mirrored plane so text reads correctly
        # when viewing the bottom (flip on X axis)
        # With flipped plane, negative extrusion goes "up" into the coin
        bottom_plane = Plane.XY.offset(0)
        bottom_plane = bottom_plane.rotated((180, 0, 0))  # Flip to mirror text

        with BuildSketch(bottom_plane) as bottom_label:
            with Locations([(0, y1)]):
                Text(line1, font_size=bottom_font_size, font="Arial",
                     align=(Align.CENTER, Align.CENTER))
            if line2:
                with Locations([(0, y2)]):
                    Text(line2, font_size=bottom_font_size, font="Arial",
                         align=(Align.CENTER, Align.CENTER))
        extrude(amount=-bottom_text_depth, mode=Mode.SUBTRACT)

    # --- Apply edge treatments to the final part ---
    result = coin.part

    # Use relative tolerances based on coin dimensions
    z_tolerance = thickness * 0.1  # 10% of thickness
    outer_radius = (diameter / 2) * 0.8  # Only select edges near outer perimeter
    vertical_tolerance = thickness * 0.15  # 15% tolerance for vertical edge length

    # First, fillet vertical edges (the 8 outer octagon corners)
    # Do this first before chamfers change edge lengths
    try:
        vertical_edges = result.edges().filter_by(
            lambda e: (
                abs(e.length - thickness) < vertical_tolerance and  # Approximately full height
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius  # On outer perimeter
            )
        )
        if vertical_edges:
            result = fillet(vertical_edges, radius=outer_fillet)
        else:
            print("No vertical edges found for fillet")
    except Exception as ex:
        print(f"Vertical fillet failed: {ex}")

    # Chamfer top edges (outer octagon edges at Z = thickness)
    try:
        top_edges = result.edges().filter_by(
            lambda e: (
                abs(e.center().Z - thickness) < z_tolerance and  # At top
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius  # On outer perimeter
            )
        )
        if top_edges:
            result = chamfer(top_edges, length=edge_chamfer)
        else:
            print("No top edges found for chamfer")
    except Exception as ex:
        print(f"Top chamfer failed: {ex}")

    # Chamfer bottom edges (outer octagon edges at Z = 0)
    try:
        bottom_edges = result.edges().filter_by(
            lambda e: (
                abs(e.center().Z) < z_tolerance and  # At bottom
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius  # On outer perimeter
            )
        )
        if bottom_edges:
            result = chamfer(bottom_edges, length=edge_chamfer)
        else:
            print("No bottom edges found for chamfer")
    except Exception as ex:
        print(f"Bottom chamfer failed: {ex}")

    return result


def main():
    """Generate the maker coin and optionally display/export it."""
    import random

    print("=" * 50)
    print("Amalgam Maker Coin Generator")
    print("=" * 50)
    print(f"Diameter (across flats): {DIAMETER}mm")
    print(f"Thickness: {THICKNESS}mm")
    print(f"Sides: {SIDES} (octagonal)")
    print(f"Recess depth: {RECESS_DEPTH}mm")
    print(f"Raised A size: {A_FONT_SIZE}, Cutout A size: {A_CUTOUT_FONT_SIZE}")

    # Show what bottom text will be used
    if BOTTOM_TEXT:
        if BOTTOM_TEXT_LINE2:
            print(f"Bottom text: \"{BOTTOM_TEXT}\" / \"{BOTTOM_TEXT_LINE2}\"")
        else:
            print(f"Bottom text: \"{BOTTOM_TEXT}\"")
    else:
        tagline = random.choice(TAGLINES)
        print(f"Bottom text: \"{tagline[0]}\" / \"{tagline[1]}\" (random tagline)")
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
