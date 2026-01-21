# Neo-Darwin "The Tractor" Frame Design Summary

A comprehensive summary of design decisions and recommendations for building a box-frame 3D printer using threaded rods, derived from iterative design discussions.

---

## 1. Design Philosophy

The Neo-Darwin (nicknamed "The Tractor") follows the **Scavenger Build** philosophy:

- Use readily available hardware from hardware stores (Bunnings) and salvaged components
- Bootstrap the build using a donor printer (Ender, Anet, i3 Mega) to print initial parts
- Prioritise repairability, adjustability, and accessibility over cutting-edge performance
- Target build volume: **235×235×235mm** (matching common heated bed sizes)

The design combines the repairability of the original Darwin/Mendel with modern performance through Klipper firmware integration.

---

## 2. Frame Rod Selection

### 2.1 Reference Specification: M10 Threaded Rod

**M10 is recommended as the reference specification** for the following reasons:

| Factor | M8 | M10 | M12 |
|--------|-----|------|------|
| Cross-sectional area | ~50 mm² | ~78 mm² | ~113 mm² |
| Rigidity vs M8 | Baseline | ~1.5× stiffer | ~2.3× stiffer |
| Weight per metre | ~0.3 kg | ~0.5 kg | ~0.7 kg |
| Nut size (hex) | 13mm | 17mm | 19mm |
| Scavengeability | Common | Very common (automotive) | Less common |
| Bracket bulk | Compact | Moderate | Chunky |

### 2.2 Why M10 Over M12

- **Tooling**: 17mm wrench is nearly universal in household toolkits
- **Automotive abundance**: M10 is standard for suspension components, engine mounts, and seat rails—excellent for scavenging
- **Bracket design**: Allows for sleeker, more refined printed parts
- **Hardware availability**: Flanged M10 nuts are readily available and look professional
- **Sufficient stiffness**: For spans of 450-500mm, M10 provides more than adequate rigidity

### 2.3 When to Consider M12

- You want the absolute "tank" aesthetic
- Maximum mass damping is desired
- You already have M12 stock available
- Building a larger-than-reference machine

### 2.4 Parametric Design

The bracket design should be **parametric** in build123d:

```python
rod_type = "M10"  # User can change to "M8" or "M12"
params = {
    "M8":  {"dia": 8.5,  "nut_flat": 13, "sleeve_od": 22},
    "M10": {"dia": 10.5, "nut_flat": 17, "sleeve_od": 28},
    "M12": {"dia": 12.5, "nut_flat": 19, "sleeve_od": 32}
}
```

---

## 3. Frame Dimensions

### 3.1 Recommended Rod Lengths

For a 235×235mm bed with Triple-Z motors and direct-drive toolhead:

| Axis | Calculation | Recommended Length |
|------|-------------|-------------------|
| X (Width) | Bed (235) + Lead screws/motors (80) + Clearance (65) | ~450mm |
| Y (Depth) | Bed (235) + Y-carriage travel (50) + Motor (60) | ~450mm |
| Z (Height) | Build height (280) + Motor/coupler (70) + Top bracket (50) | ~500mm |

> **Tip**: With the offset method, buy 1-metre rods and cut in half (500mm). Extra length isn't a problem—cap the ends with printed covers.

### 3.2 Frame Weight

With M10 rods:
- 12 rods (4 per axis) plus nuts and brackets
- Total frame weight: approximately **5-7 kg**
- This mass is beneficial—it absorbs ringing/ghosting caused by rapid direction changes

---

## 4. Squaring Strategy: The MDF Base-Anchor Method

This is the **critical innovation** that makes threaded-rod frames practical to build accurately.

### 4.1 The Core Principle

> *"If the base is square, and your brackets are printed well, the printer must be square."*

Instead of trying to square a wobbly skeleton of rods in mid-air, the MDF baseboard becomes a permanent **master reference jig**.

### 4.2 The MDF Base

**Specification:**
- Two layers of 18mm MDF laminated together = **36mm total thickness**
- Use PVA wood glue between the raw (unfinished) faces
- Clamp well and allow 24 hours to cure
- Pre-finished melamine shelving works well—the laminated faces provide a smooth, moisture-resistant surface

**Why laminated MDF works:**
- **Mass**: Heavy base lowers centre of gravity, prevents swaying during rapid accelerations
- **Damping**: MDF is internally "lossy"—converts vibration to heat rather than ringing
- **Flatness**: Factory surfaces are reliably flat
- **Moisture resistance**: Sealed surfaces prevent warping

**Sealing (optional but recommended):**
- Coat exposed MDF edges with diluted PVA glue to seal against humidity changes

