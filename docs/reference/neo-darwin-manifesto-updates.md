# Neo-Darwin Manifesto Updates (Consolidated)

This document contains all updated sections based on frame analysis and extruder selection discussions. Sections are marked with suggested destination files.

---

# ══════════════════════════════════════════════════════════════
# MANIFESTO.md - Philosophy and Mission (Keep Short)
# ══════════════════════════════════════════════════════════════

## The Mission

To prove that **software intelligence can overcome analog hardware limitations**, using scavenged parts, printed components, and open-source firmware.

Neo-Darwin is a **Tractor with the Brain of a Racecar**: heavy, reliable, battle-tested hardware given precision through Klipper's advanced motion control.

## Core Principles

### 1. Accessibility Over Optimisation

Design choices prioritise availability, simplicity, and reuse over theoretical performance gains. If a part is difficult to source, proprietary, or requires a specialised kit, it cannot be a reference component.

A design that performs 95% as well but is buildable by twice as many people is the superior design.

### 2. No Quality Penalty for Lower Tiers

All build tiers produce **equivalent print quality**. Higher tiers reduce wiring complexity, sourcing difficulty, and configuration effort—they do not unlock better prints.

Tier 1 builders are not building an inferior printer. They are building the same printer with more effort and ingenuity.

### 3. Scavengability as First-Class Requirement

Reference designs must:
- Tolerate part variation
- Accept imperfect or reused components
- Work with metric hardware commonly found in old printers, appliances, or office equipment

If a design assumes precision parts or narrow tolerances, it is optional by definition.

### 4. No Downward Complexity

Higher-performance components must never force additional mechanical or alignment complexity onto lower tiers of the build.

If supporting a component requires mid-span braces, precision alignment jigs, or structural patches at Tier 1, that component cannot be reference—regardless of its performance benefits.

### 5. Mechanical Honesty

The printer should be understandable as a machine. Designs should expose how forces flow, favour visible and inspectable mechanisms, and avoid hidden complexity.

This supports learning, debugging, and modification—core RepRap values.

## What Neo-Darwin Is

- A high-mass, low-cost, fully parametric 3D printer
- Built from M10 threaded rod frame and scavenged/commodity components
- Controlled by Klipper for precision beyond what the hardware "should" achieve
- Targeting: **<$300 AUD, 220×220×280mm build volume, MK3-class quality**

## What Neo-Darwin Is Not

