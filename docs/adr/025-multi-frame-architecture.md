# ADR-025: Multi-Frame Architecture (Scavenger Paths)

## Status
Accepted

## Amends
- ADR-001: M10 Threaded Rod Skeleton (adds alternative frame paths)
- ADR-021: Dual-Rod Motion System (adds V-slot motion path)

## Context

### The Scavenger Reality

Amalgam requires **two donor printers** for a complete build (ADR-005, ADR-021). The most common donors in 2026 fall into two categories:

| Donor Type | Examples | Frame | Motion |
|------------|----------|-------|--------|
| **Rod-based** | Anet A8, Wanhao i3, Prusa clones | Acrylic/sheet | 8mm smooth rods + LM8UU |
| **V-slot** | Ender 3, CR-10, Voxelab Aquila | 2020/2040 aluminum | V-slot + POM wheels |

The original specification (ADR-001 + ADR-021) assumed rod-based donors:
- M10 threaded rod frame (buy new, ~$30-45 AUD)
- Dual 8mm smooth rods scavenged from donors

### The Problem with V-Slot Donors

Ender 3 is arguably the most common donor printer in 2026. Under the original spec, an Ender 3 scavenger must:
1. Discard the aluminum extrusions (no use in M10 frame)
2. Buy 8× stainless smooth rods (~$43 AUD)
3. Buy 22× IGUS bearings (~$30 AUD)
4. **Total added cost: ~$73-90 AUD**

This violates the scavenger philosophy: "use what you have."

### The Insight

The MDF base serves two functions:
1. **Mass damping** — absorbs vibration from the frame
2. **Squaring jig** — precision assembly reference

With MDF as the foundation, the frame type becomes a **variable** rather than a constant. Whether M10 threaded rods or aluminum extrusions, the MDF provides:
- Geometric reference for squaring
- Mass to dampen resonance
- Consistent Z-axis mounting

The **M10 + MDF** combination is particularly elegant because:
- M10 is adequately stiff (not overkill like M12)
- MDF compensates for any remaining flexibility
- The system is heavy enough to dampen, light enough to move
- MDF is the precision reference (no need for machinist skills)

## Decision

We adopt a **Multi-Frame Architecture** with three supported paths, all sharing a common MDF base:

### Amalgam Scaffold (M10 + Smooth Rods)

| Component | Specification |
|-----------|---------------|
| Frame | M10 threaded rod skeleton |
| Base | MDF squaring jig + damping mass |
| Motion | Dual 8mm smooth rods, vertical stacking |
| Bearings | LM8LUU (X), LM8UU (Y/Z) |
| Best donors | Anet A8, Wanhao i3, Prusa clones |

**Character:** The heritage path. RepRap Darwin tribute with industrial "tractor" aesthetic.

**Why choose Scaffold:**
- RepRap heritage (inspired by the original Darwin)
- Industrial "tractor" aesthetic — threaded rod is honest, visible engineering
- Hardware-store availability
- Forces scavenger mindset (rod-based donors)
- Differentiated from commercial designs
- M10 frame adds mass for vibration damping

### Amalgam Mill (Extrusion + V-Slots)

| Component | Specification |
|-----------|---------------|
| Frame | Aluminum extrusion (2020/2040) |
| Base | MDF squaring jig + damping mass |
| Motion | V-slot rails + POM wheels |
| Bearings | POM V-wheels (3-4 per carriage) |
| Best donors | Ender 3, CR-10, Voxelab Aquila |

**Character:** The zero-waste path. Uses everything from your Ender donors.

**Why choose Mill:**
- Ender 3 is the most common donor
- Uses ALL scavenged parts (zero waste)
- Proven motion system (Ender 5 style)
- ~$70-90 cheaper than forcing smooth rods
- Cleaner aesthetic than threaded rod

### Amalgam Lathe (Extrusion + Smooth Rods)

| Component | Specification |
|-----------|---------------|
| Frame | Aluminum extrusion (2020/2040) |
| Base | MDF squaring jig + damping mass |
| Motion | Dual 8mm smooth rods, vertical stacking |
| Bearings | IGUS drylin (recommended) or LM8UU |
| Best donors | Ender 3 + purchased rods, or mixed donors |

**Character:** The precision upgrade. Best motion quality, still under budget.

**Why choose Lathe:**
- **Superior motion system** — smooth rods + IGUS bushings outperform POM wheels
- IGUS is self-lubricating, maintenance-free, quieter than linear bearings
- No eccentric nut adjustments, no flat spots developing over time
- Combines modern frame (extrusion) with proven motion (smooth rods)
- Two Ender 3 donors @ $50-60 each + ~$75 for rods/IGUS = still under $250 AUD
- Best choice if you prioritize motion quality over zero-waste

