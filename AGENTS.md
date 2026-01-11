# AGENTS.md

## Neo-Darwin CAD Project - Agent Guidelines

This document provides coding standards and workflows for AI agents working on this repository.

---

## Quick Commands

### Build/Test
```bash
cd cad

# Test single part (fastest iteration)
.venv/bin/python parts/corner_standard.py

# Build all parts
./build.sh build_all

# Build specific part
./build.sh build corner_standard

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
├── include/              # Shared components
│   └── *_components.py
├── parts/                # Individual parts
│   └── *.py
├── config.py.example      # Reference config
├── config.py            # User config (gitignored)
└── build.sh             # Build script
```

### Import Pattern (parts/)
```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from include.corner_components import make_standard_corner

try:
    from config import *
except ImportError:
    print("ERROR: config.py not found")
    print("")
    print("Please run: ./configure.py")
    print("")
    sys.exit(1)

def main():
    from build123d import export_stl as export_stl_func
    # ... generate part ...
    export_stl_func(part, "stl/filename.stl")
```

### Naming
- Files: `snake_case.py`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE` (from config)
- STL files: Match part name (`corner_standard.py` → `corner_standard.stl`)

### Config Usage
**Always use config values - no fallbacks for dimensions:**
```python
# CORRECT
corner = make_standard_corner(
    corner_size=CORNER_SIZE,
    m12_fit_dia=M12_FIT_DIA,
)

# INCORRECT (hardcoded)
corner = make_standard_corner(corner_size=50.0, m12_fit_dia=12.5)
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

## Common Pitfalls

1. Missing config.py → Exit with error (no fallbacks)
2. Wrong import path → Use `os.path.dirname(os.path.dirname(__file__))`
3. STL location → Export to `stl/`, not `parts/`
4. Method names → Use `.rotate()`, not `.rotated()`
5. Hardcoded dims → Always use `config.py` for fit parameters

---

## Version

- Python: 3.10-3.13 (NOT 3.14+)
- build123d: 0.9.0+
- numpy: 1.20.0+
