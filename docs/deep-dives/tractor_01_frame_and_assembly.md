# The Tractor: Frame Design & Assembly

## Overview

"The Tractor" is a box-frame 3D printer using M10 threaded rods for the frame structure, mounted on a laminated MDF base. This document covers frame construction, squaring strategies, and assembly workflow.

---

## Frame Specifications

### Reference Specification: M10 Threaded Rod

M10 was chosen as the "reference spec" for several reasons:

| Feature | M8 | M10 | M12 |
|---------|-----|-----|-----|
| Cross-section | ~50 mm² | ~78 mm² | ~113 mm² |
| Rigidity | Minimum viable | Very High (3× M8) | Overkill (5× M8) |
| Weight/Meter | ~0.3 kg | ~0.5 kg | ~0.7 kg |
| Nut Size (Hex) | 13mm | 17mm | 19mm |
| Printability | Easy | Easy | Can make brackets bulky |

**Why M10 over M12:**
- Standard 17mm wrench is universally available
- Easier to cut with a hacksaw
- Fits in smaller printed brackets
- Common in automotive applications (excellent for scavenging)
- Still provides massive rigidity for a 235×235×235 build volume

**Note:** The design is parametric—users can build in M8 or M12 if desired.

### Frame Dimensions (235×235 Bed)

For a 235×235mm bed with Triple-Z motors and toolhead clearance:

| Axis | Calculation | Rod Length |
|------|-------------|------------|
| X (Width) | Bed (235) + Lead Screws/Motors (80) + Clearance (65) | ~450mm |
| Y (Depth) | Bed (235) + Y-Carriage Travel (50) + Motor (60) | ~450mm |
| Z (Height) | Build Height (280) + Motor/Coupler (70) + Top Bracket (50) | ~500mm |

**Tip:** Buy 1-meter rods and cut them in half (500mm). Extra length isn't a problem with the offset method.

---

## Corner Design: The Offset Method

### Why Offset Corners?

When three rods meet at a corner, they cannot occupy the same space. The **Offset Method** (used in the original RepRap Darwin) is superior for threaded-rod builds because:

1. **No precision cuts required** - rods can extend past the corner
2. **Infinite adjustability** - brackets slide along the rod
3. **Easier assembly** - no complex hub geometry
4. **Scavenger-friendly** - tolerant of imperfect rod lengths

### The Standardized Plane Strategy

To prevent confusion, follow a strict Inside/Outside rule:

- **X-Rods (Left-to-Right):** Outermost layer
- **Y-Rods (Front-to-Back):** Middle layer  
- **Z-Rods (Vertical):** Innermost layer

This keeps Z-rods inside the frame, creating an unobstructed path for the bed to move up and down.

### Long Sleeve Design

Instead of thin brackets (like the original Mendel), use **50-60mm long sleeves** on the corner brackets:

**Benefits:**
- Forces rod perpendicularity (rod can't tilt in a long sleeve)
- Acts as a permanent squaring jig
- Provides massive clamping surface

**The "Nut Sandwich" Technique:**
- Place a nut on both sides of every plastic face the rod passes through
- Outer nut: Controls the maximum width
- Inner nut: Tensioner that locks the bracket against the outer nut
- Adjustment: Turn nuts (not the rod) to shift bracket position by fractions of a millimeter

---

## The MDF Base: "The Anvil"

### Specification

The MDF base is **mandatory** for the Tractor design:

- **Thickness:** 18mm minimum, 36mm (2×18mm laminated) preferred
- **Material:** Laminated MDF (white shelving) recommended
- **Glue:** PVA between raw particle-board faces

**Why laminated MDF is better:**
- Factory-smooth, moisture-resistant surface for layout lines
- Stiffer than raw MDF of equal thickness
- The "raw" sides glue together perfectly

### Damping Properties

36mm of laminated MDF provides:
- **Massive vibration dampening** - MDF is internally "lossy"
- **Low center of gravity** - prevents swaying during rapid accelerations
- **Clean Input Shaping** - high, clean resonance frequencies for Klipper

### Sealing (Important!)

Coat the MDF with PVA glue/water mix or paint to prevent:
- Moisture absorption
- Warping that could pull the frame out of square

---

## Squaring Strategy: Trust the Wood

### The Master Square Philosophy

Instead of squaring a wobbly skeleton of rods in mid-air, use the MDF base as the **Master Reference**:

1. The MDF baseboard is your jig
2. You only measure precisely once (when drawing layout lines)
3. The 3D printed anchors just hold rods relative to the wood

### Assembly Workflow

**Step 1: The Master Layout**
1. Draw a baseline near the front edge of the MDF
2. Draw two perpendicular lines going back
3. Draw the back line
4. **Critical Check:** Measure diagonals with a tape measure
5. Adjust lines until diagonals are exactly equal (to the millimeter)

**Step 2: Mount the Anchors**
1. Print four "Base Anchor" brackets
2. Place them precisely on the drawn rectangle corners
3. Drill through the MDF
4. Use M8 or M10 carriage bolts from underneath (counter-bored flush)
5. Tighten anchors down with large washers and nuts

**Result:** Four rigid plastic sockets fixed perfectly square to each other.

**Step 3: Drop-in Assembly**
1. **Verticals (Z):** Slide M10 Z-rods into vertical sockets—they stand perfectly plumb
2. **Horizontals (X & Y):** Slide bottom rods through horizontal sockets
3. No measuring needed—anchors are already at correct distances

### The Diagonal Rule

For any rectangular frame:
- Measure from Front-Left to Back-Right
- Measure from Front-Right to Back-Left
- If these numbers are equal, the frame is perfectly square

**The "Scavenger" Secret:** If diagonals don't match, slightly enlarge holes in the MDF to shift anchor brackets before final tightening.

---

## Squaring Jigs & Tools

### The "Squaring Block" Jig

Print four L-shaped tools that snap onto M12 rods at corners:

- Two semi-circular channels for the M12 rods
- Channels placed at exactly 90° to each other
- **Key Feature:** Channels account for rod offset (different heights)

**Assembly Hack:** Use zip-ties to hold rods in jigs while tightening nuts. Snip ties after nuts are locked.

### The "Internal Distance" Gauge

Print two "Gauge Sticks" at your exact target internal dimension (e.g., 350mm):

1. Place sticks between brackets at the bottom, tighten
2. Move same sticks to the top
3. If they don't fit or are loose, you know which nut to turn

**This eliminates tape-measure reading errors.**

### Calibration Slug (For Donor Printers)

Before printing full brackets, print a test piece with three hole sizes:

```python
# Test 10.4, 10.6, and 10.8mm holes
for i, size in enumerate([10.4, 10.6, 10.8]):
    # Create test holes in a simple block
```

**The Goal:** Find the hole where the rod slides in easily but doesn't rattle.

---

## Base Anchor Design

### Key Requirements

The bottom corner brackets are different from top corners:

1. **Massive Flange:** 100mm × 100mm × 15mm thick base plate
2. **Through-Bolt Holes:** 4 holes for mounting to MDF
3. **Central Block:** 60-70mm tall to hold the three offset rods
4. **Z-Rod Passthrough:** Hole goes through to MDF so steel rod bears weight directly

### build123d Concept

```python
# Base Anchor Parameters
flange_thickness = 15
block_height = 70
m10_clearance = 10.5

with BuildPart() as base_anchor:
    # 1. Foundation Flange
    with BuildSketch(Plane.XY) as flange_sketch:
        Rectangle(100, 100, align=(Align.MIN, Align.MIN))
        fillet(vertices(), radius=10)
    extrude(amount=flange_thickness)
    
    # 2. Central Block housing the rods
    with BuildSketch(Plane.XY.offset(flange_thickness)) as block_sketch:
        Rectangle(60, 60, align=(Align.MIN, Align.MIN))
    extrude(amount=block_height)
    
    # 3. Z-Rod through everything
    # 4. Mounting holes for MDF (M8 bolts)
```

---

## Hardware Recommendations

### From Bunnings/Hardware Store

- **M10 Threaded Rod:** Buy new for straightness
- **M10 Flanged Nuts:** Built-in washer distributes load
- **Large Fender Washers:** Prevent nuts sinking into plastic
- **Speed Square or Contractor Square:** For checking verticals
- **Laminated MDF Shelving:** 16-18mm pre-finished white

### Scavenger Sources

| Part | Best Source |
|------|-------------|
| M10 Smooth Rods | Large office photocopiers |
| Frame Fasteners | Automotive bins (flanged M10 nuts) |
| Base Material | Kitchen renovation skips (laminated countertops) |
| Rubber Gaskets | Old bike inner tubes |

---

## Key Takeaways

1. **Trust the flats:** Flat bracket surfaces will be square
2. **Trust the nuts:** Nuts/washers force rods to align with flat surfaces
3. **Trust the MDF:** The baseboard is the final "Correction Layer"
4. **Use long sleeves:** 50mm+ prevents rod tilting
5. **Diagonal check:** Equal diagonals = square frame
6. **The "Junkstrap" is safe:** Even a poorly-tuned Ender 3 can print parts that create a machine 10× more rigid than itself
