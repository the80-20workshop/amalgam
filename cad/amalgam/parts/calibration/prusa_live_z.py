"""
Amalgam Prusa-Style Live Z Calibration Pattern

Inspired by the Prusa MK3 firmware's built-in first layer calibration.
Original concept by Prusa Research (prusa3d.com).

This is a clean-room reimplementation in build123d, parametric to your bed size.

Pattern description:
- Progressive lines that get longer (for live Z adjustment)
- Small square patch at the end (for final inspection)

This pattern is ideal for live Z-offset adjustment because:
- You can adjust Z while it prints the lines
- Each line shows the result of your adjustment
- The square at the end confirms your final setting

References:
- Prusa Knowledge Base: https://help.prusa3d.com/article/first-layer-calibration-i3_112364
- Printables: https://www.printables.com/model/104767 (extracted pattern)

Usage:
    ./build.sh build prusa_live_z
"""

import sys
from build123d import *

try:
    from config import BUILD_VOLUME
    BED_X = BUILD_VOLUME["x"]
    BED_Y = BUILD_VOLUME["y"]
except ImportError:
    # Fallback: assume 200x200mm bed (common size)
    print("Note: config.py not found, using default 200x200mm bed")
    BED_X = 200
    BED_Y = 200

# =============================================================================
# Parameters
# =============================================================================

LAYER_HEIGHT = 0.2 * MM          # First layer height
LINE_WIDTH = 10 * MM             # Width of each line
LINE_SPACING = 5 * MM            # Gap between lines
MARGIN = 10 * MM                 # Margin from bed edge

# Square patch parameters
SQUARE_SIZE = 20 * MM            # Size of the final square patch

# Pattern parameters
NUM_LINES = 8                    # Number of zigzag lines
LINE_LENGTH_START = 40 * MM      # Starting line length
LINE_LENGTH_INCREMENT = 20 * MM  # How much longer each line gets


# =============================================================================
# Build the Pattern
# =============================================================================

def make_prusa_live_z(
    bed_x: float = BED_X,
    bed_y: float = BED_Y,
    layer_height: float = LAYER_HEIGHT,
    line_width: float = LINE_WIDTH,
    line_spacing: float = LINE_SPACING,
    margin: float = MARGIN,
    num_lines: int = NUM_LINES,
    line_length_start: float = LINE_LENGTH_START,
    line_length_increment: float = LINE_LENGTH_INCREMENT,
    square_size: float = SQUARE_SIZE,
) -> Part:
    """
    Create the Prusa-style live Z calibration pattern.

    Pattern consists of:
    1. Zigzag lines that get progressively longer
    2. Small square patch at the end for final inspection
    """

    # Calculate usable area
    usable_x = bed_x - (2 * margin)
    usable_y = bed_y - (2 * margin)

    # Calculate line pitch (width + spacing)
    line_pitch = line_width + line_spacing

    # Adjust num_lines to fit in usable area
    max_lines = int(usable_y / line_pitch)
    num_lines = min(num_lines, max_lines)

    # Calculate max line length
    max_line_length = usable_x - square_size - line_spacing

    print(f"Bed size: {bed_x}x{bed_y}mm")
    print(f"Pattern: {num_lines} zigzag lines")
    print(f"Line width: {line_width}mm, spacing: {line_spacing}mm")

    with BuildPart() as pattern:
        # Starting position (bottom-left, with margin)
        start_x = margin
        start_y = margin

        # Build zigzag lines
        for i in range(num_lines):
            # Calculate line length (gets longer each time)
            line_length = min(
                line_length_start + (i * line_length_increment),
                max_line_length
            )

            # Y position of this line's center
            y = start_y + (i * line_pitch) + (line_width / 2)

            # X position depends on whether line is left or right aligned
            # Alternate to create zigzag effect
            if i % 2 == 0:
                # Left-aligned
                x = start_x + (line_length / 2)
            else:
                # Right-aligned (but not past square area)
                x = start_x + max_line_length - (line_length / 2)

            # Create line
            with BuildSketch(Plane.XY):
                with Locations([(x, y)]):
                    Rectangle(line_length, line_width)
            extrude(amount=layer_height)

        # Add square patch at the end (bottom-left corner after lines)
        square_x = margin + (square_size / 2)
        square_y = start_y + (num_lines * line_pitch) + (square_size / 2)

        # Make sure square fits
        if square_y + (square_size / 2) < bed_y - margin:
            with BuildSketch(Plane.XY):
                with Locations([(square_x, square_y)]):
                    Rectangle(square_size, square_size)
            extrude(amount=layer_height)
            print(f"Square patch: {square_size}x{square_size}mm at Y={square_y:.1f}")

    return pattern.part


