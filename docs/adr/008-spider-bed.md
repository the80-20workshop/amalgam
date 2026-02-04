# ADR-008: Spider Trident Bed Support

## Status
Accepted

## Context
The bed support system must:
1. Support a 250mm²+ heated bed
2. Connect to 3 independent Z-motors/leadscrews (Triple-Z)
3. Be printable on small donor printers (A1 Mini, Ender 3)
4. Provide rigidity to prevent bed sag
5. Maintain parallelism to the gantry

In 2026, there are multiple bed support options:
- Solid plate: One-piece printed (too large for small printers)
- Aluminum frame: Machined plate (expensive)
- Modular spider: Interlocking pieces (printable, rigid)

The Amalgam's bootstrapping philosophy requires using small donor printers to build the larger Amalgam machine.

## Decision
We choose the **Modular Spider Trident Bed Support** - an interlocking three-arm design printed in sections and bolted together.

### Why Spider Trident?
1. **Bootstrapping capability**: Can be printed on 220mm³ donor printers (A1 Mini, Ender 3)
2. **Rigid triangle**: Three arms + hub create stiff structural triangle
3. **Modular assembly**: Print 4 parts (hub + 3 arms), bolt together
4. **Interlocking design**: Arm-to-arm and arm-to-hub connections for rigidity
5. **Kinematic support**: Three-point support matches Triple-Z system
6. **Scalable**: Can be scaled for 300mm³ builds with longer arms
7. **Printable**: No large parts, all fit within 220mm build volume

### Design Concept
```
       [Arm 2]
          |
          v
    [Arm 1]--[Hub]--[Arm 3]

- Hub: Central triangular piece
- Arms: Three interlocking sections
- Bed Mounting: Bolts to arm outer edges
- Leadscrew Mounts: Three positions at arm endpoints
```

## Consequences

### Benefits
- **Small printer compatible**: All parts fit 220mm³ build area
- **Rigid structure**: Interlocking design prevents flex
- **Replaceable**: Broken arm can be reprinted individually
- **Scalable**: Longer arms = larger bed volume
- **Lightweight**: Mostly hollow, print-efficient
- **Kinematic alignment**: Matches Triple-Z motor layout

### Trade-offs
- **Assembly required**: Must bolt 4 parts together (10-15 min)
- **Alignment critical**: Must ensure arm-to-hub is perpendicular during assembly
- **Bolt pattern**: Requires precise bolt hole alignment
- **Print time**: Multiple parts = longer total print time

### Why NOT Solid Plate?
1. **Too large**: 250mm+ plate won't fit on most donor printers
2. **Difficult to print**: Large flat plates warp easily
3. **Transport**: Hard to ship or store if fully assembled

### Why NOT Aluminum Frame?
1. **Cost**: Machined aluminum ~$50-80 AUD
2. **Machining required**: Can't 3D print, must buy or CNC
3. **No bootstrapping**: Defeats purpose of building from donor printer

## BOM Implications (Generic)

### Scenario A: Standard 250mm³ Build (Recommended)
- **Parts needed**:
  - 1x Central Hub (printed)
  - 3x Spider Arms (printed)
  - 12x M5 or M6 bolts (arm-to-hub connection)
  - 3x M5 or M6 bolts (bed-to-arm connection)
  - 3x M5 or M6 bolts (leadscrew nut-to-arm connection)
  - 24x washers and nuts
  - Optional: 3x corner brackets for reinforcement
- **Cost implication**: Very Low (~$5-10 AUD for hardware)
- **Donor compatibility**: All donors (3D-printed)
- **Print time**: ~8-12 hours total (hub ~4hrs, arms ~2-3hrs each)
- **Assembly**: Bolt 4 parts together

### Scenario B: Salvaged Bed from Donor
- **Parts A: Donor bed fits 3-point layout** (Prusa MK3, Voron)
  - Parts needed: Print Spider + reuse donor bed
  - Cost implication: Very Low (~$5-10 AUD)
  - Donor compatibility: Prusa MK3, Voron, etc.
  - Note: May need to adapt arm mounting points to donor bed

- **Parts B: Donor bed is rectangular** (Ender 3, CR-10)
  - Parts needed: Print Spider + new bed aluminum plate
  - Cost implication: Low (~$25-35 AUD for bed)
  - Donor compatibility: All donors
  - Note: Most donor beds too small, need new bed

### Scenario C: Upscaled 300mm³ Build
- **Parts needed**:
  - 1x Central Hub (printed)
  - 3x Extended Spider Arms (printed - 50mm longer)
  - 24x longer bolts (for larger triangle)
  - 300mm² aluminum bed plate
- **Cost implication**: Medium (~$35-45 AUD for bed + hardware)
- **Donor compatibility**: All donors
- **Build volume**: 300mm³
- **Note**: Arms still fit in 220mm³ printer (just longer)

### Scenario D: Aluminum Bed Plate (Reference Spec)
- **Parts needed**:
  - Printed Spider assembly (as Scenario A)
  - 250mm × 250mm × 3mm aluminum bed plate
  - MK52 magnetic PEI sheet (optional, ~$25 AUD)
  - Bed heater (220V 240W or 24V 300W)
  - Bed thermistor (NTC 100K)
  - 4x M4 or M5 bed clamps (bed-to-spider)
