# Amalgam Documentation

This directory contains all project documentation for Amalgam.

## Documentation Structure

```
docs/
├── adr/           # Architecture Decision Records (formal decisions)
├── analysis/      # Engineering calculations and analysis
├── articles/      # Long-form thought pieces
├── deep-dives/    # Design exploration documents
├── guides/        # Tier-specific build guides
│   └── klipper/   # Klipper host setup guides
└── reference/     # Historical AI conversations (archival)
```

---

## Quick Navigation

### Getting Started

| Document | Description |
|----------|-------------|
| [manifesto.md](manifesto.md) | Project overview and quick-start |
| [philosophy.md](philosophy.md) | The "Tractor" philosophy |
| [../REFERENCE-SPEC.md](../REFERENCE-SPEC.md) | Hardware specification |
| [../BUILDING.md](../BUILDING.md) | CAD/STL generation |

### Architecture Decisions

| ADR | Topic |
|-----|-------|
| [adr/000](adr/000-engineering-philosophy.md) | Engineering Philosophy |
| [adr/001](adr/001-m10-skeleton.md) | M10 Frame Skeleton |
| [adr/019](adr/019-pitan-extruder.md) | Pitan Extruder |
| [adr/README.md](adr/README.md) | Full ADR index |

### Deep Dives

Design exploration documents that informed the ADRs:

| Document | Topic |
|----------|-------|
| [tractor_00](deep-dives/tractor_00_decision_guide.md) | Decision overview |
| [tractor_01](deep-dives/tractor_01_frame_and_assembly.md) | Frame design (M10 rationale) |
| [tractor_06](deep-dives/tractor_06_extruder_decision.md) | Extruder selection (Pitan) |
| [deep-dives/README.md](deep-dives/README.md) | Full index |

### Engineering Analysis

| Document | Topic |
|----------|-------|
| [rod-sag-analysis](analysis/rod-sag-analysis.md) | Smooth rod deflection + acceleration limits |

### Build Guides

| Guide | Description |
|-------|-------------|
| [guides/README.md](guides/README.md) | Tier system overview |
| Tier 3 Guide | Reference Spec (coming soon) |
| Tier 2 Guide | Dual donor (coming soon) |
| Tier 1 Guide | Single donor (coming soon) |

---

## Document Relationships

```
docs/manifesto.md (Quick Start)
    │
    ├── docs/philosophy.md (Why we build tractors)
    │
    ├── REFERENCE-SPEC.md (What we build)
    │       │
    │       └── docs/adr/ (Formal decisions)
    │               │
    │               └── docs/deep-dives/ (Exploration that led to decisions)
    │
    ├── BUILDING.md (How to generate parts)
    │       │
    │       └── cad/config.py (Parametric configuration)
    │
    └── docs/guides/ (How to build each tier)
            │
            └── docs/analysis/ (Engineering calculations)
```

---

## Reference Material

The `reference/` folder contains historical AI conversation logs and planning documents. These are preserved for context but are not actively maintained.

- `reference/ai-conversations/` - Raw design discussions
- `reference/planning/` - Project tracking documents

---

## Contributing

When adding documentation:

1. **New ADR:** Use `adr/template.md`, number sequentially
2. **Design exploration:** Add to `deep-dives/`, reference from ADR
3. **Analysis:** Add to `analysis/`, include calculations
4. **Build guide:** Add to `guides/`, follow tier structure
