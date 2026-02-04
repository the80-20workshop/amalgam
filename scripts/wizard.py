#!/usr/bin/env python3
"""
Amalgam Configuration Wizard

Interactive TUI that guides builders through:
1. Parts inventory (what do you have?)
2. Tier determination (what can you build?)
3. Configuration generation (config.py)
4. Engineering analysis (will it work?)
5. Build orchestration (STLs, docs, analysis)

The wizard asks about scavenged parts and automatically determines
the appropriate tier, warns about edge cases, and generates
everything needed for the build.

Usage:
    python scripts/wizard.py              # Full interactive wizard
    python scripts/wizard.py --quick      # Quick mode with defaults
    python scripts/wizard.py --tier 3     # Force specific tier
"""

import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

# Add scripts directory to path
scripts_path = Path(__file__).parent
sys.path.insert(0, str(scripts_path))

from registry import (
    BOARDS, EXTRUDERS, BEDS, MOTORS, COMMON_BED_SIZES, MOTOR_SOURCES,
    get_board, get_extruder, get_bed,
    determine_tier, check_compatibility, get_tier_requirements,
    Severity,
)
from registry.motors import get_motor_count_for_tier


# =============================================================================
# TUI HELPERS
# =============================================================================

def print_header(title: str, char: str = "="):
    """Print a formatted header."""
    width = 65
    print(f"\n{char * width}")
    print(f" {title}")
    print(f"{char * width}")


def print_section(title: str):
    """Print a section header."""
    print(f"\n--- {title} ---")


def print_issue(severity, message: str, suggestion: str = None):
    """Print a compatibility issue with appropriate formatting."""
    icons = {
        Severity.INFO: "ℹ",
        Severity.WARNING: "⚠",
        Severity.ERROR: "✗",
    }
    icon = icons.get(severity, "•")
    print(f"  {icon} {message}")
    if suggestion:
        print(f"    → {suggestion}")


def get_input(prompt: str, default: str = None, valid_options: list = None) -> str:
    """Get user input with optional default and validation."""
    if default:
        prompt_str = f"{prompt} [{default}]: "
    else:
        prompt_str = f"{prompt}: "

    while True:
        value = input(prompt_str).strip()
        if not value and default:
            return default
        if valid_options and value.lower() not in [v.lower() for v in valid_options]:
            print(f"  Please choose from: {', '.join(valid_options)}")
            continue
        if value:
            return value
        if default:
            return default
        print("  Please enter a value")


def get_number(prompt: str, default: float = None, min_val: float = None, max_val: float = None) -> float:
    """Get numeric input with optional default and range validation."""
    while True:
        try:
            if default is not None:
                value = input(f"{prompt} [{default}]: ").strip()
                if not value:
                    return default
            else:
                value = input(f"{prompt}: ").strip()
            num = float(value)
            if min_val is not None and num < min_val:
                print(f"  Value must be at least {min_val}")
                continue
            if max_val is not None and num > max_val:
                print(f"  Value must be at most {max_val}")
                continue
            return num
        except ValueError:
            print("  Please enter a valid number")


def get_yes_no(prompt: str, default: bool = True) -> bool:
    """Get yes/no input."""
    default_str = "Y/n" if default else "y/N"
    while True:
        value = input(f"{prompt} [{default_str}]: ").strip().lower()
        if not value:
            return default
        if value in ["y", "yes"]:
            return True
        if value in ["n", "no"]:
            return False
        print("  Please enter y or n")


def select_from_list(prompt: str, options: dict, default: str = None) -> str:
    """Select from a dictionary of options."""
    print(f"\n{prompt}")
    keys = list(options.keys())
    for i, key in enumerate(keys, 1):
        value = options[key]
        if isinstance(value, tuple):
            display = f"{value[0]}x{value[1]} - {value[2]}" if len(value) >= 3 else str(value)
        elif hasattr(value, 'name'):
            display = value.name
        else:
            display = str(value)
        marker = " *" if key == default else ""
        print(f"  {i}. {key}: {display}{marker}")

    while True:
        choice = input(f"Enter number or ID [{default or 1}]: ").strip()
        if not choice:
            return default or keys[0]
        # Try as number
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(keys):
                return keys[idx]
        except ValueError:
            pass
        # Try as key
        if choice.upper() in [k.upper() for k in keys]:
            for k in keys:
                if k.upper() == choice.upper():
                    return k
        print(f"  Please enter a number 1-{len(keys)} or a valid ID")


