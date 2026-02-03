# Amalgam Calibration Guide

This guide walks you through calibrating your Amalgam printer from first power-on to validated prints. The process is designed around Klipper's capabilities and the Amalgam hardware.

**Philosophy:** Get it working, then optimize. Don't chase perfection on step 1 before confirming step 2 works.

---

## Calibration Order

Follow this sequence. Each phase builds on the previous one.

| Phase | Goal | Time |
|-------|------|------|
| 1. Mechanical Setup | Frame square, belts tight, Z aligned | First build |
| 2. First Layers | Consistent adhesion across the bed | 30-60 min |
| 3. Dimensional Accuracy | Parts come out the right size | 30 min |
| 4. Klipper Tuning | Input Shaper + Pressure Advance | 1-2 hours |
| 5. Filament Profiles | Temp, retraction, flow per material | Per filament |
| 6. Validation | Benchy + victory print | Fun |

---

## Phase 1: Mechanical Setup

Before any calibration prints, ensure the machine is mechanically sound.

### Frame Squaring

**Scaffold path (M10 threaded rod):**
- Use the MDF base as your reference — it's the squaring jig
- Check 90° at each corner with a machinist square
- Tighten jam nuts only after square is confirmed

**Mill/Lathe path (aluminum extrusion):**
- Extrusions should be perpendicular to MDF base
- Check diagonal measurements — should be equal
- Tighten all frame bolts after confirming square

### Belt Tension

Belts should be firm but not guitar-string tight.

- **Too loose:** Layer shifts, ghosting, dimensional inaccuracy
- **Too tight:** Motor strain, premature bearing wear, noise

Test: Press belt at midpoint. Should deflect 2-3mm with moderate finger pressure.

### Z-Axis: Triple-Z Leveling

Run Klipper's `Z_TILT_ADJUST` to level the bed using the three Z motors.

```gcode
G28                  ; Home all axes
Z_TILT_ADJUST        ; Auto-level using Triple-Z
```

Run 2-3 times until adjustments are minimal (< 0.01mm).

### Verify Motion

Before printing, verify all axes move correctly:

```gcode
G28                  ; Home
G1 X110 Y110 Z50 F3000  ; Move to center
G1 X10 F3000         ; Move X
G1 X210 F3000
G1 Y10 F3000         ; Move Y
G1 Y210 F3000
G1 Z10 F1000         ; Move Z
G1 Z100 F1000
```

Watch for:
- Smooth motion (no grinding, skipping)
- Correct direction (X+ moves right, Y+ moves back, Z+ moves up)
- No binding at travel limits

---

## Phase 2: First Layers

The first layer is the foundation of every print. Get this right before anything else.

### Bed Mesh Calibration

Create a mesh map of bed surface variations:

```gcode
G28                     ; Home
BED_MESH_CALIBRATE      ; Probe the bed
SAVE_CONFIG             ; Save mesh to printer.cfg
```

Re-run after any bed surface change (new G10 sheet, re-leveling, etc.).

### Z-Offset Calibration

The Z-offset determines first layer squish. Too high = no adhesion. Too low = elephant foot.

**Using paper method:**
```gcode
G28
PROBE_CALIBRATE        ; Start interactive calibration
```

Adjust until paper drags slightly under the nozzle. Save with `SAVE_CONFIG`.

**Using baby-stepping during print:**
Start a first layer test and adjust Z live:
```gcode
SET_GCODE_OFFSET Z_ADJUST=0.01 MOVE=1   ; Raise nozzle slightly
SET_GCODE_OFFSET Z_ADJUST=-0.01 MOVE=1  ; Lower nozzle slightly
```

### First Layer Test Print

Print the **first layer grid** — a 5×5 grid of small squares across the bed.

**What to look for:**

| Symptom | Cause | Fix |
|---------|-------|-----|
| Lines not touching | Z too high | Lower Z-offset |
| Transparent/rough surface | Z too high | Lower Z-offset |
| Ridges between lines | Z too low | Raise Z-offset |
| Corners lifting | Poor adhesion | Clean bed, adjust temp, check level |
| Varies across bed | Bed not flat | Re-run BED_MESH_CALIBRATE |

