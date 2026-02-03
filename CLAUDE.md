# Amalgam AI Context

This file provides context for AI assistants working on the Amalgam project.

## What This Project Is

Amalgam is a **2026 RepRap-inspired reference specification** for a scavenger-friendly 3D printer:
- **Target cost:** < $300 AUD (often $160-230 with good donors)
- **Build volume:** 220×220×220mm (Anet A8 bed size)
- **Philosophy:** "Tractor with a Racecar Brain" — heavy hardware + Klipper intelligence
- **Minimum requirement:** Two donor printers (one donor = just add Klipper, not Amalgam)
- **Target release:** End of 2026

## Read First (Priority Order)

1. **SAFETY.md** — Hazards and safety guidance (for physical builds)
2. **PHILOSOPHY.md** — The "Tractor" concept, heritage acknowledgments
3. **docs/adr/README.md** — Index of all architectural decisions
4. **docs/adr/025-multi-frame-architecture.md** — Frame paths (Darwin, S-Core, V-Core)
5. **docs/adr/021-dual-rod-motion-system.md** — Smooth rod motion system (Dual 8mm)
6. **docs/adr/012-mainboard-host-architecture.md** — Electronics paths, dual-MCU config
7. **docs/reference/donor-printer-guide.md** — Which printers to scavenge

## Key Architectural Decisions

| Topic | Decision | ADR |
|-------|----------|-----|
| Frame Paths | Darwin (M10), S-Core, V-Core — all on MDF base | ADR-025 |
| Frame (Primary) | M10 threaded rod skeleton + MDF squaring jig | ADR-001, ADR-025 |
| Motion (Primary) | Dual 8mm rods, vertical stacking | ADR-021 |
| Motion (V-Core) | V-slot rails + POM wheels | ADR-025 |
| Bearings | LM8LUU (X), LM8UU (Y/Z), IGUS, or POM wheels | ADR-022, ADR-025 |
| Z-System | Z-drop (bed moves), Triple-Z leveling | ADR-005, ADR-023 |
| Bed Size | 220×220mm (Anet A8 scavenger size) | ADR-024 |
| Extruder | Pitan (3:1 geared, single-drive) | ADR-019 |
| Hotend | E3D V6 + CHT nozzle | ADR-004 |
| Electronics | Dual-MCU Klipper or MKS SKIPR (optional upgrade) | ADR-012 |
| Drivers | TMC2209, sensorless homing optional | ADR-013 |

## Frame Paths (ADR-025)

Amalgam supports three frame/motion configurations based on donor type:

| Path | Frame | Motion | Best Donors | Use Case |
|------|-------|--------|-------------|----------|
| **Darwin** | M10 Threaded Rod + MDF | Smooth Rods + LM8UU | Anet A8, Wanhao, Prusa clones | **Primary (heritage, common donors)** |
| **V-Core** | Aluminum Extrusion + MDF | V-Slots + POM Wheels | Ender 3, CR-10, Aquila | **Primary (modern donors, zero-waste)** |
| S-Core | Aluminum Extrusion + MDF | Smooth Rods + LM8UU/IGUS | Mixed: extrusion + smooth-rod donors | Fallback (rare in practice) |

**All paths share:** MDF base (squaring jig + damping), Triple-Z, Pitan + E3D V6, Klipper.

**Two primary paths:** Darwin (RepRap heritage, industrial "tractor" aesthetic) and V-Core (modern, waste-free). S-Core exists for mixed donor scenarios but is rarely needed.

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

| Item | Darwin | S-Core/V-Core |
|------|--------|---------------|
| Two matching donors | $100-120 | $100-120 |
| MDF base | $15-20 | $15-20 |
| M10 threaded rods | $30-45 | $0 (scavenged) |
| Pitan gear + Klicky | $4 | $4 |
| Misc (wires, bolts) | $40 | $40 |
| **Total** | **~$190-230** | **~$160-185** |

## Donor Printer Categories

| Category | Examples | Frame Path | Motion | Extra Cost |
|----------|----------|------------|--------|------------|
| **Rod + Sheet** | Anet A8, Wanhao i3, Prusa clones | Darwin (M10) | Smooth rods | M10 rods ~$30-45 |
| **Rod + Extrusion** | i3 Mega, Artillery Sidewinder | S-Core | Smooth rods | $0 |
| **V-Slot** | Ender 3, CR-10, Voxelab Aquila | V-Core | V-slots | $0 |
| **Mixed** | One of each type | Darwin (usually) | Varies | ~$30-45 for M10 |
| **Limited** | Prusa Mini, deltas, resin | Not recommended | — | — |

**Key insight:** Two matching donors = zero motion parts to buy. Mixed donors require buying frame material (~$30-45).

**Advice for mixed donors:** Buy M10 rods (cheapest fix), use smooth rods from rod-donor. Or sell odd donor, buy matching.

## Heritage (What We Borrowed)

| Project | Contribution | Used In |
|---------|--------------|---------|
| RepRap Darwin | Box-frame threaded-rod skeleton | Darwin path |
| RepRap Mendel | "Plough" X-carriage sled on dual rods | All paths |
| Prusa i3 Rework | Wade geared extruder → Pitan | All paths |
| Voron Legacy | Dual 8mm rods, vertical stacking | Darwin, S-Core |
| Voron Trident | Three-pillar Z-drop, Triple-Z leveling | All paths |
| Ender 5 | Cartesian Z-drop with V-slot motion | V-Core path |
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
- **Frame paths:** Darwin (M10 + smooth rods), S-Core (extrusion + smooth rods), V-Core (extrusion + V-slots)
- **Primary path:** Darwin is the flagship; S-Core and V-Core are supported variants
- **Rod sizes:** M10 for Darwin frame, 8mm for smooth rod motion
- **Bed size:** 220×220mm reference (supports 200-250mm parametrically)
- **MDF base:** All paths use MDF for squaring jig + mass damping

## File Structure

```
amalgam/                  # (currently amalgam/, rename pending)
├── MANIFESTO.md          # Quick overview
├── PHILOSOPHY.md         # "Tractor" philosophy, heritage
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
- Don't force Ender users to buy rods — V-Core path exists (ADR-025)
- Don't treat V-Core as primary — Darwin (M10 + smooth rods) is the flagship
- Don't suggest one-donor builds as Amalgam — one donor = just add Klipper, not Amalgam

## Second-Hand Market Context

- Donor printers expected to bottom out at ~$50 AUD by end of 2026
- Real pricing (AliExpress 2026): 8× stainless rods $43, 22× IGUS $30, M10 rods $30-45
- **Two Anet A8 donors** (Darwin path) = ~$190-230 total build
- **Two i3 Mega donors** (S-Core path) = ~$160-185 total build
- **Two Ender 3 donors** (V-Core path) = ~$160-185 total build (zero waste!)
- **Mixed donors** = add ~$30-45 for M10 rods

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
```

---

*Last updated: January 2026*