# =============================================================================
# INVENTORY COLLECTION
# =============================================================================

@dataclass
class PartsInventory:
    """User's available parts."""
    # Motors
    motor_count: int
    motor_source: str  # "ender3", "cr10", "mixed", "purchase"
    extruder_motor_type: str  # "standard", "pancake", "nema14"

    # Boards
    board_ids: list[str]
    has_separate_host: bool  # Pi, CB1, old laptop

    # Bed
    bed_id: str
    bed_x: int
    bed_y: int

    # Rods
    smooth_rod_diameter: float  # 8, 10, or 12mm
    threaded_rod_type: str  # "M10" typically

    # Extruder
    extruder_id: str

    # Build height
    build_z: int

    # Export settings
    export_format: str = "stl"  # stl, step, 3mf, brep, gltf, all
    export_drawings: bool = False

    # Brand & cosmetics
    logo_pad_enabled: bool = True


def collect_inventory() -> PartsInventory:
    """Collect parts inventory from user through interactive prompts."""

    print_header("Parts Inventory")
    print("\nLet's figure out what you have to work with.")
    print("This will determine your build tier and configuration.\n")

    # --- Motors ---
    print_section("Stepper Motors")
    print("Motors are typically scavenged from donor printers.")
    print("Common sources:")
    for key, info in MOTOR_SOURCES.items():
        print(f"  {key}: {info['name']} ({info['motor_count']} motors)")

    motor_source = get_input(
        "Motor source",
        default="ender3",
        valid_options=list(MOTOR_SOURCES.keys()) + ["mixed", "purchase"],
    )

    if motor_source in MOTOR_SOURCES:
        motor_count = MOTOR_SOURCES[motor_source]["motor_count"]
        print(f"  → {motor_count} motors from {MOTOR_SOURCES[motor_source]['name']}")
    else:
        motor_count = int(get_number("How many motors total?", default=4, min_val=0, max_val=10))

    # Additional motors?
    extra = int(get_number("Any additional motors? (enter 0 if none)", default=0, min_val=0, max_val=10))
    motor_count += extra

    print(f"  → Total motors: {motor_count}")

    # Extruder motor type
    print("\nFor the extruder motor:")
    print("  1. standard: NEMA17 42x34mm (most common)")
    print("  2. pancake: NEMA17 42x25mm or shorter")
    print("  3. nema14: NEMA14 36mm frame (small)")

    extruder_motor = get_input(
        "Extruder motor type",
        default="standard",
        valid_options=["standard", "pancake", "nema14"],
    )

    # --- Control Board ---
    print_section("Control Board")
    print("What control board(s) will you use?")
    print("\nCommon options:")
    for bid, board in BOARDS.items():
        drivers = board.stepper_drivers
        host = " + integrated host" if board.integrated_host else ""
        source = " (donor)" if board.donor_common else ""
        print(f"  {bid}: {board.name} ({drivers} drivers{host}){source}")

    board_choice = select_from_list(
        "Select primary board:",
        {bid: board.name for bid, board in BOARDS.items()},
        default="CREALITY_V4",
    )
    board_ids = [board_choice]

    primary_board = BOARDS[board_choice]
    print(f"  → {primary_board.name}: {primary_board.stepper_drivers} drivers")

    # Check if need second board
    if primary_board.stepper_drivers < 6 and motor_count >= 6:
        print(f"\n  Note: {primary_board.name} has only {primary_board.stepper_drivers} drivers.")
        print("  For Triple-Z (6 motors), you may need a second board.")
        if get_yes_no("Add a second board?", default=True):
            secondary = select_from_list(
                "Select secondary board:",
                {bid: board.name for bid, board in BOARDS.items() if bid != board_choice},
                default="SKR_PICO",
            )
            board_ids.append(secondary)
            print(f"  → Added {BOARDS[secondary].name}")

    # Klipper host
    has_integrated_host = any(BOARDS[bid].integrated_host for bid in board_ids)
    if has_integrated_host:
        has_separate_host = False
        print("\n  ✓ Board has integrated Klipper host")
    else:
        print("\nKlipper needs a host computer (Pi, CB1, or old laptop).")
        has_separate_host = get_yes_no("Do you have a Klipper host?", default=True)

    # --- Heat Bed ---
    print_section("Heat Bed")
    print("What heated bed will you use?")

    bed_choice = select_from_list(
        "Select bed source:",
        {**COMMON_BED_SIZES, "other": (0, 0, "Other/Custom")},
        default="ender3",
    )

    if bed_choice == "other" or bed_choice == "custom":
        bed_x = int(get_number("Bed X dimension (mm)", default=235, min_val=100, max_val=500))
        bed_y = int(get_number("Bed Y dimension (mm)", default=235, min_val=100, max_val=500))
        bed_id = "CUSTOM"
    else:
        bed_x, bed_y, _ = COMMON_BED_SIZES[bed_choice]
        # Try to find matching bed spec
        bed_id = None
        for bid, bed in BEDS.items():
            if abs(bed.size_x - bed_x) <= 10 and abs(bed.size_y - bed_y) <= 10:
                bed_id = bid
                break
        if not bed_id:
            bed_id = "CUSTOM"

    print(f"  → Bed size: {bed_x}x{bed_y}mm")

    # Build height
    build_z = int(get_number("Build height Z (mm)", default=250, min_val=100, max_val=500))

    # --- Rods ---
    print_section("Smooth Rods")
    print("What diameter smooth rods will you use?")
    print("  8mm:  Minimum viable, limited with heavy toolheads")
    print("  10mm: REFERENCE SPEC - good balance")
    print("  12mm: Maximum rigidity, harder to source")

    smooth_rod = get_input(
        "Smooth rod diameter (mm)",
        default="10",
        valid_options=["8", "10", "12"],
    )
    smooth_rod_diameter = float(smooth_rod)

    # --- Extruder ---
    print_section("Extruder")
    print("What extruder will you use?")
    for eid, ext in EXTRUDERS.items():
        printable = " (printable)" if ext.printable else ""
        print(f"  {eid}: {ext.name} ({ext.mass_grams}g){printable}")

    extruder_id = select_from_list(
        "Select extruder:",
        {eid: f"{ext.name} ({ext.mass_grams}g)" for eid, ext in EXTRUDERS.items()},
        default="PITAN",
    )

    # --- Export Settings ---
    print_section("Export Settings")
    print("What format should parts be exported in?")
    print("  stl:   Standard 3D printing format (default)")
    print("  step:  CAD interchange (Fusion 360, FreeCAD, etc.)")
    print("  3mf:   Modern slicer format with metadata")
    print("  brep:  build123d native (exact geometry)")
    print("  gltf:  Web/3D viewer format")
    print("  all:   Export all formats")

    export_format = get_input(
        "Export format",
        default="stl",
        valid_options=["stl", "step", "3mf", "brep", "gltf", "all"],
    )

    export_drawings = get_yes_no("Generate technical drawings (SVG/PDF)?", default=False)

    # --- Brand & Cosmetics ---
    print_section("Brand & Cosmetics")
    print("Amalgam parts can include a raised logo pad on visible faces.")
    print("This is a 0.5mm raised octagon+A mark — swap to white filament")
    print("at that layer for the signature grey+white look. No MMU needed.")
    logo_pad = get_yes_no("Add logo pads to printed parts?", default=True)

    return PartsInventory(
        motor_count=motor_count,
        motor_source=motor_source,
        extruder_motor_type=extruder_motor,
        board_ids=board_ids,
        has_separate_host=has_separate_host,
        bed_id=bed_id,
        bed_x=bed_x,
        bed_y=bed_y,
        smooth_rod_diameter=smooth_rod_diameter,
        threaded_rod_type="M10",
        extruder_id=extruder_id,
        build_z=build_z,
        export_format=export_format,
        export_drawings=export_drawings,
        logo_pad_enabled=logo_pad,
    )


