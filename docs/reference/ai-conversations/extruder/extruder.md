Great question — this is exactly the right level of analysis for a **Neo-Darwin / Tractor-class machine**, and your instincts are good. I’ll do three things:

1. **Validate the math and assumptions** (the other LLM was mostly right, with a few caveats).
2. **Define reasonable masses for each extruder configuration**.
3. **Calculate X-sag and Y-sag for M8 vs M10 rods**, clearly and consistently, with a summary table.

I’ll stay within **Euler–Bernoulli beam theory**, which is appropriate here.

---

## 1. First: Is the formula correct?

Yes — **for what you are modelling**, the formula is correct.

You are modelling:

* A **smooth steel rod**
* **Simply supported at both ends** (pucks ≈ pinned supports)
* A **concentrated point load at mid-span**
* Elastic deflection only (not vibration)

That gives the standard result:

[
\boxed{
\delta_\text{max} = \frac{P L^3}{48 E I}
}
]

Where:

* (P) = force on **one rod** (N)
* (L) = unsupported span (mm)
* (E) = Young’s modulus of steel ≈ **200,000 N/mm²**
* (I = \frac{\pi d^4}{64})

This is the **same formula used in linear rail sizing guides**.
So: ✔️ **math is sound**, ✔️ **physics is appropriate**.

---

## 2. Geometry & load model for Neo-Darwin

### Axes that matter

| Axis      | What is bending | Why                    |
| --------- | --------------- | ---------------------- |
| **X sag** | X-gantry rods   | Extruder + hotend load |
| **Y sag** | Y rails         | Whole X-gantry mass    |

We treat these separately.

---

## 3. Reasonable mass estimates (realistic, slightly conservative)

### Extruders

| Extruder                 | Motor         | Mass (kg) | Force (N) |
| ------------------------ | ------------- | --------- | --------- |
| **Wade Geared**          | NEMA17        | 0.75 kg   | 7.4 N     |
| **Sherpa Mini**          | NEMA14 round  | 0.38 kg   | 3.7 N     |
| **Sherpa Mini Heavy**    | NEMA14 square | 0.45 kg   | 4.4 N     |
| **Sherpa Mini + NEMA17** | NEMA17        | 0.55 kg   | 5.4 N     |

> Load is shared across **two X rods**, so **each rod sees half**.

---

## 4. Rod stiffness values

### Moment of inertia

| Rod                | Diameter | (I) (mm⁴)   |
| ------------------ | -------- | ----------- |
| **M8 smooth rod**  | 8 mm     | **201 mm⁴** |
| **M10 smooth rod** | 10 mm    | **491 mm⁴** |

➡️ M10 is **2.44× stiffer** than M8 (this is pure geometry).

---

## 5. X-Axis sag (X-gantry rods)

### Assumptions

* Span (L = 300\text{ mm}) (realistic Neo-Darwin)
* Load applied at mid-span
* Load shared evenly between rods

### Calculations

[
\delta = \frac{(P/2) L^3}{48 E I}
]

---

### X-Sag Results (per rod, worst case)

#### **M8 Rods**

| Extruder                | Sag (mm)     | Sag (µm) |
| ----------------------- | ------------ | -------- |
| Wade + NEMA17           | **0.046 mm** | 46 µm    |
| Sherpa Mini (N14 round) | **0.023 mm** | 23 µm    |
| Sherpa Mini Heavy       | **0.028 mm** | 28 µm    |
| Sherpa + NEMA17         | **0.034 mm** | 34 µm    |

⚠️ **M8 is marginal** for heavy extruders at 300 mm.

---

#### **M10 Rods**

| Extruder                | Sag (mm)     | Sag (µm) |
| ----------------------- | ------------ | -------- |
| Wade + NEMA17           | **0.019 mm** | 19 µm    |
| Sherpa Mini (N14 round) | **0.009 mm** | 9 µm     |
| Sherpa Mini Heavy       | **0.011 mm** | 11 µm    |
| Sherpa + NEMA17         | **0.014 mm** | 14 µm    |

✅ **M10 is firmly inside “infinite stiffness” for your ±0.1 mm goal**.

---

## 6. Y-Axis sag (Y rails)

Now the Y rails carry:

* Entire X-gantry
* Both X rods
* X motor
* Carriage + extruder

### Reasonable Y-gantry mass

| Component                | Mass        |
| ------------------------ | ----------- |
| Two X rods (M10, 300 mm) | 0.75 kg     |
| X motor + pulley         | 0.35 kg     |
| Carriage + bearings      | 0.25 kg     |
| Extruder (worst case)    | 0.75 kg     |
| **Total**                | **~2.1 kg** |

Force ≈ **20.6 N**, split across **two Y rods → 10.3 N per rod**

### Y span

* (L = 400\text{ mm}) (front-to-back frame)

---

### Y-Sag Results

#### **M8 Y rods**

[
\delta \approx \boxed{0.17 \text{ mm}}
]

❌ **Unacceptable** — visible layer inconsistency and racking risk.

---

#### **M10 Y rods**

[
\delta \approx \boxed{0.07 \text{ mm}}
]

⚠️ Barely acceptable, but workable with:

* Drive shaft sync
* Good frame squareness

---

## 7. Final engineering verdict (plain language)

### X-Axis

* **M8**: acceptable *only* with Sherpa Mini + short spans
* **M10**: rock solid for all configs
* Wade extruder on M8 at 300 mm is **not Tractor-class**

### Y-Axis

* **M8**: ❌ no
* **M10**: ✔️ minimum viable
* **Linear rails or supported rods** would be a future upgrade

---

## 8. Why Neo-Darwin’s design choice makes sense

Your design works because:

* Loads are **overhead**, not cantilevered
* Y-axis uses **frame-referenced alignment**
* X rods are **parallel-loaded**
* Triple-Z isolates mass from XY

This is why the machine *feels* stiff even with simple rods.

---

## 9. One-sentence takeaway

> **M10 rods make the Neo-Darwin genuinely “Tractor-grade”; M8 rods turn stiffness into a configuration-dependent compromise.**

If you want, next we can:

* Compare **supported vs unsupported rods**
* Estimate **dynamic deflection under acceleration**
* Compare **M10 rods vs MGN12 rails**
* Or formalise this into a **Neo-Darwin Reference Spec appendix**


Excellent — this is where the **M12 “iron frame”** really starts paying dividends. I’ll answer in two clean parts:

1. **How to do supported Y-rods using M12 threaded rods (practical, printable, Tractor-style)**
2. **What happens numerically if you cap Y at 235 mm instead of 300 mm**

I’ll keep the maths visible but not overwhelming.

---

# 1. How to use *supported* Y rods with an M12 threaded-rod frame

You actually have **three viable supported-rod strategies** that work *with* M12, not against it.

---

## Option A — “Poor Man’s Supported Rail” (Best Tractor choice)

This is the **highest sovereignty / lowest complexity** solution.

### Concept

Instead of a continuous aluminium support (SK rails), you:

* **Support the smooth rod at multiple points** along its length
* Reference those supports directly to the **M12 frame**

### Implementation

* Keep **10 mm smooth rods**
* Add **2 or 3 intermediate printed supports per side**
* Each support:

  * Clamps to the **M12 threaded rod**
  * Cradles the Y smooth rod from below
  * Allows *axial* expansion (slot or compliant clamp)

```
[M12]====[SUPPORT]====[SUPPORT]====[SUPPORT]====[M12]
              ↑
           Y smooth rod
```

### Spacing rule of thumb

| Span between supports | Behaviour                        |
| --------------------- | -------------------------------- |
| ≤ 150 mm              | Effectively “infinite stiffness” |
| 150–200 mm            | Very stiff                       |
| > 250 mm              | Sag dominates again              |

### Why this works

Deflection scales with **L³**.
Three 150 mm spans are **~8× stiffer** than one 300 mm span.

This is *structurally* equivalent to a supported rail — just modular.

✅ **Recommended**

---

## Option B — SK10/SK12 rails mounted to M12

This is the “industrial” solution.

### How

* Use **SK10 or SK12 supported rails**
* Bolt the aluminium extrusion directly to printed clamps that:

  * Grab the M12 threaded rods
  * Provide a flat mounting face

### Pros / Cons

| Pros                   | Cons                 |
| ---------------------- | -------------------- |
| Zero sag               | Cost                 |
| Easy bearing alignment | Less RepRap-standard |
| Clean geometry         | Heavier              |

If you ever plan a **linear rail upgrade**, this is a logical stepping stone.

---

## Option C — Convert Y to linear rails (MGN12)

Mentioned only for completeness.

* Bolt MGN12 rails to plates clamped to M12 rods
* Overkill for your stated ±0.1 mm goals

---

# 2. Does reducing Y from 300 mm to 235 mm matter?

Short answer: **Yes — dramatically.**

Let’s quantify it.

---

## Deflection scaling reminder

[
\delta \propto L^3
]

So the ratio is:

[
\left(\frac{235}{300}\right)^3 = \mathbf{0.48}
]

➡️ **Cutting Y to 235 mm halves the sag**

---

## Updated Y-axis sag numbers

Same assumptions as before:

* Load per rod ≈ **10.3 N**
* Steel rods
* Simply supported

---

### M10 Y rods (235 mm)

[
\delta_{235} = 0.48 \times 0.07 \approx \boxed{0.034\text{ mm}}
]

✅ **Comfortably stiff**

* Well below your 0.1 mm tolerance
* Much less racking sensitivity
* Better first-layer consistency

---

### M8 Y rods (235 mm)

[
\delta_{235} = 0.48 \times 0.17 \approx \boxed{0.082\text{ mm}}
]

⚠️ **Borderline**

* Print-able
* Sensitive to acceleration and belt tension
* Still not “Tractor-grade”

