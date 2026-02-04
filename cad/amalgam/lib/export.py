"""
Amalgam Export Module

Centralized export functionality for all part scripts.
Supports multiple output formats and technical drawings.

Supported 3D formats:
- STL: Standard 3D printing format
- STEP: CAD interchange (Fusion 360, FreeCAD, SolidWorks)
- 3MF: Modern slicer format with metadata
- BREP: build123d native (exact geometry)
- glTF: Web/visualization (3D viewers)

Supported 2D formats:
- DXF: CAD interchange, laser cutting
- SVG: Vector graphics, documentation

Technical drawings:
- Orthographic projections (front, top, side)
- Isometric view
- Export as SVG and PDF

Usage:
    from amalgam.lib.export import export_part, export_drawing

    part = make_my_part()
    export_part(part, "my_part")  # Uses config default format
    export_part(part, "my_part", formats=["stl", "step"])  # Specific formats
    export_drawing(part, "my_part")  # Technical drawing
"""

import math
from pathlib import Path
from typing import Union

from build123d import (
    Part, Compound, Shape, Sketch,
    export_stl, export_step, export_brep, export_gltf,
    Mesher, ExportDXF, ExportSVG,
    Unit, Plane, Vector, Color,
    section,
)

# =============================================================================
# Configuration
# =============================================================================

import os

# Try to import config, fall back to defaults
try:
    from config import EXPORT_FORMAT as _CONFIG_FORMAT
    from config import EXPORT_DRAWINGS as _CONFIG_DRAWINGS
except ImportError:
    _CONFIG_FORMAT = "stl"
    _CONFIG_DRAWINGS = False

# Environment variables take precedence over config
# This allows CLI flags (--format) to override config.py
EXPORT_FORMAT = os.environ.get("EXPORT_FORMAT", _CONFIG_FORMAT)
EXPORT_DRAWINGS = os.environ.get("EXPORT_DRAWINGS", str(_CONFIG_DRAWINGS)).lower() in ("true", "1", "yes")

# Supported formats
SUPPORTED_3D_FORMATS = {"stl", "step", "3mf", "brep", "gltf"}
SUPPORTED_2D_FORMATS = {"dxf", "svg"}
ALL_FORMATS = SUPPORTED_3D_FORMATS | SUPPORTED_2D_FORMATS

# File extensions
FORMAT_EXTENSIONS = {
    "stl": ".stl",
    "step": ".step",
    "3mf": ".3mf",
    "brep": ".brep",
    "gltf": ".glb",  # Binary glTF
    "dxf": ".dxf",
    "svg": ".svg",
}

# Default export directory (relative to cad/)
DEFAULT_EXPORT_DIR = Path("exports")


# =============================================================================
# Export Directory Management
# =============================================================================

def get_export_dir(format_name: str, base_dir: Path = None) -> Path:
    """Get the export directory for a specific format."""
    if base_dir is None:
        # Assume we're in cad/ directory
        base_dir = DEFAULT_EXPORT_DIR

    export_dir = base_dir / format_name
    export_dir.mkdir(parents=True, exist_ok=True)
    return export_dir


def get_export_path(name: str, format_name: str, base_dir: Path = None) -> Path:
    """Get the full export path for a part in a specific format."""
    export_dir = get_export_dir(format_name, base_dir)
    extension = FORMAT_EXTENSIONS.get(format_name, f".{format_name}")
    return export_dir / f"{name}{extension}"


# =============================================================================
# 3D Export Functions
# =============================================================================

def export_to_stl(part: Part, filepath: Path, tolerance: float = 0.001) -> None:
    """Export part to STL format."""
    export_stl(part, str(filepath), tolerance=tolerance)


def export_to_step(part: Part, filepath: Path) -> None:
    """Export part to STEP format (best for CAD interchange)."""
    export_step(part, str(filepath), unit=Unit.MM)


