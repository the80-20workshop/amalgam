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
- Web: Brand-colored with chamfer border (for website)

Usage:
    python utilities/export_logo.py
    # or from repo root:
    python cad/utilities/export_logo.py

Outputs to: cad/exports/logo/
Copies web logo to: docs/images/
"""

import shutil
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
from amalgam.lib.logo import (
    SIDES,
    OCTAGON_ROTATION,
    A_SIZE_RATIO,
    A_Y_OFFSET_RATIO,
    CIRCLE_DIAMETER_RATIO,
    CIRCLE_Y_OFFSET_RATIO,
    EDGE_CHAMFER,
    OUTER_FILLET,
    DIAMETER as LOGO_DIAMETER,
)

# =============================================================================
# Configuration
# =============================================================================

OUTPUT_DIR = Path(__file__).parent.parent / "exports" / "logo"
DOCS_IMAGES_DIR = Path(__file__).parent.parent.parent / "docs" / "images"

# Default sizes
DIAMETER = 100 * MM      # Export size (mm) - large for quality
THICKNESS = 10 * MM      # For 3D projection (affects SVG shading)

# Brand palette (from ADR-029)
BRAND_COLORS = {
    "body": (74, 74, 74),       # #4A4A4A - Dark Grey
    "recess": (255, 255, 255),  # #FFFFFF - White
    "chamfer": (90, 90, 90),    # #5A5A5A - Lighter grey for chamfer highlight
}

# Derived from logo.py parameters — no magic numbers.
# The chamfer + fillet create the visible border in the 3D model.
CHAMFER_RATIO = EDGE_CHAMFER / LOGO_DIAMETER       # Chamfer inset as ratio of diameter
BORDER_RATIO = (EDGE_CHAMFER + OUTER_FILLET) / LOGO_DIAMETER  # Full border (chamfer + fillet)


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
        circle_diameter = diameter * CIRCLE_DIAMETER_RATIO
        circle_y_offset = diameter * CIRCLE_Y_OFFSET_RATIO
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

def make_layered_logo(
    diameter: float = DIAMETER,
    match_3d: bool = True,
) -> tuple[Sketch, Sketch, Sketch]:
    """
    Create logo as three stacked layers for multi-color export.

    Simple approach: three shapes layered bottom-to-top.
    All dimensions come directly from logo.py parameters.

    Args:
        match_3d: If True, draw the octagon at the chamfer-edge size
                  (EDGE_CHAMFER inset) to match the 3D top-down view.

    Returns:
        (octagon, circle, a) - three sketches, layered bottom to top:
        - octagon: Background shape (black)
        - circle: Middle layer (white)
        - a: Foreground shape (black)
    """
    # Layer 1: Octagon background
    if match_3d:
        oct_diameter = diameter * (1 - 2 * CHAMFER_RATIO)
    else:
        oct_diameter = diameter
    octagon = make_octagon_sketch(oct_diameter)

    # Layer 2: Circle (dimensions from logo.py ratios)
    circle_diameter = diameter * CIRCLE_DIAMETER_RATIO
    circle_y_offset = diameter * CIRCLE_Y_OFFSET_RATIO
    with BuildSketch() as circle_sk:
        with Locations([(0, circle_y_offset)]):
            Circle(radius=circle_diameter / 2)
    circle = circle_sk.sketch

    # Layer 3: Stylized A (positioned)
    a_size = diameter * A_SIZE_RATIO
    a_y_offset = diameter * A_Y_OFFSET_RATIO
    a_sketch = make_stylized_a_sketch(height=a_size)
    with BuildSketch() as a_positioned:
        with Locations([(0, a_y_offset)]):
            add(a_sketch)
    a_final = a_positioned.sketch

    return octagon, circle, a_final


def export_multicolor_svg(
    octagon: Sketch,
    recess: Sketch,
    a_shape: Sketch,
    filepath: Path,
    colors: dict = None,
):
    """
    Export multi-color logo as SVG.

    Args:
        colors: Dict with 'body' and 'recess' keys, each an (R, G, B) tuple.
                Defaults to pure black/white for print use.
    """
    from build123d import ExportSVG, Unit

    if colors is None:
        colors = {"body": (0, 0, 0), "recess": (255, 255, 255)}

    body = colors["body"]
    recess_color = colors["recess"]

    exporter = ExportSVG(
        unit=Unit.MM,
        scale=1,
        margin=5,
        line_weight=0.1,  # Thin lines
    )

    # Add layers with different colors
    exporter.add_layer("octagon", fill_color=body, line_color=body)
    exporter.add_layer("recess", fill_color=recess_color, line_color=recess_color)
    exporter.add_layer("a", fill_color=body, line_color=body)

    # Add shapes to their layers
    exporter.add_shape(octagon, layer="octagon")
    exporter.add_shape(recess, layer="recess")
    exporter.add_shape(a_shape, layer="a")

    exporter.write(str(filepath))
    print(f"Exported: {filepath}")


# =============================================================================
# SVG Helpers
# =============================================================================

def _octagon_svg_path(diameter: float) -> str:
    """Compute SVG path data for a regular octagon at the given across-flats diameter."""
    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / SIDES)

    points = []
    for i in range(SIDES):
        angle = math.radians(OCTAGON_ROTATION + i * (360 / SIDES))
        x = circumradius * math.cos(angle)
        y = circumradius * math.sin(angle)
        points.append((x, y))

    path = f"M {points[0][0]:.6f},{points[0][1]:.6f}"
    for p in points[1:]:
        path += f" L {p[0]:.6f},{p[1]:.6f}"
    path += " Z"
    return path


def _add_chamfer_border(svg_content: str, diameter: float, color: tuple) -> str:
    """
    Add a chamfer-edge line to an SVG, matching the 3D logo's chamfered border.

    The 3D logo has chamfered top edges that create a visible border between
    the octagon perimeter and the recessed circle. This adds an inner octagon
    stroke to replicate that visual in 2D.
    """
    inner_diameter = diameter * (1 - 2 * BORDER_RATIO)
    border_path = _octagon_svg_path(inner_diameter)

    r, g, b = color
    border_element = (
        f'    <g id="chamfer">\n'
        f'      <path fill="none" stroke="rgb({r},{g},{b})" '
        f'stroke-width="0.5" d="{border_path}" />\n'
        f'    </g>\n'
    )

    # Insert before the closing </g> of the transform group
    return svg_content.replace("  </g>\n</svg>", f"{border_element}  </g>\n</svg>")


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


def export_web_logo(diameter: float = DIAMETER) -> Path:
    """
    Export brand-colored logo with chamfer border for website use.

    Uses the brand palette from ADR-029 and adds a chamfer-edge inner
    octagon line to match the visual proportions of the 3D model.
    """
    filepath = OUTPUT_DIR / "amalgam_logo_web.svg"

    # Generate layered sketches (octagon at chamfer-edge size by default)
    octagon, circle, a_shape = make_layered_logo(diameter)

    # Export with brand colors
    export_multicolor_svg(
        octagon, circle, a_shape, filepath,
        colors={"body": BRAND_COLORS["body"], "recess": BRAND_COLORS["recess"]},
    )

    # Post-process: add chamfer border line
    svg_content = filepath.read_text()
    svg_content = _add_chamfer_border(svg_content, diameter, BRAND_COLORS["chamfer"])
    filepath.write_text(svg_content)

    return filepath


def copy_to_docs():
    """Copy the web logo to docs/images/ for Quarto site use."""
    DOCS_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    src = OUTPUT_DIR / "amalgam_logo_web.svg"
    dst = DOCS_IMAGES_DIR / "amalgam_logo_web.svg"

    if src.exists():
        shutil.copy2(src, dst)
        print(f"Copied: {dst}")
    else:
        print(f"Warning: {src} not found, skipping docs copy")


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
    print("5. Multi-color logo (black/white/black layers, match 3D)...")
    octagon, circle, a_shape = make_layered_logo(diameter)
    export_multicolor_svg(octagon, circle, a_shape, OUTPUT_DIR / "amalgam_logo_bw.svg")

    # 6. Web logo (brand colors + chamfer border)
    print("6. Web logo (brand colors, chamfer border)...")
    export_web_logo(diameter)

    # Copy web logo to docs/images/ for Quarto site
    print()
    print("Copying web logo to docs/images/...")
    copy_to_docs()

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
    print(f"  {OUTPUT_DIR}/amalgam_logo_bw.svg      - Multi-color (black/white)")
    print(f"  {OUTPUT_DIR}/amalgam_logo_web.svg     - Web logo (brand colors)")
    print(f"  {DOCS_IMAGES_DIR}/amalgam_logo_web.svg - Copy for Quarto site")
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
