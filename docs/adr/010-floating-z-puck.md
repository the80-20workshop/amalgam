# ADR-010: Floating Z-Puck System

## Status
Accepted

## Context
The Amalgam supports various bed sizes (from salvaged donor beds to MK52 250mm²). Traditional integrated Z-motor mounts (built into corner brackets) create a "parametric paradox":

1. **Frame Lock-in**: Motor position determines bed width
2. **No Adjustment**: Small manufacturing tolerances (bent rods, "lumpy" prints) cause permanent Z-misalignment
3. **Rebuild Required**: Upgrading bed size requires replacing entire iron skeleton

This creates a choice between:
- **Optimized Frame**: Minimal size for current bed, but rebuild needed for upgrades
- **Reference Frame**: Built for MK52 size, but mounting motors for smaller beds is challenging

## Decision
We adopt a **Floating Z-Puck System** for all three Z-motors, decoupling the iron skeleton from bed dimensions.

### Architecture

**The Puck**: A 3D-printed motor mount that slides along the front and rear M12 Z-rods, positioned to match any bed width.

**The Double-Nut Anchor**:
```
M12 Rod
    ↓
[Upper M12 Nut]
    ↓
[  Z-Puck (clamp)  ]
    ↓
[Lower M12 Nut]
```

- The puck is clamped to the M12 threaded rod
- Two standard M12 hex nuts trap the puck vertically
- Even if the clamp fails, the nuts provide physical fail-safe

### Why This Works

**1. Parametric Flexibility**
- Frame can be built for MK52 Reference Spec (250mm²)
- Pucks slide inward for smaller salvaged beds
- Upgrade later: only print new bed-arms, slide pucks outward
- Iron skeleton never touched

**2. The "Nylon Jam" Effect**
- Threaded rods are superior to smooth rods for clamping
- Split-clamp design deforms plastic into M12 thread valleys
- Creates mechanical interlock preventing rotation/slip
- Smooth rods rely only on friction

**3. Vibration Isolation**
- Integrated motors turn entire frame into "tuning fork"
- Floating pucks break solid vibration transmission path
- Plastic between motor and rod dampens high-frequency noise

**4. Precision Alignment (The "True-Vertical" Rule)**
- Z-wobble primarily caused by misaligned motors, not loose ones
- Integrated corners force user to live with 0.5mm misalignment
- Floating pucks allow loosening, homing bed to find "natural" center, then tightening
- Ensures perfect motor/lead-screw concentricity

### Build Wizard Logic

```
Configuration Wizard
├─ Frame Size
│  ├─ Option A: Optimized for Salvage (current bed only)
│  │  └─ Result: Minimal footprint, rebuild needed for upgrades
│  └─ Option B: Future-Proof (MK52 Reference Spec) ★
│     └─ Result: Larger footprint, upgrade bed by sliding pucks
├─ Z-Puck Mode
│  ├─ Naked Frame: Pucks clamped to rods + rubber pads under corners
│  └─ Laminated Plinth: Pucks screwed into MDF base (see ADR-011)
```

**Scale Limit**: Automatic scaling capped at MK52 (~250mm²). Larger sizes require manual engineering due to:
- M12 frame stability limits
- Thermal management limits (PSU/heater capacity)

## Consequences

### Benefits
- **Future-Proof**: Build once for MK52, use with any smaller bed
- **No Rebuilds**: Bed upgrades require only new bed-arms, not iron skeleton
- **Precision Alignment**: Eliminates Z-wobble from motor misalignment
- **Reduced Vibration**: Decoupled motors transmit less noise to frame
- **Single Design**: One Z-puck design works for all configurations
- **Fail-Safe**: Double-nut anchor prevents catastrophic failures

### Trade-offs
- **Slightly More Complex**: Additional assembly step vs integrated corners
- **Manual Alignment**: Requires user to position pucks during build
- **Cantilever Concern**: Theoretical micro-flex (mitigated by double-nut anchor)
- **Parts Count**: Two extra M12 nuts per Z-motor (6 total)

### What This Enables
- **Tier 1-2 Builds**: Small salvaged beds on Reference Spec frame
- **Tier 3 Builds**: MK52 beds with same iron foundation
- **Modular Puck System**: Consistent motor mounting across entire machine
- **Parametric Build Scripts**: No need for separate "integrated" and "floating" variants

### What This Replaces
- Integrated Z-motor corners (frame-locked to bed size)
- Fixed-position Z-motor mounts
- Multiple corner variants for different bed sizes

## BOM Implications (Generic)

