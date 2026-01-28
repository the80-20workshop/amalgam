# ADR-026: Donor Fitness & Frame Constraints

## Status
Accepted

## Context

### The Scavenger Reality Revisited

ADR-025 established three frame paths (Darwin, S-Core, V-Core) to maximize donor compatibility. However, not all donors are equally suitable, even within a frame path.

The constraint is **not** the frame type (M10 threaded rod vs. extrusion), but rather two physical dimensions that affect system stability:

1. **Bed size** — determines frame footprint and lateral vibration damping
2. **Z height** — affects resonant frequency and leveling stability

### Why These Matter

**Bed Size Issue:**
- Larger beds require larger frame members or heavier damping
- At the design limit (220×220mm reference), MDF base provides adequate mass damping
- Beyond ~300×300mm, the frame-to-mass ratio degrades; print quality suffers from nozzle compliance

**Z-Height Issue:**
- Tall unsupported gantries have lower resonant frequencies
- At printing speeds >120mm/s, high nozzle deflection compounds acceleration errors
- Bed leveling (Triple-Z) becomes less effective if gantry sag increases during acceleration

### Real-World Examples

**CR-10 (300×300mm, 400mm Z):**
- Supported path: V-Core (extrusions give lateral stiffness)
- Issue: Taller than reference, larger bed = heavier MDF required
- Mitigation: Swap heatbed for 220×220 (cost: $20-35) OR add 20mm thicker MDF

**Tevo Spider (300×300mm, 500mm Z):**
- Unsupported deviation
- Issue: Very tall + very wide = requires custom extrusion cuts + massive MDF base
- Recommendation: Sell donor, buy matching pair (e.g., 2× Ender 3), or downsize bed

### The Physics

Using simplified model (underdamped oscillator on MDF):

**Fundamental frequency of unsupported gantry:**
```
f ≈ (1/2π) × √(k / m)  [Hertz]

where:
  k = frame bending stiffness (N/m)
  m = gantry mass (kg)
```

For our system:
- **M10 frame:** k ≈ 50-100 N/μm (low stiffness, MDF compensates)
- **Extrusion frame:** k ≈ 200-400 N/μm (stiffer, less MDF needed)
- **MDF damping:** Raises effective m by ~40-60% (inertial coupling)

**Resonance at print speeds:**
- 120mm/s = 2mm/min = 0.033Hz sweep
- If f_natural < 20Hz and damping ζ < 0.3, ringing becomes visible
- Klipper Input Shaping compensates, but foundation matters

**Z-axis stability:**
- Triple-Z leveling assumes <2mm gantry sag across 220mm width
- Tall gantries at high accel: 1-2mm sag is typical
- Larger Z-drop distances amplify bed tilt errors (3mm sag over 400mm Z = 0.43° tilt per motor)

## Decision

We establish **fitness tiers** based on bed size and Z-height:

### Tier 1: Recommended (Full Support)

**Bed:** 200–235mm square
**Z travel:** <280mm
**Donors:** Anet A8, Wanhao i3, Prusa clones, Ender 3, Voxelab Aquila

**Requirements:**
- Standard 30–40mm MDF base
- No modifications to frame or bed
- All frame paths (Darwin, S-Core, V-Core) supported
- Print quality guaranteed with Klipper tuning

**Examples:**
- 2× Anet A8: 220×220 bed, 240mm Z → ✅ Perfect
- 2× Ender 3: 235×235 bed, 250mm Z → ✅ Excellent
- Anet A8 + Ender 3: Mixed bed sizes (use 220 as reference) → ✅ Supported

### Tier 2: Supported with Notes (Conditional Support)

**Bed:** 235–300mm square
**Z travel:** 280–400mm
**Donors:** CR-10, CR-10 V2, Artillery Sidewinder (larger models)

**Requirements:**
- Choose ONE mitigation:
  - **Option A (Recommended):** Swap heatbed to 220×220 ($20–35)
  - **Option B:** Use 50mm MDF base instead of standard 30–40mm (~$10 extra, heavier)
  - **Option C:** Reduce Z-travel height if gantry permits (unsupported deviation)

**Notes:**
- Extrusion-based frames (V-Core) strongly preferred due to higher stiffness
- Test with Klipper ADXL345 resonance measurement before full build
- Expect slightly lower max acceleration (80–100mm/s² vs. 120mm/s² for Tier 1)

**Example:**
- 2× CR-10: 300×300 bed, 400mm Z
  - V-Core path recommended
  - Suggested: Swap bed to 220×220 (cost: $25) → Frame: 220×220mm, MDF base stabilizes
  - OR: Heavier MDF (40–50mm) → ~$10 extra material

### Tier 3: Unsupported Deviation (Not Recommended)

**Bed:** >300mm or Z >400mm
**Donors:** Tevo Spider (500×500mm), old tall Tronxy models, Anet A2 (large)

**Recommendation:**
- **Do not attempt as Amalgam**
- Instead:
  1. Sell mismatched donor on Marketplace
  2. Buy a matching pair of Tier 1 donors
  3. Or: Just add Klipper to single large printer (not Amalgam project)

**Why not supported:**
- Custom extrusion cuts required → beyond scavenger scope
- MDF mass damping insufficient at these scales
- Z-leveling becomes unreliable (sag error >2mm)
- Engineering effort > cost of re-selling and buying Tier 1 donors