**Good first layer:**
- Lines slightly overlap
- Smooth top surface
- Consistent across entire bed
- Adheres without lifting

---

## Phase 3: Dimensional Accuracy

Once first layers are good, verify dimensional accuracy.

### Calibration Cube

Print a **20mm calibration cube** (or threaded bolt cube).

**Measure with calipers:**
- X dimension (should be 20.00mm)
- Y dimension (should be 20.00mm)
- Z dimension (should be 20.00mm)

**If dimensions are off:**

| Issue | Likely Cause | Fix |
|-------|--------------|-----|
| All dimensions small | Under-extrusion | Increase flow rate / check extruder |
| All dimensions large | Over-extrusion | Decrease flow rate |
| X or Y off, Z correct | Steps/mm wrong | Calibrate steps/mm in Klipper |
| First layer elephant foot | Z too low | Raise Z-offset slightly |

### Flow Rate Calibration

Print a single-wall cube (1 perimeter, 0 infill, 0 top layers).

Measure wall thickness with calipers. Should match your line width (typically 0.4mm for 0.4mm nozzle).

**Adjust flow rate:**
```
New flow % = (Expected width / Measured width) × Current flow %
```

Example: If expecting 0.4mm but measuring 0.44mm with flow at 100%:
```
New flow = (0.4 / 0.44) × 100 = 91%
```

### Threaded Bolt Cube (Optional)

If using the threaded bolt cube, also test:
- Thread engagement with a real nut (M6 or M8)
- If nut doesn't thread on: check for over-extrusion or Z calibration

---

## Phase 4: Klipper Tuning

These Klipper-specific calibrations significantly improve print quality.

### Input Shaper (Resonance Compensation)

Input Shaper eliminates ringing/ghosting artifacts. This is one of Klipper's superpowers.

**Option A: Manual with ringing tower**

1. Print the ringing tower at moderate speed (80-100mm/s)
2. Examine walls for ringing patterns
3. Configure shaper in printer.cfg:
   ```ini
   [input_shaper]
   shaper_freq_x: 40  ; Adjust based on test
   shaper_freq_y: 40
   shaper_type: mzv
   ```

**Option B: Automatic with ADXL345 accelerometer (recommended)**

If you have an ADXL345 accelerometer connected:

```gcode
SHAPER_CALIBRATE      ; Automatic calibration
```

Klipper will measure resonances and suggest optimal settings.

**Verify:** Print ringing tower again. Ghosting should be eliminated or greatly reduced.

### Pressure Advance

Pressure Advance compensates for filament pressure in the hotend, eliminating corner bulging and improving line consistency.

**Calibration process:**

1. Use Klipper's tuning tower:
   ```gcode
   SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500
   TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005
   ```

2. Print the PA test pattern (square tower)

3. Measure height where corners look best

4. Calculate PA value:
   ```
   PA = START + (measured_height × FACTOR)
   ```

5. Set in printer.cfg:
   ```ini
   [extruder]
   pressure_advance: 0.05  ; Your calculated value
   ```

**Typical values:**
| Filament | PA Range |
|----------|----------|
| PLA | 0.02 - 0.08 |
| PETG | 0.05 - 0.10 |
| TPU | 0.10 - 0.20 |

---

## Phase 5: Filament Profiles

Each filament type (and brand) needs its own profile.

### Temperature Tower

A temperature tower prints sections at different temperatures to find the optimal printing temp.

**Method:** Use Klipper's `SET_HEATER_TEMPERATURE` with layer-based changes, or use your slicer's temperature tower feature.

**What to look for:**
| Temp too low | Temp too high |
|--------------|---------------|
| Poor layer adhesion | Stringing/oozing |
| Weak parts | Blobbing |
| Rough surface | Discoloration |

**Typical ranges:**
| Filament | Range | Start Point |
|----------|-------|-------------|
| PLA | 190-220°C | 205°C |
| PETG | 230-250°C | 240°C |
| TPU | 220-240°C | 230°C |

### Retraction Tuning

Retraction prevents stringing during travel moves.

**Print a retraction tower** (multiple columns with travels between them).

**Adjust:**
- Retraction distance: Start at 0.5mm (direct drive) or 4mm (Bowden)
- Retraction speed: 25-45mm/s typical