def make_prusa_live_z_simple(
    bed_x: float = BED_X,
    bed_y: float = BED_Y,
    layer_height: float = LAYER_HEIGHT,
    line_width: float = 10 * MM,
    line_spacing: float = 5 * MM,
    margin: float = 10 * MM,
    num_lines: int = 10,
    square_size: float = 20 * MM,
) -> Part:
    """
    Simpler version: parallel lines of increasing length + square.
    Matches the Prusa pattern more closely.
    """

    line_pitch = line_width + line_spacing

    # Calculate total pattern height
    total_height = (num_lines * line_pitch) + square_size + line_spacing

    # Start from top of bed, work down
    start_y = bed_y - margin - (line_width / 2)

    # Lines start short on left, get longer
    min_length = 60 * MM
    max_length = bed_x - (2 * margin) - square_size - line_spacing
    length_increment = (max_length - min_length) / max(1, num_lines - 1)

    print(f"Bed size: {bed_x}x{bed_y}mm")
    print(f"Pattern: {num_lines} lines, {min_length:.0f}mm to {max_length:.0f}mm")

    with BuildPart() as pattern:
        for i in range(num_lines):
            # Line length increases with each line
            line_length = min_length + (i * length_increment)

            # Y position (from top down)
            y = start_y - (i * line_pitch)

            # X position (left-aligned)
            x = margin + (line_length / 2)

            with BuildSketch(Plane.XY):
                with Locations([(x, y)]):
                    Rectangle(line_length, line_width)
            extrude(amount=layer_height)

        # Square patch at bottom-left
        square_x = margin + (square_size / 2)
        square_y = start_y - (num_lines * line_pitch) - (square_size / 2)

        with BuildSketch(Plane.XY):
            with Locations([(square_x, square_y)]):
                Rectangle(square_size, square_size)
        extrude(amount=layer_height)

        print(f"Square: {square_size}x{square_size}mm")

    return pattern.part


# =============================================================================
# Main
# =============================================================================

def main():
    """Generate the Prusa-style live Z calibration pattern."""

    print("=" * 50)
    print("Amalgam Prusa-Style Live Z Pattern")
    print("=" * 50)
    print()

    # Generate the simple version (closer to original Prusa)
    pattern = make_prusa_live_z_simple()

    # Export
    stl_path = "stl/prusa_live_z.stl"
    export_stl(pattern, stl_path)
    print(f"\nExported: {stl_path}")

    print()
    print("How to use:")
    print("  1. Start the print")
    print("  2. Watch the first few lines print")
    print("  3. Adjust Z-offset live (baby stepping):")
    print("     - Lines too thin/rough? Lower Z (more squish)")
    print("     - Lines have ridges? Raise Z (less squish)")
    print("  4. Each new line shows your adjustment")
    print("  5. Square at end confirms final setting")
    print()
    print("Klipper command for live adjustment:")
    print("  SET_GCODE_OFFSET Z_ADJUST=-0.02 MOVE=1  # Lower")
    print("  SET_GCODE_OFFSET Z_ADJUST=+0.02 MOVE=1  # Raise")
    print()

    return pattern


if __name__ == "__main__":
    main()