def export_to_3mf(part: Part, filepath: Path, name: str = "part") -> None:
    """Export part to 3MF format using Mesher class."""
    mesher = Mesher(unit=Unit.MM)
    mesher.add_shape(part)
    # Note: add_meta_data API may vary by build123d version
    # Try simple write without metadata if it fails
    try:
        mesher.add_meta_data("", "Application", "Amalgam CAD (build123d)", "xs:string", False)
        mesher.add_meta_data("", "Title", name, "xs:string", False)
        # Add brand color hint for slicers that support it
        try:
            from amalgam.lib.brand import PALETTE
            mesher.add_meta_data("", "DisplayColor", PALETTE["body"], "xs:string", False)
        except ImportError:
            pass
    except TypeError:
        # Older API or different signature - skip metadata
        pass
    mesher.write(str(filepath))


def export_to_brep(part: Part, filepath: Path) -> None:
    """Export part to BREP format (build123d native, exact geometry)."""
    export_brep(part, str(filepath))


def export_to_gltf(part: Part, filepath: Path) -> None:
    """Export part to glTF format (binary .glb for web/visualization)."""
    # Apply brand body color if part has no color set
    if part.color is None:
        try:
            from amalgam.lib.brand import get_body_color
            part.color = get_body_color()
        except ImportError:
            pass
    export_gltf(part, str(filepath), binary=True, unit=Unit.MM)


# =============================================================================
# 2D Export Functions
# =============================================================================

def export_to_dxf(
    shape: Union[Part, Sketch],
    filepath: Path,
    projection_plane: str = "top"
) -> None:
    """
    Export 2D projection to DXF format.

    Args:
        shape: Part or Sketch to export
        filepath: Output path
        projection_plane: "top", "front", or "side"
    """
    exporter = ExportDXF(unit=Unit.MM)

    if isinstance(shape, Sketch):
        exporter.add_shape(shape)
    else:
        # Create 2D projection of 3D part
        projected = _project_part(shape, projection_plane)
        if projected:
            exporter.add_shape(projected)

    exporter.write(str(filepath))


def export_to_svg(
    shape: Union[Part, Sketch],
    filepath: Path,
    projection_plane: str = "top"
) -> None:
    """
    Export 2D projection to SVG format.

    Args:
        shape: Part or Sketch to export
        filepath: Output path
        projection_plane: "top", "front", or "side"
    """
    exporter = ExportSVG(
        unit=Unit.MM,
        margin=5,
        line_weight=0.3,
        line_color=(0, 0, 0),
    )

    if isinstance(shape, Sketch):
        exporter.add_shape(shape)
    else:
        # Create 2D projection of 3D part
        projected = _project_part(shape, projection_plane)
        if projected:
            exporter.add_shape(projected)

    exporter.write(str(filepath))


def _project_part(part: Part, plane: str = "top"):
    """
    Create a 2D projection of a 3D part.

    Args:
        part: The 3D part to project
        plane: "top" (XY), "front" (XZ), or "side" (YZ)
    """
    try:
        # Get bounding box center for section plane
        bbox = part.bounding_box()
        center = bbox.center()

        if plane == "top":
            section_plane = Plane.XY.offset(center.Z)
        elif plane == "front":
            section_plane = Plane.XZ.offset(center.Y)
        elif plane == "side":
            section_plane = Plane.YZ.offset(center.X)
        else:
            section_plane = Plane.XY.offset(center.Z)

        # Create section
        result = section(part, section_plane)
        return result
    except Exception as e:
        print(f"  Warning: Could not create {plane} projection: {e}")
        return None


# =============================================================================
# Main Export Function
# =============================================================================

