# Amalgam AI Context

This file provides context for AI assistants working on the Amalgam project.

## What This Project Is

Amalgam is a **2026 RepRap-inspired reference specification** for a scavenger-friendly 3D printer:
- **Target cost:** < $300 AUD (often $160-280 with good donors)
- **Build volume:** 220×220×220mm (Anet A8 bed size)
- **Philosophy:** "Tractor with a Racecar Brain" — heavy hardware + Klipper intelligence
- **Minimum requirement:** Two donor printers (one donor = just add Klipper, not Amalgam)
- **Target release:** End of 2026

## Read First (Priority Order)

1. **SAFETY.md** — Hazards and safety guidance (for physical builds)
2. **docs/philosophy.md** — The "Tractor" concept, heritage acknowledgments
3. **docs/adr/README.md** — Index of all architectural decisions
4. **docs/adr/025-multi-frame-architecture.md** — Frame paths (Scaffold, Mill, Lathe)
5. **docs/adr/021-dual-rod-motion-system.md** — Smooth rod motion system (Dual 8mm)
6. **docs/adr/012-mainboard-host-architecture.md** — Electronics paths, dual-MCU config
7. **docs/reference/donor-printer-guide.md** — Which printers to scavenge

## Key Architectural Decisions

| Topic | Decision | ADR |
|-------|----------|-----|
| Frame Paths | Scaffold (M10), Mill (V-slot), Lathe (extrusion+rods) — all on MDF base | ADR-025 |
| Frame (Scaffold) | M10 threaded rod skeleton + MDF squaring jig | ADR-001, ADR-025 |
| Motion (Scaffold/Lathe) | Dual 8mm rods, vertical stacking | ADR-021 |
| Motion (Mill) | V-slot rails + POM wheels | ADR-025 |
| Bearings | LM8LUU (X), LM8UU (Y/Z), IGUS, or POM wheels | ADR-022, ADR-025 |
| Z-System | Z-drop (bed moves), Triple-Z leveling | ADR-005, ADR-023 |
| Bed Size | 220×220mm (Anet A8 scavenger size) | ADR-024 |
| Extruder | Pitan (3:1 geared, single-drive) | ADR-019 |
| Hotend | E3D V6 + CHT nozzle | ADR-004 |
| Electronics | Dual-MCU Klipper or MKS SKIPR (optional upgrade) | ADR-012 |
| Drivers | TMC2209, sensorless homing optional | ADR-013 |

## Frame Paths (ADR-025)

Amalgam supports three frame/motion configurations based on donor type:

| Path | Frame | Motion | Best Donors | Character |
|------|-------|--------|-------------|-----------|
| **Scaffold** | M10 Threaded Rod + MDF | Smooth Rods + LM8UU | Anet A8, Wanhao, Prusa clones | Heritage — RepRap Darwin tribute, industrial "tractor" aesthetic |
| **Mill** | Aluminum Extrusion + MDF | V-Slots + POM Wheels | Ender 3, CR-10, Aquila | Zero-waste — uses everything from Ender donors |
| **Lathe** | Aluminum Extrusion + MDF | Smooth Rods + IGUS | Ender 3 + bought rods, mixed donors | Precision — superior motion quality, best overall |

**All paths share:** MDF base (squaring jig + damping), Triple-Z, Pitan + E3D V6, Klipper.

**Motion quality:** Lathe (smooth rods + IGUS) > Scaffold (smooth rods + LM8UU) > Mill (V-slots + POM wheels). Lathe is technically superior but costs ~$75 more than Mill.

## Who Is Amalgam For?

**Got one donor?** Just add Klipper to it. Amalgam isn't for you.

**Got two matching donors?** Perfect. Pick your frame path based on what you scavenged.

**Want to buy new parts?** Just buy a Bambu A1 Mini. This project is for scavengers.

### Electronics Paths

| Path | Description | Added Cost |
|------|-------------|------------|
| **Dual-MCU** | Two scavenged 4-driver boards + Klipper | $0 |
| **SKIPR** | MKS SKIPR single board (cleaner setup) | ~$130 |

### Cost Breakdown

| Item | Scaffold | Mill | Lathe |
|------|----------|------|-------|
| Two matching donors | $100-120 | $100-120 | $100-120 |
| MDF base | $15-20 | $15-20 | $15-20 |
| Frame material | M10 rods: $30-45 | $0 | $0 |
| Motion (rods/bearings) | $0 | $0 | ~$75 |
| Pitan gear + Klicky | $4 | $4 | $4 |
| Misc (wires, bolts) | $40 | $40 | $40 |
| **Total** | **~$190-230** | **~$160-185** | **~$235-280** |

## Donor Printer Categories

| Category | Examples | Frame Path | Motion | Extra Cost |
|----------|----------|------------|--------|------------|
| **Rod + Sheet** | Anet A8, Wanhao i3, Prusa clones | Scaffold (M10) | Smooth rods | M10 rods ~$30-45 |
| **Rod + Extrusion** | i3 Mega, Artillery Sidewinder | Lathe | Smooth rods | $0 |
| **V-Slot** | Ender 3, CR-10, Voxelab Aquila | Mill or Lathe | V-slots or smooth rods | $0 or ~$75 |
| **Mixed** | One of each type | Lathe | Smooth rods | $0-75 |
| **Limited** | Prusa Mini, deltas, resin | Not recommended | — | — |

**Key insight:** Two matching donors = minimal extra parts. Lathe costs ~$75 more but offers better motion.

