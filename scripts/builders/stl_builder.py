"""
STL Builder for Amalgam

Orchestrates CAD/STL generation using the existing cad/build.sh system.
Provides Python interface to the build system.

The actual CAD generation is handled by build123d scripts in cad/parts/.
This module wraps that system for programmatic access.
"""

import subprocess
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class BuildResult:
    """Result of a build operation."""
    success: bool
    parts_built: list[str]
    parts_failed: list[str]
    output: str
    error: str


def get_cad_dir() -> Path:
    """Get the cad/ directory path."""
    scripts_dir = Path(__file__).parent.parent
    return scripts_dir.parent / "cad"


def get_parts_dir() -> Path:
    """Get the cad/parts/ directory path."""
    return get_cad_dir() / "parts"


def get_stl_dir() -> Path:
    """Get the cad/exports/stl/ directory path."""
    return get_cad_dir() / "exports" / "stl"


def discover_parts() -> list[Path]:
    """
    Discover all buildable parts.

    Finds all Python files in cad/parts/ and subdirectories,
    excluding utilities/ and __pycache__/.

    Returns:
        List of Path objects to part scripts
    """
    parts_dir = get_parts_dir()

    if not parts_dir.exists():
        return []

    parts = []
    for py_file in parts_dir.rglob("*.py"):
        # Skip utilities and pycache
        if "utilities" in py_file.parts:
            continue
        if "__pycache__" in py_file.parts:
            continue
        if py_file.name.startswith("_"):
            continue
        parts.append(py_file)

    return sorted(parts)


def list_parts() -> dict[str, list[str]]:
    """
    List all available parts grouped by category.

    Returns:
        Dictionary mapping category to list of part names
    """
    parts = discover_parts()
    parts_dir = get_parts_dir()

    grouped = {}
    for part in parts:
        # Get relative path from parts/
        rel_path = part.relative_to(parts_dir)

        # Category is parent directory, or "root" if in parts/ directly
        if len(rel_path.parts) > 1:
            category = rel_path.parts[0]
        else:
            category = "root"

        if category not in grouped:
            grouped[category] = []

        grouped[category].append(part.stem)

    return grouped


def build_part(part_name: str, verbose: bool = False) -> BuildResult:
    """
    Build a single part by name.

    Args:
        part_name: Name of the part (without .py extension)
        verbose: Whether to print build output

    Returns:
        BuildResult with status and output
    """
    cad_dir = get_cad_dir()
    build_script = cad_dir / "build.sh"

    if not build_script.exists():
        return BuildResult(
            success=False,
            parts_built=[],
            parts_failed=[part_name],
            output="",
            error=f"Build script not found: {build_script}",
        )

    try:
        result = subprocess.run(
            ["./build.sh", "build", part_name],
            cwd=cad_dir,
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout per part
        )

        success = result.returncode == 0

        if verbose:
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)

        return BuildResult(
            success=success,
            parts_built=[part_name] if success else [],
            parts_failed=[] if success else [part_name],
            output=result.stdout,
            error=result.stderr,
        )

    except subprocess.TimeoutExpired:
        return BuildResult(
            success=False,
            parts_built=[],
            parts_failed=[part_name],
            output="",
            error=f"Build timed out for {part_name}",
        )
    except Exception as e:
        return BuildResult(
            success=False,
            parts_built=[],
            parts_failed=[part_name],
            output="",
            error=str(e),
        )


def build_stls(
    parts: Optional[list[str]] = None,
    verbose: bool = False,
    parallel: bool = False,
) -> BuildResult:
    """
    Build STL files.

    Args:
        parts: List of part names to build, or None for all
        verbose: Whether to print build output
        parallel: Whether to build in parallel (not yet implemented)

    Returns:
        BuildResult with overall status
    """
    cad_dir = get_cad_dir()
    build_script = cad_dir / "build.sh"

    if not build_script.exists():
        return BuildResult(
            success=False,
            parts_built=[],
            parts_failed=parts or ["all"],
            output="",
            error=f"Build script not found: {build_script}",
        )

    # If no parts specified, build all
    if parts is None:
        cmd = ["./build.sh", "build_all"]
    elif len(parts) == 1:
        cmd = ["./build.sh", "build", parts[0]]
    else:
        # Build each part
        all_built = []
        all_failed = []
        all_output = []
        all_errors = []

        for part in parts:
            result = build_part(part, verbose=verbose)
            all_built.extend(result.parts_built)
            all_failed.extend(result.parts_failed)
            all_output.append(result.output)
            all_errors.append(result.error)

        return BuildResult(
            success=len(all_failed) == 0,
            parts_built=all_built,
            parts_failed=all_failed,
            output="\n".join(all_output),
            error="\n".join(e for e in all_errors if e),
        )

    try:
        result = subprocess.run(
            cmd,
            cwd=cad_dir,
            capture_output=True,
            text=True,
            timeout=1800,  # 30 minute timeout for all parts
        )

        success = result.returncode == 0

        if verbose:
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)

        # Parse output to determine what was built
        # This is a simple heuristic - look for STL files in output dir
        stl_dir = get_stl_dir()
        built = [f.stem for f in stl_dir.glob("*.stl")] if stl_dir.exists() else []

        return BuildResult(
            success=success,
            parts_built=built,
            parts_failed=[] if success else ["unknown"],
            output=result.stdout,
            error=result.stderr,
        )

    except subprocess.TimeoutExpired:
        return BuildResult(
            success=False,
            parts_built=[],
            parts_failed=["all"],
            output="",
            error="Build timed out",
        )
    except Exception as e:
        return BuildResult(
            success=False,
            parts_built=[],
            parts_failed=["all"],
            output="",
            error=str(e),
        )


def clean_stls() -> bool:
    """
    Clean the STL output directory.

    Returns:
        True if successful
    """
    cad_dir = get_cad_dir()
    build_script = cad_dir / "build.sh"

    if not build_script.exists():
        return False

    try:
        result = subprocess.run(
            ["./build.sh", "clean"],
            cwd=cad_dir,
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except Exception:
        return False


def check_config_exists() -> bool:
    """Check if cad/config.py exists."""
    config_path = get_cad_dir() / "config.py"
    return config_path.exists()


def get_stl_files() -> list[Path]:
    """Get list of generated STL files."""
    stl_dir = get_stl_dir()
    if not stl_dir.exists():
        return []
    return sorted(stl_dir.glob("*.stl"))
