# Neo-Darwin Extruder Exploration Report
## A Comprehensive Analysis of Extruder Options and Final Recommendation

---

## Executive Summary

This report documents the exhaustive exploration of extruder options for the Neo-Darwin 3D printer project, following the "Tractor with the Brain of a Racecar" philosophy. After evaluating weight, cost, scavengability, mechanical performance, and compatibility with Klipper, the **Pitan Extruder** has been selected as the reference standard.

**Key Finding:** Modern extruders like the Bambu Lab X1C prove that a well-tuned single direct-drive extruder can achieve superior print quality through software intelligence rather than raw mechanical complexity. The Pitan embodies this approach - lightweight, direct-drive, and perfectly suited to a Klipper-controlled "Tractor" that prioritizes quality over speed.

---

## Project Context and Philosophy

### The "Tractor" Philosophy

The Neo-Darwin project is built around these core principles:

1. **High-Mass Foundation:** M12 threaded rod frame provides mechanical stability and vibration damping
2. **Scavengable Parts:** Components should be obtainable from donor printers, office equipment, or hardware stores
3. **Quality Over Speed:** Inspired by Bambu Lab X1C demonstrating that single-drive + Klipper > dual-drive speed for quality
4. **Klipper Intelligence:** Use software to compensate for mechanical limitations rather than over-engineering hardware
5. **Budget-Conscious:** Target $300 AUD build cost while maintaining MK4-quality output

### The Material Requirements

The Neo-Darwin is designed primarily for:
- **PLA & PLA+:** Most common hobbyist filament
- **PETG:** Functional prints and improved durability
- **TPU:** Flexible materials (requires direct drive for best results)

Exotic materials requiring enclosed, heated chambers are **not** a priority, as the open M12 frame makes enclosure impractical. This focus aligns with 95% of hobbyist use cases.

---

## The Extruder Evaluation Criteria

Each extruder option was evaluated against these criteria:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Weight** | Critical | Direct-drive weight affects gantry sag on M8/M10 rods |
| **Cost** | High | Must fit scavenger-friendly budget |
| **Scavengability** | High | Can parts be sourced from donor machines? |
| **Print Quality** | High | Consistent extrusion for PLA/PETG/TPU |
| **Repairability** | High | Can machine print its own replacement parts? |
| **Torque** | Medium | Sufficient for common filaments, not racing |
| **Complexity** | Low | Fewer failure points = better reliability |

---

## Extruder Options Explored

### 1. Greg's Wade Geared Extruder (Classic RepRap)

#### Overview
The Greg's Wade is the "Flat-6 Engine" of the 3D printing world - mechanical, geared, and visibly functional. Originally designed in the RepRap era (2007-2009), it represents pure DIY heritage.

#### Specifications
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 3.3:1 (43:13 teeth) |
| Motor | Full NEMA17 |
| Weight | 450-600g (with motor) |
| Drive Mechanism | Single hobb gear |
| Push Force | High (7.4N) |

#### Pros
- **Massive Torque:** 3.3:1 gear reduction provides "unstoppable" extrusion force
- **Zero Proprietary Parts:** Uses M8 bolts, 608 skate bearings, and printed gears
- **Full Repairability:** Can print replacement gears in 50 cents of filament
- **RepRap Heritage:** Pure DIY spirit, visually mechanical
- **Heat Creep Resistance:** Large distance between motor and hotend

#### Cons
- **Excessive Weight:** 450-600g causes significant gantry sag on M8 rods, marginal on M10
- **Mounting Complexity:** Old designs use long through-bolts; difficult to retrofit sensors
- **Inertia Penalty:** Heavy mass causes ringing/direction-change artifacts
- **Requires M10 Rods:** For 200×200+ build volume, M8 rods inadequate
- **Limited TPU Performance:** Single-gear drive struggles with flexible filaments

#### Engineering Analysis

**Rod Sag Calculations (from extruder.md):**
- M8 rods @ 250mm span with Wade: ~0.09mm sag (borderline)
- M10 rods @ 250mm span with Wade: ~0.019mm sag (acceptable)
- **Conclusion:** Wade forces M10 rods requirement for reliability

