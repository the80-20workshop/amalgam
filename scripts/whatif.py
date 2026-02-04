#!/usr/bin/env python3
"""
Amalgam What-If Analysis

Explore trade-offs interactively before committing to a configuration.
Load your current config, tweak parameters, see the impact.

Usage:
    python scripts/whatif.py                    # Interactive exploration
    python scripts/whatif.py --rods 8           # Quick: what if M8 rods?
    python scripts/whatif.py --bed 200 200      # Quick: what if 200x200 bed?
    python scripts/whatif.py --extruder WADE    # Quick: what if Wade extruder?
    python scripts/whatif.py --compare          # Compare all rod options

This reads your current config.py, lets you explore changes,
and optionally updates config.py if you like what you see.
"""

import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from copy import deepcopy

# Add scripts directory to path
scripts_path = Path(__file__).parent
sys.path.insert(0, str(scripts_path))

from analysis.rod_sag import calculate_rod_sag, RodSagResult
from analysis.frame_sizing import calculate_frame_size, FrameSizeResult
from analysis.acceleration import calculate_max_acceleration, AccelerationResult
from registry import EXTRUDERS, get_extruder


# =============================================================================
# CONFIG LOADING
# =============================================================================

@dataclass
class ConfigSnapshot:
    """A snapshot of configuration values for comparison."""
    name: str
    bed_x: int
    bed_y: int
    build_z: int
    smooth_rod_dia: float
    extruder_type: str
    extruder_mass: int

    # Calculated results (filled by analyze)
    frame: Optional[FrameSizeResult] = None
    sag: Optional[RodSagResult] = None
    accel: Optional[AccelerationResult] = None


def load_current_config() -> ConfigSnapshot:
    """Load current config.py values."""
    cad_path = scripts_path.parent / "cad"
    config_path = cad_path / "config.py"

    # Defaults if no config
    defaults = ConfigSnapshot(
        name="Current",
        bed_x=235,
        bed_y=235,
        build_z=250,
        smooth_rod_dia=10.0,
        extruder_type="PITAN",
        extruder_mass=280,
    )

    if not config_path.exists():
        print("  Note: No config.py found, using defaults")
        return defaults

    try:
        config_globals = {}
        exec(config_path.read_text(), config_globals)

        # Extract values
        build_volume = config_globals.get("BUILD_VOLUME", {})

        return ConfigSnapshot(
            name="Current",
            bed_x=config_globals.get("BED_SIZE_X", build_volume.get("x", 235)),
            bed_y=config_globals.get("BED_SIZE_Y", build_volume.get("y", 235)),
            build_z=build_volume.get("z", config_globals.get("BUILD_Z", 250)),
            smooth_rod_dia=config_globals.get("SMOOTH_ROD_DIA", 10.0),
            extruder_type=config_globals.get("EXTRUDER_TYPE", "PITAN"),
            extruder_mass=config_globals.get("EXTRUDER_MASS", 280),
        )
    except Exception as e:
        print(f"  Warning: Could not load config.py: {e}")
        return defaults


def analyze_config(config: ConfigSnapshot) -> ConfigSnapshot:
    """Run analysis on a config snapshot."""
    config.frame = calculate_frame_size(
        bed_x=config.bed_x,
        bed_y=config.bed_y,
        build_z=config.build_z,
        extruder_type=config.extruder_type,
    )

    config.sag = calculate_rod_sag(
        rod_diameter=config.smooth_rod_dia,
        span=config.frame.x_span,
        toolhead_mass=config.extruder_mass,
    )

    config.accel = calculate_max_acceleration(
        toolhead_mass=config.extruder_mass,
        rod_diameter=config.smooth_rod_dia,
        span=config.frame.x_span,
    )

    return config


# =============================================================================
# COMPARISON DISPLAY
# =============================================================================

def print_header(title: str):
    """Print a formatted header."""
    width = 70
    print(f"\n{'=' * width}")
    print(f" {title}")
    print(f"{'=' * width}")


