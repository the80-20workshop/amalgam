# ADR-030: Multi-Format Export System

## Status
Accepted

## Context

### The Python Gate Problem

ADR-017 chose build123d (Python BREP) as the CAD system. This is the right choice for parametric design — but it creates a contributor barrier:

```
Want to modify an Amalgam part?
  → Install Python 3.11+
  → Create a virtual environment
  → pip install build123d (which compiles OpenCascade bindings)
  → Learn the build123d API
  → Run the build script
```

Most 3D printer enthusiasts don't write Python. They use visual CAD tools (Fusion 360, FreeCAD, TinkerCAD, Blender) or just import STL files into slicers. Requiring Python to even *look at* a part — let alone modify one — excludes the majority of the maker community.

The RepRap tradition is "download the files and print." Any barrier beyond that costs contributors.

### The Format Landscape

Different users need different formats for different workflows:

| User | Workflow | Needs |
|------|----------|-------|
| **Printer** | Download → slice → print | STL or 3MF |
| **Modifier** | Import → tweak → re-export | STEP (parametric) or STL (mesh) |
| **Designer** | Open in Fusion/FreeCAD → modify geometry | STEP |
| **Viewer** | Preview on GitHub / web | glTF |
| **Laser cutter** | Cut flat parts from sheet | DXF |
| **Documenter** | Generate diagrams / assembly views | SVG |
| **Developer** | Exact geometry round-trip | BREP |

No single format serves all these users. STL-only repos force everyone through the lowest-common-denominator mesh format, losing the parametric precision that build123d provides.

### What Other Projects Do

| Project | Distributes | Consequence |
|---------|------------|-------------|
| Most RepRap projects | STL only | Can't edit without re-modeling from scratch |
| Voron | STL + STEP (manual) | STEP maintained separately, often out of sync |
| Prusa | STL + STEP (manual) | Same sync problem at larger scale |
| Bambu (open parts) | STEP | Good for editors, overkill for printers |

Manual multi-format maintenance is error-prone. Formats drift out of sync. The solution is automated multi-format export from a single source.

### GitHub 3D Preview

GitHub renders `.stl` and `.glb` (binary glTF) files directly in the browser. This means anyone can preview parts without downloading anything — but only if those formats exist in the repository.

## Decision

### Automated Multi-Format Export

Every Amalgam part exports to multiple formats from a single build123d source, via the centralized `amalgam/lib/export.py` module. The default format is configurable; all formats are available on demand.

```python
from amalgam.lib.export import export_part

part = make_my_part()
export_part(part, "my_part")                    # Config default (STL)
export_part(part, "my_part", formats="step")    # Single format
export_part(part, "my_part", formats=["stl", "step", "3mf"])  # Multiple
export_part(part, "my_part", formats="all")     # Everything
```

### Format Hierarchy

Formats are organized by purpose, not by technical sophistication:

#### 3D Formats

| Format | Extension | Purpose | Audience |
|--------|-----------|---------|----------|
| **STL** | `.stl` | 3D printing (universal slicer support) | Everyone who prints |
| **STEP** | `.step` | CAD interchange (Fusion 360, FreeCAD, SolidWorks) | Contributors who modify parts |
| **3MF** | `.3mf` | Modern slicing with metadata (print settings, color) | Slicer users who want richer data |
| **BREP** | `.brep` | build123d native (exact OpenCascade geometry) | Developers extending the CAD system |
| **glTF** | `.glb` | Web visualization (GitHub preview, 3D viewers) | Anyone browsing the repo |

#### 2D Formats

| Format | Extension | Purpose | Audience |
|--------|-----------|---------|----------|
| **DXF** | `.dxf` | Laser cutting, CNC routing (MDF base, jigs) | Makers with CNC/laser access |
| **SVG** | `.svg` | Vector graphics, documentation diagrams | Documentation, assembly guides |

#### Technical Drawings

| Format | Extension | Purpose | Audience |
|--------|-----------|---------|----------|
| **SVG drawing** | `.svg` | Orthographic projections (front, top, side, iso) | Documentation, Quarto integration |
| **PDF drawing** | `.pdf` | Printable technical drawings | Workshop reference |

### Directory Structure