def export_part(
    part: Part,
    name: str,
    formats: Union[str, list] = None,
    base_dir: Path = None,
    include_drawings: bool = None,
) -> dict:
    """
    Export a part to one or more formats.

    This is the main export function that should be called by part scripts.

    Args:
        part: The build123d Part to export
        name: Base name for the exported files (e.g., "maker_coin")
        formats: Format(s) to export. Options:
                 - None: Use config default (EXPORT_FORMAT)
                 - "stl", "step", etc.: Single format
                 - ["stl", "step"]: Multiple formats
                 - "all": All supported 3D formats
        base_dir: Base directory for exports (default: cad/exports/)
        include_drawings: Generate technical drawings (default: from config)

    Returns:
        dict: Mapping of format -> filepath for successful exports
    """
    # Determine formats to export
    if formats is None:
        formats = EXPORT_FORMAT  # Use config/env default

    # Handle "all" keyword
    if formats == "all":
        formats = list(SUPPORTED_3D_FORMATS)
    elif isinstance(formats, str):
        formats = [formats]

    # Validate formats
    formats = [f.lower() for f in formats]
    invalid = set(formats) - SUPPORTED_3D_FORMATS
    if invalid:
        print(f"  Warning: Unsupported formats ignored: {invalid}")
        formats = [f for f in formats if f in SUPPORTED_3D_FORMATS]

    if not formats:
        formats = ["stl"]  # Fallback to STL

    # Determine if we should generate drawings
    if include_drawings is None:
        include_drawings = EXPORT_DRAWINGS

    # Export to each format
    results = {}
    export_funcs = {
        "stl": export_to_stl,
        "step": export_to_step,
        "3mf": lambda p, f: export_to_3mf(p, f, name),
        "brep": export_to_brep,
        "gltf": export_to_gltf,
    }

    for fmt in formats:
        filepath = get_export_path(name, fmt, base_dir)
        try:
            export_funcs[fmt](part, filepath)
            results[fmt] = filepath
            print(f"  Exported: {filepath}")
        except Exception as e:
            print(f"  Error exporting {fmt}: {e}")

    # Generate technical drawings if requested
    if include_drawings:
        drawing_results = export_drawing(part, name, base_dir)
        results.update(drawing_results)

    return results


# =============================================================================
# Technical Drawing Export
# =============================================================================

def export_drawing(
    part: Part,
    name: str,
    base_dir: Path = None,
    views: list = None,
) -> dict:
    """
    Export technical drawing with multiple orthographic views.

    Creates a drawing sheet with:
    - Front elevation (XZ plane)
    - Top view / plan (XY plane)
    - Side elevation (YZ plane)
    - Isometric view (optional)

    Exports as both SVG and PDF.

    Args:
        part: The 3D part to draw
        name: Base name for the drawing files
        base_dir: Base directory for exports
        views: List of views to include (default: ["front", "top", "side", "iso"])

    Returns:
        dict: Mapping of format -> filepath for drawing exports
    """
    if views is None:
        views = ["front", "top", "side", "iso"]

    results = {}
    drawings_dir = get_export_dir("drawings", base_dir)

    # Create individual view SVGs
    for view in views:
        if view == "iso":
            # Isometric view requires different approach
            svg_path = drawings_dir / f"{name}_iso.svg"
            try:
                _export_isometric_view(part, svg_path)
                results[f"drawing_iso_svg"] = svg_path
                print(f"  Exported: {svg_path}")
            except Exception as e:
                print(f"  Warning: Could not create isometric view: {e}")
        else:
            svg_path = drawings_dir / f"{name}_{view}.svg"
            try:
                export_to_svg(part, svg_path, projection_plane=view)
                results[f"drawing_{view}_svg"] = svg_path
                print(f"  Exported: {svg_path}")
            except Exception as e:
                print(f"  Warning: Could not create {view} view: {e}")

    # Create combined drawing sheet
    try:
        combined_svg = drawings_dir / f"{name}_drawing.svg"
        _create_drawing_sheet(part, name, combined_svg, views)
        results["drawing_sheet_svg"] = combined_svg
        print(f"  Exported: {combined_svg}")

        # Convert to PDF if possible
        pdf_path = drawings_dir / f"{name}_drawing.pdf"
        if _svg_to_pdf(combined_svg, pdf_path):
            results["drawing_sheet_pdf"] = pdf_path
            print(f"  Exported: {pdf_path}")
    except Exception as e:
        print(f"  Warning: Could not create drawing sheet: {e}")

    return results