- **Cost implication**: Medium (~$45-65 AUD)
- **Donor compatibility**: Salvage heater/thermistor if possible
- **Note**: **MKS SKIPR reference spec recommends MK52 magnetic PEI**

### Scenario E: Budget Build (Tier 1)
- **Parts needed**:
  - Printed Spider assembly
  - Salvaged bed from donor
  - Salvaged bed heater
  - Salvaged thermistor (may need repotting)
- **Cost implication**: Very Low (~$0-10 AUD)
- **Donor compatibility**: Ender 3, Prusa i3, Anet A8
- **Note**: May be smaller bed (220mm vs 250mm)

## Implementation Notes

### Hub Design
```
Shape: Equilateral triangle
Size: ~120mm sides
Mounting: 3 bolt holes per arm (9 total)
Center: Cutout for cable routing
```

### Arm Design
```
Shape: Elongated triangle (trapezoid)
Length: 150mm from center to bed edge
Width: 80mm at bed end, 50mm at hub end
Interlock: Tab-and-slot design (arm-to-arm)
Connection: 3 bolts to hub
Bed mount: 2 bolts per arm (6 total)
```

### Assembly Process
1. **Print all parts**: Hub + 3 arms
2. **Dry fit**: Ensure parts fit together correctly
3. **Tighten finger-tight**: All bolts loosely
4. **Align arms**: Use square to ensure 90° to hub
5. **Tighten progressively**: One bolt per arm, repeat until all tight
6. **Test flatness**: Place on flat surface, check wobble
7. **Mount bed**: Bolt bed to outer arm edges
8. **Mount to leadscrews**: Attach spider to Z-nut mounts

### Bed Mounting Pattern
```
       [Leadscrew 3]
             |
             v
   [Bed Plate 250mm²]
    /              \
 [Arm 1]---[Hub]---[Arm 2]
      |             |      |
      v             v      v
[Leadscrew 1] [Leadscrew 2]

Bed attached to outer edges of 3 arms
```

### Material Considerations
- **Hub**: PETG for heat resistance (near bed heater)
- **Arms**: PETG or PLA+ for stiffness
- **Infill**: 30-40% (grid pattern) for rigidity
- **Walls**: 3-4 perimeters for strength
- **Supports**: Minimal (interlocking design needs few supports)

### Bed Options (Reference Spec)
```
Tier 3 (MKS SKIPR Reference):
- Bed: 250mm² aluminum plate (3mm)
- Heater: 24V 300W silicone heater
- Surface: Prusa MK52 magnetic PEI sheet
- Cost: ~$50-60 AUD total

Tier 1-2 (Salvage):
- Bed: Salvage from donor
- Heater: Salvage from donor
- Surface: Glue PEI sheet, use painter's tape
- Cost: $0-10 AUD
```

### MK52 Magnetic PEI (Prusa Reference)
- **What**: 250mm² magnetic PEI sheet
- **Why**: Easy removal, excellent adhesion, removable
- **Compatibility**: Works with BLTouch AND PINDA (metal particles)
- **Cost**: ~$25 AUD
- **Note**: Requires aluminum bed plate underneath

### Bed Heater Options
```
24V 300W (Recommended for MKS SKIPR):
- Efficient, low current draw
- Good for 250mm²
- ~$20-25 AUD

220V 240W (Salvage path):
- Found in donor printers
- Requires AC relay/mains switching
- Dangerous if not insulated
- Free if salvaged

Silicone vs PCB:
Silicone: Better heat distribution, more expensive
PCB: Cheaper, can delaminate, hotter spots
```

### Thermistor Potting (Critical)
- **Why**: Potted thermistor provides permanent thermal contact
- **How**: High-Temp Red RTV Silicone in thermistor hole
- **Process**:
  1. Drill/cut hole in bed plate (if not present)
  2. Insert thermistor
  3. Fill void with RTV silicone
  4. Cure 24 hours
  5. Verify temperature accuracy
- **Benefit**: No tape failures, no thermal drift, "set-and-forget"

### Maintenance
- **Check bolt tightness**: Every 100 hours
- **Inspect arms**: Check for cracks or deformation
- **Level calibration**: After moving printer or replacing arms
- **Bed flatness**: Check periodically with straightedge

### Common Issues
- **Bed not flat**: Re-check arm-hub alignment, verify bolts tight
- **Sagging under weight**: Increase arm infill, add corner reinforcements
- **Wobbly after assembly**: Loosen bolts, realign, retighten progressively
- **Arms don't fit**: Check print dimensions, may need scaling for donor

## References
- [../manifesto.md](../manifesto.md): Section "The Modular 'Puck' & 'Spider' Concept"
- [Voron Trident Bed](https://vorondesign.com/voron_trident): Three-point kinematic reference
- [Prusa MK3 Bed Assembly](https://help.prusa3d.com/guide/3d-printers/assembly-prusa-i3-mk3s/_25242)
- docs/AI-Conversations/ [Relevant conversations about bed support]