# =============================================================================
# TIER ANALYSIS
# =============================================================================

def analyze_tier(inventory: PartsInventory) -> tuple[int, list]:
    """Analyze inventory and determine recommended tier."""

    print_header("Tier Analysis")

    # Calculate total drivers
    total_drivers = sum(BOARDS[bid].stepper_drivers for bid in inventory.board_ids)

    # Determine tier
    result = determine_tier(
        motor_count=inventory.motor_count,
        driver_count=total_drivers,
        board_ids=inventory.board_ids,
        has_separate_host=inventory.has_separate_host,
    )

    print(f"\nYour inventory supports: Tier {result.recommended_tier}")
    tier_req = get_tier_requirements(result.recommended_tier)
    print(f"  → {tier_req.name}: {tier_req.description}")

    # Show tier breakdown
    print("\nTier qualification:")
    for tier in [1, 2, 3]:
        info = result.tier_breakdown.get(tier, {})
        status = "✓" if info.get("achievable") else "✗"
        req = get_tier_requirements(tier)
        print(f"  {status} Tier {tier} ({req.name})")
        for issue in info.get("issues", []):
            print(f"      {issue}")

    # Check component compatibility
    print_section("Compatibility Check")

    issues = check_compatibility(
        extruder_id=inventory.extruder_id,
        motor_type=inventory.extruder_motor_type,
        rod_diameter=inventory.smooth_rod_diameter,
        bed_size_x=inventory.bed_x,
        bed_size_y=inventory.bed_y,
    )

    # Add tier-specific issues
    issues.extend(result.issues)

    if issues:
        for issue in issues:
            print_issue(issue.severity, issue.message, issue.suggestion)
    else:
        print("  ✓ No compatibility issues detected")

    # Overall verdict
    errors = [i for i in issues if i.severity == Severity.ERROR]
    warnings = [i for i in issues if i.severity == Severity.WARNING]

    print_section("Verdict")
    if errors:
        print("  ✗ Configuration has blocking issues - resolve before building")
    elif warnings:
        print("  ~ Configuration will work but has some concerns")
        print("    Review warnings and run engineering analysis")
    else:
        print("  ✓ Configuration looks good!")

    return result.recommended_tier, issues


