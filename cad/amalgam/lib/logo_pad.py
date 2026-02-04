"""
Logo Pad Module

Adds a raised Amalgam logo pad to a part face for brand marking.
The pad is designed for single-filament-swap color change in the slicer:
print the body in dark grey, swap to white at the logo pad layer.

Controlled by LOGO_PAD_ENABLED in config.py. When disabled, apply_logo_pad()
returns the part unchanged — zero overhead.

Usage:
    from amalgam.lib.logo_pad import apply_logo_pad

    part = make_my_part()
    part = apply_logo_pad(part, face="top")
"""

import math
from build123d import (
    Part, Face, Vector, Location, Plane, Axis,
)

from amalgam.lib.logo import make_logo


# ---------------------------------------------------------------------------
# Read config with fallbacks
# ---------------------------------------------------------------------------

try:
    from config import LOGO_PAD_ENABLED
except ImportError:
    LOGO_PAD_ENABLED = True

try:
    from config import LOGO_PAD_HEIGHT
except ImportError:
    LOGO_PAD_HEIGHT = 0.5

try:
    from config import LOGO_PAD_DIAMETER
except ImportError:
    LOGO_PAD_DIAMETER = 18.0


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def apply_logo_pad(
    part: Part,
    face: str = "top",
    diameter: float = None,
    pad_height: float = None,
    offset: tuple = (0, 0),
) -> Part:
    """
    Add a raised Amalgam logo pad to a part's face.

    Returns the part unchanged if LOGO_PAD_ENABLED is False in config.

    Args:
        part: The build123d Part to brand.
        face: Which face to place the logo on. Options:
              "top", "bottom", "front", "back", "left", "right".
        diameter: Logo diameter in mm (default: LOGO_PAD_DIAMETER from config).
        pad_height: Height the pad is raised in mm (default: LOGO_PAD_HEIGHT).
        offset: (x, y) offset from face center on the face's local plane.

    Returns:
        Part with logo pad fused on, or the original part if disabled/failed.
    """
    if not LOGO_PAD_ENABLED:
        return part

    if diameter is None:
        diameter = LOGO_PAD_DIAMETER
    if pad_height is None:
        pad_height = LOGO_PAD_HEIGHT

    # Resolve the target face
    target = _resolve_face(part, face)
    if target is None:
        print(f"  Warning: Could not find '{face}' face for logo pad, skipping")
        return part

    # Generate a thin logo
    try:
        logo = make_logo(
            diameter=diameter,
            thickness=pad_height,
            outer_fillet=min(0.2, pad_height * 0.3),
            edge_chamfer=min(0.1, pad_height * 0.15),
        )
    except Exception as e:
        print(f"  Warning: Logo generation failed: {e}")
        return part

    # Position the logo on the target face
    try:
        face_center = target.center()
        face_normal = target.normal_at(face_center)

        # Apply user offset in the face plane
        # For now, offsets are applied in world X/Y relative to face center
        cx = face_center.X + offset[0]
        cy = face_center.Y + offset[1]
        cz = face_center.Z

        # The logo is built on XY plane, centered at origin, Z from 0 to thickness.
        # We need to move it so its bottom sits on the target face.
        if _is_top_face(face_normal):
            # Face points up (+Z) — most common case
            logo = logo.moved(Location((cx, cy, cz)))
        elif _is_bottom_face(face_normal):
            # Face points down (-Z) — flip logo and place
            logo = logo.rotate(Axis.X, 180)
            logo = logo.moved(Location((cx, cy, cz)))
        elif _is_front_face(face_normal):
            # Face points toward -Y
            logo = logo.rotate(Axis.X, -90)
            logo = logo.moved(Location((cx, cz, cy)))
        elif _is_back_face(face_normal):
            # Face points toward +Y
            logo = logo.rotate(Axis.X, 90)
            logo = logo.moved(Location((cx, cz, cy)))
        elif _is_right_face(face_normal):
            # Face points toward +X
            logo = logo.rotate(Axis.Y, 90)
            logo = logo.moved(Location((cx, cy, cz)))
        elif _is_left_face(face_normal):
            # Face points toward -X
            logo = logo.rotate(Axis.Y, -90)
            logo = logo.moved(Location((cx, cy, cz)))
        else:
            # Arbitrary face normal — place at face center along normal
            # Simplified: just move to face center, logo will be approximately correct
            logo = logo.moved(Location((cx, cy, cz)))

        result = part.fuse(logo)
        print(f"  Logo pad applied ({diameter:.0f}mm, {pad_height:.1f}mm raised, face='{face}')")
        return result

    except Exception as e:
        print(f"  Warning: Logo pad placement failed: {e}")
        return part


# ---------------------------------------------------------------------------
# Face resolution
# ---------------------------------------------------------------------------

def _resolve_face(part: Part, face_spec) -> Face:
    """
    Resolve a face name to an actual Face object.

    Uses face center position as a heuristic — picks the face whose center
    is most extreme in the requested direction.
    """
    if isinstance(face_spec, Face):
        return face_spec

    faces = part.faces()
    if not faces:
        return None

    selectors = {
        "top": lambda f: f.center().Z,
        "bottom": lambda f: -f.center().Z,
        "front": lambda f: -f.center().Y,
        "back": lambda f: f.center().Y,
        "right": lambda f: f.center().X,
        "left": lambda f: -f.center().X,
    }

    key_fn = selectors.get(face_spec)
    if key_fn is None:
        print(f"  Warning: Unknown face '{face_spec}', using 'top'")
        key_fn = selectors["top"]

    # Sort faces by the key function, pick the most extreme
    try:
        candidates = sorted(faces, key=key_fn, reverse=True)
        if candidates:
            return candidates[0]
    except Exception:
        pass

    return None


# ---------------------------------------------------------------------------
# Normal direction helpers
# ---------------------------------------------------------------------------

def _is_top_face(normal: Vector) -> bool:
    return normal.Z > 0.9

def _is_bottom_face(normal: Vector) -> bool:
    return normal.Z < -0.9

def _is_front_face(normal: Vector) -> bool:
    return normal.Y < -0.9

def _is_back_face(normal: Vector) -> bool:
    return normal.Y > 0.9

def _is_right_face(normal: Vector) -> bool:
    return normal.X > 0.9

def _is_left_face(normal: Vector) -> bool:
    return normal.X < -0.9