## Consequences

### Benefits

1. **Clear guidance** — users know if their donors fit before investing time
2. **Honest engineering** — we don't hide stability tradeoffs
3. **Cost transparency** — Tier 2 buyers know the $20–35 heatbed swap cost upfront
4. **Scavenger protection** — fewer failure stories from oversized donors
5. **Quality assurance** — all Tier 1 builds achieve target print quality

### Trade-offs

1. **Narrows donor pool slightly** — large industrial printers excluded
2. **May frustrate some users** — "But my CR-10 should work!" discussions
3. **Requires communication** — donor guide must be clear and prominent

## Bed Size Mapping to Frame Size

| Heatbed Size | Frame Size (Ref) | Extrusion Length | MDF Footprint | Tier |
|--------------|------------------|------------------|---------------|------|
| 200×200mm | 200×200mm | 220–240mm | 260×260mm | 1 |
| 220×220mm | 220×220mm | 240–260mm | 280×280mm | 1 (reference) |
| 235×235mm | 235×235mm | 260–280mm | 300×300mm | 1–2 boundary |
| 250×250mm | 250×250mm | 280–300mm | 320×320mm | 2 |
| 300×300mm | 300×300mm | 340–360mm | 380×380mm | 2–3 boundary |

**Notes:**
- Reference spec: 220×220mm bed on 280×280mm MDF base
- Bed "overhang" (bed beyond extrusion) should not exceed 20mm per side
- Larger frames require proportionally thicker MDF for equivalent damping

## Z-Height & Gantry Sag

| Z Travel | Typical Donors | Gantry Sag @ 5G accel | Leveling Impact | Tier |
|----------|----------------|----------------------|-----------------|------|
| <280mm | Ender 3, Anet A8 | <1mm | Negligible | 1 |
| 280–350mm | Most CR-10 | 1–1.5mm | Minor tilt <0.2° | 2 |
| 350–400mm | CR-10 large, Artillery | 1.5–2mm | Noticeable <0.3° | 2 (boundary) |
| >400mm | Tall Tronxy, custom | >2mm | >0.4° tilt | 3 |

**Assumption:** Dual 8mm smooth rods, standard extrusion frame. Stiffer frames (2040 extrusion) perform better at higher Z.

## Implementation Notes

### Config Parameters

```python
# Donor fitness detection
HEATBED_SIZE = 220  # mm (user input: 200-300)
Z_TRAVEL_MAX = 250  # mm (user input)

# Auto-tier assignment
def get_donor_tier(bed_size, z_travel):
    if bed_size <= 235 and z_travel < 280:
        return "TIER_1"
    elif bed_size <= 300 and z_travel < 400:
        return "TIER_2"
    else:
        return "TIER_3_UNSUPPORTED"

# MDF thickness recommendation
def mdf_thickness_mm(tier, bed_size):
    if tier == "TIER_1":
        return 40  # Standard
    elif tier == "TIER_2":
        if bed_size > 280:
            return 50  # Heavier damping
        else:
            return 40  # Standard OK
    else:
        return None  # Not supported
```

### Wizard Flow

1. **"What is your largest heatbed?"** → (200, 220, 235, 250, 300+)
2. **"What is your maximum Z-travel?"** → (auto-measure or guess from printer model)
3. **"Tier assignment & recommendations"** → Display fitness level + mitigation options

### Documentation Structure

```
docs/reference/
├── donor-printer-guide.md          # Enhanced with bed/Z columns
├── fitness-tiers.md                # Deep dive on Tier 1/2/3 physics
└── bed-swap-guide.md               # How to safely swap heatbeds (Tier 2 mitigation)
```

## Tier 2 Mitigations: Heatbed Swap

Common bed swap options for users with larger donors:

| Original Bed | Replacement | Cost (AUD) | Notes |
|--------------|-------------|-----------|-------|
| CR-10 300×300 | MK3 Dual Power 220×220 | $25–35 | Common, reliable |
| Artillery 300×300 | Prusa MK52 250×210 | $30–40 | Magnetic, expensive |
| Ender 5 (large) | Standard 220×220 | $20–30 | Generic, works |
| Anycubic (300×300) | Ultrabase 220×220 | $25–35 | Good quality |

**Process:** Remove original bed (2–4 bolts), wire heating element to relay or direct PSU, tap M3 holes on new frame for mounting.

## Quality Targets

All Tier 1 donors should achieve:
- **Layer height:** 0.1–0.2mm (20–30 micron precision)
- **Surface finish:** <0.2mm peak-to-peak vibration ringing
- **Speed tolerance:** Stable 70–120mm/s (Klipper tuning)
- **Bed leveling:** <0.05mm variance across 220mm (Triple-Z)

Tier 2 with mitigations (heatbed swap or heavier MDF) should achieve similar targets.

## References

- ADR-025: Multi-Frame Architecture
- ADR-023: Z-Drop Architecture
- ADR-005: Triple-Z Kinematic Leveling
- PHILOSOPHY.md: Scavenger mindset
- docs/reference/donor-printer-guide.md: Per-printer details
- [Modal analysis of gantry systems](https://en.wikipedia.org/wiki/Resonance_(physics)): Background physics
