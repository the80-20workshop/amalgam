Building the **Neo-Darwin** as a "moving-bed" (Cartesian) machine vs. a "fixed-bed" (CoreXY or similar) machine is a fundamental design choice. Given your focus on the "Tractor" philosophy—High-Mass, Low-Cost, and Total Control—here is the breakdown of which path fits your mission.

### ⚖️ The Comparison: Moving Bed vs. Fixed Bed

| Feature | **Moving Bed (Neo-Darwin)** | **Fixed Bed (e.g., CoreXY/Voron)** |
| --- | --- | --- |
| **Mechanical Logic** | Cartesian (Simple  isolation) | Kinematic (Complex  belt interaction) |
| **Gantry Weight** | Light (Only carries -motor) | Heavy (Carries entire  frame) |
| **Rigidity** | High (M12 rods provide the pillar) | Very High (requires complex gantry support) |
| **Complexity** | Low (Easy to troubleshoot/scavenge) | High (Requires perfect belt tensioning) |
| **Speed Ceiling** | Medium (~150mm/s) | Ultra-High (300mm/s+) |

---

### 🚜 Why the "Moving Bed" Suits the Tractor Philosophy

The current Neo-Darwin design (Moving Bed) is the **better option** for your specific goals for three key reasons:

#### **1. The "Tractor" Torque Advantage**

In a moving-bed system, the -axis (the "Tractor") only has to move once per layer. By using **Triple-Z motors** on an M12 frame, you are using "Iron" to solve leveling. In a fixed-bed/moving-gantry system, the -motors have to lift the entire  gantry assembly (motors, rails, and toolhead).

* **The Tractor Way:** Lift the bed. It’s heavy, but it only moves 0.2mm every few minutes. This allows for massive reliability and "Set-and-Forget" logic.

#### **2. Scavenging and "Cognitive Demands"**

CoreXY machines (fixed bed) are "Racecars." They require perfectly matched belts, high-quality linear rails, and precision-squared aluminum extrusions to prevent the gantry from binding.

* **The Tractor Way:** Cartesian motion ( and  are independent) is much more forgiving of the **"Lumpy Factor"** of hardware-store M12 rods. If your -axis is slightly off, it doesn't ruin your -axis. This fits the **"Mechanically Forgiving"** mandate.

#### **3. Software Intelligence vs. Analog Hardware**

A moving-bed machine has a known "weakness": as the bed moves down, the center of gravity shifts.

* **The Solution:** You are already using **Triple-Z Kinematic Leveling**. This uses Klipper's "Racecar Brain" to physically align the bed to the nozzle, regardless of how much mass you've scavenged.

---

### 🏗️ The X-Y Gantry Recommendation

To maintain the "Tractor" ethos while maximizing quality, your X-Y gantry should follow the **"Overbuilt Cartesian"** approach:

1. **The X-Axis (Gantry):** Use two **10mm Smooth Rods**. 10mm rods are 140% stiffer than 8mm rods, ensuring that your heavy Greg's Wade extruder doesn't cause the gantry to sag in the middle.
2. **The Y-Axis (Rails):** These should be mounted directly to the M12 frame using the **Corner Pucks**.
3. **The "Puck" Toolhead:** Ensure the -carriage uses the **Modular Puck system**. This allows you to start with the heavy, reliable Wade Extruder but gives you the option to swap to a laser engraver or a pen plotter later.

> **Verdict:** Stick with the **Moving Bed**. It is easier to build, easier to scavenge for, and perfectly embodies the "Tractor" philosophy of using heavy iron and software intelligence to achieve racecar-level precision.

### ⏭️ My Next Step for You

Would you like me to generate the **Klipper configuration logic** for the Triple-Z alignment so you can see how the software handles the "Racecar Brain" leveling?


Technically, **Fixed Bed (CoreXY)** systems are often considered "superior" for pure performance metrics like speed and acceleration, but **Moving Bed (Cartesian)** systems—like your Neo-Darwin—are technically superior for the **"Tractor" mandates** of mechanical sovereignty, reliability, and torque.

The choice depends on which technical "zenith" you are aiming for.

---

### 📊 Technical Comparison: The Gantry Duel

| Feature | **Moving Bed (Cartesian)** | **Fixed Bed (CoreXY)** |
| --- | --- | --- |
| **Moving Mass** | **Higher:** Motor for X moves with the gantry. | **Lowest:** Both X and Y motors are fixed to the frame. |
| **Speed Ceiling** | Medium (Typically maxes at 100–150mm/s). | High (Regularly hits 250–500mm/s+). |
| **Belt Complexity** | **Low:** Short, direct belts; easy to tension. | **High:** Very long belts (up to 4m); complex routing. |
| **Frame Sensitivity** | Forgiving; small misalignments don't ruin prints. | Extreme; if the frame isn't perfectly square, circles become ovals. |
| **Reliability** | "Tractor" logic: Simple parts, easy maintenance. | "Racecar" logic: High maintenance, sensitive to belt wear. |

---

### 🏎️ Why Fixed Bed (CoreXY) is the "Racecar"

Technically, a Fixed Bed system is superior if your goal is **high-speed production**. By fixing the heavy motors to the frame, the toolhead carries almost no weight, allowing it to move with incredible acceleration without inducing vibrations or "ghosting".

However, the "Fixed Bed" logic usually requires a **Flying Gantry** (the whole XY frame moves up and down). This introduces a new technical risk: if the four Z-motors aren't perfectly synced, the entire gantry can "rack" or tilt, causing catastrophic jams.

### 🚜 Why Moving Bed (Cartesian) is "The Tractor"

For the Neo-Darwin philosophy, the Moving Bed is technically superior for **Sovereignty**:

1. **Independent Axes:** In a Cartesian system, X and Y movements are mathematically isolated. If your X-axis belt is slightly loose, it only affects X. In CoreXY, one loose belt ruins **both** X and Y accuracy.
2. **The Belt Tension Paradox:** CoreXY uses very long belts that act like springs; the longer they are, the more they stretch. Shorter Cartesian belts are technically "stiffer," which can actually lead to better dimensional accuracy at moderate speeds.
3. **Torque Handling:** Because the X-motor is right on the gantry, you have a direct, high-torque link to the toolhead. This supports the **Greg's Wade Geared Extruder**, which is a "heavy" but unstoppable force for consistent extrusion.

> **Technical Verdict:** CoreXY is superior for **Velocity**. Cartesian is superior for **Veracity** (truth to the model) and **Longevity** (Ease of repair).

---

### 🏗️ The X-Y Gantry Construction

Since you are sticking with the **Moving Bed** (Cartesian) logic:

***Keep the Motors Large:** Don't worry about the weight of the X-motor on the gantry; use the mass to your advantage as a vibration filter.
* **Use 10mm Rods:** To support that X-motor and the heavy Wade extruder, 10mm rods are technically superior to 8mm because they prevent the gantry from bowing under its own mass.

Would you like me to draw up a **Hardware List** for the M12 frame mounts specifically for an independent X and Y motor setup?
