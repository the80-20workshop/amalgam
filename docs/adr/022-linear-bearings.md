# ADR-022: Linear Bearing Selection

## Status
Accepted

## Context

ADR-021 establishes dual 8mm smooth rods as the reference motion system. This ADR addresses what **rides on those rods** - the linear bearings that enable smooth, low-friction motion.

### Bearing Options Available

1. **Ball bearings (LM8UU, LM8LUU)**: Recirculating steel balls in a cage
2. **Polymer bushings (IGUS Drylin)**: Self-lubricating polymer sleeves
3. **Printed bearings**: DIY polymer sleeves with adjustable clamping
4. **Bronze bushings**: Oil-impregnated sintered metal

### Scavenger Context

Two donor Prusa-style printers typically provide:
- 24× LM8UU bearings (12 per printer)
- Neo-Darwin Dual-8 requires 16 bearings
- **Surplus of 8 bearings** available for spares or selection

### Rod Material Requirements

**Critical insight:** Ball bearings and polymer bushings have **different rod material requirements**.

#### Ball Bearings (LM8UU/LM8LUU) Require Hardened Steel

Linear ball bearings use the rod as their inner race. The steel balls "plow" into soft materials, causing rapid wear.

| Rod Material | Typical Hardness | Ball Bearing Life Factor | Notes |
|--------------|------------------|-------------------------|-------|
| Hardened steel (induction) | HRC 60-65 | 1.0 (100%) | **Required for ball bearings** |
| Hardened stainless (440C treated) | HRC 54-60 | 0.7-1.0 | Acceptable |
| Stainless 304/316 (annealed) | HRC 20-25 | **Very poor** | Galling risk - do not use |
| Aluminum | HRC ~15 | **Incompatible** | Will destroy bearings |