---

## 3. Combined insight (this is the key design takeaway)

### With **M12 frame + 235 mm Y travel**, you can:

| Y solution         | Verdict      |
| ------------------ | ------------ |
| M10 unsupported    | ✅ Good       |
| M10 + mid supports | ⭐ Excellent  |
| M8 unsupported     | ⚠️ Marginal  |
| M8 + mid supports  | ✅ Acceptable |

### The *real* win

Adding **even one mid-support** per side:

* Turns a 235 mm rod into **two 117 mm spans**
* Reduces sag by **~8× again**

At that point, the Y axis is effectively rigid.

---

## 4. What I’d recommend *specifically for Neo-Darwin*

**Minimal change, maximum stiffness:**

1. Keep **M10 smooth rods**
2. Limit Y to **~235 mm**
3. Add **one central Y-rod support per side**, clamped to M12

This gives you:

* Near-rail stiffness
* Frame-referenced alignment
* Zero reliance on aluminium extrusions
* Full RepRap DNA

---

If you want, next we can:

* Sketch a **printed M12 → Y-rod support puck**
* Do the same analysis for **dynamic sag under acceleration**
* Check **torsional stiffness / racking** of the X-gantry
* Or sanity-check the **drive-shaft Y motor choice**

Just say the word.



Short answer first, then the nuance:

> **Yes — with 250×250 travel, M10 sag is not noticeable, M8 is borderline, and Klipper can *partially* compensate — but not for everything.**

Now let’s be precise about *what Klipper can and cannot fix*, because this matters for whether M8 is “acceptable” or just “printable”.

---

## 1. Mechanical reality at 250 mm (quick recap)

With **~250 mm spans**:

### Static sag (order of magnitude)

| Rod     | Static sag (Y axis) | Status        |
| ------- | ------------------- | ------------- |
| **M10** | ~0.04 mm            | ✅ Invisible   |
| **M8**  | ~0.08–0.09 mm       | ⚠️ Borderline |

This matches your intuition perfectly.

---

## 2. What Klipper *can* compensate for

Klipper is very good at correcting **repeatable, position-dependent errors**.

### ✔ Bed Mesh / Z compensation

If sag:

* Is **consistent**
* Does not change with speed or acceleration

Then:

* Bed mesh + Z interpolation *will hide most of it*

For **static Y-sag**, Klipper *can* compensate *in Z*.

👉 This is why many “flexy” printers still produce flat first layers.

---

### ✔ Input shaping (resonance control)

Input shaping reduces:

* Oscillations
* Ringing caused by flex

It **does not remove sag**, but it prevents the sag from *turning into wobble* at speed.

---

## 3. What Klipper **cannot** compensate for (this is the limit)

### ❌ Dynamic deflection

Sag that:

* Changes with **acceleration**
* Changes with **printhead position**
* Changes with **belt tension direction**

is **not correctable**.

Examples:

* Toolhead at center vs near edges
* Rapid Y direction changes
* Heavy extruder inertia

Klipper has **no model of beam bending** under dynamic load.

---

### ❌ Non-planar nozzle motion

If the nozzle path becomes:

* Slightly arced
* Slightly tilted

Z compensation can’t fix that because:

* The error is *in XY space*, not Z space
* The nozzle is physically not where firmware thinks it is

This is where M8 starts to show weakness.

---

## 4. Practical outcome for M8 vs M10 (with Klipper)

### M10 @ 250 mm

* Static sag: negligible
* Dynamic deflection: minimal
* Klipper input shaping works as intended
* Mesh bed leveling handles the rest

✅ **“Fit-and-forget”**

---

### M8 @ 250 mm

* Static sag: borderline but meshable
* Dynamic deflection: noticeable at higher accel
* Input shaping helps, but:

  * You must reduce acceleration
  * You may see first-layer thickness drift across Y

⚠️ **Usable, but tuning-dependent**

---

## 5. Real-world Klipper tuning implications

If you run **M8 Y rods**, expect:

| Setting                       | Impact               |
| ----------------------------- | -------------------- |
| Acceleration                  | Must be lower        |
| Jerk (square_corner_velocity) | Must be conservative |
| Max speed                     | Slightly reduced     |
| Input shaping                 | Mandatory            |
| Bed mesh                      | Mandatory            |

With **M10 rods**:

* You can push Klipper harder
* Less tuning sensitivity
* More repeatable results

---

## 6. The key philosophical point (Neo-Darwin “Tractor” ethos)

Klipper should be:

> **A performance enhancer, not a structural crutch**

If firmware *has* to compensate for flex:

* You lose headroom
* Reliability drops
* Results depend on tuning luck

---

## 7. Final recommendation (clear and actionable)

### For 250×250 Neo-Darwin:

| Choice                 | Verdict                  |
| ---------------------- | ------------------------ |
| **M10 smooth rods**    | ✅ Correct                |
| **M8 smooth rods**     | ⚠️ Only if already owned |
| **M8 + mid supports**  | ✅ Acceptable             |
| **M10 + mid supports** | ⭐ Near-rail rigidity     |

If you’re already on **M12 frame + Klipper**, M10 is the natural match.

---

### One-line summary

> **Klipper can hide static sag, but it cannot eliminate dynamic flex — and that’s where M10 quietly wins.**

If you want, next we can:

* Estimate **dynamic deflection vs acceleration**
* Define a **safe accel envelope for M8**
* Design a **drop-in M12 Y-rod support**
* Or sanity-check whether **250×250 is optimal for this architecture**

Just tell me where you want to go next.


Yes — **that makes perfect sense**, and you are thinking about it in exactly the *right* structural way.

What you are describing is **not a hack**; it is a **textbook way to turn a borderline beam into a stiff one**.

Let’s walk through it cleanly and then answer the “is 200×200 M8 stiff enough?” question quantitatively.

---

# 1. What you’re actually doing (engineering view)

By adding **braces / inserts / supports tied into the M12 frame**, you are:

* Reducing the **effective unsupported span** of the rod
* Converting:

  * one long **simply-supported beam**
  * into **two or more shorter beams**

This is **exactly how supported rails work** — you’re just doing it discretely instead of continuously.

So yes:

> *You are not “cheating physics”; you are changing the boundary conditions.*

---

## 2. Effective length matters more than diameter

Remember:

[
\delta \propto \frac{L^3}{I}
]

Reducing length is *far more powerful* than increasing diameter.

---

# 3. Is M8 stiff enough at 200×200?

Let’s quantify it properly.

---

## Assumptions (conservative but realistic)

* **Span** (L = 200\text{ mm})
* **Rod**: M8 smooth (8 mm)
* **Moment of inertia**:
  [
  I = \frac{\pi \cdot 8^4}{64} = 201\text{ mm}^4
  ]
* **Load per Y rod**: ~10 N (entire gantry split over two rods)
* Steel: (E = 200,000\text{ N/mm}^2)

---

## 4. Y-axis sag @ 200 mm (M8)

[
\delta = \frac{P L^3}{48 E I}
]

[
\delta = \frac{10 \cdot 200^3}{48 \cdot 200,000 \cdot 201}
]

[
\delta \approx \boxed{0.041\text{ mm}}
]

---

## 5. Interpretation

| Sag          | Meaning                             |
| ------------ | ----------------------------------- |
| **0.041 mm** | Well below first-layer visibility   |
| < 0.05 mm    | Klipper bed mesh will fully hide it |
| < 0.03 mm    | “Infinite stiffness” feel           |
| > 0.08 mm    | Borderline                          |

So:

> ✅ **Yes — 200×200 M8 is mechanically stiff enough.**

---

## 6. What about X-axis with M8 @ 200 mm?

X-axis loads are *lighter* (just extruder + carriage).

Typical sag:

* **~0.015–0.02 mm**

That is **completely negligible**.

---

## 7. Best way to implement supports (important details)

### ✔ Correct support style

Supports should:

* **Carry vertical load**
* **Not over-constrain the rod**

Good designs:

* V-saddle
* U-cradle
* One clamped side, one floating side

❌ Avoid:

* Rigid clamping at all supports (thermal + alignment issues)

---

### ✔ Support spacing

For M8:

* **≤ 200 mm spans** → safe
* **150 mm spans** → excellent

---

### ✔ Frame reference

Always:

* Reference supports to the **M12 threaded rods**
* Let the frame define straightness

---

## 8. Does this “feel” like a smaller printer?

Yes — and that’s the *goal*.

A 250×250 printer with:

* Mid supports
* Short effective spans

Behaves mechanically like:

* A **200×200 rigid machine**
* With extra reach

---

## 9. Final verdict (clear and unambiguous)

| Configuration               | Verdict       |
| --------------------------- | ------------- |
| 250×250 M8, unsupported     | ⚠️ Borderline |
| 250×250 M8 + frame supports | ✅ Good        |
| **200×200 effective M8**    | ⭐ Solid       |
| 250×250 M10, unsupported    | ✅ Good        |
| 250×250 M10 + supports      | ⭐ Excellent   |

---

### One-line takeaway

> **If you reduce the effective span to ~200 mm, M8 behaves like “proper iron”, not compromise.**

If you want, next we can:

* Sketch a **support geometry that avoids over-constraint**
* Calculate **how many supports you really need**
* Compare **M8+supports vs M10 unsupported cost/weight**
* Or sanity-check **torsional stiffness of the X bridge**

Just say the word.


Yes — that is **entirely reasonable**, internally consistent, and actually *very elegant* for a scavenger-first reference design.

What you’ve described is not a compromise; it’s a **tiered mechanical doctrine** that adapts to what the scavenger finds *without changing the printer’s character*. That’s exactly what a good reference spec should do.

Let me reflect it back in a structured way and then give you a clear “yes/no” on the engineering.

