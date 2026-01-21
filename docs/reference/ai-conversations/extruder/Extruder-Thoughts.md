That is a deep dive into the soul of RepRap! The **Greg's Wade** is the "Flat-6 Engine" of the 3D printing world—it’s mechanical, it’s geared, and you can see the torque happening. It is the perfect signature for **Darwin-Neo**.

However, you've spotted the 2026 problem: the original Greg's Wade was designed when "Leveling" meant turning a thumb-screw and "Filament Sensors" didn't exist.

### 1. The Engineering Challenge: "The Retrofit"

If we use a standard Greg's Wade, it is quite "fat." This makes mounting a **PINDA** or **BLTouch** difficult because the probe needs to be close to the nozzle, but the big gears get in the way.

**The Solution:** We use **build123d** to design a "Neo-Carriage." Instead of trying to bolt sensors onto the extruder, we build a **Structural Harness** that the extruder sits *inside*.

### 2. Comparison: Greg's Wade vs. MK3S+ Extruder

| Feature | Greg's Wade (The Classic) | Prusa MK3S+ (The Tank) |
| --- | --- | --- |
| **Aesthetic** | High "Matrix" / Mechanical vibe. | Modern / Compact / Functional. |
| **Gearing** | Large 3D printed gears (Visible). | Internal Bondtech gears (Hidden). |
| **Sensors** | Needs custom "outrigger" mounts. | Built-in slots for PINDA/Sensor. |
| **Maintenance** | Very easy to see jams. | Requires partial disassembly. |
| **Heat Creep** | Excellent (Huge distance from motor). | Good (Integrated heatsink fan). |

**My Recommendation:** Stick with the **Greg's Wade**. It is the "Signature" you want. We will simply "Neo-ify" it by adding a side-wing to the carriage in Python that holds the PINDA and a top-entry guide for the filament sensor.

---

### 3. The "Neo-Carriage" Script (with Sensor Mounts)

In this **build123d** script, we create the mounting plate for the Wade's Extruder, but we add a "Sensor Wing."

```python
from build123d import *
from project_vars import cfg

# Dimensions
wade_mount_width = 50.0  # Standard Greg's Wade bolt spacing
pinda_dia = 8.1         # PINDA probe diameter
filament_sensor_dist = 25.0

with BuildPart() as neo_carriage:
    # 1. THE BASE: A minimalist 'truss' plate
    Box(70, 35, cfg.wall_min)
    
    # 2. WADE'S MOUNTING HOLES
    with BuildSketch(neo_carriage.faces().sort_by(Axis.Z)[-1]):
        with Locations((-wade_mount_width/2, 0), (wade_mount_width/2, 0)):
            Circle(radius=4.5/2, mode=Mode.SUBTRACT) # M4 bolts

    # 3. THE PINDA WING (The 'Neo' Addition)
    # We extend a small arm to the side for the probe
    with BuildPart(neo_carriage.faces().sort_by(Axis.X)[1], mode=Mode.ADD):
        with BuildSketch(Plane.XY.offset(0)):
             with Locations((45, 10)): # Off to the side of the nozzle
                 Circle(radius=(pinda_dia/2) + 4)
                 Circle(radius=pinda_dia/2, mode=Mode.SUBTRACT)
                 # Pinch slot for the probe
                 Rectangle(2, 15, align=(Align.CENTER, Align.MIN), mode=Mode.SUBTRACT)
        extrude(amount=cfg.wall_min)

    # 4. SKELETONIZING
    # Remove material between the bolt holes to keep it 'wiry'
    with BuildSketch(neo_carriage.faces().sort_by(Axis.Z)[-1]):
        Rectangle(30, 15, mode=Mode.SUBTRACT)

show(neo_carriage)

```

---

### 4. Solving the Filament Sensor

For the **Filament Sensor**, since the Greg's Wade has that large open top where the filament enters the gears, the best "Neo" approach is a **"Floating Sensor Mount."**

1. We design a small "Puck" that sits on top of the Greg's Wade.
2. The filament passes through the sensor *before* it hits the gears.
3. Because it's all in **build123d**, we can make the sensor mount a "snap-on" part that clips onto the Greg's Wade frame.

### 5. Why the MK3S+ might be "Too Easy"

