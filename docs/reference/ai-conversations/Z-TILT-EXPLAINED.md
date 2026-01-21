# Z-Tilt Leveling: How It Works & Neo-Darwin Implications

## What is Z-Tilt?

Z-Tilt is a **software bed leveling system** in Klipper for printers with **3 independent Z-motors**. It uses a Z-probe (BLTouch or inductive) to measure bed tilt relative to the gantry and automatically adjust the 3 Z-motors to make the bed **parallel to the gantry**.

### Key Principle
```
Gantry = FIXED reference plane (X and Y smooth rods)
Bed = ADJUSTABLE plane (3 independent Z-motors)
Z-Tilt = Makes bed parallel to gantry
```

---

## How Z-Tilt Works

### The Process
```
1. G28 Z (Home Z-axis)
   → All 3 Z-motors move up until endstops triggered

2. Z_TILT_ADJUST (Calibration)
   a. BLTouch probes 3 points on bed:
      - Point A: Front-left
      - Point B: Front-right or back-left
      - Point C: Back-right or back-center
   b. Klipper calculates tilt (slope) of bed relative to gantry
   c. Klipper adjusts 3 Z-motors to compensate:
      - Motor Z1 moves up/down slightly
      - Motor Z2 moves up/down slightly
      - Motor Z3 moves up/down slightly
   d. Repeat until bed is parallel (tilt < 0.01mm)

3. Store adjustments
   → Motor positions saved to config
   → Next print starts from leveled position

4. G28 Z (Home again - optional but recommended)
   → Now bed homes while LEVEL
```

### What Z-Tilt Measures
```
BLTouch measures:
- Distance from gantry (nozzle plane) to bed surface
- At 3 probe points forming a triangle
- Example probe points (250mm² bed):
  - Point 1: X=50, Y=50, Z = 3.245mm
  - Point 2: X=200, Y=50, Z = 3.218mm
  - Point 3: X=125, Y=200, Z = 3.280mm

Klipper calculates:
- Bed slope: Front is lower than back by 0.062mm
- Bed slope: Left is higher than right by 0.027mm
- Tilt adjustments needed to make plane parallel
```

### What Z-Tilt Adjusts
```
After probing 3 points:
- Motor Z1 (front-left): Move DOWN by 0.031mm
- Motor Z2 (front-right): Move UP by 0.009mm
- Motor Z3 (back-center): Move UP by 0.041mm

Result: Bed is now parallel to gantry within 0.01mm
```

---

## Critical Questions Answered

### Q1: Does bed stop at top of leadscrews or use BLTouch for calibration?

**Answer: Neither!**

**Reality:**
- Bed does NOT mechanically stop at leadscrew top
- Z-travel is set in Klipper config (position_max)
- Z-Tilt makes bed **parallel to gantry**
- BLTouch is used for Z-Tilt **calibration**, NOT as endstop

**How Z-travel is set:**
```python
# printer.cfg
[stepper_z]
position_max: 250, 250, 250  # Max X, Y, Z travel
```

**How Z-Tilt calibration works:**
1. BLTouch probes bed at 3 points
2. Calculates tilt (slope) of bed
3. Adjusts motor positions to make bed parallel
4. Saves motor offsets to config
5. Future prints start from leveled position

**Why NOT use BLTouch as endstop?**
- BLTouch is NOT used for homing
- Z-endstops (optical or mechanical) used for homing
- BLTouch ONLY used for Z-Tilt calibration and bed mesh probing
- If BLTouch used as endstop, Z-Tilt would fight with homing

---

### Q2: How do we calibrate max-Z and bed level?

**Answer: Two-step process**

#### Step 1: Calibrate Max-Z (Once, mechanical setup)
```
Physical setup:
1. Manually move bed to TOP of travel
2. Measure distance from nozzle to bed surface (paper test)
3. Determine: Z=250 is actually 0.5mm from bed
4. Set Z-offset: Z_OFFSET = 0.5mm (in config)

Or use BLTouch:
1. Home Z (G28)
2. Move nozzle to bed center
3. Probe bed repeatedly (Z_PROBE)
4. Find Z where nozzle just touches (paper test)
5. Set Z-offset: Z_OFFSET = -0.2mm (adjust based on probe)
```

#### Step 2: Calibrate Bed Level (Z-Tilt, periodic)
```
Initial setup (after assembly):
1. G28 Z (home)
2. Z_TILT_ADJUST (probe 3 points, adjust motors)
3. Check results: Tilt < 0.01mm?
4. Repeat until bed is level
5. SAVE Z_TILT_ADJUST results to config

After moves or maintenance:
1. G28 Z
2. Z_TILT_ADJUST (re-calibrate)
3. Save if improved
```

