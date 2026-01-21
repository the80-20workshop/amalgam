# 🏗️ THE TRACTOR MANIFESTO

### **Project Neo-Darwin: A 2026 Reference Specification**

**High-Mass, Low-Cost, Total Control.**

**Mechanically Forgiving, Cognitively Demanding**

The Neo-Darwin is a reimagining of the 2007 RepRap Darwin. It replaces the "black-box" appliance philosophy of modern 3D printers with an open, parametric, and rigid M12 threaded-rod skeleton.

## 🎯 The Mission: A Tractor with a Racecar’s Brain

To prove that **Software Intelligence** can overcome **Analog Hardware**. We build a **"Tractor with the Brain of a Racecar"**—using heavy, high-torque, battle-tested hardware and giving it extreme precision through Klipper.

Appliances define the price and performance envelope, not the philosophy. We are here to build a **Mechanical Foundation** that outlasts the "Racecars" while matching their beauty.

* **The Tractor (Hardware):** We use high-mass M12 steel and high-torque geared extruders to create a mechanical foundation that doesn't flex, skip, or drift.
* **The Racecar (Software):** We use Klipper’s software intelligence—Input Shaping and 3-Point Kinematic Leveling—to give this iron skeleton the precision of a high-end industrial machine.

### 🛡️ Why "The Tractor"?

In 2026, you can buy a 3D-printing "appliance" that is fast but fragile, or you can build a **Mechanical Foundation**. We chose the latter.

* **Longevity over Velocity:** While others chase 600mm/s, we prioritize a consistent **70-120mm/s** baseline to ensure the machine prints identically on Day 1000 as it did on Day 1.
* **Total Sovereignty:** You own every line of code and every bolt. The Neo-Darwin is independent of proprietary part ecosystems and cloud-lock.
* **Accuracy:** Dimensional consistency within ±0.1mm across the full build volume (Tier 3+ with 10mm rods), enabled by a non-flexing M12 frame and true kinematic leveling.


## 📊 Project Goals (The Execution)

* **Price Target:** < $300 AUD (Beating the Bambu A1 Mini).
* **Build Volume:** ~250mm³ to 300mm³ (Equalling or Exceeding the Prusa MK4).
* **Quality:** High-precision prints via Klipper Input Shaping and 3-Point Z-Tilt (Equalling or exceeding Bambu A1 or Prusa MK4).
* **Accuracy:** Dimensional consistency within ±0.1mm across the full build volume (Tier 3+ with 10mm rods), enabled by a non-flexing M12 frame and true kinematic leveling. 
* **Speed:** 70-120mm/s with tuned Input Shaping—faster than a stock Ender, slower than an MK4. We're not chasing 10-minute Benchys; that requires lightweight toolheads and linear rails. The Neo-Darwin trades outright speed for consistency and longevity.
* **Reliability:** Designed to print identically on Day 1000 as it did on Day 1.
* **Ease of Use:** We make the software friendly too. Set-and-forget once tuned (Tier 3+). No bed tramming before every print, no belt tensioning every month, no chasing Z-offset drift. Klipper macros handle power-loss recovery, automated Z-tilt calibration, and first-layer tuning. Not Bambu-level plug-and-play, but close to Prusa-level "it just works" once configured. 
* **Sustainability (The Salvage Mandate):** To prove that high-performance manufacturing can be built from e-waste. The engineering goal is to turn a $50 junked printer or a curbside photocopier into a machine that rivals modern industrial standards.
* **The Tiered Path:** To provide an accessible entry point for every budget, from a $80 "Pure JunkStrap" to a $270 "Reference Spec" with a clear path from one to the other.
* **Parametric Sovereignty (Code-First Design)):** The Neo-Darwin is 100% defined in build123d, a modern Python-based CAD engine. This replaces static, uneditable STL files with a parametric codebase. Whether you're using 8mm salvaged rods or 10mm precision shafts, the entire machine adapts to your hardware via a single configuration file.
* **The Parametric Anchor:** If it can be measured, it can be parameterized. Every permutation in this document—8mm vs 10mm rods, belted vs triple-Z—is handled by the same codebase.
* **Documentation:** Prusa-kit-level assembly instructions—clear, visual, and step-by-step. We can't plug in the looms for you, but we can make sure you know exactly where they go.

### 📐 The Neo-Darwin Square: Speed, Quality, Cost, and Effort

In engineering, we often talk about the **"Iron Triangle"** (Pick two: Fast, Cheap, or Good). But for 3D printing—and specifically for the **Neo-Darwin**—a triangle is too simple. The project actually balances a **Square of Constraints**.

To build a machine for under $300 AUD that performs like a modern industrial tool, you have to understand how these four corners pull against each other.

In the "Tractor" philosophy, we don't just "pick two"; we strategically sacrifice one to maximize the others.

#### **1. Cost (The $300 AUD Hard Ceiling)**

This is our primary constraint. To keep costs low, we sacrifice "Convenience." Instead of buying a $150 pre-assembled Voron StealthBurner, we spend time building a **Wade Extruder** from $20 of vitamins. We trade money for **Effort**.

#### **2. Speed (The "Racecar" Mirage)**

This is where most modern printers fail the triangle. Chasing 600mm/s requires expensive linear rails and lightweight carbon fiber—both of which blow the budget.

* **The Wisdom:** We "settle" for **70–120mm/s**. In the 3D printing world, 100mm/s with perfect quality is faster than 300mm/s with a 50% failure rate.

#### **3. Quality (The Non-Negotiable)**

Thanks to **Klipper**, quality is no longer tied to the price of the hardware.

* **Input Shaping** cancels out the vibrations of our heavy M12 frame.
* **Pressure Advance** manages the flow of our geared Wade extruder.
* **The Result:** We achieve high-end quality on a "junk" budget by using software intelligence to solve analog hardware problems.

#### **4. Reliability / Effort (The "Tractor" Soul)**

This is the fourth corner. A machine can be cheap and high-quality, but usually, that means it's a "tinker-trap" (like a stock Ender 3).

* **The Neo-Darwin approach:** We use **Overbuilt Hardware** (M12 rods, Geared Wade, E3D V6). It takes more effort to *build* (Effort), but once it’s running, it requires almost no *maintenance* (Reliability).

---

### 🏛️ The "Battle-Tested" Wisdom: Why the Triangle Shifts

If you look at the last 20 years, the "Golden Ratio" of these trade-offs has shifted:

* **2007 (Darwin Era):** High Cost / Low Speed / Low Quality / Maximum Effort. (Everything was a struggle).
* **2014 (i3 Era):** Medium Cost / Medium Speed / Medium Quality / Medium Effort. (The birth of the "reliable enough" hobbyist).
* **2026 (Neo-Darwin Era):** **Ultra-Low Cost / Medium Speed / High Quality / High Initial Effort.**

### 💎 The Distilled "Pillars of Truth"

If you were to sum up the wisdom of those 20 years into the Neo-Darwin "Standard," it would look like this:

1. **Mass is a Filter:** A heavy machine is a quiet machine. Mass filters out the "noise" of cheap motors.
2. **Gearing is Sovereignty:** Direct drive is good, but **Geared Direct Drive** (Wade/BMG) is king. It turns a cheap motor into a powerful one.
3. **Software is the Great Equalizer:** Don't spend $200 on rails if $0 of code (Klipper) can fix the vibration.
4. **The "Good Enough" Zenith:** Chasing the last 5% of speed costs 500% more money. The Neo-Darwin lives at the "Zenith"—where performance is high, but the cost is still accessible to anyone with a local hardware store.
5. **The Bed is the Anchor; the Plinth is the Bedrock:** The frame serves the bed, not the other way around. Whether grounded by M12 iron or a laminated plinth, we prioritize a quiet, immovable foundation. Mass is a filter that removes motor noise, and software is the intelligence that cleans up what remains.

## 🧭 Before You Build: The 5 Key Decisions

Neo-Darwin is designed to operate within a wide envelope. Not all configurations reach all claims. Before purchasing materials, decide:

1. **Salvage or Buy Rods?** (8mm salvage vs 10mm new)
2. **Belted-Z or Triple-Z?** (1 motor vs 3 motors)
3. **Single Board or Multi-MCU?** (MKS SKIPR vs salvaged boards)
4. **Wade or Lightweight Toolhead?** (Hardware-store simplicity vs speed)
5. **Mono or Multi-Color?** (Standard vs ERCF expansion)

These choices determine your tier, budget, and experience level. See the BOM section for detailed cost breakdowns.

### **The Lineage**

