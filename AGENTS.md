# AGENTS.md

## Amalgam CAD Project - Agent Guidelines

This document provides coding standards and workflows for AI agents working on this repository.

---

## Quick Commands

### Build/Test
```bash
cd cad

# Test single part (fastest iteration)
.venv/bin/python amalgam/parts/frame/corner_standard.py

# Build all parts
./build.sh build_all

# Build specific part
./build.sh build corner_standard

# Build with specific format
./build.sh build corner_standard --format step

# List parts
./build.sh list
```

### Lint/Format
```bash
cd cad
ruff check .      # Lint
ruff format .     # Format
pytest             # Run tests
```

---

## Code Style

### File Structure
```
cad/
├── amalgam/
│   ├── lib/              # Shared components
│   │   ├── export.py     # Multi-format export system
│   │   ├── corner.py     # Corner components
│   │   └── logo.py       # Logo generation
│   └── parts/            # Individual parts (by category)
│       ├── frame/        # Frame parts
│       ├── motion/       # Motion system parts
│       ├── extruder/     # Extruder parts
│       ├── bed/          # Bed parts
│       ├── calibration/  # Calibration prints
│       └── victory/      # Fun/reward parts
├── exports/              # Generated output (by format)
│   ├── stl/
│   ├── step/
│   ├── 3mf/
│   └── drawings/
├── config.py.example     # Reference config
├── config.py             # User config (gitignored)
└── build.sh              # Build script
```

### Import Pattern (parts/)
```python
from amalgam.lib.export import export_part
from amalgam.lib.corner import make_standard_corner

try:
    from config import *
except ImportError:
    print("ERROR: config.py not found")
    print("")
    print("Please run: ./configure.py")
    print("")
    sys.exit(1)

def main():
    # ... generate part ...
    export_part(part, "my_part_name")  # Uses config default format

if __name__ == "__main__":
    main()
```

### Naming
- Files: `snake_case.py`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE` (from config)
- Exports: Match part name (`corner_standard.py` → `exports/stl/corner_standard.stl`)

### Config Usage
**Always use config values - no fallbacks for dimensions:**
```python
# CORRECT
corner = make_standard_corner(
    corner_size=CORNER_SIZE,
    m10_fit_dia=M10_FIT_DIA,
)

# INCORRECT (hardcoded)
corner = make_standard_corner(corner_size=50.0, m10_fit_dia=10.5)
```

### build123d Patterns
```python
# Create and subtract holes
corner = Box(size, size, size)
hole = Cylinder(dia/2, height)
hole = hole.moved(Location((x, y, z)))
corner -= hole

# Rotate (NOT .rotated())
hole = hole.rotate(Axis.Z, 90)
```

**Key methods:** `Box()`, `Cylinder()`, `.moved()`, `.rotate()`, `Mode.SUBTRACT`, `Plane.XZ/YZ`

---

## Export System

The multi-format export system supports STL, STEP, 3MF, BREP, glTF, DXF, SVG, and technical drawings.

```python
from amalgam.lib.export import export_part

# Default format (from config.py or STL)
export_part(part, "my_part")

# Specific format(s)
export_part(part, "my_part", formats=["stl", "step"])

# All 3D formats
export_part(part, "my_part", formats="all")
```

Output goes to `cad/exports/<format>/` (e.g., `cad/exports/stl/my_part.stl`).

---

## Common Pitfalls

1. Missing config.py → Exit with error (no fallbacks)
2. Wrong import path → Use `from amalgam.lib.<module> import ...`
3. Export location → Use `export_part()`, not direct `export_stl()`
4. Method names → Use `.rotate()`, not `.rotated()`
5. Hardcoded dims → Always use `config.py` for fit parameters

---

## Version

- Python: 3.10-3.13 (NOT 3.14+)
- build123d: 0.9.0+
- numpy: 1.20.0+
