# ADR-023: Z-Drop Architecture

## Status
Accepted

## Context

A 3D printer must move the nozzle relative to the print surface in three axes. There are several ways to achieve this:

### Motion Architecture Options

**1. Bed-Slinger (Prusa i3 style)**
- Bed moves in Y, gantry moves in X, Z lifts gantry or bed
- Common in: Prusa MK3, Ender 3, Anet A8
- Characteristic: Bed swings back and forth during printing

**2. Z-Drop / Moving Bed Z (Voron Trident style)**
- XY gantry at fixed height, bed moves only in Z
- Common in: Voron Trident, RatRig V-Core
- Characteristic: Bed drops down as layers are printed

**3. Gantry-Rise / Fixed Bed (Voron 2.4 style)**
- Bed fixed at bottom, entire XY gantry rises in Z
- Common in: Voron 2.4, some industrial machines
- Characteristic: Gantry climbs upward during printing

**4. CoreXZ (Voron Switchwire style)**
- Bed moves in Y, toolhead moves in X and Z via CoreXZ kinematics
- Common in: Voron Switchwire, converted Enders
- Characteristic: Hybrid approach, complex belt paths

### Neo-Darwin Constraints

- **Triple-Z kinematic leveling** (ADR-005) - requires independent Z control
- **M10 threaded rod frame** (ADR-001) - heavy, rigid, not optimized for gantry climbing
- **Scavenger philosophy** - must work with donor printer parts
- **Heavy heated bed** - 235×235mm aluminum/glass bed has significant mass
- **"Tractor" philosophy** - mass for stability, software for precision

## Decision

We choose **Z-Drop Architecture** where the bed moves only in Z and the XY gantry operates at a fixed height near the top of the frame.

### Why Z-Drop?

#### 1. Triple-Z Synergy

Z-drop + Triple-Z is mathematically elegant:

| Architecture | Auto-Leveling Method | Motors Required |
|--------------|---------------------|-----------------|
| Z-Drop + Triple-Z | Z_TILT_ADJUST (tilt bed to match gantry) | 3 Z-motors |
| Gantry-Rise + Fixed Bed | Quad Gantry Level (tilt gantry to match bed) | 4 Z-motors |

**Three points define a plane.** With Z-drop, we tilt a static bed to match the gantry - simple geometry, fewer motors, proven by Voron Trident.

With gantry-rise, we'd need to tilt the entire moving XY assembly using 4 motors (Quad Gantry Leveling) - more complex, more parts, harder to scavenge.

#### 2. Center of Gravity Stability

As the print progresses:

**Z-Drop:**
```
Start of print:          End of print:
┌─────────────┐          ┌─────────────┐
│   [Gantry]  │          │   [Gantry]  │
│             │          │             │
│   [Bed+Print at top]   │             │
│             │          │             │
└─────────────┘          │   [Bed+Print at bottom]
     CoG: High           └─────────────┘
                              CoG: LOW ✓
```

The heaviest part (bed + growing print) moves **toward** the 36mm MDF base. Center of gravity stays low = more stability.

**Gantry-Rise:**
```
Start of print:          End of print:
┌─────────────┐          ┌─────────────┐
│             │          │   [Gantry at top]
│             │          │             │
│   [Gantry at bottom]   │             │
│   [Bed]     │          │   [Bed]     │
└─────────────┘          └─────────────┘
     CoG: Low                 CoG: HIGH ✗
```

Heavy gantry (motors, extruder, rods) climbs to top of frame = pendulum effect, frame flex amplified.

#### 3. Cable Management

| Aspect | Z-Drop | Gantry-Rise |
|--------|--------|-------------|
| Moving cables | Bed heater + thermistor (2 wires) | X motor, Y motors, extruder, fans, hotend, probe (10+ wires) |
| Cable chain | Simple, short | Long, complex, moves full Z height |
| Failure mode | Bed wire breaks (easy fix) | Toolhead wire breaks (printer stops) |