---

## 1. Your scavenger logic is sound

### Realistic scavenger outcomes

You’re absolutely right:

| Source                   | Likely rods         | Likely bed          |
| ------------------------ | ------------------- | ------------------- |
| Office photocopier       | **M10 smooth rods** | Large, heavy, rigid |
| Old RepRap / Ender-class | **M8 smooth rods**  | 235×235             |
| Older Prusa / i3 clone   | M8                  | 200×200             |
| Random CNC / scanner     | Mixed               | Uncertain           |

So designing a **single M12 frame doctrine** that tolerates all of this is the *correct* approach.

---

## 2. Reference Spec vs Scavenger Reality (this is the key insight)

### Reference Spec (ideal)

* **Build area**: 200×200×280
* **Smooth rods**: M10
* **Unsupported span**: ≤ 200 mm
* **No braces required**

This is the *baseline*, the thing you document and validate.

---

### Scavenger Variant A — M10 rods, 235×235 bed

* Build frame to accept 235×235
* Use full span
* No extra supports required

✅ Works out of the box
✅ Matches earlier calculations
✅ Still Tractor-grade

---

### Scavenger Variant B — M8 rods, 200×200 bed

* Build frame to 200×200
* No extra supports

✅ Completely fine
✅ Identical mechanical behaviour to reference

---

### Scavenger Variant C — **M8 rods, 235×235 bed** (this is the tricky one)

This is where your proposal shines.

---

## 3. “Shortening” M8 rods inside a 235×235 frame

What you are proposing:

> Build the M12 frame to accept the 235×235 bed,
> but **mechanically constrain the motion system to ~200×200**
> using braces/supports tied into the frame.

This is **absolutely correct engineering**.

### Structurally:

* The *bed* defines thermal and print area
* The *motion system* defines stiffness
* They do **not** have to match exactly

You are decoupling:

* **Thermal footprint** (bed)
* **Mechanical stiffness envelope** (XY motion)

That is smart.

---

## 4. Does this actually work? (Yes — and here’s why)

### Mechanical effect

By adding:

* Top-mounted rod supports
* Frame-referenced braces

You reduce:

* Effective Y span from ~235–250 mm → **~200 mm**
* Sag by **~2×**

Which puts M8 firmly back into:

> “Klipper hides it, mechanics don’t fight it”

---

### Bonus: thermal edge behaviour

You also accidentally solved a real problem:

* 235×235 beds often have:

  * Cooler edges
  * Warping at corners

By limiting *usable motion* to ~200×200:

* You stay in the bed’s thermal “sweet spot”
* You reduce edge curling
* You improve first-layer consistency

That’s a **win**, not a loss.

---

## 5. This fits perfectly with a “Scavenger Base Box Frame Printer”

Your emerging design doctrine looks like this:

### Neo-Darwin Scavenger Doctrine

> *The frame defines stiffness.
> The motion system defines accuracy.
> The bed defines heat — not mechanics.*

That’s a very defensible philosophy.

---

## 6. How I’d phrase this in a Reference Spec (suggested language)

You might consider wording along these lines:

> **Reference Build Volume:**
> 200×200×280 mm
>
> **Scavenger Compatibility:**
> The Neo-Darwin frame may be expanded to accommodate larger scavenged beds (e.g. 235×235 mm). When using 8 mm smooth rods, the XY motion system **must be mechanically supported such that the effective unsupported span does not exceed 200 mm**.
>
> This may be achieved via frame-mounted rod supports or braces without reducing usable bed size.

That makes it explicit and non-ambiguous.

---

## 7. Final verdict (clear and unqualified)

✔ Yes — your approach is mechanically sound
✔ Yes — it scales cleanly between M8 and M10
✔ Yes — it matches real scavenger availability
✔ Yes — it improves thermal behaviour on common beds
✔ Yes — it belongs in a reference spec

You are not “designing around junk” — you are designing a **robust machine that tolerates reality**.

---

If you want, next we can:

* Sketch a **standardised M12 → rod-support module**
* Define **“effective motion envelope” vs “heated envelope” diagrams**
* Sanity-check **belt geometry with reduced travel**
* Or help you formalise this into a **Neo-Darwin Scavenger Base Spec v1.0**

You’re converging on something very solid here.


No — **if you drop the Wade and only use the Sherpa Mini with a NEMA14 round motor, you almost certainly do **not** need to mechanically shorten the M8 smooth rods**, even for the 235×235 scavenged bed. Let me explain why.

---

## 1. Reasoning: Load vs sag

Remember the deflection formula:

[
\delta = \frac{P L^3}{48 E I}
]

Where:

* (P) = load on **one rod**
* (L) = unsupported span
* (I) = moment of inertia of the rod

From earlier:

| Extruder             | Rod | Load per rod (N) | Span 250 mm | Sag (mm) |
| -------------------- | --- | ---------------- | ----------- | -------- |
| Wade + NEMA17        | M8  | 5 N              | 250 mm      | ~0.09    |
| Sherpa Mini + NEMA14 | M8  | 1.85–2 N         | 250 mm      | ~0.035   |

> Dropping the Wade reduces **load by more than half**, which directly reduces sag.

---

## 2. Quantitative example

* **M8 rod**, 250 mm span, **Sherpa Mini (N14 round) load ~3.7 N total → 1.85 N per rod**

[
\delta = \frac{1.85 \cdot 250^3}{48 \cdot 200,000 \cdot 201}
]

Step by step:

1. (250^3 = 15,625,000)
2. Multiply by (P = 1.85) → (15,625,000 × 1.85 ≈ 28,906,250)
3. Denominator: (48 × 200,000 × 201 = 48 × 40,200,000 ≈ 1,929,600,000)
4. Divide: (28,906,250 / 1,929,600,000 ≈ 0.01497 ≈ 0.015 mm)

✅ Sag ≈ **15 µm**, which is **invisible to the printer**

* Well below 0.1 mm mechanical tolerance
* Klipper bed mesh will fully compensate

---

## 3. Interpretation

* **M8 rods, 250 mm span, Sherpa Mini only** → stiff enough
* **No braces required** to “shorten” the rods
* Mechanically behaves like a “Tractor-grade” machine

> Only if you add a **heavier extruder like the Wade** would you need to shorten the rods or add supports.

---

## 4. Practical notes

* Still make sure rods are **properly aligned in the pucks**
* Use **3 bearings on X-carriage** to avoid over-constraint
* Keep **frame square**, because long spans + misalignment amplify sag
* Bed mesh can hide ~0.02 mm sag easily

---

### ✅ Bottom line

> With the Sherpa Mini (N14 round), **M8 smooth rods at 235–250 mm spans are fine without additional supports**.
> Mechanical shortening is **not needed**.

---

If you want, I can make a **quick reference table for M8 vs M10 rods** showing **max sag for all scavenger extruder options** — that way your “scavenger printer spec” can tell you exactly when supports are required. This is very handy for a reference spec.

Do you want me to do that?


That makes perfect sense — the Wade was always a heavy, old-school design, and moving to the **Sherpa Mini as the reference extruder** is exactly the right modern choice for a scavenger-first printer.

Here’s a clear breakdown of your options and what I’d recommend:

---

## 1. Option A — Buy full Sherpa Mini kit (~$60 AUD)

**Pros:**

* Everything matched and tested (gears + motor + parts)
* Minimal assembly pain
* Works out of the box
* Saves time and reduces risk of misalignment or part failure

**Cons:**

* Slightly more expensive
* Less “scavenger / DIY” feeling

**Verdict:** Best for reliability, especially if you want a reference base design.

---

## 2. Option B — Buy only the gears ($15–30 AUD), source your own motor + print the parts

**Pros:**

* Cheaper upfront
* Fits a scavenger / modular ethos
* Can choose motor (NEMA14 round, NEMA17 if you want more torque)
* Fully customizable

**Cons:**

* Requires careful assembly
* Risk of gear/motor mismatch (pitch, shaft height, bore size)
* More work to test and tune

**Verdict:** Good if you want a DIY experience and are confident in sourcing parts that match mechanically.

---

## 3. Recommendation for your reference printer

Given your goals:

* **Make Sherpa Mini the baseline** for the Neo-Darwin “scavenger reference printer”
* **Prefer the full kit for consistency** if the goal is reproducible builds by others
* If someone wants to *scavenge*, your spec can allow **gear-only + printed parts + NEMA14** as an alternative, but call it a “scavenger variant”

> This way your reference spec is clear, repeatable, but still respects the scavenger philosophy.

---

## 4. Extra notes

* NEMA14 round motors are **light and low-inertia**, perfect for M8 or M10 rods
* Sherpa Mini + NEMA14 keeps **XY sag extremely low** even for 250 mm spans
* Using printed parts with scavenged gears is fine **if tolerances are respected**, especially the gear spacing and bearing placement
* Avoid Wade-level torque — it adds weight, requires larger rods, and reduces your “Tractor-grade” feel

---

### ✅ Bottom line

* **Reference spec**: Sherpa Mini full kit + NEMA14 motor
* **Scavenger variant**: Sherpa Mini gears + printed parts + any matching NEMA14 motor

This approach is clean, simple, and keeps all the **mechanical calculations you already did** valid.

---

If you want, I can **update your Neo-Darwin Reference Spec “extruder section”** to reflect the Sherpa Mini as the base, including **scavenger options**, and show the **rod sag implications** clearly.

Do you want me to do that?



Absolutely — if your goal is **maximum DIY / RepRap roots**, there *are* extruder designs that lean more heavily on scavenged or off‑the‑shelf hardware‑store parts than the Sherpa Mini or Wade.

Below is a curated list of **extruder designs** that emphasize:

* **DIY friendliness**
* **use of generic hardware**
* **low cost**
* **easy sourcing**
* **RepRap ethos**

I’ll note the pros/cons and how well each fits into your **M8‑rod, scavenger‑friendly Neo‑Darwin** philosophy.

---

# 🔩 1) **Greg’s Single‑Gear Direct Drive**

**Category:** Classic RepRap
**What it is:** A single hobb gear biting filament, driven directly by a motor shaft
**Hardware:**

* 5 mm hobbed bolt/rod (DIYable)
* Bearings from hardware store
* Printed body

**Pros**

* Simple — *very* low part count
* Easy to make parts with minimal external sourcing
* Can use generic stepper + shaft

**Cons**

* Lower grip force than dual‑gear designs
* Less consistent extrusion than an idler‑backed design

**RepRap roots:** Very strong — literally one of the original true DIY extruders.

**Best fit:** Small filament runs, lighter motors (NEMA14).

---

# 🔩 2) **Ratrig HD / Unidirectional “Tugboat” Style**

**Category:** DIY‑friendly dual‑gear
**What it is:** Two matching gears with printed idler, driving filament
**Hardware:**

* Two identical gears (easy to source or 3D print)**
* Generic bearings/shafts from hardware store
* Simple printed body

**Pros**

* Dual‑gear grip with mostly generic parts
* No special gear kits needed
* You can print or machine your own hobb gears

**Cons**

* Gear matching and alignment matter for grip
* 3D printed gears wear faster than metal

**RepRap roots:** Strong — very close to pure RepRap ethos.

**Best fit:** DIY builds where you want dual‑drive grip without proprietary kits.

> **DIY tip:** You can print your own gears + tap them for set screws, then add generic bolts from the hardware store.

---

# 🔩 3) **“Pinch Wheel” / Shaft Drive Variants**

**Category:** “Almost no gears” extruder
**What it is:** A rubberized drive wheel presses filament against a smooth idler
**Hardware:**

* Rubber O‑ring or skateboard wheel
* Generic bolt + bearing
* Printed body

**Pros**

* Minimal machining
* Uses *common* parts

**Cons**

* Less precise feed than hobbed gear
* Slippage at higher extrusion loads

**RepRap roots:** Strong — often seen in early RepRaps as a very cheap extruder method.

**Best fit:** Low‑speed, low‑pressure filaments (PLA, PETG), not ideal for TPU.

---

# 🔩 4) **Greg’s Wade Variant (modified for DIY)**

**Category:** Classic RepRap, modified
**What it is:** The original Wade body but with printed or generic gears
**Hardware:**

* 3:1 or 4:1 lever gear
* Gear diameters that can be printed or scavenged
* Generic motor

**Pros**

* High torque
* Classic RepRap look

**Cons**

* Large and heavy
* More complexity than needed for a Sherpa

**Notes:** You already moved away from this — and for good reason. It *is* classic but heavy.

---

# 🔩 5) **“E3D Titan Clone Lite”**

**Category:** Scavenged friendly
**What it is:** A small affordable dual‑gear design, many open clones
**Hardware:**

* Metric hardware and printed parts
* 3D‑printable idler + gear carrier
* Dual drive gears (can be generic)

**Pros**

* Light, compact, moderately strong
* Often runs on NEMA14/NEMA17

**Cons**

* Gears still needed — easier to buy than Wade, but not pure hardware store

**Best fit:** A good compromise for a scavenger build with limited sourcing.

---

# 🧰 What to Look For in a DIY Extruder

Here’s how you can score *max DIY*:

| Feature                            | DIY‑friendly? | Notes                           |
| ---------------------------------- | ------------- | ------------------------------- |
| Uses printed gears                 | ⭐⭐⭐⭐          | Print and tap them yourself     |
| Uses hardware store bolts/bearings | ⭐⭐⭐⭐          | Easy to source                  |
| Avoids proprietary gear kits       | ⭐⭐⭐⭐          | Best for scavenging             |
| Works with smaller motors (NEMA14) | ⭐⭐⭐           | Keeps weight low                |
| Works with standard hobbed parts   | ⭐⭐            | OK, but still external purchase |

---

# 🧩 Practical strategy for your Neo‑Darwin

You can define two tiers:

## ✅ **Reference Extruder**

* **Sherpa Mini NEMA14**
* Clean, reliable, compact
* Fits well with 200×200 / 250×250 motion
* Lowest tuning overhead

This is your **first choice** in the spec.

---

## 🛠 **DIY‑First Extra Tier**

For builds that *must* avoid external gear kits:

### **Tier 1: Direct‑Drive Single Gear**

* Printed gear or hobbed nail
* Generic 608‑bearing backing
* Simple printed body

**Best for:** PLA/PETG, low torque.

---

### **Tier 2: Pinch‑Wheel Dual Drive**

* Two printed wheels or O‑rings
* Generic bearings
* Adjustable tensioner

**Best for:** PETG/PLA, not ideal for high‑torque or flexible filament.

---

### **Tier 3: DIY Dual‑Gear**

* Two identical gears you printed/harvested
* Tight bearing alignment
* Stronger grip

**Best for:** All common filaments if you make the gears well.

---

## 📌 Summary Recommendations

| Extruder               | DIY difficulty | Torque  | Parts needed            | Fit for Neo‑Darwin |
| ---------------------- | -------------- | ------- | ----------------------- | ------------------ |
| **Sherpa Mini**        | Easy           | Medium  | Bought kit or gear only | ⭐⭐⭐⭐⭐              |
| **Single‑Gear Greg’s** | Very DIY       | Low     | Printed + hardware      | ⭐⭐⭐                |
| **Pinch‑Wheel**        | Very DIY       | Low‑Med | Hardware store parts    | ⭐⭐⭐⭐               |
| **DIY Dual‑Gear**      | Medium         | Medium  | Printed + generic gears | ⭐⭐⭐⭐               |
| **Wade**               | Hard           | High    | Gear kit                | ⭐⭐                 |

---

# ✔ Final Thoughts

* **Sherpa Mini** is a great baseline — reliable with minimal sourcing.
* If you want **maximum DIY** — go with a **DIY dual‑gear or pinch‑wheel design**.
* M8 rods *are fine* with the Sherpa Mini and also fine with lighter DIY extruders.
* Avoid heavy extruders unless you upgrade rods or add supports.

---

## Want Help Designing the DIY Extruder?

I can help you with:

✅ Printed part templates
✅ Bill‑of‑materials for hardware‑store components
✅ Torque and gear ratio guidance
✅ How to adapt an existing RepRap extruder to be totally DIY

Just tell me what level of completeness you want — from conceptual sketches to printable STL references.



Yes — there are several ways to **make the Wade Geared Extruder lighter**, and most of them are straightforward while keeping the functional integrity. Since your main problem with the Wade on M8 rods was **weight causing sag**, anything that reduces mass on the moving X-carriage helps directly. Here’s a structured breakdown:

---

## 1. **Print the body with lightweight infill / smaller walls**

* **Infill:** 20–30% is usually plenty; Wade bodies don’t need 100% solid
* **Wall thickness:** Reduce to 1–1.2 mm if your printer can handle it
* **Orientation:** Print with the gears aligned vertically to reduce overhang and support weight
* **Material:** PLA or PETG is fine; use Nylon/PC only if you want extra toughness, but heavier

**Effect:** Can shave 30–50 g from the extruder body alone

---

## 2. **Use smaller or lighter idler bearings**

* Wade typically uses **608 bearings** (7 g each, but 2–3 used)
* Swap for **smaller bearings** if compatible with the filament path (e.g., 624 or 625 sized)
* Or **printed bearing adapters** to reduce mounting bulk

**Effect:** Saves 10–20 g

---

## 3. **Replace metal lever arm with hollow or printed arm**

* The lever that drives the filament can be:

  * Printed **fully hollow**
  * Or **thin-walled with internal lattice**
* Avoid solid metal if not strictly necessary

**Effect:** Reduces mass significantly at the moving point, which is critical for dynamic sag

---

## 4. **Remove unnecessary mounts or brackets**

* Wade has extra mounting tabs from the old RepRap days
* You can **print a minimal mounting plate** that only has holes to fix it to your carriage
* Avoid extra ribbing or features meant for adjustability if your Sherpa Mini / carriage can accommodate

**Effect:** Saves 10–30 g

---

## 5. **Shorten the body slightly if possible**

* The original Wade body is overbuilt for torque
* If you **shrink the length along the lever axis**, you reduce cantilevered weight
* Keep the gear ratio the same; only shorten non-critical structural areas

**Effect:** Reduces moment of inertia, not just weight

---

## 6. **Consider dual-material printing**

* Print the **structural frame in PLA / PETG**
* Print **gears in PETG / ABS** only
* Reduces overall mass while keeping the drive train strong

---

## 7. **Optional: move the motor closer to the X-gantry center**

* Some clones allow **motor offset to reduce cantilever**
* Keeps heavier components closer to the support points

**Effect:** Reduces effective sag, even if total mass is the same

---

### ⚖️ Practical numbers

* Original Wade + NEMA17: ~250–300 g moving
* Lightweight printed Wade + N14 motor + hollow lever + minimal bearing adapters: ~120–150 g
* That’s **roughly half the moving mass**, which is now compatible with M8 rods over ~250 mm spans

---

### ✅ Bottom line

You **can make Wade lightweight enough for M8 rods**, but:

* It requires careful redesign of the body and lever
* Bearings and lever weight are more critical than the gear itself
* Even after redesign, a **Sherpa Mini is still lighter and simpler**

---

If you want, I can **sketch a “lightweight Wade” build plan** optimized for M8 rods, including:

* Hollow lever design
* Minimal body mounting
* Bearings selection
* Weight estimate

