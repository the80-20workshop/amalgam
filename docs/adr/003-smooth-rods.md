# ADR-003: Precision Smooth Rods

## Status
Superseded by [ADR-021: Dual-Rod Motion System](021-dual-rod-motion-system.md)

> **Note**: This ADR established M10 single-rod as the reference specification. Subsequent analysis (ADR-020, ADR-021) demonstrated that dual 8mm rods with shared load achieve equal or better deflection performance while being fully scavengeable from donor printers. ADR-021 now defines the reference specification.

## Original Status
Accepted

## Context
Linear motion is critical for dimensional accuracy. The linear guides determine how smoothly the gantry moves and how well the printer maintains position.

In 2026, there are multiple linear motion options:
- Precision ground smooth rods with linear bearings
- Linear rails (MGN9, MGN12, MGN15)
- V-slot rollers on aluminum extrusion
- Open builds with printed bearings

Modern printers often use linear rails for high-speed operation and minimal maintenance. Budget printers (Ender 3) use V-slot rollers for low cost. However, both options have trade-offs for a "forever machine."

## Decision
We choose **precision ground smooth rods with linear bearings** as the reference linear motion system.

### Why Smooth Rods?
1. **Parallelism**: Easier to align two rods than shim linear rails
2. **Maintenance**: Simple wipe-and-oil vs complex rail "re-balling"
3. **Longevity**: Rods don't wear like roller wheels or cheap linear rails
4. **Cost**: Significantly cheaper than quality linear rails
5. **Scalability**: Available in multiple diameters for different use cases
6. **Frame Integration**: Natural pairing with M12 threaded-rod skeleton
7. **Industrial aesthetics**: "Circles and Torque" philosophy

### Diameter Decision Tree
- **8mm**: Salvage path (Anet, Prusa clones, photocopiers)
- **10mm**: "Neo" standard (2.4× stiffer than 8mm, recommended)
- **MGN12 Rails**: Tinker path (for high-speed experiments)

## Consequences

### Benefits
- **Proven reliability**: Decades of use in RepRap and CNC
- **Easy alignment**: Two rods naturally create parallel guide
- **Low friction**: Linear bearings roll smoothly with minimal drag
- **Repairable**: Replace individual bearings vs entire rail assembly
- **Cost-effective**: Full set ~$50-80 AUD vs $200+ for quality rails
- **Frame-friendly**: Easy to mount to M12 threaded-rod frame with printed clamps

### Trade-offs
- **Not as smooth as quality rails**: Higher friction than MGN12
- **Requires oiling**: Maintenance interval (every ~100 hours)
- **Limited length**: Very long builds may need multiple joined rods
- **Stiffness limits**: 10mm is max practical diameter

### Why NOT V-Slot Rollers?
1. **Frame mismatch**: V-slot requires aluminum extrusion, not M12 rods
2. **Wear pattern**: Rollers develop flat spots over time
3. **Crunchy budget rails**: Cheap rails suffer from "crunchy" bearing issues
4. **Difficult alignment**: Perfectly shimming rails is challenging for beginners

### Why NOT Linear Rails (for Base Spec)?
1. **Cost**: Quality MGN12 rails cost 4-5× more than rods
2. **Alignment complexity**: Requires precision shimming for parallelism
3. **Over-engineering**: For 70-120mm/s, rods are sufficient
4. **Donor incompatibility**: Most salvaged printers don't use rails

**Note**: The "Motion Pucks" are designed with mounting points for MGN12 rails for tinkerers who want high-speed upgrades.

## BOM Implications (Generic)

### Scenario A: Buying New 10mm (Recommended for Tier 3+)
- **Parts needed**:
  - X-axis: 2x 370mm smooth rods (10mm)
  - Y-axis: 2x 350mm smooth rods (10mm)
  - Z-axis: 2x 320mm smooth rods (10mm)
  - 12x LM10UU linear bearings
- **Cost implication**: Medium (~$60-80 AUD)
- **Donor compatibility**: All donors (replaces existing motion)
- **Build volume**: Unlimited (cut to length)
- **Note**: 10mm has 2.4× stiffness over 8mm

### Scenario B: Salvaging from Donor with 8mm (Prusa i3, Anet)
- **Parts needed**:
  - Salvage: 8mm smooth rods from donor
  - Salvage: LM8UU bearings from donor
  - May need to clean/polish rods
