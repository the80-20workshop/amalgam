# ADR-000: Amalgam Engineering Philosophy (20 Years of RepRap Wisdom)

## Status
Accepted

## Context
The Amalgam project stands on the shoulders of two decades of RepRap development (2007-2027). Over this period, the 3D printing community has evolved from experimental open-source innovation to mature engineering practices. This accumulated wisdom has settled on specific engineering truths that balance physical mass, software intelligence, and environmental control.

Many modern printers chase extreme specifications (600mm/s, linear rails, carbon fiber) at the expense of accessibility, cost, and reliability. The Amalgam aims to distill 20 years of community knowledge into a cohesive engineering philosophy that delivers industrial-quality printing on a hobbyist budget.

## Decision
We adopt the **"Rigid Base, Agile Head"** philosophy, codified as the **Amalgam Engineering Principles**:

### Core Pillars

1. **Mass is a Filter**: A heavy, rigid frame dampens high-frequency vibrations and provides structural authority
2. **Software is the Great Equalizer**: Klipper features (Input Shaping, Pressure Advance) compensate for hardware limitations
3. **Gearing is Sovereignty**: Geared direct drive (Wade/BMG) provides superior extrusion reliability
4. **The "Good Enough" Zenith**: Performance that exceeds requirements without chasing diminishing returns

### The Amalgam Square
We balance four constraints, not three:

| Corner | Amalgam Position | Trade-off |
|--------|---------------------|-----------|
| **Cost** | <$300 AUD | We sacrifice **Convenience**—more Effort, less money |
| **Speed** | 70-120mm/s | We "settle" for adequate speed—perfect quality > high-speed failures |
| **Quality** | Industrial-grade | Achieved through software intelligence, not expensive hardware |
| **Effort** | High (build) / Low (maintenance) | Overbuilt hardware requires upfront effort but runs reliably |

### Motion System: "Tractor-Racecar" Balance
- **High-Mass Frame** (Tractor): M12 threaded rod skeleton absorbs vibrations, provides stability
- **Low-Weight Gantry** (Racecar): Lightweight moving parts minimize inertia
- **Geared Wade Extruder**: Heavy but unstoppable extrusion, prioritized over raw speed

### Component Selection Philosophy
- **PSU**: Mount to frame (lowers center of gravity, adds stability)
- **Filament Spool**: Keep independent (pendulum effect from top-mount ruins surface quality)
- **Electronics**: Base mount (protect from heat, keep gantry clear)
- **Fasteners**: Unified fastener system (M3 + M12) where possible

### Key Engineering Truths
- **1.75mm Filament**: Standardized for better flow control, thermal efficiency, and detail
- **Dry Filament Mandate**: No longer optional—dryers essential for consistent results
- **Triple-Z Kinematic Leveling**: Eliminates bed leveling errors rather than compensating
- **Draft-Free Enclosure**: Critical for engineering materials (ABS, PC, Nylon)
- **Input Shaping**: Enables heavy frames to perform like lightweight ones

## Consequences

### Benefits
- **Proven Architecture**: Every design choice has 20 years of community validation
- **Predictable Failures**: Well-understood failure modes and solutions
- **High Reliability**: Overbuilt hardware requires minimal maintenance once assembled
- **Global Accessibility**: All components available at local hardware stores
- **Software-Led Quality**: Klipper compensates for hardware limitations, keeping costs low
- **Scalability**: Principles apply across build volumes and donor types

### Trade-offs
- **Higher Initial Effort**: Building a "Tractor" takes more time than assembling an appliance
- **Heavy Machine**: ~15-20kg total weight—not portable
- **Moderate Speed**: Cannot compete with 300-600mm/s speed demons
- **Industrial Aesthetic**: Threaded rods and open structure less "pretty" than enclosed appliances
- **Set-and-Forget Philosophy**: Requires careful initial setup, but minimal ongoing tinkering

### What This Enables
- ADR-001 (M12 Skeleton): Chosen for mass damping and rigidity
- ADR-002 (Greg Wade): Chosen for geared extrusion reliability
- ADR-003 (Smooth Rods): Low-cost linear motion compatible with heavy frame
- ADR-005 (Triple-Z): Kinematic leveling for set-and-forget reliability
- ADR-009 (Puck System): Modularity without sacrificing rigidity

### What This Rejects
- Lightweight aluminum extrusion frames (insufficient mass damping for our cost target)
- Linear rails (unnecessary cost for our speed envelope)
- Direct-drive extruders without gearing (insufficient torque for reliable printing)
- High-speed motion chasing (diminishing returns, exponential cost increase)
- Multi-toolhead systems (too complex for <$300 target)

