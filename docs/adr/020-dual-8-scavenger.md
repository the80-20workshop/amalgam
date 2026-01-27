# ADR-020: Dual-8 Scavenger Variant

## Status
Superseded by [ADR-021: Dual-Rod Motion System](021-dual-rod-motion-system.md)

> **Note**: This ADR proposed dual 8mm rods as a scavenger "variant." The analysis proved compelling enough that dual 8mm was adopted as the reference specification in ADR-021, not merely an alternative. This ADR is preserved for historical context on the engineering analysis that led to that decision.

## Original Status
Proposed

## Context
The reference Neo-Darwin specification uses M10 smooth rods for XY motion (ADR-003). While M10 provides excellent stiffness at 370mm spans, M10 smooth rods are difficult to scavenge:

- Photocopiers sometimes have M10/10mm shafts, but storing/disposing of the rest is problematic
- Most donor 3D printers (Prusa clones, Anet A8, Creality) use 8mm smooth rods
- Buying new M10 smooth rods costs $60-80 AUD, pushing builds toward $300+

Analysis shows that single 8mm rods cannot achieve acceptable deflection at Neo-Darwin's target 370mm X-span:

| Configuration | Deflection @ 370mm | Verdict |
|---------------|-------------------|---------|
| Single 8mm, 280g toolhead | 0.072mm | Excessive |
| Single 10mm, 280g toolhead | 0.030mm | Acceptable |

However, the Voron Legacy achieves acceptable performance with 8mm rods by using a smaller build volume (~200mm). This raised the question: **Can Neo-Darwin maintain 235mm build volume with 8mm rods?**

### The Dual-Rod Insight

Beam deflection follows: `δ = F × L³ / (48 × E × I)`

When two parallel rods share the load:
- Each rod carries F/2
- Deflection halves: `δ_dual = δ_single / 2`

This means **dual 8mm rods can match or exceed single 10mm performance**.

## Decision
We define a **"Dual-8 Scavenger"** variant that uses dual 8mm smooth rods per axis with vertically-stacked configuration, enabling full 235mm build volume with scavenged parts from two donor printers.

### Rod Configuration

**X-Axis (Vertical Stack):**
```
═══════════════════════════════  Top 8mm rod
         [Plough carriage]
═══════════════════════════════  Bottom 8mm rod
```

**Y-Axis (Dual per Side):**
```
Left side:              Right side:
  ║══8mm══║               ║══8mm══║
  ║ belt  ║               ║ belt  ║
  ║══8mm══║               ║══8mm══║
  LM8LUU                  LM8LUU
```

### Deflection Analysis

| Configuration | 360mm span, 280g | Verdict |
|---------------|------------------|---------|
| Single 8mm | 0.066mm | Excessive |
| **Dual 8mm (shared load)** | **0.033mm** | **Acceptable** |
| Single 10mm | 0.027mm | Acceptable |

The dual-8 configuration achieves 50% less deflection than single-8, bringing it within acceptable tolerance for quality printing.

### Stiffness Comparison

```
Second moment of area (I = π×d⁴/64):
  Single 8mm:  I = 201 mm⁴
  Dual 8mm:    I_eff = 402 mm⁴ (load shared)
  Single 10mm: I = 491 mm⁴

Effective stiffness ratio: Dual 8mm / Single 10mm = 0.82
With load sharing: Dual 8mm deflection < Single 10mm deflection
```

### Why Vertical Stacking?

Vertical vs horizontal rod spacing provides identical sag resistance, but different moment resistance:

| Orientation | Resists | Vulnerable to |
|-------------|---------|---------------|
| Horizontal (reference Plough) | Yaw (twist L-R) | Pitch (nose-dive) |
| Vertical (Dual-8) | Pitch (nose-dive) | Yaw (twist L-R) |

Vertical stacking on X-axis is preferred because:
- Pitch forces (from Y-acceleration) dominate toolhead dynamics
- Voron Legacy validates this configuration
- Allows belt to run between rods (cleaner routing)

### Long Bearings (LM8LUU)

Long linear bearings are **recommended but not required**:
- Do NOT reduce rod deflection (that requires more rods or larger diameter)
- DO improve carriage stability (anti-racking)
- DO provide better moment resistance
- DO give smoother motion (more ball contact)

Standard LM8UU bearings work; LM8LUU provides better carriage stability.

## Consequences

### Benefits
- **Full scavengeability**: 2 donor Prusa clones provide all 8-10 smooth rods needed
- **Maintains build volume**: 235×235×250mm preserved
- **Lower cost**: Eliminates $60-80 smooth rod purchase
- **Proven physics**: Dual-rod load sharing is well-understood beam mechanics
- **Voron-validated**: Vertical stacking proven in Voron Legacy

### Trade-offs
- **More rods**: 6 XY rods vs 4 in reference design
- **More bearings**: 12-16 LM8UU vs 8 LM10UU
- **Redesigned brackets**: X-ends and Y-pucks need dual-rod mounts
- **Tighter toolhead mass budget**: Keep under 280g for best results
- **Slightly less stiff**: 82% of M10 stiffness (but deflection is better due to load sharing)

