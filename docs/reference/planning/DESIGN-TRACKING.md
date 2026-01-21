# Phase 2: Design Tracking

## Design Checklist

### Foundation: Frame Geometry
- [x] Expand config.py with frame parameters
- [x] Finalize frame parts count (9 parts)
- [x] Document Z-system geometry
- [x] Document Z-Tilt leveling process

### Corner Bracket Designs
- [x] Corner 1: Front-Left (Z-mount integrated) ✅ DESIGNED
  - [x] M12 vertical rod clamp (front L)
  - [x] M12 horizontal rod clamp (front L)
  - [x] M12 vertical rod clamp (front C-L)
  - [x] Integrated Z1 motor mount
  - [x] Leadscrew path clearance (vertical)
  - [x] Cable routing channels
  - [x] Jam nut access points
  - [ ] Render in VSCode - VSCode shows errors for old code
  - [ ] Verify geometry
  - File: cad/parts/corner_1_front_left_z1.py

- [ ] Corner 2: Front-Right (Z-mount integrated)
  - [ ] M12 vertical rod clamp (front R)
  - [ ] M12 horizontal rod clamp (front R)
  - [ ] M12 vertical rod clamp (front C-R)
  - [ ] Integrated Z2 motor mount
  - [ ] Leadscrew path clearance (vertical)
  - [ ] Cable routing channels
  - [ ] Jam nut access points
  - [ ] Render in VSCode
  - [ ] Verify geometry

- [ ] Corner 3: Back-Left (standard)
  - [ ] M12 vertical rod clamp (back L)
  - [ ] M12 horizontal rod clamp (back L)
  - [ ] M12 vertical rod clamp (back C-L)
  - [ ] No Z-motor mount
  - [ ] Reinforcement structure
  - [ ] Jam nut access points
  - [ ] Render in VSCode
  - [ ] Verify geometry

- [ ] Corner 4: Back-Right (standard)
  - [ ] M12 vertical rod clamp (back R)
  - [ ] M12 horizontal rod clamp (back R)
  - [ ] M12 vertical rod clamp (back C-R)
  - [ ] No Z-motor mount
  - [ ] Reinforcement structure
  - [ ] Jam nut access points
  - [ ] Render in VSCode
  - [ ] Verify geometry

### Z-Puck Design
- [ ] Z-puck: Back-Center (on bottom horizontal rod)
  - [ ] M12 horizontal rod clamp
  - [ ] Integrated Z3 motor mount
  - [ ] Leadscrew path clearance (vertical)
  - [ ] Leadscrew nut trap
  - [ ] Cable routing to bottom
  - [ ] Slide mechanism (if adjustable height)
  - [ ] Render in VSCode
  - [ ] Verify geometry

### Spider Bed Support
- [ ] Spider Hub (center)
  - [ ] Triangle shape (equilateral, 120mm)
  - [ ] 3 arm mounting points (40mm spacing)
  - [ ] Interlocking design
  - [ ] Cable routing cutout
  - [ ] Render in VSCode
  - [ ] Verify geometry

- [ ] Spider Arms (3x)
  - [ ] Trapezoid shape (150mm length)
  - [ ] Bed mounting points (2 bolts per arm)
  - [ ] Leadscrew nut trap
  - [ ] Interlock with hub
  - [ ] Render in VSCode
  - [ ] Verify geometry

### Gantry (Top Frame)
- [ ] Corner TL: Top-Left (standard)
  - [ ] M12 vertical rod clamp (top L)
  - [ ] M12 horizontal rod clamp (top L)
  - [ ] Smooth rod mounting
  - [ ] Render in VSCode
  - [ ] Verify geometry

- [ ] Corner TR: Top-Right (standard)
  - [ ] M12 vertical rod clamp (top R)
  - [ ] M12 horizontal rod clamp (top R)
  - [ ] Smooth rod mounting
  - [ ] Render in VSCode
  - [ ] Verify geometry

- [ ] Corner BL: Bottom-Left (standard)
  - [ ] M12 vertical rod clamp (bottom L)
  - [ ] M12 horizontal rod clamp (bottom L)
  - [ ] Smooth rod mounting
  - [ ] Render in VSCode
  - [ ] Verify geometry

- [ ] Corner BR: Bottom-Right (standard)
  - [ ] M12 vertical rod clamp (bottom R)
  - [ ] M12 horizontal rod clamp (bottom R)
  - [ ] Smooth rod mounting
  - [ ] Render in VSCode
  - [ ] Verify geometry

### Motion System
- [ ] X-carriage
  - [ ] Bearing clamps (4x LM10UU)
  - [ ] Extruder Puck base
  - [ ] Wade extruder mounting
  - [ ] BLTouch/PINDA mount
  - [ ] Render in VSCode
  - [ ] Verify geometry

- [ ] Y-gantry brackets
  - [ ] Dual smooth rod support
  - [ ] Bearing clamps (8x LM10UU)
  - [ ] Motor mounts (X and Y)
  - [ ] Render in VSCode
  - [ ] Verify geometry

### Extruder
- [ ] Wade Main Body
- [ ] Wade Motor Mount
- [ ] Wade Idler Arm
- [ ] Wade Idler Tensioner
- [ ] Wade Gears (pinion + 47-tooth)
- [ ] Extruder Puck Adapter

### Electronics
- [ ] Brain Puck
  - [ ] MKS SKIPR mount pattern
  - [ ] Cable routing
  - [ ] Fan mounting (if needed)
  - [ ] Render in VSCode
  - [ ] Verify geometry

---

## Design Workflow

### For Each Part:
1. **Read config.py** for parameters
2. **Write build123d code** in `cad/parts/` directory
3. **Import config** values into part design
4. **Render in VSCode** using build123d extension
5. **Verify geometry**:
   - Check dimensions match config
   - Check for collisions
   - Check clearance
6. **Report back**:
   - "Part renders correctly, ready for next"
   - OR "Issue: need to adjust X by Ymm"
7. **Iterate** if needed

---

## Starting Point: Corner 1 (Front-Left + Z1)

### Parameters from config.py:
```
M12_FIT_DIA = 12.5  # 12.0 + 0.5 lumpy factor
X_OVERHANG = 50.0  # Wade overhang
CORNER_TYPE = "Z_MOUNT_INTEGRATED"
```

### Design Requirements:
- 4x M12 rod clamps (vertical L, vertical C-L, horizontal L, horizontal front C-L)
- Z1 NEMA17 motor mount
- Motor bolt pattern: NEMA17 standard
- Leadscrew clearance: Vertical path through frame
- Jam nut access: Easy access to all 4 clamps
- Cable routing: Channel for motor wires
- Wall thickness: 4-5mm
- Infill: 40-50%
- Material: PETG or ABS

---

## Current Status

**Phase 2 Active**: Designing corner brackets

**Working on**: Corner 1 (Front-Left + Z1 integrated)

**Next**: After Corner 1 complete → Corner 2 (Front-Right + Z2)