### The Shared Foundation

All paths share:
- **MDF base** — squaring jig + mass damping
- **Z-drop architecture** — bed moves in Z only (ADR-023)
- **Triple-Z leveling** — three independent Z-motors (ADR-005)
- **Cartesian X-Y** — head on X, gantry on Y (not Core-XY)
- **Toolhead** — Pitan extruder + E3D V6 (ADR-019, ADR-004)
- **Electronics** — Dual-MCU Klipper or MKS SKIPR (ADR-012)

## Who Is Amalgam For?

**Got one donor?** Just add Klipper to it. Amalgam isn't for you.

**Got two matching donors?** Perfect. Pick your frame path:
- **Two smooth-rod donors** (Anet A8, Wanhao, Prusa clones) → **Scaffold** (buy M10 rods)
- **Two V-slot donors** (Ender 3, CR-10, Aquila) → **Mill** (zero-waste) or **Lathe** (buy rods for better motion)
- **Mixed donors** (one extrusion + one smooth-rod) → **Lathe** (use extrusions + scavenged rods)

**Want to buy new?** Just buy a Bambu A1 Mini. This project is for scavengers.

### Cost Breakdown (Two Donors, Matched)

| Item | Scaffold | Mill | Lathe |
|------|----------|------|-------|
| Two matching donors | $100-120 | $100-120 | $100-120 |
| MDF base | $15-20 | $15-20 | $15-20 |
| Frame material | M10 rods: $30-45 | $0 | $0 |
| Motion (rods/bearings) | $0 | $0 | ~$75* |
| Pitan gear | $2 | $2 | $2 |
| Klicky microswitch | $2 | $2 | $2 |
| Misc (wires, bolts) | $40 | $40 | $40 |
| **Total** | **~$190-230** | **~$160-185** | **~$235-280** |

*Lathe motion cost: ~$43 for 8× stainless rods + ~$30 for IGUS bushings

**Optional:** Add MKS SKIPR (~$130) for cleaner single-board electronics: **~$290-410**

All paths achieve the **<$300 AUD target** (Lathe is at the upper end but still qualifies).

### Choosing Between Mill and Lathe (Ender Donors)

If you have two Ender 3 donors, you have a choice:

| Factor | Mill | Lathe |
|--------|------|-------|
| **Cost** | $160-185 | $235-280 |
| **Motion quality** | Good | Better |
| **Maintenance** | POM wheels wear, need adjustment | IGUS is maintenance-free |
| **Waste** | Zero (use everything) | Buy rods + bearings |
| **Philosophy** | Maximum scavenger | Pragmatic upgrade |

**Recommendation:** If budget is tight, Mill is excellent. If you want the best motion and can spend ~$75 more, Lathe is the superior choice.

## Consequences

### Benefits

1. **True scavenger philosophy** — use what you have
2. **Ender 3 support** — the most common donor is fully supported (Mill or Lathe)
3. **Three distinct paths** — Scaffold (heritage), Mill (zero-waste), Lathe (precision)
4. **Same print quality** — Klipper + Pitan + E3D V6 equalizes all paths
5. **Simple requirement** — two donors, pick your path
6. **Parametric flexibility** — config.py branches on donor type

### Trade-offs

1. **More documentation** — three paths to explain
2. **More CAD work** — brackets differ per path
3. **Testing burden** — must validate all three paths
4. **Potential confusion** — users must choose a path

### What This Enables

- **Wizard improvement:** "What donor(s) do you have?" drives path selection
- **Conditional docs:** Quarto shows relevant steps per path
- **STL generation:** build123d outputs correct parts for chosen path
- **Fair comparison:** Cost estimates accurate for each donor type

## Differentiation from Other Projects

| Project | Frame | Motion | Kinematics | Cost |
|---------|-------|--------|------------|------|
| **Amalgam Scaffold** | M10 threaded rod + MDF | Smooth rods | Cartesian, Z-drop | <$300 AUD |
| **Amalgam Mill** | Aluminum extrusion + MDF | V-slots | Cartesian, Z-drop | <$300 AUD |
| **Amalgam Lathe** | Aluminum extrusion + MDF | Smooth rods | Cartesian, Z-drop | <$300 AUD |
| Voron Legacy | Aluminum extrusion | Smooth rods | Core-XY | ~$600 USD |
| Mercury One | Ender 5 conversion | V-slots | Core-XY | Ender 5 + $200+ |
| Ender 5 | Aluminum extrusion | V-slots | Cartesian, Z-drop | ~$350 AUD new |

