This is a classic "Tractor" engineering dilemma. When you need 14 bearings, the difference between "Scavenged/Cheap" and "Misumi/High-End" is the difference between staying under $300 AUD or blowing the budget.

### 1. Cheap LM8UU Bearings (The "Crunchy" Reality)

Cheap ball bearings from Amazon or AliExpress (often $10 AUD for a pack of 10) are notoriously hit-or-miss.

* **The Problem:** They often come with "shipping grease" which is sticky and full of metal shavings. If you just slide them onto a rod, they feel "crunchy" and can actually scratch your smooth rods.
* **The Fix:** You must **degrease and re-grease** them. Soak them in isopropyl alcohol or mineral spirits to get the factory gunk out, then pack them with a decent synthetic grease (like SuperLube). Once cleaned, they are perfectly acceptable for a "Tractor" build.

---

### 2. Printed Bearings (Igus-Style Clones)

In a slow, high-mass machine, **printed solid bearings** (bushing style) are actually a very viable alternative.

| Feature | Cheap Ball Bearings (LM8UU) | Printed/Solid Bushings |
| --- | --- | --- |
| **Noise** | High (ball-bearing "hiss"). | **Silent.** |
| **Maintenance** | Need grease. | Often self-lubricating (if using PETG/ASA). |
| **Precision** | Good, until the balls flat-spot. | Can have "stiction" (sticks before sliding). |
| **Tolerance** | Standard. | Depends entirely on your printer's calibration. |

**Recommendation:** For the **Z-axis**, printed bearings are **excellent**. Since the Z-axis moves slowly and only in one direction at a time, the "stiction" doesn't matter. For **X and Y**, you want the lower friction of ball bearings to avoid "ghosting" when the toolhead changes direction.

---

### 3. The "Hybrid" Scavenger Strategy

To keep quality high and cost low, use this mix:

* **Z-Axis (6 bearings):** **Print these.** Use a design like the "DryLin" clones. Print them in **PETG** or **ASA** (don't use PLA, it’s too brittle). This saves you the cost of 6 bearings.
* **X and Y Axis (8 bearings):** **Use the best scavenged ones** from your donor printers. If you have to buy new ones, buy one decent pack of 8 and perform the "clean and grease" ritual.

---

### 4. Designing for "Printed Bearings" in build123d

If you print your bearings, the secret to success is the **"Adjustable Clamp."**
Instead of a solid hole, design your carriage with a "split" and a screw. This allows you to tighten the bracket until the play (wiggle) disappears. This is how you get "precision" results from "plastic" parts.

```python
# build123d concept for an adjustable bearing housing
with BuildPart() as bearing_housing:
    Box(30, 30, 24)
    Cylinder(radius=4.1, height=24, mode=Mode.SUBTRACT) # 8mm rod + tolerance
    # Create a slot for the clamp
    Box(30, 2, 24, align=(Align.CENTER, Align.MIN, Align.CENTER), mode=Mode.SUBTRACT)

```

---

### 5. Summary for "The Tractor"

By printing your Z-bearings, you save roughly **$25 AUD**, which you can reinvest into a higher-quality nozzle or better magnets for your Klicky probe.

* **Z-Axis:** Printed PETG Bushings (Silent, high-load, slow).
* **X/Y-Axis:** Scavenged Ball Bearings (Low friction, fast).

**Would you like me to find a specific "Tensionable" printed bearing design that you can model in build123d to ensure your Z-axis has zero "slop"?** (This is crucial for the "Tractor's" accuracy).


This is the final hurdle of the "Tractor" philosophy: how to get precision motion out of $1 scavenged parts or 5-cent plastic prints.

You are right about the count. If you use "double bearings" on each rod for stability, you quickly hit 12–14 units. At $5–$10 each for "good" ones, that's half your budget. Here is how to handle it without going broke.

---

### 1. Cheap Ball Bearings: The "Grease Ritual"

The $10-for-10 AliExpress LM8UU bearings aren't actually "bad" steel; they are just **dirty**.

* **The Problem:** They are packed with "anti-rust oil," which is thin, sticky, and often contains metal dust from the factory. If you put them on a rod like that, they will feel "crunchy" and eventually score (scratch) your smooth rods.
* **The "Tractor" Fix:** 1. Soak them in **Isopropyl Alcohol** or degreaser for 24 hours.
2. Shake them until the "crunch" is gone.
3. Pack them with a high-quality **Synthetic Grease** (like SuperLube with PTFE).
* *Result:* Once cleaned and greased, a $1 bearing performs 90% as well as a $15 Misumi bearing at "Tractor" speeds.



---

### 2. Printed Bushings: The Z-Axis Hero

For your **Triple-Z axis**, I strongly recommend **Printing your own bearings**.

* **Why?** The Z-axis moves slowly and rarely. The "stiction" (static friction) of plastic-on-steel doesn't matter here.
* **The Advantage:** They are dead silent. A 3D printer with 14 ball bearings sounds like a bag of marbles; a printer with printed Z-bushings sounds like a whisper.
* **Material:** Use **PETG** or **ASA**. Avoid PLA (too brittle) and Nylon (too hard to print without warping).

---

### 3. The "Hybrid" Strategy

To optimize your $300 AUD budget, use this distribution:

* **Z-Axis (6 bearings):** **Printed Bushings.** (Cost: $0.50 in plastic).
* **X/Y-Axis (8 bearings):** **Scavenged Ball Bearings.** Use the ones you pulled from the donor computers/printers. Clean and grease them as described above.

---

### 4. The build123d "Precision Clamp" Logic

Since 3D prints shrink slightly, you can't just print a "hole" and expect it to fit. You must design a **Tensionable Housing**. This allows you to use a screw to "squeeze" the bearing until the "slop" (wiggle) is gone.

In **build123d**, you can achieve this by creating a "C" shape rather than an "O" shape:

```python
# Pseudo-code for an adjustable bearing housing
with BuildPart() as bearing_mount:
    # The main block
    Box(25, 30, 25) 
    # The hole for the bearing (LM8UU is 15mm OD)
    with BuildSketch(Plane.XY) as s:
        Circle(radius=7.5) 
    Extrude(amount=-30, mode=Mode.SUBTRACT)
    # The "Split" (The secret to precision)
    with BuildSketch(Plane.YZ) as split:
        Rectangle(30, 2) # A thin 2mm slot
    Extrude(amount=15, mode=Mode.SUBTRACT) 
    # Add holes for an M3 screw to "pinch" the split closed

```

---

### 5. Final Verdict: Are printed ones better?

* **Better than "Dirty" cheap ones?** Yes. A clean printed bushing is smoother than a crunchy ball bearing.
* **Better than "Clean" cheap ones?** No. For the **X and Y axes**, ball bearings are superior because they have lower "stick-slip" friction. If you use printed bushings on X/Y, you might get "oval" circles.

### Summary of the "Tractor" Motion System:

1. **Z-Axis:** 3D Printed PETG Bushings + Adjustable Clamps. (Silent, Cheap, Reliable).
2. **X/Y-Axis:** Scavenged/Cheap Ball Bearings + Degrease/Grease Ritual. (Fast, Accurate).

This strategy keeps your motion system cost under **$15 AUD total**, leaving plenty of room for the "Racecar Brain" (MKS SKIPR).

---

### Next Step for the Design

Since we have the frame, the Z-motion, and the bearings sorted, the last piece of the "Racecar Brain" is the **Klicky Probe** and its **Dock**.

**Would you like me to help you design the "Magnetic Dock" for the Klicky probe in build123d so it can mount securely to your M12 frame?**