def _export_isometric_view(part: Part, filepath: Path) -> None:
    """Export an isometric view of the part."""
    # Isometric projection angles
    # Standard isometric: rotate 45° around vertical, then ~35.264° down
    from build123d import project_to_viewport

    # Camera position for isometric view
    # Looking from front-right-top corner
    viewport_origin = Vector(1, 1, 1).normalized() * 1000

    try:
        visible, hidden = project_to_viewport(
            part,
            viewport_origin=viewport_origin,
        )

        exporter = ExportSVG(
            unit=Unit.MM,
            margin=10,
            line_weight=0.3,
            line_color=(0, 0, 0),
        )

        # Add visible edges
        if visible:
            exporter.add_layer("visible", line_weight=0.3, line_color=(0, 0, 0))
            for edge in visible.edges() if hasattr(visible, 'edges') else [visible]:
                exporter.add_shape(edge, layer="visible")

        # Add hidden edges (dashed)
        if hidden:
            from build123d import LineType
            exporter.add_layer("hidden", line_weight=0.15, line_color=(128, 128, 128),
                             line_type=LineType.ISO_DASH)
            for edge in hidden.edges() if hasattr(hidden, 'edges') else [hidden]:
                exporter.add_shape(edge, layer="hidden")

        exporter.write(str(filepath))
    except Exception as e:
        # Fallback: just export a simple top-down view
        print(f"  Note: Isometric projection failed, using top view: {e}")
        export_to_svg(part, filepath, projection_plane="top")


def _create_drawing_sheet(
    part: Part,
    name: str,
    filepath: Path,
    views: list,
) -> None:
    """
    Create a combined drawing sheet with multiple views.

    Layout:
    ┌─────────────┬─────────────┐
    │   TOP       │  ISOMETRIC  │
    │             │             │
    ├─────────────┼─────────────┤
    │   FRONT     │    SIDE     │
    │             │             │
    └─────────────┴─────────────┘
    """
    # For now, create a simple combined SVG
    # A more sophisticated version would use proper drawing sheet layout

    bbox = part.bounding_box()
    part_size = max(bbox.size.X, bbox.size.Y, bbox.size.Z)

    # Sheet size (A4 landscape in mm)
    sheet_width = 297
    sheet_height = 210
    margin = 15
    title_height = 20

    # View areas
    view_width = (sheet_width - 3 * margin) / 2
    view_height = (sheet_height - 3 * margin - title_height) / 2

    # Start SVG
    svg_lines = [
        f'<?xml version="1.0" encoding="utf-8"?>',
        f'<svg width="{sheet_width}mm" height="{sheet_height}mm" '
        f'viewBox="0 0 {sheet_width} {sheet_height}" '
        f'xmlns="http://www.w3.org/2000/svg">',
        f'  <style>',
        f'    .title {{ font-family: Arial, sans-serif; font-size: 8px; }}',
        f'    .view-label {{ font-family: Arial, sans-serif; font-size: 5px; fill: #666; }}',
        f'    .border {{ fill: none; stroke: #000; stroke-width: 0.5; }}',
        f'  </style>',
        f'',
        f'  <!-- Drawing border -->',
        f'  <rect x="5" y="5" width="{sheet_width-10}" height="{sheet_height-10}" class="border"/>',
        f'',
        f'  <!-- Title block -->',
        f'  <text x="{sheet_width/2}" y="{sheet_height - 8}" text-anchor="middle" class="title">',
        f'    {name.upper()} - Amalgam Project',
        f'  </text>',
        f'',
    ]

    # View positions
    positions = {
        "top": (margin, margin, "TOP VIEW"),
        "iso": (margin + view_width + margin, margin, "ISOMETRIC"),
        "front": (margin, margin + view_height + margin, "FRONT VIEW"),
        "side": (margin + view_width + margin, margin + view_height + margin, "SIDE VIEW"),
    }

    for view, (x, y, label) in positions.items():
        if view in views:
            svg_lines.extend([
                f'  <!-- {label} -->',
                f'  <rect x="{x}" y="{y}" width="{view_width}" height="{view_height}" '
                f'fill="none" stroke="#ccc" stroke-width="0.25"/>',
                f'  <text x="{x + 2}" y="{y + view_height - 2}" class="view-label">{label}</text>',
                f'',
            ])

    svg_lines.append('</svg>')

    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write('\n'.join(svg_lines))


