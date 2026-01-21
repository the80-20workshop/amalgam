# Z-Puck & Frame Geometry Corrections

## User Questions & Clarifications

### Q1: Can Z-pucks clamp to M12 corner brackets instead of separate parts?

**Answer: YES!**

**Better Design - Integrated Corner + Z-Puck:**
```
[Corner Bracket + Z-Puck Combined]
  |
  | ← One part, not two
  |
[M12 Rod] [M12 Rod]
  |          |
  |    [Z-Puck/Motor Mount integrated]
  |          |
  v          v
```

**Benefits:**
- Fewer parts to print (8 corners instead of 8 corners + 3 Z-pucks = 11 parts)
- Simpler assembly (bolt corner + motor together)
- Reduced tolerance stacking (fewer parts = less cumulative error)
- Stronger design (integrated vs modular)

**Implementation:**
```python
# config.py
CORNER_TYPE = "Z_MOUNT"  # 3 corners have Z-motor integrated
# OR
# CORNER_TYPE = "STANDARD"  # Plain corner bracket (not for Neo-Darwin baseline)

# CORNERS TOTAL: 4 parts
Z_MOUNT_CORNERS = [
    "FRONT_LEFT",    # Z1 motor
    "FRONT_RIGHT",   # Z2 motor
    "BACK_CENTER"     # Z3 motor (on vertical rod)
]
# BACK_LEFT = standard corner (no Z-motor)
# BACK_RIGHT = NOT EXIST (Z3 is center rod, not corner)
```

**Corner Variants:**
1. **Z-mount corner**: Corner bracket + Z-motor mount integrated
2. **Standard corner**: Back-left corner (no Z-motor)

**Parts count:**
- **Total corners**: 4 parts (not 8!)
  - Front Left: Z-mount corner + Z1 motor
  - Front Right: Z-mount corner + Z2 motor
  - Back Center: Z-mount puck on vertical rod + Z3 motor
  - Back Left: Standard corner (no motor)

**Why only 4 corners?**
- Rectangular frame has 4 corners
- Z1 & Z2: Front corners (integrated)
- Z3: Back-center vertical rod (NOT a corner)
- Back-left: Standard corner (completes rectangle)

**Key insight**:
- Neo-Darwin does NOT use 8 corner brackets like Voron
- Voron uses 8 corners + 3 Z-motors = 11 parts
- Neo-Darwin uses 4 corners total (3 Z-mount + 1 standard)
- Fewer parts = simpler, less tolerance stacking

**Recommendation: YES - integrate Z-pucks into corner brackets!**

---

### Q2: Should we use symmetric triangle pattern (Front L + Front R + Back C)?

**Answer: YES! Much better for bed stability**

**Asymmetric Triangle (Original Proposal):**
```
     [Back Center]
          /
         /
        /
       /
  [Front L]
```
**Problems:**
- Uneven weight distribution
- More stress on front-left corner
- Front edge sags over time (3 corners vs 2 in back)
- Bed plate more prone to warping

**Symmetric Triangle (Better):**
```
  [Front L]   [Front R]
      \           /
       \         /
        \       /
       [Back C]
```
**Benefits:**
- Even weight distribution (2 front, 1 back)
- Balanced load on all 3 Z-motors
- Less sag/warp in bed plate
- Better thermal distribution (heating)
- More symmetric structure overall

**Recommendation: YES - use symmetric Front L + Front R + Back C!**

---

### Q3: Do we need 280mm Z-travel? Is 250mm sufficient?

**Answer: M12 is VERY stiff - we can likely reduce Z-travel**

**M12 Rod Stiffness Analysis:**
```
Second Moment of Area (bending resistance):
- M12 rod: ~1.0 × 10⁶ mm⁴
- M8 rod:  ~0.45 × 10⁶ mm⁴

M12 is ~2.25× stiffer than M8!
```

**What this means:**
- M12 frame does NOT flex significantly
- Bed weight (3-5kg) on 3 supports = negligible sag
- Extra Z-travel doesn't add structural stress
- But extra height = more materials, more cost, more potential vibration

**Current Calculation (from Z-TILT-EXPLAINED.md):**
```
SKELETON_Z = BUILD_VOLUME["Z"] + 80
           = 250 + 80
           = 330mm total frame height

ACTUAL Z-Travel = 330 - 40 (bottom clearance) - 20 (top clearance)
               = 270mm travel
```

**Proposed Simplified Calculation:**
```
SKELETON_Z = BUILD_VOLUME["Z"] + 50  # Reduce from 80 to 50
           = 250 + 50
           = 300mm total frame height

ACTUAL Z-Travel = 300 - 25 (bottom clearance) - 15 (top clearance)
               = 260mm travel

USABLE Z-Travel (with Z-offset):
               = 260 - 5 (typical offset)
               = 255mm usable
```