## BOM Implications (Generic)

### Scenario A: Tier 3+ Build (Recommended)
- **Philosophy alignment**: Full "Tractor" build with overbuilt hardware
- **Parts needed**:
  - M12 threaded rods (new or galvanized)
  - Greg Wade extruder components
  - E3D V6/CHT hotend
  - Triple-Z stepper motors
  - Filament dryer (essential)
- **Cost implication**: Medium ($250-350 AUD total)
- **Donor compatibility**: All donors (may need to supplement missing parts)

### Scenario B: Tier 2 Salvage Build
- **Philosophy alignment**: Partial alignment—scavenge where possible, maintain core principles
- **Parts needed**:
  - Scavenged smooth rods/steppers from printer
  - New M12 rods (frame must match spec)
  - New Greg Wade (donor extruders usually unreliable)
  - New hotend (V6/CHT)
- **Cost implication**: Low-Medium ($150-250 AUD)
- **Donor compatibility**: Selective—keep compatible parts, replace rest

### Scenario C: Tier 1 Emergency Build
- **Philosophy alignment**: Minimal alignment—survival mode
- **Parts needed**:
  - Whatever can be salvaged
  - May violate "unified fastener" rule
  - May need to skip filament dryer initially
- **Cost implication**: Very Low ($0-100 AUD)
- **Donor compatibility**: Whatever works
- **Warning**: Violates multiple principles, expect reliability issues

### Universal Requirements Across All Scenarios
- **Filament Dryer**: Required for any quality printing (hygroscopic materials)
- **Klipper Firmware**: Required for Input Shaping and Pressure Advance
- **Draft Control**: Enclosure or draft-free environment mandatory
- **Triple-Z**: Three-point leveling system non-negotiable for first-layer reliability

## Implementation Notes

### Software Requirements
- **Klipper**: Mandatory for Input Shaping, Pressure Advance, and kinematic leveling
- **Input Shaping Calibration**: Required for all builds to cancel frame resonances
- **Pressure Advance Tuning**: Required for all builds with geared extruders

### Assembly Considerations
- **Initial Setup**: Careful alignment critical—frame squareness, rod straightness, belt tension
- **Jam Nuts**: Use on all M12 joints to prevent vibration loosening
- **Torque**: Moderate (15-20 ft-lbs) on fasteners—over-tightening deforms plastic parts
- **Validation**: Print calibration parts and tune Klipper features before production use

### Maintenance Philosophy
- **Set-and-Forget**: Once properly built, Amalgam requires minimal ongoing adjustment
- **Preventive**: Focus on preventing issues (dry filament, draft control) rather than fixing them
- **Overbuilt = Forgiving**: Heavy tolerances and robust hardware absorb minor issues

## References

### Project Documentation
- **[../philosophy.md](../philosophy.md)**: The "Tractor" philosophy and heritage acknowledgments
- **[../manifesto.md](../manifesto.md)**: Project philosophy and "Tractor" concept
- **docs/articles/3D-Printing-In-The-Age-Of-The-Appliance.md**: Context on why Amalgam rejects the appliance model

### Technical Ancestors (What We Borrowed)
| Project | Contribution to Amalgam |
|---------|---------------------------|
| [RepRap Darwin (2007)](https://reprap.org/wiki/Darwin) | Box-frame threaded-rod skeleton |
| [RepRap Mendel (2009)](https://reprap.org/wiki/Mendel) | "Plough" X-carriage sled on dual rods |
| [Prusa i3 Rework (2013)](https://www.thingiverse.com/thing:119616) | Greg's Wade geared extruder (ancestor of Pitan) |
| [Voron Legacy](https://vorondesign.com/voron_legacy) | Dual 8mm rods, vertical stacking (ADR-021) |
| [Voron Trident](https://vorondesign.com/voron_trident) | Three-pillar Z-drop, Triple-Z leveling (ADR-005, ADR-023) |
| [The 100](https://github.com/MSzturc/the100) | Klipper-first: software compensates for cheap hardware |
| [The Rook](https://github.com/Kanrog/Rook) | Box-frame serviceability and maintenance philosophy |

## Evolution Notes
This ADR captures the consensus of the RepRap community as of 2026. As new technologies emerge (e.g., AI slicers, new materials), specific implementations may change, but the core pillars—mass, software intelligence, reliability—will remain.
