# ADR-024: Heated Bed Size Selection

## Status
Accepted

## Context

Neo-Darwin's scavenger philosophy requires that the heated bed come from donor printers. The dual-rod motion system (ADR-021) provides flexibility in build volume, but the bed size should align with what's actually scavengeable.

### Previous Specification

The original config specified 250×250×250mm build volume, which is **larger than any standard donor bed**. This was aspirational rather than practical for scavenger builds.

### The Dual-Donor Reality

ADR-021 (Dual-Rod Motion) and ADR-005 (Triple-Z) establish that Neo-Darwin requires **two donor printers** for a practical scavenger build:
- 6-7 NEMA17 motors needed (most donors have 4-5)
- 8 smooth rods needed for Dual-8 configuration
- Single donor cannot provide enough parts

Given two donors, the scavenger approach is: **use the smaller of the two beds**.

### Donor Printer Bed Survey

#### Donors WITH 8mm Smooth Rods

These donors provide both beds AND rods for the Dual-8 build:

| Donor Printer | Bed Size | Smooth Rods | Notes |
|---------------|----------|-------------|-------|
| Prusa i3 clones | 200×200mm | 6× 8mm | Original RepRap lineage |
| Anet A8 | 220×220mm | 6× 8mm | Massively popular, cheap |
| Anet A6 | 220×220mm | 6× 8mm | Similar to A8 |
| Prusa MK2 | 250×210mm | 6× 8mm | Rectangular bed |
| Prusa MK3/MK3S+ | 250×210mm | 6× 8mm + 3× LM8LUU | Premium donor |
| Tronxy X3 | 220×220mm | 6× 8mm | Budget option |
| Geeetech i3 | 200×200mm | 6× 8mm | Prusa clone |

#### Donors WITHOUT Smooth Rods (V-Slot Rollers)

These donors provide beds, motors, and electronics but **no smooth rods**:

| Donor Printer | Bed Size | Motion System | Notes |
|---------------|----------|---------------|-------|
| Ender 3 / 3 Pro / 3 V2 | 235×235mm | V-slot rollers | Very common |
| Ender 5 | 235×235mm | V-slot rollers | Cube frame |
| CR-10 | 300×300mm | V-slot rollers | Large format |
| Voxelab Aquila | 235×235mm | V-slot rollers | Ender clone |
| Artillery Sidewinder | 300×300mm | V-slot rollers | Large format |

#### Compact Printers

| Donor Printer | Bed Size | Notes |
|---------------|----------|-------|
| Prusa Mini | 180×180mm | Small bed, cantilever design |
| Ender 2 | 150×150mm | Very small |

### Key Insight: 235×235mm is an "Ender Size"

The 235×235mm bed is primarily associated with Creality Ender 3 series printers. However, **Ender 3 uses V-slot rollers, not smooth rods**.

To use a 235×235mm bed in a Dual-8 Neo-Darwin:
- One donor must be Ender 3 (provides bed, motors, board)
- Other donor must be rod-bearing (provides rods, bearings)
- This is a valid but **mixed-donor** configuration

For a **pure rod-donor build** (2× Prusa clones or 2× Anet A8), the 235×235mm bed is not available from scavenging.

## Decision

We adopt **220×220mm** as the reference specification heated bed size.

### Why 220×220mm?

#### 1. Most Common Rod-Donor Bed Size

The Anet A8 was one of the most popular budget 3D printers ever sold, with millions of units. Its 220×220mm bed is:
- Widely available on the secondhand market
- Common in "broken printer" lots
- Standard replacement part (cheap if needed)

#### 2. Aligns with Dual-8 Motion Capability

For 220×220mm build volume with Dual-8 rods:

```
X-rod span = BUILD_X + CARRIAGE_OVERHANG + CLEARANCE
          = 220 + 80 + 30 = 330mm

Deflection analysis (from ADR-021):
- Dual 8mm at 330mm span, 280g toolhead: 0.026mm (GOOD)
- Well within acceptable tolerance
```

220mm build volume is comfortably within Dual-8 capability without pushing limits.

#### 3. Practical Build Volume

220×220mm (48,400 mm²) provides:
- 21% more area than 200×200mm (40,000 mm²)
- Handles most practical prints (phone cases, enclosures, brackets)
- Large enough for meaningful projects
- Not so large that print times become excessive

#### 4. Clean Number

220mm is easier to remember and communicate than 235mm. It's also a metric-friendly dimension.

#### 5. Not Ender-Dependent

Choosing 220×220mm means the reference build doesn't require an Ender 3 donor (which provides no rods). Two Anet A8 donors give you everything needed.

### Why NOT Other Sizes?

#### 200×200mm (Prusa Clone Size)

**Pros:**
- Smallest common size = maximum scavengeability
- Original RepRap heritage
- Most conservative choice

**Cons:**
- 17% less build area than 220mm
- Anet A8 beds are equally common and larger
- Leaves capability on the table

**Verdict:** Supported as minimum, but not reference.

#### 235×235mm (Ender 3 Size)

**Pros:**
- Very common bed size
- Slightly larger build volume

**Cons:**
- Primarily from V-slot printers (no rods)
- Forces mixed-donor builds
- Awkward number (not metric-round)
- Only 7% more area than 220mm

**Verdict:** Supported if Ender donor available, but not reference.

#### 250×210mm (Prusa MK2/MK3 Size)

**Pros:**
- Premium donor quality
- Rectangular allows longer prints in X

