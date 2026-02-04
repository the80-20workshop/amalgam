# Engineering Analysis & Validation

This folder contains **technical calculations and measurements** that validate Amalgam design decisions and support parametric configuration. Use this when you need to understand the physics behind design choices or want to explore trade-offs.

## Contents

| Document | Topic | Key Insight |
|----------|-------|-------------|
| [rod-sag-analysis.md](rod-sag-analysis.md) | Smooth rod deflection + acceleration limits | M8 vs M10 deflection at various spans; max safe acceleration per rod diameter |
| [z-height-analysis.md](z-height-analysis.md) | Tall Z tradeoffs | Leadscrew whip, frame resonance, and why 280mm is the Tier 1 limit |
| [single-vs-dual-rod.md](single-vs-dual-rod.md) | Single rod problems | Why single rods have 4× deflection and can't resist rotation |
| [motion-system-comparison.md](motion-system-comparison.md) | Rods vs V-slots | Precision, wear, maintenance differences between motion systems |

## What These Validate

These analyses support:
- **ADR decisions** — Physics-based justification for design choices (e.g., why M10 frame, why MDF damping)
- **Parametric defaults** — config.py settings based on tested ranges
- **Tuning guidance** — Input Shaping, acceleration profiles per frame path
- **Fitness constraints** — ADR-026 stability analysis for bed size and Z-height

## Related Documentation

- **Design Decisions** → See `docs/adr/` (these analyses inform those choices)
- **Reference Specs** → See `docs/reference/` (factual component specs)
- **Build Guides** → See `docs/guides/` (how to implement these validated designs)

---

*These are technical deep-dives. For how-to instructions, see guides/. For design context, see ADRs.*
