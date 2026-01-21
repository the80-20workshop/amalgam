# Neo-Darwin Extruder Options

A comprehensive analysis of lightweight, low-cost extruder options for the Neo-Darwin 3D printer project, following the "Tractor with the Brain of a Racecar" philosophy.

## Executive Summary

For a RepRap project prioritising accessibility, scavengeability, and low cost, we evaluated three primary extruder paths. **The Sherpa Mini is recommended** due to the ubiquity of BMG clone gears, extensive community support, and excellent documentation.

| Option | Gear Cost | Motor | Total Cost | Recommendation |
|--------|-----------|-------|------------|----------------|
| **Sherpa Mini** | ~$5 (BMG) | Round NEMA 14 pancake | **~$17-20** | ✅ Primary |
| ProtoXtruder | ~$12 (HGX-lite) | Round NEMA 14 pancake | ~$24-27 | Alternative |
| BMG Clone (complete) | N/A | NEMA 17 (heavy) | ~$15-20 | ❌ Not recommended |

**Key Insight:** Both Sherpa Mini and ProtoXtruder require the same round NEMA 14 pancake motor with integrated pinion. The deciding factor is **gear availability** - BMG clone gears are ubiquitous, cheap, and easy to source as spares. HGX-lite kits are good but less common.

---

## Context: Neo-Darwin Tier 2 Upgrade Path

In the Neo-Darwin build philosophy, builders scavenge motors from donor printers:

**Tier 1:** Scavenge X, Y, Z, E motors from donor printer (e.g., Ender 3)

**Tier 2:** Upgrade to triple Z motors and lightweight direct drive extruder

| Motor | Source | Cost |
|-------|--------|------|
| X axis | Scavenged | $0 |
| Y axis | Scavenged | $0 |
| Z1 | Scavenged (original Z) | $0 |
| Z2 | Scavenged (repurposed E) | $0 |
| Z3 | **Purchase NEMA 17** | ~$10 |
| Extruder | **Purchase round NEMA 14 pancake** | ~$12-15 |

**Total new motor cost:** ~$22-25 AUD

Both recommended extruders require the same pancake motor, so the extruder choice comes down to gear ecosystem and community support.

---

## Option 1: Sherpa Mini (Recommended)

### Overview

The Sherpa Mini is a ground-up design developed by Anlin and the team at Annex Engineering. It's a dual geared hobbed filament extruder featuring a 5:1 gear ratio for high torque while remaining near silent. It has become the de facto standard for lightweight direct drive extruders.

### Why Sherpa Mini?

**1. BMG Gear Ubiquity**

BMG clone gears are everywhere:
- Included in countless Ender 3 upgrade kits
- Available from dozens of AliExpress vendors
- Stocked by Trianglelab, Mellow, and many others
- Cost as little as $3-5 AUD on sale
- Easy to keep spares on hand

If gears wear out or get damaged, replacement is trivial and cheap.

**2. Massive Community Support**

The Sherpa Mini has years of refinement and community knowledge:
- Full PDF assembly manual with step-by-step instructions
- Hundreds of mount designs for different toolheads
- Extensive troubleshooting resources
- Active Discord community
- Well-documented failure modes and fixes

**3. Proven Design**

Thousands of Sherpa Minis are in service worldwide. The design is battle-tested and reliable.

### Specifications

| Attribute | Value |
|-----------|-------|
| Weight (complete) | ~110-127g |
| Gear Ratio | 5:1 (50:10) or 6.25:1 (50:8) |
| Drive Gears | BMG clone (dual drive) |
| Motor | Round NEMA 14 pancake with 8T or 10T pinion |
| Mounting Pattern | Sherpa Mini standard (widely adopted) |
| Push Force | ~120-180N |

### Bill of Materials

| Part | Approx. Cost (AUD) | Notes |
|------|-------------------|-------|
| BMG clone gear set | $3-8 | Drive gear, idler gear, thumbscrew, shaft |
| Round NEMA 14 pancake motor (w/pinion) | $10-15 | 8T or 10T integrated pinion required |
| 2× MR85ZZ bearings | Included in gear kit | |
| 3×20mm shaft | Included in gear kit | |
| 4-5× M3 heat-set inserts | ~$1 | Standard 4.8mm OD |
| M3 screws (various) | ~$1 | M3×8, M3×16, M3×20 BHCS |
| PTFE tube + fitting | ~$1 | |
| **Total** | **~$17-25** | |

