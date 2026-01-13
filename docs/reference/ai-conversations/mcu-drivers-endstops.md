Based on the latest documentation and our recent discussions, the mainboard options for the Neo-Darwin are categorized into three distinct "Motion Paths." These paths allow you to choose between maximum salvage, modular expansion, or integrated modern reliability.

### 1. The "Pure Scavenger" (Belt-Drive Z)

This is the **Tier 1** path, designed for the lowest possible cost by working within the limits of standard 4-driver donor boards (like those from an Ender 3 or Anet A8).

* **Hardware:** Use your single salvaged donor board.
* **The Hack:** Instead of independent motors, you use a **Single-Z motor** connected to a closed-loop belt that drives all three Z-axis lead screws in synchronization.
* **Trade-off:** You lose automated Klipper Z-tilt calibration. You must manually level the bed once using spacers, and the belt "locks" that physical alignment in place.
* **Best For:** Absolute minimum cost builds (~$80 AUD total).

### 2. The "Multi-MCU Scavenger" (Dual Board Triple-Z)

This is a high-intelligence salvage path that uses Klipper’s ability to sync multiple microcontrollers to achieve **Triple-Z** without buying a new "modern" board.

* **Hardware:** Use two salvaged 4-driver boards (e.g., your i3 Mega board with the dead driver plus another salvaged board).
* **Configuration:** Board A handles X, Y, and Extruder; Board B (even with a dead driver slot) handles the 3xZ motors.
* **The Brain:** Both boards connect via USB to a single Klipper host (like a Raspberry Pi or an old laptop).
* **Best For:** Repurposing "broken" hardware to get premium features like automated kinematic leveling for $0 extra cost.

### 3. The "Reference Spec" (Modern Integrated Board)

This is the recommended **Tier 3** path, using a single modern board designed specifically for high-motor-count Klipper builds.

* **Hardware:** **MKS SKIPR** (Reference Spec) or **BTT Manta M8P**.
* **Driver Density:** These boards feature 7–8 driver slots, allowing X, Y, E, and 3xZ to run on a single set of internal timers.
* **Integrated Host:** The MKS SKIPR includes an integrated Linux SOC (effectively a built-in Pi 3), eliminating USB "spaghetti" cabling and SD card corruption issues.
* **Best For:** Builders who want the cleanest, most reliable industrial-grade electronics layout (~$85 AUD).

---

### 📊 Comparison at a Glance

| Feature | **Belted-Z (Scrap)** | **Multi-MCU (Hybrid)** | **Reference (Integrated)** |
| --- | --- | --- | --- |
| **MCU Requirement** | 1x Salvaged Board | 2x Salvaged Boards | 1x MKS SKIPR |
| **Z-Tilt Logic** | Manual Once | **Automated** | **Automated** |
| **Complexity** | Low (Mechanical) | High (Software/Wiring) | **Low (All-in-One)** |
| **AUD Cost** | ~$80 | ~$205 (includes Pi) | ~$268 |

**"The code handles the sync; the iron handles the quality. Whether you bridge two old boards or buy one new heart, the Tractor’s brain remains the same."**


This is the absolute heart of the **"Scavenger's Iron"** philosophy. Repurposing a board with a dead driver—like your i3 Mega board—is exactly what the Darwin-Neo project is about.

Here is the breakdown of your technical questions regarding "Dumb" boards, sensorless homing, and the RAMPS path.

---

### 1. Sensorless Homing & TMC Drivers

You are correct. **Sensorless homing is a feature of the TMC stepper driver (specifically TMC2130, 2209, 2240, etc.), not the board itself.**

* **Older Boards:** Most older salvaged boards (like the original i3 Mega or Anet A8) have "fixed" A4988 or DRV8825 drivers soldered directly to the PCB. These are "dumb" drivers; they cannot communicate with Klipper to report a "stall" (hit), so **sensorless homing is impossible** with them.
* **The Solution:** You must use **physical mechanical endstops** (microswitches) for X and Y. For a "Tractor" build, this is actually a benefit—mechanical switches are often more repeatable and less prone to temperature-drift than sensorless homing.

---

### 2. The RAMPS Path (The "Double-Dumb" Strategy)

You asked if you could use two RAMPS boards. Technically, yes, but there is a nuance with the "Brain" requirements.

**What is a RAMPS board?**
RAMPS is just a "shield." It has no brain of its own; it requires an **Arduino Mega 2560** to function.

