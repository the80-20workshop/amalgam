#!/usr/bin/env python3
"""
Amalgam Engineering Analysis TUI

An interactive tool to help builders assess their Amalgam
configuration before construction. Analyzes rod sag, frame sizing,
and acceleration limits.

Usage:
    python scripts/analyze.py              # Interactive TUI
    python scripts/analyze.py --quick      # Quick analysis with defaults
    python scripts/analyze.py --help       # Show help
"""

import sys
from pathlib import Path

# Add scripts directory to path
scripts_path = Path(__file__).parent
sys.path.insert(0, str(scripts_path))

from analysis.rod_sag import (
    calculate_rod_sag,
    compare_rod_options,
    get_extruder_mass,
    EXTRUDER_MASSES,
)
from analysis.frame_sizing import (
    calculate_frame_size,
    COMMON_BEDS,
)
from analysis.acceleration import (
    calculate_max_acceleration,
    get_klipper_settings,
)


def print_header(title: str):
    """Print a formatted header."""
    width = 60
    print("\n" + "=" * width)
    print(f" {title}")
    print("=" * width)


def print_section(title: str):
    """Print a section header."""
    print(f"\n--- {title} ---")


def get_input(prompt: str, default: str = None, valid_options: list = None) -> str:
    """Get user input with optional default and validation."""
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "

    while True:
        value = input(prompt).strip()
        if not value and default:
            return default
        if valid_options and value not in valid_options:
            print(f"  Please choose from: {', '.join(valid_options)}")
            continue
        if value:
            return value
        print("  Please enter a value")


def get_number(prompt: str, default: float = None) -> float:
    """Get numeric input with optional default."""
    while True:
        try:
            if default:
                value = input(f"{prompt} [{default}]: ").strip()
                if not value:
                    return default
            else:
                value = input(f"{prompt}: ").strip()
            return float(value)
        except ValueError:
            print("  Please enter a valid number")


