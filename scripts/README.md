# Amalgam Build System

The Amalgam build system generates everything you need from a single configuration:

- **Parts** for 3D printing (STL, STEP, 3MF, and more)
- **Documentation** customized to your build
- **Engineering analysis** to verify your configuration

## Quick Start

```bash
# Run the interactive wizard
python scripts/wizard.py

# Or build everything at once
python scripts/build.py
```

## Architecture

```
scripts/
├── wizard.py           # Interactive configuration wizard
├── build.py            # Master build orchestrator
├── analyze.py          # Engineering analysis TUI
├── whatif.py           # What-if trade-off exploration
├── export_config.py    # Config to Quarto bridge
├── registry/           # Component definitions
│   ├── boards.py       # Control board specs
│   ├── extruders.py    # Extruder specs
│   ├── beds.py         # Heated bed specs
│   ├── motors.py       # Stepper motor specs
│   └── compatibility.py # Tier rules & validation
├── builders/           # Build orchestration
│   ├── config_builder.py   # Generate config.py
│   ├── stl_builder.py      # Build STL files
│   ├── docs_builder.py     # Build documentation
│   └── analysis_runner.py  # Run analysis
└── analysis/           # Analysis modules
    ├── rod_sag.py      # Beam deflection
    ├── frame_sizing.py # Frame geometry
    └── acceleration.py # Motion limits
```

## The Three Build Systems

### 1. Part Generation (CAD)

Builds parts from parametric build123d scripts. Supports multiple export formats.

```bash
cd cad
./build.sh build_all                    # Default format (STL)
./build.sh build_all --format step      # STEP format
./build.sh build_all --format all       # All formats
./build.sh build_all --drawings         # Include technical drawings
```

Output: `cad/exports/<format>/` (e.g., `cad/exports/stl/`, `cad/exports/step/`)

CAD source structure:
- `cad/amalgam/lib/` — Shared components and utilities
- `cad/amalgam/parts/` — Individual part scripts (organized by category)

### 2. Documentation (Quarto)

Generates HTML documentation with your config values embedded.

```bash
python scripts/export_config.py > docs/_variables.yml
cd docs && quarto render
```

Output: `docs/_site/`

### 3. Engineering Analysis

Validates your configuration before you build.

```bash
python scripts/analyze.py --quick   # Reference spec
python scripts/analyze.py           # Interactive
```

Calculates:
- Frame dimensions from bed size
- Rod sag under toolhead load
- Maximum safe acceleration
- Recommended Klipper settings

## What-If Analysis

Explore trade-offs before committing:

```bash
python scripts/whatif.py                    # Interactive mode
python scripts/whatif.py --rods 8           # What if M8 rods?
python scripts/whatif.py --bed 200 200      # What if smaller bed?
python scripts/whatif.py --compare-rods     # Compare M8/M10/M12
python scripts/whatif.py --compare-beds     # Compare bed sizes
```

Example output:
```
Comparison: Current vs M8 Rods

  ENGINEERING ANALYSIS
  Metric               Current              Modified             Impact
  Rod Deflection       0.0150mm (excellent) 0.0365mm (marginal) ↑ 2.4x WORSE
  Max Accel            4578                 350                  ↓ -4228 slower

  VERDICT
  Concerns:
    ⚠ Deflection increases 2.4x - may affect print quality
    ⚠ Rod sag rated 'marginal' - consider alternatives
```

The tool can also update your config.py with explored changes.

## The Wizard

The wizard guides you through configuration:

```bash
python scripts/wizard.py
```

1. **Parts Inventory**: What motors, boards, bed do you have?
2. **Tier Detection**: Auto-determines your build tier (1-3)
3. **Compatibility Check**: Warns about edge cases
4. **Config Generation**: Creates `cad/config.py`
5. **Analysis**: Runs engineering validation

### Quick Mode

```bash
python scripts/wizard.py --quick
```

Uses reference spec defaults (235mm bed, M10 rods, Pitan, MKS SKIPR).

## Component Registry

The registry defines all supported components and their properties:

### Adding a New Board

Edit `scripts/registry/boards.py`:

```python
BOARDS["MY_NEW_BOARD"] = BoardSpec(
    id="MY_NEW_BOARD",
    name="My New Board",
    manufacturer="Maker",
    stepper_drivers=6,
    has_canbus=True,
    integrated_host=False,
    # ... other properties
)
```

### Adding a New Extruder

Edit `scripts/registry/extruders.py`:

```python
EXTRUDERS["MY_EXTRUDER"] = ExtruderSpec(
    id="MY_EXTRUDER",
    name="My Extruder",
    drive_type="single",
    mass_grams=250,
    # ... other properties
)
```

## Build Orchestration

The master build script ties everything together:

```bash
# Interactive full build
python scripts/build.py

# Non-interactive full build
python scripts/build.py --all

# Individual components
python scripts/build.py --stls      # STLs only
python scripts/build.py --docs      # Docs only
python scripts/build.py --analyze   # Analysis only
python scripts/build.py --wizard    # Run wizard
```

## Configuration Flow

```
┌─────────────────┐
│  wizard.py      │  User answers questions about parts
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  config.py      │  Single source of truth
└────────┬────────┘
         │
    ┌────┴────┬──────────┐
    ▼         ▼          ▼
┌───────┐ ┌───────┐ ┌─────────┐
│ Parts │ │ Docs  │ │Analysis │
│build.sh│ │Quarto │ │analyze.py│
└───────┘ └───────┘ └─────────┘
```

## Tier System

| Tier | Motors | Drivers | Z Type | Host |
|------|--------|---------|--------|------|
| 1 | 4 | 4 | Belt | External |
| 2 | 6 | 6 | Triple | External |
| 3 | 6 | 6 | Triple | Integrated |

The wizard auto-detects your tier based on available parts.

## Extending the System

### Adding New Analysis

1. Create module in `scripts/analysis/`
2. Export from `scripts/analysis/__init__.py`
3. Call from `analyze.py` TUI

### Adding New Documentation

1. Create `.qmd` file in `docs/`
2. Use `{{< var name >}}` for config values
3. Add to `docs/_quarto.yml` navigation

### Adding New Parts (CAD)

1. Create Python file in `cad/amalgam/parts/<category>/`
2. Import components from `cad/amalgam/lib/`
3. Use `export_part(part, "name")` for output
4. Parts auto-discovered by `build.sh`

## Philosophy

This build system embodies Amalgam's principles:

1. **Single Source of Truth**: `config.py` drives everything
2. **Discoverable Components**: Add files, not code
3. **Extensible**: Registry pattern for new hardware
4. **Layered Complexity**: Simple defaults, deep customization
