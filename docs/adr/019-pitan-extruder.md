# ADR-019: Pitan Extruder (Reference Specification)

## Status
Accepted (supersedes ADR-002)

## Context

The extruder choice is critical to Neo-Darwin's philosophy of building a "Tractor with the Brain of a Racecar." After extensive evaluation documented in:

- `docs/decisions/tractor_06_extruder_decision.md` (comprehensive analysis)
- `docs/reference/ai-conversations/pitian-v-orbiter.md`
- `docs/reference/ai-conversations/single-v-dual-drive.md`

We reconsidered the original Greg's Wade decision (ADR-002) and evaluated multiple alternatives.

### Key Insight: Single-Drive Architecture

A critical discovery shaped this decision: **dual-drive extruders introduce gear mesh artifacts** that affect print quality consistency. When two drive gears mesh, microscopic variations in tooth engagement create periodic pressure fluctuations on the filament.

This is one reason Bambu Lab printers—known for print quality—use single-drive designs. For Neo-Darwin's quality-focused philosophy at 80-120mm/s, single-drive advantages outweigh dual-drive TPU benefits.

### Extruders Evaluated

| Extruder | Drive Type | Motor | Cost (AUD) | Weight | Status |
|----------|------------|-------|------------|--------|--------|
| Greg's Wade | Single | NEMA17 | $2-5 | 360-600g | Heritage Option |
| MK8/MK9 | Single | NEMA17 | $0-6 | 150-200g | Ultra-Scavenger |
| Sherpa Mini | Dual | NEMA14 | $22-34 | 110-127g | Not selected (dual-drive) |
| Orbiter v1.5 | Dual | LDO specific | $60-100 | 140-150g | Not selected (cost, dual-drive) |
| LGX Lite | Dual | NEMA14 | $120-150 | 150-165g | Not selected (cost, dual-drive) |
| **Pitan** | **Single** | **NEMA17** | **$4-10** | **260-300g** | **Reference Spec** |

## Decision

We choose the **Pitan Extruder** (Printable Titan) as the Neo-Darwin Reference Specification.

### Why Pitan?

1. **Single-Drive Design**: No gear mesh artifacts—cleaner extrusion consistency
2. **Scavengeable Motor**: Uses standard NEMA17 from any donor printer (Ender 3, Prusa, etc.)
3. **Fully Printable**: Body and gears can be printed—true RepRap spirit
4. **3:1 Gear Ratio**: Adequate torque for PLA, PETG, and careful TPU work
5. **Budget**: $4-10 total vs $20-150 for alternatives
6. **M8 Rod Compatible**: At 260-300g, works with M8 smooth rods at spans up to 280mm
7. **Repairability**: "If a gear breaks, you have a new one before your coffee gets cold"

### Why Not Wade?

The Greg's Wade was our original choice (ADR-002) but has limitations:

- **3.00mm Design**: Originally designed for 3mm filament; 1.75mm adaptation has exposed filament path—TPU will buckle
- **Heavy**: Full NEMA17 variant (450-600g) requires M10 smooth rods or causes excessive sag
- **Pancake Limitation**: Pancake motor reduces weight but also reduces torque headroom

The Wade is preserved as a **Heritage Option** for builders who value pure RepRap roots and only print PLA/PETG.

### Why Not Dual-Drive (Sherpa, Orbiter, BMG)?

- **Gear mesh artifacts**: Two meshing gears create periodic micro-variations in extrusion pressure
- **Specific motors**: Sherpa needs NEMA14 pancake with pinion ($14-21); Orbiter needs LDO motor ($50-75)
- **Not scavengeable**: These motors don't come from donor printers
- **Cost**: $22-150 vs $4-10 for equivalent print quality at our target speeds

## Consequences

### Benefits

- **Print quality parity across tiers**: Scavenger builds achieve the same quality as Reference builds
- **Universal motor sourcing**: Any NEMA17 works—from Ender 3, Prusa clone, CNC, etc.
- **True RepRap**: Print your own replacement parts
- **Budget alignment**: Entire extruder costs less than a Sherpa Mini motor alone
- **M8 compatibility**: Enables scavenged smooth rods at practical spans

