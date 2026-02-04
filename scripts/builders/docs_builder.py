"""
Documentation Builder for Amalgam

Handles Quarto-based documentation generation:
1. Export config values to Quarto variables
2. Render documentation
3. Preview with live reload

Documentation is tier-aware and config-driven:
- Variables from config.py populate templates
- Tier-specific content via Quarto conditionals
- Board/extruder guides selected by configuration
"""

import subprocess
import sys
import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class DocsResult:
    """Result of a documentation operation."""
    success: bool
    output_dir: Optional[Path]
    message: str
    error: str


def get_docs_dir() -> Path:
    """Get the docs/ directory path."""
    scripts_dir = Path(__file__).parent.parent
    return scripts_dir.parent / "docs"


def get_cad_dir() -> Path:
    """Get the cad/ directory path."""
    scripts_dir = Path(__file__).parent.parent
    return scripts_dir.parent / "cad"


def load_config() -> dict:
    """Load config.py values."""
    config_path = get_cad_dir() / "config.py"

    if not config_path.exists():
        return {}

    config_globals = {}
    try:
        exec(config_path.read_text(), config_globals)
    except Exception:
        return {}

    # Filter to just our config values
    return {
        k: v for k, v in config_globals.items()
        if not k.startswith("_") and not callable(v) and k.isupper()
    }


def config_to_quarto_vars(config: dict) -> dict:
    """
    Convert config.py values to Quarto variable format.

    Quarto variables are accessed in .qmd files as {{< var name >}}

    Args:
        config: Dictionary of config values

    Returns:
        Dictionary suitable for _variables.yml
    """
    vars = {}

    # Build volume
    if "BUILD_VOLUME" in config:
        bv = config["BUILD_VOLUME"]
        vars["bed_x"] = bv.get("x", 235)
        vars["bed_y"] = bv.get("y", 235)
        vars["build_z"] = bv.get("z", 250)

    # Individual bed values (may override BUILD_VOLUME)
    if "BED_SIZE_X" in config:
        vars["bed_x"] = config["BED_SIZE_X"]
    if "BED_SIZE_Y" in config:
        vars["bed_y"] = config["BED_SIZE_Y"]

    # Rods
    vars["smooth_rod_dia"] = config.get("SMOOTH_ROD_DIA", 10.0)
    vars["m10_nominal"] = config.get("M10_NOMINAL_DIA", 10.0)

    # Extruder
    vars["extruder_type"] = config.get("EXTRUDER_TYPE", "PITAN")
    vars["extruder_mass"] = config.get("EXTRUDER_MASS", 280)

    # Board
    vars["primary_board"] = config.get("PRIMARY_BOARD", "MKS_SKIPR")
    vars["board_ids"] = config.get("BOARD_IDS", ["MKS_SKIPR"])
    vars["total_drivers"] = config.get("TOTAL_DRIVERS", 6)

    # Tier
    vars["tier"] = config.get("BUILD_TIER", 3)
    vars["z_config"] = config.get("Z_CONFIGURATION", "triple")
    vars["has_canbus"] = config.get("HAS_CANBUS", True)

    # Frame (may be 0 if not calculated yet)
    vars["frame_x"] = config.get("FRAME_X", 0)
    vars["frame_y"] = config.get("FRAME_Y", 0)
    vars["frame_z"] = config.get("FRAME_Z", 0)
    vars["x_span"] = config.get("X_SPAN", 0)

    # Hotend
    vars["hotend_type"] = config.get("HOTEND_TYPE", "E3D_V6_CLONE")
    vars["groovemount_dia"] = config.get("GROOVEMOUNT_DIA", 16.0)

    # Derived/computed values for templates
    vars["tier_name"] = _get_tier_name(vars["tier"])
    vars["z_type_desc"] = "Triple Independent Z" if vars["z_config"] == "triple" else "Belt-Driven Z"

    return vars


def _get_tier_name(tier: int) -> str:
    """Get human-readable tier name."""
    names = {
        0: "Klipper Only",
        1: "Single Donor",
        2: "Dual Donor",
        3: "Reference Spec",
        4: "Buy Everything",
    }
    return names.get(tier, f"Tier {tier}")


