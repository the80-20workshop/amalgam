"""
Amalgam Brand System

Centralized brand constants and color utilities.
Reads palette from config.py (single source of truth), provides
build123d Color objects and CSS-compatible hex values.

Palette:
    Body:     Dark Grey (#4A4A4A) — printed parts
    Accent:   White (#FFFFFF) — logo pads, raised details
    Base:     Near-Black (#1A1A1A) — MDF base, aluminum extrusions
    Hardware: Silver (#C0C0C0) — bolts, rods, bearings (documentation only)

Usage:
    from amalgam.lib.brand import get_body_color, get_accent_color, PALETTE
"""

from build123d import Color


# ---------------------------------------------------------------------------
# Read palette from config.py, fall back to defaults
# ---------------------------------------------------------------------------

try:
    from config import BRAND_BODY_COLOR as _BODY
except ImportError:
    _BODY = "#4A4A4A"

try:
    from config import BRAND_ACCENT_COLOR as _ACCENT
except ImportError:
    _ACCENT = "#FFFFFF"

try:
    from config import BRAND_BASE_COLOR as _BASE
except ImportError:
    _BASE = "#1A1A1A"


# ---------------------------------------------------------------------------
# Palette dictionary (for programmatic access)
# ---------------------------------------------------------------------------

PALETTE = {
    "body": _BODY,
    "accent": _ACCENT,
    "base": _BASE,
    "hardware": "#C0C0C0",
}


# ---------------------------------------------------------------------------
# Color conversion utilities
# ---------------------------------------------------------------------------

def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color string to (r, g, b) as 0.0-1.0 floats."""
    h = hex_color.lstrip("#")
    return (
        int(h[0:2], 16) / 255.0,
        int(h[2:4], 16) / 255.0,
        int(h[4:6], 16) / 255.0,
    )


def hex_to_rgb_int(hex_color: str) -> tuple:
    """Convert hex color string to (r, g, b) as 0-255 integers."""
    h = hex_color.lstrip("#")
    return (
        int(h[0:2], 16),
        int(h[2:4], 16),
        int(h[4:6], 16),
    )


# ---------------------------------------------------------------------------
# build123d Color objects
# ---------------------------------------------------------------------------

def get_body_color() -> Color:
    """Dark Grey — for printed part bodies."""
    r, g, b = hex_to_rgb(_BODY)
    return Color(r, g, b, 1.0)


def get_accent_color() -> Color:
    """White — for logo accents and raised details."""
    r, g, b = hex_to_rgb(_ACCENT)
    return Color(r, g, b, 1.0)


def get_base_color() -> Color:
    """Near-Black — for MDF base and frame elements."""
    r, g, b = hex_to_rgb(_BASE)
    return Color(r, g, b, 1.0)
