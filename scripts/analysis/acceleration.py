"""
Acceleration Limits Calculator for Amalgam

Calculates maximum safe acceleration based on toolhead mass
and frame/rod stiffness. Helps builders understand the
relationship between mass and motion performance.

Key insight from MANIFESTO:
    Acceleration loads equal gravity loads at modern motion settings.
    With a realistic direct-drive toolhead (~280g for Pitan), inertial
    forces at 8-10k mm/s² match or exceed static sag forces.
"""

import math
from dataclasses import dataclass
from typing import Optional


@dataclass
class AccelerationResult:
    """Result of acceleration limit calculation."""

    toolhead_mass: float  # grams
    rod_diameter: float  # mm
    span: float  # mm

    # Calculated limits
    max_accel_for_quality: float  # mm/s² - quality-focused limit
    max_accel_structural: float  # mm/s² - structural limit
    recommended_accel: float  # mm/s² - recommended setting

    # Speed recommendations
    recommended_velocity: float  # mm/s
    max_velocity: float  # mm/s

    notes: list[str]


# Physics constants
GRAVITY = 9810  # mm/s² (9.81 m/s² in mm)


def calculate_max_acceleration(
    toolhead_mass: float,
    rod_diameter: float,
    span: float,
    max_deflection: float = 0.025,
) -> AccelerationResult:
    """
    Calculate maximum safe acceleration for print quality.

    The key insight is that acceleration-induced rod bending equals
    gravity-induced sag when accel ≈ 1g (9810 mm/s²). For quality
    printing, we want total deflection (static + dynamic) to remain
    below acceptable thresholds.

    Args:
        toolhead_mass: Toolhead mass in grams
        rod_diameter: Smooth rod diameter in mm
        span: Unsupported span in mm
        max_deflection: Maximum acceptable total deflection in mm

    Returns:
        AccelerationResult with limits and recommendations
    """
    from .rod_sag import calculate_rod_sag

    notes = []

    # Calculate static sag first
    static_result = calculate_rod_sag(rod_diameter, span, toolhead_mass)
    static_sag = static_result.deflection

    # Available deflection budget for dynamic loading
    dynamic_budget = max_deflection - static_sag

    if dynamic_budget <= 0:
        # Already at or over budget from static load alone
        max_accel_quality = 500  # Minimum usable
        notes.append("WARNING: Static sag already exceeds quality threshold")
        notes.append("Upgrade rods or reduce toolhead mass")
    else:
        # Acceleration that would cause dynamic_budget deflection
        # Since deflection ∝ force ∝ mass × accel, and static is mass × g:
        # dynamic_deflection / static_sag = accel / g
        # accel = g × (dynamic_budget / static_sag)
        if static_sag > 0:
            accel_ratio = dynamic_budget / static_sag
            max_accel_quality = GRAVITY * accel_ratio
        else:
            max_accel_quality = 15000  # Very stiff, high limit

    # Structural limit (more generous, based on rod yield strength)
    # This is a simplified estimate - real limit depends on many factors
    # Rule of thumb: M8 ≈ 5000, M10 ≈ 10000, M12 ≈ 15000 mm/s²
    structural_limits = {
        8.0: 5000,
        10.0: 10000,
        12.0: 15000,
    }
    max_accel_structural = structural_limits.get(
        rod_diameter,
        8000  # Default for unknown sizes
    )

    # Take the more conservative of quality and structural limits
    effective_max = min(max_accel_quality, max_accel_structural)

    # Recommended is 70% of max for safety margin
    recommended_accel = effective_max * 0.7

    # Velocity recommendations based on Amalgam philosophy
    # Target 70-120mm/s for quality, can push higher if system allows
    if recommended_accel >= 3000:
        recommended_velocity = 100
        max_velocity = 150
    elif recommended_accel >= 2000:
        recommended_velocity = 80
        max_velocity = 120
    elif recommended_accel >= 1000:
        recommended_velocity = 60
        max_velocity = 100
    else:
        recommended_velocity = 40
        max_velocity = 70
        notes.append("Low acceleration limits velocity potential")

    # Add contextual notes
    if rod_diameter == 8.0 and span > 280:
        notes.append("M8 rods at this span limit acceleration significantly")
        notes.append("Consider M10 rods or smaller bed for better performance")

    if toolhead_mass > 350:
        notes.append("Heavy toolhead reduces acceleration headroom")
        notes.append("Consider pancake motor or lighter extruder")

    if max_accel_quality > 5000:
        notes.append("Good acceleration headroom for quality printing")

    # Amalgam specific guidance
    notes.append(f"Amalgam target: 70-120mm/s at {int(recommended_accel)} mm/s²")

    return AccelerationResult(
        toolhead_mass=toolhead_mass,
        rod_diameter=rod_diameter,
        span=span,
        max_accel_for_quality=round(max_accel_quality, 0),
        max_accel_structural=round(max_accel_structural, 0),
        recommended_accel=round(recommended_accel, 0),
        recommended_velocity=recommended_velocity,
        max_velocity=max_velocity,
        notes=notes,
    )


def compare_configurations(
    configurations: list[tuple[float, float, float]],  # (mass, rod_dia, span)
) -> list[AccelerationResult]:
    """
    Compare acceleration limits across multiple configurations.

    Args:
        configurations: List of (toolhead_mass, rod_diameter, span) tuples

    Returns:
        List of AccelerationResult for each configuration
    """
    return [
        calculate_max_acceleration(mass, rod_dia, span)
        for mass, rod_dia, span in configurations
    ]


# Klipper configuration recommendations
def get_klipper_settings(result: AccelerationResult) -> dict:
    """
    Generate recommended Klipper settings based on analysis.

    Returns:
        Dictionary of Klipper configuration values
    """
    return {
        "max_velocity": result.max_velocity,
        "max_accel": int(result.recommended_accel),
        "max_accel_to_decel": int(result.recommended_accel * 0.5),
        "square_corner_velocity": 5.0 if result.recommended_accel > 2000 else 3.0,
    }


if __name__ == "__main__":
    # Example usage
    print("Acceleration Analysis Example")
    print("=" * 50)

    # Compare Pitan on M8 vs M10 at 280mm span
    configs = [
        (280, 8.0, 280),   # Pitan on M8
        (280, 10.0, 280),  # Pitan on M10
        (450, 10.0, 280),  # Wade on M10
    ]

    results = compare_configurations(configs)

    for result in results:
        print(f"\n{result.toolhead_mass}g toolhead, M{int(result.rod_diameter)} rods, {result.span}mm span:")
        print(f"  Quality-limited accel: {result.max_accel_for_quality:.0f} mm/s²")
        print(f"  Structural limit: {result.max_accel_structural:.0f} mm/s²")
        print(f"  Recommended: {result.recommended_accel:.0f} mm/s²")
        print(f"  Velocity range: {result.recommended_velocity}-{result.max_velocity} mm/s")

        klipper = get_klipper_settings(result)
        print(f"  Klipper settings:")
        print(f"    max_velocity: {klipper['max_velocity']}")
        print(f"    max_accel: {klipper['max_accel']}")
