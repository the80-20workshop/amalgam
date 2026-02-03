# Amalgam Calibration Cheat Sheet

Quick reference for Klipper calibration commands. For detailed explanations, see [calibration-guide.md](calibration-guide.md).

---

## Downloaded Calibration Models

Run `python utilities/download_calibration.py` to download these:

| Model | Height | Use For |
|-------|--------|---------|
| `first_layer_patch_0.2mm.stl` | 0.2mm | First layer / bed level check |
| `extrusion_multiplier_cube.stl` | ~25mm | Flow rate calibration |
| `voron_design_cube.stl` | 20mm | Dimensional accuracy (X/Y/Z) |
| `square_tower.stl` | **~80mm** | **Pressure Advance**, Temperature (TUNING_TOWER) |
| `ringing_tower.stl` | **~80mm** | **Input Shaper** (visual inspection) |
| `3DBenchy.stl` | ~48mm | Final validation torture test |

**Key:** TUNING_TOWER requires a **tall** object. Use `square_tower.stl` or `ringing_tower.stl`, NOT the 20mm Voron cube.

---

## Calibration Order

1. Mechanical check (manual)
2. PID tune hotend & bed
3. Z-offset & bed mesh
4. First layer test
5. Extruder steps (e-steps)
6. Pressure Advance
7. Input Shaper
8. Flow rate / Extrusion Multiplier
9. Temperature (optional)
10. Retraction (optional)

---

## 1. PID Tuning

Stabilizes temperature control. Run once per hotend/bed change.

```gcode
# Hotend (at typical print temp)
PID_CALIBRATE HEATER=extruder TARGET=210

# Bed
PID_CALIBRATE HEATER=heater_bed TARGET=60

# Save results
SAVE_CONFIG
```

---

## 2. Z-Offset & Bed Mesh

```gcode
G28                      # Home all
PROBE_CALIBRATE          # Interactive Z-offset (paper test)
# Adjust with TESTZ Z=-0.1 or TESTZ Z=+0.1
ACCEPT                   # When paper drags slightly
SAVE_CONFIG

# Then create bed mesh
G28
BED_MESH_CALIBRATE
SAVE_CONFIG
```

**Live Z adjust during print:**
```gcode
SET_GCODE_OFFSET Z_ADJUST=-0.02 MOVE=1   # Lower (more squish)
SET_GCODE_OFFSET Z_ADJUST=+0.02 MOVE=1   # Higher (less squish)
```

---

## 3. First Layer Test

Print the Ellis first layer patch (`first_layer_patch_0.2mm.stl`).

| Symptom | Fix |
|---------|-----|
| Lines don't touch | Lower Z-offset |
| Rough/transparent | Lower Z-offset |
| Ridges between lines | Raise Z-offset |
| Varies across bed | Re-run BED_MESH_CALIBRATE |

---

## 4. Extruder Steps (E-steps)

Ensures extruder pushes exactly 100mm when asked.

```gcode
# Heat hotend
M104 S210

# Mark filament 120mm from extruder entrance
# Extrude 100mm slowly
G91                      # Relative mode
G1 E100 F100             # Extrude 100mm at 100mm/min
G90                      # Back to absolute

# Measure remaining distance to mark
# If 20mm remains = perfect. If 18mm remains = over-extruding.
```

**Calculate new e-steps:**
```
new_e_steps = current_e_steps × (100 / actually_extruded)
```

Update `rotation_distance` in printer.cfg (inverse relationship).

---

## 5. Pressure Advance

Compensates for filament pressure lag. Eliminates bulging corners.

**Print:** `square_tower.stl` (~80mm tall)

```gcode
# Set conservative speed limits
SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500

# Start tuning tower - parameter changes with Z height
TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005
```

Examine the tower walls. Find the height where corners look best (no bulging, no gaps).

```
PA = START + (height_in_mm × FACTOR)
PA = 0 + (10mm × 0.005) = 0.05
```

**Typical values:**
| Filament | PA Range |
|----------|----------|
| PLA | 0.02 - 0.08 |
| PETG | 0.05 - 0.10 |
| TPU | 0.10 - 0.20 |

