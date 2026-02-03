# ADR-027: Build Plate Surface Selection

## Status
Accepted

## Context

Amalgam's scavenger philosophy means most builds will use whatever heated bed and build surface came with the donor printers. However, donors may arrive with damaged, missing, or unsuitable build surfaces, and builders need guidance on replacement options.

### Target Filaments

With the E3D V6 hotend (ADR-004), Amalgam supports a practical range of filaments:

| Filament | Bed Temp | Hotend Temp | Notes |
|----------|----------|-------------|-------|
| **PLA** | 50-60°C | 190-220°C | Primary material, easiest |
| **PETG** | 70-85°C | 230-250°C | Excellent strength, common |
| **TPU** | 40-60°C | 220-240°C | Flexible, slow printing |
| **ABS** | 90-110°C | 230-260°C | Possible with V6, benefits from enclosure |

Most donor beds handle PLA, PETG, and TPU without issue. ABS is achievable but pushes bed temperatures higher and benefits from an enclosure (not part of the reference spec).

### Donor Build Surfaces

Common surfaces on donor printers:

| Surface Type | Common On | PLA | PETG | TPU | ABS | Notes |
|--------------|-----------|-----|------|-----|-----|-------|
| Glass (plain) | Anet A8, many clones | OK | OK | OK | OK | Needs glue stick or hairspray |
| Glass + coating | Ender 3 (Creality glass) | Good | Good | OK | OK | Textured side works well |
| BuildTak/sticker | Various budget printers | Good | Fair | Good | Fair | Wears out, replacement ~$10 |
| Magnetic PEI | Prusa MK3, Ender 3 V2+ | Excellent | Excellent | Good | Good | Premium option |
| Bare aluminum | Some budget donors | Poor | Poor | Poor | Poor | Needs surface applied |

### The Replacement Problem

When a replacement surface is needed, builders face choices:
- **Flex sheets (PEI on spring steel)**: Excellent but $30-60 AUD
- **Glass**: Cheap but adhesion can be finicky
- **G10/FR4**: Industrial workhorse, affordable, predictable
- **BuildTak/sticker sheets**: Consumable, need periodic replacement

For a scavenger build targeting low cost and minimal fuss, the replacement surface should be:
1. Cheap (under $25 AUD)
2. Durable (not a consumable)
3. Works with PLA, PETG, and ABS without adhesives
4. Requires no special handling or maintenance

## Decision

**Primary recommendation: Use the donor's original build surface** if functional.

**If replacement is needed: FR4/G10 (Garolite)** is the recommended low-maintenance option.

### G10/FR4 Thickness by Bed Size

| Bed Size | G10 Thickness | Rationale |
|----------|---------------|-----------|
| Up to 200×200mm | 1.5mm | Sufficient rigidity for small span |
| ~235×235mm | 2mm | Standard for Ender-class beds |
| 300×300mm+ | 3mm | Prevents flex during part removal and thermal bow |

The scaling principle: thickness increases with span to maintain rigidity during part removal and resist thermal bow over repeated heating cycles. G10 is stiff but not steel—at 300×300mm with edge mounting, 2mm would have enough flex to be annoying.

### G10 Preparation and Use

1. **Surface prep**: Scuff with 400 grit sandpaper before first use
2. **Adhesion**: PLA, PETG, and ABS stick directly without glue or tape
3. **Removal**: Wait for bed to cool—parts release cleanly at room temperature
4. **Maintenance**: Occasional wipe with isopropyl alcohol (IPA)

### Temperature Compensation for Thick G10

At 300×300mm with 3mm G10, expect to increase bed temperature 5-10°C above normal settings. The thicker material acts as a thermal insulator. This isn't a problem, just something to calibrate for rather than wonder why first layers aren't sticking.

A Klipper `BED_MESH_CALIBRATE` after installing any new surface is assumed anyway.

## Alternatives Considered

### Flexible PEI Sheets (Spring Steel + Magnetic Base)

**Pros:**
- Excellent adhesion for all filaments
- Easy part removal—flex the sheet
- Premium user experience

**Cons:**
- $30-60 AUD for quality sheets
- Magnetic base adds thermal resistance (~5°C higher bed temps needed)
- Magnets can degrade above 80°C (some cheap magnetic sheets lose strength with repeated ABS temps)
- If donor already has magnetic base: may be worth keeping
- If donor lacks magnetic base: adding one is an upgrade, not scavenger-philosophy

**Verdict:** Keep if donor has one. Don't purchase for a scavenger build unless budget allows.

