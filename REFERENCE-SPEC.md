# Amalgam Reference Specification

**The "Blessed" Hardware Configuration for 2026**

This document defines the specific hardware choices for the Amalgam. For the philosophy behind these choices, see [docs/philosophy.md](docs/philosophy.md). For build instructions, see [BUILDING.md](BUILDING.md).

---

## Quick Reference

| Component | Reference Spec | ADR |
|-----------|---------------|-----|
| **Frame Skeleton** | M10 Threaded Rods (Bright Zinc or Galvanized) | [ADR-001](docs/adr/001-m10-skeleton.md) |
| **Smooth Rods (X-Y)** | M10 Precision Ground | [ADR-003](docs/adr/003-smooth-rods.md) |
| **Smooth Rods (Z)** | M8 (sufficient with Triple-Z) | [ADR-003](docs/adr/003-smooth-rods.md) |
| **Extruder** | Pitan (3:1 geared, single-drive) | [ADR-019](docs/adr/019-pitan-extruder.md) |
| **Hotend** | E3D V6 + CHT Clone Nozzle | [ADR-004](docs/adr/004-v6-cht.md) |
| **Z-System** | Triple-Z Independent Motors | [ADR-005](docs/adr/005-triple-z.md) |
| **Z-Probe** | SuperPINDA (Reference) / BLTouch (Scavenger) | [ADR-014](docs/adr/014-z-probe-selection.md) |
| **Controller** | MKS SKIPR (Integrated Klipper) | [ADR-012](docs/adr/012-mainboard-host-architecture.md) |
| **Drivers** | TMC2209 | [ADR-013](docs/adr/013-drivers-endstops.md) |

---

## Project Goals

* **Price Target:** < $300 AUD (Beating the Bambu A1 Mini)
* **Build Volume:** ~250mm³ (Equalling or Exceeding the Prusa MK4)
* **Quality:** High-precision via Klipper Input Shaping and 3-Point Z-Tilt
* **Speed:** 70-120mm/s with tuned Input Shaping
* **Accuracy:** ±0.1mm dimensional consistency (Tier 3+ with M10 rods)
* **Reliability:** Prints identically on Day 1000 as on Day 1

---

## Before You Build: The 5 Key Decisions

Amalgam operates within a wide envelope. Before purchasing materials:

1. **Salvage or Buy Rods?** (M8 salvage vs M10 new)
2. **Belted-Z or Triple-Z?** (1 motor vs 3 motors)
3. **Single Board or Multi-MCU?** (MKS SKIPR vs salvaged boards)
4. **Extruder Choice?** (Pitan reference vs Wade heritage vs what you have)
5. **Mono or Multi-Color?** (Standard vs ERCF expansion)

These choices determine your tier, budget, and experience level.

---

## The Hardware Stack

### The Skeleton: M10 Threaded Rods

M10 was chosen over M12 for practicality:

| Feature | M8 | M10 | M12 |
|---------|-----|-----|-----|
| Rigidity vs M8 | 1× | 3× | 5× (overkill) |
| Wrench Size | 13mm | 17mm (universal) | 19mm (less common) |
| Printability | Easy | Easy | Bulky brackets |

* **Bright Zinc** for smoothness (`lumpy_factor = 0.2`)
* **Hot-Dip Galvanized** for rust-proofing (`lumpy_factor = 0.5+`)

### The Heart: Pitan Extruder

The Pitan (Printable Titan) is our reference extruder:

* **Single-Drive Design:** No gear mesh artifacts (same principle as Bambu Lab)
* **3:1 Gear Ratio:** Adequate torque for PLA, PETG, careful TPU
* **Scavengeable Motor:** Uses standard NEMA17 from any donor printer
* **Fully Printable:** Body and gears can be reprinted
* **Cost:** $4-10 AUD total

**Heritage Option:** Greg's Wade with pancake NEMA17 (PLA/PETG only)
**Ultra-Scavenger:** MK8 direct drive (if you have one)

See [ADR-019](docs/adr/019-pitan-extruder.md) for full rationale.

### The Lungs: E3D V6 + CHT Nozzle

* **E3D V6** (or high-quality clone) for thermal stability
* **CHT Clone Nozzle** increases flow by 50% without ooze
* Prioritizes detail and ERCF compatibility over raw speed

### The Brain: MKS SKIPR

The cleanest "all-in-one" path:

* **Integrated Klipper Host:** No external Raspberry Pi needed
* **eMMC Storage:** More reliable than MicroSD cards
* **7 Driver Slots:** Perfect "6+1" for Triple-Z + Extruder
* **Native CAN Bus:** Future-proof for toolhead boards

**Alternative Paths:**
* **Path A (Pure Scavenger):** Multi-MCU with salvaged boards + laptop
* **Path B (Modular):** FYSETC Spider + Raspberry Pi

### The Leveling: Triple-Z Independent

Three independent Z-motors for automated Klipper Z-Tilt calibration:

* **The "Neo" Path:** Automated calibration via `Z_TILT_ADJUST`
* **The "Tractor" Path:** Single motor + belt (manual leveling once)

### The Motion: Smooth Rods

| Axis | Reference Spec | Scavenger Option |
|------|---------------|------------------|
| **X-Y** | M10 Precision Ground | M8 from donor |
| **Z** | M8 (Triple-Z reduces deflection concerns) | M8 |

