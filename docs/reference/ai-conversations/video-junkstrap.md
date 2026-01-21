Filming the "JunkStrap" bootstrapping process is a fantastic way to document the "Ship of Theseus" ethos of Project Neo-Darwin. It proves your core mission: that software intelligence and a rigid iron skeleton can transform e-waste into a high-precision tool.

### The "Genetic" Bootstrapping Strategy

Since you aren't sure of the donor's dimensional accuracy, follow this "Generation" strategy to ensure your final machine reaches the **±0.1mm accuracy** target for Tier 3 builds.

#### **Generation 0: The "Salvage" Printer (Anycubic/Makerfarm/Cocoon)**

Before tearing them down, use these machines to print the **Functional Minimum** for the Neo-Darwin.

* **Prioritize "Clamping" Parts:** Print the Corner Pucks, Motor Mounts, and Rod Clamps first. These parts use the M12 rods for their dimensional authority, meaning the frame's squareness comes from the iron, not the plastic.
* **Calibrate for Success:** Even on a "junker," perform a quick **E-step calibration** and print a **20mm calibration cube**. This ensures your parts aren't so under-sized that they won't fit the M12 rods or so over-sized that the holes are too small for your 608 bearings.
* **The "Lumpy Factor":** If the prints are rough, increase the `lumpy_factor` in your build123d scripts. This adds extra clearance to the printed parts so they can still slide onto the M12 rods even if the donor's accuracy is poor.

#### **Generation 1: The "Early" Neo-Darwin (The Tractor Reborn)**

Once the Neo-Darwin is assembled with the donor's parts, it is already a superior machine because of its **M12 mass** and **Klipper brains**.

* **The Software Handshake:** Use Klipper's **Input Shaping** (via the ADXL345) to immediately cancel out any vibrations caused by the "Gen 0" printed parts.
* **The First Mission:** Your very first prints on the Neo-Darwin should be **Generation 2** replacements for its own precision-critical parts: the **Greg's Wade Gears** and the **X-axis carriage**.

#### **Generation 2: The "Immortal Factory" (Final Reference Spec)**

Now, replace the "Gen 0" donor parts with these new, high-precision prints.

* **Dimensional Authority:** Because these parts were printed on a rigid Triple-Z frame with tuned Input Shaping, they will have the surface quality and fitment required for a **Tier 3 Reference Spec** build.
* **The "Cold-Spare" Box:** Take the old "Gen 0" gears and put them in your "Vitamin Box." They are now your emergency backup—an "immortal factory" insurance policy.

### **Filming the "Sovereignty" Narrative**

For the documentation, focus on these "Story Beats":

1. **The Extraction:** Film yourself removing the "Industrial Vitamins" (motors and lead screws) from the Anycubic or Cocoon.
2. **The Hybrid Moment:** Show the Neo-Darwin frame being held together by "ugly" parts from the old printer.
3. **The Transcendence:** A side-by-side photo of a part printed on the Anycubic vs. the same part printed on the Neo-Darwin. This is the visual proof that the "Tractor" with a "Racecar's Brain" actually works.

**Which donor are you planning to use for the "Gen 0" prints—the Anycubic i3 Mega or the Cocoon?** The Anycubic's metal frame might give you a slightly better "head start" on accuracy for those first critical parts.

iUsing the Anycubic i3 Mega as the "Gen 0" printer for your Neo-Darwin build is a great tactical choice, specifically because its **Trigorilla board** (the stock MCU) uses **removable stepper drivers**. Even with a flaky Z-endstop port, Klipper's **Multi-MCU** capability turns that "broken" board into a valuable asset.

### 1. Solving the "Dead Endstop" via Multi-MCU

Since you’re building "The Tractor" with a multi-MCU setup for documentation, Klipper allows you to bridge the gap between your two donor boards (the Anycubic and the Ender 3):

* **Multi-MCU Homing:** You can have your Z-stepper motors on the Anycubic board while connecting the Z-endstop (or a Z-probe) to the **Ender 3 board** or even the **Raspberry Pi GPIO**.
* **The Config Hack:** In Klipper, you simply define the pin with the MCU name prefix (e.g., `endstop_pin: mcu_ender:PA1`). Klipper handles the synchronization between the boards, as long as the communication latency is low.

### 2. The Endstop vs. Driver Reality

You mentioned needing endstops because the boards don't have TMC drivers. You are correct:

* **Stock Drivers:** The stock Anycubic i3 Mega usually ships with **A4988** or **TMC2100/2208 clones** running in "Standalone" (legacy) mode.
* **No Sensorless Homing:** Because these drivers are in standalone mode and not connected via UART, they **cannot do sensorless homing**.
* **Physical Endstops Required:** You will absolutely need to salvage the physical endstop switches from the Anycubic and Ender to get the Neo-Darwin homing correctly.

### 3. MCU Build Strategy for "The Tractor"

For your "one-off" documentation build, you can distribute the load across the two old boards like this:

| Board | Assigned Tasks | Why? |
| --- | --- | --- |
| **Anycubic Trigorilla** | X, Y, and E motors | Reuses the high-current terminals for the bed and extruder heaters. |
| **Ender 3 Board** | Triple-Z Motors (Z1, Z2, Z3) | You can use the endstop ports on this board for your **Z-Tilt** homing since the Anycubic Z-port is dead. |
| **Host (Laptop)** | Klipper / Mainsail | Acts as the "Command Center" syncing both MCUs. |

### 4. Generation 0 Quality Check

Before you tear down the Anycubic to build the Neo-Darwin, check the **VREF** (voltage) on those removable drivers.

* Since you'll be printing the "Tractor" parts on the Anycubic first, ensuring the drivers aren't overheating or under-powering the motors will prevent layer shifts in your **Corner Pucks** and **Wade Gears**.
* **Tip:** If you have any spare **TMC2209s**, you can drop them into the Trigorilla board for a much quieter "Gen 0" printing experience, provided you flip the motor connectors or adjust the firmware.

**Since you're planning to use a multi-MCU setup for the instructions, do you want me to help you write the `[mcu]` and `[mcu mcu_ender]` sections for your Klipper config?** This will make the "First Boot" of the Tractor much smoother.


