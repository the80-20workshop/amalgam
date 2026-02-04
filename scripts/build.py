#!/usr/bin/env python3
"""
Amalgam Master Build Script

Orchestrates all build systems:
1. Configuration (config.py generation)
2. Analysis (engineering verification)
3. STL Generation (CAD parts)
4. Documentation (Quarto website)

Usage:
    python scripts/build.py                    # Interactive wizard + build all
    python scripts/build.py --config-only      # Just generate config
    python scripts/build.py --stls             # Build STL files
    python scripts/build.py --docs             # Build documentation
    python scripts/build.py --analyze          # Run analysis only
    python scripts/build.py --all              # Build everything (non-interactive)

The build system follows Amalgam's principle of single source of truth:
config.py drives STL generation, documentation, and analysis.
"""

import sys
import argparse
from pathlib import Path

# Add scripts directory to path
scripts_path = Path(__file__).parent
sys.path.insert(0, str(scripts_path))


def print_header(title: str):
    """Print a formatted header."""
    width = 65
    print(f"\n{'=' * width}")
    print(f" {title}")
    print(f"{'=' * width}")


def print_step(num: int, title: str):
    """Print a step indicator."""
    print(f"\n[{num}] {title}")
    print("-" * 50)


def check_config_exists() -> bool:
    """Check if config.py exists."""
    config_path = scripts_path.parent / "cad" / "config.py"
    return config_path.exists()


def run_wizard():
    """Run the configuration wizard."""
    from wizard import run_wizard as wizard_run
    wizard_run()


def run_analysis(verbose: bool = True):
    """Run engineering analysis."""
    from builders import run_full_analysis
    from builders.config_builder import load_config

    if not check_config_exists():
        print("  ERROR: config.py not found. Run wizard first.")
        return None

    config = load_config()
    report = run_full_analysis(
        bed_x=config.get("BED_SIZE_X", config.get("BUILD_VOLUME", {}).get("x", 235)),
        bed_y=config.get("BED_SIZE_Y", config.get("BUILD_VOLUME", {}).get("y", 235)),
        build_z=config.get("BUILD_Z", config.get("BUILD_VOLUME", {}).get("z", 250)),
        smooth_rod_diameter=config.get("SMOOTH_ROD_DIA", 10.0),
        extruder_type=config.get("EXTRUDER_TYPE", "PITAN"),
        extruder_mass=config.get("EXTRUDER_MASS", 280),
        triple_z=config.get("Z_CONFIGURATION", "triple") == "triple",
    )

    if verbose:
        from builders.analysis_runner import format_report
        print(format_report(report))

    return report


def build_stls(verbose: bool = True):
    """Build STL files."""
    from builders import build_stls as stl_build

    if not check_config_exists():
        print("  ERROR: config.py not found. Run wizard first.")
        return False

    print("  Building STL files...")
    result = stl_build(verbose=verbose)

    if result.success:
        print(f"  SUCCESS: Built {len(result.parts_built)} parts")
        for part in result.parts_built[:10]:
            print(f"    - {part}")
        if len(result.parts_built) > 10:
            print(f"    ... and {len(result.parts_built) - 10} more")
    else:
        print(f"  FAILED: {result.error}")
        for part in result.parts_failed:
            print(f"    - {part}")

    return result.success


def build_docs(verbose: bool = True):
    """Build documentation."""
    from builders import export_quarto_vars, build_docs as docs_build

    if not check_config_exists():
        print("  ERROR: config.py not found. Run wizard first.")
        return False

    # Export variables
    print("  Exporting config to Quarto variables...")
    try:
        vars_path = export_quarto_vars()
        print(f"  Exported to {vars_path}")
    except Exception as e:
        print(f"  WARNING: Could not export variables: {e}")

    # Build docs
    print("  Building documentation with Quarto...")
    result = docs_build(export_vars=False, verbose=verbose)

    if result.success:
        print(f"  SUCCESS: Documentation built to {result.output_dir}")
    else:
        print(f"  FAILED: {result.error}")

    return result.success


def build_all(interactive: bool = True):
    """Build everything: config, analysis, STLs, docs."""

    print_header("Amalgam Complete Build")

    # Step 1: Configuration
    print_step(1, "Configuration")

    if not check_config_exists():
        if interactive:
            print("  No config.py found. Starting wizard...")
            run_wizard()
        else:
            print("  ERROR: config.py not found.")
            print("  Run 'python scripts/wizard.py' first.")
            return False
    else:
        print("  Using existing config.py")

    # Step 2: Analysis
    print_step(2, "Engineering Analysis")
    report = run_analysis(verbose=False)
    if report:
        print(f"  Verdict: {report.verdict.upper()}")
        print(f"  Rod sag: {report.sag.deflection:.4f}mm ({report.sag.verdict})")
        print(f"  Max accel: {report.accel.recommended_accel:.0f} mm/s²")
    else:
        print("  Analysis skipped (no config)")

    # Step 3: STL Generation
    print_step(3, "STL Generation")
    stl_success = build_stls(verbose=False)

    # Step 4: Documentation
    print_step(4, "Documentation")
    docs_success = build_docs(verbose=False)

    # Summary
    print_header("Build Summary")

    status = {
        "Config": "✓" if check_config_exists() else "✗",
        "Analysis": "✓" if report else "✗",
        "STLs": "✓" if stl_success else "✗",
        "Docs": "✓" if docs_success else "✗",
    }

    for component, icon in status.items():
        print(f"  {icon} {component}")

    all_success = all(s == "✓" for s in status.values())

    if all_success:
        print("\n  All builds completed successfully!")
        print("\n  Next steps:")
        print("    1. Review exports in cad/exports/")
        print("    2. Open docs/_site/index.html")
        print("    3. Run 'python scripts/analyze.py' for detailed analysis")
    else:
        print("\n  Some builds failed. Check errors above.")

    return all_success


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Amalgam Master Build Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/build.py                Full interactive build
  python scripts/build.py --all          Non-interactive full build
  python scripts/build.py --stls         Build STL files only
  python scripts/build.py --docs         Build documentation only
  python scripts/build.py --analyze      Run analysis only
  python scripts/build.py --wizard       Run configuration wizard
        """,
    )

    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Build everything (non-interactive)",
    )
    parser.add_argument(
        "--wizard", "-w",
        action="store_true",
        help="Run configuration wizard",
    )
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Run engineering analysis",
    )
    parser.add_argument(
        "--stls",
        action="store_true",
        help="Build STL files",
    )
    parser.add_argument(
        "--docs",
        action="store_true",
        help="Build documentation",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    try:
        # If no specific action, run interactive build
        if not any([args.all, args.wizard, args.analyze, args.stls, args.docs]):
            build_all(interactive=True)
            return

        # Specific actions
        if args.wizard:
            run_wizard()

        if args.analyze:
            print_step(1, "Engineering Analysis")
            run_analysis(verbose=True)

        if args.stls:
            print_step(1, "STL Generation")
            build_stls(verbose=args.verbose)

        if args.docs:
            print_step(1, "Documentation")
            build_docs(verbose=args.verbose)

        if args.all:
            build_all(interactive=False)

    except KeyboardInterrupt:
        print("\n\nBuild cancelled.")
        sys.exit(1)


if __name__ == "__main__":
    main()