### Adding Magnetic Base to Non-Magnetic Donor

If considering this upgrade:
- Magnetic adhesive sheets ~$15-20 AUD
- Flex plate ~$20-40 AUD
- Total: $35-60 AUD (exceeds G10 cost significantly)
- Adds 1-2mm height to bed stack (adjust Z endstop)
- May require higher bed temperatures

Not recommended for budget builds, but valid upgrade path.

### Removing Existing Magnetic Surface

Some donors arrive with worn or damaged magnetic surfaces. Options:
1. **Leave it**: If still flat, just add new flex plate on top
2. **Remove it**: Heat bed to 60°C, peel slowly, clean residue with IPA or Goo Gone
3. **Replace with G10**: After removal, G10 can clip or tape directly to aluminum bed

Removal is tedious but not difficult. The adhesive softens with heat.

### Plain Glass

**Pros:**
- Cheap (~$10 for cut borosilicate)
- Perfectly flat
- Easy to clean

**Cons:**
- Requires adhesion aids (glue stick, hairspray) for most filaments
- Parts can bond too well if bed cools with print attached
- Risk of glass cracking from thermal shock (rare with borosilicate)

**Verdict:** Viable budget option, but G10 is similar cost with better adhesion.

### BuildTak / Adhesive Sticker Surfaces

**Pros:**
- Good adhesion when new
- Cheap per sheet (~$10)

**Cons:**
- Consumable—wears out after 50-200 prints
- Ongoing cost over time
- PETG can bond too aggressively and damage surface

**Verdict:** Not recommended for Amalgam. G10 is permanent.

### Bare Aluminum

**Cons:**
- Poor adhesion for all filaments
- Scratches easily from nozzle contact
- Requires some surface treatment

**Verdict:** Add a surface. Don't print directly on aluminum.

## Consequences

### Benefits

1. **Zero cost for most builds**: Donor surfaces usually work fine
2. **Cheap replacement**: G10 sheets $10-20 AUD depending on size
3. **Set and forget**: G10 requires no consumables or maintenance
4. **Wide compatibility**: Works with PLA, PETG, TPU, and ABS
5. **Predictable**: Same behavior print after print

### Trade-offs

1. **Patience required**: G10 needs full cooling for easy release (no flex-and-pop)
2. **Not as "premium"**: Flex sheets offer better UX for frequent printing
3. **Appearance**: G10 is industrial green/tan, not aesthetic priority

### Philosophy Alignment

G10 fits the Amalgam "Tractor" philosophy:
- Industrial material, not boutique
- Durable over disposable
- Practical over premium
- Works reliably, no fuss

## BOM Implications

### Scenario A: Donor Surface Functional

- Parts needed: None
- Cost: $0
- Action: Use as-is, calibrate mesh

### Scenario B: G10 Replacement

| Bed Size | G10 Spec | Approximate Cost |
|----------|----------|------------------|
| 200×200mm | 1.5mm thick | $10-12 AUD |
| 220×220mm | 2mm thick | $12-15 AUD |
| 235×235mm | 2mm thick | $12-15 AUD |
| 300×300mm | 3mm thick | $18-25 AUD |

- Source: Industrial suppliers, eBay, AliExpress
- Also called: Garolite, fiberglass sheet, FR4

### Scenario C: Flex Sheet Upgrade (Optional)

- Magnetic base: $15-20 AUD
- PEI spring steel sheet: $20-40 AUD
- Total: $35-60 AUD
- Recommended only if budget allows or donor already has magnetic base

## Installation Notes

### G10 Mounting

G10 can be secured to the heated bed aluminum with:
- **Binder clips**: Simple, adjustable, removable (recommended)
- **Thermal tape**: More permanent, good thermal transfer
- **Corner brackets**: Printed, reusable

Binder clips at corners are the scavenger-friendly choice. They allow easy removal for cleaning or switching surfaces.

### Bed Leveling After Surface Change

Any surface change requires re-leveling:
1. Run `Z_TILT_ADJUST` (Triple-Z) for mechanical tramming
2. Run `BED_MESH_CALIBRATE` for surface mapping
3. Adjust Z offset if surface thickness changed significantly

## References

- ADR-004: E3D V6 Hotend (enables ABS temperatures)
- ADR-024: Heated Bed Size Selection
- ADR-005: Triple-Z Kinematic Leveling
- [G10/FR4 Material Properties](https://www.mcmaster.com/garolite/)
- [Prusa Knowledge Base: Print Surface Preparation](https://help.prusa3d.com/article/first-layer-issues_1803)
