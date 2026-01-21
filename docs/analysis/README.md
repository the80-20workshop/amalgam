# Engineering Analysis

This folder contains engineering calculations and analysis that inform Neo-Darwin design decisions.

These documents provide the mathematical foundation for understanding trade-offs in the design.

## Contents

| Document | Topic | Key Insight |
|----------|-------|-------------|
| [rod-sag-analysis.md](rod-sag-analysis.md) | Smooth rod deflection | M8 vs M10 at various spans |
| [max-safe-acceleration.md](max-safe-acceleration.md) | Motion limits | Toolhead mass vs acceleration |

## Future Analysis

The following analyses are planned for the engineering analysis TUI tool:

- **Frame rigidity calculator**: M8/M10/M12 threaded rod stiffness
- **Bed size optimizer**: Heat bed size vs frame dimensions
- **Motor torque requirements**: Extruder gear ratios vs filament resistance
- **Resonance frequency estimator**: For Input Shaping configuration

## Using These Calculations

These analyses are inputs to:
- **ADRs**: Justifying design choices
- **config.py**: Setting parametric defaults
- **Analysis TUI**: Interactive build assessment tool (planned)