The "racecar brain" (toolhead with all its sensors and actuators) stays at fixed height. Only simple power wires to the bed need to flex.

#### 4. Scavenger Simplicity

| Component | Z-Drop | Gantry-Rise |
|-----------|--------|-------------|
| Z drive | 3 standard leadscrews | 4 leadscrews + belt sync or 4 motors |
| Z rods | 2 vertical smooth rods | 4 corner rods or rails |
| Mechanics | Bed platform rises/falls | Entire gantry must climb frame |
| Donor parts | Leadscrews from any printer | Need matched quad setup |

Z-drop uses the simplest possible Z mechanics - vertical leadscrews and smooth rods that any donor printer provides.

#### 5. MDF Base Damping

The 36mm laminated MDF plinth (ADR-011) provides constrained layer damping. Z-drop keeps the heavy bed **close to the damping base** throughout printing:

- Print layer 1: Bed at top, but print mass is minimal
- Print layer 100: Bed lower, print mass increasing, closer to MDF damping
- Print layer 500: Bed near bottom, maximum mass, maximum damping benefit

This maximizes the effectiveness of Input Shaper calibration - resonances stay consistent because the mass stays near the damped base.

## Consequences

### Benefits

1. **Simpler Triple-Z**: 3 motors define a plane, no quad gantry complexity
2. **Stable center of gravity**: Heavy parts stay low throughout print
3. **Easy cable management**: Only bed wires move
4. **Scavenger-friendly**: Standard leadscrews, no custom gantry mechanics
5. **MDF damping synergy**: Heavy mass stays near damped base
6. **Proven design**: Voron Trident validates this architecture

### Trade-offs

1. **Taller frame**: Need Z-height for bed travel + clearance
2. **Bed drop risk**: Heavy bed can crash if power lost (see mitigation below)
3. **Bed heater wires**: Must accommodate Z travel (flexible cable or chain)
4. **Print removal**: Bed at bottom after tall prints (must raise to remove)

### Bed Drop Mitigation

Heavy beds can "back-drive" unpowered leadscrews and crash down. Mitigations:

1. **Leadscrew friction**: TR8×2 (2mm pitch) has enough friction to hold 235×235 bed
2. **Triple-Z distribution**: Load spread across 3 screws increases holding friction
3. **Anti-backlash nuts**: Add friction that helps hold position
4. **Software**: Klipper can park bed at safe height before shutdown
5. **Mechanical stop**: Optional hard stop at bottom of Z travel

For Neo-Darwin's 235×235mm bed (~500-800g with glass), the friction of 3 TR8×2 leadscrews is sufficient to prevent unpowered drop.

## Architectural Integration

### Relationship to Other ADRs

```
ADR-023: Z-Drop Architecture
    │
    ├── Enables → ADR-005: Triple-Z (3-motor bed leveling)
    │
    ├── Requires → ADR-008: Spider Bed Support (carries bed on Z)
    │
    ├── Informs → ADR-021: Dual-Rod Motion (XY at fixed height)
    │
    └── Benefits → ADR-011: Laminated Plinth (damping stays effective)
```

### Frame Layout

```
┌─────────────────────────────────────┐  ← Top of M10 frame
│                                     │
│  ┌─────────────────────────────┐    │  ← XY Gantry (FIXED HEIGHT)
│  │  Y-rods (dual per side)     │    │
│  │     [Plough on X-rods]      │    │
│  └─────────────────────────────┘    │
│                                     │
│         ↕ Z Travel (~250mm)         │
│                                     │
│  ┌─────────────────────────────┐    │  ← Bed Platform (MOVES IN Z)
│  │      [Heated Bed]           │    │
│  │   Z1 ─────┼───── Z2         │    │  ← Triple-Z leadscrews
│  │           Z3                │    │
│  └─────────────────────────────┘    │
│                                     │
└─────────────────────────────────────┘  ← 36mm MDF Plinth
```

### Motion Independence

**Critical design principle:** The XY gantry and Z-bed are **completely independent systems**.