### 4.3 The Squaring Workflow

#### Step 1: Mark the Master Layout

1. Draw a baseline near the front edge of the MDF
2. Draw two perpendicular lines going back (use a speed square or carpenter's square)
3. Draw the back line to complete the rectangle
4. **Critical check**: Measure both diagonals—they must be identical to the millimetre

#### Step 2: Mount the Base Anchors

1. Print four base anchor brackets
2. Place them precisely on the corners of your drawn rectangle
3. Drill through the MDF
4. Use M8 or M10 carriage bolts from underneath (counter-bored so bottom is flush)
5. Tighten anchors from above with large washers and nuts

**Result**: Four rigid plastic sockets fixed perfectly square to each other on an immovable base.

#### Step 3: Drop-In Assembly

1. **Verticals (Z)**: Slide M10 Z-rods into the vertical sockets—they will stand perfectly plumb (90° to the base)
2. **Horizontals (X & Y)**: Slide bottom X and Y rods through horizontal sockets—no measuring needed, just tighten nuts against anchors
3. **Top frame**: Slide top square onto pillars—it naturally falls into place

### 4.4 Squaring Verification

**The Diagonal Rule:**
- Measure from Front-Left to Back-Right
- Measure from Front-Right to Back-Left
- If these two measurements match, the frame is square

**Adjustment (if needed):**
- Slightly enlarge holes in MDF to "shift" an anchor bracket before final tightening

---

## 5. Corner Bracket Design

### 5.1 The Offset Method

Use the **Darwin/RepRap offset method** where rods bypass each other rather than meeting at a point:

```
Recommended layer order (outside to inside):
├── X-Rods (Left-to-Right): Outermost layer
├── Y-Rods (Front-to-Back): Middle layer
└── Z-Rods (Vertical): Innermost layer
```

**Why this order for Triple-Z:**
- Z-rods on the inside create a clear, unobstructed path for the build plate
- Horizontal rods don't block bed movement

### 5.2 Long Sleeve Design

The key to self-squaring brackets is **long sleeves** (50-60mm minimum):

**Benefits:**
- Rod physically cannot tilt within the sleeve
- Acts as a permanent squaring jig
- Eliminates need for separate squaring tools
- Provides massive grip area for the nut/washer interface

**Design features:**
- Sleeve length: 50-60mm minimum for Z-rods (the tall ones)
- Internal clearance: Rod diameter + 0.4-0.6mm (determined by calibration test)
- Optional internal alignment fins (0.2mm high ribs) to centre the rod

### 5.3 Base Anchor Bracket Requirements

The bottom four corners are different from the top—they must anchor to the MDF:

| Feature | Specification |
|---------|--------------|
| Flange size | 80-100mm × 80-100mm |
| Flange thickness | 12-15mm |
| Bolt holes | 4× for M8 bolts in corners of flange |
| Z-rod passthrough | Through the flange so rod rests on MDF |
| Structural webbing | Fillets/gussets connecting sleeves to flange |

### 5.4 Nut and Washer Strategy

- Use **extra-thick fender washers** (large outer diameter) to distribute load
- Prevents high torque from crushing 3D-printed walls
- Consider **flanged nuts** (M10 flanged nuts have built-in washer)
- Use **Nyloc nuts** for final locking—won't vibrate loose

### 5.5 Wrench Access

Design "nut windows" into the brackets:
- Generous opening for 17mm spanner (M10) or 19mm (M12)
- Consider access from multiple angles

---

## 6. X-Gantry Design

### 6.1 Motion System Overview

The Neo-Darwin uses a **Z-dropdown** configuration:
- Bed moves only vertically (Z-axis) on Triple-Z lead screws
- X-Y gantry moves at the top of the frame
- Similar to CoreXY/Voron layout but using the "Tractor" frame

### 6.2 X-Carriage: "The Plough"

The X-carriage design follows the Mendel i2 "plough" style, updated for M10 rods.

**Reference design**: [Thingiverse Thing:3940673](https://www.thingiverse.com/thing:3940673)

**Key modifications needed:**
- Replace zip-tie bearing mounts with **split-clamp housings**
- Add structural cut-aways (more walls, less infill)
- Accommodate Pitan/Titan direct-drive extruder with E3D V6 hotend

### 6.3 Smooth Rod Spacing for X-Gantry

For the "top-down" plough configuration where the **Pitan nests between the rods**:

| Configuration | Spacing (C-to-C) | Notes |
|--------------|------------------|-------|
| Vertical stack | 50mm | Rods stacked vertically |
| **Top-down/horizontal** | **58-62mm** | Pitan nested between rods (recommended) |

**60mm spacing calculation:**
- NEMA 17 motor width: 42.3mm
- Structural wall thickness: 4mm × 2 sides = 8mm
- LM10UU bearing clearance: ~10mm
- **Total: ~60mm**

### 6.4 Bearing Mounts: Split-Clamp Design

Replace zip-ties with proper clamped bearing housings:

```python
# Conceptual split-clamp for LM10UU
bearing_od = 19.0 + 0.2  # Nominal + slop
bearing_len = 29.0
clamp_bolt_dia = 3.5     # For M3 pinch bolt

# Design features:
# - C-shaped housing around bearing
# - M3/M4 bolt pinches housing closed
# - Zero slop, serviceable, adjustable preload
```

**Advantages:**
- Accounts for print inaccuracies from donor printer
- Bearings can be swapped without breaking carriage
- Tightening bolt slightly deforms plastic for perfect grip

### 6.5 Structural Optimisation

For maximum strength with minimum weight:

- **4-6 perimeter walls** provide more rigidity than solid infill
- Use **structural ribs/webbing** instead of solid blocks
- Cut-away pockets leave 3-5mm thick structural beams
- Ribs help break up resonance frequencies from stepper motors

---

## 7. Z-Axis: Triple-Z with Kinematic Joints

### 7.1 Configuration

- **Three lead screws** in a triangle pattern:
  - Two at front corners
  - One at centre-back
- Creates a stable tripod that defines a perfect plane
- Klipper's `z_tilt_adjust` automatically levels the bed

### 7.2 The Kinematic Z-Joint

**Problem**: If three Z-rods aren't perfectly parallel, a rigid bed mount will bind, skip steps, and leave print artifacts.

**Solution**: Decouple the lead screw (movement) from the smooth rod (constraint).

#### The "Ball and Cup" Design (Scavenger's GE5C)

Instead of buying GE5C spherical bearings:

1. **Nut carrier**: T8 lead screw nut bolted to a small printed part
2. **Ball**: 6mm or 8mm steel ball (from a large bearing) sits on the carrier
3. **Bed bracket**: Has a conical "cup" that rests on the ball
4. **Gravity holds it down**—if the lead screw tilts, the ball shifts in the cup without bending anything

#### The "Two-Part" Bracket

- **Smooth rod side (rigid)**: Houses LM8UU/LM10UU, bolted to bed, maintains X-Y position
- **Lead screw side (floating)**: T8 nut in an oversized pocket, can move laterally but not vertically

### 7.3 Mixing Rod Sizes

If using M8 smooth rods from an i3 Mega donor with M10 threaded frame:

- Z-guides: M8 smooth rods (scavenged)
- Frame: M10 threaded rod (purchased)
- Corner anchors need: 10.5mm hole for frame, 8.2mm hole for Z-rod

> **Note**: M8 rods are thinner and may flex more—the kinematic joints and triple-Z configuration compensate for this.

---

## 8. Motion System: Dual-Y Gantry Drive

### 8.1 Why Dual-Y Motors

For a Z-dropdown gantry design:

- **One NEMA 17 at back-left, one at back-right**
- Prevents cantilever lag at rod ends
- Each side driven independently = no racking or twisting
- Klipper handles synchronisation seamlessly

### 8.2 Automatic Squaring

With dual Y-motors on separate drivers:

1. Place one endstop on left Y-rail, one on right Y-rail
2. When printer homes, each motor moves until it hits its own switch
3. **Gantry automatically squares to frame every power-on**

Klipper configuration:
```ini
[stepper_y]
# Left side motor config

[stepper_y1]
# Right side motor config
```

### 8.3 Belt Tensioning

Design motor mounts with **slots** (not holes) for motor bolts:
- 8mm long slots allow sliding motor to tension belt
- Eliminates need for separate tensioner at front

---

## 9. Electronics and Motors

### 9.1 Motor Requirements

| Axis | Quantity | Notes |
|------|----------|-------|
| X | 1 | Use lightest motor (travels on gantry) |
| Y | 2 | Use matched pair from same donor |
| Z | 3 | Use identical motors if possible |
| E | 1 | Standard extruder motor |
| **Total** | **7** | |

### 9.2 Sourcing Strategy

**Option A: Double Donor** (recommended for scavenger builds)
- Two Ender/Anet/i3 Mega donors provide 8 motors
- Also get: second PSU, endstops, cables, smooth rods, electronics

**Option B: Single Donor + Purchase**
- One donor provides 4 motors
- Purchase 3 additional NEMA 17s

### 9.3 Multi-MCU Klipper Configuration

With two donor mainboards:

```ini
[mcu]
serial: /dev/serial/by-id/usb-board_1

[mcu aux]
serial: /dev/serial/by-id/usb-board_2
```

**Suggested allocation:**
- Board 1: X, Y1, Y2, E
- Board 2: Z1, Z2, Z3

Klipper handles microsecond synchronisation—feels like one 7-driver board.

### 9.4 Power Supply Considerations

With 7 motors and a large heated bed, a single 250-350W PSU may be insufficient.

**Two-PSU strategy:**
- PSU 1: Motherboard + X/Y/E motors
- PSU 2: 3×Z motors + heated bed
- **Critical**: Connect V- (negative) terminals together for common ground

---

## 10. Calibration and Assembly

### 10.1 The "Lumpy Gauge" Calibration Test

Before printing full brackets, print a calibration slug to find your donor printer's optimal clearance:

```python
# Test three hole sizes
test_offsets = [0.2, 0.4, 0.6]  # Added to nominal diameter

# For M10: test 10.2mm, 10.4mm, 10.6mm holes
# For M10 nut (17mm): test 17.2mm, 17.4mm, 17.6mm hex traps
```

**Testing procedure:**
1. **Push test**: Find hole where rod slides through with firm push but doesn't wiggle
2. **Drop test**: Find hex trap where nut drops in but doesn't spin under torque
3. Use those offsets in final bracket design

### 10.2 Donor Printer Preparation

Before printing Tractor parts:

1. **Paper test**: Ensure bed is level
2. **Belt tension**: Tighten belts (loose belts cause "racking")
3. **Square test**: Print 100×100mm L-shape (2mm thick), check against a square

### 10.3 Print Settings for Structural Parts

| Setting | Value | Reason |
|---------|-------|--------|
| Infill | 40%+ | Compression strength for nuts |
| Walls/Perimeters | 5-6 | Sleeve strength comes from walls |
| Material | PLA or PETG | Whatever donor prints reliably |
| Layer height | 0.2mm | Balance of speed and strength |

### 10.4 Cutting Hardened Smooth Rods

Photocopier rods are often **induction hardened**:

- Hacksaw blades will skate off and go blunt
- **Use**: Angle grinder with thin (1mm) Inox cutting disc
- **Alternative**: Dremel with reinforced cutoff wheel
- **Hacksaw hack**: Grind through hardened "skin" first, then saw soft core
- **Always wear eye protection**

---

## 11. Software Configuration

### 11.1 Klipper Features to Utilise

| Feature | Purpose |
|---------|---------|
| `[z_tilt]` | Auto-level Triple-Z bed using 3 probe points |
| `[stepper_y1]` | Dual Y-motor with independent homing |
| Input Shaping | Compensate for any residual resonance |
| Pressure Advance | Optimise extrusion for speed |

### 11.2 Expected Performance

With the massive MDF base and M10 frame:
- Very high, clean resonance frequencies
- Input Shaping calibration will be highly effective
- Minimal low-frequency wobbles
- **Exceptionally quiet operation**—frame doesn't act as speaker cone

---

## 12. Summary: The Tractor Reference Specification

| Component | Specification |
|-----------|--------------|
| Frame rods | M10 threaded (parametric for M8/M12) |
| Frame dimensions | 450×450×500mm (rod lengths) |
| Base | 36mm laminated MDF (2×18mm) |
| Squaring method | MDF base-anchor with long-sleeve brackets |
| X smooth rods | M10 (scavenged from photocopiers) |
| X-rod spacing | 60mm centre-to-centre (horizontal/top-down) |
| Z smooth rods | M8 or M10 (from donor or scavenged) |
| Z configuration | Triple-Z with kinematic joints |
| Y drive | Dual motors with dual endstops |
| Motors required | 7 total (1X, 2Y, 3Z, 1E) |
| Electronics | Dual-MCU Klipper configuration |
| Extruder | Pitan/Titan direct drive with E3D V6 |

---

## 13. Next Steps

1. **Print calibration gauge** on donor printer to determine slop factors
2. **Source materials**: M10 threaded rod, MDF sheets, hardware
3. **Design base anchors** in build123d with determined tolerances
4. **Laminate and mark MDF base**
5. **Print and mount base anchors**
6. **Assemble frame** using drop-in method
7. **Verify squareness** with diagonal measurements
8. **Continue with gantry and Z-axis assembly**

---

*Document generated from Neo-Darwin design discussions. Design philosophy: "A Tractor with the Brain of a Racecar"—heavy, reliable hardware with modern Klipper firmware.*
