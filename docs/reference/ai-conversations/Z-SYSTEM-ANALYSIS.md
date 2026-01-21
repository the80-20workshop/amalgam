# Z-System Frame Geometry Analysis

## Key Questions to Answer

1. **Z-motor location:** Where do 3 Z-motors mount?
2. **Leadscrew path:** Inside or outside the frame?
3. **Bed position:** Where does bed sit and how does it move?
4. **Z-range:** What's the actual usable Z-height?
5. **Z-tilt reference:** Where does bed meet gantry?

---

## Voron Trident Reference (Research Needed)

Based on Voron Trident architecture:

### Z-Motor Layout
```
         [Top Frame - Gantry]
                |
                |
         Z2 Motor Z3 Motor
         (Back)      (Back Center)
                |
                |
    [Bed rises UP to meet gantry]
                |
                |
         Z1 Motor Z2 Motor
       (Front L) (Front R)
                |
         [Bottom Frame]
```

**Voron Implementation:**
- **3 Z-motors at bottom frame corners**
- **Leadscrews go UP through frame interior**
- **Motors bolt TO extrusion frame (outside corner)**
- **Bed attached to leadscrew nuts, rises UP**
- **Gantry fixed at top frame**
- **Z=0**: Bed at bottom
- **Z=max**: Bed touches gantry at top

### Voron Bed Movement
```
Bottom Frame (Z=0)
  |
  | ← Leadscrew (fixed, motor at bottom)
  |
  v
Bed + Spider (MOVES UP)
  |
  | ← Leadscrew passes through spider nut
  |
  v
Top Frame + Gantry (Z=max, FIXED)
```

---

## Neo-Darwin Frame Differences

**Voron:**
- Frame = Aluminum extrusions (2020, 2040)
- Motors bolt directly to extrusion holes
- Leadscrew path through open frame interior

**Neo-Darwin:**
- Frame = M12 threaded rods (solid bars)
- No mounting holes on rods
- Need Z-pucks to slide over M12 rods
- Leadscrew path = inside or outside frame?

---

## Proposed Neo-Darwin Z-System Layout

### Option A: Corners + Back Center (Recommended)

**Z-Puck Positions:**
```
         [Top Frame Rods - Gantry]
                |
                |
       [Puck Z2]   [Puck Z3]
       (Back L)      (Back C)
                |
                |
    [Bed + Spider rises UP]
                |
                |
       [Puck Z1]   [Puck Z2]
       (Front L)     (Front R)
                |
         [Bottom Frame Rods]
```

**Positions:**
- **Z1**: Front-left vertical rod
- **Z2**: Back-left vertical rod
- **Z3**: Back-center vertical rod (not corner!)

**Why not front-right corner?**
- Spider bed is triangular
- 3 support points = triangle
- Two back corners + front left = stable triangle
- OR: Front L + Front R + Back Center

**Triangle Pattern:**
```
     [Back L]      [Back Center]
          \           /
           \         /
            \       /
             \     /
              \   /
           [Front L]
```

### Motor Mounting (Z-Puck Design)

**Option A1: Motors OUTSIDE frame**
```
         [M12 Rod]
             |
    [Z-Puck]---[MOTOR]
             |
         [Leadscrew]
             |
        [Inside Frame]
```

**Pros:**
- Easier motor access
- More leadscrew clearance inside frame
- Cleaner cable routing

**Cons:**
- Motors extend outside frame width
- Less compact footprint

**Option A2: Motors INSIDE frame**
```
         [M12 Rod]
             |
             |
    [Z-Puck]---[Leadscrew]
             |
           [MOTOR]
        [Inside Frame]
```

**Pros:**
- Compact footprint
- Motors protected by frame

**Cons:**
- Motor interferes with bed movement
- Limited leadscrew space
- Harder to service motors

### Recommendation: **Motors OUTSIDE frame**

---

## Bed Position & Movement

### Bottom Frame Clearance
```
Bottom Frame (Z=0)
  |
  | ← 30-40mm clearance for Spider + leadscrew nuts
  v
[Spider + Bed at lowest point]
```

**Requirements:**
- Bottom frame rods at Z=0
- Bed/spider sits ABOVE bottom frame
- Need 30-40mm clearance for spider + nuts
- Bed moves UP from there

### Top Frame Clearance
```
[Spider + Bed at Z=max]
  | ← 10-20mm clearance to top frame gantry
  v
Top Frame (Z=250)
```

**Requirements:**
- Bed stops 10-20mm below top frame
- Prevents bed from hitting gantry
- Z-travel = 250mm - 50mm = 200mm usable

**Wait - This is wrong!**

Let me recalculate...

---

## Corrected Frame Geometry

### Frame Dimensions (from config.py)
```
BUILD_VOLUME = 250mm³

SKELETON_Z = BUILD_VOLUME["Z"] + 80
            = 250 + 80
            = 330mm (total frame height)
```

### Where does the extra 80mm go?
From MANIFESTO.md: "Z-Puck stacking"

```
Top Frame (Gantry)
  |
  | ← 250mm usable Z-travel
  |
  v
[Bed + Spider at Z=250]
  |
  | ← 30mm for spider + leadscrew nut below bed
  v
[Bottom Frame Z=320]
  |
  | ← 10mm bottom Z-puck clearance
  v
Total: 330mm
```

### Bed Movement
```
Z=0:  Bottom of usable volume (30mm above bottom frame)
Z=250: Top of usable volume (bed near gantry)

Actual Z-travel: 250mm
Frame height: 330mm
Bed offset from bottom frame: 30mm
Clearance to top gantry: 50mm
```

