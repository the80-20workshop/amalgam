# Neo-Darwin: X-Gantry Design Decision

## Engineering Decision Record

**Project:** Neo-Darwin 3D Printer  
**Component:** X-Axis Gantry System  
**Decision:** Parallel-Rail Sled ("The Plough")  
**Status:** Accepted  

---

## Executive Summary

After evaluating multiple X-gantry architectures including Cross-Rod (Eustathios/HercuLien), CoreXY variants, and the classic Cartesian sled, we selected the **Parallel-Rail Sled design** ("The Plough") for Neo-Darwin.

**Key Drivers:**
- Simplicity over speed
- Scavenger-friendly construction
- Maintainability by non-experts
- Authentic RepRap Darwin lineage
- Leverages M10 rod stiffness advantage

---

## Design Context

### Neo-Darwin Philosophy

Neo-Darwin is designed as:
- A "Tractor with a Racecar Brain" (heavy frame, smart software)
- A scavenger/junkstrap build using donor printers
- Quality-focused rather than speed-focused
- Maintainable by people with basic mechanical skills
- A spiritual successor to the original RepRap Darwin (2007)

### Hardware Constraints

| Component | Specification |
|-----------|---------------|
| Frame | M10 threaded rod on 36mm laminated MDF |
| X-Rails | M10 smooth rods (scavenged from photocopiers) |
| Span | ~380mm |
| Extruder | Pitan (Titan clone) direct drive |
| Hotend | E3D V6 |
| Controller | Klipper on dual MCU |
| Z-System | Triple-Z steppers with kinematic joints |
| Y-System | Dual Y-steppers with auto-squaring |

---

## Alternatives Considered

### Option A: Cross-Rod Gantry (Eustathios/HercuLien Style)

**Description:**  
Two rods for X and two for Y intersect at the toolhead. The toolhead "floats" at the crossing point, often called a "spider" carriage. This is sometimes called "Ultimaker-style."

```
    ════════════════════════  Y-Rod 1
           ╲         ╱
            ╲       ╱
             [HEAD]
            ╱       ╲
           ╱         ╲
    ════════════════════════  Y-Rod 2
    
    ║                      ║
    ║      X-Rods          ║
    ║   (perpendicular)    ║
```

**Pros:**
- Extremely light toolhead (only hotend moves in X-Y)
- Excellent for high-speed printing (500mm/s+)
- The "gold standard" for high-end rod-based DIY printers
- M10 rods would provide essentially zero sag at 380mm

**Cons:**
- Complex belt routing (crossed belts or dual belt systems)
- Requires precise geometry—belt path errors cause skew
- "Spider" carriage needs tight tolerances
- Harder to scavenge parts (specific pulley positions required)
- Klipper config more complex (`[hybrid_corexy]` or custom kinematics)
- More difficult to troubleshoot and repair
- Not in the Darwin/Mendel lineage

**Verdict:** Rejected—too complex for scavenger build philosophy.

---

### Option B: CoreXY / H-Bot

**Description:**  
Two motors work together via a continuous belt loop. Both motors spinning the same direction = Y movement. Opposite directions = X movement.

```
    [Motor A]═══════════════[Motor B]
              ╲           ╱
               ╲ Belts  ╱
                ╲     ╱
                 [HEAD]
                ╱     ╲
               ╱       ╲
              ╱         ╲
    ═══════════════════════════════
```

**Pros:**
- Both motors are stationary (not on gantry)
- Very light moving mass
- Excellent acceleration capability
- Popular design with extensive community support

**Cons:**
- Requires rigid frame (usually aluminum extrusion)
- Belt routing is complex and must be precise
- Misaligned belts cause "racking" (diagonal prints)
- Not compatible with threaded-rod frame philosophy
- Requires specific pulley stacks and belt lengths
- Harder to build from scavenged parts
- Completely different lineage from RepRap Darwin

**Verdict:** Rejected—incompatible with M10 threaded rod frame design.

---

### Option C: Parallel-Rail Sled ("The Plough") ✓ SELECTED

**Description:**  
Two horizontal M10 smooth rods spaced 50-80mm apart. A sled carriage rides on linear bearings between them. Single X-motor drives belt to move sled left-right. The entire X-assembly moves on Y-rails.

```
    [Y-Motor]═══════════════════[Y-Motor]
         ║     Y-smooth rods      ║
         ║                        ║
    [X-End]══════════════════[X-End]
         ║     X-smooth rods      ║
         ║       (60mm gap)       ║
         ║    ┌───────────┐       ║
         ║    │ THE PLOUGH│       ║
         ║    │ Pitan+V6  │       ║
         ║    └───────────┘       ║
```