def print_comparison(original: ConfigSnapshot, modified: ConfigSnapshot):
    """Print side-by-side comparison of two configurations."""

    # Ensure both are analyzed
    if not original.frame:
        original = analyze_config(original)
    if not modified.frame:
        modified = analyze_config(modified)

    print_header(f"Comparison: {original.name} vs {modified.name}")

    # Configuration differences
    print("\n  CONFIGURATION")
    print(f"  {'Parameter':<20} {'Current':<20} {'Modified':<20} {'Change':<10}")
    print(f"  {'-'*70}")

    def show_param(name, orig_val, mod_val, unit=""):
        if orig_val != mod_val:
            change = "← CHANGED"
        else:
            change = ""
        print(f"  {name:<20} {str(orig_val)+unit:<20} {str(mod_val)+unit:<20} {change}")

    show_param("Bed X", original.bed_x, modified.bed_x, "mm")
    show_param("Bed Y", original.bed_y, modified.bed_y, "mm")
    show_param("Build Z", original.build_z, modified.build_z, "mm")
    show_param("Smooth Rods", f"M{int(original.smooth_rod_dia)}", f"M{int(modified.smooth_rod_dia)}")
    show_param("Extruder", original.extruder_type, modified.extruder_type)
    show_param("Toolhead Mass", original.extruder_mass, modified.extruder_mass, "g")

    # Frame dimensions
    print("\n  FRAME DIMENSIONS")
    print(f"  {'Dimension':<20} {'Current':<20} {'Modified':<20} {'Delta':<10}")
    print(f"  {'-'*70}")

    def show_dim(name, orig_val, mod_val):
        delta = mod_val - orig_val
        delta_str = f"{delta:+.0f}mm" if delta != 0 else "-"
        print(f"  {name:<20} {orig_val:<20.0f} {mod_val:<20.0f} {delta_str}")

    show_dim("Frame X", original.frame.frame_x, modified.frame.frame_x)
    show_dim("Frame Y", original.frame.frame_y, modified.frame.frame_y)
    show_dim("Frame Z", original.frame.frame_z, modified.frame.frame_z)
    show_dim("X Span", original.frame.x_span, modified.frame.x_span)

    # Engineering results
    print("\n  ENGINEERING ANALYSIS")
    print(f"  {'Metric':<20} {'Current':<20} {'Modified':<20} {'Impact':<15}")
    print(f"  {'-'*70}")

    # Rod sag
    orig_sag = original.sag.deflection
    mod_sag = modified.sag.deflection
    sag_ratio = mod_sag / orig_sag if orig_sag > 0 else 1
    if sag_ratio > 1.2:
        sag_impact = f"↑ {sag_ratio:.1f}x WORSE"
    elif sag_ratio < 0.8:
        sag_impact = f"↓ {1/sag_ratio:.1f}x better"
    else:
        sag_impact = "~ similar"

    print(f"  {'Rod Deflection':<20} {orig_sag:.4f}mm ({original.sag.verdict:<8}) {mod_sag:.4f}mm ({modified.sag.verdict:<8}) {sag_impact}")

    # Acceleration
    orig_accel = original.accel.recommended_accel
    mod_accel = modified.accel.recommended_accel
    accel_diff = mod_accel - orig_accel
    if accel_diff > 500:
        accel_impact = f"↑ +{accel_diff:.0f} faster"
    elif accel_diff < -500:
        accel_impact = f"↓ {accel_diff:.0f} slower"
    else:
        accel_impact = "~ similar"

    print(f"  {'Max Accel':<20} {orig_accel:<20.0f} {mod_accel:<20.0f} {accel_impact}")

    # Velocity
    orig_vel = f"{original.accel.recommended_velocity}-{original.accel.max_velocity}"
    mod_vel = f"{modified.accel.recommended_velocity}-{modified.accel.max_velocity}"
    print(f"  {'Velocity (mm/s)':<20} {orig_vel:<20} {mod_vel:<20}")

    # Verdict
    print("\n  VERDICT")

    # Overall assessment
    issues = []
    benefits = []

    if mod_sag > orig_sag * 1.5:
        issues.append(f"Deflection increases {sag_ratio:.1f}x - may affect print quality")
    elif mod_sag < orig_sag * 0.7:
        benefits.append(f"Deflection decreases to {mod_sag:.4f}mm - better rigidity")

    if mod_accel < orig_accel - 1000:
        issues.append(f"Acceleration drops {abs(accel_diff):.0f} mm/s² - slower prints")
    elif mod_accel > orig_accel + 1000:
        benefits.append(f"Acceleration increases {accel_diff:.0f} mm/s² - faster prints")

    if modified.sag.verdict in ["marginal", "excessive"]:
        issues.append(f"Rod sag rated '{modified.sag.verdict}' - consider alternatives")

    if benefits:
        print("  Benefits:")
        for b in benefits:
            print(f"    ✓ {b}")

    if issues:
        print("  Concerns:")
        for i in issues:
            print(f"    ⚠ {i}")

    if not issues and not benefits:
        print("    ~ Changes have minimal impact on performance")

    return modified


