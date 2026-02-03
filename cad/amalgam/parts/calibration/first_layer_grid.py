"""
Amalgam First Layer Calibration Grid

A parametric grid of squares for first layer calibration.
Covers the bed to verify first layer consistency across the entire surface.

Inspired by common first layer test patterns from the 3D printing community.
Similar patterns exist on Printables, Thingiverse, and in printer firmwares.

This is an original implementation in build123d, parametric to your bed size.

Features:
- Grid of squares at 0.2mm height (one layer)
- Parametric: adjusts to your bed size from config.py
- Tests bed leveling, Z-offset, and mesh accuracy
- Also generates a snake pattern variant

References:
- Ellis Print Tuning Guide: https://ellis3dp.com/Print-Tuning-Guide/
- Prusa Knowledge Base: https://help.prusa3d.com/

Usage:
    ./build.sh build first_layer_grid
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

# Grid parameters
LAYER_HEIGHT = 0.2 * MM          # First layer height (adjust to match slicer)
SQUARE_SIZE = 20 * MM            # Size of each square
GAP_SIZE = 5 * MM                # Gap between squares
MARGIN = 15 * MM                 # Margin from bed edge


# =============================================================================
# Build the Grid
# =============================================================================

def make_first_layer_grid(
    bed_x: float = BED_X,
    bed_y: float = BED_Y,
    square_size: float = SQUARE_SIZE,
    gap_size: float = GAP_SIZE,
    margin: float = MARGIN,
    layer_height: float = LAYER_HEIGHT,
) -> Part:
    """
    Create a grid of squares for first layer calibration.

    The grid is centered on the bed and covers as much area as possible
    while maintaining the specified margins.
    """

    # Calculate usable area
    usable_x = bed_x - (2 * margin)
    usable_y = bed_y - (2 * margin)

    # Calculate grid dimensions
    cell_size = square_size + gap_size
    grid_cols = int(usable_x / cell_size)
    grid_rows = int(usable_y / cell_size)

    # Ensure at least 2x2 grid
    grid_cols = max(2, grid_cols)
    grid_rows = max(2, grid_rows)

    # Calculate actual grid size (to center it)
    actual_width = (grid_cols * square_size) + ((grid_cols - 1) * gap_size)
    actual_height = (grid_rows * square_size) + ((grid_rows - 1) * gap_size)

    # Starting position (bottom-left of grid, centered on bed)
    start_x = (bed_x - actual_width) / 2
    start_y = (bed_y - actual_height) / 2

    print(f"Bed size: {bed_x}x{bed_y}mm")
    print(f"Grid: {grid_cols}x{grid_rows} squares ({grid_cols * grid_rows} total)")
    print(f"Square size: {square_size}mm, Gap: {gap_size}mm")
    print(f"Grid coverage: {actual_width}x{actual_height}mm")

    # Build the grid
    with BuildPart() as grid:
        for row in range(grid_rows):
            for col in range(grid_cols):
                # Calculate position of this square's center
                x = start_x + (col * cell_size) + (square_size / 2)
                y = start_y + (row * cell_size) + (square_size / 2)

                # Create square at this position
                with BuildSketch(Plane.XY):
                    with Locations([(x, y)]):
                        Rectangle(square_size, square_size)
                extrude(amount=layer_height)

    return grid.part


def make_first_layer_snake(
    bed_x: float = BED_X,
    bed_y: float = BED_Y,
    line_width: float = 10 * MM,
    gap_width: float = 5 * MM,
    margin: float = MARGIN,
    layer_height: float = LAYER_HEIGHT,
) -> Part:
    """
    Alternative: snake/zigzag pattern for first layer calibration.

    A continuous path that covers the bed in a back-and-forth pattern.
    Good for seeing extrusion consistency along long runs.
    """

    # Calculate usable area
    usable_x = bed_x - (2 * margin)
    usable_y = bed_y - (2 * margin)

    # Calculate number of lines
    line_pitch = line_width + gap_width
    num_lines = int(usable_y / line_pitch)

    # Recalculate to center
    actual_height = (num_lines * line_width) + ((num_lines - 1) * gap_width)
    start_x = margin
    start_y = (bed_y - actual_height) / 2

    print(f"Bed size: {bed_x}x{bed_y}mm")
    print(f"Snake pattern: {num_lines} lines")
    print(f"Line width: {line_width}mm")

    with BuildPart() as snake:
        for i in range(num_lines):
            y = start_y + (i * line_pitch) + (line_width / 2)

            with BuildSketch(Plane.XY):
                with Locations([(bed_x / 2, y)]):
                    Rectangle(usable_x, line_width)
            extrude(amount=layer_height)

    return snake.part


# =============================================================================
# Main
# =============================================================================

def main():
    """Generate the first layer calibration grid."""

    print("=" * 50)
    print("Amalgam First Layer Calibration Grid")
    print("=" * 50)
    print()

    # Generate grid pattern (default)
    grid = make_first_layer_grid()

    # Export
    stl_path = "stl/first_layer_grid.stl"
    export_stl(grid, stl_path)
    print(f"\nExported: {stl_path}")

    # Also generate snake pattern as alternative
    snake = make_first_layer_snake()
    snake_path = "stl/first_layer_snake.stl"
    export_stl(snake, snake_path)
    print(f"Exported: {snake_path}")

    print()
    print("Print settings:")
    print(f"  Layer height: {LAYER_HEIGHT}mm (MUST match this file)")
    print("  Infill: 100% (or use 'solid infill' / rectilinear)")
    print("  No skirt/brim needed")
    print()
    print("What to look for:")
    print("  - Lines should slightly overlap (smooth surface)")
    print("  - Consistent appearance across entire bed")
    print("  - No rough/transparent areas (Z too high)")
    print("  - No ridges between lines (Z too low)")
    print()

    return grid


if __name__ == "__main__":
    main()
