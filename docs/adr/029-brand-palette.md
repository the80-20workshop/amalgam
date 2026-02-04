# ADR-029: Brand Palette & Visual Identity

## Status
Accepted

## Context

Every successful open-source printer project has a recognizable visual identity:

| Project | Signature Color | Character |
|---------|----------------|-----------|
| Voron | Red/Black | Aggressive, performance |
| Prusa | Orange | Friendly, approachable |
| Bambu | Green | Modern, consumer |
| RatRig | Blue | Engineering, premium |
| Ender | Blue/Black | Budget, utilitarian |

Amalgam needed a palette that:
1. **Reflects the "Tractor" philosophy** — industrial, heavy, utilitarian
2. **Uses the cheapest available filaments** — no specialty colors
3. **Works with a single filament swap** — no MMU or multi-color hardware
4. **Distinguishes from every competitor** — no red, orange, green, or blue

Grey is the one color no other printer project owns. Cast iron, concrete, industrial machinery — all grey. It's the tractor color.

### The Filament-Swap Logo Problem

Most printer projects either:
- Print in one color (boring, anonymous)
- Require multi-material hardware for branding (expensive, fragile)
- Apply stickers or paint (cheap-looking, peels off)

A raised logo pad (0.5mm above the surface) enables a single filament swap at one layer — pause, swap to white, print 2-3 layers, swap back. No MMU needed. The logo is literally part of the geometry.

### Texture as Identity

Layer lines are the fingerprint of FDM printing. Rather than hiding them (impossible on a scavenger printer), fuzzy skin turns them into a feature — an intentional industrial texture that:
- Hides layer line imperfections (forgiving on a scavenger build)
- Adds grip on assembly surfaces
- Creates a distinctive "cast iron" finish that reinforces the tractor aesthetic

## Decision

### Three-Color Brand Palette

| Role | Color | Hex | Material |
|------|-------|-----|----------|
| **Body** | Dark Grey | `#4A4A4A` | PLA+/PETG filament — all printed parts |
| **Accent** | White | `#FFFFFF` | PLA filament — logo pads (filament swap) |
| **Base** | Near-Black | `#1A1A1A` | Paint (MDF base), anodized aluminum (extrusions) |

**Hardware** (Silver, `#C0C0C0`) is documented for reference but not configurable — bolts, rods, and bearings are whatever color they come in.

### Visual Hierarchy

```
Black base + frame  →  disappears, anchors the build
Grey printed parts  →  focal point, structural, industrial
White logo accents  →  branding detail, high contrast against grey
Silver hardware     →  functional, not decorative
```

### Implementation

All palette values live in `cad/config.py` Section 11 as the single source of truth:

```python
BRAND_BODY_COLOR = "#4A4A4A"
BRAND_ACCENT_COLOR = "#FFFFFF"
BRAND_BASE_COLOR = "#1A1A1A"
```

These propagate to:
- **CAD exports** — glTF and 3MF models render in brand body color
- **Documentation** — Quarto variables via `scripts/export_config.py`
- **Website** — CSS custom properties in `docs/index.html`
- **Brand module** — `amalgam/lib/brand.py` provides build123d `Color` objects

### Logo Pads

Optional raised geometry on printed parts for filament-swap branding:

```python
LOGO_PAD_ENABLED = True      # Set False for plain parts
LOGO_PAD_DIAMETER = 18.0     # mm across flats
LOGO_PAD_HEIGHT = 0.5        # mm raised (2-3 print layers)
```

- When enabled, structural parts get a small Amalgam octagon+A mark
- The pad is just geometry — the color change is a slicer operation (M600 pause)
- Parts are structurally identical with or without pads
- Applied via `amalgam/lib/logo_pad.py`, not baked into structural geometry

### Fuzzy Skin (Texture Recommendation)

Documented but not enforced by geometry — this is slicer configuration:

```python
FUZZY_SKIN_RECOMMENDED = True
FUZZY_SKIN_POINT_DISTANCE = 0.3   # mm
FUZZY_SKIN_THICKNESS = 0.2        # mm
```

Apply to cosmetic outer faces only. Never on mating surfaces, rod channels, or bearing seats.

## Consequences

### Benefits

1. **Zero added cost** — Grey and white are the cheapest filaments available
2. **No special hardware** — Single filament swap, no MMU
3. **Distinctive identity** — Grey + white logo is unique in the 3D printer space
4. **Forgiving finish** — Fuzzy skin hides imperfections on scavenger builds
5. **Fully optional** — `LOGO_PAD_ENABLED = False` for plain parts; any filament color works
6. **Single source of truth** — Palette in config.py feeds all outputs automatically

### Trade-offs

1. **Grey doesn't photograph well** — Dark grey on dark background needs good lighting for glamour shots
2. **Filament swap is manual** — Requires operator attention at the pause layer
3. **Fuzzy skin adds print time** — Marginal (~5-10%) but nonzero
4. **Grey is polarizing** — Some builders will want color; the config allows it but brand docs show grey

### What This Means for Builders

- **Following the brand palette:** Buy dark grey PLA+ and a small amount of white PLA. Paint MDF base matte black. Optionally enable fuzzy skin on cosmetic faces.
- **Ignoring the brand palette:** Set `LOGO_PAD_ENABLED = False`, print in whatever color you like. Parts are structurally identical.
- **Customizing:** Change `BRAND_BODY_COLOR` in config.py. The logo pad and exports will adapt. The palette is a recommendation, not a constraint.

## BOM Implications

### Brand-Compliant Build

| Item | Purpose | Cost (AUD) |
|------|---------|------------|
| Dark grey PLA+ (1kg) | All printed parts | $18-25 |
| White PLA (small amount) | Logo pad color swaps | $0 (leftover scraps work) |
| Matte black spray paint | MDF base | $8-12 |
| 220 grit sandpaper | MDF prep | $3-5 |

**Additional cost for brand compliance: ~$10-15** (paint + sandpaper; filament is needed regardless).

### Plain Build

No additional cost. Print in any color. Skip logo pads. Leave MDF natural or paint any color.

## References

- ADR-028: Target Filament Selection (PLA/PETG/TPU as primary filaments)
- ADR-000: Engineering Philosophy ("Tractor" aesthetic)
- `cad/config.py` Section 11: Brand & Cosmetics configuration
- `cad/amalgam/lib/brand.py`: Palette constants and Color helpers
- `cad/amalgam/lib/logo_pad.py`: Logo pad application library
- `docs/guides/print-settings.qmd`: Print settings and brand guide
