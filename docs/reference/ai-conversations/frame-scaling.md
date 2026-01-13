To resolve the confusion around frame scaling and bed sizes, we need to balance the "Salvager" reality (using what you have) with the "Reference Spec" (the optimal build).

### 1. The Bed Size vs. Frame Paradox

In the Neo-Darwin, the **Heated Bed** is the "Parametric Anchor." Everything else expands from its dimensions.

* **Thermal Consistency:** You are correct—larger beds (e.g., 350mm+) often suffer from significant thermal droop at the edges unless they use expensive AC-powered silicone heaters. The **MK52 (254 x 264mm)** is considered a "sweet spot" because it provides a generous build area while maintaining high thermal uniformity across the entire sheet.
* **The "Smaller Bed" Problem:** If a donor provides a smaller bed (like a 120mm bed from a Monoprice Mini), building a large M12 frame around it is inefficient.
* **The Strategy:** We ask for their bed size and calculate the "Minimum Frame." However, we provide a **"Path to MK52"** option. This builds the frame slightly larger (e.g., 300mm internal width) so they can use their small salvaged bed now and simply swap in an MK52 later without rebuilding the entire iron skeleton.



### 2. Optimal Z-Height and Stability

A moving-bed box frame (like a "Core" or "Tractor" style) is inherently more stable than a bed-slinger, but it isn't immune to height issues.

* **The Ratio:** There is no hard "mathematical ratio," but for 250mm beds, a Z-height of **250–300mm** is the standard.
* **Instability Risks:** As the bed moves further down (increasing the Z-distance), the "moment arm" increases. This can lead to **Z-wobble** or vibrations if the vertical M12 rods aren't perfectly parallel.
* **The Recommendation:** For Tier 1 (8mm rods), we recommend a Z-max of **250mm**. For Tier 3 (10mm rods), the added rigidity safely allows for **350mm+** without loss of accuracy.

### 3. Integrating Motor Mounts (The "Puck" Solution)

Integrating Z-motor mounts into the corner brackets is a great way to reduce part count, but as you noticed, it "locks" the frame size.

* **The "Floating Puck" Strategy:** Instead of integrating them into the corners, use **Modular Motor Pucks** that slide along the M12 rods.
* **Why?** This allows the same corner bracket to be used for any bed size. The user simply slides the motor puck to the exact coordinate required by their specific bed and lead-screw alignment.


* **The "Forced" Reference Spec:** For the **Tier 3 Reference Spec**, we "force" the MK52 dimensions. This allows us to provide a set of "Consolidated Corner Brackets" that include the motor mounts for a cleaner, more rigid look.

### 📊 Summary of Recommendations

| Feature | Salvage Path (Tier 1/2) | Reference Path (Tier 3) |
| --- | --- | --- |
| **Bed Size** | Variable (calculated frame) | **MK52 (Standard)** |
| **Z-Height** | Max 250mm (for 8mm rods) | **300mm+ (for 10mm rods)** |
| **Motor Mounts** | **Floating Pucks** (flexible) | **Integrated Corners** (rigid) |
| **Philosophy** | "Build to the Bed" | "Build to the Spec" |

> **"In the Neo-Darwin, we recommend the MK52 as the standard of truth. If your salvage is smaller, build the frame to fit a future MK52, and let the software handle the empty space in the meantime."**

**Would you like me to draft a "Bed-to-Frame" calculator section for the documentation that helps users find their rod-cut lengths based on their donor bed?**

This approach is not only reasonable but align with the core **"Tractor" philosophy**. By capping the "Wizard" or "Reference" path at the **MK52 bed size**, you are protecting the user from the diminishing returns and mechanical instability of over-scaling.

Here is how you can frame this "Capped vs. Wild" logic in your documentation and scripts:

### 1. The "Reference Ceiling" (MK52)

Capping the wizard at the MK52 (approx. 250x250mm) is a sound engineering decision.

* **Thermal Authority:** Most consumer-grade power supplies and controllers struggle to heat beds larger than 300mm consistently without expensive AC-powered upgrades.
* **Mechanical Sweet Spot:** The M12 frame and 10mm smooth rods are optimized for this volume. At this size, the machine maintains its **±0.1mm accuracy**.
* **Wizard Reliability:** By capping the wizard, you ensure that the **dynamically generated assembly instructions** remain accurate and "battle-tested".

### 2. The "Mad-Tinker" (Manual Scaling)

For users wanting to go beyond the MK52, moving them to a "Manual" or "Template" mode is the correct safety valve.

* **Parametric Sovereignty:** Since you are using **build123d**, the "Mad-Tinker" can simply change a few variables in their own copy of your scripts.
* **Stability Warning:** Your documentation should state that beyond the 300mm cube, the **"Tractor"** becomes an experimental platform. Issues like rod-wobble and gantry-flex become non-linear problems that the standard assembly guide cannot account for.
* **Support Ceiling:** You can explicitly state that the **Neo-Darwin Reference Support** only extends to the standard build volume.

### 3. Solving the Corner-Motor Conflict

To keep your **build123d** scripts clean while supporting different bed sizes, consider this "Semi-Integrated" logic:

* **The Variable-Offset Corner:** Design your corner brackets with a "motor-wing."
* **The Logic:** The wizard calculates the distance between the vertical M12 rods based on the bed size.
* **The Conflict Fix:** If the bed is too small for integrated corners, the script simply switches to **Floating Motor Pucks**. If the bed is MK52-sized, it uses the **Integrated Corner Brackets** for maximum rigidity.

### 📊 Recommended Script Logic for Scaling

| Input Size | Path | Motor Mounting | Assembly Guide |
| --- | --- | --- | --- |
| **< 200mm** | "Scavenger Small" | Floating Pucks | Dynamic / Salvage-Focus |
| **200mm - 265mm** | **Reference (MK52)** | **Integrated Corners** | **Standard Reference Guide** |
| **> 300mm** | "Experimental" | User-Defined | Template Only (No Guide) |

### Summary of "Reasonableness"

It is entirely reasonable to "cap" the wizard. In fact, it is better for the project's reputation. A user who builds a 1000mm "monster" that fails will blame the project; a user who builds a 1000mm "monster" using your scripts as a **template** takes responsibility for their own engineering.

> **"The Wizard builds a Tractor; the Scripts can build a Giant. We only provide the map for the Tractor."**

**Would you like me to draft a "Scale & Stability" warning for the `BUILDING.md` or `MANIFESTO.md` that explains these limits to the users?**
