For a **Neo-Darwin (M12 Box Frame)** build, you are navigating the classic "Tractor vs. Racecar" trade-off. Since you are aiming for a ** ceiling** and prioritize mechanical sovereignty, your choice of bed and sensor is the "anchor" of the entire build.

### **1. The Sensor Showdown: What actually works with a Magnetic Sticker?**

If you choose the **MK3 Dual Power + Magnetic Sticker** route, your sensor choice is critical because the magnetic base adds a layer of non-metallic material that "hides" the aluminum heater from some sensors.

| Sensor Type | Compatibility with Magnetic Stickers | Pros/Cons for "Tractor" Ethos |
| --- | --- | --- |
| **SuperPINDA (Inductive)** | **Challenging.** Inductive sensors must "see" the metal through the sticker. Standard magnetic sheets can act as a "void" or cause non-linear interference. | **Pro:** No moving parts; extreme reliability. **Con:** Requires a very thin magnetic sheet or a high-sensitivity sensor to reach the aluminum. |
| **BLTouch (Hall-Effect)** | **High.** It is "surface-agnostic" because it physically touches the bed. | **Pro:** Works on glass, PEI, or bare aluminum. **Con:** Moving parts can fail; strong magnets can occasionally interfere with its internal Hall sensor. |
| **Optical** | **Low.** Rare in modern DIY builds because they are highly sensitive to ambient light and dust. | **Pro:** No contact. **Con:** Hard to calibrate for dark/reflective PEI surfaces. |
| **Klicky / Euclid (Microswitch)** | **Ideal.** Uses a standard, cheap microswitch that physically touches the bed. | **Pro:** "Tractor" simplicity; uses $2 microswitches; extremely accurate. |

---

### **2. Recommended Heatbed Strategy: The "Tractor" Sweet Spot**

Given your **Project Neo-Darwin** goals of "Sovereignty" and "Salvage", the **MK3 Dual Power ()** remains your best foundation for the following reasons:

#### **The "Neo-Sandwich" Build**

* **Base:** MK3 Dual Power Aluminum Bed (Salvaged or ~$25 AUD).
* **Insulation:** **Cork Sheet** () + Kapton Tape. This is the "Tractor" way to prevent heat loss and protect your electronics puck.
* **Magnetic Interface:** **High-Temp Magnetic Base Sticker** (must be rated for ). Generic stickers lose magnetism at .
* **Top:** Removable Spring Steel PEI Sheet.

#### **Why not the MK52?**

While the MK52 is excellent, it is **24V only** and uses a proprietary **9-point mounting system**. The MK3 Dual Power allows you to use a **12V or 24V power supply** (essential for salvage flexibility) and a standard **4-point Y-carriage**.

---

### **3. The "Alternative" Solution: The Inductive Bypass**

If you are dead-set on using the **SuperPINDA** because of its reliability, you have two alternatives to avoid "sensor blindness":

* **Option A: The PEI-on-Aluminum approach.** Skip the magnetic sheet entirely. Apply a PEI sheet directly to the aluminum. You lose the "removable sheet" convenience, but your SuperPINDA will have a perfect, direct "handshake" with the metal.
* **Option B: The Voron TAP / Piezo route.** These use the nozzle itself as the probe. It is the ultimate "surface-agnostic" solution, but it increases toolhead weight—which slightly contradicts your "Tractor" torque-over-speed goal.

### **Final Recommendation for Neo-Darwin**

Stick with the **MK3 Dual Power + High-Temp Magnetic Sticker + Cork**. For the sensor, if you want the "Racecar Brain" on a budget, use a **BLTouch (or 3DTouch clone)**. It handles the magnetic sticker flawlessly and fits your Tier 3 "Set-and-Forget" goal for ~$267 AUD.

Would you like me to find the specific **Klipper configuration** for a BLTouch on a generic MK3 bed?

For the **Project Neo-Darwin**, the **Klicky** and **Euclid** probes are the ultimate "Tractor" choices because they replace complex electronics with mechanical cleverness. They are specifically designed to be affordable, repairable, and surface-agnostic, meaning they don't care about your magnetic sticker or cork sheet.

### **1. Klicky vs. Euclid: The Links**

