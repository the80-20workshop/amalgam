# The Tractor: X-Y Axis System

## Overview

"The Tractor" uses a Z-Drop (Z-Dropdown) design where the bed moves vertically on Triple-Z while a gantry handles X-Y motion at the top of the frame. This document covers the X-carriage ("The Plough"), Y-axis gantry system, and motion components.

---

## Z-Drop Architecture

### What is Z-Drop?

Unlike bed-slingers (where the bed moves in Y), a Z-Drop design:

- **Bed:** Stationary in X-Y, moves only vertically (Z) on its own independent system
- **Gantry:** X-axis assembly moves front-to-back along Y-rods (fixed height)
- **Motion:** The "Plough" (X-carriage) moves left-right, the gantry moves front-back
- **Z-Axis:** Completely separate — bed drops down as layers are printed

**Key Point:** The X-Y gantry and Z-axis are **independent systems**. The gantry never moves vertically.

**Benefits:**
- Heavy bed isn't moving back and forth (reduces "ringing")
- Higher print speeds possible
- Better for large, heavy heated beds
- Gantry stays at fixed height (simpler belt paths)

### Component Layout

```
Top of Frame (Fixed Height - X-Y Motion):
┌─────────────────────────────────┐
│  [Y-Motor]     Y-Rods    [Y-Motor]  ← Dual Y steppers
│       ════════════════════       ← Y-rods fixed to top frame
│       ↑                  ↑
│    [X-End]            [X-End]    ← Slide on Y-rods (front-back)
│       ├── X-Rods (60mm) ─┤       ← Carried by X-Ends
│       │   [THE PLOUGH]   │       ← Slides on X-rods (left-right)
│       │    Pitan + V6    │
└───────┴──────────────────┴──────┘

Inside Frame (Separate Z Motion):
┌─────────────────────────────────┐
│                                 │
│  Z-Rods (M8/M10 smooth)         │  ← Vertical guide rods
│  ↕ Triple-Z lead screws         │  ← Drive bed up/down
│      [Heated Bed Platform]      │  ← Moves ONLY in Z
│                                 │
└─────────────────────────────────┘

The X-Y gantry and Z-bed are INDEPENDENT systems.
```

---

## Dual Y-Axis System

### Why Dual Motors (Not Sync Shaft)?

The Tractor uses **two Y-steppers** (one per side) instead of a single motor with sync shaft:

| Feature | Single Motor + Sync Shaft | Dual Y Steppers |
|---------|--------------------------|-----------------|
| Parts | 1 Motor, Long Rod, 2-4 Bearings, 2 Couplers | 2 Motors, 2 Pulleys |
| Complexity | High (shaft must be parallel) | Low (self-contained units) |
| Scavenger Factor | Hard to find straight 500mm rod | Easy—second motor from donor |
| Robustness | Adds rotational slop over distance | Double torque for heavy gantry |
| Klipper Edge | Manual squaring only | **Auto-squaring every home** |

### Auto-Squaring with Klipper

The **killer feature** of dual Y motors:

1. Place one endstop on left Y-rail, one on right Y-rail
2. When printer homes, both motors move toward back
3. Left side hits switch first → stops
4. Right side continues until it hits its switch
5. **Result:** Gantry is square to frame within 0.01mm

This level of precision is nearly impossible with a manual sync shaft.

### Driver Requirements

For Dual-Y + Triple-Z:
- 1 driver for X
- 2 drivers for Y (Y and Y1)
- 3 drivers for Z (Z, Z1, Z2)
- 1 driver for Extruder

**Total: 7 Drivers**

Options:
- MKS SKIP + expansion board (SKR Pico)
- Two donor mainboards via Klipper Multi-MCU
- Hard-wire Y-motors in series (loses auto-square)

### Y-Motor Corner Mount

The Y-motors sit at top corners of the box frame:

```python
# Integrated Y-Motor Mount
motor_offset = 45  # Distance from frame center to motor shaft

with BuildPart() as y_motor_mount:
    # 1. Core Tractor Corner (M10/M12 Hub)
    # [Frame rod clamping logic]
    
    # 2. Motor Cantilever
    with BuildSketch(face.sort_by(Axis.X)[-1]) as s:
        Rectangle(50, 60)  # Massive plate for NEMA 17
    extrude(amount=12)
    
    # 3. NEMA 17 Pattern with tension slots
    # Use 10mm slots for belt tensioning by sliding motor
    for loc in GridLocations(31, 31, 2, 2):
        SlotOverall(10, 4.5, rotation=90)
```