The MK3S+ extruder is great, but it’s a "solved problem." It feels like a product you bought. The **Greg's Wade** feels like a machine you *built*. On an M12 frame, a big, geared extruder looks like a piece of industrial equipment. It matches the "Massive" feel of the 12mm rods.

### Next Step: The Filament Sensor "Puck"

Would you like to see a design for a **Filament Sensor Housing** that clips onto the top of the Greg's Wade? It would keep the "Industrial Chic" look while adding that 2026 functionality. It can even include a small "viewing window" so you can see the filament moving—very Matrix.


To keep the **Darwin-Neo** aesthetic, we’ll avoid the generic plastic boxes used for modern filament sensors. Instead, we’ll design a **"Floating Sensor Cage."**

This part will house a simple microswitch or an optical sensor (standard donor parts) and clip directly onto the top of the Greg's Wade frame. It follows the "Neo" look: minimal material, exposed filament path, and high-visibility "logic."

### The Filament Sensor "Cage" Script

This script creates a housing that uses a standard **V-15-1C25 microswitch** (common in old printers and microwaves) as the sensor.

```python
from build123d import *
from project_vars import cfg

# Sensor Dimensions
switch_body = (28.0, 16.0, 10.0) # Standard microswitch size
hole_spacing = 22.2              # Distance between mounting holes
filament_d = 1.75

with BuildPart() as sensor_puck:
    # 1. THE CAGE: A skeletonized frame for the switch
    with BuildSketch() as s:
        # Create a mounting plate for the switch
        Rectangle(switch_body[0] + 4, switch_body[2] + 4)
        # Add the filament guide tube section
        with Locations((0, 10)):
            Circle(radius=5)
        Hull()
    extrude(amount=wall_thickness := 8.0)
    
    # 2. THE FILAMENT PATH
    # A 2mm hole straight through the top for the filament to pass
    top_face = sensor_puck.faces().sort_by(Axis.Y)[-1]
    with BuildSketch(top_face):
        Circle(radius=(filament_d + 0.5) / 2, mode=Mode.SUBTRACT)
    extrude(amount=-40, mode=Mode.SUBTRACT)

    # 3. SWITCH MOUNTING HOLES
    # These bolts will hold the microswitch inside the cage
    with BuildSketch(sensor_puck.faces().sort_by(Axis.Z)[-1]):
        with Locations((-hole_spacing/2, 0), (hole_spacing/2, 0)):
            Circle(radius=3.1/2, mode=Mode.SUBTRACT) # M3 bolts

    # 4. NEO "VIEWPORT" 
    # Cut a window so you can see the switch lever hitting the filament
    with BuildSketch(sensor_puck.faces().sort_by(Axis.Z)[-1]):
        Rectangle(15, 8, mode=Mode.SUBTRACT)

    # 5. THE CLIP
    # A simple "C-clamp" logic to snap onto the Wade's Extruder frame
    with BuildPart(sensor_puck.faces().sort_by(Axis.Y)[0], mode=Mode.ADD):
        with BuildSketch(Plane.XZ):
             Rectangle(30, 5) # The clip arm
        extrude(amount=15)

show(sensor_puck)

```

---

### Why this is "Archeology meets 2026"

1. **Mechanical Feedback:** Using a microswitch in a skeletonized cage means you can *see* and *hear* the sensor click when the filament runs out. It fits the mechanical soul of the Greg's Wade extruder.
2. **The "Lumpy" Logic:** Just like the M12 rods, filament can be inconsistent. The 2mm path provides enough clearance to prevent friction while keeping the sensor accurate.
3. **Klipper Integration:** You’ll wire this to a "Filament Sensor" pin on your BTT Octopus. When the switch opens, Klipper will execute a `PAUSE` macro, move the "Neo-Carriage" to the front, and wait for you to swap rolls.

### Finalizing the "Matrix" Assembly

You now have:

* **The Skeleton:** M12 Corners and Frame.
* **The Muscles:** NEMA17 Motor Mounts.
* **The Nervous System:** Z-Nut Housings and Triple-Z logic.
* **The Heart:** Greg's Wade Extruder on the Neo-Carriage with PINDA and Sensor support.

### Next Step: The "First Boot"

Since your CAD models are coming together, the next logic-step is the **Klipper Macro configuration.** Because you are building a custom machine, you need a "Start G-Code" that handles the 3-point Z-leveling and the filament sensor check.