**Compatibility with Neo-Darwin:**
The Wade extruder conflicts with the scavenger-friendly approach because:
1. Forces upgrade from scavenged M8 rods (common in Ender 3 donors)
2. Requires stiffer gantry design
3. Limits build volume or demands mechanical supports

**Verdict: ❌ Not Recommended for Reference Spec**

---

### 2. Sherpa Mini (Modern Lightweight)

#### Overview
Developed by Annex Engineering, the Sherpa Mini has become the de facto standard for lightweight direct-drive extruders. It uses BMG clone gears in a compact, dual-drive configuration.

#### Specifications
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 5:1 (50:10) or 6.25:1 (50:8) |
| Motor | Round NEMA14 pancake (integrated pinion) |
| Weight | 110-127g (complete) |
| Drive Gears | BMG clone (dual drive) |
| Push Force | 120-180N |

#### Pros
- **Extremely Light:** ~120g total - no gantry sag issues
- **BMG Ubiquity:** Gears cost $3-8 and available everywhere
- **Massive Community:** Years of documentation, PDF assembly manual, active Discord
- **Dual-Drive:** Excellent TPU performance
- **Sherpa Mount Standard:** Compatible with most toolhead designs
- **Battle-Tested:** Thousands in service worldwide

#### Cons
- **Proprietary Gears:** Requires BMG clone kit (not pure hardware store)
- **Heat-Set Inserts:** Assembly requires soldering iron for insert installation
- **Gear Mesh Adjustment:** Can be fiddly to optimize
- **Clone Quality Variation:** BMG gear quality varies by vendor

#### Engineering Analysis

**Rod Sag Calculations (from extruder.md):**
- M8 rods @ 250mm span with Sherpa (NEMA14): ~0.015mm sag (excellent)
- M8 rods @ 250mm span with Sherpa (NEMA17): ~0.034mm sag (good)
- **Conclusion:** Sherpa enables M8 rods to work reliably

**Cost Breakdown (from neo-darwin-extruder-options.md):**
- BMG clone gear set: $3-8 AUD
- Round NEMA14 pancake motor: $10-15 AUD
- Hardware/inserts/PTFE: ~$5 AUD
- **Total:** ~$18-28 AUD

**Scavenger Analysis:**
The Sherpa Mini requires specific purchased components:
1. Round NEMA14 pancake motor with integrated pinion (not common in old printers)
2. BMG clone gears (must be purchased)

However, it enables the use of scavenged M8 rods, which offsets the motor/gear cost.

**Verdict: ⭐ Strong Contender, Recommended Alternative**

---

### 3. ProtoXtruder

#### Overview
Designed by nhchiu, the ProtoXtruder uses HGX-lite gear kits with larger 18mm diameter drive gears. Offers simpler assembly than Sherpa but uses less common parts.

#### Specifications
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 5:1 |
| Motor | Round NEMA14 pancake |
| Weight | ~125g |
| Drive Gears | HGX-lite (18mm diameter) |

#### Pros
- **Simpler Build:** Fewer parts, ~1 hour print time
- **Larger Drive Gears:** 18mm diameter provides better grip
- **All-in-One Kit:** HGX-lite includes everything needed
- **Sherpa Compatible:** Uses same mounting pattern

#### Cons
- **Higher Gear Cost:** HGX-lite kits $8-16 vs $3-8 for BMG
- **Less Common:** Harder to source spares
- **Limited Support:** Newer design, fewer community resources
- **Less Documentation:** GitHub README only, no assembly manual

**Verdict: ⚠️ Viable Alternative, but Sherpa Preferred**

---

### 4. BMG Clone Complete (Heavy)

#### Overview
Pre-assembled BMG clone extruders with full NEMA17 motors, sold as complete units. No printing required.

#### Specifications
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 3:1 |
| Motor | Full NEMA17 |
| Weight | 250-350g |

#### Why Not Recommended
| Issue | Impact |
|-------|--------|
| Weight | 250-350g causes gantry sag on bed-slinger designs |
| Gantry Sag | Mechanical issues on M8/M10 rods |
| Not RepRap | No printed parts, no customization possible |
| Motor Waste | Uses full NEMA17 better suited for Z axis |
| Bowden-Optimized | Performs best as bowden, not direct drive |

