# ADR-011: Laminated Plinth Baseboard

## Status
Accepted

## Context
The Amalgam is a heavy machine:
- M12 iron skeleton: ~15kg
- 3x Z-motors + geared extruder: ~3kg
- Total build weight: ~18-20kg

A "Naked Frame" (frame sitting directly on workspace) has limitations:
1. **Vibration Transmission**: Frame acts as speaker for motor noise
2. **Portability Issues**: Picking up frame can flex/twist it
3. **High-Frequency Resonance**: Can cause ringing/ghosting
4. **Floor Interaction**: Uneven surfaces affect frame squareness

At the same time, a well-grounded mass is an engineering advantage—mass damps vibration. The question is how to anchor that mass properly.

## Decision
We adopt a **Laminated Plinth Baseboard** as the Tier 3 Reference Spec foundation, using **Constrained Layer Damping (CLD)** to convert motor vibrations into microscopic heat.

### Architecture

**The Plinth**: Two 18mm MDF boards (36mm total thickness) glued together with viscoelastic adhesive.

**Construction**:
```
┌─────────────────────────────────────┐
│   Top MDF Board (18mm)              │
│   ↓                                 │
│   Viscoelastic Glue Layer (CLD)     │ ← Converts vibration to heat
│   ↓                                 │
│   Bottom MDF Board (18mm)           │
│   ↓                                 │
│   Rubber Feet (4x corners)          │
└─────────────────────────────────────┘
```

**Frame Attachment**:
- M12 rods pass through drilled holes in plinth
- Secured with large fender washers + M12 nuts on underside
- Frame bolts down to plinth (through-bolted)
- Z-pucks either clamped to rods (Naked) or screwed to MDF (Tier 3)

### Why Laminated?

**1. Constrained Layer Damping (CLD)**
- When motors vibrate, they send sound waves through plinth
- Glue layer is stretched/compressed (shear strain)
- Mechanical friction in glue converts kinetic energy to heat
- Result: Vibration "dies" in glue instead of ringing through frame

**2. Glue Choice Matters**
- **Standard PVA Wood Glue**: Dries hard → very stiff but poor damping
- **Green Glue / Construction Adhesive**: Stays slightly rubbery → maximizes energy conversion (acoustically dead)
- **Viscoelastic**: The gold standard for CLD in industrial/audio applications

**3. Massive Inertia**
- 36mm MDF slab anchored to M12 frame creates ~20kg+ workstation
- Provides heavy ballast resisting high-acceleration moves
- Machine won't budge or twist during operation

**4. Rods Become Alignment Rails**
- Without plinth: M12 rods carry total weight (suspended load)
- With plinth: MDF handles weight, rods ensure X/Y gantry square to bedrock
- Shifts from "support" role to "alignment" role

### Foundation Strategy Levels

| Configuration | Effort | Stability | Resonance Peak | Recommended For |
|----------------|--------|-----------|---------------|-----------------|
| **Naked Frame (No pads)** | Low | Moderate | High (Ringing) | Emergency/Tier 1 |
| **Naked + Rubber Pads** | Low | High | Medium | Tier 1-2 |
| **Single MDF Board** | Medium | Very High | Low | Tier 2-3 |
| **Laminated Plinth** | High | **Industrial** | **Negligible** | **Tier 3 Reference** |

### Z-Puck Mounting on Plinth

**The Zero-Flex Anchor**:
- Z-pucks use flanged design screwed directly into MDF
- Slotted mounting holes allow alignment adjustment
- MDF acts as massive vibration sink for Z-motors (which move most weight)

**The Hybrid Anchor**:
- Even with plinth mounting, use Double-Nut Anchor (see ADR-010)
- M12 rod passes through puck + MDF, locked by nuts
- "Handshakes" iron skeleton to plinth
- Accommodates MDF expansion/contraction from humidity

## Consequences

### Benefits
- **Industrial Silence**: Negligible resonance, no ringing/ghosting
- **Structural Rigidity**: Frame bolted to massive base can't lose squareness
- **Portability**: Easier to move—pick up by plinth, frame stays square
- **Vibration Isolation**: Z-motor vibrations sink into plinth, don't reach print
- **Thermal Stability**: MDF is less affected by ambient temperature swings
- **Professional Feel**: Machine becomes "industrial tool" rather than "toy"

### Trade-offs
- **Weight**: Final machine ~20-25kg (very heavy)
- **Assembly Effort**: Requires woodworking (cutting, drilling, gluing)
- **Space**: Larger footprint than naked frame
- **Cost**: Adds $20-30 AUD for MDF + adhesive
- **Lead Time**: Glue needs 24hr cure before drilling
- **Permanent**: Once built, machine is semi-permanent workstation

### What This Enables
- **Tier 3 Reference Spec**: Industrial-grade ±0.1mm accuracy
- **Perfect First Layers**: Vibration-free foundation aids leveling
- **Engineering Materials**: ABS, PC, Nylon benefit from stable environment
- **Quiet Operation**: Combined with software, machine is near-silent

### What This Replaces
- Naked frame with rubber pads
- Need for perfectly flat workspace (plinth compensates)
- Frequent frame re-squaring

## BOM Implications (Generic)

### Scenario A: Tier 1-2 Builds (Naked Frame)
- **Recommended**: Rubber pads under corners only
- **Cost implication**: Very Low (+$10-15 AUD)
- **Assembly**: No woodworking required
- **Performance**: Good enough for hobby printing

