# The Tractor Philosophy

**20 Years of RepRap Wisdom, Distilled**

This document captures the engineering philosophy behind Neo-Darwin. For the specific hardware specification, see [REFERENCE-SPEC.md](REFERENCE-SPEC.md). For build instructions, see [BUILDING.md](BUILDING.md).

---

## The Mission: A Tractor with a Racecar's Brain

To prove that **Software Intelligence** can overcome **Analog Hardware**. We build a "Tractor with the Brain of a Racecar"—using heavy, high-torque, battle-tested hardware and giving it extreme precision through Klipper.

* **The Tractor (Hardware):** High-mass steel and geared extruders create a mechanical foundation that doesn't flex, skip, or drift.
* **The Racecar (Software):** Klipper's software intelligence—Input Shaping and 3-Point Kinematic Leveling—gives this iron skeleton the precision of a high-end industrial machine.

### Why "The Tractor"?

In 2026, you can buy a 3D-printing "appliance" that is fast but fragile, or you can build a **Mechanical Foundation**. We chose the latter.

* **Longevity over Velocity:** While others chase 600mm/s, we prioritize a consistent 70-120mm/s baseline to ensure the machine prints identically on Day 1000 as it did on Day 1.
* **Total Sovereignty:** You own every line of code and every bolt. Independent of proprietary ecosystems and cloud-lock.
* **Accuracy:** Dimensional consistency within ±0.1mm across the full build volume, enabled by a non-flexing frame and true kinematic leveling.

---

## The Neo-Darwin Square

In engineering, we often talk about the "Iron Triangle" (Pick two: Fast, Cheap, or Good). But for 3D printing, a triangle is too simple. The Neo-Darwin balances a **Square of Constraints**:

```
         COST
           |
    EFFORT-+-QUALITY
           |
         SPEED
```

### 1. Cost (The $300 AUD Ceiling)

Our primary constraint. To keep costs low, we sacrifice "Convenience." Instead of buying a $150 pre-assembled extruder, we print one from $10 of vitamins. We trade money for **Effort**.

### 2. Speed (The "Racecar" Mirage)

This is where most modern printers fail the triangle. Chasing 600mm/s requires expensive linear rails and lightweight carbon fiber—both of which blow the budget.

**The Wisdom:** We "settle" for 70–120mm/s. In 3D printing, 100mm/s with perfect quality is faster than 300mm/s with a 50% failure rate.

### 3. Quality (The Non-Negotiable)

Thanks to Klipper, quality is no longer tied to the price of the hardware.

* **Input Shaping** cancels out the vibrations of our heavy frame
* **Pressure Advance** manages the flow of our geared extruder
* **The Result:** High-end quality on a "junk" budget by using software intelligence to solve analog hardware problems

### 4. Reliability / Effort (The "Tractor" Soul)

A machine can be cheap and high-quality, but usually that means it's a "tinker-trap" (like a stock Ender 3).

**The Neo-Darwin approach:** We use Overbuilt Hardware (M10 rods, Geared Extruder, E3D V6). It takes more effort to *build*, but once running, it requires almost no *maintenance*.

---

## The "Battle-Tested" Wisdom

If you look at the last 20 years, the "Golden Ratio" of these trade-offs has shifted:

* **2007 (Darwin Era):** High Cost / Low Speed / Low Quality / Maximum Effort
* **2014 (i3 Era):** Medium Cost / Medium Speed / Medium Quality / Medium Effort
* **2026 (Neo-Darwin Era):** **Ultra-Low Cost / Medium Speed / High Quality / High Initial Effort**

---

## The Distilled "Pillars of Truth"

If you were to sum up the wisdom of those 20 years:

1. **Mass is a Filter:** A heavy machine is a quiet machine. Mass filters out the "noise" of cheap motors.

2. **Gearing is Sovereignty:** Direct drive is good, but Geared Direct Drive is king. It turns a cheap motor into a powerful one.

3. **Software is the Great Equalizer:** Don't spend $200 on rails if $0 of code (Klipper) can fix the vibration.

