# Frame Geometry Correction

## User Feedback - Frame Has 5 Vertical Rods

You're correct - I was wrong about 4 corners only!

### Actual Frame Structure (Cuboid)

```
FRONT EDGE:                    BACK EDGE:
[VFL] [VFC]  [VBC] [VRC]     [VBL] [VMC] [VBC] [VRC]
  |      |     |     |               |      |     |     |
  |      |     |     |               |      |     |     |
  |      |     |     |               |      |     |     |
  |      |     |     |               |      |     |     |
[VFL]  [VFC] [VBC]            [VBL]  [VBC]
  |      |     |               |      |     |
  |      |     |               |      |     |
  |      |     |               |      |     |
  |      |     |               |      |     |
[Front L]  [Front C]  [Front R]      [Back L]  [Back C]  [Back R]

Legend:
VFL/VFC = Vertical Front-Left
VFR/VFC = Vertical Front-Center (optional)
VFR/VRC = Vertical Front-Right
VBL/VBC = Vertical Back-Left
VMC/VBC = Vertical Back-Center
VBR/VRC = Vertical Back-Right
```

**Total: 8 Vertical Rods (not 4 corners!)**

```
FRONT: 4 vertical rods (L, C-L, C-R, R)
BACK: 4 vertical rods (L, C-L, C-R, R)
```

---

## Z-Motor Mounting Locations

### The Challenge
We need 3 Z-motors for symmetric triangle bed support:
- **Front Left**: Z1 motor
- **Front Right**: Z2 motor
- **Back Center**: Z3 motor

### Mounting Approach

**Option 1: All Z-motors on VERTICAL rods**
```
[Front Left Corner]: Integrated Z1 mount
  |
  | ← Corner bracket + motor mount
  |
  v
[Front Left Vertical Rod]

[Front Right Corner]: Integrated Z2 mount
  |
  | ← Corner bracket + motor mount
  |
  v
[Front Right Vertical Rod]

[Back Center Vertical Rod]: Separate Z3 mount
  |
  | ← Z-puck slides onto vertical rod
  |    (not integrated into corner)
  v
```

**Option 2: Front motors on vertical, Back motor on BOTTOM rod**
```
[Front Left Corner]: Integrated Z1 mount
  |
  | ← Corner bracket + motor mount
  |
  v
[Front Left Vertical Rod]

[Front Right Corner]: Integrated Z2 mount
  |
  | ← Corner bracket + motor mount
  |
  v
[Front Right Vertical Rod]

[Back Edge Bottom Rod]: Separate Z3 mount
  |
  | ← Z-puck slides onto horizontal rod
  |    (between Back L and Back R corners)
  v
```

---

## User's Suggestion (Option 2 Better?)

"Put two into the corners. And one onto the centre. We need a bracket (perhaps slide on prior to built frame or some way to mount to the M12 rod at the back)"

### Advantages of Back-Center Z-puck on BOTTOM rod:

1. **Easier assembly**:
   - Horizontal bottom rod is accessible
   - Z-puck can slide into position before corner assembly
   - No need to reach up and mount motor to vertical rod

2. **Better leadscrew access**:
   - Leadscrew goes UP through bottom frame area
   - Motor faces up, easier to service
   - Clearer cable path to bottom

3. **Simpler bracket design**:
   - Slides onto horizontal rod (like Voron motor on extrusion)
   - Don't need to clamp onto vertical rod with motor attached
   - Less complex geometry

4. **Triangle support clarity**:
   - All 3 bed supports are on bottom frame (physically intuitive)
   - Bed/spider assembly bolts to bottom area
   - Easier to visualize "3-point support"

---

## Clarified Corner Breakdown

### Total Parts: 4 Corners (not 4 corners + 1 Z-puck!)

```
CORNER 1: Front-Left (Z-mount integrated)
  - M12 vertical rod clamp (front L)
  - M12 horizontal rod clamp (front L)
  - M12 vertical rod clamp (front C-L)
  - Integrated Z1 motor mount

CORNER 2: Front-Right (Z-mount integrated)
  - M12 vertical rod clamp (front R)
  - M12 horizontal rod clamp (front R)
  - M12 vertical rod clamp (front C-R)
  - Integrated Z2 motor mount

CORNER 3: Back-Left (Standard, no Z-motor)
  - M12 vertical rod clamp (back L)
  - M12 horizontal rod clamp (back L)
  - M12 vertical rod clamp (back C-L)
  - No Z-motor mount

CORNER 4: Back-Right (Standard, no Z-motor)
  - M12 vertical rod clamp (back R)
  - M12 horizontal rod clamp (back R)
  - M12 vertical rod clamp (back C-R)
  - No Z-motor mount

Z-PUCK (Back-Center, separate part):
  - Clamps to back horizontal bottom rod
  - Z3 motor mount
  - Leadscrew path clearance
  - Slides into position before corner assembly
```