# =============================================================================
# CONFIG GENERATION
# =============================================================================

def generate_config(inventory: PartsInventory, tier: int) -> str:
    """Generate config.py content from inventory."""

    extruder = EXTRUDERS.get(inventory.extruder_id, EXTRUDERS["PITAN"])
    boards = [BOARDS[bid] for bid in inventory.board_ids]
    primary_board = boards[0]

    config = f'''"""
Amalgam Configuration
Generated by wizard.py

Tier: {tier} ({get_tier_requirements(tier).name})
"""

# =============================================================================
# 1. BUILD VOLUME
# =============================================================================

BUILD_VOLUME = {{
    "x": {inventory.bed_x},
    "y": {inventory.bed_y},
    "z": {inventory.build_z},
}}

# =============================================================================
# 2. FRAME SKELETON (M10 Rods)
# =============================================================================

# Threaded rods (frame structure)
M10_NOMINAL_DIA = 10.0
LUMPY_FACTOR = 0.5  # Tolerance for rod variation (0.2 zinc, 0.5+ galvanized)
M10_FIT_DIA = M10_NOMINAL_DIA + LUMPY_FACTOR

# Smooth rods (linear motion)
SMOOTH_ROD_DIA = {inventory.smooth_rod_diameter}
SMOOTH_ROD_FIT = SMOOTH_ROD_DIA + 0.1  # Tight fit for linear bearings

# =============================================================================
# 3. BED CONFIGURATION
# =============================================================================

BED_SIZE_X = {inventory.bed_x}
BED_SIZE_Y = {inventory.bed_y}
BED_ID = "{inventory.bed_id}"

# =============================================================================
# 4. EXTRUDER
# =============================================================================

EXTRUDER_TYPE = "{inventory.extruder_id}"
EXTRUDER_MASS = {extruder.mass_grams}  # grams (for analysis)
EXTRUDER_MOTOR = "{inventory.extruder_motor_type.upper()}"

# =============================================================================
# 5. CONTROL BOARD
# =============================================================================

PRIMARY_BOARD = "{primary_board.id}"
BOARD_IDS = {inventory.board_ids}
TOTAL_DRIVERS = {sum(b.stepper_drivers for b in boards)}

# =============================================================================
# 6. TIER CONFIGURATION
# =============================================================================

BUILD_TIER = {tier}
Z_CONFIGURATION = "{"triple" if tier >= 2 else "belt"}"  # triple or belt
HAS_CANBUS = {any(b.has_canbus for b in boards)}

# =============================================================================
# 7. HOTEND (Reference defaults)
# =============================================================================

HOTEND_TYPE = "E3D_V6_CLONE"
GROOVEMOUNT_DIA = 16.0  # E3D V6 groove diameter
HEATER_BLOCK = "E3D_V6"

# =============================================================================
# 8. DERIVED VALUES (calculated from above)
# =============================================================================

# Frame dimensions (calculated by analysis tool)
# These will be updated when you run: python scripts/analyze.py

FRAME_X = 0  # Set by analysis
FRAME_Y = 0  # Set by analysis
FRAME_Z = 0  # Set by analysis
X_SPAN = 0   # Smooth rod span (for sag calculation)

# =============================================================================
# 9. CAD PARAMETERS
# =============================================================================

# Tolerances for 3D printing
FIT_TOLERANCE = 0.2      # General fit tolerance
TIGHT_TOLERANCE = 0.1    # Tight fit (press-fit)
LOOSE_TOLERANCE = 0.4    # Loose fit (sliding)

# Printing parameters
MIN_WALL = 1.2           # Minimum wall thickness
MIN_FLOOR = 0.8          # Minimum floor thickness

# =============================================================================
# 10. EXPORT SETTINGS
# =============================================================================

# Default export format: stl, step, 3mf, brep, gltf, or all
EXPORT_FORMAT = "{inventory.export_format}"

# Generate technical drawings (orthographic projections as SVG/PDF)
EXPORT_DRAWINGS = {inventory.export_drawings}

# =============================================================================
# 11. BRAND & COSMETICS
# =============================================================================

# Official palette (hex). Feeds into exports, docs, and website.
BRAND_BODY_COLOR = "#4A4A4A"       # Dark Grey — printed parts
BRAND_ACCENT_COLOR = "#FFFFFF"     # White — logo pad / raised details
BRAND_BASE_COLOR = "#1A1A1A"       # Near-Black — MDF base, extrusions

# Logo pad on printed parts (raised 0.5mm for filament-swap color change)
LOGO_PAD_ENABLED = {inventory.logo_pad_enabled}
LOGO_PAD_DIAMETER = 18.0           # mm, across flats
LOGO_PAD_HEIGHT = 0.5              # mm raised above surface

# Texture (slicer recommendation, not enforced by geometry)
FUZZY_SKIN_RECOMMENDED = True
FUZZY_SKIN_POINT_DISTANCE = 0.3   # mm
FUZZY_SKIN_THICKNESS = 0.2        # mm
'''

    return config