### Universal Requirements (All Scenarios)
- **Parts needed**:
  - 3x Floating Z-Puck 3D prints
  - 6x M12 hex nuts (for double-nut anchors)
  - 6x M12 flat washers
  - 3x NEMA 17 stepper motors (Z-axis)
  - 3x Lead screws (8mm, TR8x2 or TR8x1.5)
  - 3x Lead screw couplers
- **Cost implication**: Low (~$30-40 AUD for hardware + plastic)
- **Donor compatibility**: All donors (motors salvaged, lead screws salvaged)

### Scenario A: Naked Frame (Tier 1-2)
- **Additional parts**:
  - 4x High-density rubber or vibration-dampening pads (corner feet)
- **Assembly**: Clamp pucks to rods, no woodworking
- **Cost implication**: Very Low (+$10-15 AUD for pads)
- **Stability**: Moderate (relies on frame mass + pads)

### Scenario B: Laminated Plinth (Tier 3)
- **Additional parts**:
  - 2x 18mm MDF boards (see ADR-011 for dimensions)
  - Viscoelastic adhesive (Green Glue or construction adhesive)
  - 6x Wood screws (to secure pucks to MDF)
  - 4x Large fender washers (for frame thru-bolting)
  - 4x M12 nuts + washers (underside of MDF)
- **Assembly**: Drill template required, screw pucks to MDF
- **Cost implication**: Low (+$20-30 AUD for MDF + adhesive)
- **Stability**: Very High (industrial-grade)

### Scenario C: Future-Proof Build Path
- **Initial Build**: Scenario A (Naked Frame) with small salvaged bed
- **Upgrade Path**: Add laminated plinth + slide pucks outward for MK52
- **Cost implication**: Spread over time, minimal additional parts
- **Benefit**: No need to replace iron skeleton

## Implementation Notes

### Puck Design Specifications
- **Clamping**: Split-clamp design with M3 or M4 bolt
- **Motor Mount**: Standard NEMA 17 pattern (31mm bolt circle)
- **Rod Clearance**: M12 rod clearance ~12.5mm
- **Slot Design** (if plinth-mounted): 10mm slots for alignment adjustment
- **Nut Traps** (optional): Can incorporate nut traps for double-nut anchor

### Assembly Sequence

**For Naked Frame Builds**:
1. Assemble M12 skeleton on rubber pads
2. Install lead screws through pucks
3. Thread pucks onto front Z-rods
4. Slide to match bed width
5. Install upper/lower M12 nuts (hand-tight)
6. Clamp puck with bolt (compress into threads)
7. Tighten nuts fully, torque clamp bolt
8. Home bed to check alignment, adjust if needed

**For Laminated Plinth Builds**:
1. Prepare laminated MDF plinth (see ADR-011)
2. Drill holes using build123d template
3. Install Z-pucks on MDF with wood screws (loosely)
4. Thread M12 rods through pucks + MDF
5. Secure rods with fender washers + nuts underneath
6. Slide pucks to match bed width
7. Home bed, align motors to lead screws
8. Tighten wood screws fully
9. Add double-nut anchors above/below pucks

### Alignment Procedure
1. Install lead screws and connect to bed
2. Loosen all Z-puck clamps
3. Home Z-axis to bottom
4. Verify all 3 motors rotate smoothly
5. If any motor binds, slightly reposition puck
6. Repeat homing until all rotate freely
7. Tighten clamps + double-nut anchors
8. Perform Z-tilt calibration in Klipper

### Safety Considerations
- **Double-Nut Anchor**: Always use, even with strong clamp
- **Torque Specs**: Clamp bolt to ~2-3 Nm (don't crack plastic)
- **Thread Engagement**: Ensure M12 nuts fully engaged (≥10mm)
- **Plinth Screws**: Use appropriate length for MDF (1.5x board thickness)

## References
- **docs/reference/ai-conversations/floating-z-puck.md**: Complete technical discussion
- **docs/adr/011-laminated-plinth.md**: Baseboard foundation strategy
- **docs/adr/001-m12-skeleton.md**: Frame architecture
- **docs/adr/005-triple-z.md**: Triple-Z kinematic leveling
- [../manifesto.md](../manifesto.md): "The Bed is the Anchor" pillar
- [../manifesto.md](../manifesto.md): Modular Puck & Spider concept

## Evolution Notes
This ADR establishes the Z-puck as a universal mounting system that supports all bed sizes and foundation strategies. Future variations (e.g., different motor types, direct-drive Z) will maintain this modular approach.
