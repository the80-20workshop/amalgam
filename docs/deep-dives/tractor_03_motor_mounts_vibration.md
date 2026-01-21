# The Tractor: Motor Mounts & Vibration Control

## Overview

"The Tractor" addresses motor vibration through strategic mounting: Z-motors sink into the massive MDF base for mass damping, while X and Y motors use "Sandwich Mounts" with rubber isolation. This document covers mount designs, vibration control, and the Triple-Z bed system.

---

## Vibration Control Philosophy

### The Problem

Stepper motors generate high-frequency vibrations during rapid direction changes. In a threaded-rod frame (especially M10/M12 steel), these rods can act like tuning forks, amplifying motor noise into audible "singing."

### The Tractor Solution

A two-pronged approach:

1. **Mass Damping (Z-Motors):** Mount directly to 36mm MDF "Anvil"
2. **Mechanical Isolation (X/Y Motors):** Sandwich mount with rubber grommets
3. **Software Compensation:** Klipper Input Shaping

---

## Strategy B: The Sandwich Mount

### Why Sandwich Over Simple Gasket?

**Strategy A (Flat Gasket):** Motor pressed against rubber, but screws pass directly through to frame. Under belt tension, rubber compresses and vibration travels through metal screws.

**Strategy B (Sandwich Mount):** Motor bolts to a "Sub-Plate." That plate mounts to frame using rubber grommets. Motor screws and frame screws never touch each other. **True mechanical isolation.**

### How It Works

```
[MOTOR]
   ↓ (M3 bolts)
[SUB-PLATE] ←── Small printed plate
   ↓ (through rubber grommets)
[FRAME BRACKET] ←── Main corner/anchor
   ↓
[M10 THREADED ROD FRAME]
```

The motor's vibration path:
1. Motor → Sub-Plate (rigid connection)
2. Sub-Plate → Rubber → Frame Bracket (damped)
3. The frame never "feels" the motor directly

### Advantages for The Tractor

- **Handles Belt Tension:** Sub-plate distributes load; rubber doesn't get crushed unevenly
- **Thicker Rubber Possible:** Not limited to thin gaskets
- **Scavenger Friendly:** Uses standard hardware store grommets
- **Industrial Aesthetic:** Looks like proper machinery

---

## Sourcing Rubber Grommets

### Hardware Store Options

You don't need "3D printer grommets"—standard electrical/plumbing parts work perfectly:

| Source | Product | Notes |
|--------|---------|-------|
| Electrical Aisle | Wiring Grommet Assortment | Various sizes, rubber |
| Electrical Aisle | IP68 Cable Glands | Use just the rubber insert |
| Plumbing Aisle | Rubber Tap Washers | Sandwich between two washers |
| Bike Shop | Old Inner Tubes | Layer for custom thickness |

### Scavenger Sources

- **PC Power Supplies:** Wire pass-through grommets
- **Microwave Ovens:** Chassis wire grommets
- **Any Appliance:** Where wires pass through metal panels

**The "Tap Washer" Alternative:**
If you can't find grommets, sandwich the printed bracket between two rubber tap washers from plumbing section.

---

## Sandwich Mount: Printed Parts

### Part 1: The Frame Bracket (Socket)

This is your main anchor that clamps to the M10 frame. Instead of small precise holes, it has large 10mm sockets for grommets.

```python
# Frame Bracket with Grommet Sockets
grommet_hole = 10.0  # Standard rubber grommet OD

with BuildPart() as frame_bracket:
    # 1. Core frame clamping logic
    # [M10 rod sleeves, etc.]
    
    # 2. Grommet Sockets (instead of M3 holes)
    with BuildSketch(face.sort_by(Axis.X)[-1]) as s:
        for loc in GridLocations(31, 31, 2, 2):
            with Locations(loc):
                Circle(grommet_hole / 2)  # 10mm holes
    extrude(amount=-15, mode=Mode.SUBTRACT)
```

**Why Large Holes Help Donor Printers:**
- 10mm circles are much easier to print than precise 3mm holes
- Rubber grommet hides any "lumpy" print imperfections
- Grommet squishes to fill gaps

### Part 2: The Sub-Plate (Plug)

Simple flat plate that bolts directly to the motor:

```python
# Motor Sub-Plate
plate_size = 42.5  # NEMA 17 footprint
hole_spacing = 31.0

with BuildPart() as sub_plate:
    with BuildSketch() as s:
        Rectangle(plate_size, plate_size)
        # Motor mounting holes (M3)
        for loc in GridLocations(hole_spacing, hole_spacing, 2, 2):
            with Locations(loc):
                Circle(1.7)  # M3 clearance
        # Center hole for motor boss/pulley
        Circle(12)
    extrude(amount=5)
```

