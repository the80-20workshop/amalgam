# Donor 3D Printer Compatibility Guide

This guide helps Neo-Darwin builders identify which donor printers provide the most value and what to expect from each. Not all printers are equal donors—some provide smooth rods, others don't.

**Target release:** End of 2026
**Expected donor pricing:** ~$50 AUD per unit (secondhand market floor)

## Quick Reference: Donor Tiers

### Tier A: Rod-Bearing Donors (Best for Dual-8 Builds)
These provide smooth rods AND bearings—the hardest parts to find cheap:
- Anet A8 / A6
- Prusa i3 clones (Geeetech, Tronxy X3, CTC, etc.)
- Anycubic i3 Mega
- Prusa MK2 / MK2S (premium)
- Prusa MK3 / MK3S+ (premium)

### Tier B: V-Slot Donors (Good for Motors/Electronics)
These use V-slot rollers—no smooth rods, but good for everything else:
- Creality Ender 3 / 3 Pro / 3 V2 / 3 S1
- Creality Ender 5 / 5 Pro
- Creality CR-10 / CR-10S
- Voxelab Aquila
- Elegoo Neptune series
- Artillery Sidewinder / Genius

### Tier C: Specialty/Limited Donors
Limited usefulness due to size or proprietary parts:
- Prusa Mini (small bed, cantilever)
- Ender 2 (very small)
- Delta printers (wrong geometry)
- Resin printers (nothing reusable)

---

## Detailed Donor Breakdown

### Anet A8 / A6

**Why it's excellent:** Millions sold, often "broken" (usually just needs firmware update or new MOSFET). 220×220mm bed matches Neo-Darwin reference spec exactly.

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 6× 8mm (various lengths) | ✅ Direct use | Check for wear/rust |
| **Linear bearings** | 6× LM8UU | ✅ Direct use | Clean and regrease |
| **NEMA17 motors** | 5× (X, Y, Z×2, E) | ✅ Direct use | Standard 1.8° steppers |
| **Heated bed** | 220×220mm, 12V | ✅ Reference spec size | May need rewire for 24V |
| **Power supply** | 12V 20A (240W) | ⚠️ Upgrade recommended | Underpowered for 24V system |
| **Mainboard** | Anet V1.x (4 drivers) | ✅ Tier 2 MCU | Flash Klipper firmware |
| **Lead screw** | 2× T8 threaded rod | ✅ Z-axis | Check for wobble |
| **Endstops** | 3× mechanical switches | ✅ Direct use | Standard microswitches |
| **Hotend** | Anet A8 (E3D V6 clone) | ⚠️ Replace nozzle | Cheap clone, works |
| **Extruder** | MK8 style | ❌ Replace with Pitan | Not geared |
| **Wiring** | Various | ✅ Reuse connectors | JST-XH, Dupont, etc. |
| **Belts** | GT2 6mm | ✅ Direct use | Check for wear |
| **Pulleys** | GT2 16T/20T | ✅ Direct use | |
| **Hardware** | M3, M4, M5 bolts/nuts | ✅ Parts bin | Metric standard |

**Yield from 2× Anet A8:**
- 12× smooth rods (need 8)
- 12× LM8UU bearings (need 16, buy 4 more or use LM8LUU)
- 10× NEMA17 motors (need 7)
- 2× heated beds (use better one)
- 2× mainboards (Tier 2 dual-MCU)
- 4× lead screws (need 3)
- 6× endstops (need 6)

---

### Prusa i3 Clones (Geeetech, Tronxy X3, CTC, Alunar, etc.)

**Why it's good:** Direct descendants of original RepRap design. Very similar to Anet A8 but build quality varies.

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 6× 8mm | ✅ Direct use | Quality varies by brand |
| **Linear bearings** | 6× LM8UU | ✅ Direct use | Often cheap quality |
| **NEMA17 motors** | 4-5× | ✅ Direct use | |
| **Heated bed** | 200×200mm | ✅ Minimum spec | Slightly smaller than reference |
| **Power supply** | 12V | ⚠️ Upgrade | |
| **Mainboard** | Various (4 drivers) | ✅ Tier 2 MCU | Check MCU compatibility |
| **Lead screw** | 2× T8 | ✅ Z-axis | |

**Watch out for:**
- Tronxy X3: Good donor, similar to Anet A8
- Geeetech i3: Some use acrylic frame (useless), but rods/motors good
- CTC/Alunar: Cheapest clones, rod quality varies

---

### Anycubic i3 Mega / Mega S

**Why it's good:** Better build quality than Anet, still has smooth rods.

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 6× 8mm | ✅ Direct use | Good quality |
| **Linear bearings** | 6× LM8UU | ✅ Direct use | Often branded |
| **NEMA17 motors** | 5× | ✅ Direct use | Higher quality |
| **Heated bed** | 210×210mm (Ultrabase) | ✅ Works | Ultrabase is nice |
| **Power supply** | 12V 20A | ⚠️ Upgrade | |
| **Mainboard** | Trigorilla (4 drivers) | ✅ Tier 2 MCU | ATMEGA2560 based |
| **Lead screw** | 2× T8 | ✅ Z-axis | |
| **Touchscreen** | Anycubic TFT | ❌ Not useful | Proprietary |

