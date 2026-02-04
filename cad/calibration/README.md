# Calibration Prints

**This folder is gitignored.** Contents are downloaded, not stored in the repo.

## Download Calibration Prints

```bash
cd cad
python utilities/download_calibration.py
```

This downloads standard calibration STLs from their original GitHub repositories.

## What Gets Downloaded

| File | Purpose | Source |
|------|---------|--------|
| `ringing_tower.stl` | Input Shaper tuning | [Klipper](https://github.com/Klipper3d/klipper) |
| `square_tower.stl` | Pressure Advance, temperature | [Klipper](https://github.com/Klipper3d/klipper) |
| `voron_design_cube.stl` | Dimensional accuracy, overhangs | [VoronDesign](https://github.com/VoronDesign/Voron-2) |
| `xyz_calibration_cube.stl` | Quick dimensional check | [5axes](https://github.com/5axes/Calibration-Shapes) |
| `first_layer_patch_0.2mm.stl` | First layer calibration | [Ellis](https://github.com/AndrewEllis93/Print-Tuning-Guide) |
| `extrusion_multiplier_cube.stl` | Flow rate calibration | [Ellis](https://github.com/AndrewEllis93/Print-Tuning-Guide) |
| `3DBenchy.stl` | Comprehensive validation | [CreativeTools](https://github.com/CreativeTools/3DBenchy) |

## Amalgam-Generated Calibration Prints

These are built from source (not downloaded):

```bash
./build.sh build first_layer_grid   # Grid of squares across bed
./build.sh build prusa_live_z       # Prusa-style live Z pattern
```

See `amalgam/parts/calibration/` for the source code.

## Calibration Guide

See `docs/guides/calibration-cheatsheet.md` for:
- 80/20 quick calibration path
- Klipper TUNING_TOWER commands
- What each print tests

---

*All downloads respect original licenses. See ACKNOWLEDGEMENTS.md for credits.*