This is the **easiest possible shape** to print:
- No supports needed
- Won't warp easily
- Perfect "warm-up" print for donor machines

---

## Assembly: The Sandwich

### Hardware Required

Per motor:
- 1× Sub-Plate (printed)
- 4× Rubber Grommets (10mm OD)
- 4× M3×25 or M3×30 bolts (longer than normal)
- 4× M3 nuts
- 4× M3 washers (optional, helps distribute load)

### Step-by-Step

1. **Create Motor Assembly:**
   - Bolt NEMA 17 to Sub-Plate using standard M3×8 motor screws
   - This is now your "Motor Module"

2. **Install Grommets:**
   - Push rubber grommets into the 10mm holes on Frame Bracket
   - They should fit snugly

3. **Connect the Sandwich:**
   - Pass long M3 bolts through Sub-Plate
   - Through center of rubber grommets
   - Through Frame Bracket
   - Secure with nuts on back side

4. **Tension Check:**
   - Bolts should compress grommets slightly
   - Motor should "float" with slight give
   - No metal-to-metal contact anywhere

### The "Double-Nut Hack" (No Sub-Plate)

If you want Strategy B without printing the sub-plate:

1. Put long M3 screw into motor
2. Thread a nut onto screw, tighten against motor
3. Slide on rubber washer
4. Slide on printed bracket
5. Add another rubber washer
6. Final nut on the end

**Result:** Bracket sandwiched between rubber washers; screw only touches rubber as it passes through.

---

## Z-Motors: Mass Damping

### The "Anvil" Mount

Z-motors don't need sandwich mounts—they're bolted directly to the 36mm MDF base. The wood's mass absorbs vibration.

**Why This Works:**
- Z-motors move in small steps (layer height)
- They're the "least busy" motors
- Drop one layer, then all X-Y stuff happens
- MDF is "lossy"—converts vibration to heat

### Under-Mount Configuration

Motors mount to the **underside** of the MDF:

```
[MDF BASE - 36mm thick]
        ↓
    [COUPLER]
        ↓
  [NEMA 17 Z-MOTOR]
```

**Benefits:**
- Lowers center of gravity further
- Hides motors and wiring (cleaner look)
- MDF acts as sound baffle (near-silent Z-moves)

### Triple-Z Layout

For a 235×235mm bed, three motors in isosceles triangle:

| Position | X Coordinate | Y Coordinate |
|----------|--------------|--------------|
| Front Left | 20mm from left | 20mm from front |
| Front Right | 20mm from right | 20mm from front |
| Rear Center | Center (117.5mm) | 20mm from back |

This creates the most stable plane for Klipper's `z_tilt_adjust`.

---

## Kinematic Z-Joints

### The Problem: Binding

If three Z-rods aren't perfectly parallel (to the nanometer), a rigid bed mount will:
- Fight the motors
- Cause skipped steps
- Leave artifacts on prints

### The Solution: Decoupling

Separate the **movement** (lead screw) from the **constraint** (smooth rod).

### The "Ball-and-Cup" Joint

A scavenger-friendly kinematic coupling:

1. **Nut Carrier:** T8 lead screw nut bolted to small printed part
2. **The Ball:** 6mm or 8mm steel ball (from bearing) sits on carrier
3. **Bed Bracket:** Has a conical "cup" that rests on the ball

**How It Works:**
- Gravity holds bed down on balls
- If lead screw is slightly tilted, ball shifts in cup
- No bending forces transferred to bed or lead screw

### build123d: Kinematic Bracket

```python
# Kinematic Z-Bracket (LM8UU + Floating Nut)
bearing_od = 15.0  # LM8UU
bearing_len = 24.0

with BuildPart() as z_bracket:
    # 1. Rigid Carriage (slides on M8 smooth rod)
    with BuildSketch() as s:
        Rectangle(bearing_od + 10, bearing_len + 10)
    extrude(amount=20)
    
    # Bearing Bore
    # [LM8UU housing logic]
    
    # 2. Floating Cup Interface
    with BuildSketch(face.sort_by(Axis.Z)[-1]) as s3:
        with Locations((25, 0)):  # Offset from smooth rod
            Circle(10)  # Cup base
    extrude(amount=10)
    
    # Conical cup (90° countersink) for kinematic seat
    # [Chamfer or revolve to create cone]
```

### Mixing M8 and M10 Rods

If your donor provides M8 smooth rods:

- **Z-Verticals:** M8 smooth rods for Z-guides
- **Frame:** Stay with M10 threaded for structure
- **Brackets:** Have both 10.5mm (frame) and 8.2mm (Z-rod) holes

