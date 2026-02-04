# Utilities

Helper scripts that aren't printer parts.

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `download_calibration.py` | Download community calibration prints | `python utilities/download_calibration.py` |
| `export_logo.py` | Generate Amalgam logo as SVG | `python utilities/export_logo.py` |
| `list.py` | List all available parts | `./build.sh list` |

## download_calibration.py

Downloads standard calibration STLs from GitHub repositories:
- Klipper ringing tower, square tower
- Voron Design Cube
- Ellis first layer patch, EM cube
- 3DBenchy

Downloads to `../calibration/` (gitignored).

## export_logo.py

Generates the Amalgam logo in multiple SVG variants:
- `amalgam_a.svg` - Stylized A only
- `amalgam_logo_flat.svg` - Simple octagon + A (good for B&W)
- `amalgam_logo_bw.svg` - Black octagon, white recess, black A
- `amalgam_logo_outline.svg` - Full logo with outline effect

Outputs to `../exports/logo/`.

## list.py

Used internally by `build.sh` to discover available parts. You can also run it directly:

```bash
python utilities/list.py              # Human-readable list
python utilities/list.py --build-format  # Machine-readable for build.sh
```