def run_interactive():
    """Run the interactive TUI."""
    print_header("Amalgam Engineering Analysis")
    print("\nThis tool helps you assess your build configuration.")
    print("Answer the questions to get recommendations.\n")

    # Get bed size
    print_section("Heat Bed Size")
    print("Common options:")
    for key, (x, y, desc) in COMMON_BEDS.items():
        print(f"  {key}: {x}x{y}mm - {desc}")

    bed_choice = get_input(
        "Choose a bed or enter 'custom'",
        default="ender3",
        valid_options=list(COMMON_BEDS.keys()) + ["custom"],
    )

    if bed_choice == "custom":
        bed_x = get_number("Bed X dimension (mm)", 235)
        bed_y = get_number("Bed Y dimension (mm)", 235)
    else:
        bed_x, bed_y, _ = COMMON_BEDS[bed_choice]

    build_z = get_number("Build height Z (mm)", 250)

    # Get rod configuration
    print_section("Rod Configuration")
    smooth_rod = get_input(
        "Smooth rod diameter (mm)",
        default="10",
        valid_options=["8", "10", "12"],
    )
    smooth_rod = float(smooth_rod)

    # Get extruder type
    print_section("Extruder Selection")
    print("Options:")
    for ext, mass in EXTRUDER_MASSES.items():
        print(f"  {ext}: ~{mass}g")

    extruder = get_input(
        "Extruder type",
        default="PITAN",
        valid_options=list(EXTRUDER_MASSES.keys()),
    )
    toolhead_mass = get_extruder_mass(extruder)

    # Calculate frame size
    print_header("Frame Size Analysis")
    frame = calculate_frame_size(
        bed_x=bed_x,
        bed_y=bed_y,
        build_z=build_z,
        extruder_type=extruder,
        triple_z=True,
    )

    print(f"\nInput: {bed_x}x{bed_y}mm bed, {build_z}mm Z height")
    print(f"\nFrame dimensions (internal):")
    print(f"  X: {frame.frame_x:.0f}mm")
    print(f"  Y: {frame.frame_y:.0f}mm")
    print(f"  Z: {frame.frame_z:.0f}mm")
    print(f"\nM10 threaded rod lengths needed:")
    print(f"  X rods (4x): {frame.rod_x_length:.0f}mm")
    print(f"  Y rods (4x): {frame.rod_y_length:.0f}mm")
    print(f"  Z rods (4x): {frame.rod_z_length:.0f}mm")
    print(f"\nSmooth rod spans:")
    print(f"  X gantry: {frame.x_span:.0f}mm")
    print(f"  Y axis: {frame.y_span:.0f}mm")

    # Calculate rod sag
    print_header("Rod Sag Analysis")
    sag = calculate_rod_sag(
        rod_diameter=smooth_rod,
        span=frame.x_span,
        toolhead_mass=toolhead_mass,
    )

    print(f"\nConfiguration: M{int(smooth_rod)} rods, {frame.x_span:.0f}mm span, {toolhead_mass}g toolhead")
    print(f"\nDeflection: {sag.deflection:.4f}mm")
    print(f"Verdict: {sag.verdict.upper()}")
    print(f"\n{sag.recommendation}")

    # Compare rod options
    if smooth_rod == 8.0 and sag.verdict in ["marginal", "excessive"]:
        print_section("Rod Comparison")
        comparison = compare_rod_options(frame.x_span, toolhead_mass)
        print(f"\nAt {frame.x_span:.0f}mm span with {toolhead_mass}g toolhead:")
        for r in comparison:
            status = "✓" if r.verdict in ["excellent", "good", "acceptable"] else "✗"
            print(f"  M{int(r.rod_diameter)}: {r.deflection:.4f}mm - {r.verdict} {status}")

    # Calculate acceleration limits
    print_header("Acceleration Analysis")
    accel = calculate_max_acceleration(
        toolhead_mass=toolhead_mass,
        rod_diameter=smooth_rod,
        span=frame.x_span,
    )

    print(f"\nAcceleration limits:")
    print(f"  Quality-focused: {accel.max_accel_for_quality:.0f} mm/s²")
    print(f"  Structural max: {accel.max_accel_structural:.0f} mm/s²")
    print(f"  Recommended: {accel.recommended_accel:.0f} mm/s²")
    print(f"\nVelocity range: {accel.recommended_velocity}-{accel.max_velocity} mm/s")

    # Klipper settings
    klipper = get_klipper_settings(accel)
    print_section("Recommended Klipper Settings")
    print(f"""
[printer]
max_velocity: {klipper['max_velocity']}
max_accel: {klipper['max_accel']}
max_accel_to_decel: {klipper['max_accel_to_decel']}
square_corner_velocity: {klipper['square_corner_velocity']}
""")

    # Notes
    if frame.notes or accel.notes:
        print_header("Notes & Recommendations")
        for note in frame.notes:
            print(f"  • {note}")
        for note in accel.notes:
            print(f"  • {note}")

    # Overall assessment
    print_header("Overall Assessment")
    if sag.verdict in ["excellent", "good"] and accel.recommended_accel >= 2500:
        print("\n  ✓ GOOD: This configuration should perform well.")
        print("    Proceed with confidence.")
    elif sag.verdict == "acceptable" and accel.recommended_accel >= 1500:
        print("\n  ~ ACCEPTABLE: This configuration will work.")
        print("    Consider upgrades for demanding prints.")
    elif sag.verdict == "marginal":
        print("\n  ⚠ MARGINAL: Print quality may be affected.")
        print("    Strongly consider M10 rods or smaller bed.")
    else:
        print("\n  ✗ REVIEW NEEDED: Configuration has significant limitations.")
        print("    See recommendations above.")


def run_quick():
    """Run quick analysis with reference spec defaults."""
    print_header("Amalgam Quick Analysis (Reference Spec)")

    # Reference spec: 235x235 bed, Pitan, M10 rods
    bed_x, bed_y = 235, 235
    build_z = 250
    smooth_rod = 10.0
    extruder = "PITAN"
    toolhead_mass = get_extruder_mass(extruder)

    frame = calculate_frame_size(bed_x, bed_y, build_z, extruder)
    sag = calculate_rod_sag(smooth_rod, frame.x_span, toolhead_mass)
    accel = calculate_max_acceleration(toolhead_mass, smooth_rod, frame.x_span)

    print(f"""
Configuration:
  Bed: {bed_x}x{bed_y}mm
  Build height: {build_z}mm
  Smooth rods: M{int(smooth_rod)}
  Extruder: {extruder} ({toolhead_mass}g)

Results:
  Frame size: {frame.frame_x:.0f}x{frame.frame_y:.0f}x{frame.frame_z:.0f}mm
  X span: {frame.x_span:.0f}mm
  Rod deflection: {sag.deflection:.4f}mm ({sag.verdict})
  Max accel: {accel.recommended_accel:.0f} mm/s²
  Velocity: {accel.recommended_velocity}-{accel.max_velocity} mm/s

Verdict: Reference spec is well-engineered. ✓
""")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Amalgam Engineering Analysis Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/analyze.py           Interactive analysis
  python scripts/analyze.py --quick   Quick reference spec check
        """,
    )
    parser.add_argument(
        "--quick", "-q",
        action="store_true",
        help="Quick analysis with reference spec defaults",
    )

    args = parser.parse_args()

    try:
        if args.quick:
            run_quick()
        else:
            run_interactive()
    except KeyboardInterrupt:
        print("\n\nAnalysis cancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
