# Amalgam CAD Directory

This directory contains all CAD-related files for Amalgam 3D printer project.

## Quick Decision Guide

| Situation | What to Run |
|-----------|--------------|
| New user, first clone | `./setup.sh` (creates config + builds) |
| Have config.py, just build | `./build.sh build_all` |
| Want to change config | `./configure.py` then `./build.sh build_all` |
| Just updated repo | `./build.sh build_all` |

## Quick Start - For Testing

If you want to test with only the existing parts:

```bash
./build.sh build_all
```

## Quick Start - Full Setup

### Option 1: First-Time Setup (Recommended for New Users)

**Best for:** New users, first time cloning the repo

```bash
./setup.sh
```

The setup wizard will:
1. Detect your operating system (Linux/macOS/Windows)
2. Check for Python 3.9+ installation
3. Optionally install uv (fast Python package manager)
4. Set up Python environment
5. Install required packages
6. Run configuration wizard (creates `config.py`)
7. Build all parts

**Cross-platform support:**
- macOS: Works with Homebrew Python or official installer
- Linux: Works with system Python or distribution packages
- Windows: Works via Git Bash, WSL, or PowerShell

**Graceful failure:**
- If Python is not found, gives platform-specific installation instructions
- Script does NOT install Python automatically (~100-200MB)
- Always offers web interface as alternative (coming soon)

**After this:** You have `config.py` created and all parts built.

### Option 2: Just Build Parts

**Best for:** Already have `config.py` from previous build

```bash
./build.sh build_all
```

**What happens:**
- Checks for `.venv` and activates it if needed
- Installs dependencies if not found
- Builds all parts using your existing `config.py`

**Note:** If `config.py` doesn't exist, you'll get an error. Use `./configure.py` to create it.

### Option 3: Change Configuration

**Best for:** Want to modify printer settings

```bash
# Just run configuration wizard (backs up existing config)
./configure.py

# Then rebuild with new settings
./build.sh build_all
```

**What happens:**
- Asks configuration questions interactively
- Backs up existing `config.py` to `config.py.backup`
- Creates new `config.py` with your changes
- `build.sh` will use the new config

### Option 4: Manual Control

**Best for:** Experienced users, want full control

```bash
cd cad

# Create and activate virtual environment (if needed)
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies (optional - build.sh will do this if missing)
# Uses pyproject.toml (modern standard)
pip install -e .

# Run configuration wizard (or edit config.py directly)
./configure.py

# Build all parts
./build.sh build_all
```

**Note:** The build script automatically:
- Checks for `.venv` and activates it if needed
- Installs dependencies from pyproject.toml if not found
- Uses `uv` if available for faster installs

## Configuration

Three ways to configure:

1. **Interactive wizard** (recommended for new users):
   ```bash
   ./configure.py
   ```
   - Asks questions step by step
   - Backs up existing config to `config.py.backup`

2. **Manual edit**:
   - Edit `config.py` directly
   - Reference `config.py.example` for all available options

3. **Example file**:
   - `config.py.example` shows full configuration structure
   - Copy to `config.py` and customize

**Important:** `config.py` is ignored by git (keep your settings private).
Use `config.py.example` as reference for all available settings.

Key configuration parameters:
- `BUILD_VOLUME` - X, Y, Z dimensions
- `M12_FIT_DIA` - M12 rod diameter with lumpy factor
- `EXTRUDER_TYPE` - "WADE" or other
- `TRIPLE_Z` - Enable/disable triple Z system
- `Z_MOUNT_PATTERN` - Z-motor mounting configuration

## Export Formats

By default, parts are exported as STL. You can export in multiple formats:

```bash
./build.sh build maker_coin                    # Default (STL)
./build.sh build maker_coin --format step      # CAD interchange
./build.sh build maker_coin --format all       # All formats
./build.sh build maker_coin --drawings         # Include technical drawings
./build.sh formats                             # Show all available formats
```

**Available formats:**
| Format | Extension | Use Case |
|--------|-----------|----------|
| STL | `.stl` | 3D printing (default) |
| STEP | `.step` | CAD interchange (Fusion 360, FreeCAD, SolidWorks) |
| 3MF | `.3mf` | Modern slicers with metadata |
| BREP | `.brep` | build123d native (exact geometry) |
| glTF | `.glb` | Web viewers, 3D visualization |

**Technical drawings:** Front, top, side orthographic projections as SVG and combined PDF.

**Configure default format** in `config.py`:
```python
EXPORT_FORMAT = "stl"      # Options: stl, step, 3mf, brep, gltf, all
EXPORT_DRAWINGS = False    # Generate technical drawings
```

## Directory Structure

```
cad/
├── amalgam/              # Python package
│   ├── lib/              # Shared libraries (logo, export, corners)
│   └── parts/            # Part scripts by category
│       ├── calibration/  # First layer grid, Prusa live Z
│       ├── frame/        # Corner brackets
│       └── victory/      # Maker coin, fidget bolt
├── exports/              # Generated files (gitignored)
│   ├── stl/              # STL files
│   ├── step/             # STEP files
│   ├── 3mf/              # 3MF files
│   ├── brep/             # BREP files
│   ├── gltf/             # glTF files
│   ├── drawings/         # Technical drawings (SVG/PDF)
│   └── logo/             # Brand assets (SVG)
├── utilities/            # Helper scripts
│   ├── download_calibration.py  # Download community calibration prints
│   ├── export_logo.py           # Generate logo SVGs
│   └── list.py                  # List available parts
├── build.sh              # Main build script
├── setup.sh              # First-time setup
├── configure.py          # Configuration wizard
├── config.py             # Your configuration (gitignored)
└── config.py.example     # Reference configuration
```

## Dependencies

- Python 3.9+
- build123d
- numpy

See `pyproject.toml` for specific versions.