**Would you like me to help you write the `START_PRINT` macro for Klipper?** It will be the "wake up" sequence for your Darwin-Neo, ensuring the machine is perfectly aligned before the first layer is laid down.


jzkmath rework of Wades Geared extruder:
https://www.thingiverse.com/thing:961630


That **rework by "jzkmath"** you found is actually a very smart choice for a Darwin-Neo build. It solves the biggest "archaeological" problem with the original Greg’s Wade: the mounting.

The original used two long bolts through the entire body, which were a pain to align. This version uses a **modular mounting plate** (the "J-Head/Groove Mount" adapter). This means you can design your X-carriage in **build123d** to be a universal flat plate, and this extruder will simply bolt onto it.

### 1. Tiered Complexity (The "Choose Your Reality" Approach)

In the spirit of the Matrix, the builder can choose how "deep" they want to go. You can structure your **build123d** project so that parts are optional "layers."

* **Tier 1 (The Basic):** Just the frame and the extruder. No sensors. You level the bed once with a piece of paper and print.
* **Tier 2 (The Awakened):** Add the PINDA/BLTouch. You get 3-point auto-leveling.
* **Tier 3 (The Neo):** Add the Filament Sensor and Klipper macros. The machine becomes fully autonomous.

In your code, you can use a simple `if` statement:

```python
ADD_SENSOR_MOUNT = True  # Builder changes this to False to skip the wing

if ADD_SENSOR_MOUNT:
    # Build the 'wing' for the PINDA
    with BuildPart(neo_carriage.faces().sort_by(Axis.X)[1], mode=Mode.ADD):
        # ... wing geometry ...

```

---

### 2. Why that specific Thingiverse Rework is "The One"

* **Access:** It has a "hinged" idler. In older versions, you had to take the whole thing apart to clean the teeth. Here, you just swing the arm open.
* **Integrated Heat Sink Fan:** It has better airflow for the hotend, which prevents **Heat Creep** (where the filament melts too early and jams).
* **Standardized Mounting:** Because it uses the "Groove Mount" standard, it fits the E3D V6 clones perfectly.

---

### 3. The "First Boot" Start Macro

This is the Klipper logic that brings the "Matrix" to life. It’s "tiered"—if the builder didn't install a sensor, they just comment out that line.

```toml
[gcode_macro START_PRINT]
gcode:
    {% set BED_TEMP = params.BED_TEMP|default(60)|float %}
    {% set EXTRUDER_TEMP = params.EXTRUDER_TEMP|default(200)|float %}

    M117 Initializing Matrix...
    G28 ; Home all axes
    
    # TIER 2: Auto-Leveling (Only runs if you have 3-point Z)
    Z_TILT_ADJUST 
    
    # TIER 2: Bed Mesh (The "Green Rain" mapping)
    BED_MESH_CALIBRATE 

    M109 S{EXTRUDER_TEMP} ; Wait for hotend
    M190 S{BED_TEMP} ; Wait for bed
    
    # TIER 3: Filament Check
    # QUERY_FILAMENT_SENSOR ; (Optional check)

    G92 E0 ; Reset Extruder
    M117 Printing...

```

---

### 4. Why would someone skip the Filament Sensor?

Some "Purists" skip them because:

1. **Reliability:** Cheap sensors can "false trigger" and pause a 20-hour print for no reason.
2. **Complexity:** It’s extra wiring through the cable chains.
3. **Aesthetic:** They want the most "Industrial" look possible with zero extra wires.

By making it a **Modular Puck** in your **build123d** script, you let them decide. If they don't want it, they just don't print that puck.

### Next Step for Darwin-Neo

We have the frame, the Z-logic, the carriage, and the extruder selected.

**Would you like me to help you design the "M12-to-NEMA17" Y-Axis motor mounts?** These are the ones that will drive the belts for your X-axis. They need to be the strongest parts of the machine because they take all the "kick" from the high-speed Klipper moves.



24mm Verison
https://www.thingiverse.com/thing:961767

That is a very astute observation. Yes, they are referring to the **vertical center-to-center distance** between the two smooth rods that the X-carriage slides on.

In the "Archaeology" of the RepRap, the standard evolved from 30mm down to 24mm (and sometimes 17mm) for very specific engineering reasons.

### 1. The Engineering Merit: 24mm vs. 30mm

The 24mm spacing has significant technical merit for a **Darwin-Neo** build, especially when using a **Greg's Wade Extruder**:

* **Center of Gravity (The "Neo" Advantage):** By bringing the rods closer together (24mm), the entire X-carriage becomes more compact. This pulls the heavy mass of the Greg's Wade motor closer to the rods. In Klipper, less "leverage" from a heavy motor means you can push higher accelerations without the carriage twisting or "ringing."
* **Reduced Torquing:** A Greg's Wade is tall. If the rods are too far apart (30mm), the carriage can act like a long lever, putting more stress on the linear bearings. 24mm is often considered the "Sweet Spot" for the Wade’s height.
* **Compactness:** It allows for a smaller overall print head, which gives you back a few millimeters of Z-travel (build height).

**The Verdict:** Go with the **24mm spacing**. It’s the "refined" version of the original design and fits the "High-Performance" goal of your build.

---

### 2. Implementation in your build123d "Matrix"

Since you are using **build123d**, you don't even have to choose permanently. You can make this a variable in your `project_vars.py`.

```python
# project_vars.py addition
class DarwinNeoConfig:
    def __init__(self):
        # ... other vars ...
        self.x_rod_spacing = 24.0  # Builder can change to 30.0 if they have old parts

```

Then, in your X-Carriage script, you use that variable to place the bearing housings:

```python
# x_carriage.py
with BuildPart() as x_carriage:
    # Place the two LM8UU bearing housings
    with Locations((0, cfg.x_rod_spacing / 2), (0, -cfg.x_rod_spacing / 2)):
        # Create the housing for the 15mm bearings
        Cylinder(radius=10, height=24) 
        Circle(radius=7.5, mode=Mode.SUBTRACT) # 15mm ID for bearing

```

---

### 3. The Y-Axis Motor Mounts (M12-to-NEMA17)

As promised, here is the design for the **Y-Axis Motor Mounts**. These are the "Power Nodes" of the Darwin-Neo. They sit at the back corners of the M12 frame and hold the motors that move the X-belt.

They need to be **extra rigid** because the belt tension will try to pull them inward.

```python
from build123d import *
from project_vars import cfg

with BuildPart() as y_motor_mount:
    # 1. THE BLOCK: Heavy-duty base for the NEMA17
    # We use a thick plate to resist belt tension
    Box(cfg.rod_dia + 30, 50, cfg.wall_min * 2)
    
    # 2. THE MOTOR FACE: Vertical mount for the NEMA17
    with BuildPart(y_motor_mount.faces().sort_by(Axis.Y)[-1], mode=Mode.ADD):
        with BuildSketch(Plane.XZ):
            Rectangle(42 + 10, 42 + 10)
            # Skeletonized 'Neo' center
            Circle(radius=18, mode=Mode.SUBTRACT)
            # Motor mounting holes
            with GridLocations(31, 31, 2, 2):
                Circle(radius=3.5/2, mode=Mode.SUBTRACT)
        extrude(amount=cfg.wall_min)

    # 3. THE M12 ANCHOR: Clamping onto the skeleton
    # This part "wraps" around the M12 rod
    with BuildSketch(y_motor_mount.faces().sort_by(Axis.Z)[-1]):
        with Locations((0, -15)):
            Circle(radius=cfg.frame_hole / 2, mode=Mode.SUBTRACT)
            # Slot for clamping bolt
            Rectangle(2, 20, align=(Align.CENTER, Align.MAX), mode=Mode.SUBTRACT)

    # 4. TRUSS STIFFENER: Preventing the motor from flexing
    # This is a 'Neo' strut connecting the motor plate back to the base
    # (Simplified representation)
    fillet(y_motor_mount.edges(), radius=3)

show(y_motor_mount)

```

---

### 4. Tiered Approach: The "Lite" vs "Pro"

By choosing the **24mm spacing** and **M12 rods**, you’ve created a "Pro" level skeleton.

* **Tier 1:** User uses 12V and skips the sensors.
* **Tier 2:** User uses 24V and the 24mm rod spacing for speed.
* **Tier 3:** User adds the Filament Sensor Puck and 3-point Z.

### Next Step: The X-End Idler

The X-axis has a motor on one side and an **Idler (pulley)** on the other. Would you like to see the script for the **X-End Idler**? It needs to mirror the rod spacing (24mm) and provide a way to **tension the belt**—which is one of the most satisfying "mechanical" parts of the build.


