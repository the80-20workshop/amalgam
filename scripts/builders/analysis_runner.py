"""
Analysis Runner for Amalgam

Runs engineering analysis and generates reports.
Wraps the analysis/ modules for programmatic use.
"""

import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from analysis.rod_sag import calculate_rod_sag, RodSagResult
from analysis.frame_sizing import calculate_frame_size, FrameSizeResult
from analysis.acceleration import (
    calculate_max_acceleration,
    get_klipper_settings,
    AccelerationResult,
)


@dataclass
class AnalysisReport:
    """Complete engineering analysis report."""
    # Input parameters
    bed_x: int
    bed_y: int
    build_z: int
    smooth_rod_diameter: float
    extruder_type: str
    extruder_mass: int

    # Results
    frame: FrameSizeResult
    sag: RodSagResult
    accel: AccelerationResult

    # Klipper settings
    klipper_settings: dict

    # Overall verdict
    verdict: str  # "good", "acceptable", "marginal", "review"
    recommendations: list[str]


def run_full_analysis(
    bed_x: int,
    bed_y: int,
    build_z: int,
    smooth_rod_diameter: float,
    extruder_type: str,
    extruder_mass: int,
    triple_z: bool = True,
) -> AnalysisReport:
    """
    Run complete engineering analysis.

    Args:
        bed_x: Bed X dimension in mm
        bed_y: Bed Y dimension in mm
        build_z: Build height in mm
        smooth_rod_diameter: Smooth rod diameter in mm
        extruder_type: Extruder type ID
        extruder_mass: Toolhead mass in grams
        triple_z: Whether using triple-Z configuration

    Returns:
        AnalysisReport with all results and recommendations
    """
    recommendations = []

    # Calculate frame sizing
    frame = calculate_frame_size(
        bed_x=bed_x,
        bed_y=bed_y,
        build_z=build_z,
        extruder_type=extruder_type,
        triple_z=triple_z,
    )

    # Calculate rod sag
    sag = calculate_rod_sag(
        rod_diameter=smooth_rod_diameter,
        span=frame.x_span,
        toolhead_mass=extruder_mass,
    )

    # Calculate acceleration limits
    accel = calculate_max_acceleration(
        toolhead_mass=extruder_mass,
        rod_diameter=smooth_rod_diameter,
        span=frame.x_span,
    )

    # Get Klipper settings
    klipper = get_klipper_settings(accel)

    # Determine overall verdict
    if sag.verdict in ["excellent", "good"] and accel.recommended_accel >= 2500:
        verdict = "good"
        recommendations.append("Configuration is well-balanced, proceed with confidence")
    elif sag.verdict == "acceptable" and accel.recommended_accel >= 1500:
        verdict = "acceptable"
        recommendations.append("Configuration will work well for most printing")
    elif sag.verdict == "marginal":
        verdict = "marginal"
        recommendations.append("Consider M10 rods for better rigidity")
        if smooth_rod_diameter == 8.0:
            recommendations.append("M8 rods may limit print quality at higher speeds")
    else:
        verdict = "review"
        recommendations.append("Review configuration - may have quality limitations")

    # Add specific recommendations based on analysis
    if sag.deflection > 0.02:
        if smooth_rod_diameter < 10:
            recommendations.append(f"M10 rods would reduce sag to ~{sag.deflection * 0.4:.4f}mm")
        if extruder_mass > 300:
            recommendations.append("Consider lighter extruder (Pitan: 280g)")

    if accel.recommended_accel < 2000:
        recommendations.append("Acceleration limited - focus on quality over speed")

    if frame.x_span > 300:
        recommendations.append("Long X span - ensure rod straightness")

    # Add frame notes
    recommendations.extend(frame.notes)

    return AnalysisReport(
        bed_x=bed_x,
        bed_y=bed_y,
        build_z=build_z,
        smooth_rod_diameter=smooth_rod_diameter,
        extruder_type=extruder_type,
        extruder_mass=extruder_mass,
        frame=frame,
        sag=sag,
        accel=accel,
        klipper_settings=klipper,
        verdict=verdict,
        recommendations=recommendations,
    )


