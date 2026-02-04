# ADR-009: Modular Puck System

## Status
Accepted

## Context
The Amalgam requires mounting points for:
- Z-motors and leadscrew nuts
- Main electronics/brain board
- Extruder/toolhead on X-carriage
- Future toolheads (plotter, laser, etc.)
- Modular upgrades without redesign

In 2026, mounting solutions are:
- Integrated parts (printed directly into structure)
- Bolt-on brackets (custom for each part)
- Modular pucks (standardized mounting interface)

The Amalgam's "forever machine" philosophy and multipurpose gantry require a standardized mounting system that allows:
- Future upgrades without redesign
- Easy repair and replacement
- Tool swapping for multipurpose use
- Bootstrapping (print on small printer, use on large)

## Decision
We choose the **Modular Puck System** - standardized mounting interfaces for all major components.

### Why Puck System?
1. **Standardized interface**: All components mount via pucks
2. **Future-proof**: Upgrade without redesigning entire structure
3. **Easy repair**: Broken puck = reprint single part
4. **Multipurpose**: Same frame can hold different toolheads
5. **Modular**: Pucks interchangeable between tiers
6. **Parametric**: build123d generates puck variants from config.py
7. **Bootstrappable**: Small parts, printable on donor printers

### Puck Types
1. **Z-Puck**: Mounts Z-motor and leadscrew nut to M12 frame
2. **Brain Puck**: Mounts electronics board to M12 frame
3. **Extruder Puck**: Mounts toolhead to X-carriage (modular toolheads)
4. **Motion Puck**: Mounts linear rails (for tinker path)
5. **Tool Pucks**: Plotter pen, laser, CNC spindle (future expansion)

### Puck Philosophy
> "The chassis is eternal, the tools are transient."

## Consequences

### Benefits
- **Modular upgrades**: Swap toolheads without redesigning carriage
- **Repairable**: Replace individual pucks, not whole assemblies
- **Multipurpose**: Same frame for 3D printing, plotting, laser
- **Parametric**: One codebase generates all pucks from config
- **Small prints**: All pucks fit within 150mm³ (bootstrappable)
- **Scalable**: Puck sizes adapt to motor/bearings/hotend dimensions

### Trade-offs
- **More parts**: More assemblies = more bolt points
- **Interface complexity**: Must maintain consistent puck interfaces
- **Stacking tolerance**: Multiple pucks = cumulative tolerance issues
- **Weight**: Additional mounting hardware adds mass

### Why NOT Integrated?
1. **No upgrades**: Changing toolhead requires redesigning carriage
2. **No repair**: Broken part = reprint entire assembly
3. **No multipurpose**: Can't swap to plotter/laser
4. **Large prints**: Integrated carriage may exceed donor build volume

## BOM Implications (Generic)

### Scenario A: Standard Tier 3 Build (Recommended)
- **Parts needed**:
  - 3x Z-Pucks (printed, hold motors + nuts)
  - 1x Brain Puck (printed, holds MKS SKIPR)
  - 1x Extruder Puck (printed, holds Wade + hotend)
  - 3x X-carriage linear bearing clamps (printed)
  - 20-30x M5 or M6 bolts (puck-to-frame and puck-to-component)
  - 40-60x washers and nuts
- **Cost implication**: Very Low (~$5-10 AUD for hardware)
- **Donor compatibility**: All donors (3D-printed)
- **Print time**: ~10-15 hours total
- **Components**: All modular, replaceable

### Scenario B: Salvage-Specific Pucks
- **Parts A: Donor motors are different size** (oversized NEMA17, etc.)
  - Parts needed: Parametric pucks from config.py
  - Adjust config: MOTOR_SIZE, MOUNT_HOLE_PATTERN
  - Regenerate: build123d creates custom pucks
  - Cost implication: Very Low (~$5-10 AUD)
  - Donor compatibility: All donors
  - Note: build123d handles dimension changes

- **Parts B: Donor board is different shape**
  - Parts needed: Custom Brain Puck from config.py
  - Adjust config: BOARD_MOUNT_HOLES, BOARD_DIMENSIONS
  - Cost implication: Very Low (~$5-10 AUD)
  - Donor compatibility: All donors
  - Note: Standard board patterns available (Creality, Anet, Prusa)

### Scenario C: Toolhead Upgrades
- **Parts A: Wade → StealthBurner (Voron)**
  - Parts needed: New Extruder Puck (StealthBurner compatible)
  - Salvage: Existing Wade, pucks, mounts
  - Cost implication: Low (~$10-15 AUD for new puck + hardware)
  - Donor compatibility: N/A (new purchase)
  - Note: Just swap puck + toolhead, no redesign

- **Parts B: 3D Print → Pen Plotter**
  - Parts needed: Pen Plotter Tool Puck
  - Salvage: Everything except toolhead puck
  - Cost implication: Very Low (~$3-5 AUD)
  - Note: 30-second swap via puck interface

### Scenario D: High-End Upgrades (Tier 4)
- **Parts needed**:
  - 3x Enhanced Z-Pucks (with vibration damping)
  - 1x CAN Toolhead Puck (for EBB36)
  - 1x Motion Pucks (MGN12 rail mounts)
- **Cost implication**: Low (~$8-12 AUD for hardware)
- **Donor compatibility**: All donors
- **Note**: Same frame, upgraded pucks

### Scenario E: Emergency/Improvised Pucks
- **Parts needed**:
  - Print pucks with custom dimensions for non-standard parts
  - May need to drill mounting holes by hand
  - Use generic bolt patterns
- **Cost implication**: Very Low
- **Warning**: Not supported by build123d scripts, manual dimensioning required

