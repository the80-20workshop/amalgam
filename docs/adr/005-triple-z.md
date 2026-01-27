# ADR-005: Triple-Z Independent Kinematic Leveling

## Status
Accepted

## Prerequisite
This ADR assumes **Z-Drop Architecture** (ADR-023) where the bed moves only in Z and the XY gantry operates at fixed height. Triple-Z tilts the bed to match the gantry plane.

## Context
The Z-motion system is critical for first-layer quality and dimensional accuracy. The bed must be perfectly level and stay level across thousands of prints.

In 2026, there are multiple Z-system options:
- Single motor with 3-point leveling (manual or belt-synced)
- Dual independent Z-motors (Prusa style)
- Triple independent Z-motors (Voron style)
- CoreXY Z with belt lift

Most budget printers use single Z-motor systems and rely on software compensation (mesh bed leveling). This works but doesn't fix the root cause - a physically non-level bed. Industrial printers use kinematic leveling with independent motors.

## Decision
We choose **Triple-Z Independent Motors with Klipper Z-Tilt** for the Neo-Darwin reference specification.

### Why Triple-Z?
1. **Kinematic leveling**: Physically aligns bed to gantry (not software compensation)
2. **Voron-class accuracy**: Same system used in high-end Voron printers
3. **Automated calibration**: Klipper Z-Tilt provides one-command bed leveling
4. **Set-and-forget**: Once calibrated, bed stays level for thousands of hours
5. **Rigidity**: Three points define a plane - mathematically optimal
4. **Mass balanced**: Distributed drive prevents bed sag
5. **Industrial standard**: Used in high-end CNC and manufacturing equipment

### Belted-Z Alternative (Tier 1)
For budget builds, a single motor with sync belt is available:
- **How**: One Z-motor drives three leadscrews via timing belt
- **Leveling**: Manual one-time setup with spacers
- **Pros**: Cheaper, simpler electronics
- **Cons**: No auto-calibration, must manually level if moved

## Consequences

### Benefits
- **True kinematic accuracy**: Physically perfect bed level
- **Automation**: Klipper handles leveling with `Z_TILT_ADJUST`
- **Stability**: Independent motors prevent bed wobble
- **Scalability**: Can handle large beds without sag
- **Repeatability**: Same first-layer quality on Day 1000 as Day 1
- **Professional feel**: "Set-and-forget" operation

### Trade-offs
- **Cost**: Requires 3 Z-motors (vs 1 for single motor)
- **Complexity**: More motors, drivers, and wiring
- **Power**: Higher power consumption (3 motors instead of 1)
- **Calibration time**: Initial setup takes longer

### Why NOT Single Motor with Mesh Compensation?
1. **Not true leveling**: Software compensates but doesn't fix misalignment
2. **Bed sag**: Single motor can cause center sag on large beds
3. **Tuning complexity**: Requires repeated mesh calibration
4. **First-layer variability**: Changes as bed heats and expands

### Why NOT Dual-Z?
1. **Planar math**: 3 points define a plane (2 points define a line)
2. **Corner droop**: Dual-Z has uncontrolled corners
3. **Bed flex**: Can cause bed to flex under weight

## BOM Implications (Generic)

### Scenario A: Buying New (Recommended for Tier 3)
- **Parts needed**:
  - 3x NEMA17 Z-motors (matched if possible)
  - 3x 8mm TR8x8 or T8x8 lead screws (or scavenged)
  - 3x anti-backlash nuts (or standard nuts)
  - 3x couplers (motor-to-leadscrew)
  - 3x Z-Pucks (printed)
  - Spider bed support (printed)
  - MKS SKIPR (or 6+ driver board)
- **Cost implication**: Medium (~$50-70 AUD for motors/screws)
- **Donor compatibility**: All donors
- **Board requirement**: 6+ drivers (X, Y, E, Z1, Z2, Z3)
- **Experience**: Set-and-forget

### Scenario B: Salvaging + 2 New Motors
- **Parts needed**:
  - 1x salvaged Z-motor from donor
  - 2x new NEMA17 Z-motors (matched to salvaged)
  - 3x leadscrews (salvaged or new)
  - 3x Z-Pucks (printed)
  - Spider bed support (printed)
- **Cost implication**: Medium (~$25-40 AUD for 2 motors)
- **Donor compatibility**: All donors
- **Board requirement**: 6+ drivers
- **Note**: Try to match motor torque and current ratings