def run_from_config(config: dict) -> AnalysisReport:
    """
    Run analysis using values from config.py.

    Args:
        config: Dictionary of config values

    Returns:
        AnalysisReport
    """
    # Extract values with defaults
    if "BUILD_VOLUME" in config:
        bv = config["BUILD_VOLUME"]
        bed_x = bv.get("x", 235)
        bed_y = bv.get("y", 235)
        build_z = bv.get("z", 250)
    else:
        bed_x = config.get("BED_SIZE_X", 235)
        bed_y = config.get("BED_SIZE_Y", 235)
        build_z = config.get("BUILD_Z", 250)

    smooth_rod_diameter = config.get("SMOOTH_ROD_DIA", 10.0)
    extruder_type = config.get("EXTRUDER_TYPE", "PITAN")
    extruder_mass = config.get("EXTRUDER_MASS", 280)

    z_config = config.get("Z_CONFIGURATION", "triple")
    triple_z = z_config == "triple"

    return run_full_analysis(
        bed_x=bed_x,
        bed_y=bed_y,
        build_z=build_z,
        smooth_rod_diameter=smooth_rod_diameter,
        extruder_type=extruder_type,
        extruder_mass=extruder_mass,
        triple_z=triple_z,
    )


def format_report(report: AnalysisReport) -> str:
    """
    Format analysis report as human-readable text.

    Args:
        report: AnalysisReport

    Returns:
        Formatted string
    """
    lines = [
        "=" * 60,
        " NEO-DARWIN ENGINEERING ANALYSIS",
        "=" * 60,
        "",
        "CONFIGURATION",
        f"  Bed: {report.bed_x}x{report.bed_y}mm",
        f"  Build height: {report.build_z}mm",
        f"  Smooth rods: M{int(report.smooth_rod_diameter)}",
        f"  Extruder: {report.extruder_type} ({report.extruder_mass}g)",
        "",
        "FRAME SIZING",
        f"  Frame dimensions: {report.frame.frame_x:.0f}x{report.frame.frame_y:.0f}x{report.frame.frame_z:.0f}mm",
        f"  X gantry span: {report.frame.x_span:.0f}mm",
        f"  Y axis span: {report.frame.y_span:.0f}mm",
        "",
        "ROD SAG ANALYSIS",
        f"  Deflection: {report.sag.deflection:.4f}mm",
        f"  Verdict: {report.sag.verdict.upper()}",
        "",
        "ACCELERATION LIMITS",
        f"  Quality-focused: {report.accel.max_accel_for_quality:.0f} mm/s²",
        f"  Structural max: {report.accel.max_accel_structural:.0f} mm/s²",
        f"  Recommended: {report.accel.recommended_accel:.0f} mm/s²",
        f"  Velocity range: {report.accel.recommended_velocity}-{report.accel.max_velocity} mm/s",
        "",
        "KLIPPER SETTINGS",
        f"  max_velocity: {report.klipper_settings['max_velocity']}",
        f"  max_accel: {report.klipper_settings['max_accel']}",
        f"  max_accel_to_decel: {report.klipper_settings['max_accel_to_decel']}",
        f"  square_corner_velocity: {report.klipper_settings['square_corner_velocity']}",
        "",
        "OVERALL VERDICT",
        f"  {report.verdict.upper()}",
        "",
        "RECOMMENDATIONS",
    ]

    for rec in report.recommendations:
        lines.append(f"  • {rec}")

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)


def update_config_with_frame(
    config_path: Path,
    frame: FrameSizeResult,
) -> None:
    """
    Update config.py with calculated frame dimensions.

    Args:
        config_path: Path to config.py
        frame: FrameSizeResult with calculated dimensions
    """
    content = config_path.read_text()

    # Update FRAME_X, FRAME_Y, FRAME_Z, X_SPAN
    replacements = [
        ("FRAME_X = 0", f"FRAME_X = {frame.frame_x:.0f}"),
        ("FRAME_Y = 0", f"FRAME_Y = {frame.frame_y:.0f}"),
        ("FRAME_Z = 0", f"FRAME_Z = {frame.frame_z:.0f}"),
        ("X_SPAN = 0", f"X_SPAN = {frame.x_span:.0f}"),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    config_path.write_text(content)
