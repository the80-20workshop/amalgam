# CAD File Organization

## Where Are the Parts?

### OLD Code (Ignore Import Errors)
```
cad/components/  # Legacy code, ignore VSCode errors
├── corner.py          # Old corner design
├── M12-corner.py      # Old M12 design
├── z-bracket.py       # Old Z-bracket design
├── adapter-puck.py    # Old adapter
├── electronic-tray.py  # Old electronics mount
├── x-carriage.py       # Old carriage
├── y-motor.py         # Old Y motor mount
└── main.py           # Old assembly script
```

### NEW Parts (Active Work) ✅
```
cad/parts/  # New clean code, no import errors
└── corner_1_front_left_z1.py  # NEW: Corner 1 (Front-Left + Z1) ✅ DESIGNED
```

## What We've Designed So Far

### ✅ Complete (1/9 = 11%)

**Corner 1 (Front-Left + Z1 motor)**
- File: `cad/parts/corner_1_front_left_z1.py`
- Features:
  - Integrated NEMA17 Z1 motor mount (42×42mm)
  - 4× M12 rod clamps (vertical L, vertical C-L, horizontal L)
  - Leadscrew vertical path clearance (10mm diameter)
  - 2× jam nut access holes per rod
  - Cable routing channels for Z-motor
  - Reinforcement fillets
- Status: Ready to generate STL

---

## Next Parts to Design (8/9 = 89%)

### Bottom Frame (Remaining 3/5 = 60%)

- [ ] **Corner 2**: Front-Right + Z2 motor integrated
- [ ] **Corner 3**: Back-Left (standard)
- [ ] **Corner 4**: Back-Right (standard)
- [ ] **Z-puck**: Back-Center on bottom horizontal rod + Z3 motor

### Top Frame (0/4 = 0%)

- [ ] **Top Corner TL**: Top-Left (standard)
- [ ] **Top Corner TR**: Top-Right (standard)
- [ ] **Top Corner BL**: Bottom-Left (standard)
- [ ] **Top Corner BR**: Bottom-Right (standard)

### Motion System (0/2 = 0%)

- [ ] **X-carriage**: Wade + hotend + bearings
- [ ] **Y-gantry**: Dual rod brackets + motors

### Extruder (0/1 = 0%)

- [ ] **Wade extruder**: Main body, gears, motor mount

### Bed Support (0/2 = 0%)

- [ ] **Spider hub**: Central triangle
- [ ] **Spider arms**: 3× interlocking arms

### Electronics (0/1 = 0%)

- [ ] **Brain Puck**: MKS SKIPR mount

---

## File Naming Convention

**What I did**: Long descriptive names
```
corner_1_front_left_z1.py  # Very descriptive
```

**What script expects**: Short names
```
corner_1.py  # Short
```

**Solution**: Try short name first, fall back to long name if not found

---

## Progress Summary

```
Corner 1:     ████████████████████ 100%  ✅
Corner 2:     ░░░░░░░░░░░░░░░░░░   0%
Corner 3:     ░░░░░░░░░░░░░░░░░░   0%
Corner 4:     ░░░░░░░░░░░░░░░░░   0%
Z-puck:       ░░░░░░░░░░░░░░░░░░   0%
Top corners:   ░░░░░░░░░░░░░░░░░   0%
Motion:        ░░░░░░░░░░░░░░░░   0%
Extruder:      ░░░░░░░░░░░░░░░░░   0%
Bed:           ░░░░░░░░░░░░░░░░░   0%
Electronics:    ░░░░░░░░░░░░░░░░░░   0%

TOTAL: ████░░░░░░░░░░░░░░░░  11%
```
