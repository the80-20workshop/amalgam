# Rod Sag Analysis & Extruder Mass Considerations

**Reference Extruder: Pitan + NEMA17**

## 1. Purpose & Scope

This report consolidates the ongoing design discussion around **rod sag**, **moving mass**, and **extruder selection** in the Neo-Darwin printer concept. The goal is to:

* Quantify and contextualise **rod deflection (sag)** under realistic toolhead loads
* Use **Pitan + NEMA17** as a **baseline extruder mass and torque reference**
* Evaluate trade-offs between rigidity, speed, print quality, and scavenged-part flexibility
* Inform design decisions around rod diameter, span, motion system, and extrusion strategy

This is not a full finite element analysis, but a **first-order engineering justification** suitable for early-stage architecture decisions.

---

## 2. Reference Configuration

### 2.1 Motion Architecture (Assumed)

* Cartesian or Darwin-style XY with:

  * **Two parallel smooth rods per axis**
  * Toolhead mass shared unevenly depending on carriage geometry
* Rods supported at both ends (simply supported beam assumption)
* Z excluded from sag analysis (static load, not dynamic print quality limiter)

### 2.2 Reference Extruder

**Pitan + NEMA17** is used as the reference because:

* It represents a **realistic, non-optimistic mass**
* Commonly available and well understood
* Torque is sufficient for:

  * Standard E3D V6
  * 0.4–0.6 mm nozzles
  * Moderate volumetric flow (with or without CHT)

> This avoids designing around ultralight, exotic toolheads that undermine the “scavengable and adaptable” design goal.

---

## 3. Mass Budget (Order-of-Magnitude)

| Component                   | Approx. Mass (g) |
| --------------------------- | ---------------- |
| NEMA17 (short body)         | 280–320          |
| Pitan extruder body + gears | 120–160          |
| Hotend (E3D V6 class)       | 50–70            |
| Fans, shroud, wiring        | 40–60            |
| **Total Toolhead Mass**     | **500–600 g**    |

This mass is **intentionally conservative**. Designing for this load ensures:

* Bowden → Direct swaps remain viable
* Future upgrades don’t invalidate rod sizing
* Input shaping remains effective rather than compensatory

---

## 4. Rod Sag Fundamentals

### 4.1 Simplified Beam Model

Each smooth rod is approximated as:

* **Simply supported beam**
* Point load applied at carriage location
* Load shared across two rods (≈50% per rod, imperfect in practice)

Deflection scales with:

* **Rod length³**
* **Applied load**
* **Inverse of diameter⁴**
* Material modulus (steel assumed constant)

> The diameter term dominates — small increases in rod diameter dramatically reduce sag.

---

## 5. Comparative Rod Sag Trends

### 5.1 Diameter Sensitivity

Relative stiffness comparison (steel rods):

| Rod Diameter | Relative Sag   |
| ------------ | -------------- |
| 8 mm         | 1.0 (baseline) |
| 10 mm        | ~0.4×          |
| 12 mm        | ~0.2×          |

Moving from **8 mm → 10 mm** offers more benefit than halving toolhead mass.

---

### 5.2 Span Length Sensitivity

Sag increases with **length³**, meaning:

* A 400 mm rod has **~2× the sag** of a 320 mm rod
* “Just 40 mm wider” frames are not mechanically neutral

This reinforces the design principle:

> **Compactness is a structural advantage**, not merely an aesthetic one.

---

## 6. Dynamic Effects (Why Sag Still Matters with Klipper)

While Klipper provides:

* Input Shaping
* Pressure Advance
* Resonance compensation

These **cannot correct static or quasi-static deflection**:

* First layer height variation
* Dimensional inaccuracy across travel
* Inconsistent extrusion due to nozzle-to-bed distance drift

Rod sag manifests as **geometry error**, not vibration.

---

## 7. Extruder Choice Implications

### 7.1 Why Pitan + NEMA17 Is a Good Reference

* Represents a **realistic worst-case moving mass**
* Forces honest mechanical design
* Avoids dependence on:

  * Exotic motors
  * Fragile printed flexures
  * Extreme accelerations to mask compliance

If the printer performs well with this setup:

* Lighter toolheads become upside-only improvements
* Bowden or remote drive becomes optional, not mandatory

---

### 7.2 High-Flow & CHT Context

* High-flow nozzles increase **volumetric demand**, not rod load
* Flow upgrades are only beneficial if:

  * Motion system can maintain accuracy
  * Rod deflection is already under control

> Rod sag is a **prerequisite problem** — not a nozzle problem.

---


Below is an **expanded technical section** you can drop straight into your design notes, followed by a **concise manifesto-ready summary**.