def print_multi_comparison(configs: list[ConfigSnapshot]):
    """Print comparison of multiple configurations."""

    # Analyze all
    for config in configs:
        if not config.frame:
            analyze_config(config)

    print_header("Multi-Configuration Comparison")

    # Header row
    names = [c.name for c in configs]
    header = f"  {'Metric':<25}" + "".join(f"{n:<15}" for n in names)
    print(f"\n{header}")
    print(f"  {'-' * (25 + 15 * len(configs))}")

    # Rows
    def row(label, values):
        print(f"  {label:<25}" + "".join(f"{v:<15}" for v in values))

    row("Bed Size", [f"{c.bed_x}x{c.bed_y}" for c in configs])
    row("Smooth Rods", [f"M{int(c.smooth_rod_dia)}" for c in configs])
    row("Extruder", [c.extruder_type for c in configs])
    row("X Span (mm)", [f"{c.frame.x_span:.0f}" for c in configs])
    row("Deflection (mm)", [f"{c.sag.deflection:.4f}" for c in configs])
    row("Sag Verdict", [c.sag.verdict for c in configs])
    row("Max Accel (mm/s²)", [f"{c.accel.recommended_accel:.0f}" for c in configs])
    row("Velocity (mm/s)", [f"{c.accel.recommended_velocity}-{c.accel.max_velocity}" for c in configs])

    # Find best for each metric
    print(f"\n  RECOMMENDATIONS")

    min_sag = min(configs, key=lambda c: c.sag.deflection)
    max_accel = max(configs, key=lambda c: c.accel.recommended_accel)

    print(f"    Lowest deflection: {min_sag.name} ({min_sag.sag.deflection:.4f}mm)")
    print(f"    Highest accel: {max_accel.name} ({max_accel.accel.recommended_accel:.0f} mm/s²)")


# =============================================================================
# WHAT-IF SCENARIOS
# =============================================================================

def whatif_rods(current: ConfigSnapshot, new_diameter: float) -> ConfigSnapshot:
    """What if we change rod diameter?"""
    modified = ConfigSnapshot(
        name=f"M{int(new_diameter)} Rods",
        bed_x=current.bed_x,
        bed_y=current.bed_y,
        build_z=current.build_z,
        smooth_rod_dia=new_diameter,
        extruder_type=current.extruder_type,
        extruder_mass=current.extruder_mass,
    )
    return print_comparison(current, modified)


def whatif_bed(current: ConfigSnapshot, new_x: int, new_y: int) -> ConfigSnapshot:
    """What if we change bed size?"""
    modified = ConfigSnapshot(
        name=f"{new_x}x{new_y} Bed",
        bed_x=new_x,
        bed_y=new_y,
        build_z=current.build_z,
        smooth_rod_dia=current.smooth_rod_dia,
        extruder_type=current.extruder_type,
        extruder_mass=current.extruder_mass,
    )
    return print_comparison(current, modified)


def whatif_extruder(current: ConfigSnapshot, new_extruder: str) -> ConfigSnapshot:
    """What if we change extruder?"""
    ext = get_extruder(new_extruder)
    if not ext:
        print(f"  Unknown extruder: {new_extruder}")
        print(f"  Available: {', '.join(EXTRUDERS.keys())}")
        return current

    modified = ConfigSnapshot(
        name=f"{new_extruder}",
        bed_x=current.bed_x,
        bed_y=current.bed_y,
        build_z=current.build_z,
        smooth_rod_dia=current.smooth_rod_dia,
        extruder_type=new_extruder,
        extruder_mass=ext.mass_grams,
    )
    return print_comparison(current, modified)


def compare_all_rods(current: ConfigSnapshot):
    """Compare M8, M10, M12 rods."""
    configs = []
    for dia in [8.0, 10.0, 12.0]:
        config = ConfigSnapshot(
            name=f"M{int(dia)}",
            bed_x=current.bed_x,
            bed_y=current.bed_y,
            build_z=current.build_z,
            smooth_rod_dia=dia,
            extruder_type=current.extruder_type,
            extruder_mass=current.extruder_mass,
        )
        analyze_config(config)
        configs.append(config)

    print_multi_comparison(configs)


