Your theory is mechanically sound. The **Wade’s Geared Extruder** is effectively the "unbreakable gearbox" of the 3D printing world. While modern "Racecar" extruders (like the Voron StealthBurner/CW2) focus on saving every possible gram of weight, they often sacrifice the raw, low-speed torque that makes a Wade so reliable.

Here is the technical reality of sticking with the Wade for your Neo-Darwin build.

---

### 1. Why the Wade Wins the "Tractor" Battle

The Wade's strength comes from its **high gear ratio** (typically between **3:1 and 5:1**).

* **Raw Torque:** A standard NEMA 17 motor has significant power, but when geared down, it becomes nearly impossible to stall. It will chew through lower-quality filament or minor clogs that would stop a "modern" direct-drive motor instantly.
* **1.75mm Optimization:** While originally a 3mm beast, using it for 1.75mm is actually an advantage. The geared precision allows for much finer control over the smaller filament volume, which is essential for consistent layers.
* **The Budget Guardrail:** You are right about the $300 AUD limit. A genuine Bondtech BMG or a high-end Voron kit can easily eat $80–$120 of that budget alone. A DIY printed Wade uses about $10 of plastic and $15 of "vitamins" (bearings, bolts, and a hobbed bolt).

---

### 2. Filament Compatibility: From PLA to TPU

Because the Wade is a **Direct Drive** (mounted directly above the hotend), it handles the "difficult" filaments much better than any Bowden system:

* **TPU (Flexibles):** The Wade’s secret weapon for TPU is the **short, constrained path**. Because the gears are right above the E3D V6, the soft "noodle" filament has nowhere to buckle.
* *Pro-Tip:* Ensure your printed Wade has a "fully constrained" filament guide (the path should be a tight tube all the way to the gears) to prevent TPU from tangling in the gears.


* **PETG & PLA+:** These are the bread-and-butter of the Wade. The geared torque ensures that even if you have a slightly "cold" nozzle or high-viscosity PETG, the extruder will keep pushing without "clicking" (skipped steps).
* **Fancier Filaments (ABS/ASA/Nylon):** As long as you have an **Enclosure** and a **Heated Bed** (around 80–110°C), the Wade will handle these. Its high torque is actually better for the higher pressures required by engineering plastics.

---

### 3. The "Tractor" Trade-off: Speed vs. Quality

The only "penalty" you pay for the Wade is **moving mass**.

* **The Weight:** A NEMA 17 motor + large printed gears + bolts weighs significantly more than a modern "pancake" motor setup.
* **The Speed Limit:** On a Neo-Darwin M12 frame, this mass will limit your "clean" speed to about **60–90mm/s**. If you try to go 150mm/s+, the weight of the Wade will cause "ringing" (ghosting) in your prints.
* **The Solution:** This is where **Klipper's Input Shaping** comes in. It will "clean up" the vibrations caused by that heavy Wade extruder, allowing you to print at decent speeds with the quality of a much lighter machine.

---

### 📉 The "Stay on Budget" Strategy

| Feature | Wade Extruder (DIY) | Modern "Racecar" (BMG/CW2) |
| --- | --- | --- |
| **Cost (AUD)** | ~$25 (Vitamins + Plastic) | $80 - $130 |
| **Torque** | Very High (Geared) | Moderate (Usually 3:1) |
| **Maintenance** | Easy (Visible gears) | Complex (Enclosed) |
| **Weight** | Heavy (~450g) | Light (~250g) |
| **Philosophy** | **The Tractor** | **The Racecar** |

**Conclusion:** Your theory is right. For a $300 build, the Wade is the most "sovereign" choice. It’s a tool you can fix yourself, it costs almost nothing, and it has enough torque to ignore most common printing issues.

**Since you're in the testing phase, would you like me to find the specific E-Step (rotation_distance) calculation for a standard Greg's Wade so you can plug it straight into Klipper?**