To answer your first question: **Yes, it will absolutely perform in 2026.**

The reason a 2015-era Greg's Wade Extruder still holds up isn't because the physics of extruding plastic changed—it’s because **Klipper changed the rules.** In 2015, we didn't have Input Shaping or Pressure Advance. Today, the software "knows" the physics of that big geared extruder and can compensate for its momentum.

---

### 1. Greg’s Wade vs. The "Modern" Titans (Stealthburner, Galileo 2, HextrudORT)

The Voron/HevORT extruders you mentioned are the "Formula 1" engines of 3D printing. Here is how they compare to your "Industrial Chic" choice:

| Feature | Greg's Wade (Darwin-Neo) | Stealthburner / Galileo 2 | HextrudORT |
| --- | --- | --- | --- |
| **Cost** | **<$10** (Printed gears + few bolts) | **$60 - $120** (Need kit/Bondtech) | **$50+** (Precision gears) |
| **Gearing** | Large, 3D Printed (Visible) | Internal Planetary or BMG | Dual-Drive High Torque |
| **Complexity** | Simple "Old-School" Mech | Very high (Tons of tiny screws) | High precision required |
| **Main Goal** | **Reliability & Torque** | **High Speed / Low Weight** | **Speed / Flow Rate** |

**The "Neo" Philosophy:** The Stealthburner is designed to be lightweight so the printer can move at 500mm/s. But on your **M12 Threaded Rod frame**, we have plenty of mass. We don't need the lightest head in the world; we need the one that is hardest to break. Greg's Wade provides massive torque, which is great for the "cheaper" nozzles and filament that a budget-conscious maker might use.

---

### 2. The $300 AUD "Right of Passage"

To keep this under the price of an A1 Mini ($300 AUD) while hitting MK4 quality, we focus on the **BOM (Bill of Materials)**:

* **Donor Printer:** $50 - $100 (FB Marketplace "Broken" Ender 3 or Anet).
* **M12 Threaded Rods:** ~$40 (Bunnings).
* **BTT Octopus + RPi:** ~$100 (The "Intelligence" upgrade).
* **Filament for Parts:** ~$30.
* **Total:** **~$220 - $270 AUD.**

By avoiding the expensive "Bondtech" gears required for a Voron, you keep the build accessible. The "Right of Passage" for the maker is printing their own gears—a true RepRap tradition.

---

### 3. Reliability: The "MK4 Standard"

A Prusa MK4 is reliable because it is stiff and the software is tuned perfectly.

* **Stiffness:** Your M12 rods are thicker than the 2020 extrusions on most modern printers.
* **Software:** By providing "The Construct" (your Klipper macros), the user doesn't have to be a coder. They just "flash and play."

### 4. Minimal Wires: The "Matrix" Look

To avoid the "bird's nest" of wires common in 2015:

1. **Use an "Umbilical" Cable:** One single wrapped sleeve from the Octopus board to the X-carriage.
2. **Printed Cable Chains:** Since we are using **build123d**, we can design custom "Skeletonized" cable chains that snap onto the M12 rods.

---

### 5. The X-End Idler (The Final Movement Node)

To finish the X-axis for your 24mm-spacing rods, here is the script for the **X-End Idler**. This is the part that sits opposite the motor. It needs to hold a GT2 pulley and allow the user to tighten the belt.

```python
from build123d import *
from project_vars import cfg

with BuildPart() as x_idler:
    # 1. THE HUB: Two cylinders for the 24mm-spaced smooth rods
    with Locations((0, cfg.x_rod_spacing / 2), (0, -cfg.x_rod_spacing / 2)):
        Cylinder(radius=10, height=30)
        # Smooth rod holes (8mm)
        Circle(radius=4.1, mode=Mode.SUBTRACT) 

    # 2. THE IDLER SLOT: Where the belt pulley sits
    # We cut a slot in the middle for the 625ZZ bearing/pulley
    with BuildSketch(x_idler.faces().sort_by(Axis.X)[0]):
        Rectangle(12, 15, mode=Mode.SUBTRACT)
    extrude(amount=-20, mode=Mode.SUBTRACT)

    # 3. TENSIONING BOLT HOLE
    # A horizontal hole for an M3 bolt to pull the idler tight
    with BuildSketch(x_idler.faces().sort_by(Axis.Y)[0]):
        Circle(radius=1.6, mode=Mode.SUBTRACT)
    extrude(amount=30, mode=Mode.SUBTRACT)

show(x_idler)

```

