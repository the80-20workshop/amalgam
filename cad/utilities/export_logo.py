#!/usr/bin/env python3
"""
Export Amalgam Logo as SVG and PNG.

Exports the logo in various formats for editing and branding use:
- SVG: Vector format for scalable graphics
- PNG: Raster with transparent background

Variants:
- Full: Octagon with stylized A (outline effect)
- Flat: Simple octagon + A silhouette (no recess, good for B&W)
- A only: Just the stylized A (no octagon)

Usage:
    python utilities/export_logo.py
    # or from repo root:
    python cad/utilities/export_logo.py

Outputs to: cad/exports/logo/
"""

import sys
from pathlib import Path

# Add cad/ to path for imports
cad_dir = Path(__file__).parent.parent
if str(cad_dir) not in sys.path:
    sys.path.insert(0, str(cad_dir))

from build123d import *
import math

# Import logo components
from amalgam.lib.stylized_a import make_stylized_a_sketch

# =============================================================================
# Configuration
# =============================================================================

OUTPUT_DIR = Path(__file__).parent.parent / "exports" / "logo"

# Default sizes
DIAMETER = 100 * MM      # Export size (mm) - large for quality
THICKNESS = 10 * MM      # For 3D projection (affects SVG shading)

# Octagon parameters (matching logo.py)
SIDES = 8
OCTAGON_ROTATION = 22.5  # Flat edge at top
A_SIZE_RATIO = 0.68
A_Y_OFFSET_RATIO = 0.09


# =============================================================================
# 2D Logo Sketches
# =============================================================================

def make_octagon_sketch(diameter: float = DIAMETER) -> Sketch:
    """Create the octagon outline as a 2D sketch."""
    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / SIDES)

    with BuildSketch() as octagon:
        RegularPolygon(
            radius=circumradius,
            side_count=SIDES,
            rotation=OCTAGON_ROTATION,
            align=(Align.CENTER, Align.CENTER)
        )
    return octagon.sketch


def make_flat_logo_sketch(diameter: float = DIAMETER) -> Sketch:
    """
    Create a flat logo (octagon + A, no recess effect).

    Good for black & white use, simple silhouette.
    """
    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / SIDES)

    a_size = diameter * A_SIZE_RATIO
    a_y_offset = diameter * A_Y_OFFSET_RATIO

    # Get the A sketch
    a_sketch = make_stylized_a_sketch(height=a_size)

    with BuildSketch() as logo:
        # Octagon base
        RegularPolygon(
            radius=circumradius,
            side_count=SIDES,
            rotation=OCTAGON_ROTATION,
            align=(Align.CENTER, Align.CENTER)
        )
        # Cut out the A shape
        with Locations([(0, a_y_offset)]):
            add(a_sketch, mode=Mode.SUBTRACT)

    return logo.sketch


def make_outline_logo_sketch(
    diameter: float = DIAMETER,
    outline_width: float = None,
) -> Sketch:
    """
    Create an outline logo (octagon outline + A with outline gap).

    Matches the visual appearance of the 3D logo from the top.
    """
    if outline_width is None:
        outline_width = diameter * 0.05  # 5% of diameter

    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / SIDES)

    a_size = diameter * A_SIZE_RATIO
    a_y_offset = diameter * A_Y_OFFSET_RATIO

    # Get the A sketch
    a_sketch = make_stylized_a_sketch(height=a_size)

    with BuildSketch() as logo:
        # Octagon base
        RegularPolygon(
            radius=circumradius,
            side_count=SIDES,
            rotation=OCTAGON_ROTATION,
            align=(Align.CENTER, Align.CENTER)
        )

        # Cut circle (creates the bulging sides effect area)
        circle_diameter = diameter * 0.55
        circle_y_offset = diameter * -0.03
        with Locations([(0, circle_y_offset)]):
            Circle(radius=circle_diameter / 2, mode=Mode.SUBTRACT)

        # Add the outlined A cutout
        with Locations([(0, a_y_offset)]):
            add(a_sketch)
            offset(amount=outline_width, kind=Kind.ARC, mode=Mode.SUBTRACT)

        # Add the A back (raised part)
        with Locations([(0, a_y_offset)]):
            add(a_sketch, mode=Mode.ADD)

    return logo.sketch


# =============================================================================
# Multi-color Logo (black octagon, white recess, black A)
# =============================================================================

def make_recess_logo_parts(
    diameter: float = DIAMETER,
    outline_width: float = None,
) -> tuple[Sketch, Sketch, Sketch]:
    """
    Create logo as separate parts for multi-color export.

    Returns:
        (octagon_sketch, recess_sketch, a_sketch) - three separate sketches
        - octagon: The full octagon (black background)
        - recess: The recessed area (circle + expanded A outline, white)
        - a: The raised A (black foreground)
    """
    if outline_width is None:
        outline_width = diameter * 0.05

    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / SIDES)

    a_size = diameter * A_SIZE_RATIO
    a_y_offset = diameter * A_Y_OFFSET_RATIO
    circle_diameter = diameter * 0.55
    circle_y_offset = diameter * -0.03

    # Get the A sketch
    a_sketch = make_stylized_a_sketch(height=a_size)

    # 1. Full octagon
    with BuildSketch() as octagon:
        RegularPolygon(
            radius=circumradius,
            side_count=SIDES,
            rotation=OCTAGON_ROTATION,
            align=(Align.CENTER, Align.CENTER)
        )
    octagon_sketch = octagon.sketch

    # 2. Recess area (circle + expanded A, but NOT the A itself)
    with BuildSketch() as recess:
        # Start with circle
        with Locations([(0, circle_y_offset)]):
            Circle(radius=circle_diameter / 2)
        # Add expanded A outline
        with Locations([(0, a_y_offset)]):
            add(a_sketch)
            offset(amount=outline_width, kind=Kind.ARC, mode=Mode.ADD)
        # Subtract the A itself (so recess is just the outline gap)
        with Locations([(0, a_y_offset)]):
            add(a_sketch, mode=Mode.SUBTRACT)
    recess_sketch = recess.sketch

    # 3. The A (positioned)
    with BuildSketch() as a_positioned:
        with Locations([(0, a_y_offset)]):
            add(a_sketch)
    a_final = a_positioned.sketch

    return octagon_sketch, recess_sketch, a_final


