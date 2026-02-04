# Deep Dives: Historical Design Explorations

⚠️ **Note:** This folder contains historical design explorations that informed the formal Architecture Decision Records (ADRs). With the project's maturation to a **two-donor, three-frame-path** model (ADR-025, ADR-026), some content here is **partially outdated** but preserved for historical context.

**Relationship to ADRs:**
- **ADRs** (`docs/adr/`) = Current, formal decisions with Status/Context/Decision/Consequences
- **Deep Dives** = Historical thinking process and exploration (useful for understanding "why", not "what")

## Contents & Current Status

| Document | Topic | Status | Read For | See Instead For Current Decision |
|----------|-------|--------|----------|------|
| [tractor_00_decision_guide.md](tractor_00_decision_guide.md) | Overview of key design space | ⚠️ Partially Outdated | Historical perspective on scavenger philosophy | **ADR-025** (Multi-Frame), **ADR-026** (Donor Fitness), **ADR-000** (Philosophy) |
| [tractor_01_frame_and_assembly.md](tractor_01_frame_and_assembly.md) | M10 frame design, squaring, MDF | ✅ Relevant | Scaffold path details | **ADR-001** (M10 Skeleton), **ADR-025** (Multi-Frame) |
| [tractor_02_xy_axis_system.md](tractor_02_xy_axis_system.md) | X-Y motion, smooth rods | ✅ Relevant | Motion system design rationale | **ADR-021** (Dual-Rod Motion), **ADR-022** (Bearings) |
| [tractor_03_motor_mounts_vibration.md](tractor_03_motor_mounts_vibration.md) | Motor mounting, vibration damping | ✅ Relevant | Why mass damping matters | **ADR-000** (Philosophy), **ADR-011** (Plinth) |
| [tractor_04_xgantry_design_decision.md](tractor_04_xgantry_design_decision.md) | X-gantry architecture | ⚠️ Partially Outdated | Core-XY vs Cartesian trade-offs | **ADR-025** (Multi-Frame paths) |
| [tractor_05_psu_configurations.md](tractor_05_psu_configurations.md) | PSU options | ⚠️ Outdated | Old tier system (0/1/2/3) | **ADR-012** (Electronics), **docs/reference/** (current BOM) |
| [tractor_06_extruder_decision.md](tractor_06_extruder_decision.md) | Pitan selection, single-drive | ✅ Relevant | Why Pitan over Wade/E3D | **ADR-019** (Pitan Extruder) |

## Recommended Reading Order

**For understanding Amalgam architecture:**
1. **Current** → Read ADRs first (`docs/adr/`)
   - Start: ADR-000 (Philosophy), ADR-025 (Multi-Frame), ADR-026 (Fitness)
2. **For deeper context** → Return to relevant deep dives
   - Frame design → `tractor_01_*`
   - Motion system → `tractor_02_*`
   - Vibration damping → `tractor_03_*`
   - Extruder → `tractor_06_*`

**For historical decision context:**
- `tractor_00_decision_guide.md` gives you a view into pre-formalization thinking

## What Changed?

The pivot from "Tier 0/1/2/3" to "**Two Donors + Three Paths**" (ADR-025, ADR-026) simplified many of these explorations:
- ✅ **Scaffold path** (M10 + smooth rods) — primary, well-established
- ✅ **Mill/Lathe paths** — zero-waste donor alternatives
- ✅ **Donor fitness tiers** — explicit constraints on bed size and Z-height

Old tier system docs are outdated; refer to ADR-025 and `docs/reference/donor-printer-guide.md` instead.

---

*Use ADRs for current decisions. Return here for "how did we arrive at this" context.*