**Advice for Ender donors:** Mill is zero-waste and cheap. Lathe is better motion if you can spend ~$75 on rods + IGUS.

## Heritage (What We Borrowed)

| Project | Contribution | Used In |
|---------|--------------|---------|
| RepRap Darwin | Box-frame threaded-rod skeleton | Scaffold path |
| RepRap Mendel | "Plough" X-carriage sled on dual rods | All paths |
| Prusa i3 Rework | Wade geared extruder → Pitan | All paths |
| Voron Legacy | Dual 8mm rods, vertical stacking | Scaffold, Lathe |
| Voron Trident | Three-pillar Z-drop, Triple-Z leveling | All paths |
| Ender 5 | Cartesian Z-drop with V-slot motion | Mill path |
| The 100 / The Rook | Klipper-first philosophy | All paths |

## Technology Stack

- **CAD:** build123d (Python BREP, not OpenSCAD)
- **Documentation:** Quarto (literate programming, conditional content)
- **Firmware:** Klipper (Input Shaping, Pressure Advance, Z-tilt)
- **Config:** Python (`cad/config.py`) drives parametric generation

## Conventions

- **Currency:** Always AUD (Australian Dollars)
- **ADRs:** All major decisions documented in `docs/adr/`
- **Supersession:** Old ADRs preserved with "Superseded by ADR-XXX" notes
- **Frame paths:** Scaffold (M10 + smooth rods), Mill (extrusion + V-slots), Lathe (extrusion + smooth rods)
- **Path character:** Scaffold = heritage, Mill = zero-waste, Lathe = precision
- **Rod sizes:** M10 for Scaffold frame, 8mm for smooth rod motion
- **Bed size:** 220×220mm reference (supports 200-250mm parametrically)
- **MDF base:** All paths use MDF for squaring jig + mass damping

## File Structure

```
amalgam/                  # (currently amalgam/, rename pending)
├── REFERENCE-SPEC.md     # Hardware specification
├── BUILDING.md           # Build instructions
├── cad/
│   ├── config.py.example # Master configuration
│   ├── parts/            # build123d part scripts
│   └── build.sh          # STL generation
├── docs/
│   ├── adr/              # Architecture Decision Records
│   ├── guides/           # Path-specific build guides
│   ├── reference/        # Background material, donor guide
│   └── deep-dives/       # Design exploration
└── scripts/
    ├── wizard.py         # Configuration wizard
    ├── analyze.py        # Engineering analysis
    └── whatif.py         # Trade-off comparisons
```

## Current Project Status

| Component | Status |
|-----------|--------|
| Philosophy & ADRs | ✅ Complete |
| Build system (wizard, analysis) | ✅ Complete |
| build123d parametric parts | 🔧 In development |
| Klipper configurations | 🔧 In development |
| Assembly documentation | 🔧 Planned |
| Reference build | ⏳ Planned (2026) |

## What NOT To Do

- Don't use OpenSCAD — we chose build123d (ADR-017)
- Don't suggest linear rails — smooth rods or V-slots are intentional (ADR-021, ADR-025)
- Don't chase high speed — 70-120mm/s is the target, not 300mm/s
- Don't add cloud features — 100% local control is a core value
- Don't forget heritage credits — we stand on shoulders of giants
- Don't force Ender users to buy rods — Mill path exists for zero-waste (ADR-025)
- Don't suggest one-donor builds as Amalgam — one donor = just add Klipper, not Amalgam

## Second-Hand Market Context

- Donor printers expected to bottom out at ~$50 AUD by end of 2026
- Real pricing (AliExpress 2026): 8× stainless rods $43, 22× IGUS $30, M10 rods $30-45
- **Two Anet A8 donors** (Scaffold) = ~$190-230 total build
- **Two Ender 3 donors** (Mill) = ~$160-185 total build (zero waste!)
- **Two Ender 3 donors** (Lathe) = ~$235-280 total build (best motion)
- **Mixed donors** (Lathe) = ~$160-220 depending on what you can scavenge

## Useful Commands

```bash
# Generate config from wizard
python scripts/wizard.py

# Quick engineering analysis
python scripts/analyze.py --quick

# Compare rod options
python scripts/whatif.py --compare-rods

# Build all STL parts
cd cad && ./build.sh build_all

# Build specific part
cd cad && ./build.sh build corner_standard

# Build with specific format
cd cad && ./build.sh build corner_standard --format step

# List available parts
cd cad && ./build.sh list

# Test single part (fastest iteration)
cd cad && .venv/bin/python amalgam/parts/frame/corner_standard.py

# Lint/format
cd cad && ruff check . && ruff format .

# Run tests
cd cad && pytest
```

## CAD Development

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

### Import Pattern

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

Always use config values — no fallbacks for dimensions:

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

Key methods: `Box()`, `Cylinder()`, `.moved()`, `.rotate()`, `Mode.SUBTRACT`, `Plane.XZ/YZ`

### Export System

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

### Common Pitfalls

1. Missing config.py → Exit with error (no fallbacks)
2. Wrong import path → Use `from amalgam.lib.<module> import ...`
3. Export location → Use `export_part()`, not direct `export_stl()`
4. Method names → Use `.rotate()`, not `.rotated()`
5. Hardcoded dims → Always use `config.py` for fit parameters

### Versions

- Python: 3.10-3.13 (NOT 3.14+)
- build123d: 0.9.0+
- numpy: 1.20.0+

---

*Last updated: February 2026*