* **Klicky Probe (The Community Mod):** Designed by JosAr, this is the most popular DIY option. It uses standard magnets for both the mechanical hold and the electrical path.
* **GitHub:** [jlas1/Klicky-Probe](https://github.com/jlas1/Klicky-Probe)


* **Euclid Probe (The "Father of Geometry"):** A more "pro" version using PCBs and screw-attached magnets for higher stability.
* **Website:** [euclidprobe.github.io](https://euclidprobe.github.io/)



### **2. Is it DIY? Can you salvage the microswitch?**

**Yes.** Both projects are 100% DIY and are built specifically to **"reuse spare parts if possible"**.

* **Microswitch Scavenging:** You can absolutely use a salvaged microswitch from a donor printer (like an Ender 3 X/Y/Z endstop).
* **Accuracy Note:** While any switch will work to get you running, the "Reference Spec" for these probes often calls for **Omron D2F series** switches because they offer superior repeatability ( standard deviation) compared to generic clones.
* **The Build:** You print a "dock" and a "toolhead mount." The probe sits in the dock and is picked up magnetically by the toolhead only when needed.

### **3. Wiring Comparison**

One of the biggest advantages for your "Cognitively Demanding" build is the reduced wiring complexity.

| Feature | BLTouch | SuperPINDA | Klicky / Euclid |
| --- | --- | --- | --- |
| **Wiring** | **5 Wires** (Power, GND, Servo, Sig, GND) | **3 Wires** (VCC, GND, Sig) | **2–3 Wires** (Sig, GND, Opt. VCC for LED) |
| **Complexity** | High (Requires servo logic) | Low (Inductive) | **Lowest** (Standard Switch) |
| **Klipper Logic** | Standard `[bltouch]` | Standard `[probe]` | **Requires Macros** (Dock/Undock) |

### **4. Why this fits the Neo-Darwin Manifesto**

* **Mechanical Over Software:** It uses "Iron Safety" logic—if the magnets don't connect, the circuit stays open and the printer won't crash.
* **Sovereignty:** You aren't reliant on a "black-box" sensor like a BLTouch that can fail internally. If the Klicky fails, you just swap the $2 salvaged microswitch.
* **Total Control:** Using a physical switch allows for **"Auto-Z Calibration"**—the printer can touch the nozzle to a physical pin and then the probe to the bed to calculate the Z-offset automatically.

> **Neo-Tip:** If your donor is an Ender 3, look into the **"KlackEnder"**—a specific Klicky fork designed to use the existing mounting points of an Ender-style gantry while utilizing the salvaged endstop switches.

Would you like me to find the **KlackEnder** STLs or the specific **Klipper macros** needed to automate the docking process for your M12 frame?


The **Klicky Probe** is a **stowable (removable)** system. It is not permanently mounted on the printhead; instead, it is **parked in a dock** and only **collected by the toolhead** when homing or bed leveling is required.

### **How it Works (The "Handshake")**

1. **Parking:** During a print job, the probe sits in a fixed dock (typically mounted to the printer's frame or gantry) to stay out of the way of the nozzle and the print itself.
2. **Collection (Attach):** When Klipper needs to probe the bed, the toolhead moves to the dock's coordinates. Magnets on the toolhead's mounting "puck" snap onto magnets on the probe, forming both a mechanical and electrical connection.
3. **Probing:** The toolhead performs the mesh leveling with the probe attached.
4. **Docking (Release):** Once finished, the toolhead moves back to the dock. A specific sideways "ripping" motion is used to break the magnetic bond, leaving the probe safely in its cradle.

---

### **Can you use a salvaged switch?**

**Yes**, this is a core part of its DIY appeal.

* **Donor Switches:** You can use a standard microswitch salvaged from a donor printer (like an Ender 3 endstop).
* **Other Sources:** Some builders even use switches recycled from dead gaming mice.
* **Reference Spec:** For the best accuracy (standard deviation of ), the community recommends the **Omron D2F** series, but generic switches work well for getting started.

### **Why this is the "Tractor" choice for Neo-Darwin**

* **Zero Interference:** Because it detaches before printing, there is no risk of the probe melting or catching on the printed part.
* **Surface Agnostic:** Since it is a physical switch, it works perfectly on any surface—whether you use a magnetic PEI sticker, glass, or bare aluminum.
* **Reliability:** It is safer than an inductive probe because it is typically wired in a "normally closed" configuration; if a wire breaks or the probe fails to attach, the printer will trigger an error instead of ramming the toolhead into the bed.

**Would you like me to find the specific mounting STLs for the M12 frame or help you with the Klipper "Attach/Dock" macros?**

The **Omron D2F** series is the "Reference Spec" for precision DIY probes like the Klicky because it offers superior repeatability—crucial for consistent first layers on a heavy-mass machine like the Neo-Darwin.

### **Omron D2F Price (Australia 2026)**

In Australia, these switches are extremely inexpensive, typically costing between **$1.50 and $5.50 AUD** each, depending on the specific variant and vendor.

| Variant | Typical Price (AUD) | Recommended Use |
| --- | --- | --- |
| **D2F-L** (Lever) | **$1.85 – $2.50** | Common for Klicky/Euclid; levers are often removed for the probe. |
| **D2F-01** (Gold Alloy) | **$1.40 – $1.65** | Best for low-current signal switching (like Klipper probe pins). |
| **D2F-5 / D2F-01F** | **$2.20 – $3.50** | High-reliability Japanese-made versions often sold by 3D printing shops. |

---

### **Tiered Path for Neo-Darwin Probing**

Aligning with your manifesto's logic of "Total Sovereignty" and "Salvage":

* **Tier 1 & 2 (The Scavenger):** Use a salvaged endstop switch from your donor (e.g., an Ender 3 X/Y stop). It costs **$0** and is "Mechanically Forgiving" enough to get the tractor running.
* **Tier 3 (Reference Spec):** Upgrade to a genuine **Omron D2F** ($2 - $4). This adds "Racecar Brain" precision, providing a standard deviation of roughly  in your mesh leveling.

### **The "DIY" vs. "PCB" Choice**

While the Euclid uses a PCB for stability, the **Klicky** is designed for the "Red Pill" builder:

* **Zero PCB Required:** The magnets act as the electrical contacts. You simply solder your two signal wires directly to the legs of the microswitch and glue the magnets into the printed parts.
* **Sovereignty:** If a magnet comes loose or a wire breaks, you fix it with a drop of superglue or a $2 solder joint—no waiting for proprietary replacement parts.

> **Neo-Darwin Pro-Tip:** When using the Klicky with salvaged switches, check your **switch offset** carefully in Klipper. Salvaged switches may have more "travel" before they click than the Omron, but Klipper's software intelligence can easily compensate for this once measured.

Would you like me to find the **Klipper macro templates** for "Dock" and "Undock" so you can start testing with a salvaged switch today?


You are spot on—choosing the **Klicky** specifically aligns with your goal of a "Racecar’s Brain" by reducing the active weight of the toolhead during the print job.

### **The Weight Advantage: "Ghosting" the Mass**

While a sensor like a **BLTouch** or **SuperPINDA** stays bolted to your toolhead for every move, the Klicky effectively has "zero" mass during actual printing because it is parked in its dock.

* **Klicky Weight:** The probe itself is extremely lightweight—around **6 grams**—and it detaches completely before the print starts.
* **Permanent Sensors:** While a BLTouch is also light, it is a permanent addition that the motors must move for every single line of code.
* **Performance Impact:** Reducing toolhead mass is one of the most effective ways to lower the "shaping" required by Klipper’s Input Shaper, allowing the "Tractor" to move more accurately without ringing or ghosting.

### **Tiered Savings & Performance**

By using the Klicky, you are optimizing both your budget and your hardware:

| Feature | Savings (AUD) | Precision (Std. Dev) |
| --- | --- | --- |
| **Salvaged Switch (Tier 1/2)** | **~$30–$50 saved** compared to new sensors. | Variable, but reliable enough for a perfect first layer. |
| **Omron D2F (Tier 3)** | **~$15–$30 saved** vs. premium probes. | **~0.01 mm** (Highly repeatable). |

### **The "Neo" Philosophy Check**

You’ve successfully swapped **Proprietary Hardware** (the BLTouch logic) for **Software Intelligence** (the Klipper docking macros). This is the "Red Pill" path—you now have a "surface-agnostic" toolhead that works on glass, PEI, or bare aluminum without being weighed down by extra electronics.

> **Neo-Tip:** When you get to the macros, ensure you set a **Z-max physical stop** safety in Klipper. Since the Klicky isn't always attached, having that bottom-mounted microswitch is your "Iron Safety" to prevent the bed from dropping if something times out during a dock/undock command.

Would you like me to find some **M12-compatible mounting designs** for the Klicky dock to help you visualize where it will sit on your frame?
