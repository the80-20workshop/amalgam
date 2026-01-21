# Neo-Darwin Documentation & Build System Plan

**Status**: In Progress - ADR Updates Complete
**Date**: 2026-01-21
**Last Updated**: 2026-01-21

## Decisions Made

The following decisions were confirmed:

1. **Config structure**: Single `config.py` with clear sections (common, CAD-only, docs-only)
2. **MANIFESTO split**: Three documents - Philosophy, Reference Spec, Quick Start
3. **ADR approach**: Archive old ADRs, create new ones (preserves history)
4. **Documentation tool**: Quarto (familiar, avoids reinventing)
5. **Analysis tool**: TUI from the start
6. **Priority**: Fix ADRs first, then restructure
7. **Folder naming**: `docs/deep-dives/` instead of `docs/deep-dives/` (clearer distinction from ADRs)

## Completed Work

- [x] ADR-001: Updated for M10 (renamed `001-m10-skeleton.md`)
- [x] ADR-002: Archived (points to ADR-019)
- [x] ADR-019: Created for Pitan extruder
- [x] ADR README: Updated with new index
- [x] Fixed typo: `traxctor_06` → `tractor_06`

This document captures the proposed documentation reorganization, tiered build system, and engineering analysis tools for the Neo-Darwin project.

---

## Part 1: Current State Issues

### 1.1 Outdated References

| Document | Says | Should Be |
|----------|------|-----------|
| MANIFESTO.md | Wade extruder | Pitan extruder |
| MANIFESTO.md | M12 threaded rods | M10 threaded rods |
| config.py | `EXTRUDER_TYPE = "WADE"` | `EXTRUDER_TYPE = "PITAN"` |
| config.py | `M12_NOMINAL_DIA = 12.0` | `M10_NOMINAL_DIA = 10.0` |
| ADR-002 | Greg's Wade | Needs archiving |

### 1.2 Structural Issues

- **MANIFESTO.md is too large** (~56KB) - doing too much
- **tractor_\* files** scattered in docs/ root - need own folder
- **Typo**: `traxctor_06_extruder_decision.md` (missing 'a')
- **ADR gap**: No ADR documenting Pitan decision
- **BUILDING.md** only covers CAD/STL generation

---

## Part 2: Proposed Documentation Structure

```
docs/
├── README.md                      # Documentation index/navigation
├── guides/                        # NEW: User-facing guides (tiered)
│   ├── tier-0-klipper-only.md    # Flash Klipper, no Neo-Darwin build
│   ├── tier-1-single-donor.md    # 1 donor + buy 1 motor
│   ├── tier-2-dual-donor.md      # 2 donors, multi-MCU
│   ├── tier-3-reference-spec.md  # MKS SKIPR, CAN bus, single PSU
│   └── klipper/                  # Klipper-specific guides
│       ├── laptop-host.md
│       ├── rpi-3b-host.md
│       └── zero-2w-host.md
├── decisions/                     # NEW: Deep-dive design discussions
│   ├── tractor_00_decision_guide.md
│   ├── tractor_01_frame_and_assembly.md
│   ├── tractor_02_xy_axis_system.md
│   ├── tractor_03_motor_mounts_vibration.md
│   ├── tractor_04_xgantry_design_decision.md
│   ├── tractor_05_psu_configurations.md
│   └── tractor_06_extruder_decision.md  # Fixed typo
├── analysis/                      # NEW: Engineering analysis docs
│   ├── rod-sag-analysis.md
│   ├── max-safe-acceleration.md
│   └── frame-strength.md
├── adr/                           # Architecture Decision Records
│   ├── 000-engineering-philosophy.md
│   ├── 001-m10-skeleton.md        # UPDATED from M12
│   ├── 002-greg-wade.md           # ARCHIVED
│   ├── 002-pitan-extruder.md      # NEW - supersedes 002
│   ├── ... (rest unchanged)
│   └── README.md
├── articles/                      # Long-form thought pieces
│   └── (existing articles)
├── reference/                     # Historical conversations (unchanged)
│   ├── ai-conversations/
│   └── planning/
└── MASTER_PARTS_LIST.md
```

