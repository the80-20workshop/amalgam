# Neo-Darwin: Extruder Selection & Decision Record

## Executive Summary

After extensive evaluation of weight, cost, scavengability, mechanical performance, drive architecture, and Klipper compatibility, the **Pitan Extruder** has been selected as the Neo-Darwin reference specification.

**Key Decision: Single-Drive Architecture**

Neo-Darwin uses single-drive extruders exclusively. Dual-drive designs (BMG, Sherpa, Orbiter, LGX) introduce gear mesh artifacts that affect print quality consistency — a hidden factor in why Bambu Lab printers achieve exceptional results with their single-drive design.

### Extruders Evaluated

| # | Extruder | Drive | Motor | Cost | Weight | Status |
|---|----------|-------|-------|------|--------|--------|
| 1 | **Greg's Wade** | ✅ Single | NEMA17 | ~$2-5 | 360-600g | ⚠️ Heritage (PLA/PETG) |
| 2 | **MK8/MK9** | ✅ Single | NEMA17 | ~$0-6 | 150-200g | ⚠️ Ultra-Scavenger |
| 3 | Sherpa Mini | ❌ Dual | NEMA14 | ~$22-34 | 110-127g | ❌ Dual-drive |
| 4 | Sherpa Micro | ❌ Dual | NEMA14 | ~$20-34 | ~85g | ❌ Dual-drive |
| 5 | Orbiter v1.5 | ❌ Dual | LDO specific | ~$60-100 | 140-150g | ❌ Dual-drive, cost |
| 6 | Bondtech LGX Lite | ❌ Dual | NEMA14 | ~$120-150 | 150-165g | ❌ Dual-drive, cost |
| 7 | **Pitan** | ✅ Single | NEMA17 | ~$4-10 | 260-300g | ✅ **Reference Spec** |
| 8 | Voron (various) | ❌ Dual | Various | ~$60-120 | 100-150g | ❌ Cost, complexity |
| 9 | BMG Clone | ❌ Dual | NEMA17 | ~$15-25 | 250-350g | ❌ Dual-drive |

### Recommendation Summary

| Tier | Extruder | Cost | Notes |
|------|----------|------|-------|
| ✅ **Reference Spec** | Pitan + NEMA17 | ~$4-10 | Best balance for Tractor philosophy |
| ⚠️ Heritage Option | Wade + Pancake NEMA17 | ~$2-5 | RepRap nostalgia, PLA/PETG only |
| ⚠️ Ultra-Scavenger | MK8 Direct | ~$0-6 | If you have one, PLA/PETG only |

**Important:** This is the *reference specification*. As a tinkerer/maker, you're free to use whatever extruder configuration suits you—perhaps you have one in your parts bin. Use that!

---

## The Decision Philosophy

### Why This Matters for "The Tractor"

The Neo-Darwin project follows the "Tractor with the Brain of a Racecar" philosophy:

1. **Quality over Speed** — Not chasing 300mm/s; targeting reliable 80-120mm/s
2. **Scavenger-Friendly** — Parts from donor printers, hardware stores, and minimal purchases
3. **Klipper Intelligence** — Software compensates for mechanical simplicity
4. **Budget-Conscious** — Target $300 AUD total build cost
5. **Repairability** — Print your own replacement parts

The extruder choice must serve these principles, not fight them.

### The Bambu Lab X1C Insight

Modern printers like the Bambu Lab X1C prove that a well-tuned single direct-drive extruder achieves superior print quality through **software intelligence** rather than raw mechanical complexity.

> **Key Finding:** A 150g extruder with Klipper Input Shaping produces better quality than a 600g extruder without it, at any speed under 150mm/s.

This insight shaped our entire evaluation process.

### Single-Drive vs Dual-Drive: A Critical Decision

Early in our evaluation, we made a key architectural decision: **Neo-Darwin will use a single-drive extruder**.

**What's the difference?**

| Type | Mechanism | Examples |
|------|-----------|----------|
| **Single-drive** | One drive gear + one idler bearing | Pitan, Wade, MK8, E3D Titan |
| **Dual-drive** | Two meshing drive gears, both grip filament | BMG, Sherpa Mini, Orbiter, LGX Lite |

