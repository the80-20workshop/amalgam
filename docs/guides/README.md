# Build Guides & Assembly Instructions

This folder contains **step-by-step instructional guides** for assembling Amalgam. These are Quarto documents that generate professional PDFs with conditional content per frame path and configuration.

## Core Principle

Amalgam requires **two matching donor printers**. Choose your frame path based on your donors, then follow the guides.

## Frame Paths

| Path | Frame | Motion | Best Donors | Reference |
|------|-------|--------|-------------|-----------|
| **Scaffold** | M10 threaded rod + MDF | Dual 8mm smooth rods | Anet A8, Wanhao i3, Prusa clones | ADR-025, ADR-001, ADR-021 |
| **Mill** | Aluminum extrusion + MDF | V-slot rails + POM wheels | Ender 3, CR-10, Aquila | ADR-025 |
| **Lathe** | Aluminum extrusion + MDF | Dual 8mm smooth rods + IGUS | Ender 3 + bought rods, mixed | ADR-025, ADR-021 |

## Electronics Options

| Option | Controller | Cost | Complexity |
|--------|-----------|------|-----------|
| **Dual-MCU** | Two scavenged boards + Klipper | $0 (scavenged) | Medium (wiring) |
| **SKIPR** | Single MKS SKIPR board | ~$130 | Low (cleaner setup) |

## Available Guides

| Guide | Description |
|-------|-------------|
| [calibration-guide.md](calibration-guide.md) | Complete calibration sequence: first layer, dimensions, Klipper tuning, filament profiles |
| [maintenance-setup.md](maintenance-setup.md) | Mechanical setup procedures and ongoing maintenance for all frame paths |

## Guides (In Progress)

Build order for documentation:
1. **frame-assembly.qmd** - Construct your frame per path (Scaffold/Mill/Lathe)
2. **klipper-config.qmd** - Configure Klipper firmware (electronics-agnostic)
3. **klipper/** - Host-specific setup (Raspberry Pi, laptop, etc.)

### Frame Assembly Guides

Each frame path has its own assembly section:
1. **Prerequisites** - What you need before starting
2. **Bill of Materials** - Frame-path-specific BOM
3. **Assembly** - Step-by-step with photos
4. **Wiring** - Electrical connections (all paths share Triple-Z, Pitan + E3D V6)
5. **Klipper Config** - printer.cfg per path

### Klipper Configuration

The `klipper-config.qmd` guide covers:
- Printer configuration for all frame paths
- Dual-MCU vs. single-board (SKIPR) wiring
- Input shaping and motion tuning
- First print calibration

### Klipper Host Guides

The `klipper/` subfolder contains host-specific setup:
- Host options: Laptop, Raspberry Pi 3B+, Pi Zero 2W, etc.
- Installation and service configuration
- Network setup for remote access

## Config-Driven Documentation

These guides are generated from templates using `config.py` settings via Quarto.
This ensures documentation stays in sync with the parametric CAD system.

## Related Documentation

- **Donor Selection** → See `docs/reference/donor-printer-guide.md`
- **Parts & Costs** → See `docs/reference/MASTER_PARTS_LIST.md`
- **Design Decisions** → See `docs/adr/` (why these design choices)
- **Technical Specs** → See `docs/analysis/` (calculations and measurements)

---

*All paths use: MDF base damping, Triple-Z leveling, Pitan extruder, E3D V6 hotend, Klipper firmware.*