### Root-Level Documents

```
/
├── MANIFESTO.md                   # Slimmed: Philosophy + quick-start only
├── BUILDING.md                    # EXPANDED: All three build systems
├── PHILOSOPHY.md                  # NEW: Split from MANIFESTO
├── REFERENCE-SPEC.md              # NEW: The "blessed" configuration
└── VENV-SETUP.md                  # Keep as-is
```

---

## Part 3: MANIFESTO.md Splitting Proposal

The current MANIFESTO.md tries to be:
1. Philosophy document ("Tractor vs Racecar")
2. Engineering specification (M12, Wade, etc.)
3. Quick-start guide (5 Key Decisions)
4. BOM reference
5. Historical context

### Proposed Split

| New Document | Content |
|--------------|---------|
| **MANIFESTO.md** | Philosophy only - "Why we build tractors" (~10KB) |
| **REFERENCE-SPEC.md** | The "blessed" configuration (Pitan, M10, Triple-Z, etc.) |
| **PHILOSOPHY.md** | Deep engineering philosophy (Neo-Darwin Square, 20 years wisdom) |
| **docs/guides/README.md** | How to choose your tier |

---

## Part 4: Tiered Build System

### Tier Definitions

| Tier | Donors | Key Hardware | MCU | Klipper Host |
|------|--------|--------------|-----|--------------|
| **0** | N/A | Keep donor, flash Klipper | Donor board | Laptop/RPi/Zero2W |
| **1** | 1 | Buy 1 motor (dual Y), belted Z | Donor board | Laptop/RPi/Zero2W |
| **2** | 2 | Enough steppers, 1-2 PSUs | Multi-MCU | Laptop/RPi/Zero2W |
| **3** | 1-2 | MKS SKIPR, CAN bus, single PSU | Integrated | Laptop/RPi/Zero2W |
| **4** | 0 | Buy everything (not recommended) | Any | Any |

### Documentation Build Order

You plan to:
1. Build & document **Tier 3** (with 3 Klipper options)
2. Tear down, build & document **Tier 2** (with 3 Klipper options, + MCU variations)
3. Tear down, build & document **Tier 1** (with 3 Klipper options)
4. **Tier 0** = pointers to Klipper flashing resources

### Documentation Variations Matrix (Updated)

| Tier | Klipper Host | PSU Config | Total Variations |
|------|--------------|------------|------------------|
| 3 | 1 (Integrated - MKS SKIPR) | 1 (single) | 1 |
| 2 | 3 (Laptop, RPi 3B+, Zero2W) | 2 (single PSU, dual PSU) | 6 |
| 1 | 3 | 1 | 3 |
| 0 | 3 | N/A | 3 |

**Total: 13 documentation variations** (significant overlap between tiers)

**Note:** Tier 3 uses MKS SKIPR with integrated Klipper host, CAN bus, and ADXL—no external host variations needed.

---

## Part 5: Config-Driven Build System

### Proposed Architecture

```
cad/
├── config/
│   ├── common.py              # Shared settings (rod types, clearances)
│   ├── cad.py                 # CAD-specific (tolerances, filament, etc.)
│   └── docs.py                # Documentation-specific (tier, host, PSU)
├── config.py                  # User's merged config (gitignored)
├── configure.py               # Interactive wizard (already exists)
└── ...
```

### Alternative: Single config.py with Sections

```python
# === COMMON SETTINGS ===
ROD_TYPE = "M10"           # M8, M10, M12
SMOOTH_ROD_DIA = 10.0      # 8.0, 10.0
EXTRUDER_TYPE = "PITAN"    # PITAN, WADE, ORBITER

# === CAD-ONLY SETTINGS ===
LUMPY_FACTOR = 0.5         # For galvanized rods
TOLERANCE = 0.2            # Print tolerance

# === DOCUMENTATION-ONLY SETTINGS ===
TIER = 3                   # 0, 1, 2, 3, 4
KLIPPER_HOST = "RPI_3B"    # LAPTOP, RPI_3B, ZERO_2W
PSU_CONFIG = "SINGLE"      # SINGLE, DUAL

# === BUILD VOLUME ===
BUILD_VOLUME = {"X": 250, "Y": 250, "Z": 250}
BED_SIZE = (235, 235)      # Heatbed dimensions
```