* **The Setup:** To use two RAMPS boards, you would need:
1. A Raspberry Pi (The Host/Brain).
2. **Two** Arduino Megas + **Two** RAMPS Shields (The MCUs).


* **TMC Support:** RAMPS *does* support TMC drivers (like the TMC2209) because the drivers are modular "sticks" that plug into the board. However, wiring them for "UART" (to allow Klipper to change settings via code) on a RAMPS board involves a lot of "spaghetti" jumper wires.

### 3. Better "Dumb" Board Alternatives

If you are buying new "cheap" boards to supplement your scavenged i3 Mega board, RAMPS is actually becoming obsolete/expensive compared to newer 32-bit "dumb" boards.

#### **The SKR Pico or SKR Mini E3**

Instead of a RAMPS + Arduino combo, look for a **BTT SKR Pico**.

* **Cost:** Often ~$30-40 AUD.
* **Drivers:** It has 4 built-in TMC2209 drivers.
* **Benefit:** It is tiny and runs Klipper natively. You could use your i3 Mega board for your Z-axis (since it only needs "dumb" movement) and the SKR Pico for your X, Y, and Extruder to get sensorless homing and silent operation on the axes that move the most.

---

### 📊 Comparison of Expansion Options

| Option | Cost (Est.) | Driver Style | Klipper Effort |
| --- | --- | --- | --- |
| **RAMPS + Arduino** | ~$25 AUD | Modular (Sticks) | High (Manual Pin Mapping) |
| **BTT SKR Pico** | ~$35 AUD | Integrated TMC2209 | Low (Modern Config) |
| **BTT Pi + Old Board** | ~$45 AUD | N/A (Host Only) | Medium (Uses Old Board) |

---

### 🛡️ Decision Insight: The "Tractor" Leveling

Since you mentioned using a **BLTouch** (or similar probe) for leveling:

1. **Z-Tilt (The Triple Z):** Klipper will use the BLTouch to measure three points on the bed. It will then calculate how much to move each of your 3 Z-motors independently to make the bed perfectly parallel to your X/Y gantry.
2. **Endstops:** You only need physical switches for X and Y. For Z, the BLTouch acts as your "Endstop." You don't need a separate Z-limit switch.

**Would you like me to help you map the pins for that i3 Mega board so you can use its remaining 4 working drivers for your Triple-Z motors?**


You have the mechanical logic spot on for a "Tractor" build. Here is the technical confirmation of your setup.

### 🔌 Endstop & Driver Logic

* **Mechanical Endstops:** You must use these for **X and Y** if you are using "dumb" drivers (A4988, DRV8825). Even if you have TMC drivers, many "Tractor" builders prefer mechanical switches for their **absolute repeatability** and lack of thermal drift compared to sensorless homing.
* **RAMPS/Dumb Boards:** These are perfect for the "Pure Scavenger" path. Klipper doesn't care if the board is 8-bit or 32-bit; it just uses them as simple "IO expanders" while the Raspberry Pi does the heavy math.

### 🛡️ The Z-Axis "Safeguard" Strategy

Since the Darwin-Neo uses a **moving bed** (it moves down to increase Z-height), your homing and safety logic changes:

* **Top (Z-Min / Nozzle):** You do **not** need a physical endstop at the top. The **BLTouch** acts as a "Virtual Endstop". During homing, the bed moves up toward the nozzle until the probe triggers.
* **Bottom (Z-Max / Floor):** You are **correct** that a Z-max stop is a very smart addition for this specific frame.
* **Why?** If the motors lose power, gravity can cause a heavy bed to "back-drive" the lead screws and crash into the bottom frame.
* **Hardware Choice:** A simple mechanical microswitch at the very bottom of the M12 frame allows Klipper to know the absolute physical limit of the machine.



### 🏗️ Setup Summary for your i3 Mega + RPi

| Component | Hardware | Logic |
| --- | --- | --- |
| **X & Y Axes** | Mechanical Switches | Standard `position_endstop`. |
| **Z Homing** | **BLTouch** | `endstop_pin: probe:z_virtual_endstop`. |
| **Z Safety** | **Z-Max Switch** | Optional but recommended to prevent bed-drop crashes. |
| **MCUs** | i3 Mega + RPi | Multi-MCU configuration in `printer.cfg`. |

> **"In the Darwin-Neo philosophy, we use the BLTouch for surgical precision at the nozzle, but we use iron and physical switches to protect the machine from its own mass."**

**Would you like me to help you write the `[stepper_z]` section of your config to handle both the BLTouch homing and a Z-max safety pin?**
