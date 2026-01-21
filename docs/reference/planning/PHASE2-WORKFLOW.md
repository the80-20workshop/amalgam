# Phase 2: config.py Expansion & Part Design Workflow

## Corner Bracket Diagonal Support Decision

### Question: Do we need fishing line diagonals like original Darwin?

**Original Darwin (2007) Approach:**
- Used fishing line/string diagonally across corners
- Tuned tension to keep frame square
- Necessary because M8 rods were flexible and hard to square

**Modern M12 Reality:**
- M12 rods are 2.25× stiffer than M8
- Jam nuts at each joint prevent movement
- CAD-designed corner brackets have precise angles (90°)
- Triple-Z system provides additional rigidity
- Klipper Z-Tilt can compensate for minor misalignment

### Recommendation: **Optional Diagonal Supports**

**Baseline (Tier 1-3):**
- Corner brackets designed WITHOUT diagonal attachment points
- Rely on:
  - Precise 3D-printed angles
  - Jam nuts on M12 joints
  - Careful assembly with square during build
  - M12 rod stiffness

**Optional Upgrade (Tier 4 or Difficulty Squaring):**
- Corner brackets include optional diagonal attachment holes
- Fishing line or steel cable diagonals can be added if needed
- Provides "safety net" for difficult assembly
- Not required for most builders

**Rationale:**
1. **Simplicity first**: Don't complicate baseline for all builders
2. **Modern materials**: M12 + precision CAD make diagonals unnecessary
3. **Fallback available**: Optional holes if builder struggles with squaring
4. **Historical context**: Darwin needed them, Mendel Revisited doesn't

---

## Design Workflow Proposal

### Option A: Complete Parts List → Sequential Design
```
1. Create complete printed parts list
2. Work through parts one-by-one
3. Design corner bracket → render → verify
4. Design Z-puck → render → verify
5. etc.
```

**Pros:**
- Focused, one part at a time
- Easy to track progress
- Less overwhelming

**Cons:**
- May discover dimension conflicts late
- Hard to see system-wide relationships
- Slower iteration

### Option B: System-First → Parallel Design (Recommended)
```
1. Expand config.py with ALL parameters first
2. Design foundation parts (corners, frame)
3. Design motion parts (bearings, carriages)
4. Design functional parts (Z-pucks, pucks, Wade)
5. Iterate together as system
```

**Pros:**
- See how parts interact early
- Parametric relationships clear
- Catch dimension conflicts early
- System-focused thinking

**Cons:**
- More open loops initially
- Need to track multiple parts

### Recommended Workflow: Option B with Iterative Feedback

```
ITERATION 1: Foundation
├─ Expand config.py (all frame dimensions)
├─ Design corner brackets (with optional diagonal holes)
├─ Render in VSCode → Verify geometry
├─ Adjust config if needed → Re-render
└─ Mark brackets as "foundation complete"

ITERATION 2: Motion System
├─ Add bearing clamp dimensions to config.py
├─ Design X-carriage (bearing clamps + Extruder Puck)
├─ Design Y-gantry (dual rod support)
├─ Render → Check fit with corner brackets
└─ Iterate

ITERATION 3: Z-System
├─ Add Z-puck parameters to config.py
├─ Design Z-puck (motor mount + nut trap)
├─ Check alignment with corner brackets
├─ Render → Verify
└─ Iterate

ITERATION 4: Functional Systems
├─ Add Brain Puck parameters
├─ Design Brain Puck
├─ Design Spider Bed Support (hub + arms)
├─ Design Wade Extruder parts
├─ Render → System-wide fit check
└─ Iterate

ITERATION 5: Refinement
├─ Check all parts in CAD together
├─ Verify mounting bolt patterns
├─ Check clearances and collisions
├─ Final config.py values
└─ Generate final STL exports
```

### Each Part Design Cycle:
```python
# 1. Reference config.py
from config import M12_FIT_DIA, BUILD_VOLUME, etc.

# 2. Write build123d code
def corner_bracket():
    rod_hole = builder.make_cylinder(
        diameter=M12_FIT_DIA,
        height=40
    )
    # ... rest of design

# 3. Render in VSCode
# → Visual check in 3D viewer

# 4. Report back
# → "Corner bracket renders correctly, rod holes line up"
# → "Issue: Need to increase bolt hole spacing by 2mm"

# 5. Update config or code
# → Adjust CORNER_BOLT_SPACING = 52.0 (was 50.0)

# 6. Re-render → Verify fix
```

---

## Complete Printed Parts List

### Foundation (Frame & Structure)
- [ ] Corner Brackets (8x) - frame vertices
- [ ] Frame Reinforcements (optional) - X/Y bracing

### Motion System
- [ ] X-Carriage (1x)
  - Bearing clamps (4x)
  - Extruder Puck base
- [ ] Y-Gantry Brackets (2x)
  - Bearing clamps (4x per side)
  - Motor mounts (X and Y)

### Z-System
- [ ] Z-Pucks (3x)
  - Motor mount
  - Leadscrew nut trap
  - M12 rod clamp

### Bed Support
- [ ] Spider Hub (1x)
- [ ] Spider Arms (3x)

### Electronics Mounting
- [ ] Brain Puck (1x)
- [ ] Wire management clips (10-20x)