def compare_all_extruders(current: ConfigSnapshot):
    """Compare all available extruders."""
    configs = []
    for ext_id, ext in EXTRUDERS.items():
        config = ConfigSnapshot(
            name=ext_id,
            bed_x=current.bed_x,
            bed_y=current.bed_y,
            build_z=current.build_z,
            smooth_rod_dia=current.smooth_rod_dia,
            extruder_type=ext_id,
            extruder_mass=ext.mass_grams,
        )
        analyze_config(config)
        configs.append(config)

    print_multi_comparison(configs)


def compare_bed_sizes(current: ConfigSnapshot):
    """Compare common bed sizes."""
    beds = [
        (200, 200, "200x200"),
        (220, 220, "Ender 5"),
        (235, 235, "Ender 3"),
        (250, 210, "Prusa MK3"),
        (300, 300, "CR-10"),
    ]

    configs = []
    for x, y, name in beds:
        config = ConfigSnapshot(
            name=name,
            bed_x=x,
            bed_y=y,
            build_z=current.build_z,
            smooth_rod_dia=current.smooth_rod_dia,
            extruder_type=current.extruder_type,
            extruder_mass=current.extruder_mass,
        )
        analyze_config(config)
        configs.append(config)

    print_multi_comparison(configs)


# =============================================================================
# CONFIG UPDATE
# =============================================================================

def update_config(modified: ConfigSnapshot) -> bool:
    """Update config.py with modified values."""
    cad_path = scripts_path.parent / "cad"
    config_path = cad_path / "config.py"

    if not config_path.exists():
        print("  No config.py to update. Run wizard first.")
        return False

    content = config_path.read_text()

    # Simple replacements - look for the patterns
    replacements = [
        (f'BED_SIZE_X = ', f'BED_SIZE_X = {modified.bed_x}'),
        (f'BED_SIZE_Y = ', f'BED_SIZE_Y = {modified.bed_y}'),
        (f'SMOOTH_ROD_DIA = ', f'SMOOTH_ROD_DIA = {modified.smooth_rod_dia}'),
        (f'EXTRUDER_TYPE = ', f'EXTRUDER_TYPE = "{modified.extruder_type}"'),
        (f'EXTRUDER_MASS = ', f'EXTRUDER_MASS = {modified.extruder_mass}'),
    ]

    # Also update BUILD_VOLUME if present
    import re

    # Update BED_SIZE_X/Y
    content = re.sub(r'BED_SIZE_X = \d+', f'BED_SIZE_X = {modified.bed_x}', content)
    content = re.sub(r'BED_SIZE_Y = \d+', f'BED_SIZE_Y = {modified.bed_y}', content)
    content = re.sub(r'SMOOTH_ROD_DIA = [\d.]+', f'SMOOTH_ROD_DIA = {modified.smooth_rod_dia}', content)
    content = re.sub(r'EXTRUDER_TYPE = "[^"]+"', f'EXTRUDER_TYPE = "{modified.extruder_type}"', content)
    content = re.sub(r'EXTRUDER_MASS = \d+', f'EXTRUDER_MASS = {modified.extruder_mass}', content)

    # Update BUILD_VOLUME dict
    content = re.sub(r'"x": \d+', f'"x": {modified.bed_x}', content)
    content = re.sub(r'"y": \d+', f'"y": {modified.bed_y}', content)

    # Backup and write
    backup_path = config_path.with_suffix(".py.backup")
    import shutil
    shutil.copy(config_path, backup_path)

    config_path.write_text(content)
    print(f"  ✓ Updated config.py (backup at {backup_path.name})")
    return True


# =============================================================================
# INTERACTIVE MODE
# =============================================================================

def get_input(prompt: str, default: str = None) -> str:
    """Get user input with optional default."""
    if default:
        value = input(f"{prompt} [{default}]: ").strip()
        return value if value else default
    return input(f"{prompt}: ").strip()


def get_number(prompt: str, default: float = None) -> float:
    """Get numeric input."""
    while True:
        try:
            if default is not None:
                value = input(f"{prompt} [{default}]: ").strip()
                if not value:
                    return default
            else:
                value = input(f"{prompt}: ").strip()
            return float(value)
        except ValueError:
            print("  Please enter a valid number")