**Why Not Rollers?**
1. Can't mount to threaded-rod frame
2. Rollers wear out and flat-spot
3. 10mm smooth rods on M10 frame = "forever machine"

---

## Tiered BOM Strategy

All prices estimated in AUD (2026).

| Category | Tier 1 (Scrap) | Tier 2 (Hybrid) | Tier 3 (Reference) |
|----------|----------------|-----------------|-------------------|
| **Logic Path** | Single-Z Belt | Triple-Z | Triple-Z + SKIPR |
| **Mainboard** | Salvaged | Salvaged | MKS SKIPR |
| **Klipper Host** | Laptop ($0) | RPi Zero 2W (~$32) | Integrated |
| **Linear Motion** | Salvaged M8 | Salvaged M8 | Buy M10 (~$65) |
| **Motors** | 4 Salvaged | 4 Salvaged + 2 New | 4 Salvaged + 2 New |
| **Skeleton** | M10 Hardware (~$40) | M10 Hardware (~$40) | M10 Hardware (~$40) |
| **TOTAL** | **~$80** | **~$200** | **~$270** |

### Tier Recommendations

| Tier | Experience |
|------|------------|
| Tier 1 | Set-and-monitor (manual tuning) |
| Tier 2 | Set-and-tune (ADXL required) |
| Tier 3 | Set-and-forget (recommended) |

---

## Component Shopping List

### Hotend Stack
* **Primary:** TriangleLab or Mellow E3D V6 Clone (All-Metal)
* **Nozzles:** 0.4mm Brass, 0.6mm Brass, 0.4mm CHT Clone

### Gearing & Motion
* **Extruder:** Pitan printed parts + MK8 drive gear ($2-5)
* **Bearings:** 12× LM10UU (for M10) or LM8UU (for M8)
* **Smooth Rods:** 10mm Precision Ground (don't buy 8mm if buying new)

### Brain Essentials
* **Controller:** MKS SKIPR (~$85)
* **Drivers:** TMC2209 (often included or ~$6 each)
* **Resonance Sensor:** ADXL345 (~$18, required for Input Shaping)
* **Toolhead Sensor:** KW11-3Z Microswitch ($2, for ERCF)

### The "Tractor" Supplies
* **Thermal Bonding:** High-Temp Red RTV Silicone (for potting thermistor)

---

## Z-System Permutations

| Decision | Option A (Neo) | Option B (Tractor) |
|----------|---------------|-------------------|
| Z System | Triple-Z | Belted-Z |
| Motors | 3 | 1 |
| Board Requirement | 6+ drivers | 4 drivers |
| Experience | Auto-level | Manual once |
| Tier | 2+ | 1 |

---

## Multi-Color Expansion: ERCF v2

The Enraged Rabbit Carrot Feeder is the official multi-color expansion:

* **Total Sovereignty:** Fully 3D-printable, standard hardware
* **Modular Scale:** Start with 4 colors, expand to 12+
* **Scavenger Edge:** Uses NEMA17 motors and 608 bearings

| Component | Est. Cost (AUD) |
|-----------|----------------|
| ERCF v2 (8-Gate) | ~$120-150 |
| Filametrix Cutter | ~$5 |
| ERCT Buffer | ~$15 |

---

## Safety Requirements

* **Z-Max Physical Stop:** Mandatory microswitch at Z-max prevents bed-drop
* **Electrical:** Verify all salvaged wiring is intact
* **Thermal:** Allow hotend and bed to cool before touching
* **Ventilation:** Operate in well-ventilated area

---

## Self-Healing Machine Strategy

### The "Cold-Spare" Principle

The Amalgam is self-replicating. Maintain a "Vitamin Box" containing:

* Complete set of Pitan gears (printed)
* Spare MK8 drive gear or hobbed bolt
* Spare thermistor (NTC 100K)
* 5× 0.4mm nozzles
* 4010 ball-bearing fan

### Maintenance Checklist (Every 1000 Hours)

- [ ] Inspect gear teeth for wear
- [ ] Clear plastic dust from drive gear
- [ ] Verify frame nuts haven't vibrated loose
- [ ] Re-run `SHAPER_CALIBRATE` if machine was moved

---

## High-Level Assembly Overview

1. **Frame Construction:** Cut M10 rods, assemble with printed corners, verify square
2. **Gantry & X-Axis:** Mount X-axis to vertical pillars, install Pitan extruder
3. **Triple-Z Foundation:** Install Z-motors, leadscrews, and Spider bed support
4. **Wiring & Electronics:** Mount SKIPR, wire motors (Z1, Z2, Z3 on independent drivers)
5. **Klipper Setup:** Flash `printer.cfg`, verify with `STEPPER_BUZZ`

For detailed instructions, see [docs/guides/](docs/guides/).

---

## Related Documents

* [docs/philosophy.md](docs/philosophy.md) - The engineering philosophy
* [BUILDING.md](BUILDING.md) - CAD/STL generation
* [docs/adr/](docs/adr/) - Architecture Decision Records
* [docs/deep-dives/](docs/deep-dives/) - Design exploration documents
* [docs/guides/](docs/guides/) - Tier-specific build guides

---

*"The code handles the permutations; the iron handles the quality."*
