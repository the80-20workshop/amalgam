# ADR-028: Target Filament Selection

## Status
Accepted

## Context

Amalgam is a scavenger-friendly printer built from donor parts. The choice of target filaments affects every hardware decision—hotend, extruder, bed temperature capability, and whether exotic upgrades like enclosures or hardened nozzles are needed.

The project follows an 80/20 philosophy: optimize for the filaments that cover 80-90% of real-world use cases, rather than chasing edge cases that require expensive upgrades.

### What Donors Provide

Most donor printers (Anet A8, Ender 3, Prusa clones, i3 Mega) shipped with:
- **Hotends**: PTFE-lined, max ~240°C safely
- **Beds**: 12V or 24V, capable of 60-100°C
- **Extruders**: Basic single-drive, often with brass drive gears
- **Nozzles**: Brass, 0.4mm

This hardware handles PLA and PETG reliably. TPU is possible with care. ABS pushes bed temperatures and benefits from enclosures most donors lack.

### The E3D V6 Upgrade (ADR-004)

Amalgam specifies the E3D V6 all-metal hotend, which:
- Handles temperatures up to 285°C safely
- Eliminates PTFE degradation concerns
- Opens the door to ABS, ASA, and some exotics

However, having capability doesn't mean we should optimize for it.

### The Pitan Extruder (ADR-019)

The Pitan extruder provides:
- 3:1 gear reduction for consistent extrusion
- Single-drive simplicity (scavenged NEMA17)
- Adequate grip for flexible filaments at moderate speeds

This handles PLA, PETG, and TPU well. Highly flexible TPU (Shore 85A and below) may require slower speeds.

## Decision

Amalgam's **target filaments** are:

| Filament | Priority | Bed Temp | Hotend Temp | Notes |
|----------|----------|----------|-------------|-------|
| **PLA** | Primary | 50-60°C | 190-220°C | Default material, widest compatibility |
| **PETG** | Primary | 70-85°C | 230-250°C | Structural parts, outdoor use |
| **TPU** | Primary | 40-60°C | 220-240°C | Flexible parts, grips, bumpers |

These three filaments are the **reference specification**. Amalgam is optimized for them.

### Why These Three?

#### 1. They Cover 80-90% of Use Cases

| Use Case | Best Filament | Why |
|----------|---------------|-----|
| Prototypes, models, enclosures | PLA | Cheap, easy, looks good |
| Functional parts, brackets, housings | PETG | Strong, heat-resistant, layer adhesion |
| Outdoor parts, UV exposure | PETG | Better UV resistance than PLA |
| Phone cases, grips, bumpers | TPU | Flexible, impact-absorbing |
| Gaskets, seals, vibration dampening | TPU | Compressible, durable |
| Printer parts (non-heated) | PETG | Survives ambient chamber temps |

The vast majority of home 3D printing falls into these categories.

#### 2. Donor Hardware Handles Them

- **Beds**: 60-85°C is well within donor bed capability
- **Hotends**: 190-250°C is safe even for PTFE-lined donors (though we use V6)
- **Extruders**: Single-drive handles all three; TPU just needs slower speed
- **Nozzles**: Brass works fine; no hardened nozzle needed

No exotic upgrades required. Donors provide what's needed.

#### 3. No Enclosure Required

PLA, PETG, and TPU print reliably in open air:
- No warping concerns (unlike ABS)
- No toxic fume concerns at normal temps
- No heated chamber needed

This keeps build complexity low and avoids the cost/effort of enclosure construction.

#### 4. Widely Available and Cheap

| Filament | Typical Price (AUD/kg) | Availability |
|----------|------------------------|--------------|
| PLA | $18-30 | Everywhere |
| PETG | $22-35 | Everywhere |
| TPU | $30-50 | Common |

No specialty suppliers needed. Hardware stores, office supply chains, and online retailers all stock these.

### Filaments That Work But Aren't Optimized For

