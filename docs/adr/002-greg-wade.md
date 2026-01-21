# ADR-002: Greg's Wade Geared Extruder

## Status
**Archived** — Superseded by [ADR-019: Pitan Extruder](019-pitan-extruder.md)

> **Note:** This ADR is preserved for historical reference. The Greg's Wade remains
> a valid "Heritage Option" for PLA/PETG-only builds, but the Pitan is now the
> Reference Specification. See ADR-019 for the current extruder decision.

## Context
The extruder is the "heart" of a 3D printer, responsible for pushing filament through the hotend. In 2026, there are multiple extruder options:
- Direct drive extruders (Voron Clockwork, Sherpa Mini, Orbiter)
- Geared extruders (Greg's Wade, BMG)
- Bowden extruders (Ender 3 stock)

Modern "racecar" printers prioritize lightweight direct drive for high acceleration and short retraction distances. However, these often require proprietary gear kits, expensive components, and can lack the torque for challenging filaments.

The Neo-Darwin's philosophy is "Tractor Torque" over "Racecar Speed."

## Decision
We choose **Greg's Wade Geared Extruder** (5.22:1 gear ratio) as the reference extruder.

### Why Greg's Wade?
1. **Zero Proprietary Hardware**: Built with standard M8 bolts, 608 "skate" bearings, and NEMA17 motor
2. **Extreme Torque**: 5.22:1 reduction provides "Tractor" grip that doesn't skip
3. **Total Repairability**: All parts are 3D-printable or hardware-store available
4. **Self-Replicating**: The machine can print its own replacement gears
5. **Battle-Tested**: 10+ years of community proven reliability
6. **ERCf Compatible**: High torque essential for reverse Bowden color swaps
7. **Flexible Filament Hero**: Geared reduction handles TPU, PETG-CF, and flexibles easily

### Selected Build
- **Source**: [Greg's Wade Rework (Thingiverse 961630)](https://www.thingiverse.com/thing:961630)
- **Gear Ratio**: 13:43 (5.22:1)
- **Genealogy**: [Archeology of Greg's Wade](https://reprap.org/wiki/Genealogy_/_Archeology_of_the_Greg's_Wade's_Geared_Extruder)

## Consequences

### Benefits
- **Indestructible torque**: Brute forces through filament jams
- **Universal sourcing**: Every part available at hardware store
- **Cost-effective**: Under $10 in non-printed parts
- **Multi-color reliability**: Essential for ERCF reverse Bowden pulling
- **High-torque baseline**: More consistent extrusion than budget direct drives

### Trade-offs
- **Mass**: Significantly heavier (~300g) than modern extruders
- **Inertia**: Limits max acceleration (contributes to 70-120mm/s limit)
- **Not compact**: Takes significant space on X-carriage
- **Manual hobbed bolt**: Requires grinding or buying hobbed bolt
- **Z-probe integration**: Requires mounting for BLTouch/PINDA sensor

### Direct Drive Clarification
**Greg's Wade IS direct drive** - the extruder is mounted directly to the hotend on the X-carriage, not a Bowden setup. This provides:
- Instant extrusion response
- Flexible filament capability (TPU, PETG-CF)
- Retraction precision for multi-color (ERCF)
- No long Bowden tube path

For multi-color (ERCF), the filament path is: **ERCF → Reverse Bowden → Direct Drive Wade → Hotend**

### "Neo" Flexibility
The Neo-Darwin uses a **Modular Toolhead Puck** - the Wade is our baseline, but the carriage is compatible with:
- Voron StealthBurner (for speed tinkerers)
- Sherpa Mini (for lightweight upgrades)
- Orbiter 1.5 (for precision direct drive)

## BOM Implications (Generic)

### Scenario A: Buying New (Recommended for Tier 3+)
- **Parts needed**:
  - M8 hobbed bolt (Hobb-Goblin or DIY ground)
  - 4x 608 skate bearings
  - 1x NEMA17 motor (new or salvaged)
  - M8 nuts, washers, bolts
  - 3D-printed Wade parts (from build123d)
  - **Z-probe**: BLTouch v3.1 (~$25 AUD) or PINDA v2 (~$15 AUD)
  - **Z-probe mount**: 3D-printed (included with Wade carriage)
- **Cost implication**: Low (~$35-50 AUD for hardware + probe)
- **Donor compatibility**: All donors (uses standard motor)
- **Complexity**: Low (simple assembly + probe wiring)

### Scenario B: Salvaging from Donor
- **Parts A: Donor has Wade-style extruder** (Prusa i3, Anet A8)
  - Parts needed: Salvage hobbed bolt, bearings, motor
  - **Z-probe**: Buy BLTouch/PINDA (~$15-25 AUD)
  - Cost implication: Very Low ($15-30 AUD total)
  - Donor compatibility: Prusa i3 clones, Anet A8, Prusa MK2
  - Note: Verify gear ratio matches 13:43

- **Parts B: Donor has direct drive extruder** (Ender 3, CR-10)
  - Parts needed: Buy M8 hobbed bolt, 608 bearings
  - Salvage: NEMA17 motor (reuse donor extruder motor)
  - **Z-probe**: Buy BLTouch/PINDA (~$15-25 AUD)
  - **Salvage**: BLTouch/PINDA if donor has it
  - Cost implication: Low (~$23-37 AUD)
  - Donor compatibility: Ender 3, CR-10, V-Core
  - Note: Donor BLTouch may be compatible (Prusa pinout different)

### Scenario C: Salvaging from Non-Printer Sources
- **Parts needed**:
  - M8 bolts from hardware store (grind hobbing yourself)
  - 608 bearings from skateboards/laser printers
  - NEMA17 motor from any CNC/electronics equipment
- **Cost implication**: Very Low (~$5-10 AUD)
- **Donor compatibility**: Any equipment with NEMA17 motors
- **Complexity**: Medium (requires grinding hobbed bolt)
- **Skill required**: Basic metalwork (or buy pre-hobbed)

### Scenario D: Commercial Upgrade Path
- **Parts needed**:
  - BMG or similar geared extruder kit
  - 3D-printed adapter puck
- **Cost implication**: Medium (~$40-60 AUD)
- **Donor compatibility**: All donors
- **Note**: Commercial extruders often use proprietary parts, violates "hardware store" ethos

## Implementation Notes

### Hobbed Bolt Options
1. **Buy pre-hobbed** (Hobb-Goblin): ~$5-8 AUD
2. **Grind your own**: Use M8 bolt + angle grinder + jig
3. **Salvage**: From donor if available

### Motor Requirements
- **Standard NEMA17**: 42mm body height (NEMA17-42 or similar)
- **Current**: 1.5-2.0A
- **Torque**: Higher is better for geared extruder
- **Shaft**: 5mm D-shaft

### Gear Assembly
- **Pinion gear**: 9-tooth (motor shaft)
- **Drive gear**: 47-tooth (hobbed bolt)
- **Ratio**: 13:43 (5.22:1)
- **Lubrication**: Light lithium grease on gear teeth

### Extruder Puck Integration
- The Wade mounts to a standardized "Extruder Puck"
- Puck provides interface to X-carriage
- Allows future toolhead swaps without redesign

### Calibration
```
# Steps/mm calculation
Motor steps/rev = 200 (standard NEMA17)
Gear reduction = 5.22:1
Driver microsteps = 16 (TMC2209)
Bolt diameter = 8mm

Extruder steps/mm = 200 * 16 / (5.22 * 8 * 3.14159)
                ≈ 246.4 steps/mm
```

## References
- MANIFESTO.md: Section "Extruder Archaeology"
- [Greg's Wade Rework](https://www.thingiverse.com/thing:961630)
- [Hobb-Goblin Hobbed Bolt](https://www.thingiverse.com/thing:1058422)
- [Genealogy of Greg's Wade](https://reprap.org/wiki/Genealogy_/_Archeology_of_the_Greg's_Wade's_Geared_Extruder)
- docs/AI-Conversations/ [Relevant conversations about extruder selection]