## Implementation Notes

### Puck Design Philosophy
```
All pucks follow standard pattern:
1. Frame Interface: Mounts to M12 rods or X-carriage
2. Component Interface: Standardized bolt pattern (per component type)
3. Interlock: Tab/slot or chamfered edges for alignment
4. Serviceability: Easy bolt access, removable without disassembly
```

### Z-Puck (Motor Mount)
```
Function: Mounts Z-motor and leadscrew nut to M12 vertical rod

Design:
- Motor mount: 4x M3 bolt holes (NEMA17 standard)
- Nut trap: Captures leadscrew nut (M8 or TR8)
- Frame clamp: Slides over M12 rod
- Jam nuts: 2 per rod to lock puck in place
- Adjustable: Can slide up/down for initial positioning

Configuration:
Z_PUCK_HEIGHT = 60.0  # From config.py
MOTOR_OFFSET = [X, Y, Z]  # Relative to rod center
```

### Brain Puck (Electronics Mount)
```
Function: Mounts main board to M12 frame

Design:
- Board mount: Matches board mounting pattern (varies by board)
- Cable routing: Cutouts for wire looms
- Fan mounting: Optional cooling fan for board
- Frame clamp: Slides over M12 rod
- Adjustable: Height and rotation

Standard Boards (Pre-defined Patterns):
- MKS SKIPR: 100mm × 100mm pattern
- BTT SKR 3: 95mm × 100mm pattern
- Creality 4.2.2: 110mm × 70mm pattern
- Anet V1.0: 115mm × 75mm pattern

Configuration:
BOARD_TYPE = "MKS_SKIPR"  # From config.py
BOARD_MOUNT_PINS = [[x1, y1], [x2, y2], ...]  # Auto-generated
```

### Extruder Puck (Toolhead Mount)
```
Function: Mounts extruder/hotend to X-carriage

Design:
- Extruder mount: 4x M4 bolt holes (Greg's Wade pattern)
- Hotend mount: GrooveMount pattern (16mm diameter)
- Z-probe mount: BLTouch/PINDA mounting tabs
- Carriage interface: Bolts to X-carriage bearing clamps
- Modular: Swap entire puck for different toolheads

Toolhead Variants:
- WADE_PUCK:      Standard Greg's Wade
- STEALTHBURNER:  Voron StealthBurner
- SHERPA:         Sherpa Mini
- ORBITER:         Orbiter 1.5
- PLOTTER:         Pen holder
- LASER:           Laser module

Configuration:
EXTRUDER_TYPE = "WADE"  # From config.py
TOOLHEAD_PUCK_TYPE = "WADE_PUCK"
Z_PROBE_OFFSET = [X, Y, Z]  # Auto-adjusts in config
```

### Motion Puck (Linear Rail - Tinker)
```
Function: Mounts MGN12 rail to M12 frame (optional upgrade)

Design:
- Rail mount: MGN12 bolt pattern (M3 screws)
- Frame clamp: Slides over M12 rod
- Adjustable: Precise alignment set screws
- Shim slots: For rail parallelism adjustment

Configuration:
MOTION_SYSTEM = "RAILS"  # vs "RODS" from config.py
RAIL_TYPE = "MGN12H"
```

### Tool Pucks (Multipurpose)
```
Function: Convert 3D printer to other uses

Variants:
- PLOTTER_PUCK: Pen holder + Z-lift mechanism
- LASER_PUCK:  Laser module mount + safety interlock
- CNC_PUCK:    Spindle mount + dust shoe
- CAMERA_PUCK:  Time-lapse camera mount

Benefits:
- 30-second swap: One puck interface
- Software profiles: Klipper configs per tool
- No redesign: Frame stays same
```

### build123d Puck Generation
```python
# config.py drives all puck generation
from config import *

# Z-Puck generation
z_puck = create_z_puck(
    rod_dia=M12_FIT_DIA,
    motor_size=MOTOR_SIZE,
    nut_type=leadscrew_nut
)

# Brain Puck generation
brain_puck = create_brain_puck(
    rod_dia=M12_FIT_DIA,
    board_type=BOARD_TYPE
)

# Extruder Puck generation
extruder_puck = create_extruder_puck(
    extruder_type=EXTRUDER_TYPE,
    hotend_type=HOTEND_TYPE
)
```

### Puck Mounting Pattern
```
Standard Bolt Sizes (from config.py):
Z-Puck:           M5 bolts (strength for motor weight)
Brain Puck:       M5 bolts (board weight)
Extruder Puck:     M4 bolts (precision, lighter)
Motion Puck:       M3 bolts (rail standard)

Standard Spacing:
M12 rod clamp:    40mm bolt spacing
Bearing clamp:     60mm spacing (dual-bearing carriage)
Board patterns:    Per-board (defined in config.py)
```

### Maintenance
- **Check tightness**: Every 100 hours
- **Inspect for cracks**: Annual visual inspection
- **Re-tighten after moves**: If printer relocated
- **Swap pucks**: If upgrading components

### Common Issues
- **Puck slips on rod**: Increase clamp pressure, check M12 diameter (lumpy factor)
- **Bolt holes misaligned**: Verify config.py dimensions, regenerate pucks
- **Puck too loose**: Add shims or adjust clamp design
- **Cracked puck**: Check print quality (infill, perimeters)

## References
- [../manifesto.md](../manifesto.md): Section "The Modular 'Puck' & 'Spider' Concept"
- [Parametric Design Pattern](https://github.com/guykabu/build123d)
- docs/AI-Conversations/ [Relevant conversations about modular mounting]