### Scenario C: Donor Has Dual-Z (Prusa MK2/3)
- **Parts A: Upgrade to Triple-Z**
  - Parts needed: 1x new NEMA17 motor + 1x leadscrew + 1x Z-Puck
  - Cost implication: Low (~$12-15 AUD)
  - Donor compatibility: Prusa MK2/3
  - Note: Reuse 2 donor motors

- **Parts B: Keep Dual-Z (Not Recommended)**
  - Parts needed: None (use donor dual-Z)
  - Cost implication: Very Low ($0)
  - Donor compatibility: Prusa MK2/3 only
  - Note: Will suffer from corner droop on 250mm+ beds

### Scenario D: Belted-Z Single Motor (Tier 1)
- **Parts needed**:
  - 1x salvaged Z-motor
  - 3x leadscrews (salvaged or new)
  - 3x Z-Pucks (printed)
  - 3x pulleys (same tooth count)
  - 3x timing belts (matching length)
  - 3x belt clamps
  - Spider bed support (printed)
- **Cost implication**: Low (~$15-25 AUD for belts/pulleys)
- **Donor compatibility**: All donors
- **Board requirement**: 4 drivers (X, Y, E, Z)
- **Experience**: Set-and-monitor (manual leveling)

### Scenario E: Scavenging 3 Motors
- **Parts needed**:
  - 3x NEMA17 motors from various sources
  - 3x leadscrews (scavenged or new)
  - 3x Z-Pucks (printed)
  - Spider bed support (printed)
- **Cost implication**: Very Low ($0-15 AUD)
- **Donor compatibility**: Multiple donors or photocopiers
- **Board requirement**: 6+ drivers
- **Note**: Motors may have different torque/current - requires careful tuning

### Scenario F: High-End Matched Motors (Tier 4)
- **Parts needed**:
  - 3x matched NEMA17 motors (same brand, torque, current)
  - 3x high-quality leadscrews (anti-backlash)
  - 3x anti-backlash nuts
  - 3x Z-Pucks (printed)
  - Spider bed support (printed)
- **Cost implication**: High (~$60-80 AUD for motors)
- **Donor compatibility**: N/A (new purchase)
- **Board requirement**: 6+ drivers
- **Benefits**: Perfectly synchronized Z motion
- **Experience**: Overkill

## Implementation Notes

### Lead Screw Options
```
TR8x8: 8mm diameter, 2mm lead (recommended)
T8x8:  8mm diameter, 2mm lead (budget alternative)
```

### Z-Motor Configurations
```python
# config.py
TRIPLE_Z = True  # Triple independent Z-motors
```

### Spider Bed Support
- **Central hub**: Printed with 3 mounting points
- **Three arms**: Printed separately, bolted to hub
- **Bed mounting**: Triangle provides stability
- **Modular**: Arms can be printed on small donor printers

### Z-Tilt Calibration
```
Klipper Command: Z_TILT_ADJUST

Process:
1. Probe 3 points on bed
2. Calculate tilt and adjust motors
3. Repeat until tilt < 0.01mm
4. Save result to config
```

### Motor Wiring
- Z1: Front-left motor
- Z2: Front-right motor
- Z3: Back-center motor
- Must be on independent drivers (not shared)

### Board Requirements
```
Minimum 6 drivers for Triple-Z:
- Driver 1: X-axis
- Driver 2: Y-axis
- Driver 3: Extruder
- Driver 4: Z1
- Driver 5: Z2
- Driver 6: Z3

MKS SKIPR: 7 drivers (perfect for Triple-Z + ERCF)
BTT SKR 3: 8 drivers (excellent)
```

### Bed Leveling Accuracy
- **Manual leveling**: ±0.5mm (good enough for first layer)
- **Dual-Z**: ±0.2mm (better, but corners uncontrolled)
- **Triple-Z with Z-Tilt**: ±0.02mm (industrial accuracy)

### Maintenance
- **Check alignment**: After moving printer
- **Re-calibrate**: If bed replaced or leadscrews changed
- **Lubricate**: Light grease on leadscrews every 100 hours
- **Check couplers**: Verify tightness every 6 months

## References
- ADR-023: Z-Drop Architecture (explains why Z-drop enables Triple-Z)
- MANIFESTO.md: Section "The Tiered Path" and "Triple-Z Kinematic Leveling"
- [Voron Trident Z-System](https://vorondesign.com/voron_trident): Triple-Z reference design
- [Klipper Z-Tilt Documentation](https://www.klipper3d.org/Bed_Level.html#z-tilt)
- docs/AI-Conversations/ [Relevant conversations about Z-system selection]