I’ve kept the math explicit but readable, and the numbers intentionally conservative so they remain valid even with scavenged or slightly imperfect rods.

---

# Rod Sag Analysis with Deflection Equations

**Reference Extruder: Pitan + NEMA17**

## 1. Beam Deflection Model

Each smooth rod is modelled as a **simply supported beam** with a **central point load**.

This is a reasonable approximation for:

* Darwin-style carriages
* Two-rod-per-axis layouts
* Toolhead load applied near mid-span during typical motion

### 1.1 Deflection Equation

For a simply supported beam with a central point load:

[
\delta = \frac{F L^3}{48 E I}
]

Where:

* ( \delta ) = maximum deflection (m)
* ( F ) = applied load per rod (N)
* ( L ) = unsupported rod length (m)
* ( E ) = Young’s modulus (Pa)
* ( I ) = second moment of area (m⁴)

---

### 1.2 Second Moment of Area (Circular Rod)

[
I = \frac{\pi d^4}{64}
]

Where:

* ( d ) = rod diameter (m)

This ( d^4 ) term is why **small diameter changes dominate stiffness**.

---

## 2. Assumptions for Numeric Examples

### 2.1 Material

* Hardened steel smooth rod
* ( E = 200 \times 10^9 , \text{Pa} )

### 2.2 Geometry & Load

* Toolhead mass: **0.6 kg** (Pitan + NEMA17 reference)
* Gravity: ( g = 9.81 , \text{m/s}^2 )
* Total load:
  [
  F_{total} = 0.6 \times 9.81 = 5.9 , \text{N}
  ]
* Load shared across two rods:
  [
  F_{rod} \approx 2.95 , \text{N}
  ]

### 2.3 Span Length

* Unsupported rod length: **350 mm (0.35 m)**
  Representative of a ~300×300 class frame with end supports.

---

## 3. Example Sag Calculations

### 3.1 8 mm Rod

**Parameters**

* ( d = 0.008 , \text{m} )
* ( I = \frac{\pi (0.008)^4}{64} = 2.01 \times 10^{-11} , \text{m}^4 )

**Deflection**

[
\delta_{8mm} =
\frac{2.95 \times (0.35)^3}
{48 \times 200 \times 10^9 \times 2.01 \times 10^{-11}}
]

[
\delta_{8mm} \approx 0.00065 , \text{m} = \mathbf{0.065 , mm}
]

---

### 3.2 10 mm Rod

**Parameters**

* ( d = 0.010 , \text{m} )
* ( I = 4.91 \times 10^{-11} , \text{m}^4 )

**Deflection**

[
\delta_{10mm} \approx \mathbf{0.027 , mm}
]

---

### 3.3 12 mm Rod

**Parameters**

* ( d = 0.012 , \text{m} )
* ( I = 1.02 \times 10^{-10} , \text{m}^4 )

**Deflection**

[
\delta_{12mm} \approx \mathbf{0.013 , mm}
]

---

## 4. Results Summary

| Rod Diameter | Mid-Span Sag | Relative to 0.2 mm Layer |
| ------------ | ------------ | ------------------------ |
| 8 mm         | 0.065 mm     | 33% of layer height      |
| 10 mm        | 0.027 mm     | 13% of layer height      |
| 12 mm        | 0.013 mm     | 6% of layer height       |

### Interpretation

* **8 mm rods** are mechanically marginal for direct drive at this span
* **10 mm rods** are acceptable with good assembly and calibration
* **12 mm rods** are mechanically robust and future-proof

Static sag above ~0.05 mm begins to:

* Affect first-layer consistency
* Undermine dimensional accuracy
* Force software compensation to hide hardware limits

---

## 5. Why Software Cannot Fix This

* Input shaping addresses **dynamic vibration**
* Rod sag is a **static geometric error**
* Bed meshes compensate Z, not XY-induced deflection

If the nozzle moves in an arc, no amount of tuning can make it straight.

---

## 6. Design Implications

* Increasing rod diameter by **2 mm** is more effective than:

  * Halving toolhead mass
  * Aggressive acceleration tuning
* Designing around **Pitan + NEMA17** prevents fragile optimisations
* Compact frame geometry directly improves print quality

Great — acceleration-induced bending is exactly the *right* next layer, and it reinforces the same design conclusions without changing direction.

Below is a **clean add-on section** you can append to the existing report, followed by a **short optional manifesto addendum** if you want it folded in later.

---

# Acceleration-Induced Rod Deflection

## 1. Why Acceleration Matters

Static sag defines the **baseline geometric error**, but during printing the toolhead is also subjected to **inertial forces** from acceleration and deceleration.