### Extruder & Hotend
- [ ] Wade Extruder Main Body (1x)
- [ ] Wade Motor Mount (1x)
- [ ] Wade Idler Arm (1x)
- [ ] Wade Idler Tensioner (1x)
- [ ] Wade Gear Cover (optional, 1x)
- [ ] Extruder Puck Adapter (Wade to Puck)

### Z-Probe
- [ ] BLTouch Mount (1x) - for Wade carriage
- [ ] PINDA Mount (alternative, 1x)

### Motion Pucks (Optional Tinker)
- [ ] MGN12 Rail Mounts (if using rails, 6x)

### Tool Pucks (Future)
- [ ] Pen Plotter Puck
- [ ] Laser Puck
- [ ] CNC Puck

---

## config.py Expansion Checklist

### Frame Parameters
```python
# M12 Skeleton
M12_NOMINAL_DIA = 12.0
LUMPY_FACTOR = 0.5
M12_FIT_DIA = 12.5

# Frame Dimensions (calculated)
SKELETON_X = 540  # From BUILD_VOLUME + overhangs
SKELETON_Y = 370
SKELETON_Z = 330

# Corner Bracket
CORNER_BRACKET_HEIGHT = 40
CORNER_BOLT_SPACING = 52
CORNER_DIAGONAL_SUPPORT = True  # Optional holes
```

### Motion Parameters
```python
# Linear Motion
SMOOTH_ROD_DIA = 10.0
BEARING_TYPE = "LM10UU"
X_ROD_LENGTH = 370
Y_ROD_LENGTH = 350
Z_ROD_LENGTH = 320

# Carriage
X_CARRIAGE_WIDTH = 120
X_CARRIAGE_LENGTH = 80
BEARING_SPACING = 60
```

### Z-System Parameters
```python
# Triple-Z
TRIPLE_Z = True
Z_PUCK_HEIGHT = 60
MOTOR_OFFSET_X = 30
MOTOR_OFFSET_Y = 30
LEADSCREW_DIA = 8
LEADSCREW_PITCH = 2
```

### Puck Parameters
```python
# Puck Interfaces
PUCK_BOLT_PATTERN = "M5"  # M5 for Z/Brain, M4 for Extruder
PUCK_ROD_CLAMP_WIDTH = 40
PUCK_ROD_CLAMP_HEIGHT = 30

# Brain Puck
BOARD_TYPE = "MKS_SKIPR"
BOARD_DIMENSIONS = [100, 100]
BOARD_MOUNT_HOLES = [[20, 20], [20, 80], [80, 20], [80, 80]]

# Extruder Puck
EXTRUDER_TYPE = "WADE"
HOTEND_TYPE = "V6"
GROOVEMOUNT_DIA = 16
Z_PROBE_OFFSET = [35, 0]
```

### Spider Parameters
```python
# Spider Bed Support
SPIDER_ARM_LENGTH = 150
SPIDER_HUB_SIZE = 120
SPIDER_BOLT_PATTERN = "M6"
SPIDER_INTERLOCK = True
```

---

## Starting Recommendation

**Begin with:**
1. **Corner brackets** - Foundation, defines frame geometry
2. **config.py expansion** - Add all frame/bracket parameters first
3. **Render and verify** - Check angles, bolt holes, M12 fit

**Then expand to:**
4. **X-carriage** - Motion system foundation
5. **Z-pucks** - Triple-Z mounting
6. **Brain pucks** - Electronics mounting

**Keep in mind:**
- Parts relate to each other (corner brackets define frame, frame affects all others)
- Iterate quickly - small changes, render, verify
- Report back often - "corner brackets done, moved to X-carriage"
- Optional features (diagonal support) don't block baseline

---

## Questions to Answer Before Starting ✅ ANSWERED

1. ~~**Corner diagonal support**: Add optional holes to all corners?~~ → **NO - M12 is stiff enough, optional diagonals not needed for baseline**
2. ~~**Design workflow**: System-first (Option B) or sequential (Option A)?~~ → **System-first (Option B) adopted**
3. ~~**config.py expansion**: Start with frame parameters, add others as needed?~~ → **Yes, start with frame**
4. ~~**Print order**: Design in system but can print in any order?~~ → **Yes, design system, print any order**

## Z-System Geometry Decisions ✅ ADOPTED

Based on Voron research and user feedback:

1. **Z-motor placement**: Integrated into corner brackets (not separate Z-pucks)
   - 3 corners have Z-mount, 1 corner is standard
   - Parts: 4 total vs 11 (corners + separate Z-pucks)

2. **Triangle pattern**: Symmetric Front L + Front R + Back Center
   - Better stability, even weight distribution
   - Less bed sag/warp than asymmetric pattern

3. **Frame height**: Reduced from 330mm to 300mm
   - M12 is very stiff, extra height not needed for rigidity
   - Z-travel: 280mm → 260mm (still sufficient)
   - Savings: ~$5 on rods, lighter frame, less vibration

4. **Leadscrew path**: Inside frame (Voron-like)
   - Motors face inward on integrated corner mounts
   - Leadscrews go UP through frame interior
   - Spider bed support designed with 40mm clearance

5. **Z-Tilt leveling**:
   - BLTouch calibrates bed level (NOT endstop)
   - Bed moves up/down via motors, Z-travel in Klipper config
   - Max-Z: Physical calibration once, Bed level: Periodic Z_TILT_ADJUST

Documents:
- Z-TILT-EXPLAINED.md: Full Z-Tilt how it works
- Z-PUCK-CLARIFICATIONS.md: Design decisions and recommendations