**Cons:**
- Prusa MK2/MK3 are less common as scrap
- Rectangular complicates some designs
- Overkill for typical prints

**Verdict:** Supported for those with MK2/MK3 donors.

#### 250×250mm (Original Spec)

**Cons:**
- No standard donor provides this size
- Would require purchasing a bed
- Contradicts scavenger philosophy

**Verdict:** Removed from reference spec.

## Consequences

### Benefits

1. **True scavengeability**: 220×220mm beds available from Anet A8 donors
2. **Aligned with Dual-8**: Well within rod capability at 330mm span
3. **Practical volume**: Large enough for real projects
4. **No mixed donors required**: Two rod-bearing donors provide everything
5. **Common replacement**: If bed damaged, 220×220mm beds are $15-25 AUD

### Trade-offs

1. **Smaller than Ender 3**: 220mm vs 235mm (15mm difference)
2. **Not maximum possible**: Could go larger with purchased bed
3. **May have leftover bed**: If one donor has 250×210mm Prusa bed

### Parametric Support

The build system supports multiple bed sizes via config.py:

```python
# Reference specification
BUILD_VOLUME = {"X": 220, "Y": 220, "Z": 220}

# Alternatives (parametric CAD handles all)
# BUILD_VOLUME = {"X": 200, "Y": 200, "Z": 200}  # Prusa clone minimum
# BUILD_VOLUME = {"X": 235, "Y": 235, "Z": 235}  # Ender 3 size
# BUILD_VOLUME = {"X": 250, "Y": 210, "Z": 210}  # Prusa MK3 rectangular
```

## BOM Implications

### Reference Build: Two Anet A8 Donors

| Component | Source | Size |
|-----------|--------|------|
| Heated bed | Donor (smaller of two) | 220×220mm |
| Bed heater | Donor | 12V or 24V (rewire if needed) |
| Build surface | Donor or purchase | PEI/glass/BuildTak |
| Thermistor | Donor | 100K NTC |

**Cost if bed damaged:** ~$15-25 AUD for replacement 220×220mm MK3 aluminum bed

### Mixed Donor Build (Prusa Clone + Ender 3)

| Component | Source | Size |
|-----------|--------|------|
| Heated bed | Ender 3 donor | 235×235mm |
| Smooth rods | Prusa clone donor | 8mm |
| Build volume | Limited by config | Up to 235×235mm |

This configuration is supported but requires updating config.py to match the larger bed.

## Frame Sizing Update

With 220×220mm build volume, frame dimensions (from ADR-001 formula):

```python
X_OVERHANG = 35.0  # Pitan extruder
SKELETON_X = BUILD_X + (X_OVERHANG * 2) + 40 = 220 + 70 + 40 = 330mm
SKELETON_Y = BUILD_Y + 120 = 220 + 120 = 340mm
SKELETON_Z = BUILD_Z + 50 = 220 + 50 = 270mm
```

This is a more compact frame than the previous 250mm specification, reducing:
- M10 threaded rod usage
- Total frame weight
- Material cost

## Rod Span Analysis

### X-Axis (Critical for Dual-8)

```
X-rod length ≈ BUILD_X + 2×CARRIAGE_OVERHANG + CLEARANCE
            = 220 + 80 + 30 = 330mm

Deflection at 330mm span, dual 8mm, 280g toolhead:
δ = 0.026mm (GOOD - well under 0.035mm threshold)
```

### Y-Axis

```
Y-rod length ≈ BUILD_Y + GANTRY_DEPTH + CLEARANCE
            = 220 + 80 + 30 = 330mm

Load: X-gantry assembly (~1.5kg distributed across 4 rods per side)
Verdict: Well within capacity
```

## Supported Bed Sizes Summary

| Size | Status | Donor Source | Notes |
|------|--------|--------------|-------|
| 200×200mm | Supported | Prusa i3 clones | Minimum size |
| **220×220mm** | **Reference** | **Anet A8** | **Recommended** |
| 235×235mm | Supported | Ender 3 (no rods) | Mixed donor build |
| 250×210mm | Supported | Prusa MK2/MK3 | Rectangular |
| 180×180mm | Supported | Prusa Mini | Compact build |

## Implementation Notes

### Config.py Update

```python
# Reference specification (updated from 250×250×250)
BUILD_VOLUME = {"X": 220, "Y": 220, "Z": 220}
```

### Heated Bed Compatibility

Most 220×220mm beds use:
- **Mounting**: 3-point or 4-point M3 screws, ~209mm spacing
- **Power**: 12V (~120W) or 24V (~200W)
- **Thermistor**: 100K NTC (standard)
- **Connector**: 2-pin or screw terminal

The Spider Bed support (ADR-008) accommodates standard mounting patterns.

### Z-Height Consideration

With 220mm XY build volume, Z-height options:
- **220mm** (cube): Balanced, reference spec
- **250mm**: Taller prints, uses full Z travel
- **200mm**: Shorter frame, faster builds

Reference spec uses 220×220×220mm (cube) for simplicity.

## References

- ADR-021: Dual-Rod Motion System (rod span capability)
- ADR-008: Spider Bed Support System
- ADR-005: Triple-Z Independent Kinematic Leveling
- [Anet A8 Specifications](https://3dprint.wiki/reprap/anet/a8)
- [Ender 3 Bed Size](https://www.creality3dofficial.com)
- [Prusa MK3S+ Specifications](https://www.prusa3d.com)