These forces:

* Act **horizontally** in X/Y
* Vary with acceleration, not speed
* Add to (or exceed) gravity-induced loads during fast direction changes

Unlike vibration, this is **quasi-static bending** during acceleration ramps — still not something input shaping can eliminate.

---

## 2. Inertial Load Model

### 2.1 Inertial Force

[
F_a = m a
]

Where:

* ( m ) = toolhead mass (kg)
* ( a ) = commanded acceleration (m/s²)

Using the reference toolhead:

* ( m = 0.6 , \text{kg} )

---

### 2.2 Typical Klipper Acceleration Ranges

| Acceleration | Value (m/s²) |
| ------------ | ------------ |
| Conservative | 2,000        |
| Moderate     | 5,000        |
| Aggressive   | 10,000       |

---

## 3. Equivalent Rod Loading

Assuming:

* Acceleration force shared across two rods
* Worst-case direction aligns fully with one axis

[
F_{rod,a} = \frac{m a}{2}
]

---

## 4. Example Inertial Loads

| Acceleration           | Total Force (N) | Force per Rod (N) |
| ---------------------- | --------------- | ----------------- |
| 2,000 mm/s² (2 m/s²)   | 1.2             | 0.6               |
| 5,000 mm/s² (5 m/s²)   | 3.0             | 1.5               |
| 10,000 mm/s² (10 m/s²) | 6.0             | 3.0               |

> At 10,000 mm/s², inertial force **matches or exceeds gravity load**.

---

## 5. Acceleration-Induced Deflection Calculations

Using the same beam model and geometry as the static sag section:

* ( L = 0.35 , \text{m} )
* ( E = 200 , \text{GPa} )

---

### 5.1 8 mm Rod

| Acceleration | Deflection |
| ------------ | ---------- |
| 2,000 mm/s²  | 0.013 mm   |
| 5,000 mm/s²  | 0.033 mm   |
| 10,000 mm/s² | 0.065 mm   |

> At aggressive acceleration, inertial bending **equals static gravity sag**.

---

### 5.2 10 mm Rod

| Acceleration | Deflection |
| ------------ | ---------- |
| 2,000 mm/s²  | 0.005 mm   |
| 5,000 mm/s²  | 0.011 mm   |
| 10,000 mm/s² | 0.027 mm   |

---

### 5.3 12 mm Rod

| Acceleration | Deflection |
| ------------ | ---------- |
| 2,000 mm/s²  | 0.002 mm   |
| 5,000 mm/s²  | 0.005 mm   |
| 10,000 mm/s² | 0.013 mm   |

---

## 6. Combined Worst-Case Deflection

Worst case occurs when:

* Toolhead is at mid-span
* Acceleration direction aligns with gravity sag direction (vector addition)
* First layer or slow perimeter (low speed, high accel segments)

### Approximate Combined Deflection

| Rod Diameter | Static Sag | Dynamic Sag | Total        |
| ------------ | ---------- | ----------- | ------------ |
| 8 mm         | 0.065 mm   | 0.065 mm    | **0.13 mm**  |
| 10 mm        | 0.027 mm   | 0.027 mm    | **0.054 mm** |
| 12 mm        | 0.013 mm   | 0.013 mm    | **0.026 mm** |

---

## 7. Design Interpretation

### Key Observations

* Acceleration, not speed, dominates dynamic bending
* Input shaping suppresses oscillation, **not beam curvature**
* High acceleration on flexible rods produces:

  * Path curvature
  * Corner rounding
  * Inconsistent extrusion width

### Practical Thresholds

* **<0.03 mm total deflection**: mechanically invisible
* **0.03–0.06 mm**: manageable, tuning-sensitive
* **>0.06 mm**: software masking required

---

## 8. Implications for Neo-Darwin

* Designing for **moderate acceleration (5–8k mm/s²)** is mechanically honest
* 8 mm rods force either:

  * Low acceleration
  * Bowden extrusion
  * Compromised geometry
* 10–12 mm rods allow:

  * Direct drive
  * Modern accelerations
  * Predictable scaling


Below is a **clean derivation**, followed by **numerical “max safe acceleration” values** per rod diameter using the same assumptions as the earlier sections. This is written so it can stand alone as a design rule, not just a calculation exercise.

---

# Maximum Safe Acceleration vs Rod Diameter

## 1. Definition of “Safe”

For this derivation, **safe acceleration** is defined as:

> Acceleration at which **acceleration-induced rod deflection does not exceed a chosen allowable deflection**.

We will use two practical limits:

* **Strict limit**:
  [
  \delta_{allow} = 0.03 , \text{mm}
  ]
  (mechanically invisible; below tuning noise)

* **Lenient limit**:
  [
  \delta_{allow} = 0.05 , \text{mm}
  ]
  (upper bound before quality depends on compensation)

---

## 2. Governing Equations

### 2.1 Acceleration-Induced Deflection

From beam theory (same model as before):

[
\delta = \frac{F L^3}{48 E I}
]

Acceleration force per rod:

[
F = \frac{m a}{2}
]

Substitute:

[
\delta = \frac{m a L^3}{96 E I}
]

---

### 2.2 Solve for Maximum Acceleration

Rearranging for ( a ):

[
\boxed{
a_{max} =
\frac{96 E I \delta_{allow}}{m L^3}
}
]

This is the **design equation**.

---

## 3. Constants Used

| Parameter             | Value                         |
| --------------------- | ----------------------------- |
| Toolhead mass ( m )   | 0.6 kg (Pitan + NEMA17)       |
| Rod length ( L )      | 0.35 m                        |
| Young’s modulus ( E ) | 200 GPa                       |
| Gravity               | Not used (pure inertial case) |

---

## 4. Second Moment of Area

[
I = \frac{\pi d^4}{64}
]

| Rod Diameter | ( I ) (m⁴)             |
| ------------ | ---------------------- |
| 8 mm         | (2.01 \times 10^{-11}) |
| 10 mm        | (4.91 \times 10^{-11}) |
| 12 mm        | (1.02 \times 10^{-10}) |

---

## 5. Maximum Safe Acceleration Results

### 5.1 Strict Limit (≤ 0.03 mm deflection)

| Rod Diameter | Max Acceleration   |
| ------------ | ------------------ |
| **8 mm**     | **≈ 4,600 mm/s²**  |
| **10 mm**    | **≈ 11,200 mm/s²** |
| **12 mm**    | **≈ 23,200 mm/s²** |

---

### 5.2 Lenient Limit (≤ 0.05 mm deflection)

| Rod Diameter | Max Acceleration   |
| ------------ | ------------------ |
| **8 mm**     | **≈ 7,700 mm/s²**  |
| **10 mm**    | **≈ 18,700 mm/s²** |
| **12 mm**    | **≈ 38,700 mm/s²** |

---

## 6. Interpretation (What This Really Means)

### 8 mm Rods

* Mechanically honest acceleration limit: **~4–5k mm/s²**
* Anything higher:

  * Relies on compensation
  * Produces path curvature during accel ramps
* Explains why “8 mm + direct drive + 10k accel” feels fragile

### 10 mm Rods

* Comfortable at **10–12k mm/s²**
* Aligns perfectly with modern Klipper defaults
* Best balance of availability, stiffness, and mass

### 12 mm Rods

* Acceleration ceases to be a structural limiter
* Toolhead mass or frame stiffness dominates instead
* Overkill unless spans are long or frame is very rigid

---

## 7. Scaling Laws (Key Design Insight)

From the derived equation:

[
a_{max} \propto \frac{d^4}{L^3}
]

Which means:

* **+2 mm rod diameter** ≫ halving toolhead mass
* **+50 mm span length** can erase stiffness gains
* Compactness is as important as rod size

---

## 8. Design Rule of Thumb

> **Choose rod diameter such that your *desired* acceleration is ≤ 50% of the theoretical max.**

This leaves margin for:

* Uneven load sharing
* Carriage offset
* Rod straightness and mounting compliance

---


## 8. Design Recommendations

### 8.1 Minimum Practical Targets

* **≤0.05 mm static sag** at mid-span under reference load
* Sag significantly less than:

  * Layer height
  * First-layer squish tolerance

### 8.2 Preferred Strategies (in order)

1. **Increase rod diameter**
2. **Reduce rod span**
3. **Improve carriage load sharing**
4. **Only then reduce toolhead mass**

---

## 9. Design Philosophy Alignment

This approach aligns with your broader manifesto themes:

* Mechanical honesty over software compensation
* Scavenged-part tolerance
* Upgrade-agnostic architecture
* Predictable behaviour over headline speed

Designing around **Pitan + NEMA17** ensures the printer remains:

* Robust
* Understandable
* Forgiving of real-world parts and assemblies

---

## 10. Conclusion

Rod sag is not an academic concern — it directly impacts print consistency, dimensional accuracy, and long-term reliability. By anchoring the analysis around a **realistic extruder mass**, the Neo-Darwin design avoids fragile assumptions and remains adaptable.

If the rods are stiff enough for **Pitan + NEMA17**, they are stiff enough for almost anything else you’ll reasonably bolt on.
