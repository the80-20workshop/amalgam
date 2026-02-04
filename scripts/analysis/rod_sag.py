"""
Rod Sag Analysis for Amalgam

Calculates smooth rod deflection under toolhead load using beam theory.
This helps builders assess whether their rod diameter is sufficient
for their build volume.

Theory:
    For a simply-supported beam with center load:
    deflection = (F * L^3) / (48 * E * I)

    Where:
    - F = Force (toolhead weight in N)
    - L = Span length (mm)
    - E = Young's modulus (steel ≈ 200 GPa)
    - I = Second moment of area (π * d^4 / 64 for circular rod)
"""

import math
from dataclasses import dataclass
from typing import Optional


# Material properties
STEEL_YOUNGS_MODULUS = 200e9  # Pa (200 GPa for steel)
GRAVITY = 9.81  # m/s²


@dataclass
class RodSagResult:
    """Result of rod sag calculation."""

    rod_diameter: float  # mm
    span: float  # mm
    toolhead_mass: float  # grams
    deflection: float  # mm
    verdict: str  # "excellent", "good", "acceptable", "marginal", "excessive"
    recommendation: str


def calculate_second_moment(diameter_mm: float) -> float:
    """
    Calculate second moment of area for a circular cross-section.

    I = π * d^4 / 64

    Args:
        diameter_mm: Rod diameter in mm

    Returns:
        Second moment of area in m^4
    """
    d = diameter_mm / 1000  # Convert to meters
    return math.pi * (d ** 4) / 64


def calculate_rod_sag(
    rod_diameter: float,
    span: float,
    toolhead_mass: float,
    acceleration: Optional[float] = None,
) -> RodSagResult:
    """
    Calculate rod deflection under toolhead load.

    Args:
        rod_diameter: Smooth rod diameter in mm (e.g., 8, 10)
        span: Unsupported span length in mm (e.g., 250, 300)
        toolhead_mass: Toolhead mass in grams (e.g., 280 for Pitan)
        acceleration: Optional acceleration in mm/s² for dynamic loading

    Returns:
        RodSagResult with deflection and recommendations
    """
    # Convert units
    L = span / 1000  # mm to m
    mass_kg = toolhead_mass / 1000  # g to kg

    # Static force (gravity)
    F_static = mass_kg * GRAVITY  # N

    # Add dynamic force if acceleration specified
    if acceleration:
        # Convert mm/s² to m/s²
        accel_m_s2 = acceleration / 1000
        F_dynamic = mass_kg * accel_m_s2
        F_total = F_static + F_dynamic
    else:
        F_total = F_static

    # Calculate second moment of area
    I = calculate_second_moment(rod_diameter)

    # Calculate deflection using beam equation
    # δ = F * L³ / (48 * E * I)
    deflection_m = (F_total * (L ** 3)) / (48 * STEEL_YOUNGS_MODULUS * I)
    deflection_mm = deflection_m * 1000

    # Determine verdict based on deflection thresholds
    # These thresholds are based on typical layer heights and quality requirements
    if deflection_mm < 0.015:
        verdict = "excellent"
        recommendation = "Well within tolerance for high-quality prints."
    elif deflection_mm < 0.025:
        verdict = "good"
        recommendation = "Good for most printing applications."
    elif deflection_mm < 0.035:
        verdict = "acceptable"
        recommendation = "Acceptable for standard prints. Consider M10 for demanding work."
    elif deflection_mm < 0.050:
        verdict = "marginal"
        recommendation = (
            "May affect print quality at fine layer heights. "
            "Consider upgrading to M10 rods or reducing span."
        )
    else:
        verdict = "excessive"
        recommendation = (
            "Excessive deflection will affect print quality. "
            "Upgrade to larger diameter rods or reduce build volume."
        )

    return RodSagResult(
        rod_diameter=rod_diameter,
        span=span,
        toolhead_mass=toolhead_mass,
        deflection=round(deflection_mm, 4),
        verdict=verdict,
        recommendation=recommendation,
    )


def compare_rod_options(
    span: float,
    toolhead_mass: float,
    rod_sizes: list[float] = [8.0, 10.0, 12.0],
) -> list[RodSagResult]:
    """
    Compare deflection across multiple rod sizes.

    Args:
        span: Unsupported span length in mm
        toolhead_mass: Toolhead mass in grams
        rod_sizes: List of rod diameters to compare

    Returns:
        List of RodSagResult for each rod size
    """
    return [
        calculate_rod_sag(rod_dia, span, toolhead_mass)
        for rod_dia in rod_sizes
    ]


# Extruder mass estimates (grams, including NEMA17 motor)
EXTRUDER_MASSES = {
    "PITAN": 280,  # Pitan + standard NEMA17
    "PITAN_PANCAKE": 200,  # Pitan + pancake NEMA17
    "WADE": 450,  # Wade + standard NEMA17
    "WADE_PANCAKE": 360,  # Wade + pancake NEMA17
    "MK8": 180,  # MK8 direct drive
    "SHERPA_MINI": 120,  # Sherpa Mini + NEMA14
    "ORBITER": 150,  # Orbiter v1.5
}


def get_extruder_mass(extruder_type: str) -> float:
    """Get estimated mass for an extruder type."""
    return EXTRUDER_MASSES.get(extruder_type.upper(), 280)  # Default to Pitan


if __name__ == "__main__":
    # Example usage
    print("Rod Sag Analysis Example")
    print("=" * 50)

    # Compare M8 vs M10 at 250mm span with Pitan extruder
    results = compare_rod_options(
        span=250,
        toolhead_mass=280,  # Pitan
        rod_sizes=[8.0, 10.0],
    )

    for result in results:
        print(f"\nM{int(result.rod_diameter)} rod at {result.span}mm span:")
        print(f"  Deflection: {result.deflection:.4f} mm")
        print(f"  Verdict: {result.verdict}")
        print(f"  {result.recommendation}")
