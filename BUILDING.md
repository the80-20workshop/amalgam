# Building Amalgam

> **Safety first:** Before starting any physical assembly, read [SAFETY.md](SAFETY.md). This covers electrical hazards, burn risks, tool safety, and scavenger-specific concerns like inspecting donor wiring.

This guide covers the three build systems:
1. **CAD/STL Generation** - Parametric parts from build123d
2. **Engineering Analysis** - Assess your configuration before building
3. **Documentation** - Config-driven docs with Quarto

## Part 1: Building STL Parts

This section explains how to generate STL files from the parametric CAD files.

## Quick Start

Clone the repository and navigate to the CAD directory:

```bash
git clone https://github.com/amalgam-reprap/amalgam.git
cd amalgam/cad
```

Run the setup wizard:

```bash
./setup.sh
```

The wizard will guide you through:
1. Checking Python installation
2. Setting up virtual environment
3. Installing dependencies
4. Configuring your printer
5. Building all parts

## System Requirements

### Operating Systems
- **Linux**: Ubuntu, Fedora, Arch, Debian, etc.
- **macOS**: 10.14+ (Mojave or later)
- **Windows**: Via Git Bash, WSL, or PowerShell

### Software
- **Python 3.10-3.13**: Required for running build123d scripts
  - [macOS](https://www.python.org/downloads/) - Download installer
  - [Linux](https://docs.python.org/3/installing/) - Use system packages
  - [Windows](https://www.python.org/downloads/) - Check "Add to PATH"

**Note:** Python 3.10-3.13 is required for build123d 0.9.x compatibility. Python 3.14 is not yet supported.

### Hardware
- ~500MB free disk space (for venv + dependencies)
- 4GB+ RAM recommended (build123d can be memory-intensive)

## Build Workflow

### Quick Decision Guide

| Situation | What to Run |
|-----------|--------------|
| New user, no setup yet | `./setup.sh` (everything) |
| Have config.py, want to build | `./build.sh build_all` |
| Want to change config | `./configure.py` then `./build.sh build_all` |
| Just updated repo, no config changes | `./build.sh build_all` |

### Option 1: First-Time Setup (Recommended)

**Best for:** New users, first time cloning the repo

```bash
cd cad
./setup.sh
```

**What happens:**
1. Detects your OS
2. Checks for Python 3.9+
3. Installs `uv` (optional, faster package manager)
4. Creates virtual environment (`.venv/`)
5. Installs dependencies (`build123d`, `numpy`)
6. Runs interactive configuration wizard (creates `config.py`)
7. Builds all parts

**After this:** You have a working setup with `config.py` created.

### Option 2: Just Build Parts

**Best for:** Already have `config.py` from previous build

```bash
cd cad
./build.sh build_all
```

**What happens:**
1. Checks for and activates `.venv/` automatically
2. Installs missing dependencies if needed
3. Builds all parts using your existing `config.py`

**Note:** If `config.py` doesn't exist, you'll get an error. Use `./configure.py` to create it.

### Option 3: Change Configuration

**Best for:** Want to modify printer settings

```bash
cd cad

# Just run configuration wizard (backs up existing config)
./configure.py

# Then rebuild with new settings
./build.sh build_all
```

**What happens:**
1. Asks configuration questions interactively
2. Backs up existing `config.py` to `config.py.backup`
3. Creates new `config.py` with your changes
4. `build.sh` will use the new config

### Option 4: Manual Control

**Best for:** Experienced users, want full control

```bash
cd cad

# Step 1: Create virtual environment (if needed)
python3 -m venv .venv

# Step 2: Activate environment
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Step 3: Install dependencies (if needed)
# Uses pyproject.toml (modern standard)
pip install -e .

# Step 4: Configure your printer (or edit config.py directly)
./configure.py

# Step 5: Build parts
./build.sh build_all
```

## Configuration

### When to Run Configuration Wizard

**Run `./configure.py` when:**
- First time setting up (creates new `config.py`)
- Want to change printer settings
- Switching hardware (different rods, hotend, etc.)

**Don't need to run when:**
- Just updated code from git
- Have `config.py` already set up
- Just want to rebuild parts

### Interactive Wizard

Run configuration wizard:

```bash
./configure.py
```

The wizard will ask about:
- **Build Volume**: X, Y, Z dimensions (mm)
- **M12 Rods**: Diameter and "lumpy factor" (0.2 for zinc, 0.5+ for galvanized)
- **Extruder**: Wade extruder settings
- **Hotend**: Type and mounting
- **Electronics**: Mainboard, Z-probe, CANbus

**Important:** This backs up your existing `config.py` to `config.py.backup`.

### Manual Configuration

Edit `config.py` directly:

```bash
vim config.py
# or
nano config.py
# or
code config.py
```

See `config.py.example` for all available options.

**Important:** `config.py` is ignored by git (your settings stay private).

## Building Parts

### Build All Parts

```bash
./build.sh build_all
```

The build script automatically:
- Discovers all Python parts in `parts/` directory
- Checks for and activates `.venv`
- Installs dependencies if not found

### Build Specific Parts

```bash
./build.sh build corner_front_left
```

The build system automatically discovers all Python files in `parts/` subdirectories.

### List Available Parts

```bash
./build.sh list
```

This runs `utilities/list.py` to dynamically discover all parts, grouped by category:
- Frame corners, extruder parts, bed components, etc.
- No hardcoded lists - just add new Python files to `parts/`

### Advanced: Test Mode

For testing with only a subset of parts:

```bash
TEST_MODE=true ./build.sh build_all
```

This uses only the corner motorized parts instead of discovering all files.

### Clean STL Directory

```bash
./build.sh clean
```

### View Help

```bash
./build.sh help
```

## What Happens When You Build

1. **Environment Check**: `build.sh` automatically detects and activates `.venv`
2. **Dependency Check**: Installs missing dependencies if needed
3. **Part Generation**: Runs Python CAD scripts to generate STLs
4. **Output**: STL files saved to `stl/` directory

## Troubleshooting

### Python Not Found

```bash
# macOS
brew install python@3.11

# Ubuntu/Debian
sudo apt install python3 python3-venv python3-pip

# Fedora
sudo dnf install python3 python3-venv python3-pip
```

### Build123d Import Error

```bash
# Make sure venv is activated
source .venv/bin/activate

# Reinstall dependencies (uses pyproject.toml)
pip install --force-reinstall -e .
```

### Out of Memory

If build123d runs out of RAM during part generation:
1. Close other applications
2. Add swap space (Linux)
3. Build parts individually instead of all at once

### Virtual Environment Issues

```bash
# Remove corrupted venv and recreate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Understanding the CAD System

### Architecture: Engine + Parts

Amalgam's CAD system follows a **library + application** pattern:

**`include/` - The Engine:**
- Contains all reusable build123d components
- Shared functions for motors, rods, mounts, clamps, etc.
- Single source of truth for geometric logic
- When you fix a bug here, it's fixed everywhere

**`parts/` - The Applications:**
- Lightweight scripts that import and configure components
- Each part is a specific configuration of shared components
- Easy to create new parts by reusing existing logic
- Organized by type (corner/, extruder/, bed/, etc.)

### Parametric Design

Amalgam uses **build123d**, a modern Python CAD library:
- **Code-based design**: All parts defined in Python scripts
- **Single source of truth**: `config.py` controls all dimensions
- **Composable components**: Import from `include/`, configure, export
- **Easy customization**: Change config, rebuild all parts automatically

### Why Not Just Download STLs?

**Dynamic sizing**:
- Want larger build volume? Change `BUILD_VOLUME` in config
- Using salvaged 8mm rods instead of 10mm? Change `SMOOTH_ROD_DIA`
- Different hotend diameter? Update `GROOVEMOUNT_DIA`

**Code reuse**:
- All corners share the same motorized corner logic from `include/corner_components.py`
- Fix a motor mount bug once, all corners benefit
- Add new features to shared components, all parts automatically get them

**One command rebuilds everything**:
```bash
./configure.py
./build.sh build_all
```

No manually editing STL files or dealing with version mismatches!

### File Structure

```
cad/
├── include/              # Shared CAD components (project engine)
│   └── corner_components.py   # Reusable motorized corner logic
├── parts/                # Part definitions (use include/ components)
│   └── corner_front_left.py   # Individual part files
├── utilities/            # Build system helpers and scripts
│   └── list.py               # Dynamic part discovery
├── stl/                  # Generated STL files (output)
├── config.py             # Your configuration (gitignored)
├── config.py.example     # Reference configuration
├── pyproject.toml        # Python dependencies (modern standard)
├── setup.sh              # Automated setup wizard
├── configure.py          # Interactive configuration
└── build.sh              # Part builder
```

**Key Design Principle:**
- **`include/`**: Contains all reusable CAD logic and build123d functions
- **`parts/`**: Lightweight scripts that import from `include/` and configure parts
- This separation maximizes code reuse and makes the codebase more maintainable

---

## Engineering Analysis Tool

Before building, assess your configuration with the analysis tool.

### Quick Analysis

```bash
python scripts/analyze.py --quick
```

This runs a quick check with reference spec defaults (235mm bed, M10 rods, Pitan).

### Interactive Analysis

```bash
python scripts/analyze.py
```

The interactive mode lets you:
- Choose your bed size (or enter custom dimensions)
- Select rod diameter (M8, M10, M12)
- Pick extruder type (Pitan, Wade, MK8, etc.)

It calculates:
- **Frame dimensions** needed for your bed
- **Rod sag** under toolhead load
- **Acceleration limits** for quality printing
- **Recommended Klipper settings**

### Example Output

```
Configuration:
  Bed: 235x235mm, Build height: 250mm
  Smooth rods: M10, Extruder: PITAN (280g)

Results:
  Frame size: 350x345x370mm
  Rod deflection: 0.0150mm (excellent)
  Max accel: 4578 mm/s²
  Velocity: 100-150 mm/s
```

---

## Documentation System (Quarto)

The documentation uses Quarto for config-driven generation.

### Setup Quarto

1. Install Quarto from [quarto.org](https://quarto.org/docs/get-started/)
2. Export config variables:

```bash
python scripts/export_config.py > docs/_variables.yml
```

### Build Documentation

```bash
cd docs
quarto render
```

This generates the website in `docs/_site/`.

### Preview Documentation

```bash
cd docs
quarto preview
```

Opens a live-reload preview in your browser.

### Config-Driven Content

Documentation uses variables from `config.py`:
- Frame dimensions update automatically
- Extruder references match your config
- Tier-specific content based on settings

---

## Three Build Systems Summary

| System | Command | Output |
|--------|---------|--------|
| **CAD/STL** | `./build.sh build_all` | `cad/stl/*.stl` |
| **Analysis** | `python scripts/analyze.py` | Terminal output |
| **Documentation** | `quarto render` | `docs/_site/` |

All three systems read from `cad/config.py` for consistency.

---

## Next Steps

After building parts:

1. **Run Analysis**: `python scripts/analyze.py` to verify your configuration
2. **Review STLs**: Open in slicer (Cura, PrusaSlicer, etc.)
3. **Prepare for Printing**: Check orientation, supports, infill
4. **Gather Hardware**: See [REFERENCE-SPEC.md](REFERENCE-SPEC.md) for BOM
5. **Build Guides**: See [docs/guides/](docs/guides/) for tier-specific instructions

## Contributing

Want to add new parts or improve existing ones?

1. **Design in build123d**: Create or modify Python scripts in `parts/`
2. **Update config**: Add new parameters to `config.py.example`
3. **Test**: Build and verify parts work correctly
4. **Document**: Add to this guide

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/amalgam-reprap/amalgam/issues)
- **Discussions**: Coming soon
- **Documentation**: See `docs/` directory for detailed design docs

---

> **Remember**: This is a reference specification. If you want a printer, buy one. If you want the Red Pill, build this.