### Decision Required

**Option A: Single config.py** (recommended)
- Simpler to maintain
- One file to edit
- Clear section comments
- Some settings unused by each system (acceptable)

**Option B: Split configs**
- More explicit separation
- Config inheritance complexity
- More files to manage

---

## Part 6: Documentation Generation System

### Concept

Use config.py to conditionally generate documentation via Quarto or similar.

```python
# docs/guides/tier-2-dual-donor.qmd (Quarto markdown)

---
title: "Tier 2 Build Guide"
---

{{< include _common-intro.qmd >}}

::: {.callout-note}
## Your Configuration
- Klipper Host: {{< var KLIPPER_HOST >}}
- PSU Configuration: {{< var PSU_CONFIG >}}
:::

{{#if PSU_CONFIG == "DUAL"}}
## Dual PSU Wiring

Connect your two power supplies as follows...
{{/if}}

{{#if PSU_CONFIG == "SINGLE"}}
## Single PSU Wiring

Your single 24V supply connects...
{{/if}}
```

### Alternative: Python-based Generation

```python
# scripts/generate_docs.py

from config import TIER, KLIPPER_HOST, PSU_CONFIG
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('docs/templates'))
template = env.get_template('tier-guide.md.j2')

output = template.render(
    tier=TIER,
    klipper_host=KLIPPER_HOST,
    psu_config=PSU_CONFIG
)

with open(f'docs/guides/tier-{TIER}-guide.md', 'w') as f:
    f.write(output)
```

---

## Part 7: Engineering Analysis Tool

### Purpose

A CLI/TUI tool that takes user configuration and analyzes build feasibility:
- Rod sag at given span
- Frame rigidity assessment
- Max safe acceleration
- Bed size vs frame size recommendations
- Extruder mass impact on motion quality

### Example Usage

```bash
$ ./analyze.py --bed 235x235 --rods M8 --span 400

Neo-Darwin Engineering Analysis
================================

Configuration:
  Bed Size: 235mm x 235mm
  Rod Type: M8 smooth rods
  Frame Span: 400mm

Analysis Results:

  ROD SAG ANALYSIS
  ----------------
  Span: 400mm with M8 rods
  Expected deflection: 0.15mm at center (with toolhead load)

  WARNING: For spans > 350mm, M8 rods may affect print quality.

  Recommendation: Consider:
  - Reducing to 200x200 MK3 Dual bed (~$20 AliExpress)
  - Upgrading to M10 rods (~$15-25 additional)

  FRAME SIZE CALCULATION
  ----------------------
  Minimum frame (internal): 275mm x 275mm x 285mm
  M10 rod length needed:
    - 4x 275mm (X axis)
    - 4x 275mm (Y axis)
    - 4x 285mm (Z axis)

  ACCELERATION LIMITS
  -------------------
  With Pitan extruder (~180g toolhead):
    Max safe X/Y accel: 2500 mm/s^2
    Recommended cruise speed: 70-120 mm/s

  OVERALL ASSESSMENT: MARGINAL
  Consider M10 upgrade or smaller bed for optimal results.
```

### Implementation Structure

```
scripts/
├── analyze.py              # Main CLI entry point
├── analysis/
│   ├── __init__.py
│   ├── rod_sag.py         # Beam deflection calculations
│   ├── frame_sizing.py    # Frame geometry from bed size
│   ├── acceleration.py    # Max accel from mass + rigidity
│   └── recommendations.py # Decision support logic
└── tests/
    └── test_analysis.py
```

### Data from config.py

