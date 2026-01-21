# Phase 2: Clean Design Workflow (No venv required)

## User Clarification

**User only uses VSCode as STL viewer, not for running code.**

So:
- VSCode import errors are ANNOYING but NOT blocking
- Just need part files to generate clean STL exports
- No need for venv or complex setup

---

## Simplified Design Workflow

### For Each Part:

1. **Write part code** in `cad/parts/`
   - Import from config.py
   - Use build123d directly
   - Write clean, self-contained code

2. **Generate STL**
   ```bash
   python cad/parts/your_part.py
   ```
   - STL automatically exports to `cad/stl/`

3. **View in VSCode** (build123d extension)
   - Open `cad/stl/your_part.stl`
   - Check dimensions
   - Verify geometry
   - Adjust if needed

4. **Iterate**
   - Edit part code
   - Regenerate STL
   - Verify again

---

## Current Status

✅ **Corner 1 (Front-Left + Z1)**: Designed
- File: `cad/parts/corner_1_front_left_z1.py`
- Ready to generate STL

---

## VSCode Notes

### Import Errors Are Expected
- VSCode tries to lint old code (`main.py`, `components/*.py`)
- These imports will fail (files/modules don't exist)
- **Ignore these errors** - they don't affect new part generation
- Only `cad/parts/` has clean, working code

### What Matters
- Can you open the STL file in VSCode?
- Can you verify dimensions look correct?
- Did the STL export successfully?

### Disable VSCode Linting for Old Files (Optional)

**Create `.vscode/settings.json`:**
```json
{
  "python.linting.ignorePatterns": [
    "cad/main.py",
    "cad/components/*.py",
    "cad/project_vars.py",
    "cad/parts/corners.py",
    "cad/parts/z_pucks.py",
    "cad/parts/carriage.py",
    "cad/parts/electronics.py"
  ]
}
```

**Result:** VSCode won't try to lint old code, focus only on new parts/

---

## Quick Start

### Generate Corner 1 STL:

```bash
cd /Users/michael/Projects/Personal/neo-darwin
python cad/parts/corner_1_front_left_z1.py
```

### Check in VSCode:
1. Open `cad/stl/corner_1_front_left_z1.stl`
2. Use build123d extension viewer
3. Verify dimensions:
   - M12 rod diameter: 12.5mm
   - Motor mount: 42×42mm NEMA17
   - Rod clamps: 4 positions
4. Adjust code if needed

### Continue Workflow:
- ✅ Corner 1 designed
- [ ] Corner 2 (Front-Right + Z2)
- [ ] Corner 3 (Back-Left)
- [ ] Corner 4 (Back-Right)
- [ ] Z-puck (Back-Center)
- [ ] Spider bed support
- [ ] Top corners (TL, TR, BL, BR)
- [ ] X-carriage
- [ ] Y-gantry
- [ ] Wade extruder
- [ ] Electronics

---

## config.py Status

Current `cad/config.py` is basic (46 lines).

For Phase 2, you can:
1. Keep using basic config.py (it works!)
2. Add parameters in individual part files as needed
3. OR expand config.py gradually with new parameters

**Recommendation:** Keep config.py simple, add what you need directly in part files.