**Why two steps?**
- **Max-Z**: Mechanical limit set once (position_max in config)
- **Bed level**: Software adjustment runs periodically (Z_TILT_ADJUST)
- Z-offset handles the gap between max-Z and actual bed surface

---

### Q3: Do motors go inside or outside frame?

**Answer: Voron Trident = INSIDE frame, Neo-Darwin can do either**

#### Voron Trident Approach
```
[Aluminum Extrusion Frame]
  |
  | ← Z-motor bolted to EXTRUSION (inside corner)
  |
  |
[Leadscrew goes UP through frame interior]
  |
  |
  v
[Bed moves up/down]
```

**Voron implementation:**
- Motors bolted to inside of 2020 extrusion corners
- Leadscrews go UP through frame interior
- Compact footprint
- Protected motors

#### Neo-Darwin M12 Frame Options

**Option A: Inside frame (Voron-like)**
```
[M12 Rod Frame]
  |
  | ← Z-puck clamped to vertical rod
  |    [MOTOR mounted to puck, inside frame]
  |
  | ← Leadscrew goes UP through frame
  |
[Bed moves up/down]
```

**Pros:**
- Compact footprint
- Motors protected by frame
- Matches Voron design

**Cons:**
- Motor access limited (inside frame)
- Leadscrew clearance must be designed
- Spider bed must fit around leadscrews

**Option B: Outside frame (Alternative)**
```
[M12 Rod Frame]
  |
  | ← Z-puck clamped to vertical rod
  |
[Motor] ← Mounted OUTSIDE frame
  |
  | ← Leadscrew goes UP through frame
  |
[Bed moves up/down]
```

**Pros:**
- Easy motor access
- More leadscrew clearance
- Easier assembly

**Cons:**
- Wider footprint
- Motors exposed
- Less "clean" look

**Recommendation: INSIDE frame (Voron-like)**
- Leadscrew path through frame interior
- Motor mounted to Z-puck, which clamps to M12 rod
- Design Z-puck with motor mount extending INSIDE frame
- Spider bed designed around leadscrew clearance

---

## Neo-Darwin Frame Geometry Decisions

### Z-Motor Placement
```
Based on Voron Trident and spider bed support:

        [Top Frame - Gantry]
                |
                |
       [Puck Z2]   [Puck Z3]
       (Back L)      (Back C)
                |
                |
    [Bed + Spider rises UP]
                |
                |
       [Puck Z1]   [Puck Z4 optional]
       (Front L)     (Front R)
                |
         [Bottom Frame]

ACTUAL: 3 motors needed for stable triangle
- Z1: Front-left vertical rod
- Z2: Back-left vertical rod
- Z3: Back-center vertical rod (NOT corner!)

Why back-center instead of front-right?
- Spider bed is triangular support
- Triangle = 3 points
- Front L + Back L + Back C = stable triangle
- Avoids front-right corner (would be unbalanced)
```

### Leadscrew Path
```
RECOMMENDED: Inside frame (Voron-like)

[M12 Rod]   [M12 Rod]
   |            |
   |            | ← Leadscrews go UP through frame interior
   |            |
[Z-Puck]   [Z-Puck]
   |            |
[MOTOR]     [MOTOR]
   |            |

Clearance requirements:
- 40mm between leadscrews (for spider hub)
- 30mm clearance from bottom frame (bed at Z=0)
- 20mm clearance from top gantry (bed at Z=max)
```

### Z-Travel Calculation
```
From config.py:
BUILD_VOLUME["Z"] = 250mm

SKELETON_Z = BUILD_VOLUME["Z"] + 80
           = 250 + 80
           = 330mm total frame height

ACTUAL Z-Travel = SKELETON_Z - bottom_clearance - top_clearance
               = 330 - 30 - 20
               = 280mm total travel

USABLE Z-Travel (with Z-offset):
               = 280 - Z_offset
               = 280 - 5 (typical offset)
               = 275mm usable

CONFIGURATION IN KLIPPER:
[stepper_z]
position_max: 280  # Total physical travel
position_min: -2    # Allow bed to go slightly below 0
z_offset: 5.0       # Set during calibration
```

---

## Voron Trident Reference Research