# =============================================================================
# BUILD ORCHESTRATION
# =============================================================================

def run_analysis(inventory: PartsInventory):
    """Run engineering analysis."""
    print_header("Engineering Analysis")

    # Import analysis modules
    from analysis.rod_sag import calculate_rod_sag
    from analysis.frame_sizing import calculate_frame_size
    from analysis.acceleration import calculate_max_acceleration, get_klipper_settings

    extruder = EXTRUDERS.get(inventory.extruder_id, EXTRUDERS["PITAN"])

    # Frame sizing
    frame = calculate_frame_size(
        bed_x=inventory.bed_x,
        bed_y=inventory.bed_y,
        build_z=inventory.build_z,
        extruder_type=inventory.extruder_id,
        triple_z=inventory.motor_count >= 6,
    )

    print(f"\nFrame dimensions (internal):")
    print(f"  X: {frame.frame_x:.0f}mm")
    print(f"  Y: {frame.frame_y:.0f}mm")
    print(f"  Z: {frame.frame_z:.0f}mm")
    print(f"\nSmooth rod spans:")
    print(f"  X gantry: {frame.x_span:.0f}mm")
    print(f"  Y axis: {frame.y_span:.0f}mm")

    # Rod sag
    sag = calculate_rod_sag(
        rod_diameter=inventory.smooth_rod_diameter,
        span=frame.x_span,
        toolhead_mass=extruder.mass_grams,
    )

    print(f"\nRod Sag Analysis:")
    print(f"  Config: M{int(inventory.smooth_rod_diameter)} rods, {frame.x_span:.0f}mm span, {extruder.mass_grams}g toolhead")
    print(f"  Deflection: {sag.deflection:.4f}mm")
    print(f"  Verdict: {sag.verdict.upper()}")

    # Acceleration
    accel = calculate_max_acceleration(
        toolhead_mass=extruder.mass_grams,
        rod_diameter=inventory.smooth_rod_diameter,
        span=frame.x_span,
    )

    print(f"\nAcceleration Limits:")
    print(f"  Quality-focused: {accel.max_accel_for_quality:.0f} mm/s²")
    print(f"  Recommended: {accel.recommended_accel:.0f} mm/s²")
    print(f"  Velocity range: {accel.recommended_velocity}-{accel.max_velocity} mm/s")

    # Klipper settings
    klipper = get_klipper_settings(accel)
    print(f"\nRecommended Klipper Settings:")
    print(f"  max_velocity: {klipper['max_velocity']}")
    print(f"  max_accel: {klipper['max_accel']}")
    print(f"  max_accel_to_decel: {klipper['max_accel_to_decel']}")

    return frame, sag, accel