---

### Prusa MK2 / MK2S / MK3 / MK3S+

**Why it's premium:** Highest quality parts, but rarely found cheap secondhand.

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 6× 8mm (hardened) | ✅ Excellent | Premium quality |
| **Linear bearings** | 3× LM8UU + 3× LM8LUU | ✅ Direct use | Mix of short/long |
| **NEMA17 motors** | 5× | ✅ Direct use | Genuine LDO/Moons |
| **Heated bed** | 250×210mm (MK52) | ✅ Rectangular option | Magnetic, excellent |
| **Power supply** | 24V (MK3) | ✅ Direct use | Right voltage |
| **Mainboard** | Einsy (5 drivers, TMC) | ✅ Excellent | Has TMC2130 |
| **Lead screw** | 2× T8 integrated | ✅ Z-axis | Motor-integrated |
| **PINDA probe** | SuperPINDA (MK3S+) | ✅ Reference spec | Metal bed sensing |

**Reality check:** MK3 owners rarely sell cheap. Expect $150+ even broken. Better to buy parts directly.

---

### Creality Ender 3 / 3 Pro / 3 V2 / 3 S1

**Why it's common:** Best-selling printer ever. Cheap and everywhere. But NO SMOOTH RODS.

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | ❌ None | ❌ Must purchase | Uses V-slot rollers |
| **Linear bearings** | ❌ None | ❌ Must purchase | |
| **NEMA17 motors** | 4× (X, Y, Z, E) | ✅ Direct use | Need 2 donors for 7+ |
| **Heated bed** | 235×235mm, 24V | ✅ Good size | Slightly larger than ref |
| **Power supply** | 24V (various) | ✅ Direct use | Meanwell on Pro |
| **Mainboard** | Creality 4.2.x (4 drivers) | ✅ Tier 2 MCU | STM32/GD32 based |
| **Lead screw** | 1× T8 | ⚠️ Need 3 | Only one Z motor |
| **Endstops** | 2-3× mechanical | ✅ Direct use | |
| **Hotend** | MK8/Creality | ⚠️ Replace | Not E3D compatible |
| **Extruder** | Bowden or direct | ❌ Replace | Plastic, breaks |
| **Belts** | GT2 6mm | ✅ Direct use | |
| **V-slot extrusions** | 2020/2040 | ❌ Not useful | Wrong frame system |

**The Ender 3 Gap:**
You MUST purchase smooth rods and bearings:
- 8× stainless steel 8mm rods: ~$43 AUD (AliExpress)
- 16-22× IGUS RJ4JP-01-08: ~$30 AUD (AliExpress)
- **Total motion gap: ~$73 AUD**

**Yield from 2× Ender 3:**
- 0× smooth rods (must buy)
- 0× linear bearings (must buy IGUS)
- 8× NEMA17 motors (need 7) ✅
- 2× heated beds (use one)
- 2× mainboards (Tier 2 dual-MCU) ✅
- 2× lead screws (need 3, buy 1 more)
- 4-6× endstops
- 2× 24V PSU (use better one) ✅

---

### Creality CR-10 / CR-10S / CR-10 V2

**Why consider it:** Larger format, dual Z motors. Still V-slot though.

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | ❌ None | ❌ Must purchase | V-slot system |
| **NEMA17 motors** | 5× (dual Z) | ✅ Direct use | Extra Z motor! |
| **Heated bed** | 300×300mm | ⚠️ Too large | Overhangs reference |
| **Power supply** | 12V or 24V | Varies | Check model |
| **Lead screw** | 2× T8 | ✅ Z-axis | Has dual Z |

---

### Voxelab Aquila

**Essentially an Ender 3 clone.** Same compatibility, same gap (no rods).

---

### Artillery Sidewinder X1 / Genius

**Why consider it:** Direct drive, good PSU, but V-slot.

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | ❌ None | ❌ Must purchase | V-slot system |
| **NEMA17 motors** | 5× | ✅ Direct use | Dual Z standard |
| **Heated bed** | 300×300mm (Sidewinder) | ⚠️ Too large | |
| **Power supply** | 24V | ✅ Direct use | Good quality |
| **Direct drive** | Titan clone | ⚠️ Parts useful | Gears may work |

---

### Elegoo Neptune Series

**Ender 3 competitor.** Similar to Ender 3 in what's reusable (no rods).

---

### Prusa Mini / Mini+

**Limited donor value:**

| Component | Spec | Neo-Darwin Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 4× 8mm (short) | ⚠️ Too short | Cantilever design |
| **Heated bed** | 180×180mm | ⚠️ Very small | Below minimum |
| **Mainboard** | Buddy (5 drivers) | ✅ Could work | STM32, Klipper ok |
| **SuperPINDA** | Yes | ✅ Excellent | Reference spec probe |