def export_quarto_vars(output_path: Optional[Path] = None) -> Path:
    """
    Export config values to Quarto variables file.

    Args:
        output_path: Path for _variables.yml (defaults to docs/_variables.yml)

    Returns:
        Path where variables were written
    """
    if output_path is None:
        output_path = get_docs_dir() / "_variables.yml"

    config = load_config()
    vars = config_to_quarto_vars(config)

    # Format as YAML
    content = yaml.dump(vars, default_flow_style=False, sort_keys=False)

    output_path.write_text(content)
    return output_path


def check_quarto_installed() -> bool:
    """Check if Quarto is installed and available."""
    try:
        result = subprocess.run(
            ["quarto", "--version"],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def build_docs(
    export_vars: bool = True,
    verbose: bool = False,
) -> DocsResult:
    """
    Build documentation using Quarto.

    Args:
        export_vars: Whether to export config to _variables.yml first
        verbose: Whether to print build output

    Returns:
        DocsResult with status and paths
    """
    docs_dir = get_docs_dir()

    if not check_quarto_installed():
        return DocsResult(
            success=False,
            output_dir=None,
            message="",
            error="Quarto not installed. Install from https://quarto.org",
        )

    # Export variables if requested
    if export_vars:
        try:
            vars_path = export_quarto_vars()
            if verbose:
                print(f"Exported variables to {vars_path}")
        except Exception as e:
            return DocsResult(
                success=False,
                output_dir=None,
                message="",
                error=f"Failed to export variables: {e}",
            )

    # Check for _quarto.yml
    quarto_config = docs_dir / "_quarto.yml"
    if not quarto_config.exists():
        return DocsResult(
            success=False,
            output_dir=None,
            message="",
            error=f"Quarto config not found: {quarto_config}",
        )

    # Run quarto render
    try:
        result = subprocess.run(
            ["quarto", "render"],
            cwd=docs_dir,
            capture_output=True,
            text=True,
            timeout=300,
        )

        if verbose:
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)

        output_dir = docs_dir / "_site"

        if result.returncode == 0:
            return DocsResult(
                success=True,
                output_dir=output_dir,
                message=f"Documentation built to {output_dir}",
                error="",
            )
        else:
            return DocsResult(
                success=False,
                output_dir=None,
                message="",
                error=result.stderr or "Quarto render failed",
            )

    except subprocess.TimeoutExpired:
        return DocsResult(
            success=False,
            output_dir=None,
            message="",
            error="Documentation build timed out",
        )
    except Exception as e:
        return DocsResult(
            success=False,
            output_dir=None,
            message="",
            error=str(e),
        )


def preview_docs(
    export_vars: bool = True,
    port: int = 4000,
) -> DocsResult:
    """
    Start Quarto preview server with live reload.

    Args:
        export_vars: Whether to export config to _variables.yml first
        port: Port for preview server

    Returns:
        DocsResult (note: this blocks until preview is stopped)
    """
    docs_dir = get_docs_dir()

    if not check_quarto_installed():
        return DocsResult(
            success=False,
            output_dir=None,
            message="",
            error="Quarto not installed",
        )

    # Export variables if requested
    if export_vars:
        try:
            export_quarto_vars()
        except Exception as e:
            return DocsResult(
                success=False,
                output_dir=None,
                message="",
                error=f"Failed to export variables: {e}",
            )

    # Run quarto preview (this blocks)
    try:
        print(f"Starting preview server on port {port}...")
        print("Press Ctrl+C to stop")

        subprocess.run(
            ["quarto", "preview", "--port", str(port)],
            cwd=docs_dir,
        )

        return DocsResult(
            success=True,
            output_dir=None,
            message="Preview stopped",
            error="",
        )

    except KeyboardInterrupt:
        return DocsResult(
            success=True,
            output_dir=None,
            message="Preview stopped by user",
            error="",
        )
    except Exception as e:
        return DocsResult(
            success=False,
            output_dir=None,
            message="",
            error=str(e),
        )


def get_docs_structure() -> dict:
    """
    Get the documentation structure.

    Returns:
        Dictionary describing available docs organized by category
    """
    docs_dir = get_docs_dir()

    structure = {
        "guides": [],
        "deep-dives": [],
        "adr": [],
        "reference": [],
    }

    # Find .qmd files
    for qmd_file in docs_dir.rglob("*.qmd"):
        rel_path = qmd_file.relative_to(docs_dir)

        # Categorize by parent directory
        if len(rel_path.parts) > 1:
            category = rel_path.parts[0]
            if category in structure:
                structure[category].append(rel_path.stem)

    return structure