- A speed demon (50-80mm/s, not 200mm/s)
- A plug-and-play appliance (you will learn how it works)
- A Voron alternative (different goals, different philosophy)
- The "best" printer (it's the most *accessible* quality printer)

## The Tractor Philosophy

> *If you want a printer, buy one. If you want to understand a printer, build this.*

Old tractors were cast iron and weighed tons. Modern tractors are lighter, more efficient, same work output. Neo-Darwin is a modern tractor—lighter than its ancestors, but still built for reliability over speed, understanding over convenience.

---

# ══════════════════════════════════════════════════════════════
# SPECIFICATION.md - Reference Build Specification
# ══════════════════════════════════════════════════════════════

## Reference Specification Summary

| Parameter | Reference Spec | Notes |
|-----------|----------------|-------|
| **Build Volume** | 220 × 220 × 280 mm | Tier 3 reference |
| **Maximum Build Volume** | 235 × 235 × 280 mm | Scavenger beds accepted |
| **Frame** | M10 threaded rod | Buy new, not scavenged |
| **Motion Rods** | M10 smooth rod | Scavengeable from photocopiers |
| **Motion Bearings** | LM10UU | |
| **Extruder** | Pitan (Printed Titan) | Single-drive, GT2 pulleys |
| **Extruder Motor** | NEMA17 (NEMA14 for M8 builds) | |
| **Hotend** | E3D V6 or quality clone | |
| **Nozzle** | 0.4mm brass (default) | 0.6mm optional |
| **Bed** | 220×220 or 235×235 heated | Scavenged acceptable |
| **Electronics (Tier 3)** | MKS SKIPR + CANBus | |
| **Electronics (Tier 1/2)** | Donor boards, multi-MCU | |
| **Firmware** | Klipper | |
| **Target Price** | <$300 AUD | Tier 3 all-in |
| **Print Speed** | 50-80 mm/s | Not a speed printer |
| **Target Quality** | MK3-class | Reliability over speed |

---

## Frame Specification

### M10 Threaded Rod (Reference)

M10 threaded rod is selected for the frame skeleton.

| Factor | M8 | M10 | M12 |
|--------|-----|------|------|
| Cross-sectional area | ~50 mm² | ~78 mm² | ~113 mm² |
| Rigidity vs M8 | Baseline | ~1.5× stiffer | ~2.3× stiffer |
| Weight per metre | ~0.3 kg | ~0.5 kg | ~0.7 kg |
| Nut size (hex) | 13mm | 17mm | 19mm |
| Scavengeability | Common | Very common | Less common |
| Bracket bulk | Compact | Moderate | Chunky |

**Why M10:**
- 17mm wrench is nearly universal in household toolkits
- Automotive abundance (suspension, engine mounts, seat rails)
- Allows sleeker printed brackets than M12
- Sufficient rigidity for spans up to 450-500mm

**Critical: Buy New Rod**

While M10 threaded rod is theoretically scavengeable from automotive and industrial sources, **new rod is strongly recommended**. 

Frame geometry depends on straight stock. Scavenged threaded rod may carry invisible bends or work-hardening that propagate alignment errors throughout the build. The cost (~$15-20 AUD from Bunnings) is trivial compared to the debugging time a bent frame causes.

**Optional Alternatives:**
- M12: Maximum mass damping, "tank" aesthetic, larger builds
- M8: Smaller builds where bracket compactness matters

---

## Motion System Specification

### Smooth Rods

The X and Y gantry use smooth rods with linear bearings in a fixed-gantry Cartesian layout.

| Configuration | Max Span | Extruder | Calculated Sag | Status |
|---------------|----------|----------|----------------|--------|
| M10 smooth rod | 250mm | Pitan + NEMA17 | ~0.024mm | ✅ Reference |
| M10 smooth rod | 280mm | Pitan + NEMA17 | ~0.035mm | ✅ Acceptable |
| M10 smooth rod | 300mm | Pitan + NEMA17 | ~0.042mm | ⚠️ Edge case |
| M8 smooth rod | 200mm | Pitan + NEMA14 | ~0.015mm | ✅ Scavenger option |
| M8 smooth rod | 250mm | Pitan + NEMA14 | ~0.035mm | ⚠️ Borderline |
| M8 smooth rod | 280mm | Any | >0.05mm | ❌ Requires supports |

**Scavenging Sources:**
- M10: Photocopiers, large office printers, scanners, CNC equipment
- M8: Donor 3D printers (Ender, Anet, Prusa clones, i3 variants)

**Design Rule:** The project deliberately avoids structural "patches" (mid-span supports, braces) that exist only to accommodate overweight toolheads or excessive spans. If a configuration requires supports, it is outside the reference specification.

### Motion System Layout

**Y-Axis (The "Tracks"):**
- Two parallel M10 smooth rods mounted to frame
- Run front-to-back
- Held by printed Corner Pucks clamped to M10 threaded rod frame
- Y-Pucks slide on LM10UU bearings

**X-Gantry (The "Bridge"):**
- Two M10 smooth rods in horizontal parallel layout
- 50mm centre-to-centre spacing (RepRap standard)
- Locked into Left and Right Y-Pucks
- One puck houses X motor, other houses idler

**X-Carriage (The "Plow"):**
- Printed bearing block (Mendel90-inspired)
- Three LM10UU bearings (two on one rod, one on other—avoids over-constraint)
- Pitan extruder mounts on top
- Nozzle passes between the two rods

**Belt Configuration:**
- Standard Cartesian belts (not CoreXY)
- Y-motion: Single motor at back with drive shaft connecting both sides
- X-motion: Single GT2 belt loop along X-gantry

---

## Extruder Specification

### Pitan Extruder (Reference)

The Pitan (Printed Titan-style) extruder is the reference specification.

**Why Pitan:**
- Fully printable body and gears
- Uses GT2 pulleys (scavengeable from donor printers)
- Drive shaft from M5/M6 threaded rod or scavenged stepper shaft
- Single-drive topology (avoids dual-gear meshing issues)
- Weight: ~160-220g depending on motor (within motion system load budget)
- No proprietary gear kits required

**Motor Options:**
- NEMA17: Reference for M10 builds (~220-250g total toolhead)
- NEMA14: Preferred for M8 builds (~160-180g total toolhead)

**Key Components:**
| Part | Source |
|------|--------|
| Body, gears, lever | Printed (PETG or Nylon recommended) |
| GT2 pulley (small) | Scavenged from donor printer X/Y axis |
| GT2 belt (short loop) | Scavenged from donor printer |
| Drive shaft | M5/M6 threaded rod OR scavenged stepper shaft |
| Bearings | 623/625 or similar (scavengeable or ~$2-5) |
| Idler bearing | 608 or similar |
| Tension spring | Scavenged or hardware store |
| Stepper motor | Scavenged or purchased |

### Why Not Wade?

The Wade Geared Extruder embodies the original Tractor philosophy—raw torque through mechanical advantage. It was seriously considered as the reference.

However, at ~280-350g with NEMA17, Wade exceeds the motion system load budget:
- M8 rods at 250mm span: ~0.09mm sag (borderline)
- M10 rods at 250mm span: ~0.04mm sag (acceptable but reduced margin)

Supporting Wade would require either:
- Mid-span rod supports (adds complexity)
- Reduced build volume (defeats purpose)
- M10-only builds (excludes M8 scavengers)

All of these push complexity downward to Tier 1/2 builders, violating the "No Downward Complexity" principle.

The Pitan inherits Wade's spirit (geared reduction, printed simplicity, scavengeable hardware) while respecting the motion system constraints. It is a lighter tractor for the same field.

### Optional Extruders (Tinker Options)

These are valid alternatives for experienced builders but excluded from reference:

| Extruder | Why Optional |
|----------|--------------|
| Wade Geared | Exceeds load budget, requires M10 + reduced spans |
| Orbiter v1.5 | Requires specific belt + pulley configuration |
| Voron M4 | Requires precision gears or gear kit |
| Sherpa Mini | Requires purchased gear kit |
| ProtXtruder | Requires purchased gear kit |
| Wristwatch | Niche mechanical complexity |

**These do not materially improve print quality** for Neo-Darwin's target use case. They may appeal to builders interested in mechanical experimentation.

---

## Hotend Specification

### E3D V6 (Reference)

The E3D V6 form factor (including quality clones) is the reference hotend.

**Why V6:**
- Battle-tested reliability over many years
- Massive ecosystem and documentation
- Quality clones readily available (~$10-20 AUD)
- Known thermal behaviour, easy to tune
- Compatible with Pitan mounting

**Clone Acceptance:** Quality V6 clones are explicitly acceptable for reference builds. The V6 ecosystem is mature enough that clones perform reliably.

### Nozzle Specification

**Reference Set:**
- 0.4mm brass (default, general purpose)
- 0.6mm brass (faster prints, structural parts)

**Optional:**
- 0.2mm brass (fine detail work)
- CHT/high-flow nozzles (speed builds)
- Hardened steel (abrasive filaments)

### Why Not High-Flow by Default?

CHT-style nozzles increase melt surface area, enabling higher volumetric flow. However:

**Neo-Darwin targets 50-80mm/s.** At these speeds:
- Stock V6 delivers ~8-10 mm³/s (sufficient)
- CHT enables ~15-20 mm³/s (not needed)

**High-flow nozzles add:**
- Temperature tuning sensitivity
- More internal geometry (debris traps)
- Greater clone quality variability
- No quality improvement at reference speeds

CHT is supported for builders wanting speed experiments, but stock brass nozzles are correct for the reference specification.

---

## Electronics Specification

### Tier 3: MKS SKIPR

The reference Tier 3 build uses MKS SKIPR with integrated:
- Raspberry Pi compute module
- TMC drivers
- CANBus support
- ADXL345 for input shaping

**Approximate cost:** ~$130 AUD

**Why SKIPR:**
- All-in-one reduces wiring complexity
- Built-in Pi eliminates separate SBC
- CANBus enables clean toolhead wiring
- ADXL integrated for input shaping calibration

### Tier 2: Multi-MCU (Two Donor Boards)

Uses two scavenged mainboards in Klipper multi-MCU configuration.

**Required drivers:** X, Y, Z1, Z2, Z3, E (minimum 6)

If single donor board lacks sufficient drivers, second board provides remainder. May require two PSUs from donors.

**Approximate cost:** ~$150 AUD (mostly consumables and new parts)

### Tier 1: Single Donor + Separate Host

Single scavenged mainboard plus Raspberry Pi or old laptop running Klipper.

**Constraints:**
- May require creative driver assignment
- Manual bed leveling (no automated z-tilt)
- Klippy probe still functional

**Approximate cost:** ~$100 AUD

### Tier Comparison

| Aspect | Tier 1 | Tier 2 | Tier 3 |
|--------|--------|--------|--------|
| Electronics cost | ~$0 (scavenged) | ~$0-50 | ~$130 |
| Wiring complexity | High | Medium | Low |
| Configuration effort | High | Medium | Low |
| Z-leveling | Manual | Z-tilt macro | Z-tilt macro |
| **Print quality** | **Reference** | **Reference** | **Reference** |

**Critical:** All tiers produce equivalent print quality. Tier 3 is not "better"—it is easier to assemble and debug.

---

# ══════════════════════════════════════════════════════════════
# RATIONALE.md - Design Rationale and Appendices
# ══════════════════════════════════════════════════════════════

## Appendix A: Extruder Topology Rationale

### Single-Drive vs Dual-Drive

The Neo-Darwin reference design adopts a **single-drive** extruder topology. This decision is based on mechanical behaviour, tolerance to variation, and long-term stability across scavenged components.

### Single-Drive Characteristics

A single-drive extruder uses one driven hobbed gear and a spring-loaded idler to grip filament.

**Advantages:**
- Single torque source
- Single periodic error source
- Tolerant of minor misalignment
- Fails gradually and visibly
- Compliance is smooth and continuous
- Easy to compensate with pressure advance

### Dual-Drive Concerns

Dual-drive extruders use two opposing driven gears that must mesh correctly and remain synchronised under load.

**Additional dependencies:**
- Matched gear tooth profiles
- Precise centre-to-centre spacing
- Consistent preload
- Uniform wear between gears

**Failure modes:**
- Torque ripple from gear mismatch
- Micro stick-slip behaviour
- Subtle extrusion inconsistency
- Difficult to diagnose with scavenged/printed parts

### Design Conclusion

Dual-drive extruders primarily increase pushing force and filament grip robustness—valuable for very soft filaments or extreme flow rates.

For Neo-Darwin's target materials (PLA, PETG, light TPU) and speeds (50-80mm/s), single-drive provides equivalent print quality with:
- Fewer failure modes
- Greater tolerance to part variation
- Lower mechanical complexity
- Easier firmware compensation

---

## Appendix B: Motion System Load Budget

### Purpose

This appendix defines acceptable mass limits for moving components to ensure predictable motion behaviour across all build tiers.

### Reference Toolhead Mass Budget

**Target: 220-260g** (with NEMA17)
**Preferred: 160-200g** (with NEMA14, for M8 builds)

| Component | NEMA17 Build | NEMA14 Build |
|-----------|--------------|--------------|
| Extruder (printed) | 30-50g | 30-50g |
| Stepper motor | 180-220g | 80-120g |
| V6 hotend + mount | 50-80g | 50-80g |
| **Total** | **260-350g** | **160-250g** |

### Deflection Calculations

Using Euler-Bernoulli beam theory for simply-supported beam with centre point load:

```
δ = (P × L³) / (48 × E × I)

Where:
  δ = deflection (mm)
  P = load per rod (N) — total load ÷ 2
  L = span (mm)
  E = Young's modulus (200,000 N/mm² for steel)
  I = moment of inertia (mm⁴)

Moment of inertia for solid circular rod:
  I = (π × d⁴) / 64

Reference values:
  M8:  I ≈ 201 mm⁴
  M10: I ≈ 491 mm⁴
  
M10 is 2.44× stiffer than M8 (geometry alone)
```

### The L³ Relationship

Span length is cubed in the deflection equation. This is critical:

| Span | Relative Sag |
|------|--------------|
| 200mm | 1.0× (baseline) |
| 250mm | 1.95× |
| 300mm | 3.38× |

Doubling span increases sag by 8×. This is why span limits matter more than rod diameter.

### Design Rule

Reference components must not exceed the motion system load budget or require structural compensation (mid-span supports, braces) to function correctly.

Components exceeding the budget are classified as Optional regardless of performance benefits.

---

## Appendix C: Frame Analysis Summary

### Why Not CoreXY?

CoreXY offers efficient belt paths and theoretically higher speeds. However:

**Alignment sensitivity:** CoreXY requires precise belt routing and tensioning. Misalignment causes geometric errors that are difficult to diagnose.

**Tuning complexity:** Two motors work together for each axis. Debugging motion issues requires understanding the coupled system.

**Part variation tolerance:** Scavenged pulleys and belts with slight dimensional variation can introduce systematic errors.

**Neo-Darwin's position:** At 50-80mm/s, fixed-gantry Cartesian achieves equivalent print quality with:
- Simpler belt paths
- Independent axis debugging
- Greater tolerance for part variation
- Mechanical clarity (easy to understand force flow)

CoreXY is supported as an Optional architecture for experienced builders but excluded from reference.

### Why Smooth Rods Instead of Linear Rails?

Linear rails offer high stiffness and compactness but:

**Environmental sensitivity:** Rails require clean environments and consistent lubrication. Dust and debris cause binding.

**Evaluation difficulty:** Scavenged rails vary widely in condition. Worn balls, damaged raceways, and contamination are hard to detect visually.

**Alignment precision:** Rails require careful mounting to avoid preload issues.

**Smooth rod advantages:**
- Abundant from donor equipment
- Condition is visually inspectable (roll on glass, sight down length)
- Tolerate minor misalignment
- Fail gradually and visibly
- Easy to clean, replace, and realign

For Neo-Darwin's spans and loads, smooth rods provide sufficient stiffness without additional sourcing or maintenance burden.

Linear rails are supported as an Optional upgrade but not required for reference builds.

---

## Appendix D: Hotend Thermal Analysis

### Stock V6 Flow Capacity

At typical printing temperatures:

| Material | Temp | Max Flow (stock 0.4mm) |
|----------|------|------------------------|
| PLA | 210°C | ~10 mm³/s |
| PETG | 240°C | ~8 mm³/s |
| ABS | 250°C | ~9 mm³/s |

### Speed Translation

```
Volumetric flow = layer height × line width × speed

Example (0.2mm layer, 0.44mm width):
  8 mm³/s ÷ (0.2 × 0.44) = ~91 mm/s max
```

Neo-Darwin targets 50-80mm/s—comfortably within stock V6 capacity.

### CHT Benefit Analysis

CHT nozzles approximately double flow capacity:

| Nozzle | Flow Capacity | Max Speed (0.2mm layer) |
|--------|---------------|-------------------------|
| Stock 0.4mm | ~8-10 mm³/s | ~90-110 mm/s |
| CHT 0.4mm | ~15-20 mm³/s | ~170-220 mm/s |

**Conclusion:** CHT enables speeds Neo-Darwin doesn't target. The added complexity (tuning, clone variation) isn't justified for the reference use case.

---

# ══════════════════════════════════════════════════════════════
# GOVERNANCE.md - Reference vs Optional Policy
# ══════════════════════════════════════════════════════════════

## Classification Principles

### Reference Components

A **Reference Component** is the baseline expectation for all builds.

A component may be Reference if it:
- Is fully printable or uses generic hardware
- Can be built without proprietary or precision kits
- Is tolerant of part variation
- Is reasonably achievable through scavenging or common suppliers
- Does not exceed the motion system load budget
- Does not impose print-quality advantage over alternatives

Reference components must:
- Be documented first and most thoroughly
- Be supported across all tiers
- Define the mechanical and electrical assumptions of the printer

### Optional Components

An **Optional Component** is a valid alternative that:
- Improves ease of assembly, compactness, or aesthetics
- Appeals to experienced builders or tinkerers
- May require purchased kits or specialised parts

Optional components must not:
- Be required for acceptable print quality
- Invalidate reference documentation
- Create perception that reference builds are inferior

**Optional components are explicitly non-normative.** They are choices, not expectations.

---

## Classification Checklist

A component is **Optional by default**. It becomes **Reference** only if it passes ALL criteria:

### A. Cross-Tier Compatibility
- [ ] Can this component be used in Tier 1, Tier 2, and Tier 3 without modification?
- [ ] If tier-specific, is it clearly marked as Optional?

### B. No Downward Complexity
- [ ] Does this component avoid increasing mechanical complexity in lower tiers?
- [ ] Does it avoid requiring:
  - Mid-span supports or braces
  - Precision alignment procedures
  - Special tools
  - Structural patches

### C. Print Quality Parity
- [ ] Does this component provide equivalent (not superior) print quality to alternatives?
- [ ] If it improves only convenience or aesthetics, is that worth fragmenting the build?

### D. Scavengeability Test
- [ ] Can this component be built using:
  - Printed parts
  - Generic fasteners
  - Commonly scavenged hardware
- [ ] Does it avoid dependence on proprietary kits or narrow-tolerance parts?

### E. Load Budget Compliance
- [ ] Does toolhead mass stay within 260g (NEMA17) or 200g (NEMA14)?
- [ ] Does this avoid requiring structural compensation?

### F. Failure Mode Clarity
- [ ] Are failure modes visible, understandable, and repairable?
- [ ] Can a builder diagnose issues without specialised tools?

---

## Classification Rule

**A component is Optional by default.**

It becomes Reference only if it passes all checklist criteria without exception.

This rule exists to prevent:
- Scope creep
- Tier fragmentation
- "Better" components that increase complexity
- Perception that lower tiers are inferior

---

## Current Classifications

### Extruders
| Component | Classification | Reason |
|-----------|----------------|--------|
| Pitan | **Reference** | Printable, scavengeable, within load budget |
| Wade Geared | Optional | Exceeds load budget, requires structural compensation |
| Orbiter v1.5 | Optional | Requires specific belt/pulley configuration |
| Voron M4 | Optional | Requires precision gears |
| Sherpa Mini | Optional | Requires purchased gear kit |

### Frame
| Component | Classification | Reason |
|-----------|----------------|--------|
| M10 threaded rod | **Reference** | Available, adequate rigidity, universal tooling |
| M12 threaded rod | Optional | Heavier, larger brackets, less common |
| M8 threaded rod | Optional | Smaller builds only |

### Motion
| Component | Classification | Reason |
|-----------|----------------|--------|
| M10 smooth rod | **Reference** | Scavengeable, adequate stiffness |
| M8 smooth rod | Optional | Limited to ≤200mm span with light extruder |
| Linear rails | Optional | Evaluation difficulty, environmental sensitivity |

### Hotend
| Component | Classification | Reason |
|-----------|----------------|--------|
| E3D V6 / clone | **Reference** | Battle-tested, massive ecosystem |
| CHT nozzles | Optional | Speed benefit not needed at reference speeds |

### Motion Architecture
| Component | Classification | Reason |
|-----------|----------------|--------|
| Fixed-gantry Cartesian | **Reference** | Simple, debuggable, tolerant |
| CoreXY | Optional | Alignment sensitivity, tuning complexity |

---

# ══════════════════════════════════════════════════════════════
# FAQ.md - Frequently Asked Questions
# ══════════════════════════════════════════════════════════════

## Design Decisions

### Why not CoreXY?

CoreXY is an efficient and capable motion system, but it introduces additional belt paths, alignment sensitivity, and tuning complexity. These factors increase the build and debugging burden, particularly when using scavenged or mixed-quality components.

Neo-Darwin prioritises:
- Mechanical clarity
- Ease of diagnosis
- Tolerance of part variation
- Predictable behaviour under imperfect assembly

A fixed-gantry Cartesian layout achieves equivalent print quality at the speeds and accelerations targeted by the project (50-80mm/s), while remaining easier to understand, assemble, and repair.

CoreXY does not materially improve print quality for the reference use case. It is treated as Optional.

---

### Why smooth rods instead of linear rails?

Linear rails offer high stiffness and compactness, but they require:
- Clean environments
- Careful alignment
- Consistent lubrication
- Difficult-to-evaluate condition when scavenged

Smooth rods and linear bearings:
- Are widely available from donor printers and office equipment
- Tolerate minor misalignment
- Fail gradually and visibly
- Are easier to clean, replace, and realign

For the spans and loads used in Neo-Darwin, smooth rods provide sufficient stiffness without introducing additional sourcing or maintenance burden.

Linear rails are supported as Optional upgrades but not required for reference builds.

---

### Why not dual-drive extruders?

Dual-drive extruders primarily improve pushing force and filament grip—valuable for very soft filaments (TPU) or extreme flow scenarios.

However, they introduce gear mesh dependencies:
- Matched tooth profiles required
- Precise spacing critical
- Printed gears introduce torque ripple
- Failure modes are subtle and hard to diagnose

For PLA, PETG, and moderate TPU at Neo-Darwin's target speeds, single-drive (Pitan) provides equivalent print quality with:
- Fewer failure modes
- Greater tolerance for scavenged/printed parts
- Easier firmware compensation

Dual-drive is supported as Optional for builders wanting experimentation.

---

### Why not Wade extruder?

The Wade Geared Extruder was seriously considered—it embodies the Tractor philosophy of raw torque through mechanical advantage.

However, at 280-350g with NEMA17, Wade exceeds the motion system load budget:
- Causes excessive sag on M8 rods
- Pushes M10 rods toward their limits
- Would require mid-span supports or reduced build volume

This violates the "No Downward Complexity" principle. Supporting Wade would make Tier 1/2 builds more complex.

The Pitan inherits Wade's spirit (geared, printable, scavengeable) while respecting motion system constraints. Wade is supported as Optional for M10-only builds with reduced spans.

---

### Why not a high-flow hotend by default?

CHT-style nozzles increase volumetric flow capacity, enabling faster printing. However:

Neo-Darwin targets **50-80mm/s**. At these speeds:
- Stock V6 delivers ~8-10 mm³/s (sufficient)
- CHT enables ~15-20 mm³/s (not needed)

High-flow nozzles add:
- Temperature tuning sensitivity
- Clone quality variability
- No quality improvement at reference speeds

CHT is supported as Optional for speed experiments. Stock brass nozzles are correct for reference builds.

---

### Why buy M10 threaded rod instead of scavenging?

M10 threaded rod is theoretically scavengeable from automotive and industrial sources (aircon brackets, cable tray, suspension components).

However, **frame geometry depends on straight stock**. Scavenged threaded rod may carry:
- Invisible bends
- Work-hardening from previous stress
- Corrosion weakening

A bent frame rod propagates error into everything mounted to it. The debugging cost of a misaligned frame far exceeds the ~$15-20 AUD cost of new rod from Bunnings.

**Scavenge where quality is visible. Buy where hidden defects propagate systemic error.**

---

## Tier Questions

### Is Tier 3 a better printer than Tier 1?

**No.** All tiers produce equivalent print quality.

Tier 3 reduces:
- Wiring complexity
- Configuration effort
- Debugging time

Tier 3 does **not** improve:
- Print quality
- Dimensional accuracy
- Surface finish
- Reliability

Tier 1 builders trade effort for cost. Tier 3 builders trade cost for convenience. Both get the same printer.

---

### Can I mix tiers?

Yes. The tier system describes common configurations, not rigid requirements.

Examples:
- Tier 2 electronics with Tier 3 motion system: Fine
- Scavenged bed with new frame rod: Fine
- Pitan with different motor than specified: Fine (check load budget)

The reference specification defines what's tested and documented. Variations are expected.

---

### What if I already have a Wade extruder?

Wade is supported as Optional. It works on:
- M10 smooth rods only
- Spans ≤250mm recommended
- May require reduced acceleration

Document your build and share results. Community data on Wade configurations helps future builders.

---

## Build Questions

### What's the minimum I need to buy new?

For a scavenger-heavy build:

**Must buy new:**
- M10 threaded rod for frame (~$15-20 AUD)
- Heated bed (if not scavengeable, ~$20-40 AUD)
- Possibly bearings (~$10-20 AUD)
- Fasteners, wire, connectors (~$20-30 AUD)

**Scavengeable:**
- Smooth rods (photocopiers, large printers)
- Stepper motors (donor printers)
- GT2 belts and pulleys (donor printers)
- Power supply (donor printers, electronics)
- Control board (donor printers)
- Hotend (if you have a spare)

**Total minimum buy:** ~$50-100 AUD depending on scavenge success

---

### What donor printers work best?

**Excellent donors:**
- Prusa i3 variants (MK2, MK3 clones)
- Creality Ender 3/5 (steppers, belts, pulleys, bed)
- Anet A8 (steppers, rods if M8 build)
- Anycubic i3 Mega (very rigid, good steppers)

**Good for parts:**
- Office photocopiers (M10 smooth rods, large steppers)
- Flatbed scanners (smooth rods, small steppers)
- Laser printers (belts, pulleys, rods)

**Avoid relying on:**
- Very cheap printers with bent rods
- Anything with proprietary connectors
- Printers with integrated boards you can't reflash

---

### Can I use an old laptop instead of Raspberry Pi?

Yes. An old laptop running Linux works well for Klipper:
- More processing headroom than Pi
- Built-in screen for Mainsail/Fluidd
- Webcam support trivial
- Often free (old MacBooks, ThinkPads)

The only requirement is USB connection to the control board and ability to run Klipper host software.