```
cad/exports/
├── stl/          # STL files (default)
├── step/         # STEP files
├── 3mf/          # 3MF files
├── brep/         # BREP files
├── gltf/         # glTF binary (.glb)
├── dxf/          # DXF files
├── svg/          # SVG files
└── drawings/     # Technical drawing sheets
```

Each format gets its own directory. Flat structure within each — no nested subdirectories. Part names are the filename: `corner_standard.stl`, `corner_standard.step`, etc.

### Configuration

Export settings live in `config.py` Section 10:

```python
# Default export format: stl, step, 3mf, brep, gltf, or all
EXPORT_FORMAT = "stl"

# Generate technical drawings (orthographic projections as SVG/PDF)
EXPORT_DRAWINGS = False
```

Environment variables override config, enabling CLI workflows:

```bash
EXPORT_FORMAT=step ./build.sh build corner_standard    # One-off STEP export
EXPORT_FORMAT=all ./build.sh build_all                 # Everything, all formats
EXPORT_DRAWINGS=true ./build.sh build_all              # Include drawings
```

### The "Not Forcing Python" Principle

The export system exists so that the full build123d toolchain is only required for **generating** parts. Once generated, every downstream workflow uses standard formats:

| Task | Requires Python? | Uses |
|------|------------------|------|
| Print a part | No | STL or 3MF |
| Modify a part in Fusion 360 | No | STEP |
| Preview on GitHub | No | glTF |
| Cut an MDF template | No | DXF |
| Read technical drawings | No | SVG or PDF |
| Regenerate from source | **Yes** | build123d |

Python is the *build tool*, not the *distribution format*. This is analogous to how a C project requires a compiler to build, but distributes binaries.

### Metadata in Exports

Where formats support it, exports include project metadata:

- **3MF**: Application name ("Amalgam CAD"), part title, brand display color
- **glTF**: Brand body color applied to mesh for correct rendering in viewers
- **SVG drawings**: Title block with part name and "Amalgam Project" label

This makes exported files self-documenting — a STEP file opened in Fusion 360 or a glTF previewed on GitHub identifies itself as an Amalgam part.

## Consequences

### Benefits

1. **Lowers contribution barrier** — STEP files let visual-CAD users modify parts without learning Python
2. **GitHub discoverability** — glTF files render directly in the repo browser
3. **Slicer flexibility** — STL for compatibility, 3MF for metadata-rich workflows
4. **CNC/laser integration** — DXF enables fabrication of flat parts (jigs, MDF templates)
5. **Documentation automation** — SVG projections feed into Quarto docs without manual screenshots
6. **Single source of truth** — All formats generated from the same build123d source, guaranteed in sync
7. **Future-proof** — Adding a new format means adding one export function, not re-modeling

### Trade-offs

1. **Storage** — Multiple formats per part increases repo size; STL + STEP + glTF for one part ≈ 3x STL alone
2. **Build time** — Exporting all formats is slower than STL-only (STEP and glTF are the slowest)
3. **Maintenance** — The export module itself must be maintained as build123d evolves its API
4. **Drawing quality** — Automated orthographic projections are functional but not as polished as hand-drafted drawings

### What This Enables

- **"Download and print" workflow** — No toolchain required for basic use
- **Visual CAD contributions** — Someone can download STEP, modify in Fusion 360, and submit changes
- **Automated documentation** — Technical drawings generated alongside parts, always current
- **CI/CD validation** — Build pipeline can generate all formats and verify exports succeed
- **Web-based part browsing** — glTF files work in GitHub's built-in 3D viewer

## BOM Implications

None. This is a software/workflow decision. No hardware costs.

The export module depends on:
- `build123d` (already required by ADR-017)
- `cairosvg` or `inkscape` or `rsvg-convert` (optional, for PDF drawing conversion)

## References

- ADR-017: Parametric CAD System (build123d selection)
- ADR-029: Brand Palette & Visual Identity (brand colors in glTF/3MF exports)
- `cad/amalgam/lib/export.py`: Export module implementation
- `cad/config.py` Section 10: Export settings
- [3MF Specification](https://3mf.io/specification/)
- [glTF Specification](https://www.khronos.org/gltf/)
- [GitHub 3D File Viewer](https://docs.github.com/en/repositories/working-with-files/using-files/3d-file-viewer)