### Key Findings from Voron Research
1. **Z-motors bolt to bottom frame extrusions** (not vertical rods)
2. **Leadscrews go UP through frame interior**
3. **Bed rises to meet fixed gantry**
4. **Z=0: Bed at bottom, Z=max: Bed near top gantry**
5. **Triangle support pattern: Front L + Front R + Back C** OR variations

### Voron vs Neo-Darwin Differences

| Aspect | Voron Trident | Neo-Darwin |
|---------|---------------|--------------|
| Frame | 2020/2040 aluminum | M12 threaded rods |
| Z-mount | Bolt to extrusion | Z-puck clamped to rod |
| Motor location | Bottom corners | Bottom or vertical rods |
| Leadscrews | Inside frame | Inside or outside |
| Z-Tilt | BLTouch calibration | BLTouch calibration (same) |
| Endstops | Optical or mechanical | Optical or mechanical |

---

## Recommended Neo-Darwin Z-System Design

### Z-Puck on Vertical Rods (Inside Frame)
```
[M12 Vertical Rod]
  |
  |
[Z-Puck] ← Clamps to vertical rod
  |
  |    [Motor mount extends INSIDE frame]
  |    [Motor faces inward]
  |    [Leadscrew goes UP through frame]
  |
  v
[Bottom Frame]
```

**Design requirements:**
- Z-puck slides over M12 rod
- Motor mount extends 40-50mm INSIDE frame
- Leadscrew path has 40mm clearance from frame edges
- Jam nuts secure Z-puck to rod (2 per position)
- Cable routing along vertical rod to bottom

### Spider Bed Support
```
        [Leadscrew Z1]  [Leadscrew Z2]  [Leadscrew Z3]
              |               |               |
              v               v               v
           [Spider Arm 1]  [Spider Hub]  [Spider Arm 3]
                       \            |            /
                        \           |           /
                         \          |          /
                           \        |         /
                             [Bed 250mm²]

Spider arms have leadscrew nut traps
Bed bolted to outer edges of spider arms
```

**Design requirements:**
- Hub: 120mm triangle with 3 arm mounts
- Arms: 150mm from hub to bed edge
- Nut traps: Anti-backlash nuts for leadscrews
- Interlock: Arms bolt to hub for rigidity
- Clearance: Spider fits between 3 leadscrews (40mm spacing)

---

## Calibration Workflow Summary

### Initial Assembly (One-time)
```
1. Mechanical setup:
   - Assemble frame
   - Install Z-motors, leadscrews, bed
   - Set position_max in Klipper config

2. Max-Z calibration:
   - G28 Z (home)
   - Move to bed center
   - BLTouch probe → Find Z where nozzle touches
   - Set z_offset in config (e.g., z_offset: 5.0)

3. Bed leveling (Z-Tilt):
   - G28 Z (home)
   - Z_TILT_ADJUST (probe 3 points, adjust motors)
   - Repeat until tilt < 0.01mm
   - Save Z_TILT_ADJUST results to config
```

### Ongoing Maintenance
```
After moving printer:
  - G28 Z
  - Z_TILT_ADJUST
  - Save if improved

Periodically (every few weeks):
  - G28 Z
  - Z_TILT_ADJUST
  - Check for drift

After replacing leadscrews/motors:
  - Re-run Max-Z calibration
  - Re-run Z_TILT_ADJUST
```

---

## Open Design Questions

1. **Z-puck clamping**:
   - Clamp to VERTICAL rod or mount to BOTTOM horizontal rod?
   - Vertical = Voron-like (leadscrews up through frame)
   - Bottom = Different approach, easier?

2. **Triangle pattern**:
   - Front L + Back L + Back C? (my proposal)
   - Front L + Front R + Back C? (symmetric)
   - What's most stable?

3. **Z-travel**:
   - Is 280mm total travel sufficient?
   - 330mm frame - 30mm bottom - 20mm top = 280mm
   - Is 250mm claimed Z-height achievable with Z-offset?

4. **Spider clearance**:
   - Is 40mm between leadscrews enough for spider hub?
   - Can spider arms fit around leadscrews without interference?

5. **Motor access**:
   - If motors inside frame, how to service?
   - Is access panel needed on frame?
   - Or just remove Z-puck + motor as unit?

---

## Next Steps

1. [ ] Confirm Z-motor placement (vertical rod vs bottom rod)
2. [ ] Design Z-puck with motor mount INSIDE frame
3. [ ] Design spider bed with leadscrew clearance
4. [ ] Update ADR-005 with geometry decisions
5. [ ] Update config.py with Z-system parameters
6. [ ] Start Z-puck design in build123d