4. **The "Good Enough" Zenith:** Chasing the last 5% of speed costs 500% more money. The Neo-Darwin lives at the "Zenith"—where performance is high, but the cost is still accessible.

5. **The Bed is the Anchor:** The frame serves the bed, not the other way around. We prioritize a quiet, immovable foundation.

---

## The Lineage

* **[RepRap Darwin (2007)](https://reprap.org/wiki/Darwin):** The origin. The first practical self-replicating 3D printer. We carry its name forward.
* **[Prusa i3 Rework (2013)](https://www.thingiverse.com/thing:119616):** The source of our geared extruder heritage.
* **[RepRap Mendel Revisited (2024)](https://www.thingiverse.com/thing:6783269):** A modern nod to heavy threaded-rod skeletons.
* **[The 100](https://github.com/MSzturc/the100)/[The Rook](https://github.com/Kanrog/Rook):** Box-frame cousins who proved Klipper makes DIY frames truly accurate.

---

## Why Build a Neo-Darwin?

### What it IS for

* **The Scavengers:** Turn $80 AUD and a pile of salvage into a machine that rivals a $1,100 printer
* **The Engineers:** Those who love understanding every bolt and line of code
* **The Sovereign:** Those who reject cloud-lock and proprietary ecosystems
* **The Repairers:** Those who want a machine that can print its own replacement parts

### What it is NOT for

* **If you want 'set-and-forget':** Buy a Bambu Lab A1. It works out of the box.
* **If you're buying all new parts:** You're approaching commercial printer prices. At that point, the only reason to build is because you love the engineering challenge.

### The Reality Check

| Feature | Neo-Darwin | Bambu A1 Mini | Prusa MK4 |
|---------|------------|---------------|-----------|
| **Price (AUD)** | ~$250 | ~$489 | ~$1,100 |
| **Z-Logic** | Triple-Z Tilt | Single Motor | Dual (Synced) |
| **Repair** | Hardware Store | Proprietary | Open (Premium) |
| **Control** | 100% Local | Cloud-Lock | Local/Cloud |

---

## The RepRap Tradition

Historically, a RepRap builder's "Rite of Passage" was to use their first machine to print parts for **two more machines** for others *at cost*.

In a world of proprietary "Cloud" appliances, we choose the Red Pill. We choose the code, the torque, and the iron.

> **"If you want a printer, buy one. If you want the Red Pill, build this."**

---

## Standing on the Shoulders of Giants

The Neo-Darwin is not an island; it is a 2026 entry into a long-running conversation about mechanical sovereignty.

### Heritage Builds
* **[RepRap Mendel Revisited](https://www.thingiverse.com/thing:6783269):** Validates our skeleton choice with M12 threaded rods
* **[Voron Legacy](https://vorondesign.com/voron_legacy):** Celebrates old-school aesthetics with modern firmware
* **[RepRap Micron](https://reprap.org/wiki/RepRapMicron):** Returns to threaded-rod roots for micro-precision

### Performance Scavengers
* **[The 100](https://github.com/MSzturc/the100):** Proves software intelligence makes cheap parts perform like elite hardware
* **[The Rook](https://github.com/Kanrog/Rook):** Prioritizes ease of service and reliability

### North Stars
* **[Voron Trident](https://vorondesign.com/voron_trident):** Gold standard for 3-point kinematic leveling
* **[Rat Rig V-Core 4](https://v-core4.ratrig.com/):** Pinnacle of open-source hybrid motion

> **"You aren't just building a printer; you're joining a 20-year conversation about sovereignty."**

---

## License: GNU GPL v3

We use the **GNU General Public License v3**, the same license used by the original RepRap Darwin.

* **RepRap Heritage:** Honoring our roots
* **"Copyleft" Protection:** Modifications must be shared under the same license
* **Community Evolution:** Prevents "black-box" commercialization

---

*For the specific hardware specification, see [REFERENCE-SPEC.md](REFERENCE-SPEC.md).*