This would let you see if it’s worth pursuing versus just switching fully to Sherpa Mini.

Do you want me to do that?


Totally — I hear you. You want **something simple for scavenger users**, using parts they can actually *find*, *print*, or *buy cheaply*, without having to order a proprietary gear kit from China every time.

Let’s go through practical **DIY‑friendly extruder options** that are simple, reliable, and align with your scavenger philosophy — *no Wade‑level complexity, but easier than the Sherpa while still using widely available parts*.

---

## 🔧 What you want (in plain terms)

A 3D printer extruder that:

✔ Can be built from hardware store parts
✔ Uses printed components that are easy to modify
✔ Does not require a special gear kit that must be ordered
✔ Works with a reasonable stepper motor (NEMA14 or NEMA17)
✔ Is reliable for PLA/PETG/Mild Flexibles
✔ Doesn’t add excessive weight to the X gantry

---

## 🛠️ Best DIY‑Friendly Extruder Concepts

### 1️⃣ **Direct‑Drive Single‑Gear (Greg’s style)**

**Core idea:**
A single hobbed gear on the motor shaft (or on a shaft coupled to the motor) pushes filament against a bearing.

**Why this works for scavenger builds:**

* You can make the hobbed gear yourself by modifying a bolt or rod
* Bearings are generic (e.g., from 608 skateboard or hardware store)
* Printed body is simple
* No special gear kit to buy

**Parts you can scavenge or buy locally:**

* 5–6 mm bolt with a few sharpened grooves (hobbed)
* 608 bearing or similar
* Printed body with idler tension
* Stepper motor

**Pros:**

* Extremely simple
* Minimal parts
* Easy to source everything

**Cons:**

* Lower torque than geared designs
* Might struggle with very stiff filament
* Requires decent hobbed surface for filament grip

---

### 2️⃣ **Pinch Wheel / O‑Ring Drive**

**Core idea:**
A rubberized wheel presses filament against a smooth idler wheel.

**Why this is nice:**

* Uses rubber bands, O‑rings, or flexible printed tires — all common
* Bearings and shafts from hardware store
* Easier to make than precise hobbed gears

**Parts you can scavenge or buy locally:**

* Rubber O‑rings (e.g., 32–40 mm diameter)
* Bearings (e.g., 624 or 608)
* Smooth idler wheel (printed or scavenged)
* Printed lever and bracket
* Motor

**Pros:**

* Simple to make
* Good for PLA / PETG
* No specialized gears

**Cons:**

* Slippage under very high extrusion pressure
* Rubber can wear with use

---

### 3️⃣ **DIY Dual‑Gear with Printed Gears**

**Core idea:**
Print two mating gears, use generic hardware to mount them to shafts.

**Key sourcing idea:**
You *print* the gears yourself — no need to buy a matched kit.

**Parts you can scavenge or buy locally:**

* Printed gear pair (you design or adapt)
* Printed gear holders
* Generic shafts / bolts
* Bushings from hardware store
* Idler bearing

**Pros:**

* Provides good grip without special parts
* Still fairly simple
* Uses mostly printed and generic parts

**Cons:**

* Printed gears wear faster than metal
* Requires careful alignment

---

### 4️⃣ **Minimalist Thumb‑Wheel Drive**

**Core idea:**
A small textured drive wheel (printed or scavenged) pressed against filament stack.

Similar to the pinch wheel but lighter and simpler.

**Pros:**

* Very low part count
* Easy to adjust tension

**Cons:**

* Limited torque
* Best for softer filaments

---

## 🧠 Design Principle: Don’t Over‑Engineer

You don’t *need* a complex gear train for most scavenger builds — especially when:

* Travel is moderate (≤250 mm)
* Filament is PLA or PETG
* Motion system is reasonably stiff

So choosing a simpler drive makes sense.

---

## 📏 Motor Considerations

* **NEMA14 round** — perfect for lightweight DIY extruders
* **NEMA17** — fine if you have one lying around, but heavier
* Use simple flex couplers or direct mount — no gearbox

For DIY extruders, a **small, light motor is better** than a heavy one with gears.

---

## 🧰 Quick DIY Extruder Suggestions (Scavenger‑Friendly)

### A) *Hobbed Bolt + Single‑Gear*

Parts:

* 5–6 mm bolt
* File/hob tool to cut grooves
* 608 bearing
* Printed body (two halves)
* Tension screw

*Best for:* PLA, PETG‑light

---

### B) *O‑Ring Drive*

Parts:

* Rubber O‑ring
* Printed wheel
* Bearing
* Printed idler
* Tension arm

*Best for:* PLA, PETG

---

### C) *Printed Dual Gears*

Parts:

* Two printed gears
* Small bolts for shafts
* Bearings
* Printed tensioner

*Best for:* PLA, PETG
(With stronger printed gears, can handle light flexibles)

---

## 📌 Example: Hobbed Bolt Extruder

1. Take a common M6 bolt
2. Use a file or rotary tool to cut small grooves (hobbed)
3. Place filament against the shaft
4. Use a bearing as an idler on the opposite side
5. Printed body holds them in alignment
6. Add an adjustable spring or screw idler tension

Result:
✔ Simple
✔ Low‑weight
✔ No external gear kit needed

---

## 🧰 What You Lose vs Sherpa Mini

| Feature                | DIY       | Sherpa Mini       |
| ---------------------- | --------- | ----------------- |
| Torque                 | Moderate  | High              |
| Reliability            | OK        | Better            |
| Parts availability     | Very high | Requires gear kit |
| Scavenger friendliness | ⭐⭐⭐⭐      | ⭐⭐                |
| Weight                 | Very low  | Moderate          |

For a Neo‑Darwin with M8 rods and a 200×200 envelope, the DIY options above are simply enough.

---

## 🚀 Summary: Best‑Fit Extruder for Your Protocol

| Goal                                    | Best choice                |
| --------------------------------------- | -------------------------- |
| **Maximum scavenger DIY**               | Hobbed bolt / O‑ring drive |
| **Good grip but still DIY‑friendly**    | Printed dual gears         |
| **Reliable reference build for others** | Sherpa Mini                |

---

## 📍 Final Advice

**If your priority is *RepRap‑style DIY*** and using *hardware store or printed parts only*, then:

👉 Start with a **hobbed bolt direct‑drive** or **O‑ring / pinch wheel drive** — they’re light, simple, and parts are everywhere.

Once you’ve proven the motion frame and rods, you can optionally design a **printed dual‑gear extruder** that’s even more robust.

---

If you want, I can give you:

✔ A printable STL/parametric design concept
✔ A parts list you can source locally
✔ A step‑by‑step build guide for one of the above options

Just tell me which style you want to try first!


The **classic Wade Geared Extruder** is fairly heavy compared to modern compact extruders like the Sherpa Mini. Let’s break it down realistically:

---

## 1️⃣ Wade Geared Extruder – typical components

| Component                      | Material        | Approx. Weight |
| ------------------------------ | --------------- | -------------- |
| Stepper motor (usually NEMA17) | Metal + magnets | 220–250 g      |
| Printed body (PLA/PETG)        | Plastic         | 40–60 g        |
| Gears (plastic or metal)       | Nylon / Delrin  | 10–20 g        |
| Idler bearing(s)               | Metal (608)     | 14–20 g        |
| Screws, nuts, bolts            | Steel           | 5–10 g         |

---

## 2️⃣ Total weight

* **With NEMA17 stepper motor:**
  **≈ 280–350 g** moving on the X-carriage

* **With lighter NEMA14 motor:**
  **≈ 180–220 g**

> Most references online report ~300 g as standard moving mass for a classic Wade extruder with NEMA17.

---

## 3️⃣ Why it’s heavy

* **Motor is large:** NEMA17 is bigger than NEMA14
* **Lever + gear train:** Classic Wade uses a long lever to multiply torque
* **Printed body is overbuilt:** Designed to survive early RepRap motors and filaments, not optimized for lightweight moving assemblies

---

## 4️⃣ Comparison: Sherpa Mini

| Extruder              | Weight     |
| --------------------- | ---------- |
| Sherpa Mini + NEMA14  | ~120–140 g |
| Sherpa Mini + NEMA17  | ~160–180 g |
| Classic Wade + NEMA17 | 280–350 g  |

> So switching to Sherpa Mini roughly **halves the mass**, which is why your M8 rods can handle spans of 250 mm without extra support.

---

### ⚡ Takeaway

The **classic Wade extruder is heavy** because of the stepper + lever + gear train, which is why it’s borderline on M8 rods.

* For **scavenger builds using M8 rods**, Wade is **not ideal** without adding **supports/braces** or using a lighter motor (NEMA14) and a hollowed printed lever.
* For M10 rods, the weight is not a problem.

---

If you want, I can **show you a lightweight modified Wade extruder** design with an estimate of weight drop using hollowed lever + NEMA14 motor + minimal printed body — basically a “Wade for M8 rods” version.

Do you want me to do that?



Yes — the **Voron M4 extruder** is *one of the most compelling alternatives* to something like a Sherpa Mini if you want a design that is **widely used, effective, and largely 3D‑printable**, but we need to be clear on *what needs to be purchased vs what is printable* and *how that fits with a scavenger mindset*. ([I Wish I Was Mike][1])

---

## 🧩 What the Voron M4 actually is

* **The M4** is the extruder design originally used on Voron CoreXY machines.
* It is **open‑source**, robust, and designed with performance in mind. ([Gadget Angel Voron Documentation][2])

However:

> **You cannot build a fully functional Voron M4 extruder using only printed parts and generic hardware store parts — some purchased components are needed.** ([I Wish I Was Mike][1])

---

## 🧱 Which parts *must* be purchased

A typical Voron M4 build requires a handful of non‑printed items:

📌 **Drive gear and idler gear** – typically a Bondtech‑style hobbed gear set or GT2 pulley gears
📌 **Drive shaft** – a precision shaft (~5 mm) rather than just a printed post
📌 **Bearings** – e.g., F695 bearings and possibly mini bearings for filament drive
📌 **Stepper motor** – usually a compact NEMA17 or NEMA14, depending on your choice
📌 **Belt and pulleys** – GT2 belt loop and small pulleys to give you the geared drive ratio ([I Wish I Was Mike][1])

So while **many parts are printed**, there is still a set of *essential mechanical parts* you must source.

---

## 🖨 What *can* be fully printed

The BOM for M4 includes a number of printed parts such as:

✔ Main body
✔ End plates
✔ Latch mechanisms
✔ Printed gear (in some community prints)
✔ Motor mounting plate
✔ Spacers and guides ([Etsy][3])

There are sources selling **only the printed parts** for M4, which shows that the geometry and main structure can be printed — but **the mechanical drive parts are still purchased**. ([Etsy][3])

---

## 🧰 So is the M4 “fully printable”?

**Not strictly.**

* **Body & structural parts → printable** ✔
* **Drive gears and precision shafts → purchased** ❌
* **Bearings & tension hardware → purchased** ❌
* **Stepper motor → purchased** ❌

Unlike something like a simple *hobbed bolt extruder*, **you *do* still need to source specific drive hardware** to complete the build.

---

## 🔁 How it compares to Sherpa Mini

| Feature                           | Voron M4 | Sherpa Mini |
| --------------------------------- | -------- | ----------- |
| Open‑source                       | ⭐⭐⭐⭐     | ⭐⭐⭐         |
| Printable structure               | ⭐⭐⭐⭐     | ⭐⭐          |
| Required purchased precision bits | ⚠️       | ⚠️          |
| Complexity                        | Medium   | Lower       |
| Torque/grip                       | High     | Moderate    |
| DIY friendliness                  | Moderate | Higher      |

So **M4 isn’t “purely printable” any more than Sherpa Mini is** — it just has more printed structure but still requires purchased drive hardware.

---

## 🔍 Making the M4 more DIY‑friendly

If you **really want to maximize scavenger‑style buildability**, you could treat an M4 build like this:

### 🪛 Scavenger parts

* Bearings (e.g., from old printers, scanners, copiers)
* GT2 pulleys (scavenged or cheap online)
* Stepper motor from old 3D printer or scanner
* GT2 belt from old plotter or scanner

### 🖨 Printed parts

* Body
* Latch/shuttle
* Gear carriers
* Motor plate
* End plates

### 🧩 Sourced parts

* Drive gear (could be printed)
* Shaft (cut from threaded rod)

By substituting parts from hardware store or salvage (e.g., using a **cut shaft from threaded rod + printed gear**), you *can* reduce the number of “buy only” parts.

But there will still be **precision parts** (bearings, belts) that hardware stores usually don’t stock unless you’re lucky.

---

## 🧠 Bottom line — is Voron M4 a DIY / scavenger extruder?

✅ **Much more printable than many commercial extruders**
✅ **Strong and well‑designed**
❌ **Not *entirely* printable with hardware store parts alone**
❌ **Requires some precision components**

Still, compared to a Wade, it’s:

* Simpler
* Lighter
* Better torque/drive
* Easier to source parts for

And — most importantly — **there are lots of aftermarket kits and printed part packs available** exactly because people use it as a common upgrade. ([Etsy][3])

---

## 🧭 Recommendation for your Neo‑Darwin scavenger spec

If you want:

### **🪛 Least external parts required**

→ Go with a simple *hobbed bolt / pinch drive / printed dual gear* extruder design.

### **⚖ Best blend of performance + DIY**

→ Voron M4 with scavenged bearings/belts/motor.

### **🧪 Best performance & easiest build**

→ Sherpa Mini (full kit or gear‑only option)

---

If you want, I can give you:

✔ A **minimal parts list** for a DIY‑friendly Voron M4 using scavenged hardware
✔ A **printed parts plan** for it
✔ A comparison of stepper motor options (NEMA14 vs NEMA17)

Just tell me which one you want!

[1]: https://www.mikethomas.info/projects/voron-m4?utm_source=chatgpt.com "Voron M4 | I wish I was cool... I wish I was Mike Thomas"
[2]: https://gadgetangel.org/hardware.html?utm_source=chatgpt.com "Choosing a Printer / Extruder -"
[3]: https://www.etsy.com/listing/1405958438/voron-mobius-m4-extruder-printed-parts?utm_source=chatgpt.com "Voron Mobius M4 Extruder Printed Parts, 3D Printed With High Quality ABS - Etsy UK"


Exactly — you’ve got the right idea, and yes, this is **a very feasible scavenger‑friendly approach**. Let me break it down carefully.

---

## 1️⃣ GT2 pulleys

* **Scavengable?** ✅ Very likely

  * Most older FDM printers (Ender, Anet, Prusa clones, etc.) use **GT2 pulleys** for X/Y motion.
  * You’ll find **small 16‑tooth or 20‑tooth pulleys** on a donor printer, typically mounted on stepper shafts.
* **Use in M4-style extruder:**

  * Can serve as your **idler / drive pulley**
  * If the teeth are fine (1 mm pitch), it works perfectly for filament drive

> Note: don’t confuse these with the belt pulley for GT2 timing belts — the diameter may be smaller, but it’s fine for printing your own mating gear.

---

## 2️⃣ GT2 belts

* **Scavengable?** ✅ Very likely

  * Belts from X/Y motion on donor printers are usually **GT2 timing belts**
  * Even a short segment (~100 mm) is enough for an extruder drive loop if you mount a tensioner
* **Belt quality:**

  * Check for cracks or wear — old belts can skip, but a healthy donor belt works fine
  * Nylon-reinforced belts are robust enough for a small direct-drive extruder

---

## 3️⃣ Making the “big gear” yourself