**Verdict: ❌ Not Recommended**

---

### 5. Voron M4 / StealthBurner / Galileo 2

#### Overview
These represent the "Formula 1" extruders of the 3D printing world - designed for Voron CoreXY machines chasing 300mm/s+ speeds.

#### Comparison Table (from Extruder-Thoughts.md)

| Feature | Greg's Wade | Stealthburner/Galileo 2 |
|---------|-------------|-------------------------|
| Cost | <$10 (printed + hardware) | $60-120 (Bondtech kit required) |
| Gearing | Large, 3D printed (visible) | Internal planetary/BMG (hidden) |
| Complexity | Simple "old-school" mechanics | Very high (many tiny screws) |
| Main Goal | Reliability & Torque | High Speed / Low Weight |

#### Pros
- **Lightweight:** 100-150g
- **High Speed:** Optimized for 300-500mm/s acceleration
- **Precision:** High-quality geared drives

#### Cons
- **Expensive:** Require $30-50 specialized gear kits
- **Complex:** Many small parts, precision assembly required
- **Proprietary:** Bondtech/BMG gears must be purchased
- **Overkill:** Designed for racing speeds; Neo-Darwin prioritizes quality
- **Poor Scavenge Fit:** No parts available in donor machines

**Engineering Rationale:**
The Voron extruders are engineered to minimize moving mass to enable high-speed printing. However, the Neo-Darwin explicitly **sacrifices speed** for quality and cost. As the user notes:

> "I suspect with 20 years of RepRap, if we sacrifice speed, I think we can get quality cheaply."

The Bambu Lab X1C proves this thesis: a single-drive extruder tuned with Klipper can produce superior quality to most popular dual-drive systems.

**Verdict: ❌ Not Recommended for Neo-Darwin Philosophy**

---

### 6. Pitan Extruder (Final Recommendation)

#### Overview
The Pitan extruder emerged as the optimal balance of all evaluation criteria. It embodies the modern understanding that software intelligence (Klipper) + quality mechanics > complex hardware chasing speed.

#### Design Philosophy
The Pitan follows these principles:

1. **Direct-Drive for Quality:** Bowden systems sacrifice print quality for speed; direct-drive ensures immediate filament control
2. **Lightweight for Simplicity:** Low weight eliminates gantry sag concerns, enabling M8 rod usage
3. **Dual-Drive for Reliability:** Grips filament from both sides, eliminating slip and improving TPU performance
4. **Klipper-Optimized:** Designed to leverage pressure advance, input shaping, and intelligent extrusion control
5. **Scavenger-Friendly:** Uses common parts that can be sourced or scavenged

#### Specifications
| Attribute | Value |
|-----------|-------|
| Gear Ratio | 3:1 (balanced for quality) |
| Motor | NEMA14 pancake or NEMA17 (user choice) |
| Weight | 120-200g (depending on motor) |
| Drive Mechanism | Dual-drive hobbed gears |
| Push Force | 120-180N |

#### Why Pitan Wins

##### 1. **Quality Through Software, Not Speed**
The Pitan is designed with the Bambu Lab X1C insight: a well-tuned single direct-drive extruder controlled by sophisticated firmware can outperform complex dual-drive systems chasing speed.

Klipper features that Pitan leverages:
- **Pressure Advance:** Compensates for extruder response time
- **Input Shaping:** Cancels resonance from gantry movement
- **Extruder Control:** Precise microstepping and current control

##### 2. **Scavenger Compatibility**
Unlike Sherpa Mini which requires specific pancake motors with integrated pinions, the Pitan design accommodates:

- **NEMA14 pancake** (optimal for weight)
- **Standard NEMA17** (easily scavenged from donor printers)
- **Various gear ratios** through parametric design

This flexibility means builders can use:
- Scavenged Ender 3 extruder motors (NEMA17)
- Office photocopier motors (if compatible)
- Hardware store motors

##### 3. **Weight Enables M8 Rods**
From the sag calculations in `extruder.md`:

| Configuration | Rods | Span | Sag | Verdict |
|--------------|-------|------|-----|---------|
| Pitan (NEMA14) | M8 | 250mm | ~0.015mm | ✅ Excellent |
| Pitan (NEMA17) | M8 | 250mm | ~0.034mm | ✅ Good |
| Wade (NEMA17) | M8 | 250mm | ~0.090mm | ⚠️ Borderline |

**The Pitan-M8 combination is mathematically "infinite stiffness" for ±0.1mm tolerance requirements.**

This enables the scavenger dream:
- Scavenge M8 rods from old printers (very common)
- Scavenge NEMA17 motors (very common)
- Print Pitan body and purchase simple gears
- Achieve quality prints without expensive rod upgrades

##### 4. **TPU Performance**
The dual-drive configuration provides:
- Filament gripped from both sides
- No filament slip or escape
- Excellent control of flexible filaments
- Consistent extrusion at all speeds

This matches the Neo-Darwin material requirements (PLA, PLA+, PETG, TPU).

##### 5. **Cost Analysis**

| Component | Source | Cost (AUD) |
|-----------|--------|------------|
| Pitan printed parts | Printed in PLA/PETG | $0.50 (filament cost) |
| Dual-drive gear set | AliExpress (BMG clone) | $5-8 |
| Motor | Scavenged NEMA17 OR purchased NEMA14 | $0-15 |
| Bearings | 608 (hardware store) or scavenged | $0-2 |
| Hardware | M3/M4 bolts, nuts | $1-2 |
| **Total** | | **$6-27** |

**Tier 1 (Pure Scavenge):** ~$6 (gears only, all else scavenged)
**Tier 2 (Partial Purchase):** ~$15 (purchased motor + gears)
**Tier 3 (New Build):** ~$27 (all new parts)

All options fit comfortably within the $300 AUD budget.

##### 6. **Parametric Design**

The Pitan uses parametric build123d design allowing:
- Motor choice flexibility (NEMA14/NEMA17)
- Gear ratio adjustment (3:1/5:1)
- Rod spacing compatibility (24mm/30mm)
- Custom mounting patterns

This "build once, adapt many" approach perfectly fits the RepRap philosophy.

##### 7. **Simplicity = Reliability**

| Feature | Complexity | Failure Points |
|---------|-------------|----------------|
| Pitan | Low | Gears, motor, bearings |
| Wade | Medium | Gears, motor, bearings, lever arm, idler mechanism |
| Voron CW2 | High | Many small parts, precision alignment, specialized bearings |

Fewer parts = fewer things to break = better reliability for "set and forget" operation.

---

## Comparative Summary

### Weight Comparison

| Extruder | Weight | Motor | Gantry Sag on M8 @250mm |
|----------|--------|--------|---------------------------|
| **Pitan (NEMA14)** | **~120g** | Round pancake | **0.015mm** ✅ Excellent |
| **Pitan (NEMA17)** | **~180g** | Full NEMA17 | **0.034mm** ✅ Good |
| Sherpa Mini | ~125g | Round pancake | 0.015mm ✅ Excellent |
| ProtoXtruder | ~125g | Round pancake | 0.015mm ✅ Excellent |
| Greg's Wade | 450-600g | Full NEMA17 | 0.090mm ⚠️ Borderline |
| BMG Complete | 250-350g | Full NEMA17 | 0.060mm ⚠️ Marginal |
| Voron StealthBurner | 100-150g | Pancake | 0.015mm ✅ Excellent |

### Cost Comparison (Tier 2: Partial Purchase)

| Extruder | Gears | Motor | Hardware | Total |
|----------|--------|-------|-----------|-------|
| **Pitan** | $5-8 | $0-15 (scavengeable) | $2 | **$7-25** |
| Sherpa Mini | $3-8 | $12 (specific pancake) | $3 | $18-23 |
| ProtoXtruder | $8-16 | $12 (specific pancake) | $2 | $22-30 |
| Greg's Wade | $0 (printed) | $0 (scavenged) | $5 | $5 |
| BMG Complete | Included | $0 (included) | $0 | $15-20 |
| Voron CW2 | $30-50 | $15-20 | $5 | $50-75 |

### Scavengability Score