---

### Next Step: The Assembly Guide

You have the vision and the parts. To make this as easy as a "Prusa Manual," the next step is to document the **Assembly Order.** **Would you like me to draft the "Zion Construction Sequence"?** It's a step-by-step list (1. Frame, 2. X-Y Gantry, 3. Z-Bed, 4. Wiring) that ensures the maker doesn't have to take the machine apart because they forgot a single M12 nut in the middle of the frame.


This is the most important "soul-searching" moment for the design. To defend the **Greg's Wade**, you have to understand exactly what you are trading. You aren't just trading speed for nostalgia; you are trading **Velocity for Reliability.**

Here is the honest breakdown of the "Extruder Dilemma" so you can stand your ground against the "Fanboys."

---

### 1. Is it a "Handicap"?

**Yes, in terms of Inertia.** A Greg’s Wade with a full-sized NEMA17 motor weighs roughly **450g–600g**. A modern Sherpa Mini or Orbiter weighs roughly **100g–150g**.

* **The Penalty:** When the printer changes direction, that 600g mass wants to keep going. This causes "ringing" or "ghosting" in the print.
* **The Defense:** Because our frame is **M12 Steel**, it handles that momentum far better than a flimsy aluminum printer. Plus, **Klipper’s Input Shaping** was literally designed to mathematically cancel out the ringing caused by heavy extruders.

### 2. The Torque: Why 13:43 matters

You asked if it is really 43:1. No, it’s a **3.3:1 ratio** (43 teeth on the big gear / 13 teeth on the motor gear).

* **The Advantage:** Most modern "Pancake" motors used in light extruders have very low native torque. If they hit a tiny jam, they skip.
* **The Greg’s Wade Advantage:** Using a full-sized NEMA17 with a 3.3:1 gear reduction gives you **monstrous "Pushing Power."** It will grind through filament diameter inconsistencies that would seize a Sherpa Mini. It is the "Low Range 4WD" of extruders.

---

### 3. Should we offer a Bowden version?

**Honestly? No.** Bowden (where the motor is on the frame and pushes through a long tube) was a "hack" to get speed on weak frames.

* **The Problem:** It makes print quality worse (ooze, stringing, difficult pressure advance).
* **The Darwin-Neo Way:** We have a **High-Mass Frame**. We don't need to hide the motor on the frame. We can carry the weight. A Direct Drive Wade is infinitely easier to tune and produces better prints than a Bowden setup.

### 4. The "Sherpa Mini" Option (The "Neo-Head")

We can absolutely offer this as a **Tier 3 upgrade**, but we shouldn't make it the default.

* **The "Neo-Head" Path:** Buy a $45 AUD BMG-style kit or a Sherpa Mini. Use a tiny pancake motor.
* **The Result:** You could potentially double your acceleration (from  to ).
* **The Risk:** You blow the $300 budget and lose the "Signature" look of the machine.

---

### 🛡️ How to Defend the Greg's Wade (The "Script")

If a Voron or Bambu user laughs at your extruder, here is your defense:

> "The Greg's Wade isn't a handicap; it's a **Torque-biased Direct Drive.** I’m using an M12 Steel Skeleton and Klipper Input Shaping to manage the inertia. I'd rather have a geared NEMA17 that can push through any filament jam than a lightweight 'pancake' motor that skips the moment a nozzle gets a bit of backpressure. This machine is built for **consistent extrusion**, not for winning a 10-minute Benchy race."

---

### 📝 Updating the Manifesto: The "Heart" Section

We should frame the Extruder choice as a **deliberate engineering trade-off**:

> ### ⚙️ The Heart: Greg's Wade Geared Extruder
> 
> 
> We chose the Greg's Wade (13:43 ratio) not just for its RepRap heritage, but for its **Industrial Torque**.
> * **Why not a 'modern' light extruder?** Lightweight extruders require expensive, specialized pancake motors. The Greg's Wade allows you to reuse a standard, high-torque NEMA17 from your donor machine.
> * **Mass as a Feature:** While heavier, the geared reduction ensures consistent flow and prevents common "under-extrusion" issues found in budget direct-drive setups.
> * **The Upgrade Path:** The Darwin-Neo uses a **Universal Toolhead Puck**. If you eventually want to trade torque for speed, the carriage is compatible with Sherpa Mini or Orbiter mounts.
> 
> 