**Total parts**: 4 corner brackets + 1 Z-puck = 5 parts

---

## Frame Layout (Top View)

```
                    [Back Edge]
  +-------------------------------------------------+
  |  [Back L]   [Back C]   [Back R]   |
  |     |            |          |            |
  |  [Corner 3]  [Z-Puck]  [Corner 4]   |
  |     |            |          |            |
  |     |            |   [Motor Z3]           |
  |     |            |   (on Z-puck)          |
  |     |            |                        |
  |-----|------------|------------------------|
  |     |            |                        |
  | [Motor Z1]   [Motor Z2]               |
  | (Corner 1)   (Corner 2)              |
  |                                        |
  +-----|------------|------------------------+
        |  [Front C]    |
        |      |           |
        +-----|-----------+
              |
              |
        [Front Edge]

Note: Vertical center rods (Front C, Back C) shown but optional
```

---

## Triangle Bed Support (Symmetric)

### Support Points:
```
Point A (Z1): Front-Left corner
Point B (Z2): Front-Right corner
Point C (Z3): Back-Center (on Z-puck)

Bed/Spider bolts to:
- Front-Left edge (at Corner 1)
- Front-Right edge (at Corner 2)
- Back edge (at Z-puck)

Result: Symmetric triangle (2 front, 1 back center)
```

---

## Revised Parts Count

### Previous (Wrong):
```
8 corner brackets + 3 separate Z-pucks = 11 parts
```

### Current (Correct):
```
2 front Z-mount corners + 1 back-left corner + 1 back-right corner + 1 back-center Z-puck = 5 parts
```

**Reduction: 11 → 5 parts**

---

## User's Question: "Bound to three bed motor"

"back base/bottom M12 rod with bound to three bed motor"

I think you mean: **Z-puck mounted to back bottom rod, which connects to bed/spider**

The back-bottom rod:
- Runs horizontally between Back L and Back R corners
- Z-puck slides onto this rod
- Z3 motor mounted to Z-puck
- Leadscrew goes UP through frame
- Bed/spider attaches to Z3 nut

**This is the cleanest design!**

---

## Final Recommendation

### Option 2 Adopted:

**Front Z-motors**: Integrated into corner brackets (Front L + Front R)
- Corner 1: Front-Left + Z1 motor
- Corner 2: Front-Right + Z2 motor

**Back Z-motor**: Separate Z-puck on back bottom rod
- Z-puck: Slides onto back horizontal rod
- Z3 motor: Mounted to Z-puck
- Leadscrew: Goes UP through frame

**Back corners**: Standard (no Z-motor)
- Corner 3: Back-Left
- Corner 4: Back-Right

**Total parts**: 4 corners + 1 Z-puck = 5 parts

---

## config.py Update Needed

```python
# --- FRAME GEOMETRY ---
BUILD_VOLUME = {"X": 250, "Y": 250, "Z": 250}

# VERTICAL RODS (8 total)
FRONT_VERTICAL_RODS = 4  # FL, FCL, FCR, FR
BACK_VERTICAL_RODS = 4   # BL, BCL, BCR, BR
TOTAL_VERTICAL_RODS = 8

# M12 SKELETON
SKELETON_X = BUILD_VOLUME["X"] + (X_OVERHANG * 2) + 40
SKELETON_Y = BUILD_VOLUME["Y"] + 120
SKELETON_Z = BUILD_VOLUME["Z"] + 50  # Reduced from 80

# Z-SYSTEM
TRIPLE_Z = True
Z_MOUNT_PATTERN = "FRONT_CORNERS_BACK_BOTTOM"
# Front L + Front R: Integrated into corners
# Back C: Separate Z-puck on bottom rod

# Z-MOTOR POSITIONS
Z_MOTORS = [
    {"id": "Z1", "location": "front_left_corner", "type": "integrated"},
    {"id": "Z2", "location": "front_right_corner", "type": "integrated"},
    {"id": "Z3", "location": "back_center_rod", "type": "z_puck"}
]

# CORNER COUNT
CORNER_COUNT = 4  # Not 8!

# CORNER TYPES
FRONT_LEFT_CORNER = "Z_MOUNT_INTEGRATED"
FRONT_RIGHT_CORNER = "Z_MOUNT_INTEGRATED"
BACK_LEFT_CORNER = "STANDARD"
BACK_RIGHT_CORNER = "STANDARD"
```