def _svg_to_pdf(svg_path: Path, pdf_path: Path) -> bool:
    """
    Convert SVG to PDF using available tools.

    Tries (in order):
    1. cairosvg (Python library)
    2. inkscape (CLI)
    3. rsvg-convert (CLI)

    Returns True if successful, False otherwise.
    """
    # Try cairosvg
    try:
        import cairosvg
        cairosvg.svg2pdf(url=str(svg_path), write_to=str(pdf_path))
        return True
    except ImportError:
        pass
    except Exception as e:
        print(f"  Note: cairosvg failed: {e}")

    # Try inkscape
    try:
        import subprocess
        result = subprocess.run(
            ["inkscape", str(svg_path), "--export-type=pdf", f"--export-filename={pdf_path}"],
            capture_output=True,
            timeout=30
        )
        if result.returncode == 0 and pdf_path.exists():
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    except Exception as e:
        print(f"  Note: inkscape failed: {e}")

    # Try rsvg-convert
    try:
        import subprocess
        result = subprocess.run(
            ["rsvg-convert", "-f", "pdf", "-o", str(pdf_path), str(svg_path)],
            capture_output=True,
            timeout=30
        )
        if result.returncode == 0 and pdf_path.exists():
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    except Exception as e:
        print(f"  Note: rsvg-convert failed: {e}")

    print("  Note: PDF conversion requires cairosvg, inkscape, or rsvg-convert")
    return False


# =============================================================================
# Convenience Functions
# =============================================================================

def get_supported_formats() -> dict:
    """Return information about supported export formats."""
    return {
        "3d": {
            "stl": "Standard 3D printing format (mesh)",
            "step": "CAD interchange - Fusion 360, FreeCAD, SolidWorks (BREP)",
            "3mf": "Modern slicer format with metadata (mesh)",
            "brep": "build123d native format (exact geometry)",
            "gltf": "Web/3D viewer format (mesh)",
        },
        "2d": {
            "dxf": "CAD interchange, laser cutting",
            "svg": "Vector graphics, documentation",
        },
        "drawings": {
            "svg": "Technical drawing sheet",
            "pdf": "Technical drawing sheet (requires converter)",
        },
    }


def print_format_help():
    """Print help about available export formats."""
    formats = get_supported_formats()
    print("\nSupported Export Formats:")
    print("=" * 50)

    print("\n3D Formats:")
    for fmt, desc in formats["3d"].items():
        print(f"  {fmt:6} - {desc}")

    print("\n2D Formats:")
    for fmt, desc in formats["2d"].items():
        print(f"  {fmt:6} - {desc}")

    print("\nTechnical Drawings:")
    for fmt, desc in formats["drawings"].items():
        print(f"  {fmt:6} - {desc}")

    print("\nUsage:")
    print("  export_part(part, 'name')              # Use config default")
    print("  export_part(part, 'name', 'step')      # Single format")
    print("  export_part(part, 'name', ['stl','step'])  # Multiple formats")
    print("  export_part(part, 'name', 'all')       # All 3D formats")
    print()