- XY gantry never moves in Z
- Bed never moves in X or Y
- Z_TILT_ADJUST tilts the bed plane to match the gantry plane
- No mechanical coupling between XY and Z motion

This independence simplifies:
- Klipper configuration (separate stepper sections)
- Calibration (XY and Z tuned independently)
- Troubleshooting (isolate issues to one system)
- Scavenging (Z parts don't need to match XY parts)

## Alternatives Considered

### Alternative A: Bed-Slinger (Rejected)

Moving bed in Y (like Prusa i3):

**Pros:**
- Simpler frame (shorter in Y)
- Well-proven design
- Easy to scavenge (most donors are bed-slingers)

**Cons:**
- Heavy bed moving in Y causes ringing artifacts
- Limits print speed for quality
- Y-motor works harder (accelerating bed mass)
- Bed leveling more complex (bed moves during probe)

**Verdict:** Rejected. Moving heavy bed in Y contradicts "Tractor" philosophy of keeping mass stationary for quality.

### Alternative B: Gantry-Rise (Rejected)

Fixed bed at bottom, gantry climbs (like Voron 2.4):

**Pros:**
- Bed always accessible
- Excellent for enclosed chambers (heat rises to gantry)
- Premium feel

**Cons:**
- Requires 4 Z-motors for Quad Gantry Leveling
- Center of gravity rises during print
- Complex cable management (toolhead wires must travel full Z)
- Heavier gantry (carries more structure)
- Harder to scavenge (need 4 matched Z-motors)

**Verdict:** Rejected. QGL requires 4 motors vs Triple-Z's 3. Harder to scavenge, higher CoG during printing.

### Alternative C: CoreXZ (Rejected)

Bed moves in Y, toolhead moves in X and Z via crossed belts:

**Pros:**
- Compact design
- Good for conversions (Ender → Switchwire)

**Cons:**
- Still a bed-slinger (Y-axis bed movement)
- Complex belt paths
- Not compatible with M10 threaded rod frame
- Different lineage from Darwin/Mendel

**Verdict:** Rejected. Still has bed-slinger drawbacks, incompatible with frame philosophy.

## Implementation Notes

### Z Travel Calculation

```python
# From config.py
Z_TRAVEL = BUILD_VOLUME["Z"] + CLEARANCE
        = 250 + 30
        = 280mm minimum Z travel

FRAME_HEIGHT = Z_TRAVEL + GANTRY_HEIGHT + BED_THICKNESS + PLINTH_CLEARANCE
            = 280 + 80 + 40 + 30
            = 430mm internal height
```

### Leadscrew Positioning (for Z_TILT_ADJUST)

Optimal Triple-Z placement for Z_TILT_ADJUST:

```
        ┌─────────────────────┐
        │                     │
        │    Z3 (back-center) │
        │         ●           │
        │                     │
        │  ●               ●  │
        │ Z1               Z2 │
        │ (front-left) (front-right)
        └─────────────────────┘
```

**Spread as wide as possible** - maximizes the "lever arm" for tilt correction, improving accuracy.

### Klipper Configuration

```ini
[stepper_z]   # Z1 - front left
[stepper_z1]  # Z2 - front right
[stepper_z2]  # Z3 - back center

[z_tilt]
z_positions:   # Leadscrew positions
    30, 30     # Z1 front-left
    200, 30    # Z2 front-right
    115, 200   # Z3 back-center
points:        # Probe points (near leadscrews)
    30, 30
    200, 30
    115, 200
```

## References

- ADR-005: Triple-Z Independent Kinematic Leveling
- ADR-008: Spider Bed Support System
- ADR-011: Laminated Plinth Baseboard
- ADR-021: Dual-Rod Motion System
- [Voron Trident](https://vorondesign.com/voron_trident): Z-drop + Triple-Z reference
- [Voron 2.4](https://vorondesign.com/voron2.4): Gantry-rise + QGL reference
- docs/deep-dives/tractor_02_xy_axis_system.md: Detailed Z-drop implementation