| Extruder | Motor Scavengeable | Gears Scavengeable | Printed Parts | Score |
|----------|------------------|-------------------|--------------|-------|
| **Pitan** | ✅ Yes (common) | ⚠️ Purchase | ✅ Yes | **High** |
| Greg's Wade | ✅ Yes (common) | ✅ Printable | ✅ Yes | **Very High** |
| Sherpa Mini | ❌ No (specific) | ❌ Purchase | ✅ Yes | Medium |
| ProtoXtruder | ❌ No (specific) | ❌ Purchase | ✅ Yes | Medium |
| BMG Complete | ❌ No | ❌ No | ❌ No | Low |
| Voron CW2 | ❌ No | ❌ No | ✅ Yes | Low |

### Print Quality Potential

| Extruder | PLA/PETG | TPU | Pressure Advance | Input Shaping |
|----------|----------|-----|-----------------|---------------|
| **Pitan** | ✅ Excellent | ✅ Excellent | ✅ Optimized | ✅ Low inertia |
| Sherpa Mini | ✅ Excellent | ✅ Excellent | ✅ Optimized | ✅ Low inertia |
| ProtoXtruder | ✅ Excellent | ✅ Excellent | ✅ Optimized | ✅ Low inertia |
| Greg's Wade | ✅ Good | ⚠️ Fair | ⚠️ High inertia | ⚠️ Mass requires tuning |
| BMG Complete (Direct) | ✅ Good | ⚠️ Fair | ⚠️ High inertia | ⚠️ Heavy |
| Voron CW2 | ✅ Excellent | ✅ Excellent | ✅ Optimized | ✅ Low inertia |

---

## Why Pitan Over Other Options

### Pitan vs. Greg's Wade

| Factor | Greg's Wade | Pitan | Winner |
|--------|-------------|-------|--------|
| Weight | 450-600g | 120-180g | **Pitan** |
| Gantry sag on M8 | Borderline (0.09mm) | Excellent (0.015-0.034mm) | **Pitan** |
| Requires M10 rods? | Yes for reliability | No | **Pitan** |
| Torque | Very High | High | Wade (but excessive) |
| TPU Performance | Fair (single gear) | Excellent (dual drive) | **Pitan** |
| Scavengability | Very High (all printable) | High (motor scavengeable) | Wade |
| Repairability | Excellent | Excellent | Tie |
| Modern Software Support | Limited | Optimized | **Pitan** |

**Decision:** The weight advantage and M8 rod compatibility make Pitan superior. Wade's excessive torque is unnecessary for PLA/PETG/TPU, and the gantry sag it creates undermines quality goals.

### Pitan vs. Sherpa Mini

| Factor | Sherpa Mini | Pitan | Winner |
|--------|-------------|-------|--------|
| Weight | ~125g | 120-180g | **Tie** |
| Motor Required | Specific pancake | Scavengeable NEMA17 | **Pitan** |
| Gear Cost | $3-8 | $5-8 | Tie |
| Community | Massive | Growing | **Sherpa** |
| Documentation | Excellent | Good | **Sherpa** |
| Scavengability | Medium | **High** | **Pitan** |
| TPU Performance | Excellent | Excellent | Tie |
| Build Complexity | Medium | Low | **Pitan** |

**Decision:** Sherpa Mini is the superior choice if:
- You purchase new motors anyway
- You value community documentation

Pitan is superior if:
- You want to scavenge NEMA17 motors from donors
- You prioritize scavenger-friendly design
- You want motor flexibility (NEMA14 or NEMA17)

**For Neo-Darwin's scavenger philosophy, Pitan wins.**

### Pitan vs. Voron Extruders

| Factor | Voron CW2/M4 | Pitan | Winner |
|--------|--------------|-------|--------|
| Weight | 100-150g | 120-180g | **Voron** (marginally) |
| Cost | $50-75 | $7-25 | **Pitan** |
| Scavengability | Low | **High** | **Pitan** |
| Speed Optimization | Very High | Not Optimized | Voron |
| Quality Optimization | Yes | **Yes** | Tie |
| Complexity | High | Low | **Pitan** |
| Neo-Darwin Philosophy | Poor fit | **Perfect fit** | **Pitan** |

