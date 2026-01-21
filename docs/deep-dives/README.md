# Deep Dives

This folder contains in-depth design explorations and discussions that led to the formal Architecture Decision Records (ADRs).

**Relationship to ADRs:**
- **ADRs** (`docs/adr/`) = Formal, structured decisions with Status/Context/Decision/Consequences
- **Deep Dives** = The thinking process, analysis, and exploration that informed those decisions

## Contents

| Document | Topic | Related ADRs |
|----------|-------|--------------|
| [tractor_00_decision_guide.md](tractor_00_decision_guide.md) | Overview of key decisions | Multiple |
| [tractor_01_frame_and_assembly.md](tractor_01_frame_and_assembly.md) | M10 frame design, squaring | ADR-001 |
| [tractor_02_xy_axis_system.md](tractor_02_xy_axis_system.md) | X-Y motion, smooth rods | ADR-003 |
| [tractor_03_motor_mounts_vibration.md](tractor_03_motor_mounts_vibration.md) | Motor mounting, damping | ADR-000, ADR-011 |
| [tractor_04_xgantry_design_decision.md](tractor_04_xgantry_design_decision.md) | X-gantry architecture | ADR-003 |
| [tractor_05_psu_configurations.md](tractor_05_psu_configurations.md) | PSU options for tiers | ADR-012, ADR-016 |
| [tractor_06_extruder_decision.md](tractor_06_extruder_decision.md) | Pitan selection, single-drive | ADR-019 |

## Reading Order

For understanding the Neo-Darwin design:

1. Start with `tractor_00_decision_guide.md` for an overview
2. Read the ADRs for formal decisions
3. Return to specific deep dives for detailed rationale

## Contributing

When making significant design decisions:
1. Document the exploration in a deep dive
2. Create or update the relevant ADR
3. Cross-reference between them
