# Neo-Darwin Architecture Decision Records (ADRs)

This directory contains all Architecture Decision Records (ADRs) for the Neo-Darwin project. Each ADR documents a significant engineering decision, including context, alternatives, rationale, and consequences.

## How to Read This Directory

ADRs are numbered chronologically in order of creation (000-021). However, for understanding the project's engineering philosophy:

1. **Start with ADR-000**: Engineering Philosophy and "Tractor" principles
2. **Read Core Hardware ADRs**: Foundation (001), motion (021), extruder (019), hotend (004)
3. **Read Motion & Leveling ADRs**: Triple-Z (005), puck system (009, 010)
4. **Read Electronics ADRs**: Mainboard (012), drivers (013), CAN bus (007)
5. **Read Tooling/Software ADRs**: CAD (017), documentation (018)

Note: Some ADRs are superseded (003→021, 002→019, 006→014). Superseded ADRs are preserved for decision history.

## ADR Index

### Foundational ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-000](000-engineering-philosophy.md) | Engineering Philosophy (20 Years of RepRap Wisdom) | Accepted | Core principles: Mass, Software, Gearing, Neo-Darwin Square trade-offs |
| [ADR-001](001-m10-skeleton.md) | M10 Threaded Rod Skeleton | Accepted | Steel frame for mass damping and rigidity (M10 over M12 for practicality) |
| ~~[ADR-002](002-greg-wade.md)~~ | ~~Greg's Wade Geared Extruder~~ | **Archived** | Superseded by ADR-019 (Pitan) |
| ~~[ADR-003](003-smooth-rods.md)~~ | ~~Smooth Rods vs Linear Rails~~ | **Superseded** | Superseded by ADR-021 (Dual-Rod Motion System) |
| [ADR-004](004-v6-cht.md) | E3D V6 Hotend with CHT Nozzle | Accepted | Standard V6 with CHT clone nozzle for high flow without ooze |

### Motion & Leveling ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-005](005-triple-z.md) | Triple-Z Kinematic Leveling | Accepted | 3 independent Z-motors for automated bed leveling |
| ~~ADR-006~~ | Z-Probe Selection (Legacy) | **Archived** | Superseded by ADR-014 |
| [ADR-009](009-puck-system.md) | Modular Puck & Spider Bed System | Accepted | Standardized mounting for toolheads, bed supports, Z-motors |
| [ADR-010](010-floating-z-puck.md) | Floating Z-Puck System | Accepted | Parametric Z-motor pucks for any bed size, double-nut anchor |
| ~~[ADR-020](020-dual-8-scavenger.md)~~ | ~~Dual-8 Scavenger Variant~~ | **Superseded** | Analysis merged into ADR-021 |
| [ADR-021](021-dual-rod-motion-system.md) | Dual-Rod Motion System | **Accepted** | Dual 8mm vertical stacking as reference spec (supersedes ADR-003, ADR-020) |
| [ADR-022](022-linear-bearings.md) | Linear Bearing Selection | **Accepted** | LM8LUU for X, LM8UU for Y/Z; scavenged bearing protocol |
| [ADR-023](023-z-drop-architecture.md) | Z-Drop Architecture | **Accepted** | Bed moves only in Z, XY gantry at fixed height; enables Triple-Z |
| [ADR-024](024-heated-bed-size.md) | Heated Bed Size Selection | **Accepted** | 220×220mm reference (Anet A8); analysis of scavengeable bed sizes |

### Foundation & Electronics ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-007](007-can-bus.md) | CAN Bus Architecture | Accepted | Future-proofing for toolhead boards, ERCF, modular expansion |
| [ADR-008](008-spider-bed.md) | Spider Bed Support System | Accepted | Modular 3-part bed support for printing on small donor machines |
| [ADR-011](011-laminated-plinth.md) | Laminated Plinth Baseboard | Accepted | Constrained Layer Damping (CLD) foundation for Tier 3 Reference Spec |
| [ADR-012](012-mainboard-host-architecture.md) | Mainboard & Host Architecture | Accepted | MKS SKIPR Reference Spec, multi-MCU salvage paths |
| [ADR-013](013-drivers-endstops.md) | Driver & Endstop Strategy | Accepted | TMC2209 with mechanical switches, Z-max safety switch |
| [ADR-016](016-electronics-mounting.md) | Electronics & PSU Mounting Strategy | Accepted | Direct MDF coupling (Reference) vs printed puck frames |