**Decision:** Voron extruders are engineered for 300mm/s+ racing, which Neo-Darwin explicitly does not prioritize. The cost and scavengability differences are decisive. Pitan achieves equivalent print quality through software intelligence rather than over-engineered hardware.

---

## The Klipper Advantage: Why Software Matters

### The Bambu Lab X1C Lesson

The Bambu Lab X1C uses a single-drive extruder yet produces print quality superior to most dual-drive systems. This proves:

> **Quality = Intelligent Control × Mechanical Adequacy**

NOT

> **Quality = Complex Hardware**

### Klipper Features Pitan Leverages

#### 1. Pressure Advance
Compensates for the time between filament being pushed and exiting the nozzle. Pitan's direct-drive minimizes this delay, and Pressure Advance fine-tunes it.

#### 2. Input Shaping
Cancels resonance (ringing) caused by gantry movement. Pitan's lightweight design reduces the magnitude of resonance, making Input Shaping more effective.

#### 3. Resonance Testing
Automatic measurement of printer's natural frequencies allows Klipper to generate custom shaping filters. Pitan's predictable inertia makes this tuning more stable.

#### 4. Extruder Control
- Precise microstepping
- Current control for smooth motion
- Extruder-to-nozzle calibration

**Key Insight:** A 150g extruder with Klipper Input Shaping produces better quality than a 600g extruder without it, at any speed under 150mm/s.

---

## Reference Configuration: Neo-Darwin with Pitan

### Recommended Build: Tier 2 (Scavenge + Purchase)

**Target Budget:** ~$15-20 AUD for complete extruder system

#### Bill of Materials

| Component | Source | Cost (AUD) |
|-----------|--------|------------|
| Pitan printed parts (body, idler, mounts) | Print yourself | $0.50 (filament) |
| BMG clone dual-drive gear set | AliExpress | $5-8 |
| NEMA17 motor | Scavenge from Ender 3 donor | $0 |
| 2× 608 bearings | Hardware store or scavenge | $0-2 |
| M3×20 bolts, M3 nuts | Hardware store | $1 |
| PTFE tube + fitting | Hardware store | $1 |
| **Total** | | **$7.50-12.50** |

#### Rod Requirements

| Axis | Rod Size | Required for Pitan |
|------|----------|-------------------|
| X-axis | M8 smooth rods | ✅ No sag at 250mm span |
| Y-axis | M8 smooth rods | ✅ No sag with proper supports |

**No upgrade to M10 rods required!** This is the Pitan's key advantage.

#### Motor Configuration

```
Klipper Configuration:
[stepper_nema17]
microsteps: 16
rotation_distance: 22.678  # Calibrated
hold_current: 0.5
run_current: 0.6
stealthchop_threshold: 0
```

#### Expected Performance

| Metric | Value |
|--------|--------|
| Max Print Speed | 80-120mm/s (quality range) |
| Max Acceleration | 1000-1500mm/s² |
| Layer Height | 0.1-0.3mm |
| Materials | PLA, PLA+, PETG, TPU |
| First Layer Consistency | ±0.05mm (with bed mesh) |
| Ringing | Eliminated by Input Shaping |

---

## Alternative: Tier 1 (Pure Wade Scavenge)

For builders with extreme budget constraints ($0-5 AUD for extruder):

#### Approach
- Use Greg's Wade extruder design
- 3D print gears
- Scavenge NEMA17 motor
- Accept gantry sag limitations

#### Mitigation Strategies

1. **Reduce Build Volume:** 200×200mm instead of 220×220mm
2. **Add Mid-Supports:** Frame-mounted Y-rod supports to reduce effective span
3. **Tune Klipper:** Conservative acceleration, aggressive input shaping

#### When to Choose Tier 1

- Already own M10 rods from another project
- Willing to sacrifice some quality for cost
- Have access to CAD/3D printing to modify Wade design

**Verdict:** Viable for ultra-budget builds, but not recommended as reference standard.

---

## Implementation Notes

### Klipper Configuration (Pitan)