---

## X-Axis: "The Plough"

### Design Philosophy

The X-carriage is called "The Plough" in Tractor terminology. It's based on the Mendel i2 style but upgraded:

- **Redesigned:** Clamps instead of zip-ties for linear bearings
- **Structural:** Cut-aways with thick walls (not solid infill)
- **Nested:** Pitan/Titan extruder sits between the two X-rods

### Rod Spacing: 60mm (Center-to-Center)

For a top-down "nests between the rods" configuration:

| Component | Dimension |
|-----------|-----------|
| NEMA 17 Motor Width | 42.3mm |
| Plastic Wall Thickness (each side) | 4mm × 2 = 8mm |
| LM10UU Bearing Clearance | ~10mm |
| **Total Spacing** | ~60mm |

**Why 60mm:**
- Wide stance resists "yaw" (twisting left-right)
- Fits Pitan motor body with clearance between rods
- Provides balanced weight distribution for direct drive

### Structural Optimization: "Hollow Bone" Principle

Strength comes from **skin tension**, not solid plastic:

- Use 4-6 perimeters (walls) instead of 100% infill
- Design structural "ribs" and "webs"
- Cut-away weight-saving pockets leaving 3-5mm thick beams

```python
# The Plough: Skeletonized Carriage
rod_spacing = 60  # Center-to-center
bearing_od = 19.4  # LM10UU with slop
wall_thickness = 4.0

with BuildPart() as plough:
    # 1. Two horizontal Bearing Cylinders
    # Top and bottom bearing housings
    
    # 2. The 'Spine' connecting them
    # Structural plate, not solid block
    
    # 3. Cut-aways (Lumpy optimization)
    # Triangular or slot subtractions leaving X/V truss
```

### Split-Clamp Bearing Housing

Replace zip-ties with proper clamps:

```python
# LM10UU Bearing Clamp
bearing_od = 19.0 + 0.2  # Nominal + slop
bearing_len = 29.0
clamp_bolt_dia = 3.5     # For M3 bolt

with BuildPart() as bearing_mount:
    # 1. Main Block
    with BuildSketch() as s:
        Rectangle(bearing_od + 10, bearing_len)
    extrude(amount=bearing_od / 2 + 5)
    
    # 2. Bearing Bore
    # Semi-circular channel for LM10UU
    
    # 3. The "Split" for clamping
    with BuildSketch(Plane.XY.offset(bearing_od / 2)) as s3:
        Rectangle(2, bearing_len)  # 2mm slot
    extrude(amount=10, mode=Mode.SUBTRACT)
    
    # 4. Bolt ears for M3 pinch bolt
```

**Benefits of Split-Clamp:**
- Zero slop (accounts for print inaccuracies)
- Serviceable (swap bearings without breaking carriage)
- Pre-load adjustment (slight tightening grips bearing perfectly)

---

## X-Ends (Where X Meets Y)

### Function

The X-Ends are the "sliders" that carry the X-axis rods while moving along the Y-axis:

1. Hold LM10UU bearings to slide on Y-axis rods (front-back motion)
2. Clamp M10 smooth rods for X-axis (carry the Plough's rails)
3. Provide mounting point for Y-axis belt attachment

**Note:** The X-Ends have **nothing to do with the Z-axis**. In Neo-Darwin's Z-drop design, the Z-axis (bed platform) is a completely separate system with its own rods and lead screws.

### Design for 60mm Horizontal Spacing

```python
# Tractor Gantry X-End
with BuildPart() as x_end:
    # 1. Y-Axis Bearing Housing (slides on Y-rods, front-back)
    with BuildSketch() as s1:
        Circle(radius=15)  # Outer housing for LM10UU
    extrude(amount=40)
    
    # 2. X-Axis Rod Sockets (perpendicular, carries The Plough)
    # Two M10 holes at 60mm spacing
    with BuildSketch(Plane.YZ.offset(20)) as s2:
        for loc in [(0, 30), (0, -30)]:  # 60mm total
            with Locations(loc):
                Circle(radius=5.1)
    extrude(amount=30, mode=Mode.ADD)
    
    # 3. Belt Anchor
    # Attachment point for Y-axis belt (pulls X-End front-back)
```

---

## Belt Path Strategy

### For Top-Down (60mm Spacing)

The GT2 belt should run:

1. **Center-line:** Exactly at 30mm mark (midpoint between rods)
2. **Underneath the carriage:** Avoids interference with motor
3. **Parallel to rods:** Prevents "cocking" during fast moves

**Single Belt (Recommended):**
For a 300mm span on M10 rods, one center-line belt provides sufficient force.

**Belt Gripper:**
Use screw-tensioned gripper instead of just a slot:
- M3 bolt pinches belt into toothed cavity
- Much more secure than friction-fit slots

### Belt as "Weakest Link"

On a 300mm span with M10 rods, belts are the compliance point:

**Tractor Tip:** Keep belt as close to smooth rods as possible. The further belt is from rod, the more "leverage" to twist carriage during fast moves.

---

## Smooth Rod Specifications

### M10 Smooth Rods (Reference Spec)

For X and Y axes, M10 smooth rods provide:

- ~2.4× stiffer than M8
- Higher natural frequency (reduces resonance)
- Cleaner Input Shaping results
- Can push to higher accelerations

### Scavenging Smooth Rods

**Best Source:** Large office photocopiers

**The Challenge:** Photocopier rods are often **induction hardened** (HRC 60+)

**Cutting Methods:**
1. **Angle Grinder (Best):** 1mm thin "Inox" cutting disc
2. **Dremel:** Reinforced cutoff wheel (slower but works)
3. **Hacksaw (Pro Hack):** Grind away hardened skin first, then cut soft core

**Safety:** Always wear eye protection—hardened steel shards are very sharp.

### Rod Quality Check

Roll the rod across your MDF baseboard:
- If it "wobbles" or light gaps appear underneath → it's bent
- For frame: slight bend is okay (nuts pull it straight)
- For Z-axis movement: must be perfectly straight

---

## Hybrid Mounting: Threaded + Smooth

Your corner brackets hold both:

- **M10 Threaded:** For the structural frame
- **M10 Smooth:** For the motion rails

### "MK2/MK3 Style" Cradles

The smooth rods sit "on top of" the threaded rods:

```python
# Threaded-to-Smooth Rod Adapter
with BuildPart() as adapter:
    # Lower half: Clamps onto M10 Threaded
    with BuildSketch() as s:
        Circle(radius=15)  # Outer shell
    extrude(amount=30)
    
    # Subtract Threaded Rod hole
    Circle(radius=5.5)  # M10 clearance
    
    # Upper half: Cradles M10 Smooth (20mm above)
    with BuildSketch(Plane.XZ.offset(15)) as s3:
        Circle(radius=5.1)  # Tight fit for smooth rod
    extrude(amount=30, both=True, mode=Mode.SUBTRACT)
```

**Securing Smooth Rods:**
- Blind socket (30mm deep hole)
- Blue-tack at bottom, or
- Small M3 grub screw to pinch rod

---

## Direct Drive: Pitan + E3D V6

### Configuration

- **Extruder:** Pitan (Titan clone) direct drive
- **Hotend:** E3D V6
- **Fans:** Heatsink fan + part cooling fan

### Carriage Integration

The Pitan motor nests **between** the X-rods:

- Motor body centered at 30mm mark
- Nozzle exactly centered between rods (balanced weight)
- Belt grippers included in carriage design

### Weight Considerations

Pitan + V6 = ~400-500g concentrated mass

**The "Nod" Problem:**
As carriage accelerates, front-heavy mass wants to twist gantry.

**Solution:** 60mm rod spacing creates large "I-beam" effect, drastically reducing tendency to nod or twist.

---

## Key Parameters Summary

| Parameter | Value | Notes |
|-----------|-------|-------|
| X-Rod Spacing | 60mm (center-to-center) | Horizontal, top-down |
| Y-Rod Spacing | Determined by frame | Fixed to top of box |
| Rod Diameter | M10 smooth | Reference spec |
| Bearing | LM10UU | 19mm OD, 29mm length |
| Belt | GT2 6mm | Single, center-line |
| Motor Mounting | 31mm pattern | NEMA 17 standard |

---

## Assembly Sequence

1. **Build Frame First:** Complete the M10 threaded box
2. **Install Y-Rods:** Fixed to top corners via cradles
3. **Assemble X-Ends:** With bearings for Y-rods
4. **Install X-Rods:** Through X-Ends, maintaining 60mm spacing
5. **Mount The Plough:** Slide onto X-rods with bearings
6. **Install Belts:** Through grippers, tension via motor slots
7. **Wire Endstops:** Left Y, Right Y, X-min

### Squaring Check

After assembly:
1. Home Y-axis (both motors)
2. Verify gantry is parallel to frame
3. Home X-axis
4. Verify Plough moves smoothly full travel