**Best use:** Scavenge the SuperPINDA and maybe mainboard.

---

## What Else to Scavenge

Beyond the major components, don't overlook:

### Hardware (Nuts, Bolts, Washers)
- **M3 bolts** (various lengths): Frame, brackets, mounts
- **M3 nuts** (standard and nylock): Most printed parts
- **M3 washers**: Bed leveling, spacing
- **M4/M5 bolts**: Bed mounting, larger brackets
- **Heatset inserts**: If donor used them

### Wiring and Connectors
- **JST-XH connectors**: Motor, endstop, thermistor
- **Dupont connectors**: Headers, jumpers
- **Silicone wire**: 18-22 AWG for heated bed, hotend
- **Cable chains**: If donor had them
- **Zip ties**: Always useful

### Microswitches and Sensors
- **Mechanical endstops**: 3× minimum for XYZ homing
- **Optical endstops**: High precision alternative
- **Thermistors**: 100K NTC (bed, hotend)
- **Fans**: 4010, 4020, 5015 blowers

### Belts and Pulleys
- **GT2 belts**: 6mm width, check for wear/cracks
- **GT2 pulleys**: 16T or 20T, 5mm bore
- **Idler pulleys**: Smooth or toothed
- **Belt tensioners**: Springs, adjustment screws

### Misc Useful Parts
- **PTFE tube**: Bowden tube (4mm OD, 2mm ID)
- **Couplers**: Pneumatic fittings for PTFE
- **Springs**: Bed leveling springs
- **Thumbwheels**: Bed adjustment knobs
- **Heatsinks**: Motor, driver cooling

---

## Recommended Donor Combinations

### Best Value: 2× Anet A8 (or i3 clones)
- **Total cost:** ~$100 AUD
- **Motion gap:** $0 (all rods included)
- **Electronics gap:** $0 (Tier 2 dual-MCU)
- **Missing:** 4× LM8UU bearings (~$5), frame materials

### Most Common: 2× Ender 3
- **Total cost:** ~$100 AUD
- **Motion gap:** ~$73 (stainless + IGUS)
- **Electronics gap:** $0 (Tier 2 dual-MCU)
- **Missing:** 1× lead screw (~$8), frame materials

### Mixed Donor: Ender 3 + Anet A8
- **Total cost:** ~$100 AUD
- **Motion gap:** $0 (rods from Anet)
- **Electronics gap:** $0 (Tier 2 dual-MCU)
- **Best of both:** Anet rods + Ender's 24V system

### Premium Path: Prusa MK3 + Ender 3
- **Total cost:** ~$200+ AUD
- **Motion gap:** $0 (MK3 rods are excellent)
- **Electronics gap:** $0 (Einsy + Creality = overkill)
- **Bonus:** SuperPINDA, LM8LUU bearings, 24V PSU

---

## Where to Find Donors

### Best Sources (Australia)
1. **Facebook Marketplace** - Search "broken 3D printer", "Ender 3 parts", "Anet A8"
2. **Gumtree** - Similar to Marketplace
3. **University/TAFE surplus** - Often bulk lots
4. **Makerspace clearouts** - Ask your local space
5. **eBay** - For specific parts, rarely whole printers cheap

### Hunting Tips
- **Post "wanted" ads** - "Looking for broken 3D printers, any condition, $30-50"
- **Be patient** - $150 listings will eventually drop
- **Lot deals** - "Take all 3 for $100" is common
- **Condition doesn't matter** - "Won't heat" or "won't home" = easy fix
- **Inspect rods** - Roll on glass to check for bends

### What to Avoid
- **Resin printers** - Nothing reusable
- **Delta printers** - Wrong geometry, weird steppers
- **Heavily modified** - Missing stock parts
- **Fire damage** - Wiring compromised
- **"Upgraded" expensive** - Paying for someone else's mods

---

## Pre-Teardown Checklist

Before dismantling, verify:

1. **Power on test** (if safe)
   - Motors move? → Good steppers
   - Bed heats? → Good heater, thermistor
   - Home works? → Good endstops

2. **Rod quality check**
   - Roll on glass/mirror
   - Check for rust, scoring, wear marks
   - Measure diameter (should be 8.00 ±0.02mm)

3. **Motor test**
   - Spin by hand - should feel smooth with detents
   - Check for grinding or binding

4. **Bearing test** (if accessible)
   - Slide on rod - should be smooth
   - No grinding, clicking, or excessive play

5. **Document wiring**
   - Photo before disconnecting
   - Label connectors with tape

---

## References

- **ADR-021**: Dual-Rod Motion System (rod requirements)
- **ADR-022**: Linear Bearing Selection (bearing options, IGUS path)
- **ADR-024**: Heated Bed Size Selection (bed compatibility)
- **ADR-012**: Mainboard Architecture (dual-MCU configuration)
- **docs/reference/ai-conversations/scavenger-guide.md**: Office equipment scavenging

---

*"The code handles the permutations; the iron handles the quality."*