### Printed Parts

- Housing front (skeleton design)
- Housing rear
- Idler arm
- Optional guidler/filament guide

Print time: ~2-3 hours in ABS/ASA at Voron spec settings.

### Build Process

1. Install heat-set inserts into housing (soldering iron required)
2. Press MR85ZZ bearings into housing
3. Assemble idler arm with thumbscrew mechanism
4. Install BMG shaft and gears
5. Mount motor and adjust gear mesh
6. Install PTFE fitting
7. Tension adjustment

Full assembly manual available at: `github.com/Annex-Engineering/Sherpa_Mini-Extruder/tree/master/Build_Instructions`

### Pros

1. **Cheapest gear option** - BMG clones cost $3-8
2. **Ubiquitous parts** - Spares available everywhere
3. **Massive community** - Years of support and documentation
4. **Full assembly manual** - Professional PDF instructions
5. **Lightest weight** - ~110-127g complete
6. **Standard mounting pattern** - Compatible with most toolheads
7. **Battle-tested** - Thousands in service

### Cons

1. **Heat-set inserts** - Requires soldering iron for installation
2. **More printed parts** - Skeleton housing has multiple components
3. **Gear mesh adjustment** - Can be fiddly to optimise
4. **BMG clone quality varies** - Check reviews when sourcing

---

## Option 2: ProtoXtruder (Alternative)

### Overview

The ProtoXtruder, designed by nhchiu, utilises HGX-lite gear kits with larger 18mm diameter drive gears. It offers a simpler build process but uses less common parts.

### Specifications

| Attribute | Value |
|-----------|-------|
| Weight (complete) | ~125g |
| Gear Ratio | 5:1 |
| Drive Gears | HGX-lite (18mm diameter) |
| Motor | Round NEMA 14 pancake with 10T pinion |
| Mounting Pattern | Sherpa Mini compatible |
| Push Force | ~120-180N |

### Bill of Materials

| Part | Approx. Cost (AUD) | Notes |
|------|-------------------|-------|
| HGX-lite gear kit | $8-16 | Complete: gears, bearings, shafts, hardware |
| Round NEMA 14 pancake motor (w/pinion) | $10-15 | Same as Sherpa Mini |
| 2× M3 heat-set inserts | ~$0.50 | |
| M3 screws | ~$1 | |
| ECAS04 PTFE fitting | Included in kit | |
| **Total** | **~$20-32** | |

### Pros

1. **Simpler build** - Fewer parts, ~1 hour print time
2. **Larger drive gears** - 18mm diameter for better grip
3. **All-in-one kit** - HGX-lite includes everything
4. **Sherpa Mini mount compatible** - Works with existing ecosystem

### Cons

1. **Higher gear cost** - HGX-lite kits cost $8-16 vs $3-8 for BMG
2. **Less common parts** - Harder to source spares
3. **Less community support** - Newer design, fewer resources
4. **Limited documentation** - GitHub README only

### When to Choose ProtoXtruder

- You already have HGX-lite gears
- You want the simplest possible build
- You prefer larger drive gears
- You don't mind sourcing less common parts

Documentation at: `github.com/nhchiu/VoronMods/tree/main/Extruders/ProtoXtruder`

---

## Option 3: Complete BMG Clone Extruder (Not Recommended)

### Overview

Pre-assembled BMG clone extruders require no printing but use full-size NEMA 17 motors.

### Why Not Recommended

| Issue | Impact |
|-------|--------|
| Weight | 250-350g vs ~120g for Sherpa Mini |
| Gantry sag | Causes mechanical issues on bed-slingers |
| Not RepRap | No printed parts, no customisation |
| Motor waste | Uses NEMA 17 better suited for Z axis |

The complete BMG extruder is suitable only for bowden setups or as a parts donor for Sherpa Mini builds.

---

## Motor Requirements

### Both Extruders Need the Same Motor

Both Sherpa Mini and ProtoXtruder require a **round NEMA 14 pancake motor** with integrated pinion gear:

| Specification | Value |
|---------------|-------|
| Form factor | Round, 36mm diameter |
| Body length | 17-20mm typical |
| Pinion teeth | 8T or 10T (affects gear ratio) |
| Step angle | 1.8° |
| Current | ~1A |
| Connector | JST-XH 4-pin typical |