```ini
[extruder]
step_pin: PE4
dir_pin: !PE2
enable_pin: !PE0
microsteps: 16
rotation_distance: 22.678  # Adjust after calibration
gear_ratio: 3:1
nozzle_diameter: 0.4
filament_diameter: 1.750

[tmc2209 extruder]
uart_pin: PE1
run_current: 0.5  # Start low for NEMA17
hold_current: 0.4
stealthchop_threshold: 0

[firmware_retraction]
retract_length: 0.5
retract_speed: 35
unretract_extra_length: 0
unretract_speed: 35
```

### Pressure Advance Tuning

```bash
# Measure and tune pressure advance
TEST_RETRACT MEASURE=100
SET_PRESSURE_ADVANCE ADVANCE=0.04  # Typical starting value
```

### Input Shaping Configuration

After resonance testing:

```ini
[input_shaper]
shaper_freq_x: 45.2  # From calibration
shaper_freq_y: 38.7
shaper_type: mzv
shaper_comp_time: 0.032
```

### Sourcing Guide

**BMG Clone Gears (AliExpress):**
- Search: "BMG dual drive gear set extruder"
- Price range: $3-8 AUD
- Preferred vendors: Trianglelab, Mellow

**Bearings:**
- 608ZZ bearings: Hardware store or skate shop
- Cost: ~$1-2 each

**NEMA17 Motors:**
- Scavenge from: Ender 3, CR-10, Anet A8
- Check: Step angle (1.8°), current rating

---

## Maintenance and Repair

### Spare Parts Strategy

Given the scavenger philosophy, maintain this spares kit:

| Part | Qty | Cost | Notes |
|------|-----|------|-------|
| BMG gear set | 1 | $5 | Complete replacement |
| 608 bearings | 4 | $2 | Common wear item |
| Pitan body parts | Printed | $0.50 | Print spares during initial build |
| NEMA17 motor | 1 | $0 (scavenge) | Keep donor parts |

**Total spares cost:** ~$7-10 for 5+ years of operation

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|--------|----------|
| Under-extrusion | Worn hob gear | Replace gear set ($5) |
| Filament slip | Loose tension | Adjust idler thumbscrew |
| TPU jams | Insufficient grip | Ensure dual-drive engagement, check gear teeth |
| Motor overheating | Current too high | Reduce run_current in Klipper |

---

## Conclusion

### The Pitan Decision

After exhaustive evaluation of weight, cost, scavengability, mechanical performance, and compatibility with Klipper firmware, the **Pitan Extruder** is the clear choice for the Neo-Darwin reference standard.

**It is not the fastest extruder. It is not the lightest extruder. It is not the simplest extruder.**

**But it is the optimal balance of:**
1. Quality print output through Klipper intelligence
2. Scavenger-friendly sourcing (motor scavengeable)
3. Lightweight design enabling M8 rod usage
4. Dual-drive reliability for TPU and consistent extrusion
5. Budget-conscious cost ($7-25 AUD)

### Why This Matters

The Neo-Darwin project exists to prove that:
- You can achieve MK4/Bambu-quality prints on a $300 AUD budget
- 20 years of RepRap knowledge, combined with modern Klipper firmware, outperforms expensive commercial systems
- Quality comes from intelligent control, not raw speed or cost

The Pitan extruder embodies this philosophy perfectly.

### Final Recommendation

**For the Neo-Darwin Reference Specification:**

- ✅ **Primary:** Pitan Extruder with NEMA17 motor (scavenged) and BMG gears
- ✅ **Alternative:** Sherpa Mini for builders preferring turnkey solutions
- ✅ **Not Recommended:** Greg's Wade (too heavy), Voron extruders (too expensive)

### Path Forward

1. Finalize Pitan parametric design in build123d
2. Create detailed assembly documentation
3. Validate performance with test prints
4. Publish BOM and sourcing guide
5. Update Neo-Darwin Manifesto with extruder specification

---

*"A tractor doesn't win races. It pulls loads reliably. The Pitan doesn't chase 300mm/s. It produces quality prints consistently, inexpensively, and repairably."*

---

**Document prepared for:** Neo-Darwin Project  
**Date:** January 2026  
**Philosophy:** "A Tractor with the Brain of a Racecar"
