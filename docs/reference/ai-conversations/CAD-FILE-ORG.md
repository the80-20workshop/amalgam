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

### NEW Parts (Active Work)
```
cad/parts/  # New clean code, no import errors
└── corner_1_front_left_z1.py  # NEW: Corner 1 (Front-Left + Z1)
```

## What We've Designed So Far

✅ **Corner 1 (Front-Left + Z1 motor)** - Designed
- File: `cad/parts/corner_1_front_left_z1.py`
- Features:
  - Integrated NEMA17 Z1 motor mount (42×42mm)
  - 4× M12 rod clamps
  - Leadscrew vertical path clearance (10mm diameter)
  - 2× jam nut access holes per rod
  - Cable routing channels
  - Reinforcement fillets

## Next Parts to Design

From FINAL-FRAME-PARTS.md, we need  design:

### Bottom Frame (5 parts total)
- [x] **Corner 2**: Front-Right + Z2 motor integrated
- [x] **Corner 3**: Back-Left (standard)
- [x] **Corner 4**: Back-Right (standard)
- [x] **Z-puck**: Back-Center on bottom horizontal rod + Z3 motor

### Top Frame / Gantry (4 parts total)
- [ ] **Top Corner TL**: Top-Left (standard)
- [ ] **Top Corner TR**: Top-Right (standard)
- [ ] **Top Corner BL**: Bottom-Left (standard)
- [ ] **Top Corner BR**: Bottom-Right (standard)

### Motion System (later)
- [ ] X-carriage
- [ ] Y-gantry brackets
- [ ] Wade extruder parts
- [ ] Electronics/Brain Puck

### Bed Support (later)
- [ ] Spider Hub
- [ ] Spider Arms (3×)

---

## Naming Convention

**My mistake**: I named files with full descriptions
```
corner_1_front_left_z1.py  # Too long
```

**Better naming** for generate.sh script:
```
corner_1.py               # Corner 1 (Front-Left + Z1)
corner_2.py               # Corner 2 (Front-Right + Z2)
corner_3.py               # Corner 3 (Back-Left)
corner_4.py               # Corner 4 (Back-Right)
z_puck.py                  # Z-puck (Back-Center + Z3)
spider_hub.py             # Spider bed hub
spider_arm.py              # Spider arm
top_corner_tl.py           # Top corner TL
top_corner_tr.py           # Top corner TR
top_corner_bl.py           # Top corner BL
top_corner_br.py           # Top corner BR
```

**Or keep full names** and update generate.sh:
```
corner_1_front_left_z1.py   # Full description
```

I'll use full names (more descriptive).

---

## Status Summary

**Complete**: 1/9 frame parts (11%)
**In Progress**: 0/9
**Pending**: 8/9 (89%)

**Total Progress**:
```
Corner 1:     ████████████████████ 100%  ✅
Corner 2:     ░░░░░░░░░░░░░░░░░░   0%
Corner 3:     ░░░░░░░░░░░░░░░░░░   0%
Corner 4:     ░░░░░░░░░░░░░░░░░░   0%
Z-puck:       ░░░░░░░░░░░░░░░░░░   0%
Top corners:   ░░░░░░░░░░░░░░░░░░   0%
```
