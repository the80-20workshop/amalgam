"""
Amalgam Maker Coin
Victory print / keyring featuring the Amalgam logo (octagonal nut + stylized A)

A simple "I built an Amalgam" badge.

Uses the amalgam_logo module as the single source of truth for the logo design.
This module adds: lanyard hole, bottom text (from config or random tagline).
"""

from build123d import *
import math

# Import the logo from lib/
from amalgam.lib.logo import make_logo

# Import centralized export
from amalgam.lib.export import export_part

# Try to import show for interactive viewing
try:
    from ocp_vscode import show
    HAS_VIEWER = True
except ImportError:
    HAS_VIEWER = False

# =============================================================================
# Coin Parameters (extends logo with coin-specific features)
# =============================================================================

# Standard coin dimensions
DIAMETER = 38 * MM          # Across flats (standard maker coin size)
THICKNESS = 5 * MM          # Coin thickness

# Lanyard hole
HOLE_ENABLED = True         # Victory prints should have lanyard hole
HOLE_DIAMETER = 4 * MM      # Lanyard hole diameter
HOLE_INSET = 5 * MM         # Distance from edge to hole center

# Bottom text (frame path + date, or tagline)
# If empty, a random tagline is selected
BOTTOM_TEXT = ""            # e.g., "Darwin 2026-02" or leave empty for random tagline
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


# =============================================================================
# Build the Maker Coin
# =============================================================================

def make_amalgam_coin(
    diameter: float = DIAMETER,
    thickness: float = THICKNESS,
    hole_enabled: bool = HOLE_ENABLED,
    hole_diameter: float = HOLE_DIAMETER,
    hole_inset: float = HOLE_INSET,
    bottom_text: str = BOTTOM_TEXT,
    bottom_text_line2: str = BOTTOM_TEXT_LINE2,
    bottom_font_size: float = BOTTOM_FONT_SIZE,
    bottom_text_depth: float = BOTTOM_TEXT_DEPTH,
    bottom_line_spacing: float = BOTTOM_LINE_SPACING,
) -> Part:
    """
    Create the Amalgam maker coin.

    The coin is the standard Amalgam logo (octagon + stylized A) with:
    - Optional lanyard hole at top
    - Bottom text (from config or random tagline)

    Args:
        diameter: Across-flats diameter of the octagon
        thickness: Coin thickness
        hole_enabled: Whether to add the lanyard hole
        hole_diameter: Lanyard hole diameter
        hole_inset: Distance from edge to hole center
        bottom_text: First line of bottom text (empty = random tagline)
        bottom_text_line2: Second line of bottom text
        bottom_font_size: Font size for bottom text
        bottom_text_depth: How deep to engrave text
        bottom_line_spacing: Multiplier for line spacing

    Returns:
        The completed maker coin Part
    """
    import random

    # Start with the logo (handles all the complex geometry and edge treatments)
    result = make_logo(diameter=diameter, thickness=thickness)

    inradius = diameter / 2

    # --- Lanyard hole at top edge (optional) ---
    if hole_enabled:
        hole_y = inradius - hole_inset
        with BuildPart() as hole_part:
            with BuildSketch(Plane.XY.offset(thickness / 2)):
                with Locations([(0, hole_y)]):
                    Circle(radius=hole_diameter / 2)
            extrude(amount=thickness, both=True)
        result = result.cut(hole_part.part)

    # --- Bottom text (frame path + date, or random tagline) ---
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
    bottom_plane = Plane.XY.offset(0)
    bottom_plane = bottom_plane.rotated((180, 0, 0))  # Flip to mirror text

    with BuildPart() as text_part:
        with BuildSketch(bottom_plane):
            with Locations([(0, y1)]):
                Text(line1, font_size=bottom_font_size, font="Arial",
                     align=(Align.CENTER, Align.CENTER))
            if line2:
                with Locations([(0, y2)]):
                    Text(line2, font_size=bottom_font_size, font="Arial",
                         align=(Align.CENTER, Align.CENTER))
        extrude(amount=-bottom_text_depth)

    result = result.cut(text_part.part)

    return result


def main():
    """Generate the maker coin and optionally display/export it."""
    import random

    print("=" * 50)
    print("Amalgam Maker Coin Generator")
    print("=" * 50)
    print(f"Diameter (across flats): {DIAMETER}mm")
    print(f"Thickness: {THICKNESS}mm")
    print(f"Lanyard hole: {'Yes' if HOLE_ENABLED else 'No'}")

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

    # Export using centralized export module (format from config/env)
    print("\nExporting...")
    export_part(coin, "maker_coin")

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