def export_multicolor_svg(
    octagon: Sketch,
    recess: Sketch,
    a_shape: Sketch,
    filepath: Path,
):
    """
    Export multi-color logo: black octagon, white recess, black A.
    """
    from build123d import ExportSVG, Unit

    exporter = ExportSVG(
        unit=Unit.MM,
        scale=1,
        margin=5,
        line_weight=0.1,  # Thin lines
    )

    # Add layers with different colors
    exporter.add_layer("octagon", fill_color=(0, 0, 0), line_color=(0, 0, 0))
    exporter.add_layer("recess", fill_color=(255, 255, 255), line_color=(255, 255, 255))
    exporter.add_layer("a", fill_color=(0, 0, 0), line_color=(0, 0, 0))

    # Add shapes to their layers
    exporter.add_shape(octagon, layer="octagon")
    exporter.add_shape(recess, layer="recess")
    exporter.add_shape(a_shape, layer="a")

    exporter.write(str(filepath))
    print(f"Exported: {filepath}")


# =============================================================================
# Export Functions
# =============================================================================

def export_sketch_svg(sketch: Sketch, filepath: Path, fill: bool = True):
    """
    Export a 2D sketch to SVG.

    Uses build123d's ExportSVG class for proper vector export.
    """
    from build123d import ExportSVG, Unit

    # Create SVG exporter
    exporter = ExportSVG(
        unit=Unit.MM,
        scale=1,
        margin=5,  # Add margin around shape
        line_weight=0.5,  # Visible line weight
        fill_color=(0, 0, 0) if fill else None,  # Black fill
        line_color=(0, 0, 0),  # Black outline
    )

    # Add the sketch shape
    exporter.add_shape(sketch)

    # Write the file
    exporter.write(str(filepath))
    print(f"Exported: {filepath}")


def export_all_variants(diameter: float = DIAMETER):
    """Export all logo variants."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Amalgam Logo Export")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Size: {diameter}mm diameter")
    print()

    # 1. Stylized A only (filled)
    print("1. Stylized A (standalone, filled)...")
    a_size = diameter * A_SIZE_RATIO
    a_sketch = make_stylized_a_sketch(height=a_size)
    export_sketch_svg(a_sketch, OUTPUT_DIR / "amalgam_a.svg", fill=True)

    # 2. Octagon only (outline)
    print("2. Octagon (outline only)...")
    octagon = make_octagon_sketch(diameter)
    export_sketch_svg(octagon, OUTPUT_DIR / "amalgam_octagon.svg", fill=False)

    # 3. Flat logo (simple cutout, good for B&W)
    print("3. Flat logo (octagon with A cutout, filled)...")
    flat_logo = make_flat_logo_sketch(diameter)
    export_sketch_svg(flat_logo, OUTPUT_DIR / "amalgam_logo_flat.svg", fill=True)

    # 4. Outline logo (matches 3D appearance)
    print("4. Outline logo (with circle and outline effect, filled)...")
    outline_logo = make_outline_logo_sketch(diameter)
    export_sketch_svg(outline_logo, OUTPUT_DIR / "amalgam_logo_outline.svg", fill=True)

    # 5. Multi-color logo (black octagon, white recess, black A)
    print("5. Multi-color logo (black/white/black layers)...")
    octagon, recess, a_shape = make_recess_logo_parts(diameter)
    export_multicolor_svg(octagon, recess, a_shape, OUTPUT_DIR / "amalgam_logo_bw.svg")

    print()
    print("=" * 60)
    print("Export Complete")
    print("=" * 60)
    print()
    print("Files created:")
    print(f"  {OUTPUT_DIR}/amalgam_a.svg            - Stylized A only")
    print(f"  {OUTPUT_DIR}/amalgam_octagon.svg      - Octagon outline only")
    print(f"  {OUTPUT_DIR}/amalgam_logo_flat.svg    - Simple logo (good for B&W)")
    print(f"  {OUTPUT_DIR}/amalgam_logo_outline.svg - Full logo with outline effect")
    print(f"  {OUTPUT_DIR}/amalgam_logo_bw.svg      - Multi-color (black octagon, white recess, black A)")
    print()
    print("To convert to PNG with transparent background:")
    print("  inkscape -w 512 -h 512 amalgam_logo_flat.svg -o logo_512.png")
    print("  # or use any vector editor (Inkscape, Illustrator, Figma)")
    print()


# =============================================================================
# Main
# =============================================================================

def main():
    export_all_variants()


if __name__ == "__main__":
    main()