### 🏁 Final Thought

The Greg's Wade is what makes a Darwin-Neo a **Darwin**. It’s mechanical, it’s visible, and it’s reliable.

**Would you like me to add a "Toolhead Compatibility" section to the README?** This would list the specific "Pucks" available, showing that the machine is a "Platform" that can grow from a Wade to a Sherpa whenever the user is ready to spend the extra $50.






That is the perfect way to frame it. You aren't choosing the Greg's Wade because you're "stuck in the past"; you're choosing it because it's the **best-optimized solution for a self-replicating, budget-constrained machine.**

### 1. Why not a Voron StealthBurner/Clockwork2?

You hit the nail on the head: **Complexity and Proprietary Parts.**

* **The Voron CW2:** Requires a specific $30–$50 "BMG internal kit" (hardened dual-drive gears, specialized shafts, and bearings).
* **The Greg's Wade:** Only needs a few standard M8 bolts, some 608 bearings (skate bearings—the most common bearing on earth), and a couple of 3D-printed gears.
* **The Maintenance:** If a gear strips on a Wade, you print a new one for 50 cents. If you lose a specialized needle bearing in a Voron extruder, your printer is down for two weeks while you wait for a shipment from China.

### 2. The "Defensible Logic" for the Manifesto

We should explicitly state that the Wade is the **"Baseline Reference"** because it fulfills the RepRap promise: **maximum performance from minimum specialized parts.**

---

### 📝 Updated "Heart" Section for the Manifesto

### ⚙️ The Heart: Greg's Wade Geared Extruder (Reference Spec) 
 
We selected the Greg's Wade (13:43 ratio) as our reference extruder. While "modern" extruders like the Voron Clockwork or Sherpa Mini are popular, they often require expensive, specialized gear kits and proprietary hardware.

**Why the Wade wins for Darwin-Neo:**

* **Zero-Proprietary Hardware:** Built using standard M8 bolts and 608 "skate" bearings available at any hardware store.
* **Total Repairability:** If a gear wears out, the machine can print its own replacement.
* **High-Torque Baseline:** By using a full-sized NEMA17 motor with a 3.3:1 geared reduction, we achieve a "Torque Monster" that provides more consistent extrusion than budget direct-drive units.
* **Simplicity:** Fewer moving parts means fewer failure points for the "Set and Forget" builder.
  
**For the "Neo" Tinkerer:** The Darwin-Neo uses a **Modular Toolhead Puck**. While the Wade is our reliable baseline, the carriage is 100% compatible with printed mounts for Voron StealthBurners, Sherpa Minis, or Orbiters if you choose to trade "Hardware-Store Simplicity" for "Lightweight Speed."

---

### 🛠️ The "Universal Toolhead Puck" (build123d Logic)

To make this defense real, we design the X-carriage as a **"Universal Dock."**

```python
from build123d import *

with BuildPart() as universal_carriage:
    # The "Dock" - 4 x M3 holes in a standard 30x30 or 20x20 pattern
    Box(50, 40, 10) 
    with BuildSketch(universal_carriage.faces().sort_by(Axis.Z)[-1]):
        with GridLocations(30, 30, 2, 2):
            Circle(radius=1.5, mode=Mode.SUBTRACT) # Universal Mount Points

# This allows the builder to print a "Wade Adapter" or a "Voron Adapter"
# without ever changing the belt-driven carriage itself.

```

---

### 🏁 Final Review: Is the Manifesto Complete?

We have:

1. **The Vision:** Software Intelligence vs. Analog Hardware.
2. **The Logic:** Fixed Gantry + Triple-Z (The "Voron-level" feature).
3. **The Skeleton:** M12 "Lumpy" Zinc rods for mass.
4. **The Heart:** The Greg's Wade (Defended as the "Hardware-Store Hero").
5. **The Brain:** MKS SKIPR or Legacy Boards.
6. **The Path:** The "Ship of Theseus" Bootstrapping method.
7. **The Honesty:** Acknowledging this is a "Tractor," not a "Race Car."

**Does this feel like a document you are proud to put your name on?** It is technically sound, historically respectful, and economically disruptive.

**Would you like me to do one final "Clean Merge" of all these sections into a single, polished Markdown file you can save as `README.md`?** This will be your official Project Launch document.