### Scenario B: Tier 2-3 Upgrade (Single Board)
- **Parts needed**:
  - 1x 18mm MDF board (cut to script dimensions)
  - 4x M12 nuts + fender washers (for frame thru-bolting)
  - Optional: Z-puck wood screws
- **Cost implication**: Low (+$15-20 AUD)
- **Assembly**: Cut board, drill using template
- **Performance**: Very good, significant vibration reduction

### Scenario C: Tier 3 Reference (Laminated Plinth)
- **Parts needed**:
  - 2x 18mm MDF boards (cut to script dimensions)
  - 1x Tube viscoelastic adhesive (Green Glue or construction adhesive)
  - 6x Wood screws (for Z-pucks, if not clamped to rods)
  - 4x Large fender washers (50mm+ dia)
  - 4x M12 nuts + washers (underside of MDF)
  - 4x Rubber feet (for plinth corners)
- **Cost implication**: Low (+$20-30 AUD)
- **Assembly**:
  - Glue boards together (24hr cure)
  - Drill holes using build123d template
  - Thru-bolt frame to plinth
  - Mount Z-pucks
- **Performance**: Industrial-grade, negligible resonance

### Donor Compatibility
- **All donors**: Plinth is independent of donor parts
- **Salvage Benefit**: Donor printers often have beds that need stable platform

## Implementation Notes

### MDF Dimensions (from build123d)
```
PLINTH_X = SKELETON_X + 100  # 50mm overhang each side
PLINTH_Y = SKELETON_Y + 100  # 50mm overhang each side
PLINTH_Z = 36mm              # 2x 18mm boards
```

For 250mm³ build volume (MK52):
- Frame: ~550mm × ~370mm
- Plinth: ~650mm × ~470mm × 36mm

### Build Procedure

**Phase 1: Preparation**
1. Cut both MDF boards to exact dimensions
2. Clean surfaces (remove dust)
3. Clamp boards together evenly
4. Apply viscoelastic adhesive in serpentine pattern (approx. 3mm bead)
5. Re-clamp with even pressure
6. Cure 24 hours (follow adhesive spec)

**Phase 2: Drilling**
1. Use build123d-generated drill template
2. Template includes:
   - M12 rod hole positions (8 total: 4 front, 4 rear)
   - Z-puck mounting positions (3 front, 0 rear if clamped)
   - Corner hole for fender washers (4)
   - Alignment marks for frame placement
3. Drill all holes with appropriate bits:
   - M12 holes: 12.5mm drill bit
   - Puck screws: Pilot bit matching screw size
   - Fender washers: Clearance holes

**Phase 3: Assembly**
1. Place plinth on rubber feet
2. Insert M12 rods through plinth holes
3. Install fender washers + nuts underneath (hand-tight)
4. Assemble corner brackets onto rods
5. Position Z-pucks:
   - If clamped: Slide onto rods, use double-nut anchor (see ADR-010)
   - If screwed: Position on MDF, use slotted holes for alignment
6. Home bed, align Z-pucks to lead screws
7. Tighten all connections fully:
   - M12 thru-bolts: 15-20 ft-lbs
   - Z-puck clamps: 2-3 Nm
   - Puck wood screws: Firm, don't strip MDF

**Phase 4: Validation**
1. Verify frame is level on plinth
2. Check all M12 nuts are tight
3. Tap plinth - should sound "dead", not ringing
4. Perform Z-tilt calibration
5. Print test tower, check for resonance

### Drill Template Features
The build123d script generates a printable template:
- **Full-size paper template**: Tape to MDF for drilling
- **Alignment marks**: Ensures consistent positioning
- **Hole size labels**: Confirms drill bit selection
- **Z-puck slot positions**: Pre-marked for puck mounting

### Counter-Sinking (Optional)
For flush underside:
- Counter-sink M12 nuts 5mm into bottom board
- Use template to mark positions before gluing
- Result: Machine sits perfectly flat on workbench

### Environmental Considerations
- **Humidity**: MDF expands/contracts - use Hybrid Anchor with double-nuts
- **Moisture**: Keep plinth dry, consider sealing edges with paint/varnish
- **Temperature**: MDF is stable, but avoid extreme heat sources

### Safety Considerations
- **Dust**: MDF dust is harmful - use mask/ventilation when cutting/drilling
- **Weight**: Get help moving 36mm plinth - it's very heavy
- **Adhesive**: Follow manufacturer safety instructions (PPE, ventilation)
- **Torque**: Don't over-tighten M12 nuts into MDF - may pull through

## References
- **docs/reference/ai-conversations/baseboard.md**: Complete technical discussion
- **docs/adr/010-floating-z-puck.md**: Z-puck mounting on plinth
- **docs/adr/001-m12-skeleton.md**: Frame architecture
- [../manifesto.md](../manifesto.md): "The Bed is the Anchor; the Plinth is the Bedrock" pillar
- [../manifesto.md](../manifesto.md): Tier 3 Reference Spec

## Evolution Notes
This ADR establishes the laminated plinth as the optimal foundation for Tier 3 builds. The plinth concept can be adapted for different applications (e.g., enclosed build chamber, heated build chamber) while maintaining CLD principles.

**Related Standards**:
- CLD widely used in automotive, aerospace, and high-end audio
- Green Glue Noiseproofing Compound: Commercial viscoelastic adhesive
- Industrial machine tools often use similar laminated bases
