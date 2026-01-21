# Final Frame Parts Count

## Confirmed: 9 Parts Total

### Breakdown:

```
BOTTOM FRAME (Z-system):
┌─────────────────────────────────────────────┐
│                                             │
│  [Corner 1: Front L + Z1 motor]        │
│                                             │
│  [Corner 2: Front R + Z2 motor]        │
│                                             │
│  [Corner 3: Back L (standard)]           │
│                                             │
│           [Z-puck + Z3 motor on back rod]   │
│                                             │
│  [Corner 4: Back R (standard)]           │
└─────────────────────────────────────────────┘

TOP FRAME (Gantry):
┌─────────────────────────────────────────────┐
│  [Corner TL: Top-Left]                 │
│                                             │
│  [Corner TR: Top-Right]                │
│                                             │
│  [Corner BL: Bottom-Left]              │
│                                             │
│  [Corner BR: Bottom-Right]             │
└─────────────────────────────────────────────┘
```

### Parts List:

**Bottom Frame (5 parts):**
1. Corner 1: Front-Left + integrated Z1 motor mount
2. Corner 2: Front-Right + integrated Z2 motor mount
3. Corner 3: Back-Left (standard, no Z-motor)
4. Corner 4: Back-Right (standard, no Z-motor)
5. Z-puck: Back-center on bottom horizontal rod + Z3 motor mount

**Top Frame (4 parts):**
6. Corner TL: Top-Left (standard)
7. Corner TR: Top-Right (standard)
8. Corner BL: Bottom-Left (standard)
9. Corner BR: Bottom-Right (standard)

**Total: 9 parts**

---

## config.py Update

```python
# --- FRAME GEOMETRY ---
BUILD_VOLUME = {"X": 250, "Y": 250, "Z": 250}

# M12 SKELETON
SKELETON_Z = BUILD_VOLUME["Z"] + 50  # Reduced from 80
SKELETON_X = BUILD_VOLUME["X"] + (X_OVERHANG * 2) + 40
SKELETON_Y = BUILD_VOLUME["Y"] + 120

# CORNER COUNTS
BOTTOM_CORNERS = 4  # 2 Z-mount + 2 standard
TOP_CORNERS = 4     # All standard
TOTAL_CORNERS = 8

# Z-MOTOR POSITIONS
Z1_MOTOR = "front_left_corner"  # Integrated into Corner 1
Z2_MOTOR = "front_right_corner" # Integrated into Corner 2
Z3_MOTOR = "back_center_rod"     # On Z-puck (not corner!)

# Z-PUCK LOCATION
Z3_PUCK_LOCATION = "back_bottom_horizontal_rod"

# CORNER TYPES
FRONT_LEFT_CORNER = "Z_MOUNT_INTEGRATED"
FRONT_RIGHT_CORNER = "Z_MOUNT_INTEGRATED"
BACK_LEFT_CORNER = "STANDARD"
BACK_RIGHT_CORNER = "STANDARD"
```

---

## Next: Start Phase 2 Design

All planning complete. Ready to design:

1. [ ] Expand config.py with frame parameters
2. [ ] Design Corner 1 (Front L + Z1 mount)
3. [ ] Design Corner 2 (Front R + Z2 mount)
4. [ ] Design Corner 3 (Back L, standard)
5. [ ] Design Corner 4 (Back R, standard)
6. [ ] Design Z-puck (Back center, on bottom rod)
7. [ ] Design Top Corner TL
8. [ ] Design Top Corner TR
9. [ ] Design Top Corner BL
10. [ ] Design Top Corner BR