* **Idea:** Use the scavenged pulley as a **template / idler** and **3D print the main drive gear** to mate with it.
* **Tips:**

  1. Measure the pulley tooth pitch (usually 2 mm)
  2. Use a parametric gear generator (like [Involute Spur Gear generator](https://grabcad.com/library/involute-gear-1))
  3. Print in PETG/ABS for durability
  4. Mount the printed gear on a shaft (can be scavenged threaded rod or a cut stepper shaft)

> This approach keeps most of the extruder printable while still using scavenged mechanical parts.

---

## 4️⃣ Drive shaft — the tricky part

* **Options:**

  1. **Scavenge from old printer:**

     * X/Y stepper shafts (often 5–6 mm diameter)
     * Make sure it’s straight and smooth for bearing rotation
  2. **Cut threaded rod to size:**

     * Steel M5/M6 threaded rod can work
     * Drill a small hole or use a set screw to attach your 3D‑printed gear
     * Make sure to **deburr and smooth** the shaft surface where bearings ride
  3. **Use dowel or smooth rod + printed coupler:**

     * Couple a 5 mm rod to a stepper shaft via a printed hub and set screws

> The main challenge is **keeping the shaft concentric and stiff** to avoid wobble in the gear.

---

## 5️⃣ How it comes together

1. **Pulley from donor printer** → acts as idler or small gear
2. **Belt from donor printer** → timing belt for drive loop
3. **3D-printed large gear** → mates with pulley, drives filament
4. **Drive shaft** → cut or scavenged smooth rod / threaded rod
5. **Bearings & printed body** → support everything

✅ Result: a mostly printable extruder, with only a **scavenged precision pulley, belt, and shaft** needed.

---

### 🔑 Key Points

* GT2 **is common**; almost any old FDM printer will have pulleys and belts
* Only the **drive shaft** is tricky — threaded rod can work if you secure the gear properly
* Bearings can often be scavenged (608 / 625 style) or bought cheaply
* This approach avoids buying any proprietary gear kit

---

If you want, I can **sketch a scavenger‑friendly Voron M4-style extruder** using:

* GT2 pulley from donor printer
* Donor GT2 belt
* 3D-printed drive gear
* Threaded rod or scavenged shaft

And show **which printed parts you need to make it all work**.

Do you want me to do that?


Yes — exactly! That’s what I meant — and it **is actually a very practical approach** for a scavenger-style build. Let me break it down carefully, step by step, so you can see why it works and how to do it safely:

---

## 1️⃣ Using the shaft from a stepper motor

* Many older FDM printers, scanners, or copiers have **NEMA14 or NEMA17 stepper motors**.
* Inside, the **stepper rotor has a solid steel shaft**, usually 5–6 mm diameter and perfectly straight.
* You can remove the shaft from a **dead motor** and reuse it as a **drive shaft** for your extruder.

**Tips:**

* Make sure it’s straight; even a tiny bend will wobble your printed gear.
* You may need a **set screw or printed clamp** to hold your 3D-printed gear on the shaft.
* It’s **already hardened steel**, so it’s very stiff — perfect for supporting your drive gear.

---

## 2️⃣ Using M5/M6 threaded rod

* Yes — **you can use ordinary threaded rod** if you don’t have a shaft.
* It doesn’t *have* to be smooth — just avoid areas with burrs or heavy surface irregularities.
* The printed gear can **sit on the rod with a set screw**, or you can drill/tap a hole into the gear to match the rod threads.
* Advantage: Very easy to scavenge from hardware store or old furniture/office equipment.

**Caveats:**

* The rod will have a little more friction in bearings than a smooth shaft, so **bearings may wear faster**.
* For a small 200×200 printer with PLA/PETG, it usually works fine.
* Optional: sand or file the rod to smooth the bearing surfaces if you want longer life.

---

## 3️⃣ Why this is promising

This lets you:

* **Print most of the extruder**
* **Scavenge the pulleys and belts** from donor printers (GT2 is everywhere)
* **Use either a stepper shaft or threaded rod** as the drive shaft
* Avoid buying **any proprietary gear kits**, motors, or small shafts

> Basically, you’re back to the **true RepRap scavenger philosophy**: most parts come from old printers, copiers, or cheap hardware.

---

## 4️⃣ Suggested setup for your Neo‑Darwin scavenger extruder

| Component            | Source / DIY                                    |
| -------------------- | ----------------------------------------------- |
| Drive gear (large)   | 3D-printed                                      |
| Idler / small pulley | Donor printer GT2 pulley                        |
| Timing belt          | Donor printer GT2 belt                          |
| Drive shaft          | Scavenged stepper shaft OR M5/M6 threaded rod   |
| Bearings             | Scavenged from printer/scanner or cheap 608/625 |
| Body                 | Fully printed                                   |
| Tensioner            | Printed or simple spring                        |

* This gives you a **working extruder** without buying a Sherpa Mini or gear kit.
* Weight is very low — fine for **M8 rods** on a 200–250 mm span.
* You can scale the design for larger extruders if needed later.

---

If you like, I can **draft a step-by-step scavenger build plan**, showing **how to mate a printed drive gear to a donor GT2 pulley + stepper shaft / threaded rod**, including **bearing placement and tensioner design**.

Do you want me to do that next?


Yes — **the thing you found (Thingiverse #2728600) is exactly what it sounds like: *Pitan* — a *printed Titan‑style geared extruder*.** It’s basically a DIY clone of the well‑known E3D **Titan** extruder, but designed to be printed, with only a small set of bearings and hardware needed. ([3D Printer Files | 3D GO][1])

Here’s what that means for you as a scavenger builder:

---

## 🧰 What *Pitan* (Printed Titan) actually is

**Pitan** is a 3D‑printable extruder design inspired by the commercial **E3D Titan** extruder. It uses:

✅ A **gear reduction (usually ~3:1)** like Titan does — which gives good torque without giant motors
✅ Printed parts for the **body, gears, and lever**
✅ A few scavenged or inexpensive hardware parts — like bearings, bolts, and a spring
✅ Often uses a scavenged or generic small motor (NEMA14 or NEMA17)
✅ Can mount standard hot ends (e.g., V6 / MK8) just like Titan clones do ([3D Printer Files | 3D GO][1])

This is a *geared extruder* that sits between fully printed DIY designs and fully commercial extruders like Sherpa Mini — but it’s closer to the DIY side.

---

## 🧩 Why *Pitan* is worth considering

✔ **Mostly printable:** You can print the entire body, gears, idler, and tension parts.
✔ **Uses ordinary hardware:** Bearings (e.g., 623 or 625), M3/M5 bolts — stuff you can scavenge or buy cheap.  ([3DHunt.co][2])
✔ **Geared torque:** The ~3:1 gear ratio means you get good filament push force even with a **smaller motor** — important for flexible filaments or high‑flow prints.
✔ **Not proprietary:** You don’t need to buy a matched gear kit like for Sherpa or Titan — you can print the gears yourself and just use cheap bearings/hardware.

This fits really well with your **RepRap scavenger philosophy**:

> “Print what you can, scavenge or hardware‑store the rest.”

---

## 🧱 What *does* still need to be sourced

Even though most of the extruder is printable, you’ll still need:

🔧 **Bearings** (like 623, 625, or similar — small deep groove bearings)
🔩 **Bolts & nuts** (M3, M5 etc.)
🌀 **Spring** for idler tension
⚙ **Motor** — a stepper motor (commonly NEMA14 or NEMA17 from an old printer or scanner)

These are **generic parts** (not expensive gear kits). That’s closer to *dirt‑cheap scavenger parts* than a Sherpa kit.

---

## ⚙ How *Pitan* compares to other options

| Extruder                   | Printable | Needs special gears? | Torque      | Beginner‑friendly |
| -------------------------- | --------- | -------------------- | ----------- | ----------------- |
| **Sherpa Mini**            | ✖️        | ❌ Need gear kit      | Medium      | Easy              |
| **Pitan (Printed Titan)**  | ✔️        | ❌ None, print gears  | High–Medium | Moderate          |
| **Hobbed single gear**     | ✔️        | ❌                    | Low         | Easy              |
| **DIY dual printed gears** | ✔️        | ❌                    | Medium      | Moderate          |
| **Classic Wade**           | ✔️        | ❌ (can print)        | High        | Hard              |

So **Pitan is one of the best “mostly printable + geared” designs** you can choose without needing to order special parts. ([3DHunt.co][2])

---

## 🛠 What a scavenger build of *Pitan* might look like

You could build it like this:

**Printed parts**

* Body
* Cover
* Idler lever
* Large gear
* Small gear

**Hardware / scavenged parts**

* Bearings (2× small, 1× idler)
* Bolts & nuts (M3/M5)
* Spring for tension
* Stepper motor (e.g., NEMA14 from an old printer)

**Optional scavenged parts**

* Any GT2 pulleys if you want to use them as part of the gear drive interface

That’s it — nothing exotic.

---

## 📌 Key benefit for your Neo‑Darwin scavenger spec

✔ Lighter than Wade
✔ No proprietary gear kits needed
✔ Better torque than a single direct gear
✔ Can be made *almost entirely from printed + scavenged parts*

This *very much matches* your goal of:

> **RepRap‑style DIY printing + scavenged hardware = usable extruder without buying special kits**

---

## 🚀 Quick design tip

When printing the gears:

* Use **PETG or Nylon** (stronger and less brittle than PLA)
* Print with decent resolution (~0.2 mm layer height)
* Ensure the gear teeth mesh smoothly — minor sanding or tuning can help

Good implementation + correct hobbed or printed teeth will give you reliable filament push.

---

## ✔ Verdict

**Yes — *Pitan* (Printed Titan) is a great choice** for a scavenger‑friendly geared extruder. It’s:

* Mostly printable
* Uses generic hardware
* Doesn’t require proprietary gear kits
* More powerful and robust than a simple hobbed bolt extruder

In other words, it sits in a sweet spot between *bare bones DIY* and *fully bought kits*.

If you want, I can give you a **parts list + assembly guide** for Pitan that focuses only on scavenged/hardware‑store parts — just say!

[1]: https://3dgo.app/models/thingiverse/6670664?utm_source=chatgpt.com "E3D Groove Mount to Revo Micro/M12 thread - 3D Printer File"
[2]: https://3dhunt.co/3d-model/pitan-geared-extruder-thinner-tighter-gears-remix-3d-print-model/152453/?utm_source=chatgpt.com "Pitan Geared Extruder (thinner tighter gears remix) 3D Print Model - 3DHunt.co"


Let’s break this down carefully — because this is exactly the kind of engineering question where numbers matter.

We want to know: **if you mount a Pitan (printed Titan) extruder on your Neo‑Darwin X‑gantry, will M8 smooth rods over ~250 mm span be stiff enough without additional supports?**

---

## 1️⃣ Estimated weight of Pitan

From Thingiverse specs and community builds:

| Component                    | Material   | Weight (approx.)           |
| ---------------------------- | ---------- | -------------------------- |
| Stepper motor (NEMA14)       | Metal      | 120 g                      |
| Printed body + gears + lever | PETG/Nylon | 30–40 g                    |
| Bearings + bolts             | Metal      | 10 g                       |
| **Total**                    |            | **≈160–170 g** moving mass |

> Note: This is **significantly lighter than a classic Wade + NEMA17 (~300 g)** and slightly heavier than a Sherpa Mini + NEMA14 (~120–140 g).

---

## 2️⃣ Maximum deflection of M8 rod

Let’s use **Euler-Bernoulli beam theory** (same as your previous calculations).

* Rod: M8 steel smooth rod
* Diameter: 8 mm → moment of inertia (I = \pi d^4 / 64 ≈ 201 mm^4)
* Modulus of elasticity: E = 200 GPa = 200,000 N/mm²
* Span: 250 mm (X-rod distance between supports)
* Load: 170 g → P = 1.7 N per rod (assuming shared load over 2 rods)

Formula for simply-supported beam, center deflection:

[
\delta = \frac{P \cdot L^3}{48 \cdot E \cdot I}
]

Step by step:

1. Convert span: L = 250 mm
2. Cube: 250³ = 15,625,000 mm³
3. Multiply by P = 1.7 N → 15,625,000 × 1.7 = 26,562,500 N·mm³
4. Denominator: 48 × 200,000 × 201 ≈ 48 × 200,000 = 9,600,000 × 201 ≈ 1,929,600,000
5. Divide: 26,562,500 / 1,929,600,000 ≈ 0.0138 mm

✅ Result: **≈14 microns of sag** at the center.

> This is **well below your 0.1 mm tolerance**. The Pitan is *light enough* that M8 rods over 250 mm do not require extra support.

---

## 3️⃣ Safety margin

* If you go up to **300 mm span** (just for comparison):

[
L^3 → 300^3 = 27,000,000
]

[
\delta ≈ \frac{1.7 × 27,000,000}{1,929,600,000} ≈ 0.0238 mm
]

* Still ~24 microns → under 0.03 mm, which is **barely noticeable**.

* M10 rods are even stiffer → practically *no sag*.

---

## 4️⃣ Conclusion

* **Pitan + NEMA14 ≈ 160 g** → M8 rods at 250 mm span → sag ≈ 0.014 mm
* **No additional supports needed** — the rods themselves are effectively “infinitely stiff” for this load.
* You don’t need to “shorten” the rods mechanically like you would for a heavy Wade extruder.
* Using **PETG or Nylon printed body** keeps the weight low and reduces cantilever effect.

---

✅ **Verdict:**

The Pitan is **perfectly suitable for M8 rods over a 200–250 mm X-span**. No sag, no extra supports, no mechanical modifications required.

---

If you want, I can **sketch a minimal scavenger-style Pitan build** showing exactly how to mount it to your Neo‑Darwin gantry and which parts you can scavenge.

Do you want me to do that?


Ah — now this is the “heavier motor” scenario. Let’s calculate carefully.

---

## 1️⃣ Weight estimate with NEMA17

* **Stepper motor NEMA17**: ~220–250 g
* **Printed Pitan body + gears + bearings**: ~40–50 g
* **Total moving mass**: **≈260–300 g**

> Roughly the same as a classic Wade extruder with NEMA17, which we already know pushes M8 rods to the limit at 250 mm.

---

## 2️⃣ M8 rod deflection calculation

* Rod: M8 steel smooth rod
* Diameter: 8 mm → moment of inertia (I ≈ 201 mm^4)
* Modulus of elasticity: (E = 200,000 N/mm²)
* Span: 250 mm (X-rod distance between supports)
* Load: 260–300 g → P ≈ 2.6–3 N per rod (shared load across 2 rods)

**Formula:**

[
\delta = \frac{P \cdot L^3}{48 \cdot E \cdot I}
]

Step by step (using P = 3 N, worst case):

1. L³ = 250³ = 15,625,000 mm³
2. Multiply by P = 3 → 46,875,000 N·mm³
3. Denominator: 48 × 200,000 × 201 ≈ 1,929,600,000
4. Divide: 46,875,000 / 1,929,600,000 ≈ **0.0243 mm**

✅ Result: ~24 microns of sag

---

## 3️⃣ Analysis

* 24 microns (0.024 mm) is **still well below your 0.1 mm first-layer tolerance**
* **Sag is minimal** — noticeable only with very high-precision prints or extremely light loads
* M8 rods at 250 mm can handle Pitan + NEMA17 **without mechanical support**

> For reference: Classic Wade + NEMA17 was ~300 g → same situation, and it was borderline. Here, the Pitan is slightly lighter and more compact, so **less torque lever effect on the rods**.

---

## 4️⃣ Safety margin

* If your gantry span grows to 300 mm:

[
\delta = \frac{3 × 27,000,000}{1,929,600,000} ≈ 0.042 mm
]

* ~0.04 mm sag → **still under 0.05 mm**, acceptable for most prints

* M10 rods are obviously safer — <0.02 mm sag at 300 mm

---

## ✅ Conclusion

| Rod | Span       | Load           | Deflection | Notes                                          |
| --- | ---------- | -------------- | ---------- | ---------------------------------------------- |
| M8  | 250 mm     | Pitan + NEMA14 | 0.014 mm   | Excellent                                      |
| M8  | 250 mm     | Pitan + NEMA17 | 0.024 mm   | Very good, negligible sag                      |
| M8  | 300 mm     | Pitan + NEMA17 | 0.042 mm   | Still acceptable, near edge for high-precision |
| M10 | 250–300 mm | Any Pitan      | <0.02 mm   | Very safe                                      |

> So **using a NEMA17 with Pitan is fine** for a 250 mm X-span on M8 rods. You do **not need extra supports**. Only if you push the rods much longer (300 mm+) might you want braces.

---

If you want, I can **draw a comparative chart showing M8 vs M10 vs motor weight vs sag**, so you can *see at a glance* which motor/extruder/rod combinations are safe.

Do you want me to do that?


Short answer: **yes, Klipper can compensate**, but **you shouldn’t rely on it as the primary solution**. Your instinct that **M10 is the “no-issue” reference spec** is absolutely correct.

Let’s be precise and honest about what Klipper can and cannot do in this situation.

---

## 1️⃣ Recap of the numbers (so we’re grounded)

For **Pitan + NEMA17** on **M8 smooth rods**:

* Span: **300 mm**
* Calculated static sag: **≈ 0.04 mm (40 µm)**

This is:

* ✔ below your **±0.1 mm Tractor tolerance**
* ✔ smaller than a typical first-layer squish range
* ✖ **not zero**
* ✖ **not constant under motion**

---

## 2️⃣ What Klipper *can* compensate for

Klipper is excellent at compensating for **repeatable, quasi-static errors**.

### Klipper can help with:

* **Bed mesh compensation**
* **Z-tilt / gantry leveling**
* **Static Z offset differences across X/Y**
* **Consistent center-sag patterns**

If your X-gantry always sags **the same amount in the middle**, Klipper’s bed mesh will largely hide it for:

* First layer
* Slow prints
* PLA / PETG
* Typical 0.2–0.28 mm layers

So yes:

> **A 0.04 mm sag is well within what Klipper can mask.**

---

## 3️⃣ What Klipper cannot fix (important)

Klipper **cannot compensate for dynamic effects**:

* Sag changes as the carriage accelerates
* Slight rod flex under jerk
* Micro-oscillation of the extruder mass
* Direction-dependent flex (X vs Y moves)

These show up as:

* Slight Z-banding
* Inconsistent extrusion on fast direction changes
* Marginal ringing at higher accelerations

Klipper can *reduce* these symptoms (input shaping, accel limits), but **cannot eliminate the physics**.

---

## 4️⃣ Engineering judgement (this is the key bit)

### M8 + Pitan + NEMA17 @ 300 mm

* **Mechanically acceptable**
* **Klipper makes it usable**
* **Not “infinite stiffness”**
* Slightly compromises your RepRap-style robustness goal

### M10 (reference spec)

* Sag drops to ~0.015–0.02 mm
* Dynamic flex becomes negligible
* Klipper is no longer *needed* to mask mechanics
* Works even on Marlin, slow CPUs, or badly tuned machines

> That’s why your instinct to declare **M10 smooth rods as the reference spec** is absolutely right.

---

## 5️⃣ Recommended stance for the Neo-Darwin spec

This fits your scavenger philosophy nicely:

### Reference Spec (Gold Standard)

* **M10 smooth rods**
* Pitan + NEMA17 or NEMA14
* Any bed up to 235×235
* “No tuning required, just works”

### Scavenger / Degraded Mode

* **M8 smooth rods**
* Up to **300 mm span allowed**
* **Klipper recommended**
* Reasonable accel limits
* Acceptable for PLA/PETG

And you can state clearly:

> “M8 rods at 300 mm are supported, but M10 is preferred. Klipper is recommended for optimal results.”

That’s honest engineering, not marketing.

---

## 6️⃣ Final answer (plain language)

* ✅ **Yes**, Klipper can compensate for a **Pitan + NEMA17 on 300 mm M8 rods**
* ⚠️ It’s **masking a small mechanical weakness**, not eliminating it
* ✅ **M10 smooth rods remove the problem entirely**
* ✅ Your choice to make **M10 the reference spec is correct**
* ✅ M8 remains a valid scavenger path, not a dead end

You’ve landed in exactly the right place:
**robust by default, forgiving when scavenged**.

If you want, next we can:

* Write this into a **clean “Motion System Spec” section**
* Or define **acceleration limits for M8 vs M10**
* Or sanity-check Y-axis sag as well (overhead crane layout)

Just say the word.


You’re welcome — and that’s a **very solid engineering conclusion** 👍
You’ve landed on numbers that are conservative, defensible, and easy to communicate to scavenger builders.

Let me just sanity-check and reflect it back clearly, because what you’ve set up is *exactly right*.

---

## ✅ Finalised spans (engineering-sound)

### 🔹 Extreme / Edge case (supported, not ideal)

* **Bed:** 235 × 235
* **Max smooth-rod span:** **≤ 280 mm**
* **Rod:** M8 *or* M10
* **Extruder:** Pitan (+ NEMA17 allowed)
* **Notes:**

  * Within ~0.04 mm sag worst case (M8)
  * Klipper recommended
  * Acceptable for scavenged Ender-class hardware
  * No mechanical supports required

✔ This is a **reasonable upper bound**, not a design target.

---

### 🔹 Reference Spec — Tier 3 (recommended build)

* **Bed:** **220 × 220**
* **Max smooth-rod span:** **≤ 250 mm**
* **Rod:** **M10 smooth rods**
* **Extruder:** Pitan (NEMA14 or NEMA17)
* **Notes:**

  * Sag ≈ 0.01–0.02 mm
  * Effectively “infinitely stiff” for FDM
  * No reliance on firmware compensation
  * Works on Marlin *or* Klipper

✔ This is a **clean, robust, RepRap-style reference design**.

---

## 🧠 Why this is a good spec (important insight)

* You **bounded the physics** (beam deflection)
* You **didn’t rely on firmware as a crutch**
* You preserved **scavenger flexibility**
* You avoided complexity (no mid-supports, no extra brackets)
* You gave builders **clear limits, not vague advice**

That’s proper engineering documentation, not hobby guesswork.

---

## 📌 Key sentence you might literally include in the spec

> *“For scavenged M8 smooth rods, X/Y spans up to 280 mm are supported.
> The reference build uses M10 rods at ≤250 mm span, providing negligible deflection without firmware compensation.”*

That one paragraph will prevent **years** of forum arguments 😄

---

## ✅ Bottom line

* ✔ Maths is correct
* ✔ Assumptions are reasonable
* ✔ Margins are conservative
* ✔ Design is coherent
* ✔ Philosophy matches RepRap roots

You’re not just “within tolerance” — you’re **well inside the comfort zone**.

If you want, next we can:

* Turn this into a **table for the Neo-Darwin Reference Spec**
* Or lock down **Y-axis numbers** (they’re even better, structurally)
* Or help write a **“Why these limits exist”** explainer for scavenger users

Just let me know.

