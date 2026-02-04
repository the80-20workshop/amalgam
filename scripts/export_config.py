#!/usr/bin/env python3
"""
Export config.py values to Quarto variables format.

Usage:
    python scripts/export_config.py > docs/_variables.yml
    python scripts/export_config.py --tier 3    # Tier-specific

This generates a YAML file that Quarto can use for conditional content
and variable substitution in documentation.
"""

import sys
from pathlib import Path

# Add scripts directory to path
scripts_path = Path(__file__).parent
sys.path.insert(0, str(scripts_path))


def get_config_values() -> dict:
    """Load config.py and extract values."""
    cad_path = scripts_path.parent / "cad"
    config_path = cad_path / "config.py"

    if not config_path.exists():
        print("Error: cad/config.py not found", file=sys.stderr)
        print("Run 'python scripts/wizard.py' first", file=sys.stderr)
        sys.exit(1)

    config_globals = {}
    try:
        exec(config_path.read_text(), config_globals)
    except Exception as e:
        print(f"Error reading config.py: {e}", file=sys.stderr)
        sys.exit(1)

    return {
        k: v for k, v in config_globals.items()
        if not k.startswith("_") and not callable(v)
    }


def export_quarto_variables():
    """Export config values as Quarto variables."""
    config = get_config_values()

    # Get build volume
    build_volume = config.get("BUILD_VOLUME", {})

    # Build the variables dict
    variables = {
        # Bed/build volume
        "bed_x": config.get("BED_SIZE_X", build_volume.get("x", 235)),
        "bed_y": config.get("BED_SIZE_Y", build_volume.get("y", 235)),
        "build_z": build_volume.get("z", config.get("BUILD_Z", 250)),

        # Rods
        "smooth_rod_dia": config.get("SMOOTH_ROD_DIA", 10.0),
        "m10_nominal": config.get("M10_NOMINAL_DIA", 10.0),
        "lumpy_factor": config.get("LUMPY_FACTOR", 0.5),

        # Extruder
        "extruder_type": config.get("EXTRUDER_TYPE", "PITAN"),
        "extruder_mass": config.get("EXTRUDER_MASS", 280),

        # Board
        "primary_board": config.get("PRIMARY_BOARD", "MKS_SKIPR"),
        "total_drivers": config.get("TOTAL_DRIVERS", 6),

        # Tier and Z config
        "tier": config.get("BUILD_TIER", 3),
        "z_config": config.get("Z_CONFIGURATION", "triple"),
        "has_canbus": config.get("HAS_CANBUS", True),

        # Frame dimensions
        "frame_x": config.get("FRAME_X", 0),
        "frame_y": config.get("FRAME_Y", 0),
        "frame_z": config.get("FRAME_Z", 0),
        "x_span": config.get("X_SPAN", 0),

        # Hotend
        "hotend_type": config.get("HOTEND_TYPE", "E3D_V6_CLONE"),
        "groovemount_dia": config.get("GROOVEMOUNT_DIA", 16.0),

        # Brand palette
        "brand_body_color": config.get("BRAND_BODY_COLOR", "#4A4A4A"),
        "brand_accent_color": config.get("BRAND_ACCENT_COLOR", "#FFFFFF"),
        "brand_base_color": config.get("BRAND_BASE_COLOR", "#1A1A1A"),

        # Logo pad
        "logo_pad_enabled": config.get("LOGO_PAD_ENABLED", True),
        "logo_pad_diameter": config.get("LOGO_PAD_DIAMETER", 18.0),
        "logo_pad_height": config.get("LOGO_PAD_HEIGHT", 0.5),

        # Texture recommendations
        "fuzzy_skin_recommended": config.get("FUZZY_SKIN_RECOMMENDED", True),
        "fuzzy_skin_point_distance": config.get("FUZZY_SKIN_POINT_DISTANCE", 0.3),
        "fuzzy_skin_thickness": config.get("FUZZY_SKIN_THICKNESS", 0.2),
    }

    # Add derived values
    tier = variables["tier"]
    tier_names = {
        0: "Klipper Only",
        1: "Single Donor",
        2: "Dual Donor",
        3: "Reference Spec",
        4: "Buy Everything",
    }
    variables["tier_name"] = tier_names.get(tier, f"Tier {tier}")

    z_config = variables["z_config"]
    variables["z_type_desc"] = "Triple Independent Z" if z_config == "triple" else "Belt-Driven Z"

    # Output as YAML
    print("# Auto-generated from cad/config.py")
    print("# Run: python scripts/export_config.py > docs/_variables.yml")
    print("")

    for key, value in variables.items():
        if isinstance(value, bool):
            print(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, str):
            # Quote strings
            print(f'{key}: "{value}"')
        elif isinstance(value, (int, float)):
            print(f"{key}: {value}")
        elif isinstance(value, list):
            # Format lists
            print(f"{key}:")
            for item in value:
                print(f'  - "{item}"')
        else:
            print(f'{key}: "{value}"')


def export_tier_config(tier: int):
    """Export tier-specific configuration."""

    tier_configs = {
        0: {
            "tier_name": "Tier 0: Klipper Only",
            "tier_desc": "Flash Klipper on existing printer",
            "klipper_host": "Laptop/RPi/Zero2W",
            "mcu": "Donor board",
            "z_system": "Keep donor Z system",
            "cost_estimate": "$0",
        },
        1: {
            "tier_name": "Tier 1: Single Donor",
            "tier_desc": "One donor printer, belt-driven Z",
            "klipper_host": "Laptop/RPi/Zero2W",
            "mcu": "Donor board",
            "z_system": "Belted Single-Z",
            "cost_estimate": "~$80 AUD",
        },
        2: {
            "tier_name": "Tier 2: Dual Donor",
            "tier_desc": "Two donors, Triple-Z, multi-MCU",
            "klipper_host": "Laptop/RPi/Zero2W",
            "mcu": "Multi-MCU (2 donor boards)",
            "z_system": "Triple-Z Independent",
            "cost_estimate": "~$200 AUD",
        },
        3: {
            "tier_name": "Tier 3: Reference Spec",
            "tier_desc": "MKS SKIPR, Triple-Z, CAN bus ready",
            "klipper_host": "Integrated (SKIPR)",
            "mcu": "MKS SKIPR",
            "z_system": "Triple-Z Independent",
            "cost_estimate": "~$270 AUD",
        },
    }

    if tier not in tier_configs:
        print(f"Error: Unknown tier {tier}", file=sys.stderr)
        sys.exit(1)

    print(f"# Tier {tier} Configuration")
    for key, value in tier_configs[tier].items():
        print(f'{key}: "{value}"')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Export config.py to Quarto variables")
    parser.add_argument("--tier", type=int, choices=[0, 1, 2, 3],
                        help="Export tier-specific config")
    args = parser.parse_args()

    if args.tier is not None:
        export_tier_config(args.tier)
    else:
        export_quarto_variables()