**Pros:**
- Simple—one motor per axis, straightforward kinematics
- Extremely scavenger-friendly (any smooth rods, any bearings)
- Easy to understand, maintain, and repair
- Tolerant of frame imperfections (nuts adjust everything)
- Native Klipper support (simple `[stepper_x]` config)
- Direct lineage from Darwin → Mendel → Mendel i2
- M10 rods provide massive stiffness at 380mm span
- Pitan/V6 can be centered between rods (balanced)
- All components visible and accessible

**Cons:**
- Higher moving mass on Y-axis (entire X-assembly moves)
- Higher moving mass on X-axis (Plough + extruder + motor)
- Lower theoretical maximum speed than CoreXY
- X-motor rides on gantry (adds moving mass)

**Verdict:** Accepted—best fit for Neo-Darwin philosophy.

---

## Detailed Comparison Matrix

| Factor | Cross-Rod | CoreXY | The Plough |
|--------|-----------|--------|------------|
| **Simplicity** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Scavengeability** | ⭐⭐ | ⭐ | ⭐⭐⭐⭐⭐ |
| **Maintainability** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Frame Tolerance** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Klipper Config** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Max Speed** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Moving Mass (X)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Moving Mass (Y)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Rigidity** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Darwin Heritage** | ❌ | ❌ | ✅ |
| **Repairability** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## Why Moving Mass Penalty is Acceptable

### The M10 Advantage