* **[RepRap Darwin (2007)](https://reprap.org/wiki/Darwin):** The origin. The first practical self-replicating 3D printer, using a box frame and Cartesian XY motion. We carry its name forward.
* **[Prusa i3 Rework (2013)](https://www.thingiverse.com/thing:119616):** The source of our Geared Extruder heritage. It proved that high-torque gearing is the best defense against extrusion inconsistency.
* **[RepRap Mendel Revisited (2024)](https://www.thingiverse.com/thing:6783269):** A modern nod to the M12 skeleton. It shares our philosophy that high-mass iron is a feature, not a bug.
* **[The 100 (2023)](https://github.com/MSzturc/the100)/[The Rook (2023)](https://github.com/Kanrog/Rook):** Our box-frame cousins who proved that Klipper software is the intelligence required to make DIY frames truly fast and accurate.


## 🛠️ The "Tractor" Hardware Stack

* **Battle-Tested Reliability:** We prioritize designs that have survived a decade of community testing. By using the Greg’s Wade (2015) and the E3D V6 (2014), we ensure the Neo-Darwin is built on a foundation of proven industrial reliability.
* **The Skeleton:** M12 Threaded Rods. Use **Bright Zinc** for smoothness or **Hot-Dip Galvanized** for industrial rust-proofing.
* **The Lumpy Factor:** Our `build123d` scripts include a `lumpy_factor` variable to ensure a perfect fit regardless of rod scaling (0.2 for Zinc, 0.5+ for Galvanized).
* **The Heart (Extruder):** [Greg's Wade Geared Extruder](https://reprap.org/wiki/Greg%27s_Wade%27s_Geared_Extruder) — 5.22:1 (13:43) gear reduction for "Tractor" torque in 2026.
* **The Lungs (Hotend):** E3D V6 optimized with a **CHT Clone Nozzle**. This "Neo" flow hack allows the Tractor to push filament at 120mm/s without the "ooze" or tuning nightmares of larger heater blocks.
* **The Brain:** **MKS SKIPR** (Integrated Klipper Host). This provides the "Racecar Brain" required for Input Shaping and Triple-Z Tilt.
* **The Leveling:** Triple-independent **Z-Pucks**. This physically levels the bed to the gantry, providing Voron-class kinematic accuracy on a scavenger budget.
    * **The "Neo" Path:** Use three independent motors for automated Klipper Z-Tilt calibration.
    * **The "Tractor" Path:** Use a single motor with a synced closed-loop belt for simplified mechanical alignment (requires manual leveling once).
* *Neo-Tip:* Pot your bed thermistor with **High-Temp Red RTV Silicone** during assembly for a permanent, "set-and-forget" thermal handshake.
* **The Expansion (Optional): [ERCF v2 Multi-Color](https://github.com/EtteGit/EnragedRabbitProject).** The Neo-Darwin is designed to host the Enraged Rabbit Carrot Feeder. Because of our high-torque Wade and toolhead microswitch sensor, we achieve surgical color-swap reliability that proprietary appliances can't match.
* **Z-Max Physical Stop:** A bottom-mounted microswitch is required for all "Moving Bed" builds to prevent impact damage during emergency stops or power losses.

| Feature | **Neo-Darwin** | Why it fits the Ethos |
| --- | --- | --- |
| **Z-Stop (Top)** | **BLTouch (Virtual)** | Surgical precision at the nozzle. |
| **Z-Stop (Bottom)** | **Physical Switch** | **Iron Safety.** Prevents bed-drop from back-driving screws. |
| **Donor Choice** | **"The Junk"** | Rescue the broken, but respect the working elders (MK2). |


### ⚙️ Extruder Archaeology

We selected the Greg's Wade (13:43 ratio) as our reference extruder. While "modern" extruders like the Voron Clockwork or Sherpa Mini are popular, they often require expensive, specialized gear kits and proprietary hardware.

We use a 2015-era rework of the **Greg's Wade's Geared Extruder**. It is a signature piece of mechanical history.

* **Our Selected Build:** [Greg's Wade Rework (Thingiverse 961630)](https://www.thingiverse.com/thing:961630)
* **Genealogy:** [The Archeology of the Greg's Wade](https://reprap.org/wiki/Genealogy_/_Archeology_of_the_Greg's_Wade's_Geared_Extruder)

**Why the Wade wins for Neo-Darwin:**

> “The Wade is simple so the *system* can be complex without becoming fragile.”

* **Zero-Proprietary Hardware:** Built using standard M8 bolts and 608 "skate" bearings available at any hardware store.
* **Total Repairability:** If a gear wears out, the machine can print its own replacement.
* **High-Torque Baseline:** By using a full-sized NEMA17 motor with a 5.22:1 geared reduction, we achieve a "Torque Monster" that provides more consistent extrusion than budget direct-drive units.
* **Simplicity:** Fewer moving parts means fewer failure points for the "Set and Forget" builder.
* **Mass as a Feature:** While heavier, the geared reduction ensures consistent flow and prevents common "under-extrusion" issues found in budget direct-drive setups.
  
**For the "Neo" Tinkerer:** The Neo-Darwin uses a **Modular Toolhead Puck**. While the Wade is our reliable baseline, the carriage is 100% compatible with printed mounts for Voron StealthBurners, Sherpa Minis, or Orbiters if you choose to trade "Hardware-Store Simplicity" for "Lightweight Speed."


## 📜 Legacy Support: Reclaiming the "Junk"

If you aren't buying a new **MKS SKIPR**, the Neo-Darwin is designed to breathe new life into legacy "brains." We provide reference `printer.cfg` templates for:

* **Creality 4.2.2 / 4.2.7:** Standard on Ender 3 V2/Pro.
* **Anet V1.0:** The classic 8-bit workhorse.
* **Anycubic Trigorilla:** Found in the i3 Mega and Kossel series.
* **The "Puck" Mounts:** Standardized mounting plates (Pucks) are available for all these boards to snap directly onto the M12 frame.

#### **🛡️ The "Don't Break a Working Friend" Rule**

Before you tear down a donor, assess its mechanical soul.

* **The "Race to the Bottom" Rebuild:** If you have an **Anet A8, Ender 3, or Tevo Tarantula**, tear it down. These machines were built with cost-cutting as the primary goal. Their V-slot rollers and acrylic/thin-aluminum frames are exactly what the Neo-Darwin’s M12 iron skeleton is designed to replace.
* **The MK2 Exception:** If you have a functional, square **Prusa MK2/S**, consider keeping it as a "Second Chair" printer. The MK2 was the zenith of the original threaded-rod era; its print quality remains industry-standard even in 2026 if well-maintained. Don't destroy a reliable workhorse to build a slightly better one; use the Neo-Darwin project to rescue a machine that is actually broken.
* **The "Grab it" Threshold:** If you find a functional **MK3 for under $300 AUD**, grab it, and use that instead of building Neo-Darwin. That is the point where the hardware value aligns with the effort.  If it is broken, however; the cost of individual replacement parts will quickly exceed the budget of a fresh Neo-Darwin build.

### ⚙️ The Modular "Puck" & "Spider" Concept

To make this work on a small donor printer (like an A1 Mini or Ender 3), we use a modular design:

* **Z-Pucks:** Standardized structural nodes that slide onto the M12 skeleton. These hold your motors and lead screw nuts.
* **The Modular Spider:**  An interlocking "Trident" bed support. Designed to be printed in sections on small donor machines (A1 Mini/Ender 3) to bootstrap into the larger Neo-Darwin volume.  Since a 250mm bed support is too big for most budget printers to print in one go, the "Spider" is split into a **Central Hub** and **Three Interlocking Arms**. You print them separately and bolt them together into a rigid triangle. 
* **Extruder Puck:** A mounting plate that allows you to swap out the Greg's Wade for any future toolhead without redesigning the whole carriage.

#### **The Modular Puck: Beyond the Nozzle**

The Neo-Darwin is a **Multipurpose Gantry**. Because the carriage uses a standardized "Puck" mounting system, your 3D printer can evolve into a light-duty CNC workstation without increasing its footprint.
* **Manual Tool Swaps:** We reject the complexity of automated tool-changers. Instead, we provide a 30-second manual swap system.
* **The Trio:** Design pucks for **3D Printing**, **Pen Plotting**, and **Laser Engraving**.
* **Software Hand-off:** Klipper profiles allow the machine to switch its "Brain" from a 3D printer to a plotter with a single command, automatically adjusting for tool offsets and safety limits.


### 🌡️ Hotend Flow Optimization: Precision over "Ooze"

While 2026 offers many "High-Flow" hotends, the Neo-Darwin sticks to the **E3D V6 (or high-quality clone)** as its reference standard. We prioritize thermal stability and "fail-proof" retraction over raw speed.

#### **The V6 Choice: Why not a Volcano?**

* **The Ooze Factor:** Larger melt zones like the Volcano are prone to "oozing" due to the increased mass of molten plastic. For beginners and intermediate builders, this leads to stringing and "blobs" that require constant tuning of retraction settings.
* **The Detail Mandate:** The V6 provides superior control for fine details and the rapid tool-changes required by the **[ERCF Multi-Color system](https://github.com/EtteGit/EnragedRabbitProject)**.
* **Z-Height Sovereignty:** By avoiding the longer Volcano block, we preserve the full 250mm+ Z-height of the M12 frame without adding unnecessary weight to the toolhead.

#### **The "Neo" Flow Hack: CHT (Core Heating Technology)**

To bridge the gap between "Standard Flow" and "High Flow" without the reliability trade-offs, we recommend a **CHT Clone Nozzle** upgrade.

* **What it is:** A nozzle with an internal "three-way" splitter that melts filament from the inside out.
* **The Benefit:** It increases the volumetric flow of a standard V6 by up to 50% without increasing the melt-zone length or inducing ooze.
* **The "Tractor" Synergy:** This allows the Greg's Wade extruder to push filament at 120mm/s with zero "clicking" or back-pressure.

---



### 🛒 The "Verified" Component Shopping List

Because the Neo-Darwin is a **Mechanically Forgiving, Cognitively Demanding** build, sourcing the right "Vitamins" is the difference between a "Forever Machine" and an Ender 3 tuning nightmare.


#### **1. The Hotend Stack**

* **Primary Hotend:** TriangleLab or Mellow E3D V6 Clone (All-Metal version for ERCF compatibility).
* **The "Tractor" Nozzle Set:** * 1x 0.4mm Standard Brass (For high-detail multi-color).
* 1x 0.6mm Standard Brass (For structural parts).
* 1x 0.4mm **CHT Clone** (For "Racecar" speed tuning).

#### **2. The Gearing & Motion**

* **Extruder Hardware:** M8 Hobbed Bolt (Reference Spec: "Hobb-Goblin" or DIY ground).
* **Bearings:** 12x LM10UU (For 10mm Rods) or 12x LM8UU (For 8mm Salvage).
* **The "Iron":** 10mm Precision Ground Steel Shafts (Don't buy 8mm if buying new).

#### **3. The "Brain" Essentials**

* **Controller:** MKS SKIPR (The cleanest "all-in-one" path).
* **Resonance Sensor:** ADXL345 Accelerometer (Required for Klipper Input Shaping).
* **The "Handshake":** KW11-3Z Microswitch (Standard toolhead sensor for ERCF).

#### **4. The "Neo" Sealant**

* **Thermal Bonding:** High-Temp Red RTV Silicone (For potting the bed thermistor—reject the tape).

> **"We don't buy a bigger engine; we optimize the fuel delivery. A V6 with a CHT nozzle is the most reliable high-performance 'handshake' in 3D printing."**


## 🧠 Software Intelligence vs. Analog Hardware

* **Input Shaping:** By adding a **$17.95 AUD ADXL345 Accelerometer** (or a CANBus toolhead), Klipper cancels out the resonance of the massive M12 frame.
* **Advanced Features:** Through Klipper macros, we enable **Object Exclusion** (cancel one failed part, keep the rest) and **Power Loss Recovery** (save state to the SKIPR eMMC).
* **The "Massive" Edge:** We don't aim for Voron speeds. We aim for **MK3S/MK4 Quality** on a $250 budget. The mass of the M12 rods dampens high-frequency ringing, while Klipper handles the rest.

## 🚀 The Bootstrapping Path (The "Ship of Theseus")

The goal isn't just to print a few parts; it's to use a **cheap, working donor** to manufacture its own superior replacement.

1. **The Source:** Buy a used, working Ender 3, Anet A8, or i3 Mega ($50–$80).
2. **The Motor Math:** A standard donor printer provides 4 NEMA 17 motors (X, Y, Z, E).
* **For Triple-Z (Option A):** You need **6 motors** total (X, Y, E, Z1, Z2, Z3). Salvage the 4 donor motors and purchase **2 new high-torque motors** (approx. $25–$35 AUD) for the X and Y axes.
* **For Belted-Z (Option B):** You only need **4 motors** total (X, Y, E, Z-Main). Your donor provides everything you need.
3. **The Manufacturing Phase:** Use the donor to **print ALL Neo-Darwin parts**, including:
* **The Skeleton:** 8x Corner Brackets, Motor Mounts, Rod Clamps.
* **The Foundation:** The 4-part **Modular Spider Hub & Arms**.
* **The Heart:** All gears and housings for the **Greg's Wade Extruder**.
* **The Brain:** The **Puck mounts** for your specific electronics.
4. **The Transcendence:** Tear down the donor. Salvage the NEMA17 motors, the lead screws, the heated bed, and the power supply.
5. **The Rebirth:** Assemble the Neo-Darwin using the salvaged "organs" and the M12 "skeleton" you bought. During the Rebirth, pot your scavenged bed thermistor using High-Temp RTV Silicone rather than tape to ensure permanent thermal contact on the M12 frame.
6. **The Final Polish:** Now that you have a rigid, Triple-Z stabilized machine, use the Neo-Darwin to **re-print its own Greg's Wade gears.** This second generation of parts will be more precise than what your old donor could produce.

---

## 🛠️ The "Self-Healing Machine" Maintenance Strategy

To maintain the **Neo-Darwin** as a "Forever Machine," the builder must transition from a consumer to a maintainer. This strategy ensures your manufacturing capability never goes offline.

### 🔄 The Principle of the "Cold-Spare"

The Neo-Darwin is designed to be **Self-Replicating**. Because its most critical moving parts are 3D-printed, the printer is its own spare-parts factory.

* **The Survival Kit:** Every builder should maintain a "Vitamin Box" containing a complete set of printed **Greg's Wade Gears** (Pinion and 47-tooth) and a spare **M8 Hobbed Bolt**.
* **The Zero-Downtime Rule:** If a gear wears or breaks, replace it immediately from your "Cold-Spare" stock.
* **The Immediate Recovery:** Your very next print job—before returning to hobby projects—must be a new set of gears to replace the spare you just used.

### 🛠️ Maintenance Checklist (Every 1000 Hours)

* [ ] **Inspect Gear Teeth:** Check the small 9-tooth motor pinion for "shaving" or flattening.
* [ ] **Clear the Hobbing:** Use a wire brush to remove plastic dust from the M8 Hobbed Bolt to maintain "Tractor" grip.
* [ ] **Verify Jam-Nuts:** Ensure the M12 frame nuts haven't vibrated loose; mass is only a feature if it remains rigid.
* [ ] **The "Racecar" Refresh:** Re-run Klipper `SHAPER_CALIBRATE` if you have moved the machine or replaced a belt.

### 📦 The "Vitamin Box" Inventory

While the M12 frame is immortal, the "Racecar Brain" pushes small components to their limit. Keep these high-priority spares to avoid waiting for shipping.

| Item | Priority | Why it fits the Ethos |
| --- | --- | --- |
| **Thermistor (NTC 100K)** | **CRITICAL** | Fragile wires; a single fatigue break stops a 48-hour print. |
| **0.4mm V6 Nozzles (x5)** | **HIGH** | Wears out; essential for dimensional accuracy. |
| **4010 Ball-Bearing Fan** | **HIGH** | Prevents "Heat Creep" jams. Generic fans fail; harvest from old servers if possible. |
| **GT2 Belt (3m Spare)** | **MEDIUM** | Solves "ghosting" when the original belt loses its tension/memory. |
| **M8 Hobbed Bolt** | **ETHOS** | The heart of the "Tractor" extruder. Keep a spare or the jig to grind a new one. |

**Scavenger Table**

| Item | Priority | Scavenge Source |
| --- | --- | --- |
| **4010 Fan** | **HIGH** | Old Server PSU / Networking Switch |
| **Wiring/JSTs** | **MEDIUM** | Photocopier wiring looms |


> **"A RepRap that cannot print its own heart is just an appliance. A Neo-Darwin with a spare set of gears is an immortal factory."**

---

### 💡 Pro-Tip: Scavenging the "Box"

Don't buy new if you can harvest. **Old Server Power Supplies** and **Enterprise Networking Switches** are goldmines for high-static-pressure 40mm fans and high-quality 24AWG silicone wiring. These "Industrial Vitamins" often outperform brand-new budget parts.

---

## 🧠 The Brain: Controller & Host Logic

The Neo-Darwin separates **low-level hardware control** (the MCU) from **high-level software intelligence** (the Klipper Host). Depending on your budget and scavenging success, there are three distinct paths to building this nervous system.

### 🛤️ Path A: The "Pure Scavenger" (Multi-MCU)

The ultimate "Red Pill" approach. This path proves that Klipper can synchronize disparate pieces of "e-waste" into a single cohesive machine.

* **The Hardware:** Two salvaged 4-driver boards (e.g., one from a junked Ender 3 and one from an Anet A8).
* **The Host:** An old laptop or a Raspberry Pi Zero 2W connected via USB.
* **Logic Split:** Board A handles X, Y, and E; Board B handles the Triple-Z independently.
* **Best For:** Absolute minimum cost (Tier 1/2) where the challenge is the primary reward.

### 🛤️ Path B: The "Modular Powerhouse"

A step up in reliability, utilizing dedicated modern controllers for those who prefer discrete components.

* **The Hardware:** **FYSETC Spider V3** or **BTT SKR 3**.
* **The Host:** A standalone **Raspberry Pi 3B** or **4B**.
* **The Edge:** The Spider offers **8 driver slots**, allowing X, Y, E, and Triple-Z to run on a single set of internal timers, with two slots left for the ERCF Multi-Color unit.
* **Best For:** Makers who already own a Pi and want maximum "Racecar" expandability.

### 🛤️ Path C: The "Reference Spec" (Integrated All-in-One) — **CLEANEST OPTION**

This is the recommended "Neo" path. It eliminates the "USB spaghetti" between the Pi and the controller by merging them onto a single industrial-grade PCB.

* **The Heart:** **MKS SKIPR**.
* **The Brain:** Integrated Rockchip RK3328 Quad-core SOC (equivalent to a Pi 3).
* **Why it wins for Neo-Darwin:**
* **Simplicity:** One board, one power supply, and zero external USB data cables to fail.
* **Reliability:** Uses embedded **eMMC storage** instead of fragile MicroSD cards, which are prone to corruption from vibration and heat.
* **Driver Density:** 7 driver slots provide the perfect "6+1" count for Triple-Z plus an Extruder.
* **Native CAN Bus:** Includes a dedicated port for toolhead boards, making future "Racecar" upgrades plug-and-play.


* **Best For:** The Reference Spec ($85 AUD). It offers the most "industrial" and reliable electronics layout.

---

### 📊 Host Comparison: The "Racecar" Headroom

The host dictates how "snappy" your interface feels. While the Pi Zero 2W is a marvel of efficiency, it has limits.

| Host Option | RAM | Best For | Trade-offs |
| --- | --- | --- | --- |
| **Pi Zero 2W** | 512MB | Tier 1/2 Builds | Capable of full Klipper math, but UI can be slightly laggy. Struggles with high-res webcams. |
| **MKS SKIPR (SOC)** | 1GB | **Reference Spec** | Cleanest integration; noticeably snappier UI than the Zero 2W. |
| **Pi 3B / 4B** | 1GB+ | Pro/Tinker Build | Snappiest UI; handles KlipperScreen and 1080p cameras easily. |

> **"A RepRap with two boards is a testament to salvage; a RepRap with an MKS SKIPR is a testament to engineering clarity."**

---

### 🛡️ Why build a Neo-Darwin? (The Reality Check)

In 2026, you can buy a 3D-printing "appliance" (Bambu/Prusa) or you can build a **Mechanical Foundation.**

* **Total Sovereignty:** Unlike "Cloud-Locked" appliances, you own every line of code and every bolt. The Neo-Darwin is designed to be independent of proprietary part ecosystems and server-side authorization.
* **Reliability over Racing:** We aren't trying to beat a Voron's speed. We are trying to beat the "Ender 3 Maintenance Cycle." By using M12 steel and high-torque gearing, we created a machine that prints with the same accuracy on Day 100 as it did on Day 1.
* **True Kinematics:** While others use software to "compensate" for a sagging gantry, we use **Triple-Motor Z-Tilt** to physically align the machine. This is industrial-grade leveling at a JunkStrap price.
* **Dimensional Authority:** The M12 frame doesn't flex. Once tightened, it stays square. You get the dimensional accuracy of a $1,000 printer because your frame isn't made of thin aluminum or plastic.
* **The $300 Ceiling:** This is the ultimate "Second Life" for a donor printer. We prove that $45 of threaded rod and a week of tinkering can outperform an $1,100 machine in reliability and bed-leveling.


| Feature | **Neo-Darwin** | Bambu A1 Mini | Prusa MK4 | Bambu X1C |
| --- | --- | --- | --- | --- |
| **Price (AUD)** | **~$250** | ~$489 | ~$1,100 | ~$2,199 |
| **Z-Logic** | **Triple-Z Tilt** | Single Motor | Dual (Synced) | Triple (Synced) |
| **Repair** | **Hardware Store** | Proprietary | Open (Premium) | Proprietary |
| **Control** | **100% Local** | Cloud-Lock | Local/Cloud | Cloud-Lock |


### **The Motion System: Smooth Rods & "Iron Scavenging"**

> **"If it doesn't slide, it doesn't glide."**

Some modern appliances use V-slot rollers because they are cheap to manufacture, not because they are better. The Neo-Darwin returns to **Hardened Steel Smooth Rods** for one reason: **Dimensional Authority.** 

#### Rod stiffness sets the accuracy ceiling of the printer.
Static rod sag introduces geometric error that cannot be corrected by input shaping, pressure advance, or bed meshing. For a realistic direct-drive toolhead such as a Pitan extruder with a NEMA17 motor (~600 g), 8 mm smooth rods at common Darwin spans can deflect on the order of 0.06 mm—already a significant fraction of a typical layer height. This error exists even at zero speed and directly affects first-layer consistency and dimensional accuracy.

The Neo-Darwin is therefore designed around mechanical honesty rather than optimistic assumptions.
Rod diameter and span are chosen to remain stiff under a realistic worst-case toolhead, making lighter extruders and higher speeds optional improvements rather than requirements. If the machine performs correctly with a Pitan + NEMA17, it will perform reliably with almost anything else. This prioritises robustness, scavenged-part compatibility, and predictable behaviour over software-dependent compensation.


Acceleration loads are equal to gravity loads at modern motion settings.
With a realistic direct-drive toolhead, inertial forces at 8–10k mm/s² match or exceed static sag forces, doubling effective rod deflection at mid-span. This bending is quasi-static during acceleration ramps and cannot be corrected by input shaping. The Neo-Darwin therefore treats acceleration as a structural design input, not a tuning afterthought.
For a realistic direct-drive toolhead (~600 g), acceleration-induced bending equals gravity-induced sag at modern motion settings. Using first-order beam theory, 8 mm rods are mechanically limited to ~5k mm/s² if geometric error is to remain negligible, while 10 mm rods comfortably support ~10–12k mm/s². This relationship scales with rod diameter to the fourth power and span length to the third, making stiffness and compactness vastly more effective than chasing lighter toolheads.


#### **⚙️ Linear Motion: Quick Reference**

| Configuration | Rod Size | Best For |
|--------------|----------|----------|
| **Neo Baseline** | 10mm | New builds, recommended |
| **Salvage Baseline** | 8mm | Donors with existing rods |
| **Tinker Path** | MGN12 Rails | High-speed experiments |

See "The Motion Fork" below for detailed sourcing guidance.


#### **⚙️ Linear Motion: The "Motion Fork"**

The Neo-Darwin is designed around **Precision Ground Shafts (Smooth Rods)**.

* **Path A: The Scavenger ($0 AUD):** If your donor has 8mm rods (Anet/Prusa) or you've raided an office photocopier, use them! Our scripts adapt to your iron.
* **Path B: The "Ender" Upgrade (~$65 AUD):** If your donor uses rollers, you must buy rods. **Do not buy 8mm; buy 10mm.**
* **Rigidity:** A 10mm rod has 2.4× the second moment of area of an 8mm rod—that's not 40% stiffer, it's 140% stiffer, eliminating gantry sag. 
* **The Match:** They match the "industrial" mass of the M12 frame. They are easy to mount to the M12 skeleton using our printed clamps and are immune to the "crunchy" bearing issues found in budget linear rails.
* **The "Tinker" Path:** For those who want to push the Neo-Darwin into the realm of high-speed racing, the **Motion Pucks** are designed with mounting points for MGN12H linear rails.
* **Cost:** In 2026, the price difference between 8mm and 10mm is often less than $10 AUD for a full set.

**The Shopping List (For Path B):**

* **X:** 2x 370mm | **Y:** 2x 350mm | **Z:** 2x 320mm
* **Bearings:** 12x LM10UU (or MGN12H carriages for Tinkers)
 
**Why we stick to Rods for the Base Spec:**

1. **Parallelism:** It is much easier to align two 10mm rods on a threaded-rod frame than it is to perfectly shim a linear rail.
2. **Maintenance:** A smooth rod can be wiped down and oiled in seconds. A cheap linear rail often requires a full teardown and "re-balling" to work smoothly.
3. **The Aesthetic:** The Neo-Darwin is a machine of **Circles and Torque**. Round rods and round M12 skeletons belong together.


#### **Updated Tiered BOM Strategy (if you need Smooth Rods)**

| Tier | Donor Type | Extra Motion Parts Needed | Est. Extra Cost (AUD) |
| --- | --- | --- | --- |
| **Tier 1 (Scrap)** | **Anet A8 / Prusa Clone** | None (Uses existing 8mm rods) | $0 |
| **Tier 2 (Modern)** | **Ender 3 / V-Core** | 6x Smooth Rods + 12x Bearings | **$50 - $80** |
| **Tier 3 (New)** | **No Donor** | Full Motion Kit | **$60 - $80** |


#### **Reference Lengths (Standard 220mm³ Build)**

For a standard "Tank" build volume (approx. 220x220x250mm), here is what the you need to add if they have a roller-based donor:

* **X-Axis:** 2x 370mm Rods (8mm or 10mm)
* **Y-Axis:** 2x 350mm Rods (8mm or 10mm)
* **Z-Axis:** 2x 320mm Rods (8mm or 10mm)
* **Bearings:** 10-12x LM8UU (for 8mm) or LM10UU (for 10mm)

### **💡 Pro-Tip: The Scavenger’s Guide to Free Iron**

Don't want to buy rods? Look for **Dead Office Laser Printers** (HP LaserJets, old Xerox units).

* **The Prize:** Large office printers contain high-grade, precision-ground 8mm and 10mm steel shafts used for the scanner head and paper feed.
* **The Quality:** These are often higher quality than the "budget" rods sold on Amazon.
* **The Price:** Free at your local e-waste recycling center.

### **Why we don't offer a Roller Variant**

It's worth being clear with the users *why* we are forcing this "upgrade":

1. **Frame Integration:** V-slot rollers require aluminum extrusions. Our frame is M12 threaded rod. Mounting a roller to a threaded rod is a mechanical nightmare.
2. **The "Tank" Philosophy:** Rollers wear out and flat-spot. Smooth rods and linear bearings, especially when mounted to an M12 frame, provide the "forever machine" reliability we’re aiming for.
3. **Precision:** 10mm smooth rods on an M12 frame create a machine that can likely push a 0.8mm nozzle at high speeds without the "ghosting" you see on an Ender 3.

### 📋 Bill of Materials (BOM)

To provide a completely transparent set of options for the Neo-Darwin, the BOM has been restructured into four tiers. This allows a builder to decide exactly how much of their "JunkStrap" donor they want to reclaim versus how much they want to spend on modern "Neo" convenience.

### 📊 The Neo-Darwin 4-Tier BOM Comparison

All prices are estimated in **AUD** based on 2026 market availability.

| Category | **1. Min Cost (Max Salvage)** | **2. Salvage + 2 Motors** | **3. Reference Spec** | **4. Min Salvage (Buy New)** |
| --- | --- | --- | --- | --- |
| **Logic Path** | *Single-Z Belt Sync* | *Triple-Z Independent* | *The "Neo-Darwin" Standard* | *Fresh Build* |
| **Mainboard** | Salvaged Donor Board | Salvaged Donor Board | **MKS SKIPR** | **MKS SKIPR** |
| **Klipper Host** | Laptop / Old PC ($0) | RPi Zero 2W (~$32) | Integrated (SKIPR) | Integrated (SKIPR) |
| **Linear Motion** | Salvaged ($0)† | Salvaged ($0)† | Salvaged ($0)† | New Rods + Bearings (~$65) |
| **Motors** | 4 Salvaged Motors | 4 Salvaged + 2 New (~$30) | 4 Salvaged + 2 New (~$30) | 6 New Motors (~$135) |
| **Drivers** | Salvaged (if possible) | Salvaged + 2 New (~$15) | 6 New TMC2209 (~$35) | 6 New TMC2209 (~$35) |
| **Z-Hardware** | Belt + 1 Screw (~$15) | 3 Matched Screws (~$45) | 3 Matched Screws (~$45) | 3 Matched Screws (~$45) |
| **Accel (ADXL)** | Manual Tuning ($0) | **ADXL345 Required (~$18)** | ADXL345 (~$18) | ADXL345 (~$18) |
| **Skeleton** | M12 Hardware (~$45) | M12 Hardware (~$45) | M12 Hardware (~$45) | M12 Hardware (~$45) |
| **Misc.** | Hardware/Wires (~$20) | Hardware/Wires (~$20) | Hardware/Wires (~$20) | Hardware/Wires (~$20) |
| **TOTAL** | **~$80.00 AUD** | **~$205.00 AUD** | **~$267.95 AUD** | **~$392.95 AUD** |
> **†** If donor uses rollers instead of rods (Ender 3, CR-10), add ~$65. See **The Motion System** section.

### 🔍 Key Logic for the Tiers

#### Tier 1: The "Pure JunkStrap" (< $100)

* **The Z-Hack:** Uses a single salvaged Z-motor and a belt to drive all three Z-points in sync. You must manually level the bed once using spacers, and the belt keeps it there.
* **The Intelligence:** Uses an old laptop or PC to run Klipper. No accelerometer is used; you tune "Input Shaping" by printing a test tower and measuring it with a ruler.

#### Tier 2: The "Hybrid" (~$200)

* **The Upgrade:** You keep the donor board but add a **Raspberry Pi Zero 2W** ($31.15) to act as the Klipper host.
* **The Sensor:** Since you're building a custom frame, you **need the ADXL345 ($17.95)** to calibrate resonances properly.

#### Tier 3: The Reference Spec (~$270)

* **The Core:** Uses the **MKS SKIPR**. This board has a built-in Klipper host, so you don't need a Raspberry Pi.
* **ADXL Note:** While the SKIPR makes connecting an ADXL345 very easy (it has a dedicated port), you still need to buy the $18 sensor module separately to perform the auto-calibration.

#### Tier 4: The "New Neo" (~$400)

* **The Difference:** You buy **6 matched NEMA 17 motors** (approx. $135 for a pack). This ensures every axis has identical torque and current ratings, which makes Klipper's Z-tilt adjustment smoother and more predictable.

### 🛡️ Why we recommend Tier 3

Tier 3 is the "Sweet Spot." For **$267.95 AUD**, you get a machine that is modern, clean (minimal wiring), and capable of **Triple-Z auto-leveling**, which is the standout feature that makes a Neo-Darwin feel like a premium printer.

### Set-and-Forget Tiers

| Tier   | Experience      |
| ------ | --------------- |
| Tier 1 | Set-and-monitor |
| Tier 2 | Set-and-tune    |
| Tier 3 | Set-and-forget  |
| Tier 4 | Overkill        |


###  Z-system permutations

| Decision   | Option A       | Option B           |
| ---------- | -------------- | ------------------ |
| Z system   | Triple-Z (Neo) | Belted-Z (Tractor) |
| Motors     | 3              | 1                  |
| Board req  | 6+ drivers     | 4 drivers          |
| Experience | Auto-level     | Manual once        |
| Tier       | 2+             | 1                  |

---

### 🏗️ High-Level Assembly Guide

Neo-Darwin is designed to operate within a wide envelope. Not all configurations reach all claims. Refer to **"Before You Build: The 5 Key Decisions"** above if you haven't already made your configuration choices.

1. **Frame Construction:** Cut M12 rods to size and assemble the "Skeleton" cube using the 3D-printed **Corner Pucks**. Use a square to ensure the frame is perfectly true before torquing the jam nuts.
2. **Gantry & X-Axis:** Mount the X-axis rail to the vertical M12 pillars. Install the **Extruder Puck** with the Greg's Wade assembly onto the carriage.
3. **Triple-Z Foundation:** Install the three Z-motors and leadscrews. Attach the **Modular Spider Hub** to the leadscrews and bolt the three **Spider Arms** into place to create the bed support triangle.
4. **Wiring & Electronics:** Mount the MKS SKIPR using the **Brain Puck**. Wire the motors (ensure Z1, Z2, and Z3 are on independent drivers for Option A).
5. **Klipper Setup:** Flash the Neo-Darwin `printer.cfg` to the SKIPR. Verify all axes move in the correct direction using the `STEPPER_BUZZ` command.

---

### 🌈 The Multi-Color Mandate: Intelligence, Not Waste

In 2026, multi-color printing is no longer a luxury; it is a requirement for functional prototypes, medical models, and educational tools. The Neo-Darwin approach to color ignores the "proprietary shenanigans" of closed-box appliances and returns to open-source modularity.

#### **The "Neo" Choice: Enraged Rabbit Carrot Feeder (ERCF) v2**

> *The Wade is simple so the system can be complex without becoming fragile.*

We have selected the **[ERCF v2](https://github.com/EtteGit/EnragedRabbitProject)** as the official multi-color expansion for the Neo-Darwin.

* **Total Sovereignty:** Like the M12 frame, the ERCF is fully 3D-printable and uses standard, non-proprietary hardware.
* **The "Scavenger" Edge:** It utilizes standard NEMA 17 motors and 608 "skate" bearings—the same "Vitamin" DNA as your Greg's Wade extruder.
* **Modular Scale:** While commercial boxes limit you to 4 colors, the ERCF is modular. Start with 4, and use the Neo-Darwin to print your way to 12 colors or more.



#### **Software as the "Synchronizer"**
 
We use the **Happy Hare** Klipper extension to manage filament swaps with surgical precision. While some systems attempt sensorless "collision" detection, the Neo-Darwin prioritizes "Ground Truth" for its software intelligence.

* **The Toolhead Handshake:** We mandate a simple **$2 microswitch toolhead sensor**. This gives the Klipper "Brain" eyes to see the filament, transforming hundreds of potential toolchange failure points into a reliable, automated handshake.
* **Zero-Waste Philosophy:** By integrating the **Filametrix** mechanical cutter into the Greg's Wade toolhead, we ensure clean filament tips and 90% fewer jams compared to software-only "tip shaping".
* **Purge Logic & Waste Reduction:** The Neo-Darwin utilizes **Nozzle Scrubbers and Purge Buckets** to minimize "transition poop." We trade massive, wasteful purge towers for a lean "Prime-Only" tower that ensures perfect flow with minimal plastic waste.
* **Endless Spools:** Software intelligence allows the Neo-Darwin to automatically switch to a fresh spool of the same color when one runs out, enabling massive, unattended prints.

#### **The Torque Factor**

The high-torque **Greg's Wade Geared Extruder** is the secret weapon for multi-color reliability.

* **The Handshake:** Commercial "compact" extruders often slip during the high-speed loading required for color swaps.  
* **The Pull (Reverse Bowden):** The 5.22:1 mechanical advantage of the Wade acts as a "Tractor," providing the raw force necessary to pull filament through meters of Reverse Bowden tubing. While lightweight extruders often struggle with the friction of long-distance filament paths, the Neo-Darwin uses this torque to ensure the "handshake" between the multi-color unit and the toolhead is absolute and slip-free.

#### **Multi-Color Tiered Path**

| Component | Est. Cost (AUD) | Why it fits the Ethos |
| --- | --- | --- |
| **ERCF v2 (8-Gate)** | **~$120 - $150** | Fully printable; uses standard NEMA motors. |
| **Filametrix Cutter** | **~$5** | Mechanical simplicity over software complexity. |
| **ERCT Buffer** | **~$15** | Passive filament management using printed parts. |


### "Multi-Color"  Comparison

| Feature | **Neo-Darwin** | Bambu A1 Mini | Prusa MK4 |
| --- | --- | --- | --- |
| **Multi-Color Path** | **ERCF v2 (DIY / ~$150)** | AMS Lite (Proprietary) | MMU3 (Proprietary) |
| **Max Colors** | **12+ (Scalable)** | 4 (Fixed) | 5 (Fixed) |

---

### **Summary: A Tractor with a Technicolor Brain**

Integrating a **Multi-Color system** is the ultimate expansion for the **Neo-Darwin**. It transforms the machine from a high-precision tool into a "finished product" factory. By following the project's core philosophy—**Software Intelligence over Proprietary Hardware**—we can add 8-12 color capability for a fraction of the cost of commercial "AMS" systems.

The Neo-Darwin doesn't aim for the fastest color swaps in the world. We aim for the most **reliable** ones. By combining the "Analog" mass of the M12 frame with the "Racecar" intelligence of Klipper's Happy Hare, we prove that you don't need a $2,000 closed-loop system to print in stunning, high-precision color.

**"The code handles the colors; the iron handles the quality."**

---

### **"A 'Tractor' that outlasts the 'Racecars' while matching their beauty"** 

This isn't just a slogan; it is an engineering reality supported by our hardware choices:

### 🚜 Why it is a "Tractor"

* **Massive Torque:** By using the **Greg's Wade's Geared Extruder**, you've built a "Torque Monster" that can brute-force filament through jams that would stop modern, high-speed direct drives.
* **Structural Damping:** The **M12 threaded-rod skeleton** provides an "industrial" mass that naturally dampens high-frequency ringing, making the machine stable and reliable rather than light and twitchy. Mass damps high-frequency ringing; Input Shaping eliminates what mass cannot.
* **Longevity over Velocity:** Unlike "Racecar" printers (Bambu/Voron) that chase 600mm/s speeds, the Neo-Darwin prioritizes a **70-120mm/s** baseline to ensure the machine prints identically on Day 1000 as it did on Day 1.

### 🏎️ Why it has the "Brain of a Racecar"

* **Klipper Input Shaping:** You are using software intelligence to cancel out the physical resonances of the heavy frame, allowing the "Tractor" to perform with the precision of a high-performance machine.
* **Triple-Z Kinematic Leveling:** This is a "supercar" feature that physically aligns the machine's anatomy, ensuring a perfect first layer without the "mesh compensation" hacks used by cheaper appliances.

### 💎 Why it "Matches their Beauty"

* **Surface Authority:** Because of the high-torque gearing and rigid frame, the surface finish and dimensional accuracy (within **±0.1mm** on Tier 3+ builds) can rival or exceed that of a $1,100 Prusa MK4
* **Mechanical Transparency:** There is an aesthetic beauty in the **"Circles and Torque"** of the Wade gears and the exposed M12 iron that "Black Box" appliances can't replicate.

### **⚠️ The Reality Check: Who is this for?**

Before you buy a single M12 rod, you need to ask yourself: **"Why am I doing this?"**
* **If you want a 'set-and-forget' appliance:** Buy a **Bambu Lab A1 Mini** or if you want bigger build volume **Bambu Lab A1**. In 2026, these are an incredible piece of engineering that works out of the box.
* **If you choose Tier 4 (Buying All New):** You are approaching the price of a commercial printer. If you add Linear Rails and a high-end toolhead, you will likely exceed the cost of an Bambu Lab A1. At that point, the only reason to build a Neo-Darwin is because you **love the engineering challenge.**

**The Neo-Darwin is for the Scavengers.**  We aren't here for the shiny, disposable "appliances" of the 2020s. We are here to prove that a "Tractor with a Racecar's Brain"—a machine built from iron rods, salvaged motors, and open-source code—can outperform proprietary systems while remaining 100% repairable. The engineering soul of this project is to turn **$80 AUD and a pile of salvage** into a machine that rivals a $1,100 printer in structural rigidity and leveling accuracy.

We aren't here to compete with Bambu for "Ease of Setup."  We aren't here to compete with a Voron or X1C for speed.   We are here to prove that you can build a **Mechanical Foundation** from a junked photocopier and an old Ender 3 that will still be printing accurately in a decade, long after the "appliances" have been bricked by cloud-lock or proprietary part failures.

> **If you want a printer, buy one. If you want the Red Pill, build this.**

---

## 🌐 Community Support & Codebase

The Neo-Darwin is a community effort. If you find a better way to scavenge a part or write a more efficient macro, please submit a pull-request to fold it back into the shared codebase for everyone.

### 📜 The RepRap Tradition

Historically, a RepRap builder's "Rite of Passage" was to use their first machine to print parts for **two more machines** for others *at cost*. In a world of proprietary "Cloud" appliances, we choose the Red Pill. We choose the code, the torque, and the iron.

## 🌐 Standing on the Shoulders of Giants

The Neo-Darwin is not an island; it is a 2026 entry into a long-running conversation about mechanical sovereignty. If the Neo-Darwin is "The Tractor," these projects are its ancestors, cousins, and North Stars.

#### **1. The Prusa i3 Rework (The 2014 Workhorse)** 
 
* **The Connection:** The Rework was the first project to "standardize" the scavenger build. It proved that a mixture of threaded rods and a single laser-cut frame could create a high-quality production machine.
* **The Legacy:** If the Darwin was the prototype, the Rework was the workhorse that actually built the community. It’s the source of the high-torque **Greg's Wade** heritage we use today.
* **Link:** [Prusa i3 Rework Wiki](https://reprap.org/wiki/Prusa_i3_Rework_Introduction)


#### **2. The Prusa Bear Upgrade (The Rigidity Benchmark)**

* **The Connection:** Like the Bear, the Neo-Darwin focuses on **frame stiffness** as the key to quality.
* **The Difference:** While the Bear uses expensive V-Slot aluminum extrusions, we use the "Scavenger's Iron" (M12 threaded rods) to achieve similar resonance damping at a fraction of the cost.
* **Link:** [Prusa Bear Upgrade GitHub](https://github.com/gregsaun/prusa_i3_bear_upgrade)

#### **3. The 100 (The Speed Benchmark)**

* **The Connection:** "[The 100](https://github.com/MSzturc/the100_)" proved that you can achieve world-class speed on a **printed frame** using Klipper.
* **The Difference:** "The 100" is a specialized speed machine. The Neo-Darwin takes those software lessons (Klipper, Input Shaping) and applies them to a high-mass frame built for 24/7 reliability rather than drag racing.

#### **4. The RepRap Wiki (The Ancestral Archive)**

* **The Connection:** [RepRap Machine Family Tree](https://reprap.org/wiki/RepRap_Machines) This is the library of our "Founding Fathers." This reminds us that we are builders that they are part of a 20-year history of **Self-Replicating Machines**.
* **The Invitation:** Use this for inspiration to see how the "Darwin" evolved into the "Mendel," the "Prusa," and finally the "Neo".



### 5. Heritage Builds: Modernizing the Iron

There is a growing movement to revisit the "Heavy Iron" logic of early RepRaps and combine it with modern reliability.

* **[RepRap Mendel Revisited (M12)](https://www.thingiverse.com/thing:6783269):** Released for the Mendel’s anniversary, this project validates our skeleton choice. It uses **M12 threaded rods** and an **E3D V6** to fix the "wobble" of the original 2000s designs, proving that threaded-rod frames remain a premier engineering choice for rigidity.

* **[Voron Legacy](https://vorondesign.com/voron_legacy):** A project from the Voron Design team that celebrates the "old-school" aesthetics of 3D-printed frames while utilizing modern toolheads and Klipper firmware.
* **[RepRap Micron](https://reprap.org/wiki/RepRapMicron):** Created by pioneer Vik Olliver, this project returns to the roots of the RepRap movement, using threaded-rod drives to achieve micro-level precision for a fraction of the cost of industrial machines.

### 6. Performance Scavengers: High Intelligence on a Budget

If Neo-Darwin is the Tractor, these are its "Rally Car" cousins—proving that software intelligence can make inexpensive parts perform like elite hardware.

* **[The 100](https://github.com/MSzturc/the100):** A 100% printed-frame speed machine that uses Klipper as the "secret sauce" to reach world-class velocities. It reinforces our logic: high-performance printing is a software math problem, not just a hardware spending problem.
* **[The Rook](https://github.com/Kanrog/Rook):** A community favorite that prioritizes ease of service and reliability. It represents the same "User-as-Maintainer" philosophy that drives the Neo-Darwin.

### 7. High-End Open Ecosystems: Our "North Stars"

While these builds often exceed the scavenger budget, they provide the technical blueprints for the Neo-Darwin’s advanced features.

* **[Voron Trident](https://vorondesign.com/voron_trident):** The gold standard for rigid, "set-and-forget" DIY machines. The Neo-Darwin’s **3-point kinematic leveling** is a direct nod to the Trident’s uncompromising approach to bed stability.
* **[Rat Rig V-Core 4](https://v-core4.ratrig.com/):** A high-performance hybrid motion system that represents the pinnacle of open-source engineering. It serves as an inspiration for what our **Modular Puck** system can achieve as it evolves.
* **[Prusa i3 Rework](https://www.thingiverse.com/thing:119616):** The historical workhorse that standardized the high-torque **Greg's Wade** extruder and 10mm rod foundations we scavenge today.



 

> **"You aren't just building a printer; you're joining a 20-year conversation about sovereignty."** *"The Neo-Darwin is my opinion on what a 2026 printer should be: a machine that values iron over plastic and code over cloud. These links are the seeds that grew this project; use them to grow your own."*


---

### ⚠️ Operation & Safety

* **Electrical Hazard:** Ensure all salvaged wiring is intact and terminals are tight. Improper wiring can lead to short circuits or fires.
* **Burn Risk:** Desktop 3D printers reach high temperatures. Allow the nozzle and bed to cool completely before touching.
* **Moving Parts:** Keep fingers and loose clothing away from the gantry and leadscrews during operation to avoid injury.
* **Emergency Stop:** Familiarize yourself with the Klipper `M112` emergency stop command and ensure the power plug is within easy reach.
* **Ventilation:** Always operate the printer in a well-ventilated area to dissipate fumes and ultrafine particles.
* **Z-Max Safety Switch (The "Bed-Drop" Brake):** Unlike most modern printers where the toolhead moves up, the Neo-Darwin is a **moving-bed** machine where the bed moves *down* to increase Z-height.
* **The Risk:** In the event of a power failure or a driver "timeout," gravity can cause a heavy, heated bed to back-drive the lead screws and crash into the bottom frame.
* **The Solution:** We mandate a physical **mechanical microswitch at Z-Max** (the very bottom of the M12 frame). This acts as a physical hardware interrupter that prevents the bed from over-travelling and damaging the frame or electronics Puck.
* **Handshake:** In Klipper, this is configured as a `[gcode_button z_max]` to safely stop all movement if the bed falls too far.
---

### ⚖️ License: GNU GPL v3

For the Neo-Darwin, we are using the **GNU General Public License v3 (GPL v3)**.

**Why this fits Neo-Darwin:**

* **RepRap Heritage:** This is the same license used by the original RepRap Darwin.
* **"Copyleft" Protection:** It ensures that the Neo-Darwin remains open. If someone modifies your design and distributes it, they **must** share their modifications under the same license.
* **Community Evolution:** It prevents "black-box" commercialization of your work, ensuring the community always has access to the latest improvements.