def run_wizard(quick: bool = False, force_tier: int = None, auto_save: bool = False):
    """Run the complete wizard flow."""

    print_header("Amalgam Configuration Wizard", "═")
    print("\nThis wizard will help you configure your Amalgam build.")
    print("It analyzes what parts you have and determines your build tier.\n")

    # Quick mode implies auto-save
    if quick:
        auto_save = True

    if quick:
        # Quick mode with reference spec defaults
        print("Running in quick mode with reference spec defaults...\n")
        inventory = PartsInventory(
            motor_count=6,
            motor_source="ender3",
            extruder_motor_type="standard",
            board_ids=["MKS_SKIPR"],
            has_separate_host=False,
            bed_id="ENDER3_BED",
            bed_x=235,
            bed_y=235,
            smooth_rod_diameter=10.0,
            threaded_rod_type="M10",
            extruder_id="PITAN",
            build_z=250,
            export_format="stl",
            export_drawings=False,
        )
    else:
        inventory = collect_inventory()

    # Analyze and determine tier
    tier, issues = analyze_tier(inventory)

    if force_tier is not None:
        print(f"\n  Note: Forcing Tier {force_tier} (was {tier})")
        tier = force_tier

    # Run engineering analysis
    frame, sag, accel = run_analysis(inventory)

    # Generate config
    print_header("Configuration")

    config_content = generate_config(inventory, tier)

    # Show summary
    print("\nConfiguration Summary:")
    print(f"  Tier: {tier} ({get_tier_requirements(tier).name})")
    print(f"  Bed: {inventory.bed_x}x{inventory.bed_y}mm")
    print(f"  Build height: {inventory.build_z}mm")
    print(f"  Smooth rods: M{int(inventory.smooth_rod_diameter)}")
    print(f"  Extruder: {inventory.extruder_id}")
    print(f"  Board(s): {', '.join(inventory.board_ids)}")
    print(f"  Export format: {inventory.export_format}")
    if inventory.export_drawings:
        print(f"  Technical drawings: enabled")

    # Ask to save
    print_section("Save Configuration")

    cad_path = scripts_path.parent / "cad"
    config_path = cad_path / "config.py"

    if config_path.exists() and not auto_save:
        print(f"  Note: {config_path} already exists")
        if not get_yes_no("Overwrite existing config?", default=False):
            print("  Config not saved. You can copy the output above manually.")
            return

    if config_path.exists():
        # Backup existing
        backup_path = config_path.with_suffix(".py.backup")
        import shutil
        shutil.copy(config_path, backup_path)
        print(f"  Backed up existing config to {backup_path.name}")

    print(f"\nSaving to: {config_path}")
    with open(config_path, "w") as f:
        f.write(config_content)
    print("  ✓ Configuration saved")

    # Next steps
    print_header("Next Steps")
    print("""
1. Review your config:
   cat cad/config.py

2. Run detailed analysis:
   python scripts/analyze.py

3. Build STL files:
   cd cad && ./build.sh build_all

4. Generate documentation:
   python scripts/export_config.py > docs/_variables.yml
   cd docs && quarto render
""")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Amalgam Configuration Wizard",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/wizard.py           Full interactive wizard
  python scripts/wizard.py --quick   Quick mode with reference spec
  python scripts/wizard.py --tier 2  Force specific tier
        """,
    )
    parser.add_argument(
        "--quick", "-q",
        action="store_true",
        help="Quick mode with reference spec defaults",
    )
    parser.add_argument(
        "--tier", "-t",
        type=int,
        choices=[1, 2, 3],
        help="Force specific tier (overrides auto-detection)",
    )

    args = parser.parse_args()

    try:
        run_wizard(quick=args.quick, force_tier=args.tier)
    except KeyboardInterrupt:
        print("\n\nWizard cancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