**Note:** M8 rods may flex more than M10. Triple-Z and kinematic joints compensate for this.

---

## Klipper Input Shaping

### How It Complements Hardware Isolation

Even with rubber mounts, some vibration reaches the frame. Klipper handles this in software:

1. **Attach ADXL345** accelerometer to carriage (~$5)
2. **Run Calibration:** Printer shakes at different frequencies
3. **Klipper Calculates:** Mathematical "anti-vibration" signal
4. **Real-time Compensation:** Motor pulses offset to cancel resonance

**Result:** Even if frame rings, Klipper "shapes" movement to never excite those frequencies.

### Configuration

In `printer.cfg`:

```ini
[adxl345]
cs_pin: ...  # Your pin

[resonance_tester]
accel_chip: adxl345
probe_points: 117.5, 117.5, 20  # Center of bed

[input_shaper]
# Auto-calibrated values go here
```

### StealthChop vs SpreadCycle

For TMC drivers:

| Mode | Use For | Why |
|------|---------|-----|
| StealthChop | X-motor | Quieter, lighter load |
| SpreadCycle | Y-motors (dual) | More torque for heavy gantry |
| SpreadCycle | Z-motors | Holding torque for bed |

---

## The "Quiet Tractor" Specification

| Axis | Mount Style | Damping Method |
|------|-------------|----------------|
| X | Sandwich Mount | Strategy B (Rubber Grommets) |
| Y (Dual) | Sandwich Mount | Strategy B (Rubber Grommets) |
| Z (Triple) | MDF Rigid Mount | Mass Damping (36mm Laminated MDF) |

**Additional:**
- Klipper Input Shaping for residual resonance
- StealthChop on X for quiet operation
- SpreadCycle on Y/Z for torque

---

## Gasket Cutting Template

For users who want the simpler flat-gasket approach (Strategy A), provide a cutting template:

```python
# Motor Gasket Cutting Template
# Print 2mm thick as stencil for rubber mat

with BuildPart() as template:
    with BuildSketch() as s:
        Rectangle(42.5, 42.5)  # NEMA 17 footprint
        # Center Shaft Hole (24mm for clearance)
        Circle(12)
        # Mounting Holes (4.5mm for easy bolt passthrough)
        for loc in GridLocations(31, 31, 2, 2):
            with Locations(loc):
                Circle(2.25)
    extrude(amount=2)
```

**Usage:**
1. Place template on rubber mat (bike tube, hardware store rubber)
2. Stab through holes with screwdriver/knife
3. Cut the square outline
4. Ready to install

---

## Hardware Store Shopping List

### For Sandwich Mounts (Per Motor)

- 4× Rubber Grommets (10mm OD) - Electrical aisle
- 4× M3×25 or M3×30 bolts
- 4× M3 nuts
- 4× M3 washers (optional)

### For Simple Gaskets (Alternative)

- Rubber utility mat OR
- Bike inner tube
- 4× Rubber tap washers per motor (plumbing aisle)

### For Z-Motor MDF Mounting

- 6× M4 or M5 bolts (through MDF from bottom)
- 6× Large washers (prevent pull-through)
- 3× Flexible shaft couplers (5mm to 8mm typical)

---

## MDF Drill Jig for Z-Motors

### Purpose

Print a jig that hooks onto the MDF corner to mark exact drill locations—no measuring required.

### Design Concept

```python
# MDF Drill Jig (L-shaped ruler)
with BuildPart() as drill_jig:
    # Long arm that hooks over MDF edge
    # Hole at exact motor position
    # User: hook on corner, drill through hole, move to next corner
```

**Positions to mark:**
- Front-Left Z-motor: (20, 20)
- Front-Right Z-motor: (Width-20, 20)
- Rear-Center Z-motor: (Width/2, Depth-20)

---

## Weight and Anti-Drop Protection

### The Z-Drop Weight Concern

Heavy Z-drop beds can slide down if power goes out.

**The Tractor Solution:**
M10 threaded rods or lead screws have steep enough thread pitch that friction holds the bed in place—even without power.

### Additional Safety

- Use lead screws with low pitch (T8×2 recommended)
- NEMA 17 stepper motor cogging provides holding torque
- Bed should not free-fall even with motors disabled

---

## Key Takeaways

1. **Z-Motors → MDF:** Mass damping is the simplest, most effective solution
2. **X/Y Motors → Sandwich Mount:** True mechanical isolation from frame
3. **Rubber Grommets:** Available at any hardware store
4. **Klipper Input Shaping:** Handles any residual resonance in software
5. **Kinematic Z-Joints:** Prevent binding in Triple-Z system
6. **The "Scavenger" wins:** Bike tubes and tap washers work as well as specialty parts
