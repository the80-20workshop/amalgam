# ADR-001: M10 Threaded Rod Skeleton

## Status
Accepted (Updated: M12 → M10)

## Context
The Amalgam requires a rigid frame that maintains dimensional accuracy over years of operation. In 2026, there are multiple frame options available:
- Aluminum extrusions (2020, 2040)
- V-slot profiles
- M8/M10/M10 threaded rods (RepRap heritage)
- 2020 extrusion with printed corners

Modern "appliance" printers often use aluminum extrusions for lightweight frames and high-speed operation. However, this approach creates machines that can be expensive, proprietary, or require complex assembly.

### Original Decision (M12)
The original ADR specified M10 threaded rods, prioritizing maximum rigidity. After deeper analysis documented in `docs/decisions/tractor_01_frame_and_assembly.md`, we reconsidered this choice.

## Decision
We choose **M10 threaded rods** as the reference specification for the Amalgam frame skeleton.

### Why M10 Over M12?

| Feature | M8 | M10 | M12 |
|---------|-----|-----|-----|
| Cross-section | ~50 mm² | ~78 mm² | ~113 mm² |
| Rigidity vs M8 | 1× | 3× | 5× (overkill) |
| Weight/Meter | ~0.3 kg | ~0.5 kg | ~0.7 kg |
| Nut Size (Hex) | 13mm | 17mm | 19mm |
| Printability | Easy | Easy | Can make brackets bulky |

1. **Standard 17mm Wrench**: Universally available (vs 19mm for M12 which is less common)
2. **Easier to Cut**: Hacksaws handle M10 more easily than M12
3. **Smaller Printed Brackets**: M10 fits in more compact corner designs
4. **Scavenger-Friendly**: Common in automotive applications—excellent for salvaging
5. **Adequate Rigidity**: 3× the rigidity of M8 is plenty for a 235×235 build volume
6. **M12 is Overkill**: 5× M8 rigidity provides no practical benefit at our target speeds

### Why Not M8?
M8 remains viable for ultra-budget scavenger builds, but:
- Requires very careful corner design to maintain rigidity
- Less margin for error in assembly
- May flex at larger build volumes (>250mm)

The design remains **parametric**—users can build in M8 or M12 if desired.

## Consequences

### Benefits
- **Long-term stability**: Frame doesn't flex or deform over time
- **No bed tramming**: Once square, the frame stays square
- **Software-compatible**: Heavy frame works with Klipper Input Shaping to cancel remaining resonances
- **Repairable**: Any broken rod can be replaced at a hardware store in minutes
- **Salvage-friendly**: No proprietary extrusions or special hardware required

### Trade-offs
- **Heavy**: The frame is significantly heavier than aluminum alternatives (~15-20kg total)
- **Slower max speeds**: Mass limits max velocity to 70-120mm/s (not 600mm/s like Voron)
- **Longer setup time**: Requires careful alignment and torque of jam nuts
- **Less "pretty"**: Threaded rods have an industrial, exposed look

## BOM Implications (Generic)

### Scenario A: Buying New (Recommended for Tier 3+)
- **Parts needed**:
  - M10 threaded rods (Bright Zinc or Hot-Dip Galvanized)
  - M10 hex nuts (for jam nuts)
  - M10 flat washers
  - 3D-printed corner brackets
- **Cost implication**: Low (~$45-55 AUD for skeleton)
- **Donor compatibility**: All donors
- **Build volume**: Unlimited (cut to length)

### Scenario B: Salvaging from Photocopier/Large Equipment
- **Parts needed**:
  - Scavenged M10 rods (verify straightness)
  - May need to clean threads
  - 3D-printed corner brackets
- **Cost implication**: Very Low ($0-10 AUD for nuts/washers)
- **Donor compatibility**: Only if large equipment has M10 rods
- **Build volume**: Limited to scavenged lengths
- **Note**: May have higher `lumpy_factor` due to worn threads

### Scenario C: Converting from Donor with Aluminum Frame (Ender 3, etc.)
- **Parts needed**:
  - Must buy new M10 rods (aluminum not compatible)
  - Corner brackets replace existing frame parts
  - Some donor hardware may be incompatible
- **Cost implication**: Medium (~$45-55 AUD)
- **Donor compatibility**: All donors, but requires replacing frame
- **Build volume**: Unlimited (cut to length)

### Scenario D: Emergency/Improvised (Not Recommended)
- **Parts needed**:
  - Any available steel rod (may be non-standard diameter)
  - Custom-printed brackets with adjusted dimensions
  - Manual alignment critical
- **Cost implication**: Very Low
- **Donor compatibility**: N/A
- **Build volume**: Limited to available rods
- **Warning**: Significant risk of misalignment, no support in build123d scripts

## Implementation Notes

### Thread Types
- **Bright Zinc Plated**: Smoother threads, `lumpy_factor = 0.2`
- **Hot-Dip Galvanized**: Industrial rust-proof, `lumpy_factor = 0.5+`
- **Black Oxide**: Intermediate, `lumpy_factor = 0.3-0.4`

### Frame Geometry (from config.py)
```
SKELETON_X = BUILD_VOLUME["X"] + (X_OVERHANG * 2) + 40
SKELETON_Y = BUILD_VOLUME["Y"] + 120
SKELETON_Z = BUILD_VOLUME["Z"] + 80
```

For 250mm³ build volume:
- **8x horizontal rods**: ~550mm length
- **4x vertical rods**: ~330mm length
- **Total**: 12 rods

### Assembly Considerations
- Use two jam nuts per joint to prevent vibration loosening
- Verify squareness at each corner during assembly
- Torque nuts to 15-20 ft-lbs (moderate, not extreme)

## References
- [../manifesto.md](../manifesto.md): Section "The Skeleton" and "Why we don't offer a Roller Variant"
- [RepRap Darwin (2007)](https://reprap.org/wiki/Darwin): Original threaded-rod design
- [RepRap Mendel Revisited (M12)](https://www.thingiverse.com/thing:6783269): Modern M12 implementation
- docs/AI-Conversations/ [Relevant conversations about frame selection]