Add to printer.cfg:
```ini
[extruder]
pressure_advance: 0.05
```

---

## 6. Input Shaper

Eliminates ringing/ghosting. Klipper's superpower.

**Option A: With accelerometer (recommended)**
```gcode
SHAPER_CALIBRATE
SAVE_CONFIG
```

**Option B: Manual with ringing tower**
```gcode
# Print ringing_tower.stl at 80-100mm/s
# Examine for ringing patterns
# Try different shapers:
SET_INPUT_SHAPER SHAPER_FREQ_X=40 SHAPER_FREQ_Y=40 SHAPER_TYPE=mzv
```

Add to printer.cfg:
```ini
[input_shaper]
shaper_freq_x: 40
shaper_freq_y: 40
shaper_type: mzv
```

---

## 7. Flow Rate / Extrusion Multiplier

Print Ellis extrusion_multiplier_cube.stl (single wall, 0 infill, 0 top layers).

Measure wall thickness with calipers. Should equal line width (typically 0.4mm).

```
new_flow = (expected_width / measured_width) × current_flow
new_flow = (0.4 / 0.44) × 100% = 91%
```

Adjust in slicer, not Klipper.

---

## 8. Temperature Tuning (Optional)

**Print:** `square_tower.stl` (~80mm tall)

```gcode
# Temperature varies with Z height
# START=190, FACTOR=2 means: 190°C at Z=0, 200°C at Z=5mm, 210°C at Z=10mm...
TUNING_TOWER COMMAND=SET_HEATER_TEMPERATURE HEATER=extruder PARAMETER=TARGET START=190 FACTOR=2
```

Examine each 5-10mm section of the tower:
- **Too cold:** Poor layer adhesion, rough surface, weak
- **Too hot:** Stringing, blobbing, discoloration

Mark the height of the best-looking section, calculate temp: `temp = 190 + (height × 2)`

---

## 9. Retraction Tuning (Optional)

For direct drive (like Pitan), start with:
- Distance: 0.5-1.0mm
- Speed: 30-45mm/s

Test with stringing torture test or travel-heavy print.

**PETG:** Less retraction than PLA (more viscous)
**TPU:** Minimal or zero retraction

---

## Validation Prints

After calibration, print these to verify:

| Print | File | What to Check |
|-------|------|---------------|
| Voron Cube | `voron_design_cube.stl` | Measure 20.0mm on X, Y, Z axes |
| 3DBenchy | `3DBenchy.stl` | Overhangs, bridging, detail, stringing |
| Maker Coin | `./build.sh build maker_coin` | Logo clarity, layer adhesion |
| Fidget Bolt | `./build.sh build fidget_bolt` | **Threads work = well calibrated!** |

---

## Quick Troubleshooting

| Problem | Likely Cause | Fix |
|---------|--------------|-----|
| First layer doesn't stick | Z too high | Lower Z-offset |
| Elephant foot | Z too low | Raise Z-offset |
| Ringing/ghosting | No Input Shaper | Run SHAPER_CALIBRATE |
| Bulging corners | No Pressure Advance | Calibrate PA |
| Stringing | Retraction/temp | Tune retraction, lower temp |
| Layer shifts | Loose belts, too fast | Tighten belts, reduce accel |
| Inconsistent extrusion | Flow rate wrong | Calibrate e-steps and flow |

---

## External Resources

- **Ellis Print Tuning Guide:** [ellis3dp.com/Print-Tuning-Guide](https://ellis3dp.com/Print-Tuning-Guide/) - Detailed methodology, works for any Klipper printer
- **Teaching Tech Calibration:** [teachingtechyt.github.io/calibration](https://teachingtechyt.github.io/calibration.html) - Interactive gcode generators
- **Klipper Documentation:** [klipper3d.org](https://www.klipper3d.org/Config_Reference.html) - Official reference

---

## Download Calibration Prints

```bash
cd cad
python utilities/download_calibration.py
```

Downloads from Klipper, Voron, and Ellis GitHub repos. See [calibration-guide.md](calibration-guide.md) for print settings.

---

*"Measure twice, print once. Or just print it and iterate."*