### Sourcing

| Source | Price (AUD) | Notes |
|--------|-------------|-------|
| AliExpress clones | $10-15 | Check for 8T or 10T pinion |
| LDO Motors | $18-25 | Premium quality |
| Moons' | $15-22 | High temperature rated |

**Important:** The motor must have an integrated pinion gear. Standard round NEMA 14 motors without pinion will not work.

---

## Weight Comparison

| Extruder | Total Weight | Notes |
|----------|--------------|-------|
| **Sherpa Mini** (printed) | **~110-127g** | Lightest option |
| ProtoXtruder | ~125g | Slightly heavier |
| Sherpa Mini (CNC aluminium) | ~115-138g | Premium option |
| BMG Clone + NEMA 17 | ~250-350g | Too heavy |

---

## Cost Comparison

### Scenario: Tier 2 Neo-Darwin Build

| Component | Sherpa Mini | ProtoXtruder |
|-----------|-------------|--------------|
| Gear kit | $5 | $12 |
| Motor | $12 | $12 |
| Hardware | $3 | $2 |
| **Total** | **~$20** | **~$26** |

**Sherpa Mini saves ~$6** while providing better parts availability.

---

## Spare Parts Strategy

One of the key advantages of Sherpa Mini is spare parts planning:

### Recommended Spares Kit (~$10-15)

| Part | Qty | Cost | Notes |
|------|-----|------|-------|
| BMG clone gear set | 1 | $5 | Complete replacement |
| MR85ZZ bearings | 4 | $2 | Wear items |
| 3×20mm shaft | 2 | $1 | In case of damage |
| M3 heat-set inserts | 10 | $1 | For reprints |
| Thumbscrew spring | 2 | $1 | Tension mechanism |

With BMG gears being so common, builders can easily maintain a small spares kit.

---

## Recommendation Summary

### Primary: Sherpa Mini ✅

The Sherpa Mini is recommended as the **official Neo-Darwin extruder** for these reasons:

1. **BMG gear ubiquity** - Cheapest and most available gears
2. **Community support** - Massive ecosystem of help and resources
3. **Full documentation** - Professional assembly manual
4. **Lightest weight** - ~110-127g complete
5. **Easy spares** - Can maintain cheap spare parts kit
6. **RepRap philosophy** - Common, available, repairable parts

### Alternative: ProtoXtruder

Document as alternative for builders who:
- Already own HGX-lite gears
- Want simplest possible assembly
- Don't mind less common spare parts

### Not Recommended: Complete BMG Clone

Too heavy for direct drive applications.

---

## Implementation Notes

### Klipper Configuration (Sherpa Mini)

```ini
[extruder]
step_pin: E_STEP
dir_pin: E_DIR  # May need inversion depending on wiring
enable_pin: !E_EN
microsteps: 16
rotation_distance: 22.6789  # Calibrate for your setup
gear_ratio: 50:10  # Sherpa Mini with 10T motor
# gear_ratio: 50:8  # Sherpa Mini with 8T motor
nozzle_diameter: 0.4
filament_diameter: 1.750
# ... hotend config ...

[tmc2209 extruder]
uart_pin: E_UART
run_current: 0.5  # Start low, adjust as needed
stealthchop_threshold: 0
```

### Sourcing Guide

**BMG Clone Gears:**
- AliExpress (generic): $3-5 - check reviews
- Trianglelab: $8-12 - consistent quality
- Mellow: $6-10 - good mid-range

**Round NEMA 14 Pancake Motor:**
- AliExpress clones: $10-15
- LDO Motors: $18-25 (premium)
- Search: "NEMA 14 36mm pancake 8T" or "10T"

---

## References

- Sherpa Mini GitHub: `github.com/Annex-Engineering/Sherpa_Mini-Extruder`
- Sherpa Mini BOM: `docs.google.com/spreadsheets/d/1O3eyVuQ6M4F03MJSDs4Z71_XyNjXL5HFTZr1jsaAtRc`
- Annex Engineering Discord: `discord.gg/MzTR3zE`
- ProtoXtruder (alternative): `github.com/nhchiu/VoronMods/tree/main/Extruders/ProtoXtruder`

---

*Document prepared for the Neo-Darwin Project*  
*"A Tractor with the Brain of a Racecar"*