**PETG note:** PETG is stringy. Use lower retraction than PLA (it's more viscous) and enable "wipe" in your slicer.

**TPU note:** Minimal or zero retraction for flexible filaments — they compress and jam.

### Per-Filament Settings

Create profiles in your slicer for each filament:

| Setting | PLA | PETG | TPU |
|---------|-----|------|-----|
| Hotend temp | 200-210°C | 235-245°C | 225-235°C |
| Bed temp | 55-60°C | 75-85°C | 50-60°C |
| Cooling fan | 100% | 50-70% | 50-100% |
| Retraction | 0.5-1.0mm | 0.3-0.8mm | 0-0.5mm |
| Print speed | 70-120mm/s | 50-80mm/s | 20-40mm/s |
| Pressure Advance | 0.02-0.08 | 0.05-0.10 | 0.10-0.20 |

---

## Phase 6: Validation Prints

### Benchy

The 3D Benchy is the standard "torture test." Print one to validate your calibration.

**What to check:**
- Hull: Smooth, no layer lines visible
- Bow overhang: Clean without drooping
- Cabin roof: Flat bridging
- Chimney: No stringing, round hole
- Text: Readable on stern
- Dimensions: Hull should be ~60mm long

**Download:** [3DBenchy.com](https://www.3dbenchy.com/)

### Victory Prints

Once Benchy passes, print your Amalgam victory prints:

1. **Amalgam Maker Coin** — Octagonal coin with Logo 10
2. **Amalgam Fidget Bolt** — Working threaded nut and bolt

These are your "I built an Amalgam" badges. If the threads work smoothly, your printer is well-calibrated.

---

## Calibration Prints Reference

| Print | File | Purpose |
|-------|------|---------|
| First Layer Grid | `cad/parts/first_layer_grid.py` | Bed level verification |
| Calibration Cube | Standard 20mm XYZ cube | Dimensional accuracy |
| Threaded Bolt Cube | `cad/parts/calibration_bolt_cube.py` | Dimensions + threads |
| Ringing Tower | Input Shaper test | Resonance tuning |
| Benchy | External (3DBenchy.com) | Comprehensive validation |
| Maker Coin | `cad/parts/amalgam_maker_coin.py` | Victory print |
| Fidget Bolt | `cad/parts/amalgam_fidget_bolt.py` | Victory print |

---

## Troubleshooting Quick Reference

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| First layer doesn't stick | Z too high, dirty bed | Lower Z-offset, clean with IPA |
| Elephant foot | Z too low, bed too hot | Raise Z-offset, lower bed temp |
| Layer shifts | Loose belts, too fast | Tighten belts, reduce speed/accel |
| Ghosting/ringing | No Input Shaper | Run SHAPER_CALIBRATE |
| Blobby corners | No Pressure Advance | Calibrate PA |
| Stringing | Retraction, temp | Tune retraction, lower temp |
| Under-extrusion | Flow rate, clog | Calibrate flow, check nozzle |
| Over-extrusion | Flow rate too high | Reduce flow rate |
| Warping | Bed adhesion, drafts | Brim, enclosure, bed temp |
| Z banding | Lead screw issues | Check coupling, lubricate |

---

## Maintenance Schedule

| Interval | Task |
|----------|------|
| **Every print** | Check first layer, remove debris |
| **Weekly** | Clean bed with IPA, check belt tension |
| **Monthly** | Lubricate Z lead screws, check for loose bolts |
| **Quarterly** | Re-run BED_MESH_CALIBRATE, check bearing wear |
| **Annually** | Full mechanical inspection, replace worn parts |

---

## References

- [Klipper Configuration Reference](https://www.klipper3d.org/Config_Reference.html)
- [Klipper Pressure Advance](https://www.klipper3d.org/Pressure_Advance.html)
- [Klipper Input Shaper](https://www.klipper3d.org/Resonance_Compensation.html)
- [Ellis' Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/)
- [3D Benchy](https://www.3dbenchy.com/)
- ADR-028: Target Filament Selection (PLA, PETG, TPU)
- ADR-027: Build Plate Surface Selection

---

*"Calibration is not a destination, it's a journey. But at some point, you should actually print something."*