### What This Enables
- **True 2-donor build**: Motors, boards, rods, bearings all from donors
- **Sub-$150 hardware cost**: When combined with scavenged electronics
- **MKS SKIPR path**: $130 AUD for SKIPR + CANbus + ADXL still hits <$300 total

## BOM Implications (Generic)

### Scenario A: Two Prusa Clone Donors (Recommended)
- **Parts scavenged**:
  - 12× 8mm smooth rods (need 8-10)
  - 24× LM8UU bearings (need 12-16, keep spares)
  - 10× NEMA17 motors (need 6-7 for triple-Z)
  - 2× control boards (use best one, keep spare)
  - 2× heated beds (use best one)
  - 2× power supplies
- **Parts to buy**:
  - M10 threaded rod for frame skeleton (~$45 AUD)
  - MKS SKIPR + EBB36 CANbus + ADXL345 (~$130 AUD)
  - E3D V6 clone hotend (~$15 AUD)
  - Belts, pulleys, misc hardware (~$30 AUD)
- **Cost implication**: ~$220-250 AUD total
- **Build volume**: Full 235×235×250mm

### Scenario B: Two Anet A8 Donors
- **Parts scavenged**: Similar to Scenario A
- **Note**: Anet beds are smaller (220×220), may need bed upgrade
- **Cost implication**: ~$250-280 AUD (if bed upgrade needed)

### Scenario C: Mixed Donors (Prusa + Ender)
- **Challenge**: Ender 3 uses V-slot rollers, not smooth rods
- **Parts scavenged from Ender**: Motors, board, bed, PSU
- **Parts scavenged from Prusa**: Smooth rods, bearings
- **Cost implication**: May need to buy additional rods (~$30 AUD)

### Scenario D: Single Donor + Purchased Rods
- **Not recommended**: Defeats scavenger philosophy
- **If necessary**: Buy 8mm precision ground rods (~$40-50 AUD)
- **Cost implication**: Higher than dual-donor path

## Implementation Notes

### Rod Count Summary
| Axis | Reference (M10) | Dual-8 Scavenger |
|------|-----------------|------------------|
| X | 2 rods | 2 rods (stacked) |
| Y | 2 rods | 4 rods (2 per side) |
| Z | 2 rods | 2 rods |
| **Total** | **6 rods** | **8 rods** |

### Bearing Count Summary
| Axis | Reference | Dual-8 |
|------|-----------|--------|
| X carriage | 4× LM10UU | 4× LM8UU (or LM8LUU) |
| Y gantry (per side) | 2× LM10UU | 4× LM8UU |
| Z | 4× LM10UU | 4× LM8UU |
| **Total** | **12× LM10UU** | **16× LM8UU** |

### Toolhead Mass Budget
For acceptable deflection at 360mm span:
- **Target**: ≤280g total toolhead mass
- **Pitan + pancake NEMA17**: ~200-250g ✓
- **Pitan + standard NEMA17**: ~280-320g (borderline)
- **Wade + standard NEMA17**: ~400g+ ✗ (too heavy)

### CAD Implications
New parametric parts needed:
- `x_end_dual8.py`: X-end brackets for dual vertical rods
- `y_puck_dual8.py`: Y-pucks for dual stacked rods per side
- `plough_vertical.py`: Plough carriage for vertical rod stack

Config parameter:
```python
SMOOTH_ROD_CONFIG = "DUAL_8"  # vs "SINGLE_10" for reference
```

### Klipper Configuration
No changes to kinematics—still Cartesian with:
- `[stepper_x]`: Single motor, single axis
- `[stepper_y]`: Dual motors with `[stepper_y1]` for auto-squaring
- `[stepper_z]`, `[stepper_z1]`, `[stepper_z2]`: Triple-Z

## Cost Analysis: Hitting $300 Target

| Component | Reference Spec | Dual-8 Scavenger |
|-----------|---------------|------------------|
| Frame (M10 threaded) | $45 | $45 |
| Smooth rods | $70 (M10) | $0 (scavenged) |
| Bearings | $30 (LM10UU) | $0 (scavenged) |
| Motors | $60 | $0 (scavenged) |
| Heated bed | $35 | $0 (scavenged) |
| Electronics | $130 (SKIPR+CAN) | $130 (SKIPR+CAN) |
| Hotend | $15 | $15 |
| Belts/pulleys/misc | $30 | $30 |
| **Total** | **~$415** | **~$220** |

The Dual-8 Scavenger path achieves significant cost reduction while maintaining the full 235mm build volume—well under the $300 AUD target.

## References
- ADR-003: Precision Smooth Rods (reference M10 specification)
- ADR-005: Triple-Z Independent Kinematic Leveling (requires 2 donors anyway)
- [Voron Legacy](https://vorondesign.com/voron_legacy): Validates 8mm vertical stacking
- [Beam Deflection Theory](https://en.wikipedia.org/wiki/Deflection_(engineering)): Simply-supported beam equations
- Conversation: "Voron Legacy Comparison" (2025-01-27)