**Key finding:** Using HRC 40 shaft with ball bearings gives only **20% of rated life** compared to HRC 60. ([Linear Motion Tips](https://www.linearmotiontips.com/how-does-shaft-hardness-affect-the-life-of-a-linear-ball-bushing/))

**Warning:** Standard 304/316 stainless steel is prone to **galling** (cold welding) with steel ball bearings. The balls create grooves and the rod surface tears. ([Nickel Institute](https://nickelinstitute.org/media/1780/reviewofwearandgallingcharacteristicsofstainlesssteel_9006_.pdf))

#### Polymer Bushings (IGUS Drylin) Work on Multiple Materials

IGUS Drylin bushings use self-lubricating polymer (iglidur J4) that glides rather than rolls. This enables compatibility with softer materials:

| Rod Material | IGUS Compatibility | Notes |
|--------------|-------------------|-------|
| Hardened steel | ✅ Excellent | Works perfectly |
| Stainless steel (any grade) | ✅ Excellent | No galling risk |
| Aluminum | ✅ Good | Lightweight option |
| Carbon fiber | ✅ Good | Premium/experimental |
| Chrome-plated steel | ✅ Excellent | Common scavenged rods |

**Source:** [IGUS Official - Drylin RJ4JP](https://www.igus.com/product/drylin_RJ4JP_01)

#### Can Scratched Rods Be Salvaged?

A common scavenger question: can damaged hardened rods be reused?

| Damage Type | Ball Bearings | IGUS Bushings |
|-------------|---------------|---------------|
| Light scratches | May click/jam on grooves | **Can bridge over** (larger contact area) |
| Deep gouges | Unusable - will damage balls | May work, test carefully |
| Bent rod | Unusable | Unusable |
| Surface rust | Clean and test | Clean and test |

**The IGUS advantage:** Because polymer bushings have a large contact area (vs point contact of balls), they can "bridge" minor surface imperfections that would jam ball bearings.

### The Long Bearing Question

LM8UU vs LM8LUU comparison:

| Spec | LM8UU | LM8LUU |
|------|-------|--------|
| Length | 15mm | 24mm |
| Inner diameter | 8mm | 8mm |
| Outer diameter | 15mm | 15mm |
| Ball rows | 4 | 6 |
| Load capacity | Lower | ~50% higher |
| Moment resistance | Lower | Higher |

Long bearings (LM8LUU) provide better **moment resistance** - they resist tilting and racking forces better than standard length bearings.

## Decision

We recommend **LM8LUU for X-axis** and **LM8UU for Y and Z axes** as the reference specification.

### Bearing Assignment

| Axis | Bearing | Quantity | Rationale |
|------|---------|----------|-----------|
| X (Plough carriage) | **LM8LUU** | 4 | Highest dynamic loads, pitch/yaw resistance critical |
| Y (gantry, per side) | LM8UU | 4 (8 total) | Dual rods provide stability, standard bearings sufficient |
| Z (bed support) | LM8UU | 4 | Slow movement, minimal dynamic loads |
| **Total** | | **16** | |

### Why LM8LUU for X Only?

The X-axis carriage (Plough) experiences the most severe dynamic forces:

1. **Y-acceleration** creates pitch moment (nose-dive)
2. **X-acceleration** creates lateral shift forces
3. **Extruder retraction** creates small Z-moments
4. **Belt tension** creates constant preload

Long bearings on X provide:
- Better pitch resistance during Y-acceleration
- More stable carriage during direction changes
- Reduced "racking" tendency under load

### Why LM8UU is Sufficient for Y and Z?

**Y-axis (gantry):**
- Dual rods per side already provide excellent moment resistance
- Load is distributed across 4 bearings per side
- Lower acceleration than X-axis
- Long bearings would add cost without proportional benefit

**Z-axis:**
- Very slow movement (typically 5-10mm/s)
- Primarily static load (bed weight)
- No significant dynamic moments
- Standard bearings have decades of proven service in this role

### Scavenged Bearing Protocol

Donor printer bearings should be:

1. **Inspected**: Roll on a clean rod section - should be smooth, no grinding
2. **Cleaned**: Flush with isopropyl alcohol, remove old grease and debris
3. **Dried**: Allow to fully dry before regreasing
4. **Regreased**: Light machine oil or lithium grease
5. **Tested**: Should roll smoothly with minimal resistance

**Reject bearings that:**
- Have visible rust or pitting
- Make grinding sounds when rolled
- Have excessive play (wobble on rod)
- Have flat spots or notchy feel

With 24 bearings from 2 donors, you can afford to reject questionable units.

## Consequences

### Benefits

1. **Optimized performance**: Long bearings where they matter most (X)
2. **Cost-effective**: Standard bearings where sufficient (Y, Z)
3. **Fully scavengeable**: All bearings from 2 donor printers
4. **Proven technology**: Ball bearings have decades of RepRap validation
5. **Low maintenance**: Occasional regrease, no adjustment needed

### Trade-offs

1. **LM8LUU may need purchase**: Some donors have only LM8UU
2. **Slightly longer X-carriage**: LM8LUU housings are 9mm longer
3. **Not "pure" scavenger**: May need to buy 4× LM8LUU (~$5-8 AUD)

## Scavenger Decision Tree

Use this flowchart to select your bearing/rod combination:

```
What does your donor printer have?
│
├─► Hardened steel rods + LM8UU bearings (Prusa clone, Anet A8)
│   │
│   └─► Are the rods in good condition?
│       │
│       ├─► YES: Use scavenged rods + bearings (clean & regrease)
│       │       Cost: $0 | Result: Standard "printer hum"
│       │
│       └─► NO (scratched/grooved):
│           │
│           ├─► Option A: Try IGUS bushings on scratched rods
│           │   Cost: ~$30-40 | Bridges minor scratches
│           │
│           └─► Option B: Buy stainless rods + IGUS
│               Cost: ~$70-90 | Silent, maintenance-free
│
├─► V-slot rollers, no rods (Ender 3, CR-10)
│   │
│   └─► Must purchase rods. Choose:
│       │
│       ├─► Hardened steel rods + LM8UU
│       │   Cost: ~$50-70 | Standard ball bearing setup
│       │
│       └─► Stainless steel rods + IGUS (Recommended for V-slot donors)
│           Cost: ~$70-90 | Silent, corrosion-proof
│
└─► Mixed donors (e.g., Ender + Prusa clone)
    │
    └─► Use rods from rod-bearing donor
        Use best bearings available
        Consider IGUS if rods are damaged
```

### Quick Reference: Two Valid Paths

| Path | Rods | Bearings | Cost | Characteristics |
|------|------|----------|------|-----------------|
| **Scavenger (reference)** | Hardened steel (donor) | LM8UU/LM8LUU (donor) | $0-8 | Standard printer sound, proven reliability |
| **Silent/Premium** | Stainless steel (buy) | IGUS Drylin (buy) | ~$70-90 | Silent operation, maintenance-free, corrosion-proof |

Both paths produce quality prints. Choose based on your donor situation and noise preferences.

## Alternative Paths (Documented for Reference)

### Alternative A: All LM8UU (Pure Scavenger)

```
X: 4× LM8UU
Y: 8× LM8UU
Z: 4× LM8UU
Total: 16× LM8UU
```

**Pros:**
- Guaranteed scavengeable from 2 donors
- Zero bearing purchase cost
- Simpler parts list

**Cons:**
- Reduced X-carriage stability
- May see more racking on X during fast Y moves
- Acceptable for quality-focused (not speed-focused) printing

**Verdict:** Acceptable fallback if LM8LUU unavailable.

### Alternative B: IGUS Drylin + Stainless Steel (Silent Build Path)

This alternative is **recommended for V-slot donors** (Ender 3, CR-10) that provide no scavengeable rods or bearings.

**Configuration:**
```
Rods: 8× stainless steel 8mm (420mm length)
Bearings: 16-22× IGUS Drylin RJ4JP-01-08
Cost: ~$70-90 AUD total
```

**Pros:**
- **Silent operation**: No "printer hum" from ball bearings
- **Maintenance-free**: Self-lubricating polymer, no grease needed
- **Corrosion-proof**: Stainless rods + polymer = zero rust risk
- **Tolerant of imperfect rods**: Can bridge minor scratches
- **Works with any stainless grade**: No galling risk (unlike ball bearings)
- **Vibration damping**: Polymer absorbs some mechanical noise

**Cons:**
- **Higher friction**: 2-3× static friction ("stiction") vs ball bearings
- **Higher cost**: ~$70-90 vs $0 for scavenged
- **Not scavengeable**: Must be purchased new
- **Requires housing compliance**: Needs slight clamping pressure to seat
- **Lower speed ceiling**: Not ideal for 300mm/s+ printing

**When to choose this path:**
1. V-slot donor (Ender 3) - no rods to scavenge anyway
2. Silent operation is priority (bedroom/office printer)
3. Scavenged rods are scratched/damaged beyond ball bearing use
4. Humid environment where rust is a concern

**Cost breakdown (AUD):**
| Part | Quantity | Unit Price | Total |
|------|----------|------------|-------|
| 8mm stainless rod 420mm | 8 | ~$5-6 | ~$40-48 |
| IGUS RJ4JP-01-08 | 20 | ~$1.50-2 | ~$30-40 |
| **Total** | | | **~$70-88** |

**Installation notes:**
1. **Chamfer rod ends**: File 45° bevel to avoid slicing IGUS internal ribs
2. **Do NOT lubricate**: IGUS bushings are self-lubricating; grease reduces life
3. **Housing design**: Include compliance gap for slight clamping pressure
4. **Cutting stainless**: Use angle grinder with thin "Inox" cutoff wheel

**Verdict:** Excellent alternative for V-slot donors or silent builds. Not reference spec due to higher friction and cost, but a legitimate "premium" path.

**References:**
- [Tom's 3D IGUS analysis](https://toms3d.org/2016/06/07/should-you-be-using-igus-polymer-bushings/)
- [IGUS Official Drylin RJ4JP](https://www.igus.com/product/drylin_RJ4JP_01)

### Alternative C: Printed Adjustable Bearings

DIY polymer sleeve bearings with split-clamp adjustment:

```
    ┌─────────────┐
    │  ╭───────╮  │  ← Printed PETG sleeve
    │  │  rod  │  │
    │  ╰───────╯  │
    └──────┬──────┘
         screw    ← Adjustable preload
```

**Pros:**
- Zero cost (print them)
- Adjustable preload compensates for wear
- Works with slightly imperfect rods
- Silent operation
- True self-replication (RepRap philosophy)

**Cons:**
- 2-3× higher friction than ball bearings
- Requires careful tuning (too tight = binding, too loose = play)
- Will wear over time
- Needs periodic relubrication (PTFE grease, not oil)
- Unproven at Neo-Darwin's 360mm spans

**Best candidate axis:** Z (slowest, lowest risk)

**Material recommendation:** PETG with PTFE/silicone grease

**Verdict:** Experimental option for Z-axis. Not recommended for X or Y in reference spec.

**Reference:** [RepRap Printed Bearings Wiki](https://github.com/superjamie/lazyweb/wiki/3D-Printing-Linear-Bearings)

### Alternative D: Bronze Bushings

Oil-impregnated sintered bronze sleeves.

**Pros:**
- Very long service life
- Self-lubricating
- High load capacity
- Industrial proven

**Cons:**
- Not scavengeable from printers
- Require precise rod diameter match
- Higher friction than ball bearings
- Heavier than alternatives

**Verdict:** Not aligned with scavenger philosophy.

## BOM Implications

### Reference Build (2 Donors)

**Scavenged:**
| Part | Quantity | Source | Notes |
|------|----------|--------|-------|
| LM8UU | 12 | Donors | For Y (8) + Z (4) |

**Purchased (if needed):**
| Part | Quantity | Cost (AUD) | Notes |
|------|----------|------------|-------|
| LM8LUU | 4 | ~$5-8 | For X-axis carriage |

**Alternative (pure scavenger):**
| Part | Quantity | Source |
|------|----------|--------|
| LM8UU | 16 | Donors (select best 16 of 24) |

### Donor Bearing Yield

| Donor Type | LM8UU | LM8LUU | Rods | Notes |
|------------|-------|--------|------|-------|
| Prusa i3 clone | 11-12 | 0 | 6× 8mm | Standard config |
| Anet A8 | 10-12 | 0 | 6× 8mm | Standard config |
| Prusa MK2/MK3 | 9 | 3 | 6× 8mm | Y-carriage uses LM8LUU |
| Creality Ender 3 | 0 | 0 | **None** | Uses V-slot rollers |
| CR-10 | 0 | 0 | **None** | Uses V-slot rollers |

If one donor is MK2/MK3 style, you may get LM8LUU for free.

### V-Slot Donor Build (Ender 3, CR-10)

If your donor uses V-slot rollers, you must purchase the motion system:

**Option 1: Traditional (Hardened + Ball Bearings)**
| Part | Quantity | Cost (AUD) |
|------|----------|------------|
| 8mm hardened steel rods 400mm | 8 | ~$40-50 |
| LM8UU bearings | 16 | ~$15-20 |
| LM8LUU bearings (X-axis) | 4 | ~$8-10 |
| **Total** | | **~$63-80** |

**Option 2: Silent (Stainless + IGUS) - Recommended**
| Part | Quantity | Cost (AUD) |
|------|----------|------------|
| 8mm stainless steel rods 420mm | 8 | ~$40-48 |
| IGUS RJ4JP-01-08 bushings | 20 | ~$30-40 |
| **Total** | | **~$70-88** |

For V-slot donors, the IGUS path costs only ~$10 more but provides silent operation and zero maintenance.

## Maintenance Protocol

### Initial Setup
1. Clean all bearings with IPA
2. Dry completely
3. Apply light lithium grease or machine oil
4. Install with bearing seated fully in housing

### Ongoing Maintenance
- **Every ~100 print hours**: Wipe rods, check for debris
- **Every ~500 print hours**: Remove bearings, clean, regrease
- **Signs of wear**: Grinding sound, increased resistance, visible play

### Lubrication Options

| Lubricant | Pros | Cons |
|-----------|------|------|
| Lithium grease | Long-lasting, good protection | Can attract dust |
| PTFE/silicone grease | Clean, low friction | Needs more frequent application |
| Light machine oil (3-in-One) | Easy to apply, low friction | Needs frequent reapplication |
| Sewing machine oil | Very light, clean | Minimal protection |

**Reference spec recommendation:** Lithium grease for long service intervals.

## Implementation Notes

### X-Carriage (Plough) Bearing Layout

```
     LM8LUU        LM8LUU
    ┌──────┐      ┌──────┐     ← Top rod
    │      │      │      │
    │ 24mm │      │ 24mm │
    │      │      │      │
    └──────┘      └──────┘
       ├── ~60mm ──┤            ← Bearing spacing for stability

    ┌──────┐      ┌──────┐     ← Bottom rod
    │      │      │      │
    └──────┘      └──────┘
     LM8LUU        LM8LUU
```

4× LM8LUU total, spaced for maximum wheelbase.

### Y-Gantry Bearing Layout (Each Side)

```
    ═══════════════════  ← Top Y rod
         │      │
       LM8UU  LM8UU      ← 2 bearings, spaced apart
         │      │
    ═══════════════════  ← Bottom Y rod
         │      │
       LM8UU  LM8UU
```

4× LM8UU per side (8 total), standard length is sufficient with dual-rod stability.

### Z-Axis Bearing Layout

```
    ┌─LM8UU─┐        ┌─LM8UU─┐
    │       │        │       │
    │  Z    │        │   Z   │
    │  rod  │        │  rod  │
    │       │        │       │
    └─LM8UU─┘        └─LM8UU─┘
```

4× LM8UU total (2 per rod), handles bed weight with large margin.

## Quality Verification

### New Bearing Test
1. Roll on clean rod - should be silent and smooth
2. Check for lateral play - minimal acceptable
3. Verify dimensions with calipers

### Scavenged Bearing Test
1. Visual inspection for rust, pitting, damage
2. Roll test - reject if grinding or notchy
3. Play test - reject if excessive wobble
4. Clean, regrease, retest before installation

## References

### Related ADRs
- ADR-021: Dual-Rod Motion System (rod configuration)
- ADR-024: Heated Bed Size Selection (donor printer analysis)

### Technical Sources
- [Linear Motion Tips: Shaft Hardness and Bearing Life](https://www.linearmotiontips.com/how-does-shaft-hardness-affect-the-life-of-a-linear-ball-bushing/) - HRC requirements for ball bearings
- [Nickel Institute: Galling Characteristics of Stainless Steel](https://nickelinstitute.org/media/1780/reviewofwearandgallingcharacteristicsofstainlesssteel_9006_.pdf) - Why 304/316 galls with ball bearings
- [IGUS Official: Drylin RJ4JP Specifications](https://www.igus.com/product/drylin_RJ4JP_01) - Shaft material compatibility
- [Tom's 3D: IGUS Polymer Bushings](https://toms3d.org/2016/06/07/should-you-be-using-igus-polymer-bushings/) - Real-world friction comparison
- [RepRap Wiki: Printed Linear Bearings](https://github.com/superjamie/lazyweb/wiki/3D-Printing-Linear-Bearings)
- [RepRap Wiki: Lubrication](https://reprap.org/wiki/Lubrication)
- [RepRap Forum: LM8UU vs IGUS](https://reprap.org/forum/read.php?1,221763)
