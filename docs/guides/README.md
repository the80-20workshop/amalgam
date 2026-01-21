# Build Guides

This folder contains tier-specific build guides for Neo-Darwin.

## Tier System

| Tier | Description | Klipper Host | Key Characteristic |
|------|-------------|--------------|-------------------|
| **0** | Klipper-only | Laptop/RPi/Zero2W | Keep donor printer, just flash Klipper |
| **1** | Single donor | Laptop/RPi/Zero2W | 1 donor + buy 1 motor (dual Y) |
| **2** | Dual donor | Laptop/RPi/Zero2W | 2 donors, multi-MCU, enough parts |
| **3** | Reference Spec | Integrated (SKIPR) | MKS SKIPR, CAN bus, single PSU |

## Guides (In Progress)

Build order for documentation:
1. **Tier 3** - Reference specification (MKS SKIPR integrated)
2. **Tier 2** - Dual donor with Klipper host variations
3. **Tier 1** - Single donor, minimal purchases
4. **Tier 0** - Pointers to Klipper flashing resources

### Klipper Host Guides

The `klipper/` subfolder contains host-specific setup:
- `laptop-host.md` - Repurposed laptop running Klipper
- `rpi-3b-host.md` - Raspberry Pi 3B+ setup
- `zero-2w-host.md` - Raspberry Pi Zero 2W setup

## Guide Structure

Each tier guide follows this structure:
1. **Prerequisites** - What you need before starting
2. **Bill of Materials** - Tier-specific BOM
3. **Assembly** - Step-by-step with photos
4. **Wiring** - Electrical connections
5. **Klipper Config** - printer.cfg for the tier
6. **First Print** - Calibration and tuning

## Config-Driven Documentation

These guides are generated from templates using `config.py` settings via Quarto.
This ensures documentation stays in sync with the parametric CAD system.