At 380mm span with M10 smooth rods:
- Deflection under load is measured in microns
- Natural frequency is very high (won't resonate at print speeds)
- The "bounce" that plagues M8 systems doesn't exist

**The moving mass penalty of The Plough is almost irrelevant when rails don't flex.**

### Klipper Compensation

Klipper's Input Shaping can compensate for the higher moving mass:
- ADXL345 accelerometer measures actual resonance
- Software shapes motor commands to avoid exciting those frequencies
- Pressure Advance handles extruder response

**Result:** Quality prints at moderate speeds (150-250mm/s) with excellent surface finish.

### Quality Over Speed Philosophy

Neo-Darwin prioritizes:
1. Print quality (layer consistency, surface finish)
2. Reliability (prints complete successfully)
3. Repairability (fix it yourself)
4. Understanding (know how it works)

Speed is explicitly **not** a priority. A well-tuned Plough at 150mm/s produces better prints than a poorly-tuned CoreXY at 500mm/s.

---

## The Darwin Lineage

The Plough design maintains authentic RepRap heritage:

```
RepRap Darwin (2007)
    │
    ├── Box frame with threaded rods
    ├── Sled-style X-carriage
    └── Simple Cartesian kinematics
         │
         ▼
RepRap Mendel (2009)
    │
    ├── Triangular frame (still threaded rods)
    ├── Sled X-carriage between parallel rods
    └── Same kinematic philosophy
         │
         ▼
Mendel i2 (2012)
    │
    ├── Refined sled design
    ├── Better bearing arrangements
    └── Still threaded rod construction
         │
         ▼
Neo-Darwin (2025)
    │
    ├── M10 threaded rod frame (upgraded)
    ├── M10 smooth rod rails (upgraded)
    ├── "The Plough" sled (evolved)
    ├── Klipper brain (modernized)
    └── Same fundamental philosophy
```

**The Eustathios/HercuLien and CoreXY come from different branches:**

```
Ultimaker (2011)
    │
    └── Cross-rod / floating head
         │
         ▼
H-Bot → CoreXY (2012+)
    │
    └── Crossed belt systems
         │
         ▼
Eustathios / HercuLien (2014+)
    │
    └── Rod-based CoreXY variants
```

Neo-Darwin should remain true to its Darwin ancestry.

---

## The Plough: Design Specifications

### Rod Spacing

**60mm center-to-center (horizontal, top-down)**

Rationale:
- NEMA 17 motor is 42.3mm wide
- 4mm plastic walls on each side = 8mm
- ~10mm clearance for LM10UU housings
- Pitan/V6 nests perfectly between rods

### Bearing Arrangement

**LM10UU linear bearings with split-clamp housings**

- Minimum 2 bearings per rod (4 total)
- Spaced as far apart as carriage allows
- Split-clamp design (no zip ties)
- "Long wheelbase" prevents pitching during acceleration

### Extruder Positioning

**Pitan centered between rods, nozzle at geometric center**

- Weight balanced left-right
- No torque trying to twist carriage
- Belt attachment at carriage center (or balanced dual-attachment)

### Belt Path

**Single GT2 6mm belt, center-line routing**

- Belt runs parallel to X-rods
- Centered at 30mm mark (halfway between 60mm-spaced rods)
- Minimizes "cocking" force during acceleration

---

## Structural Optimization

### "Hollow Bone" Principle

The Plough should be designed with:
- 4-6 perimeter walls (not high infill)
- Structural ribs and webs
- Cut-away weight reduction where possible
- 3-5mm thick structural members

### Why Not Solid?

Solid plastic:
- Heavier (bad for moving mass)
- Cools unevenly (warps during printing)
- Wastes material

Ribbed structure:
- Lighter
- Cools evenly
- Looks "engineered"
- Actually stronger in bending

---

## Integration with Other Systems

### Dual Y-Steppers

The Plough design works perfectly with dual Y:
- Each Y-motor pulls one side of the X-assembly
- Klipper auto-squares on every home
- No mechanical coupling needed between Y-motors

### Triple Z with Kinematic Joints

Z-axis independence means:
- Plough doesn't need to compensate for bed tilt
- Klipper's `z_tilt_adjust` handles leveling
- X-gantry only needs to be parallel to itself

### Rubber Gasket Motor Isolation

X-motor on the Plough benefits from Strategy B sandwich mount:
- Reduces vibration transmitted to gantry
- Quieter operation
- Klipper Input Shaping handles residual resonance

---

## Rejected Optimizations

### Carbon Fiber X-Rods

**Considered:** Replacing M10 steel with CF tubes for weight reduction.

**Rejected:** 
- Not scavenger-friendly (must purchase)
- M10 steel is already stiff enough
- Adds complexity to bearing interface
- Against "hardware store" philosophy

### Pancake X-Motor

**Considered:** Using shorter NEMA 17 to reduce moving mass.

**Rejected:**
- Reduced torque
- May not be available from donor printer
- Standard NEMA 17 is fine for quality-focused printing

### Bowden Extruder

**Considered:** Moving extruder off gantry to reduce mass.

**Rejected:**
- Worse print quality (retraction tuning nightmare)
- Against quality-over-speed philosophy
- Direct drive is better for flexible filaments
- Pitan is the reference spec

---

## Future Upgrade Path

If users want more speed later, they can:

1. **Lighter Plough:** Redesign with more aggressive weight reduction
2. **Pancake Motor:** Swap X-motor for shorter variant
3. **Higher Acceleration:** Increase Klipper accel values
4. **Better Belts:** Upgrade to Gates GT3 belts

But the fundamental geometry—**sled on parallel rails**—scales well and doesn't need to change.

---

## Conclusion

The Parallel-Rail Sled ("The Plough") is the correct choice for Neo-Darwin because:

1. **It's simple** — One motor, one belt, two rods. Anyone can understand it.

2. **It's scavenger-friendly** — Photocopier rods, donor bearings, hardware store parts.

3. **It's maintainable** — All parts visible, accessible, replaceable with basic tools.

4. **It's authentic** — Direct descendant of RepRap Darwin and Mendel designs.

5. **It leverages M10** — The stiffness advantage negates the moving mass penalty.

6. **It prioritizes quality** — Reliable prints over maximum speed.

7. **It's a Tractor** — Heavy, reliable, fixable with a wrench.

**Neo-Darwin should feel like a machine tool, not a race car.**

---

## Decision Record

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025 | Selected Parallel-Rail Sled | Best fit for scavenger philosophy |
| 2025 | Rejected Cross-Rod | Too complex, wrong lineage |
| 2025 | Rejected CoreXY | Incompatible with threaded rod frame |
| 2025 | Set 60mm rod spacing | Optimal for Pitan nesting |
| 2025 | Specified split-clamp bearings | Better than zip-ties |
| 2025 | Confirmed center-line belt | Minimizes carriage twist |

---

## References

- RepRap Darwin (2007) — Original box-frame threaded rod printer
- RepRap Mendel (2009) — Triangular frame evolution
- Mendel i2 (2012) — Refined sled carriage
- Eustathios — Cross-rod gantry reference design
- HercuLien — Large-format cross-rod printer
- Ingentis — Modernized Cartesian sled design
- V-Core (early versions) — Rod-based Cartesian reference