**Why single-drive for Neo-Darwin?**

Dual-drive extruders have a hidden quality issue: **gear meshing artifacts**. When two drive gears mesh, microscopic variations in tooth engagement create periodic pressure fluctuations on the filament. This manifests as subtle but measurable extrusion inconsistencies.

> **The Bambu Lab Secret:** One reason Bambu Lab printers achieve exceptional print quality is their use of single-drive extruders. While the community often focuses on their motion system and software, the single-drive design eliminates gear mesh artifacts entirely.

**Engineering trade-offs:**

| Factor | Single-Drive | Dual-Drive |
|--------|--------------|------------|
| Extrusion consistency | ✅ No mesh artifacts | ⚠️ Periodic micro-variations |
| Filament grip (rigid) | ✅ Adequate with good tension | ✅ Excellent |
| Filament grip (TPU) | ⚠️ Requires careful tuning | ✅ Superior |
| Mechanical complexity | ✅ Simpler | ⚠️ More parts |
| Failure modes | ✅ Fewer | ⚠️ Gear wear, alignment |

For Neo-Darwin's quality-focused philosophy at 80-120mm/s, the single-drive advantages outweigh the dual-drive TPU benefits. We're building a Tractor for consistent quality, not a race car for exotic filaments.

**This decision shaped our entire evaluation.** Several excellent extruders (Sherpa Mini, Orbiter, LGX Lite) were evaluated but ultimately not selected as reference spec due to their dual-drive architecture.

---

## Options Evaluated

### Single-Drive Extruders (Preferred)

### 1. Greg's Wade Geared Extruder (Classic RepRap)

The Greg's Wade is the "Flat-6 Engine" of 3D printing—mechanical, geared, visible torque. Pure RepRap heritage from 2007-2009.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 5.22:1 (39:11 or similar, varies by version) |
| Motor | Full NEMA17 (or pancake variant) |
| Weight | 450-600g (full motor) / 360-410g (pancake) |
| Drive | Single hobbed bolt + idler |
| Original Design | 3.00mm filament (adaptable to 1.75mm) |

**Pros:**
- ✅ Single-drive design (no gear mesh artifacts)
- Massive torque — 5.22:1 ratio with NEMA17 = overkill for any filament
- Zero proprietary parts (M8 bolts, 608 bearings, printed gears)
- Full repairability (print replacement gears for $0.50)
- Heat creep resistance (motor far from hotend)
- True RepRap heritage and philosophy