def run_interactive():
    """Run interactive what-if exploration."""

    print_header("Amalgam What-If Analysis")
    print("\nExplore trade-offs before committing to a configuration.")

    current = load_current_config()
    analyze_config(current)

    print(f"\nCurrent configuration:")
    print(f"  Bed: {current.bed_x}x{current.bed_y}mm")
    print(f"  Smooth rods: M{int(current.smooth_rod_dia)}")
    print(f"  Extruder: {current.extruder_type} ({current.extruder_mass}g)")
    print(f"  Rod deflection: {current.sag.deflection:.4f}mm ({current.sag.verdict})")
    print(f"  Max accel: {current.accel.recommended_accel:.0f} mm/s²")

    modified = None

    while True:
        print("\nWhat would you like to explore?")
        print("  1. Change rod diameter (M8/M10/M12)")
        print("  2. Change bed size")
        print("  3. Change extruder")
        print("  4. Compare all rod options")
        print("  5. Compare all extruders")
        print("  6. Compare common bed sizes")
        print("  7. Apply last change to config.py")
        print("  8. Exit")

        choice = get_input("\nChoice", "8")

        if choice == "1":
            print("\n  Rod options: 8, 10, 12")
            dia = get_number("  New diameter", current.smooth_rod_dia)
            modified = whatif_rods(current, dia)

        elif choice == "2":
            print("\n  Common sizes: 200x200, 220x220, 235x235, 250x210, 300x300")
            x = int(get_number("  New bed X", current.bed_x))
            y = int(get_number("  New bed Y", current.bed_y))
            modified = whatif_bed(current, x, y)

        elif choice == "3":
            print(f"\n  Available: {', '.join(EXTRUDERS.keys())}")
            ext = get_input("  New extruder", current.extruder_type).upper()
            modified = whatif_extruder(current, ext)

        elif choice == "4":
            compare_all_rods(current)

        elif choice == "5":
            compare_all_extruders(current)

        elif choice == "6":
            compare_bed_sizes(current)

        elif choice == "7":
            if modified:
                confirm = get_input(f"  Update config.py with {modified.name}? (y/n)", "n")
                if confirm.lower() == "y":
                    update_config(modified)
                    current = modified  # New baseline
            else:
                print("  No changes to apply. Explore an option first.")

        elif choice == "8":
            print("\nExiting what-if analysis.")
            break

        else:
            print("  Invalid choice")


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Amalgam What-If Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/whatif.py                    Interactive mode
  python scripts/whatif.py --rods 8           What if M8 rods?
  python scripts/whatif.py --bed 200 200      What if 200x200 bed?
  python scripts/whatif.py --extruder WADE    What if Wade extruder?
  python scripts/whatif.py --compare-rods     Compare M8/M10/M12
  python scripts/whatif.py --compare-beds     Compare common bed sizes
        """,
    )

    parser.add_argument("--rods", type=float, help="What if this rod diameter?")
    parser.add_argument("--bed", type=int, nargs=2, metavar=("X", "Y"), help="What if this bed size?")
    parser.add_argument("--extruder", type=str, help="What if this extruder?")
    parser.add_argument("--compare-rods", action="store_true", help="Compare all rod options")
    parser.add_argument("--compare-extruders", action="store_true", help="Compare all extruders")
    parser.add_argument("--compare-beds", action="store_true", help="Compare common bed sizes")
    parser.add_argument("--apply", action="store_true", help="Apply changes to config.py")

    args = parser.parse_args()

    # If no args, run interactive
    if not any([args.rods, args.bed, args.extruder, args.compare_rods, args.compare_extruders, args.compare_beds]):
        try:
            run_interactive()
        except KeyboardInterrupt:
            print("\n\nExiting.")
        return

    # Quick mode
    current = load_current_config()
    analyze_config(current)
    modified = None

    if args.compare_rods:
        compare_all_rods(current)
    elif args.compare_extruders:
        compare_all_extruders(current)
    elif args.compare_beds:
        compare_bed_sizes(current)
    elif args.rods:
        modified = whatif_rods(current, args.rods)
    elif args.bed:
        modified = whatif_bed(current, args.bed[0], args.bed[1])
    elif args.extruder:
        modified = whatif_extruder(current, args.extruder.upper())

    # Apply if requested
    if args.apply and modified:
        update_config(modified)


if __name__ == "__main__":
    main()