---

## Z-Tilt Reference

### How Z-Tilt Works
```
Gantry: [Fixed plane]
           |
           | ← Z-probe measures distance to bed
           v
Bed:    [Plane to be leveled]

Klipper Z-Tilt:
1. Probe 3 points on bed
2. Calculate tilt relative to gantry
3. Adjust 3 Z-motors to make bed parallel
4. Repeat until tilt < 0.01mm
```

### Reference Plane
- **Gantry = Reference plane** (fixed by X/Y smooth rods)
- **Bed = Plane to adjust** (via 3 Z-motors)
- **Z-probe measures perpendicular distance** between planes

### Bed Position During Z-Tilt
- Bed moves UP and DOWN slightly during calibration
- After calibration, bed is parallel to gantry
- Z=0 is set when nozzle just touches bed at center

---

## Leadscrew Path Decision

### Option 1: Leadscrews INSIDE frame rectangle
```
[M12 Rod] [M12 Rod]
   |          |
   | [Leadscrew path inside]
   |          |
   |          |
[M12 Rod] [M12 Rod]
```

**Pros:**
- Compact footprint
- Protected leadscrews
- Matches Voron design

**Cons:**
- May interfere with bed spider
- Limited clearance

### Option 2: Leadscrews OUTSIDE frame rectangle
```
[Leadscrew] [M12 Rod] [M12 Rod]
   |            |          |
   |            |          |
   |            |          |
   |            |          |
[Leadscrew] [M12 Rod] [M12 Rod]
```

**Pros:**
- More bed clearance inside frame
- Easier cable routing

**Cons:**
- Wider footprint
- Leadscrews exposed

### Recommendation: **INSIDE frame (like Voron)**

But ensure:
- Spider design has leadscrew clearance
- Bed doesn't hit leadscrews at Z=0
- Cable routing along frame edges

---

## Z-Puck Height Adjustment

### Question: Where along vertical rod?

**Option 1: At very bottom**
```
[M12 Rod]
  |
  |
[Z-Puck] ← Motor mount here
  |
  |
[Bottom Frame Rods]
```

**Pros:**
- Maximum Z-travel
- Motors at frame bottom (stable)

**Cons:**
- Hard to access motors
- Cables must go up and back down

**Option 2: Slightly above bottom**
```
[M12 Rod]
  |
  |
[Bottom Frame Rods]
  |
  |
[Z-Puck] ← Motor mount 10-20mm above bottom
```

**Pros:**
- Motor access easier
- Cable routing simpler

**Cons:**
- Reduces Z-travel slightly

### Recommendation: **At bottom frame level**

But make Z-puck extend BELOW bottom frame rods to capture motor, OR mount Z-puck TO bottom frame rods (not vertical rods).

Actually, wait...

---

## Alternative: Z-Pucks on Bottom Frame, NOT Vertical Rods

### What if Z-motors mount to BOTTOM FRAME rods?

```
[Top Frame]
  |
  |
[Z1 Motor]  [Z2 Motor]  [Z3 Motor]
   |             |             |
[Bottom Frame Rods] ← Motors bolt here
   |             |             |
   |             |             |
[Leadscrews go UP through frame]
```

**Advantages:**
- Z-pucks mount to HORIZONTAL M12 rods (easier)
- Motors at bottom (stable)
- Leadscrews go UP through interior
- Matches Voron approach better

**Z-Puck on Bottom Frame:**
```
[Bottom Frame M12 Rod]
  |
[Z-Puck] ← Clamps to bottom rod
  |      |
  |   [MOTOR]
  |
[Leadscrew goes UP]
```

**Disadvantage:**
- Need to design Z-puck to clamp HORIZONTALLY to bottom rod
- M12 rod is threaded - clamping might be tricky
- Leadscrew needs to pass through bottom frame plane

---

## Open Questions for Design

1. **Z-motor mounting:**
   - Option A: Z-pucks on VERTICAL rods at bottom
   - Option B: Z-pucks on BOTTOM HORIZONTAL rods
   - Which is easier to build?

2. **Leadscrew path:**
   - Inside frame or outside?
   - Inside matches Voron, but check clearance

3. **Bed clearance:**
   - Bed at Z=0 needs 30-40mm clearance from bottom
   - Bed at Z=max needs 10-20mm clearance from top gantry
   - Is 330mm frame height sufficient?

4. **Z-motor positioning:**
   - 3 motors: Front L + Back L + Back C?
   - Or: Front L + Front R + Back C?
   - What's the most stable triangle?

5. **Z-travel:**
   - Claimed: 250mm Z-travel
   - Actual: 250mm - bottom clearance - top clearance
   - What's the REAL usable Z-height?

---

## Need: Voron Trident CAD Review

Before committing to design, we should:
1. Find Voron Trident CAD/model
2. Review their exact Z-system implementation
3. Understand bed/gantry clearances
4. Learn from their motor mounting approach

Where can we find Voron Trident CAD?
- GitHub: https://github.com/VoronDesign/Voron-Trident
- CAD source files in repository
- Can import to CAD viewer or compare dimensions

---

## Next Steps

1. [ ] Research Voron Trident Z-system CAD
2. [ ] Decide Z-motor mounting approach (vertical vs bottom rod)
3. [ ] Decide leadscrew path (inside vs outside)
4. [ ] Calculate actual Z-travel with frame height
5. [ ] Update ADR-005 with geometry decisions
6. [ ] Update config.py with Z-system parameters
7. [ ] Start designing Z-pucks