Amalgam is unique in combining:
- **RepRap threaded-rod heritage** (Scaffold path)
- **Scavenger economics** (all paths)
- **Modern Klipper intelligence** (all paths)
- **MDF squaring jig** (all paths)

## Physics Comparison

### Frame Stiffness (Bending)

| Frame Member | Bending Stiffness (EI) | Relative |
|--------------|------------------------|----------|
| M10 Steel Rod | ~98,000 | 1× |
| M12 Steel Rod | ~204,000 | 2× |
| 2020 Aluminum | ~483,000 | 5× |
| 2040 Aluminum | ~3,850,000 | 39× |

Aluminum extrusion is stiffer, but:
- M10 is "adequate" for 70-120mm/s target speeds
- MDF base compensates with mass damping
- Klipper Input Shaping cancels resonance
- M10 has the "tractor" aesthetic

### Motion Comparison

| System | Deflection @ 360mm | Pros | Cons |
|--------|-------------------|------|------|
| Dual 8mm smooth rods + LM8UU | 0.033mm | Precision, proven | Requires rod donors or purchase |
| Dual 8mm smooth rods + IGUS | 0.033mm | Precision, maintenance-free, quiet | Must purchase (~$75) |
| V-slot + POM wheels | ~0.05mm | Zero cost from donors | Wheel wear, periodic adjustment |

Smooth rods with IGUS (Lathe) offer the best motion quality. V-slot with POM wheels (Mill) is acceptable and zero-cost from Ender donors. Input Shaping compensates for minor differences.

## Implementation Notes

### Config Parameters

```python
# Frame path selection
FRAME_TYPE = "SCAFFOLD"  # or "MILL", "LATHE"

# Derived settings
if FRAME_TYPE == "SCAFFOLD":
    FRAME_MATERIAL = "M10_THREADED"
    MOTION_SYSTEM = "SMOOTH_ROD_DUAL"
    BEARING_TYPE = "LM8UU"
elif FRAME_TYPE == "MILL":
    FRAME_MATERIAL = "ALUMINUM_EXTRUSION"
    MOTION_SYSTEM = "V_SLOT"
    BEARING_TYPE = "POM_WHEELS"
elif FRAME_TYPE == "LATHE":
    FRAME_MATERIAL = "ALUMINUM_EXTRUSION"
    MOTION_SYSTEM = "SMOOTH_ROD_DUAL"
    BEARING_TYPE = "IGUS"
```

### Wizard Flow

1. "What donor printer(s) do you have?"
2. → Detect donor type (rod-based, V-slot, mixed)
3. → Recommend path (Scaffold, Mill, or Lathe)
4. → Generate appropriate STLs, BOM, Klipper config

### Documentation Structure

```
docs/guides/
├── scaffold-build.qmd    # M10 + smooth rods (heritage)
├── mill-build.qmd        # Extrusion + V-slots (zero-waste)
├── lathe-build.qmd       # Extrusion + smooth rods (precision)
└── common/
    ├── z-axis.qmd        # Shared Triple-Z assembly
    ├── toolhead.qmd      # Shared Pitan + E3D V6
    └── electronics.qmd   # Shared Klipper setup
```

## Quality Consistency

All paths achieve the same print quality because:

1. **Same toolhead:** Pitan + E3D V6 + CHT nozzle
2. **Same firmware:** Klipper with Input Shaping, Pressure Advance
3. **Same Z-system:** Triple-Z kinematic leveling
4. **Same calibration:** ADXL345 resonance measurement

The frame and motion type affect resonance frequency, not quality. Input Shaping measures and compensates.

## References

- ADR-001: M10 Threaded Rod Skeleton
- ADR-005: Triple-Z Kinematic Leveling
- ADR-021: Dual-Rod Motion System
- ADR-023: Z-Drop Architecture
- PHILOSOPHY.md: "Tractor with a Racecar Brain"
- [RepRap Darwin](https://reprap.org/wiki/Darwin): Original threaded-rod heritage
- [Voron Legacy](https://vorondesign.com/voron_legacy): Extrusion + smooth rod validation
- [Ender 5](https://www.creality.com/products/ender-5-3d-printer): V-slot Cartesian Z-drop reference
- AI Conversation: "Multi-Frame Architecture Discussion" (2025-01-28)