**Cons:**
- **Heavy with full NEMA17** — 450-600g causes significant gantry sag
- Originally designed for 3.00mm filament (longer filament path)
- 1.75mm adaptation has exposed filament path — TPU will buckle
- Forces upgrade to M10 rods with full motor (can't use scavenged M8)
- Inertia causes ringing at direction changes

**Pancake Motor Variant:**

With a pancake NEMA17 (~160g vs ~350g), the Wade drops to ~360-410g total. The 5.22:1 gear ratio provides enough mechanical advantage that the reduced motor torque (~17 N·cm motor × 5.22 = ~89 N·cm output) remains adequate for PLA/PETG.

**Engineering Analysis:**

Rod sag calculations:
- M8 rods + Wade (full motor, 600g), 250mm span: ~0.037mm sag (borderline)
- M8 rods + Wade (full motor, 600g), 280mm span: ~0.052mm sag (❌ too much)
- M8 rods + Wade (pancake, 385g), 250mm span: ~0.024mm sag (✅ good)
- M8 rods + Wade (pancake, 385g), 280mm span: ~0.034mm sag (✅ acceptable)
- M10 rods + Wade (full motor), 280mm span: ~0.021mm sag (✅ good)

**Verdict:** The Wade with a pancake NEMA17 becomes M8-compatible and offers pure RepRap heritage. However, the 3.00mm filament path design makes it unsuitable for TPU with 1.75mm filament. Documented as heritage option for PLA/PETG builders who value RepRap roots.

**Status: ⚠️ Heritage Option (PLA/PETG only, pancake motor recommended)**

---

### 2. MK8/MK9 Direct Drive (Ultra-Simple)

The MK8 is the simplest possible extruder — a drive gear mounted directly on the motor shaft with an idler bearing opposite. No gearing, no reduction, pure simplicity.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 1:1 (direct drive, no reduction) |
| Motor | NEMA17 standard |
| Weight | ~150-200g complete |
| Drive | Single MK8 gear + idler |

**Pros:**
- ✅ Single-drive design (no gear mesh artifacts)
- Ultra-simple — fewest parts of any extruder
- Extremely scavengeable (every cheap printer has one)
- Lightweight enables M8 rods easily
- Near-zero cost if scavenged

**Cons:**
- No gear reduction means relying entirely on motor torque
- Less forgiving of partial clogs or high-viscosity filaments
- Higher motor current required for equivalent pushing force
- TPU difficult without the mechanical advantage of gearing

**Cost Breakdown:**
| Component | Cost (AUD) |
|-----------|------------|
| MK8 drive gear | $1-3 (or scavenged) |
| NEMA17 motor | $0 (scavenged) |
| Idler bearing + arm | $0-2 (scavenged/printed) |
| Hardware | $1 |
| **Total** | **$0-6** |

**Engineering Analysis:**

Without gear reduction, motor torque = output torque. A typical NEMA17 provides ~40-45 N·cm, which is adequate for PLA/PETG at moderate speeds but offers no headroom for difficult situations.

Klipper's pressure advance helps compensate for the lack of mechanical advantage, making MK8 more viable than it would be on Marlin.

**Verdict:** Viable ultra-budget option for PLA/PETG if you already have one. The lack of gear reduction limits performance ceiling. Not recommended as primary choice but documented for completeness.

**Status: ⚠️ Ultra-Scavenger Option (PLA/PETG only)**

---

### Dual-Drive Extruders (Evaluated but Not Selected)

The following extruders were carefully evaluated but not selected as reference spec due to their dual-drive architecture, which introduces gear mesh artifacts that affect print quality consistency.

### 3. Sherpa Mini (Annex Engineering)

Developed by Annex Engineering, the Sherpa Mini is the de facto standard for lightweight direct-drive in the Voron community. Uses BMG clone gears in a compact **dual-drive** configuration.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 5:1 (50:10) or 6.25:1 (50:8) |
| Motor | Round NEMA14 pancake with pinion |
| Weight | 110-127g complete |
| Drive | ❌ BMG clone dual-drive |

**Pros:**
- Extremely light (~120g) — no gantry sag
- BMG gears ubiquitous ($3-8, available everywhere)
- Massive community (PDF manual, Discord, years of refinement)
- Dual-drive excellent for TPU
- Battle-tested (thousands in service)
- Printable body

**Cons:**
- ❌ **Dual-drive architecture** — gear mesh artifacts affect consistency
- Requires specific NEMA14 pancake motor with integrated pinion (~$14-21 AUD)
- Heat-set inserts require soldering iron
- BMG quality varies by vendor
- Motor not scavengeable from donor printers

**Cost Breakdown:**
| Component | Cost (AUD) |
|-----------|------------|
| BMG clone gear set | $3-8 |
| Round NEMA14 pancake motor | $14-21 |
| Hardware, inserts, PTFE | ~$5 |
| **Total** | **$22-34** |

**Engineering Analysis:**

Rod sag calculations (250mm span):
- M8 rods + Sherpa (NEMA14): ~0.015mm sag (excellent)

The Sherpa Mini is mechanically excellent. Its rejection for Neo-Darwin is purely architectural — the dual-drive design conflicts with our quality philosophy.

**Verdict:** Excellent extruder for builders who prioritize TPU capability and lightweight toolheads over absolute extrusion consistency. Not selected due to dual-drive architecture and non-scavengeable motor.

**Status: ❌ Not Recommended (dual-drive architecture)**

---

### 4. Sherpa Micro (Annex Engineering)

The Sherpa Micro is an even more compact version of the Sherpa Mini, designed for the smallest possible toolhead footprint.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Gear Ratio | ~4:1 |
| Motor | Round NEMA14 pancake with 6T pinion |
| Weight | ~85g complete |
| Drive | ❌ Dual-drive (BMG-style) |

**Pros:**
- Extremely compact and lightweight (~85g)
- Excellent for space-constrained builds
- Printable body
- Good community support (shares ecosystem with Sherpa Mini)

**Cons:**
- ❌ **Dual-drive architecture** — gear mesh artifacts
- Requires specific NEMA14 motor with integrated pinion (~$14-21 AUD)
- Motor not scavengeable
- Less torque than Sherpa Mini due to smaller gearing

**Cost Breakdown:**
| Component | Cost (AUD) |
|-----------|------------|
| BMG clone gear set | $3-8 |
| Round NEMA14 pancake motor (6T) | $14-21 |
| Hardware, inserts | ~$3-5 |
| **Total** | **$20-34** |

**Verdict:** Even more compact than Sherpa Mini but shares the same dual-drive limitation. The smaller gearing also reduces torque headroom.

**Status: ❌ Not Recommended (dual-drive architecture)**

---

### 5. Orbiter v1.5 (LDO Motors)

The Orbiter is a high-performance planetary geared extruder designed by Róbert Lőrincz in cooperation with LDO Motors. Features an innovative orbiting gear mechanism.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 7.5:1 (planetary) |
| Motor | LDO-36STH20-1004AHG (specific motor required) |
| Weight | ~140-150g complete |
| Drive | ❌ Dual-drive planetary |
| Filament Force | Up to 9.4kg pushing force |

**Pros:**
- Very high gear ratio (7.5:1) in compact package
- Excellent filament pushing force
- High-quality injection molded housing (glass-fiber reinforced nylon)
- Good for high-speed printing and flexible filaments
- Proven design with strong community

**Cons:**
- ❌ **Dual-drive architecture** — planetary gears still mesh
- **Requires specific LDO motor** (~$50-75 AUD) — not scavengeable
- Expensive complete kit (~$75-100 AUD)
- Proprietary gears — clone quality questionable (~$10 AUD but risky)
- Injection molded parts — not printable for repairs

**Cost Breakdown:**
| Component | Cost (AUD) |
|-----------|------------|
| Orbiter v1.5 kit with motor | $75-100 |
| OR: Clone gears + LDO motor | $10 + $50-75 |
| **Total** | **$60-100** |

**Engineering Analysis:**

The Orbiter's 7.5:1 ratio provides exceptional torque from a small motor, enabling high acceleration extrusion. However, the planetary gear system is still dual-drive — two gears grip the filament, introducing mesh artifacts.

**Verdict:** Excellent high-performance extruder, but the specific motor requirement, cost, and dual-drive architecture exclude it from Neo-Darwin consideration. The clone gears available on AliExpress (~$10) are a quality gamble.

**Status: ❌ Not Recommended (dual-drive, specific motor, cost)**

---

### 6. Bondtech LGX Lite

The Bondtech LGX Lite is a commercial extruder using Bondtech's "Large Gears eXtruder" technology with oversized drive gears for increased filament contact.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Gear Ratio | ~3.5:1 (44:10, 37:17 compound) |
| Motor | Round NEMA14 36mm pancake |
| Weight | ~150-165g complete |
| Drive | ❌ Dual-drive (Bondtech LGX gears) |
| Filament Tension | 3-position lever (open/rigid/flexible) |

**Pros:**
- High-quality commercial product
- Large drive gears (18mm Ø) = 50% more filament contact area
- Excellent tension adjustment system
- Good for flexible filaments
- Professional injection-molded PA12 housing

**Cons:**
- ❌ **Dual-drive architecture** — two meshing gears
- **Expensive** — ~$120-150 AUD complete with motor
- Commercial product — no printed parts, no customization
- Requires specific NEMA14 motor (~$25-35 AUD)
- Not scavengeable, not repairable with printed parts

**Cost Breakdown:**
| Component | Cost (AUD) |
|-----------|------------|
| LGX Lite V2 with motor | $120-150 |
| LGX Lite V2 without motor | $85-100 |
| NEMA14 36mm motor | $25-35 |
| **Total** | **$120-150** |

**Verdict:** Premium commercial option with excellent build quality, but the cost exceeds our entire extruder budget, and the dual-drive architecture conflicts with our quality philosophy. Represents the opposite of RepRap principles — buy rather than build.

**Status: ❌ Not Recommended (dual-drive, cost, commercial)**

---

### Selected Reference Specification

### 7. Pitan Extruder (Selected Reference Spec)

The Pitan (Printable Titan) is a 3D-printed clone of the E3D Titan, designed for the RepRap philosophy—lightweight, easy to assemble, and optimized for NEMA17 motors with full repairability.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 3:1 (same as E3D Titan) |
| Motor | NEMA17 standard or pancake |
| Weight | ~260-300g (with NEMA17) |
| Drive | ✅ Single drive gear + idler (Titan-style) |

**Pros:**
- ✅ **Single-drive design** — no gear mesh artifacts
- **Motor scavengeable** — Uses standard NEMA17 from any donor printer
- Fully printable gears and body (true RepRap spirit)
- 3:1 gear ratio provides excellent torque
- Moderate weight enables M8 rods at 250mm span
- Can use pancake NEMA17 for lighter builds
- Simple design is easy to maintain and repair

**Cons:**
- Heavier than Sherpa Mini (but lighter than Wade)
- Single-drive less aggressive than dual-drive for flexible filaments (TPU)
- Less community support than Sherpa

**Cost Breakdown:**
| Component | Cost (AUD) |
|-----------|------------|
| Pitan printed parts (body + gears) | $0.50-1 (filament) |
| NEMA17 motor | $0 (scavenged) |
| 608 bearings | $0-2 |
| Hobbed bolt or MK8 drive gear | $2-5 |
| Hardware (springs, fasteners) | $1-2 |
| **Total** | **$3.50-10** |

**Engineering Analysis:**

Rod sag calculations:
- M8 @ 250mm span + Pitan/NEMA17: ~0.024mm sag (very good)
- M8 @ 280mm span + Pitan/NEMA17: ~0.034mm sag (acceptable)
- M10 @ 280mm span + Pitan/NEMA17: ~0.014mm sag (excellent)

**Why Pitan Wins for Neo-Darwin:**

1. **Scavengeable motor** — The NEMA17 from your Ender 3 donor works perfectly
2. **Enables M8 rods** — Don't need to upgrade to M10 for reasonable spans
3. **3:1 geared torque** — Handles PLA, PETG reliably; adequate for careful TPU
4. **Printable** — "If a gear breaks, you have a new one before your coffee gets cold"
5. **Budget** — $4-10 vs $18-28 for Sherpa saves money for other components

**Status: ✅ Selected as Reference Specification**

---

### Other Extruders Evaluated

### 8. Voron Extruders (Stealthburner, Clockwork 2, Galileo 2)

These represent the "Formula 1" extruders—designed for Voron CoreXY machines chasing 300-500mm/s.

**Specifications:**
| Attribute | Value |
|-----------|-------|
| Weight | 100-150g |
| Cost | $60-120 (Bondtech kit required) |
| Complexity | Very high |

**Why Not Recommended:**

| Issue | Impact on Neo-Darwin |
|-------|----------------------|
| Cost | $60-120 exceeds entire extruder budget |
| Proprietary | Requires Bondtech/BMG kits that can't be scavenged |
| Complexity | Many tiny parts, precision assembly |
| Overkill | Designed for 300mm/s; we target 80-120mm/s |
| Philosophy Mismatch | Racing speed vs. reliable quality |

**The Defense:**

> "We chose the Pitan not because Voron extruders are bad, but because they solve problems we don't have. Neo-Darwin isn't chasing speed records—it's chasing reliable, repairable, affordable quality."

**Status: ❌ Not Recommended**

---

### 9. Complete BMG Clone (Pre-assembled)

Pre-assembled BMG extruders with full NEMA17 motors, sold as complete units.

**Why Not Recommended:**

| Issue | Impact |
|-------|--------|
| Weight | 250-350g causes gantry sag |
| Not RepRap | No printed parts, no customization |
| Motor Waste | Full NEMA17 better used for Z-axis |
| Design | Optimized for Bowden, not direct drive |

**Status: ❌ Not Recommended**

---

## The Decision: Pitan as Reference Spec

### Why Pitan?

The Pitan wins on multiple fronts for Neo-Darwin's philosophy:

| Factor | Pitan | Dual-Drive Options | Wade |
|--------|-------|-------------------|------|
| Drive Architecture | ✅ Single (no mesh artifacts) | ❌ Dual (mesh artifacts) | ✅ Single |
| Motor Scavengeable | ✅ NEMA17 (everywhere) | ❌ Specific motors | ✅ NEMA17 |
| Total Cost | $4-10 | $20-150 | $2-5 |
| Weight | ~280g | 85-165g | 360-600g |
| M8 Rod Compatible | ✅ Yes (≤280mm) | ✅ Yes | ⚠️ Pancake only |
| 1.75mm Filament Path | ✅ Designed for it | ✅ Yes | ⚠️ 3mm adapted |
| TPU Capability | ⚠️ With care | ✅ Good | ❌ Poor |
| Repair Printability | ✅ Full body + gears | ⚠️ Varies | ✅ Full |

**The single-drive + scavengeable motor combination is decisive.** The Pitan delivers consistent extrusion quality without gear mesh artifacts, using motors from any donor printer, at a fraction of the cost of alternatives.

### Why Not Sherpa Mini (or other dual-drive)?

The Sherpa Mini is mechanically excellent — lightweight, strong community, great TPU handling. But:

1. **Dual-drive architecture** introduces gear mesh artifacts
2. **Specific motor required** — NEMA14 pancake with integrated pinion (~$14-21)
3. **BMG gears** — quality varies, and meshing gears = periodic extrusion variations

For Neo-Darwin's quality-focused philosophy, the single-drive Pitan produces more consistent results.

### Why Not Wade?

The Wade offers pure RepRap heritage and massive torque, but:

1. **3.00mm design** — adapted 1.75mm path struggles with TPU
2. **Heavy** — requires pancake motor or M10 rods
3. **Less refined** — older design lacks modern conveniences

The Wade is documented as a heritage option for builders who value RepRap roots and only print PLA/PETG.

### The Quote That Captures It

> "If a gear breaks on a Pitan, you have a new one before your coffee gets cold. That's the RepRap spirit."

---

## Reference Configuration

### Bill of Materials

| Component | Source | Cost (AUD) |
|-----------|--------|------------|
| Pitan printed parts (body + gears) | Print yourself | $0.50-1 |
| Hobbed bolt or MK8 drive gear | AliExpress/hardware | $2-5 |
| NEMA17 motor | Scavenge from donor | $0 |
| 608 bearings (×2) | Hardware store/scavenge | $0-2 |
| M3 hardware + springs | Hardware store | $1-2 |
| PTFE tube + fitting | Hardware store | $1 |
| **Total** | | **$4.50-11** |

### Rod Requirements

| Configuration | Rod Size | Span | Sag | Verdict |
|---------------|----------|------|-----|---------|
| Pitan + NEMA17 | M8 | 250mm | 0.024mm | ✅ Reference spec |
| Pitan + NEMA17 | M8 | 280mm | 0.034mm | ✅ Acceptable |
| Pitan + NEMA17 | M10 | 280mm | 0.014mm | ✅ Excellent |
| Pitan + Pancake | M8 | 280mm | 0.020mm | ✅ Ideal lightweight |

### Klipper Configuration

```ini
[extruder]
step_pin: E_STEP
dir_pin: E_DIR
enable_pin: !E_EN
microsteps: 16
rotation_distance: 22.678  # Calibrate for your setup
gear_ratio: 3:1            # Pitan standard
nozzle_diameter: 0.4
filament_diameter: 1.750

[tmc2209 extruder]
uart_pin: E_UART
run_current: 0.5           # Start low, adjust as needed
hold_current: 0.4
stealthchop_threshold: 0

[firmware_retraction]
retract_length: 0.5
retract_speed: 35
unretract_extra_length: 0
unretract_speed: 35
```

### Expected Performance

| Metric | Value |
|--------|-------|
| Print Speed | 80-120mm/s (quality range) |
| Acceleration | 1000-1500mm/s² |
| Layer Heights | 0.1-0.3mm |
| Materials | PLA, PLA+, PETG (TPU with care) |
| Consistency | ±0.05mm (with bed mesh) |

---

## Alternative Configurations

### Heritage Option: Greg's Wade + Pancake NEMA17

For builders who value pure RepRap heritage and only print PLA/PETG:

| Component | Cost (AUD) |
|-----------|------------|
| Printed gears and body | $0.50 |
| Pancake NEMA17 motor | $0-15 (scavenged or purchased) |
| 608 bearings | $0-2 (scavenged) |
| Hobbed bolt | $2-3 |
| Hardware | $1-2 |
| **Total** | **$3.50-22** |

**Key considerations:**
- Use pancake NEMA17 to keep weight under 410g (M8 compatible)
- Full NEMA17 requires M10 rods
- 3.00mm adapted design — not suitable for TPU with 1.75mm filament
- 5.22:1 gear ratio provides massive torque headroom

**When to choose Wade:**
- You value pure RepRap heritage over modern conveniences
- You only print PLA and PETG (no flexible filaments)
- You have or can scavenge a pancake NEMA17
- You appreciate the "Flat-6 Engine" aesthetic of visible gears

### Ultra-Scavenger Option: MK8 Direct Drive

For extreme budget constraints or if you already have one:

| Component | Cost (AUD) |
|-----------|------------|
| MK8 drive gear | $0-3 (scavenged or purchased) |
| NEMA17 motor | $0 (scavenged) |
| Idler assembly | $0-2 (scavenged/printed) |
| Hardware | $1 |
| **Total** | **$0-6** |

**Key considerations:**
- No gear reduction — relies entirely on motor torque
- Lightweight (~150-200g) — excellent for M8 rods
- Klipper pressure advance helps compensate for 1:1 ratio
- Best for moderate speeds with PLA/PETG

**When to choose MK8:**
- You already have one from a donor printer
- Ultra-minimal budget
- Only printing PLA/PETG at moderate speeds
- You value simplicity over performance headroom

### Use What You Have

**This is the most important option.**

If you have an extruder in your parts bin—Titan, Hemera, or even a dual-drive BMG—**use it**. The Neo-Darwin carriage design is meant to be adaptable.

The Pitan is the *reference specification*, not a mandate. The whole point of being a tinkerer is making it your own. If you already own a Sherpa Mini or Orbiter, the dual-drive concerns are academic — use what you have and enjoy printing.

The single-drive recommendation is about optimal quality for new builds, not a condemnation of existing equipment.

---

## Spare Parts Strategy

### Recommended Spares Kit (~$5-10 AUD)

| Part | Qty | Cost | Notes |
|------|-----|------|-------|
| Hobbed bolt or MK8 gear | 1 | $2-3 | Drive gear replacement |
| 608 bearings | 4 | $2 | Common wear item |
| Pitan body (printed) | 1 set | $0.50 | Print during initial build |
| Printed gears | 1 set | $0.25 | Print spares with body |
| PTFE tube | 1m | $1 | Cut to length as needed |
| M3 hardware assortment | Various | $2 | For any repairs |

With these spares, you're covered for 5+ years of operation.

---

## Responding to Critics

### "Why not just use a Sherpa Mini like everyone else?"

> "The Sherpa Mini is mechanically excellent, but it has two issues for Neo-Darwin: First, its dual-drive architecture introduces gear mesh artifacts that affect extrusion consistency — the same reason Bambu Lab uses single-drive. Second, it requires a specific NEMA14 pancake motor that can't be scavenged. The Pitan delivers cleaner extrusion with motors from any donor printer."

### "Dual-drive artifacts? That sounds like audiophile nonsense."

> "Fair skepticism! The effect is subtle but measurable — periodic micro-variations in extrusion pressure as gear teeth mesh and unmesh. For most printing it's invisible. But Neo-Darwin targets quality over speed, and the single-drive architecture removes one variable from the quality equation. It's also why Bambu Lab — known for print quality — uses single-drive designs."

### "The Orbiter has 7.5:1 gearing — isn't that better?"

> "The Orbiter is excellent for high-speed printing where you need rapid extrusion acceleration. But Neo-Darwin targets 80-120mm/s where the Pitan's 3:1 ratio is plenty. The Orbiter also requires a specific $50-75 LDO motor and costs $75-100 complete. For our philosophy, the Pitan's $4-10 with scavenged motor makes more sense."

### "The Wade has more torque — isn't that better?"

> "The Wade's 5.22:1 ratio provides impressive torque, but it was designed for 3.00mm filament. The adapted 1.75mm filament path has too much exposure — TPU will buckle and jam. With a pancake motor it's M8-compatible and makes a fine heritage option for PLA/PETG, but the Pitan handles all materials better."

### "Why not a Voron extruder? They're proven."

> "Voron extruders are designed for 300mm/s+ racing with dual-drive BMG gears. Neo-Darwin targets 80-120mm/s quality printing with single-drive consistency. The $60-120 cost of a Clockwork 2 kit equals our entire extruder budget plus half the frame. We'd rather spend that money on a better heated bed or quality thermistors."

### "Can I use [other extruder] instead?"

> "Absolutely! The Pitan is our reference spec, but you're a maker — use what you have. If there's a Sherpa, Orbiter, or BMG in your parts bin, use it. The dual-drive concerns are about optimal quality for new builds, not a condemnation of existing equipment. The documentation is a starting point, not a constraint."

---

## Conclusion

### The Pitan Decision

The Pitan extruder embodies the Neo-Darwin philosophy:

| Principle | How Pitan Delivers |
|-----------|-------------------|
| Quality-Focused | ✅ Single-drive = no gear mesh artifacts |
| Scavenger-Friendly | Uses NEMA17 from any donor printer |
| Budget-Conscious | $4-10 total cost |
| Repairable | Print replacement parts yourself |
| Mechanically Sound | 3:1 gearing + Klipper = consistent extrusion |
| M8 Compatible | Enables scavenged rods at practical spans |

### The Final Word

> *"A tractor doesn't win races. It pulls loads reliably. The Pitan doesn't chase 300mm/s. It produces quality prints consistently, inexpensively, and repairably — without the hidden artifacts of dual-drive designs."*

**Your extruder, your choice.** The Pitan is our answer — but Neo-Darwin is your machine.

---

## References

### Extruders Evaluated
- Pitan Extruder: Community designs on Printables/Thingiverse (Printable Titan clone)
- Greg's Wade: Original RepRap design, various community versions
- MK8/MK9: Standard on Creality, Anet, and most budget printers
- Sherpa Mini/Micro: `github.com/Annex-Engineering/Sherpa_Mini-Extruder`
- Orbiter v1.5: `orbiterprojects.com` (designed by Róbert Lőrincz)
- Bondtech LGX Lite: `bondtech.se/product/lgx-lite-v2-large-gears-extruder/`
- Voron Extruders: `vorondesign.com`

### Component Sourcing
- BMG Gear Clones: AliExpress (Trianglelab, Mellow, FYSETC)
- NEMA14 Pancake Motors: AliExpress, KB-3D, West3D (~$14-21 AUD)
- LDO Motors: Official distributors, ~$50-75 AUD for Orbiter-specific

### Engineering Calculations
- Rod sag analysis: See `extruder.md` for full deflection calculations
- Motor torque specifications: LDO Motors datasheets

---

*Document prepared for the Neo-Darwin Project*
*"A Tractor with the Brain of a Racecar"*
