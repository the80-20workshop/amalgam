"""
Amalgam Component Registry

Defines available components, their properties, and compatibility rules.
This is the single source of truth for what hardware Amalgam supports.

Architecture:
- Each component type (boards, extruders, etc.) has its own module
- Components define metadata, not code - they're data structures
- Compatibility rules live here, build logic lives in builders/
- Adding new hardware = adding to registry, no code changes needed

Usage:
    from registry import BOARDS, EXTRUDERS, BEDS, MOTORS
    from registry import get_tier_requirements, check_compatibility
"""

from .boards import BOARDS, get_board
from .extruders import EXTRUDERS, get_extruder
from .beds import BEDS, COMMON_BED_SIZES, get_bed
from .motors import MOTORS, MOTOR_SOURCES, get_motor_count_for_tier
from .compatibility import (
    determine_tier,
    check_compatibility,
    get_tier_requirements,
    TierRequirements,
    CompatibilityResult,
    Severity,
)

__all__ = [
    # Component registries
    "BOARDS",
    "EXTRUDERS",
    "BEDS",
    "MOTORS",
    "COMMON_BED_SIZES",
    "MOTOR_SOURCES",
    # Lookup functions
    "get_board",
    "get_extruder",
    "get_bed",
    "get_motor_count_for_tier",
    # Compatibility
    "determine_tier",
    "check_compatibility",
    "get_tier_requirements",
    "TierRequirements",
    "CompatibilityResult",
    "Severity",
]