- **Cost implication**: Very Low ($0-10 AUD for cleaning)
- **Donor compatibility**: Prusa i3, Anet A8, Prusa MK2/3
- **Build volume**: Limited to salvaged lengths
- **Note**: 8mm is lighter but less rigid

### Scenario C: Donor has V-Slot Rollers (Ender 3, CR-10)
- **Parts needed**: **MUST BUY**
  - 6x smooth rods (8mm or 10mm)
  - 10-12x linear bearings (LM8UU or LM10UU)
  - Cannot use existing rollers
- **Cost implication**: Medium (~$50-70 AUD)
- **Donor compatibility**: Ender 3, CR-10, V-Core
- **Build volume**: Unlimited (cut to length)
- **Note**: **Critical** - rollers incompatible with M12 frame

### Scenario D: Salvaging from Photocopier/Office Equipment
- **Parts needed**:
  - Scavenge: 8mm or 10mm precision shafts
  - May need to replace bearings
- **Cost implication**: Very Low ($0-15 AUD)
- **Donor compatibility**: Office laser printers, scanners
- **Build volume**: Limited to scavenged lengths
- **Quality**: Often higher quality than budget rods
- **Note**: Verify straightness and diameter consistency

### Scenario E: Linear Rail Upgrade (Tinker Path)
- **Parts needed**:
  - MGN12H x 4 (or MGN9H for lighter builds)
  - 4x carriages per axis
  - Custom printed "Rail Pucks"
- **Cost implication**: High (~$200-300 AUD for quality rails)
- **Donor compatibility**: N/A (requires new purchase)
- **Build volume**: Limited to rail lengths
- **Experience**: High-speed capable (200mm/s+)
- **Warning**: Requires precise alignment and shimming

### Scenario F: Emergency/Improvised (Not Recommended)
- **Parts needed**:
  - Any steel rod of correct diameter
  - May use generic bearings
- **Cost implication**: Very Low
- **Donor compatibility**: Any steel rod source
- **Build volume**: Limited to available rods
- **Warning**: Significant risk of poor surface finish, dimensional inaccuracy
- **No support**: build123d scripts not designed for non-standard rods

## Implementation Notes

### Rod Length Calculation (from config.py)
```
# For 250mm³ build volume with Wade extruder
X_OVERHANG = 50.0 (Wade gear overhang)

X-axis rods: BUILD_VOLUME["X"] + (X_OVERHANG * 2) + clearance
            = 250 + 100 + 20 = 370mm

Y-axis rods: BUILD_VOLUME["Y"] + cable_management + clearance
            = 250 + 80 + 20 = 350mm

Z-axis rods: BUILD_VOLUME["Z"] + Z-puck_height + carriage_clearance
            = 250 + 50 + 20 = 320mm
```

### Bearing Configurations
```
SMOOTH_ROD_DIA = 10.0 → BEARING_TYPE = "LM10UU"
SMOOTH_ROD_DIA = 8.0  → BEARING_TYPE = "LM8UU"
```

### X-Axis Carriage
- 4 bearings per carriage (2 per rod)
- Spaced ~60mm apart for stability
- Printed carriage provides bearing housing

### Y-Axis Gantry
- 4 bearings per side (2 per rod)
- Dual-rod Y-gantry for stability
- Printed gantry brackets

### Z-Axis Motion
- 4 bearings total (2 per rod)
- Single-rod Z with linear bearings
- Z-pucks provide structural mount to M12 frame

### Maintenance
- **Cleaning**: Wipe rods with IPA or clean cloth every ~50 hours
- **Lubrication**: Light machine oil (3-in-One or sewing machine oil)
- **Inspection**: Check for rust, scratches, or bearing wear every ~100 hours
- **Replacement**: Bearings ~$1-2 AUD each (cheap to replace)

### Quality Indicators
- **Look for**: "Precision Ground" or "Hardened" marking
- **Avoid**: "Construction" or "general purpose" rods (too rough)
- **Test**: Roll bearing across rod - should be smooth with no grinding
- **Measure**: Verify diameter with calipers (critical for bearing fit)

## References
- MANIFESTO.md: Section "The Motion System" and "Why we don't offer a Roller Variant"
- [RepRap Mendel Revisited](https://www.thingiverse.com/thing:6783269): Modern smooth rod implementation
- docs/AI-Conversations/ [Relevant conversations about linear motion]