The analysis tool would read:
- `SMOOTH_ROD_DIA` - for deflection calculations
- `BUILD_VOLUME` / `BED_SIZE` - for frame sizing
- `EXTRUDER_TYPE` - for mass estimates
- `ROD_TYPE` - for frame rod strength

---

## Part 8: Updated BUILDING.md Scope

### Current Coverage
- CAD/STL generation only

### Proposed Coverage

```markdown
# Building Neo-Darwin

This guide covers three build systems:

## 1. Building STL Parts (CAD System)
   - Quick start with setup.sh
   - Configuration wizard
   - Building parts
   - Understanding parametric design

## 2. Building Documentation (Docs System)
   - Generating tier-specific guides
   - Configuration for your build
   - Exporting to PDF

## 3. Engineering Analysis (Analysis System)
   - Assessing your component choices
   - Rod sag calculations
   - Frame sizing recommendations
   - Acceleration limits
```

---

## Part 9: ADR Updates Required

### Archive ADR-002

```markdown
# ADR-002: Greg's Wade Geared Extruder

## Status
**Archived** - Superseded by ADR-002-pitan

## Original Decision
[Keep original content for historical reference]

## Superseded By
See ADR-002-pitan for current extruder decision.
```

### New ADR-019: Pitan Extruder

```markdown
# ADR-019: Pitan Direct Drive Extruder

## Status
Accepted (supersedes ADR-002)

## Context
After extensive evaluation documented in:
- docs/deep-dives/tractor_06_extruder_decision.md
- docs/reference/ai-conversations/pitian-v-orbiter.md
- docs/reference/ai-conversations/single-v-dual-drive.md

We reconsidered the Greg's Wade extruder decision.

## Decision
We choose the **Pitan Direct Drive Extruder** as the reference specification.

### Why Pitan over Wade?
1. [Document reasons from your discussions]
2. ...

## Consequences
...
```

### Update ADR-001 for M10

Either:
- Archive ADR-001 and create ADR-001-m10
- Or update ADR-001 in-place with change history

---

## Part 10: Immediate Action Items

### Phase 1: Documentation Cleanup (Quick Wins)
1. [ ] Fix typo: `traxctor_06` -> `tractor_06`
2. [ ] Create `docs/deep-dives/` folder
3. [ ] Move tractor_* files to `docs/deep-dives/`
4. [ ] Archive ADR-002 (mark as superseded)
5. [ ] Update ADR README index

### Phase 2: Core Updates
6. [ ] Update MANIFESTO.md (Wade -> Pitan, M12 -> M10)
7. [ ] Update config.py defaults
8. [ ] Create new ADR for Pitan decision
9. [ ] Update ADR-001 for M10

### Phase 3: Restructure
10. [ ] Split MANIFESTO.md into focused documents
11. [ ] Create `docs/guides/` structure
12. [ ] Create `docs/analysis/` structure
13. [ ] Update BUILDING.md scope

### Phase 4: New Systems
14. [ ] Design config.py structure (single vs split)
15. [ ] Create documentation generation system
16. [ ] Create engineering analysis CLI
17. [ ] Write tier-specific guides (as you build each tier)

---

## Questions for You

1. **Config structure**: Single `config.py` with sections, or split into `common.py`, `cad.py`, `docs.py`?

2. **ADR approach**: Archive ADR-002 and create new ADR-019, or update ADR-002 in-place with "superseded by" notes?

3. **ADR-001 (M12)**: Same question - archive and create new, or update in-place?

4. **MANIFESTO split priority**: Should we do this before or after the Pitan/M10 updates?

5. **Analysis tool**: CLI only first, or include TUI from the start?

6. **Documentation generation**: Quarto (more powerful, steeper learning) or Jinja2 templates (simpler, Python-native)?

---

## Notes

- `docs/reference/` and subfolders remain unchanged (historical record)
- All changes should maintain git history
- Pitan references already exist in 19 files - consolidation needed
- Existing analysis docs (rod sag, acceleration) can seed the analysis tool

