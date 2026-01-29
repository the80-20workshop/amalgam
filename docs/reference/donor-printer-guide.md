# Donor 3D Printer Compatibility Guide

This guide helps Amalgam builders identify which donor printers provide the most value and what to expect from each. Not all printers are equal donors—some provide smooth rods, others don't.

**Target release:** End of 2026
**Expected donor pricing:** ~$50 AUD per unit (secondhand market floor)

⚠️ **Cost Reality Check:** Before you start shopping, read [When NOT to Scavenge](#when-not-to-scavenge-enclosed--proprietary-printers) later in this guide. Amalgam makes financial sense only when donors are $100-150 each. Beyond that, commercial alternatives are competitive.

💡 **Budget for Contingencies:** Expect to spend **$80-150 on parts you can't scavenge** (M10 rods, M8 leadscrews, bearings, PSU, misc). See [Parts Sourcing & Replacement Guide](parts-sourcing-guide.md) for how to source these if a donor part fails or is damaged. **Total realistic budget: $250-380 AUD.**

## Quick Reference: Donor Tiers

### Fitness Categories (See ADR-026)

This section now uses **fitness tiers** based on bed size and Z-height (see ADR-026: Donor Fitness & Frame Constraints):

- **Tier 1 (Recommended):** 200–235mm bed, <280mm Z → Full support, no modifications
- **Tier 2 (Supported with notes):** 235–300mm bed, 280–400mm Z → Works with heatbed swap or heavier MDF
- **Tier 3 (Unsupported):** >300mm bed, >400mm Z → Not recommended, re-sell and buy Tier 1 donors

## Frame Paths by Donor Type

**Amalgam has three frame paths** (see ADR-025):

| Path | Component Match | Common Donors | Recommendation |
|------|-----------------|---------------|----------------|
| **Darwin** | Two smooth-rod donors | Anet A8, Wanhao i3, Prusa clones | Primary—buy M10 rods (~$30-45) |
| **V-Core** | Two v-slot donors | Ender 3, CR-10, Aquila | Primary—zero-waste, recommended |
| **S-Core** | Mixed: extrusion + smooth-rod | Rare; mixed donor scenarios | Fallback only—usually avoid |

**S-Core is rare:** Most real-world printers are either all-smooth-rods (Darwin path) or all-v-slots (V-Core path). Extrusion + smooth-rod combinations are uncommon. If you have mixed donors, either:
1. Buy M10 rods and use Darwin path (cheaper, simpler)
2. Build S-Core if you have good extrusions available

---

### Tier 1: Rod-Bearing Donors (Recommended)

**Component compatibility:** Provide smooth rods AND bearings—the hardest parts to find cheap.
**Bed size:** 200–235mm. **Z-travel:** <280mm.

- **Anet A8 / A6** → Tier 1 ✅ (220×220, 240mm Z)
- **Prusa i3 clones** → Tier 1 ✅ (Geeetech, Tronxy X3, CTC; 200–220mm bed, ~260mm Z)
- **Anycubic i3 Mega** → Tier 1 ✅ (210×210, 200mm Z)
- **Prusa MK2 / MK2S** → Tier 1 ✅ (250×210, 210mm Z; premium quality)
- **Prusa MK3 / MK3S+** → Tier 1 ✅ (250×210, 210mm Z; premium quality, highest parts quality)

---

### Tier 1: V-Slot Donors (Recommended)

**Component compatibility:** V-slot motion system (no smooth rods), but excellent motors/electronics.
**Bed size:** 200–235mm. **Z-travel:** <280mm.

- **Creality Ender 3 / 3 Pro / 3 V2 / 3 S1** → Tier 1 ✅ (235×235, 250mm Z)
- **Voxelab Aquila** → Tier 1 ✅ (235×235, 250mm Z; Ender 3 clone)
- **Creality Ender 5 / 5 Pro** → **See Tier 3 note** ⓘ (Has own dedicated projects like Mercury One)
- **Elegoo Neptune series** → Tier 1 ✅ (235×235, 250mm Z; Ender 3 competitor)

---

### Tier 2: Larger Bed Donors (Supported with Mitigation)

**Bed size:** 235–300mm. **Z-travel:** 280–400mm. **Note:** Recommend heatbed swap (to 220×220) or heavier MDF base.

- **Creality CR-10 / CR-10S** → Tier 2 ⚠️ (300×300, 400mm Z)
- **Artillery Sidewinder X1 / Genius** → Tier 2 ⚠️ (300×300, 360mm Z)

*See ADR-026 for heatbed swap guide and MDF thickness recommendations.*

---

### Tier 3: Specialty/Limited Donors (Not Recommended)

Limited usefulness due to size, proprietary parts, or unsupported geometry:

- **Prusa Mini / Mini+** → Limited (180×180, too small; good for SuperPINDA probe scavenge)
- **Ender 2** → Limited (165×165, too small)
- **Ender 5 / Ender 5 Pro** → **Has own project** ⓘ (Mercury One and other Ender 5 conversions exist; those communities are more appropriate)
- **Tronxy models (especially X5S, large format)** → **Has own projects** ⓘ (Tronxy community has dedicated upgrade paths; Amalgam not optimized for Tronxy geometry)
- **Delta printers** → Unsupported (wrong geometry, can't use components)
- **Resin printers** → Unsupported (nothing reusable)
- **Tevo Spider (large models)** → Tier 3 ❌ (500×500, too large; unsupported)
- **Custom/modified printers** → Varies (too many unknowns)

---

## Detailed Donor Breakdown

### Anet A8 / A6

**Fitness Tier:** ✅ **Tier 1 (Recommended)**
**Bed:** 220×220mm | **Z-travel:** 240mm | **Frame path:** Darwin (primary)

**Why it's excellent:** Millions sold, often "broken" (usually just needs firmware update or new MOSFET). 220×220mm bed matches Amalgam reference spec exactly. Perfect fit for Darwin frame path. Steel frame is not useful for Amalgam, but motion components are excellent.

| Component | Spec | Amalgam Use | Notes |
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

### Prusa i3 Clones (Geeetech, Tronxy X3, Wanhao i3, Coolcoin Create, CTC, Alunar, etc.)

**Fitness Tier:** ✅ **Tier 1 (Recommended)**
**Bed:** 200–220mm | **Z-travel:** 260mm (typical) | **Frame path:** Darwin (primary)
**Frame type:** Steel rod frame (like Anet A8, not extrusion-based)

**Why it's good:** Direct descendants of original RepRap design. Rod-based steel frames are compatible with Darwin/M10 path philosophy. Build quality varies by brand. All Tier 1 compatible. Steel frame not useful for Amalgam, but smooth rods and motors are excellent.

| Component | Spec | Amalgam Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 6× 8mm | ✅ Direct use | Quality varies by brand |
| **Linear bearings** | 6× LM8UU | ✅ Direct use | Often cheap quality; use IGUS if worn |
| **NEMA17 motors** | 4-5× | ✅ Direct use | Standard steppers |
| **Heated bed** | 200–220mm | ✅ Works well | Slightly smaller than reference; acceptable |
| **Steel frame** | Rod-based structure | ⚠️ Not reused | Can't transfer to Amalgam box frame (use M10 rods instead) |
| **Power supply** | 12V | ⚠️ Upgrade | Consider 24V for dual MCU |
| **Mainboard** | Various (4 drivers) | ✅ Tier 2 MCU | Check MCU (ATMEGA, STM32) compatibility |
| **Lead screw** | 2× T8 | ✅ Z-axis | Inspect for wobble |

**Watch out for:**
- **Tronxy X3:** Good donor, classic i3 clone (220×220, 260mm Z) ✅ Tier 1
- **Wanhao i3:** Good donor, similar to Anet A8 (220×220, 240mm Z) ✅ Tier 1
- **Coolcoin Create:** Similar to Wanhao/Anet (210×210 typical, 260mm Z) ✅ Tier 1
- **Tronxy X5S / large format models:** **See Tier 3 note** ⓘ (Have their own project communities)
- **Geeetech i3:** Some use acrylic frame (useless), but rod-based ones are Tier 1
- **CTC/Alunar:** Cheapest clones, rod quality varies; inspect carefully before purchase

---

### Anycubic i3 Mega / Mega S

**Fitness Tier:** ✅ **Tier 1 (Recommended)**
**Bed:** 210×210mm | **Z-travel:** 200mm | **Frame path:** Darwin (primary)

**Why it's good:** Better build quality than Anet A8, still has smooth rods and a steel frame. Rod-based design like Anet A8. Excellent components for Darwin path. Steel frame not useful for Amalgam, but motion components are premium quality.

| Component | Spec | Amalgam Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 6× 8mm | ✅ Direct use | Good quality, hardened steel |
| **Linear bearings** | 6× LM8UU | ✅ Direct use | Branded bearings, excellent quality |
| **NEMA17 motors** | 5× | ✅ Direct use | Higher quality than Anet |
| **Heated bed** | 210×210mm (Ultrabase) | ✅ Works | Ultrabase PEI surface is excellent |
| **Power supply** | 12V 20A | ⚠️ Upgrade | Consider 24V for efficiency |
| **Mainboard** | Trigorilla (4 drivers) | ✅ Tier 2 MCU | ATMEGA2560 based, very capable |
| **Lead screw** | 2× T8 | ✅ Z-axis | Good quality |
| **Steel frame** | Structural steel | ⚠️ Not useful | Not aluminum extrusion; discard or repurpose |
| **Touchscreen** | Anycubic TFT | ❌ Not useful | Proprietary, leave behind |

**Frame note:** i3 Mega uses a **steel frame** (not aluminum extrusions), similar to Anet A8. The frame itself won't transfer to an Amalgam build, but all the motion and electronics components are excellent.

---

### Prusa MK2 / MK2S / MK3 / MK3S+

**Fitness Tier:** ⚠️ **Tier 1 Components, But Frame Not Easily Adaptable**
**Recommendation:** **Just add Klipper, don't dismantle.** Prusa machines have excellent structural design that's hard to repurpose; not ideal Amalgam donors despite component quality.

**Why not ideal as donors:** Prusa's CNC aluminum frame (especially MK3) is not a box-frame design. Disassembling and repurposing these machines would destroy their most valuable feature—a well-engineered, integrated structure. Better to upgrade with Klipper than to scavenge.

**Component Quality (If You Must Scavenge):**

| Component | Spec | Amalgam Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** (MK2/3) | 6× 8mm (hardened) | ✅ Excellent | Premium hardened steel |
| **Linear bearings** | 3× LM8UU + 3× LM8LUU | ✅ Direct use | Top-tier bearings, mix sizes |
| **NEMA17 motors** | 5× | ✅ Direct use | Genuine LDO or Moons motors |
| **Heated bed** (MK2/3) | 250×210mm (MK52) | ✅ Works | Magnetic PEI, but rectangular |
| **Power supply** (MK3) | 24V (15A+) | ✅ Direct use | Ideal voltage |
| **Mainboard** (MK3) | Einsy (5 drivers, TMC) | ✅ Excellent | Has TMC2130 steppers |
| **PINDA probe** (MK3S+) | SuperPINDA | ✅ Reference spec | Metal-detecting, ideal |
| **Frame** (MK2/3) | CNC aluminum | ❌ Not useful | Integrated design; can't adapt to Amalgam box frame |

**Better use:** Buy a broken MK3 (~$150), flash Klipper firmware, keep it as a working printer. You gain a known-good machine + reference quality components without the scavenge overhead.

**MK2 Note:** Uses threaded rod frame (not extrusions), but still integrated design—harder to repurpose than Anet A8.

---

### Creality Ender 3 / 3 Pro / 3 V2 / 3 S1

**Fitness Tier:** ✅ **Tier 1 (Recommended)**
**Bed:** 235×235mm | **Z-travel:** 250mm | **Frame path:** V-Core (recommended) or Darwin (requires buying rods)

**Why it's excellent:** Best-selling printer ever. Cheap and everywhere. **With ADR-025 Multi-Frame Architecture, Ender 3 is now fully supported via V-Core path—use the aluminum extrusions and V-slot rails directly.** No rod purchase needed if using V-Core.

| Component | Spec | Amalgam Use | Notes |
|-----------|------|----------------|-------|
| **V-slot extrusions** | 2020/2040 frame | ✅ V-Core path | Reuse as frame structure |
| **V-slot rollers** | 4× wheels per carriage | ✅ V-Core motion | Scavenged motion system, zero waste |
| **NEMA17 motors** | 4× (X, Y, Z, E) | ✅ Direct use | Need 2 donors for 7+ total |
| **Heated bed** | 235×235mm, 24V | ✅ Good size | Slightly larger than 220 reference; works |
| **Power supply** | 24V 30A typical | ✅ Direct use | Ideal for 24V system |
| **Mainboard** | Creality 4.2.x (4 drivers) | ✅ Tier 2 MCU | STM32/GD32 based, good quality |
| **Lead screw** | 1× T8 | ⚠️ Need 3 total | Only one per printer; buy one more |
| **Endstops** | 2-3× mechanical | ✅ Direct use | Standard microswitches |
| **Hotend** | MK8/Creality | ⚠️ Replace | Not E3D compatible; use E3D V6 |
| **Extruder** | Bowden or direct | ❌ Replace | Replace with Pitan (all paths) |
| **Belts** | GT2 6mm | ✅ Direct use | Check for wear |
| **Smooth rods** | ❌ None | ✅ Not needed for V-Core | Darwin path would need to buy |

**Two Ender 3 Donors (V-Core Path):**
- ✅ Frame: 2× full extrusion sets (use better condition one or combine)
- ✅ Motion: All V-slot wheels scavenged (zero additional cost)
- ✅ Motors: 8× NEMA17 (need 7, one spare)
- ✅ Beds: 2× 235×235 (use one)
- ✅ Electronics: 2× Creality mainboards (dual-MCU setup)
- ✅ PSU: 2× 24V (use better one)
- ⚠️ Lead screws: 2× T8 (need 3, buy 1 more ~$5–8)
- **Total new parts needed:** ~$8–12 (just one lead screw!)

---

### Creality CR-10 / CR-10S / CR-10 V2

**Fitness Tier:** ⚠️ **Tier 2 (Supported with Mitigation)**
**Bed:** 300×300mm | **Z-travel:** 400mm | **Frame path:** V-Core (recommended) | **Mitigation:** Heatbed swap to 220×220 (recommended) OR heavier MDF base

**Why consider it:** Larger format with dual Z motors. V-slot motion system. **Note:** See ADR-026 for fitness constraints. The large bed size and Z-height require either heatbed swap or heavier MDF damping for stability.

| Component | Spec | Amalgam Use | Notes |
|-----------|------|----------------|-------|
| **V-slot extrusions** | 2020/2040 frame | ✅ V-Core path | Good stiffness for larger format |
| **V-slot rollers** | 4-6× per carriage | ✅ V-Core motion | Scavenged system works |
| **NEMA17 motors** | 5× (dual Z motors!) | ✅ Direct use | Extra Z motor is bonus ✅ |
| **Heated bed** | 300×300mm | ⚠️ Swap recommended | Too large; recommend swap to 220×220 ($25–35) |
| **Power supply** | 24V 30A (typical) | ✅ Direct use | Good quality PSU |
| **Mainboard** | Creality 4.2.x (4 drivers) | ✅ Tier 2 MCU | STM32/GD32 based |
| **Lead screw** | 2× T8 | ✅ Z-axis | Already has dual Z, excellent |
| **Endstops** | 3× mechanical | ✅ Direct use | Standard microswitches |
| **Hotend** | MK8/Creality | ⚠️ Replace | Not E3D; replace with E3D V6 |
| **Extruder** | Bowden | ❌ Replace | Replace with Pitan |
| **Belts** | GT2 6mm (wider available) | ✅ Direct use | Check condition |

**Mitigation Options (Choose One):**

1. **Option A (Recommended):** Swap heatbed to 220×220
   - Cost: $25–35 (MK3 Dual Power or generic)
   - Result: Frame becomes 220×220mm, Z-height unchanged (~400mm)
   - Benefit: Perfect frame size, only moderate Z-height for Tier 2
   - Process: 4× M3 bolts, rewire heating element

2. **Option B:** Use heavier MDF base (50–60mm instead of 40mm)
   - Cost: ~$10 extra material
   - Result: Improved mass damping for larger bed
   - Drawback: Heavier final machine, may need stronger Z-motors

3. **Option C:** Not Recommended: Use as-is (300×300 on standard MDF)
   - Risk: Nozzle compliance issues, bed leveling instability
   - Outcome: Tier 3 unsupported deviation

**Why Tier 2:** CR-10's 400mm Z-height is at the boundary of stability. With heatbed swap, it becomes an excellent Tier 1 candidate.

---

### Voxelab Aquila

**Fitness Tier:** ✅ **Tier 1 (Recommended)**
**Bed:** 235×235mm | **Z-travel:** 250mm | **Frame path:** V-Core (primary) or Darwin (with rod purchase)

**Essentially an Ender 3 clone.** Nearly identical compatibility, same V-Core path benefits (no rod purchase needed). Scavenged motion system is zero-waste.

---

### Artillery Sidewinder X1 / Genius

**Fitness Tier:** ⚠️ **Tier 2 (Supported with Mitigation)**
**Bed:** 300×300mm | **Z-travel:** 360mm | **Frame path:** V-Core (recommended) | **Mitigation:** Heatbed swap to 220×220 (recommended)

**Why consider it:** Direct drive, excellent PSU, good dual Z motors. V-slot motion. Similar to CR-10 in size constraints—see ADR-026 for fitness details.

| Component | Spec | Amalgam Use | Notes |
|-----------|------|----------------|-------|
| **V-slot extrusions** | 2020/2040 frame | ✅ V-Core path | Good stiffness |
| **V-slot rollers** | 4-6× per carriage | ✅ V-Core motion | Scavenged system |
| **NEMA17 motors** | 5× | ✅ Direct use | Dual Z standard (bonus) |
| **Heated bed** | 300×300mm | ⚠️ Swap recommended | Too large; recommend swap to 220×220 ($25–35) |
| **Power supply** | 24V 30A | ✅ Direct use | Excellent quality PSU, premium feature |
| **Mainboard** | Mainboard K | ✅ Tier 2 MCU | STM32 based, capable |
| **Direct drive** | Titan clone | ⚠️ Parts for bin | Gears/springs useful; replace nozzle |

**Mitigation:** Same as CR-10—recommend heatbed swap to 220×220. With swap, becomes excellent Tier 1 candidate.

---

### Elegoo Neptune Series

**Fitness Tier:** ✅ **Tier 1 (Recommended)**
**Bed:** 235×235mm | **Z-travel:** 250mm | **Frame path:** V-Core (primary)

**Ender 3 competitor.** Similar to Ender 3 in what's reusable—V-slot motion system, zero rod purchase needed. V-Core path highly recommended.

---

### Prusa Mini / Mini+

**Fitness Tier:** ❌ **Tier 3 (Limited, Not Recommended as Primary Donor)**
**Bed:** 180×180mm | **Z-travel:** 180mm | **Issue:** Bed too small, rods too short for standard Amalgam specs.

**Limited donor value:** Below Tier 1 minimum (200×200mm bed). Consider Prusa Mini as **secondary** donor or parts scavenge only.

| Component | Spec | Amalgam Use | Notes |
|-----------|------|----------------|-------|
| **Smooth rods** | 4× 8mm (short) | ⚠️ Too short | Cantilever design, not 220mm+ length |
| **Heated bed** | 180×180mm | ❌ Too small | Below 200mm minimum for Tier 1 |
| **NEMA17 motors** | 3× (no Y) | ⚠️ Cantilever | Mini uses gantry-mounted Z |
| **Mainboard** | Buddy (5 drivers, TMC) | ✅ Good MCU | STM32, Klipper compatible; save for electronics |
| **SuperPINDA** | Yes | ✅ Excellent | Z-probe is reference-spec quality; valuable |

**Best use:** Scavenge the SuperPINDA (reference spec z-probe) and Buddy mainboard. Use 4× short rods for parts bin, not motion. Combine with a Tier 1 donor (e.g., Ender 3) for complete build.

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

All combinations below use **Tier 1 donors** (200–235mm beds, <280mm Z). For Tier 2 donors (CR-10, Artillery), see ADR-026 mitigation options.

⚠️ **Note:** These are best-case costs assuming all donor parts are usable. **Budget an additional $80-150 for parts you'll likely source** (M10 rods, M8 leadscrews, replacement bearings, PSU, etc.). See [Parts Sourcing & Replacement Guide](parts-sourcing-guide.md) if a donor part fails or is damaged. **Realistic total budget: $250-380 AUD.**

### Best Value: 2× Anet A8 (or Prusa i3 Clones) — Darwin Path
**Fitness:** ✅ Tier 1 + Tier 1 → **Fully Supported**
- **Total cost:** ~$100 AUD (two donors)
- **Frame path:** Darwin (M10 rods) + MDF base
- **Motion system:** Dual 8mm smooth rods (scavenged)
- **Heatbed size:** 220×220mm (reference spec)
- **Electronics:** Dual-MCU Klipper
- **New parts required:** M10 threaded rods (~$30–45), MDF (~$15–20)
- **Total Amalgam build:** ~$160–190 AUD
- **Why excellent:** Zero need to buy motion parts, perfect bed size, RepRap heritage

### Most Common: 2× Ender 3 — V-Core Path
**Fitness:** ✅ Tier 1 + Tier 1 → **Fully Supported (with ADR-025)**
- **Total cost:** ~$100 AUD (two donors)
- **Frame path:** V-Core (extrusions + V-slots)
- **Motion system:** V-slot wheels (scavenged, zero-waste)
- **Heatbed size:** 235×235mm (within Tier 1, works great)
- **Electronics:** Dual-MCU Klipper
- **New parts required:** 1× lead screw (~$8), MDF (~$15–20)
- **Total Amalgam build:** ~$160–180 AUD
- **Why excellent:** Zero rod/bearing purchase, perfect waste-free scavenging, 24V power supply included

### Mixed Donor: Ender 3 + Anet A8 — Flexible Hybrid
**Fitness:** ✅ Tier 1 + Tier 1 → **Fully Supported**
- **Total cost:** ~$100 AUD
- **Frame path:** Darwin (use Anet's rod-based wisdom)
- **Motion system:** 8mm smooth rods (from Anet, scavenged)
- **Heatbed:** Ender 3's 235×235 or Anet's 220×220 (both work)
- **Electronics:** Both mainboards contribute to Tier 2 dual-MCU
- **Advantage:** Ender 3's 24V PSU, Anet's proven rods
- **Total:** ~$160–190 AUD
- **Why good:** Best of both worlds; no compromise on any component

### Premium Path: Prusa MK3 + Ender 3 — Dual-MCU Overkill (Optional)
**Fitness:** ✅ Tier 1 + Tier 1 → **Fully Supported**
- **Total cost:** ~$200+ AUD (if you find an MK3 cheap)
- **Frame path:** Darwin or V-Core (your choice)
- **Heatbed:** Prusa's 250×210 (rectangular, excellent)
- **Electronics:** Einsy (5-driver TMC) + Creality board = overkill, but works
- **Bonus:** SuperPINDA reference-spec probe, LM8LUU premium bearings, 24V PSU
- **Why premium:** Highest quality scavenged parts, but hard to find MK3 cheap
- **Recommendation:** Only pursue if MK3 <$120. Otherwise, better to buy MK3 electronics new.

### Tier 2 Upgrade Path: CR-10 + Ender 3 (with Heatbed Swap) — V-Core with Mitigation
**Fitness:** ⚠️ Tier 2 + Tier 1 → **Supported with Heatbed Swap**
- **Total cost:** ~$120 AUD (two donors) + $25–35 (heatbed swap)
- **Frame path:** V-Core
- **Motion system:** V-slot wheels (scavenged from both)
- **Heatbed:** Swap CR-10's 300×300 to 220×220 (MK3 Dual Power ~$25–35)
- **Electronics:** Dual-MCU (two Creality boards)
- **New parts:** Lead screw (~$8) + heatbed (~$25) + MDF (~$15)
- **Total Amalgam build:** ~$180–210 AUD
- **Why consider it:** CR-10's dual Z motors and better PSU; workable with mitigation
- **Note:** Follow ADR-026 for heatbed swap process and MDF damping requirements

---

## Understanding Fitness Tiers (ADR-026)

This guide uses **fitness tiers** to help you assess donor suitability. See **ADR-026: Donor Fitness & Frame Constraints** for the full physics and rationale.

**Quick Summary:**

| Tier | Bed Size | Z-Height | Support Level | Mitigation |
|------|----------|----------|---------------|-----------|
| **Tier 1 ✅** | 200–235mm | <280mm | Full support | None needed |
| **Tier 2 ⚠️** | 235–300mm | 280–400mm | Supported | Heatbed swap or heavier MDF |
| **Tier 3 ❌** | >300mm | >400mm | Not recommended | Buy different donor pair |

**Examples:**
- Anet A8 (220×220, 240mm Z) → **Tier 1** ✅
- Ender 3 (235×235, 250mm Z) → **Tier 1** ✅
- CR-10 (300×300, 400mm Z) → **Tier 2** ⚠️ (swap bed or use heavier MDF)
- Tevo Spider (500×500, 500mm Z) → **Tier 3** ❌ (don't use)

**Why it matters:** Larger beds and taller gantries reduce system stiffness. MDF base provides damping, but there are physical limits. Tier 2 donors work great with simple mitigations (heatbed swap = $25–35). Tier 3 is beyond the scavenger philosophy—sell it and buy a matched Tier 1 pair.

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

## When NOT to Scavenge: Enclosed & Proprietary Printers

At a certain price point, **dismantling an old printer costs more than its parts are worth**. These machines are better off Klipperized whole or skipped entirely.

### Cost Threshold Reality

**Amalgam makes financial sense only if donors are reasonably priced.** Before you commit:

| Donor Cost | Recommendation |
|-----------|-----------------|
| **$100-150 each** | ✅ Good range—Amalgam build: $200-300 total |
| **$150-200 each** | ⚠️ Borderline—reconsider your strategy |
| **>$200 each** | ❌ Just buy **Bambu A1 Mini** (~$180) or **Ender 3 V3 SE** (~$150) new |

**Your goal:** Save money by scavenging. If you're paying premium prices, you've already lost.

### Enclosed Box-Frame Printers: Just Klipperize, Don't Dismantle

These machines are **better upgraded whole than dismantled**:

#### Anycubic 4Max Pro 2.0
- **Secondhand price:** ~$250 AUD
- **Why keep it whole?** Already enclosed, good frame, dual Z built-in, TMC drivers
- **What to do:** Flash Klipper firmware; use as-is
- **Benefit:** Working closed-loop system + Klipper's best features
- **Dismantle cost:** Labor > parts value at this price

#### XYZ da Vinci (All Models: Pro, Jr., Mini)
- **Mainboard:** Proprietary; reverse engineering required for Klipper
- **Hotend:** Proprietary cartridge system; incompatible with E3D V6
- **Bed system:** Single-point support (sag issues, like Ender 5)
- **Frame:** Integrated design (can't reuse cleanly)
- **Donor value:** Low; locked-down ecosystem
- **What to do:** Keep and upgrade with Klipper if you want it; don't dismantle for parts
- **Reality:** Parts salvage value << disassembly effort

#### FlashForge (Creator, Pro, Adventure)
- **Everything:** Proprietary firmware, mainboard, hotend connectors, bed system
- **Integration:** Tightly integrated; difficult disassembly
- **Donor value:** Very low
- **Compatibility:** None with standard Klipper builds
- **What to do:** Keep as-is or recycle; not a practical Amalgam source

### Scavenging Strategy: How to Avoid Wasting Money

**Before you buy an old printer to scavenge:**

1. **Identify two matched donors** (both smooth-rod OR both v-slot)
   - Example: Two Anet A8s, or Two Ender 3s
   - Avoid mixing (requires extra purchases)

2. **Calculate total cost:**
   - Donor 1: $_____
   - Donor 2: $_____
   - MDF base: $15-20
   - Frame material (M10 rods if Darwin, $0 if V-Core): $0-45
   - Misc (bolts, wires): ~$40
   - **Total: $____**

3. **Apply the rule:**
   - **If total < $280 AUD:** ✅ Good scavenger territory (matched donors)
   - **If total $280-300 AUD:** ⚠️ At parity with Bambu A1 Mini; reconsider
   - **If total > $300 AUD:** ❌ Just buy a new commercial printer instead

4. **If you find one printer, but no second match:**
   - Don't overpay for a second one just to avoid buying M10 rods
   - Buy M10 rods (~$35) and pick *any* other Darwin-compatible donor
   - Or buy a different matched pair

### The Enclosed Printer Problem in a Nutshell

**Enclosed machines gain little from Amalgam disassembly:**

| Issue | Impact |
|-------|--------|
| Proprietary mainboards | Don't work with standard Klipper setups; reverse engineering required |
| Integrated frame + electronics | Can't reuse either cleanly; disassembly is destructive |
| Non-standard hotends | Require custom mounts; incompatible with E3D V6 reference spec |
| Proprietary bed systems | Can't adapt to Amalgam's Triple-Z leveling |
| Difficult disassembly | More labor than the salvaged parts are worth |

---

**Bottom line:** Amalgam is for **matching donor pairs** scavenged in the **$100-150 each range**. Enclosed, proprietary machines at $200+ are better left alone, upgraded whole with Klipper, or skipped entirely. Don't pay premium prices for parts that will cost you premium labor to extract.

---

## What If a Donor Part Fails?

Sometimes you'll discover mid-build that a PSU is dead, a leadscrew is bent, or bearings are worn.

**See [Parts Sourcing & Replacement Guide](parts-sourcing-guide.md)** for:
- How to source replacements from AliExpress, Temu, eBay
- How to spot counterfeits and avoid duds
- Budget planning and decision tree
- Common pitfalls (wrong pitch leadscrew, fake bearings, etc.)

---

## References

- **ADR-026**: Donor Fitness & Frame Constraints (bed size, Z-height, stability physics)
- **ADR-025**: Multi-Frame Architecture (Darwin, S-Core, V-Core paths)
- **ADR-021**: Dual-Rod Motion System (rod requirements)
- **ADR-022**: Linear Bearing Selection (bearing options, IGUS path)
- **ADR-024**: Heated Bed Size Selection (bed compatibility)
- **ADR-012**: Mainboard Architecture (dual-MCU configuration)
- **docs/reference/ai-conversations/scavenger-guide.md**: Office equipment scavenging

---

*"The code handles the permutations; the iron handles the quality."*