| Filament | Bed Temp | Hotend Temp | Challenges |
|----------|----------|-------------|------------|
| **ABS** | 90-110°C | 230-260°C | Warping without enclosure, fumes, bed adhesion |
| **ASA** | 90-110°C | 240-260°C | Same as ABS, slightly better UV |
| **Nylon (PA)** | 70-90°C | 250-270°C | Hygroscopic, needs drying, enclosure helps |
| **PC** | 100-120°C | 270-310°C | Very high temps, warping, enclosure required |
| **Carbon-filled** | Varies | Varies | Requires hardened nozzle |

**These are possible but not the target.** Users can experiment, but:
- ABS/ASA: Expect warping without enclosure; use brim, draft shield
- Nylon: Dry filament thoroughly; expect challenges
- PC: Pushes V6 to its limits; enclosure strongly recommended
- Carbon-filled: Will wear brass nozzle; upgrade to hardened steel

The Amalgam spec doesn't prevent these—it just doesn't optimize for them.

### Filaments Explicitly Not Supported

| Filament | Why Not |
|----------|---------|
| **PEEK/ULTEM** | Requires 350°C+ hotend, all-metal construction, heated chamber |
| **Metal/Wood-filled** | Niche, requires hardened nozzle |
| **Highly flexible TPU (<85A)** | May need direct drive or very slow speeds |

These require hardware beyond the scavenger spec.

## Consequences

### Benefits

1. **Maximizes donor reuse**: No exotic upgrades needed for primary filaments
2. **Low barrier to entry**: PLA/PETG/TPU are beginner-friendly
3. **Cost-effective printing**: Cheap, widely available materials
4. **Reliable results**: These filaments are well-understood, documented
5. **No enclosure needed**: Simpler build, lower cost
6. **Safe operation**: No toxic fumes at normal temperatures

### Trade-offs

1. **ABS not optimized**: Users wanting ABS should consider enclosure addition
2. **High-temp materials limited**: PC, Nylon need care and upgrades
3. **Abrasive filaments wear nozzle**: Carbon-fill users should buy hardened nozzles

### What This Means for the Build

| Component | Implication |
|-----------|-------------|
| Hotend (V6) | 285°C max is plenty; no upgrade needed |
| Bed | 60-85°C target; all donors handle this |
| Extruder (Pitan) | Single-drive adequate; no dual-drive needed |
| Nozzle | Brass is fine; hardened optional |
| Enclosure | Not required for reference spec |
| Drying | Nice to have for PETG, not critical |

## BOM Implications

### Reference Build (PLA/PETG/TPU)

No additional parts beyond standard Amalgam spec:
- E3D V6 hotend (or clone) — already specified (ADR-004)
- Pitan extruder — already specified (ADR-019)
- Donor heated bed — already specified (ADR-024)
- Brass 0.4mm nozzle — comes with V6

**Additional cost for filament focus: $0**

### Optional Upgrades for Expanded Materials

| Upgrade | Enables | Cost (AUD) |
|---------|---------|------------|
| Hardened steel nozzle | Carbon-filled, glow-in-dark | $8-15 |
| Enclosure (DIY) | ABS, ASA, Nylon, PC | $30-80 |
| Filament dryer | Nylon, PETG (improved) | $40-80 |
| All-metal heatbreak upgrade | Higher temps (if using clone V6) | $10-20 |

These are user-choice upgrades, not part of reference spec.

## Recommended First Prints

For new Amalgam builds, suggested calibration/test order:

1. **PLA calibration cube** — Verify basic function
2. **PLA Benchy** — Check overhangs, bridging
3. **PETG functional bracket** — Test layer adhesion, strength
4. **TPU phone bumper or grip** — Verify flexible filament handling

Master these before attempting exotics.

## Filament Storage Note

While not strictly part of this ADR, builders should know:
- **PLA**: Tolerates humidity reasonably well
- **PETG**: Benefits from dry storage; slight moisture causes stringing
- **TPU**: Quite tolerant of humidity

A sealed container with desiccant is good practice but not critical for these three filaments.

## References

- ADR-004: E3D V6 Hotend with CHT Nozzle
- ADR-019: Pitan Extruder
- ADR-024: Heated Bed Size Selection
- ADR-027: Build Plate Surface Selection
- [Prusa Material Guide](https://help.prusa3d.com/materials)
- [E3D V6 Specifications](https://e3d-online.com/products/v6-all-metal-hotend)