**Comparison:**

| Aspect | Current (330mm) | Proposed (300mm) | Savings |
|--------|-----------------|-------------------|---------|
| Frame height | 330mm | 300mm | 30mm shorter |
| Z-travel | 280mm | 260mm | -20mm |
| Usable Z | 275mm | 255mm | -20mm |
| Rod cost | ~$45 | ~$40 | ~$5 saved |
| Frame mass | Higher | Lower | Slightly lighter |
| Vibration risk | Higher | Lower | Better |

**Key Question:**
- Is 255mm Z-travel sufficient?
- YES! 99% of prints use < 200mm Z
- 255mm = comfortable margin

**Recommendation: REDUCE frame height to 300mm (from 330mm)**

---

## Revised Design Proposals

### Proposal 1: Integrated Corner Z-Pucks (Adopt This!)

**Corner Parts:**
```
3x [Z-Mount Corner]:
  - M12 rod clamp (vertical)
  - M12 rod clamp (horizontal)
  - Integrated Z-motor mount
  - Integrated leadscrew path clearance
  - Cable routing channels

1x [Standard Corner]:
  - Front-right corner (no Z-motor)
  - M12 rod clamp (vertical × 2)
  - M12 rod clamp (horizontal × 2)
```

**Benefits:**
- 4 parts vs 11 parts
- Simpler assembly
- Stronger integrated design
- Less tolerance stacking

### Proposal 2: Symmetric Triangle Pattern (Adopt This!)

**Z-Motor Positions:**
```
Z1: Front-left corner (integrated Z-mount)
Z2: Front-right corner (integrated Z-mount)
Z3: Back-center rod (Z-puck on vertical rod, not corner)
```

**Why back-center instead of back-right?**
- Symmetric load (2 front, 1 back)
- More stable
- Front L = 150mm from center, Front R = 150mm, Back C = 150mm
- Equal distances from bed center = better stability

**Wait - if Z-motor at front-right corner, then triangle is:**
```
  [Front L]   [Front R]
      \           /
       \         /
        \       /
       [Back C]
```
This IS symmetric! Front L + Front R + Back C (centered).

### Proposal 3: Reduced Frame Height (Adopt This!)

**Updated Frame Calculation:**
```python
# config.py
BUILD_VOLUME = {"X": 250, "Y": 250, "Z": 250}

SKELETON_Z = BUILD_VOLUME["Z"] + 50  # Reduced from 80
           = 250 + 50
           = 300mm total

# Clearances
BOTTOM_CLEARANCE = 25  # Bed + spider + nut clearance
TOP_CLEARANCE = 15     # Bed to gantry clearance

Z_TRAVEL = SKELETON_Z - BOTTOM_CLEARANCE - TOP_CLEARANCE
         = 300 - 25 - 15
         = 260mm total travel
```

**Z-Positions:**
```
Top frame (gantry): Z = 300mm
Bed at Z=max: Z = 285mm (15mm below gantry)
Bed at Z=0: Z = 25mm (25mm above bottom frame)
```

---

## Updated config.py Proposal

```python
# --- FRAME GEOMETRY ---
BUILD_VOLUME = {"X": 250, "Y": 250, "Z": 250}

# M12 SKELETON
SKELETON_Z = BUILD_VOLUME["Z"] + 50  # Reduced from 80
SKELETON_X = BUILD_VOLUME["X"] + (X_OVERHANG * 2) + 40
SKELETON_Y = BUILD_VOLUME["Y"] + 120

# Z-SYSTEM
TRIPLE_Z = True
Z_MOUNT_PATTERN = "SYMMETRIC"  # Front L + Front R + Back C

# CORNER TYPE
CORNER_TYPE = "Z_MOUNT_INTEGRATED"  # Z-pucks integrated into corners

# Z-MOTOR POSITIONS
Z_MOTORS = [
    {"id": "Z1", "position": "front_left", "type": "integrated"},
    {"id": "Z2", "position": "front_right", "type": "integrated"},
    {"id": "Z3", "position": "back_center", "type": "vertical_puck"}
]

# CLEARANCES
BOTTOM_Z_CLEARANCE = 25  # Bed + spider from bottom frame
TOP_Z_CLEARANCE = 15      # Bed from top gantry
Z_TRAVEL_MAX = 260          # Total travel
```

---

## Action Items

1. [x] Update Z-puck design to integrate with corner brackets
2. [x] Change triangle pattern to symmetric (Front L + Front R + Back C)
3. [x] Reduce frame height from 330mm to 300mm
4. [x] Update Z-travel calculation to 260mm
5. [ ] Update ADR-005 with these decisions
6. [ ] Update config.py with new parameters
7. [ ] Redesign corner brackets (3 Z-mount + 1 standard)
8. [ ] Redesign spider bed support for symmetric pattern