### Trade-offs

- **Heavier than Sherpa Mini**: ~280g vs ~120g (but still M8-compatible)
- **TPU requires care**: Single-drive is less aggressive than dual-drive for flexible filaments
- **Less community support**: Smaller community than Voron ecosystem extruders
- **Printed gear wear**: May need reprinting after many hours (but cost is $0.25 in filament)

### Rod Compatibility Analysis

| Configuration | Rod Size | Span | Sag | Verdict |
|---------------|----------|------|-----|---------|
| Pitan + NEMA17 | M8 | 250mm | 0.024mm | Reference spec |
| Pitan + NEMA17 | M8 | 280mm | 0.034mm | Acceptable |
| Pitan + NEMA17 | M10 | 280mm | 0.014mm | Excellent |
| Pitan + Pancake | M8 | 280mm | 0.020mm | Ideal lightweight |

## BOM Implications

### Reference Build (Tier 3)

| Component | Source | Cost (AUD) |
|-----------|--------|------------|
| Pitan printed parts (body + gears) | Print yourself | $0.50-1 |
| Hobbed bolt or MK8 drive gear | AliExpress/hardware | $2-5 |
| NEMA17 motor | Scavenge from donor | $0 |
| 608 bearings (x2) | Hardware store/scavenge | $0-2 |
| M3 hardware + springs | Hardware store | $1-2 |
| PTFE tube + fitting | Hardware store | $1 |
| **Total** | | **$4.50-11** |

### Scavenger Build (Tier 1-2)

Same as above—the Pitan is scavenger-native by design.

## Klipper Configuration

```ini
[extruder]
step_pin: E_STEP
dir_pin: E_DIR
enable_pin: !E_EN
microsteps: 16
rotation_distance: 22.678  # Calibrate for your setup
gear_ratio: 3:1            # Pitan standard
nozzle_diameter: 0.4
filament_diameter: 1.750

[tmc2209 extruder]
uart_pin: E_UART
run_current: 0.5           # Start low, adjust as needed
hold_current: 0.4
stealthchop_threshold: 0

[firmware_retraction]
retract_length: 0.5
retract_speed: 35
unretract_extra_length: 0
unretract_speed: 35
```

## Alternative Configurations

### Heritage Option: Greg's Wade + Pancake NEMA17

For builders who value pure RepRap heritage and only print PLA/PETG:

- Use pancake NEMA17 to keep weight under 410g (M8 compatible)
- 5.22:1 gear ratio provides massive torque headroom
- Not suitable for TPU with 1.75mm filament

### Ultra-Scavenger Option: MK8 Direct Drive

For extreme budget constraints or if you already have one:

- No gear reduction—relies entirely on motor torque
- Lightweight (~150-200g)—excellent for M8 rods
- Klipper pressure advance compensates for 1:1 ratio

### Use What You Have

**This is the most important option.** If you have an extruder in your parts bin—Titan, Hemera, BMG, Sherpa—**use it**. The Neo-Darwin carriage design is adaptable.

The Pitan is the *reference specification*, not a mandate. The single-drive recommendation is about optimal quality for new builds, not a condemnation of existing equipment.

## References

- [ADR-002](002-greg-wade.md): Original Wade decision (now archived)
- `docs/decisions/tractor_06_extruder_decision.md`: Full evaluation document
- `docs/reference/ai-conversations/pitian-v-orbiter.md`: Pitan vs Orbiter analysis
- `docs/reference/ai-conversations/single-v-dual-drive.md`: Drive architecture discussion
- Pitan designs: Community versions on Printables/Thingiverse (Printable Titan clone)
- E3D Titan: Original design the Pitan is based on

---

*"A tractor doesn't win races. It pulls loads reliably. The Pitan doesn't chase 300mm/s. It produces quality prints consistently, inexpensively, and repairably."*