### Tooling & Probing ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-014](014-z-probe-selection.md) | Z-Probe Selection (SuperPINDA vs BLTouch) | Accepted | SuperPINDA for Reference Spec (metal beds), BLTouch for scavenger (universal) |
| [ADR-015](015-single-toolhead.md) | Single Toolhead Architecture | Accepted | Base spec single toolhead, ERCF v2 expansion, manual puck swaps for laser/pen |

### Software & Tooling ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-017](017-parametric-cad-system.md) | Parametric CAD System | Accepted | build123d over OpenSCAD/FreeCAD/TinkerCAD for BREP and Python ecosystem |
| [ADR-018](018-documentation-system.md) | Documentation & Assembly Guide System | Accepted | Quarto for literate CAD, professional PDFs, conditional content |
| [ADR-019](019-pitan-extruder.md) | Pitan Extruder | Accepted | Single-drive, scavengeable NEMA17, $4-10 cost (supersedes ADR-002) |

## ADR Categories

### Core Hardware (001, 004, 019, 021)
Frame, extruder, hotend, and motion system - the physical foundation of the machine.
- ADR-001: M10 Frame Skeleton
- ADR-021: Dual-Rod Motion System (Dual 8mm vertical stacking - Reference Spec)
- ADR-004: E3D V6 + CHT Hotend
- ADR-019: Pitan Extruder (Reference Spec)

### Motion & Leveling (005, 007-010)
Z-axis leveling, CAN bus, modular bed, and Z-motor mounting - kinematic accuracy and foundation.

### Foundation & Electronics (008-009, 011-013, 016)
Baseboard, mainboard, drivers, endstops, and electronics mounting - "Brain" and power.

### Tooling & Probing (014-015)
Z-probe selection and toolhead architecture - single/multi-material capability.

### Software & Tooling (017-018)
CAD system and documentation - parametric design and assembly guides.

## Reading Order for New Contributors

If you're new to Neo-Darwin and want to understand the engineering decisions:

1. **Engineering Philosophy** → ADR-000
2. **Hardware Foundations** → ADR-001 (M10 Frame), ADR-019 (Pitan Extruder), ADR-004 (Hotend)
3. **Motion System** → ADR-021 (Dual-Rod Motion), ADR-005 (Triple-Z)
4. **Electronics** → ADR-012, 013
5. **Probing** → ADR-014
6. **Advanced Features** → ADR-007, 009, 011, 015, 016
7. **Tooling** → ADR-017, 018

Notes:
- ADR-002 (Greg's Wade) is archived—see ADR-019 for the current extruder decision.
- ADR-003 (Smooth Rods) is superseded—see ADR-021 for the current motion system decision.

## ADR Template

When creating a new ADR, use the template at `template.md`:

```markdown
# ADR-XXX: [Title]

## Status
Accepted | Proposed | Deprecated | Superseded

## Context
What is the issue we're facing that motivated this decision?

## Decision
What is the change we're proposing?

## Consequences
What becomes easier or more difficult to do because of this change?

## BOM Implications (Generic)
What parts are affected by this decision?

## References
Links to relevant documentation, AI conversations, or external resources.
```

## ADR Lifecycle

- **Proposed**: Initial draft, under discussion
- **Accepted**: Decision finalized, implemented
- **Deprecated**: Still in use, but recommended against for new builds
- **Superseded**: Replaced by newer ADR, kept for decision history (links forward to replacement)
- **Archived**: No longer relevant, kept for historical reference only

## Version Control

All ADRs are tracked in git. Changes to accepted ADRs should be:
- Clearly explained in commit messages
- Discussed with project maintainers before merging
- Documented with rationale for the change

## References

- **Project Manifesto**: `MANIFESTO.md` - High-level philosophy and goals
- **Reference Documentation**: `docs/reference/` - Detailed technical discussions
- **AI Conversations**: `docs/reference/ai-conversations/` - Raw design discussions
- **CAD System**: `cad/` - build123d parametric scripts
- **Build Instructions**: `docs/planning/` - Assembly and construction guides

---

**"The code handles the permutations; the iron handles the quality."**
