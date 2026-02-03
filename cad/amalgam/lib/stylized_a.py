"""
Stylized A Logo - Pure Geometric Version

Builds the stylized A from geometric primitives (no font).
Based on reference: logos/Gemini_Generated_Image_utackcutackcutac.png

The shape is:
  1. Outer triangle (the A silhouette)
  2. Inner triangle cutout (the hole)
  3. Parallelogram crossbar (detached, extends past left leg)
  4. Gap below crossbar
  5. Flat top cut (optional) - removes pointed apex
"""

from build123d import *

# Try to import show for interactive viewing
try:
    from ocp_vscode import show
    HAS_VIEWER = True
except ImportError:
    HAS_VIEWER = False

# =============================================================================
# Parameters - All proportions relative to HEIGHT
# =============================================================================

HEIGHT = 30 * MM          # Overall height of the A
THICKNESS = 3 * MM        # Extrusion thickness

# --- Outer triangle (A silhouette) ---
WIDTH_RATIO = 0.9         # Width as ratio of height (base width = HEIGHT * this)
APEX_X = 0.0              # Apex X offset (0 = centered)

# --- Leg thickness ---
LEG_THICKNESS = 0.32      # Leg thickness as ratio of height

# --- Inner triangle (hole) ---
INNER_APEX_EXTRA_DROP = 0.05  # Extra drop for inner apex beyond leg thickness calc (ratio of height)

# --- Crossbar ---
CROSSBAR_TOP_Y = -0.08    # Top of crossbar (ratio from center)
CROSSBAR_BOTTOM_Y = -0.22 # Bottom of crossbar
CROSSBAR_EXTEND_LEFT = 0.15   # How far crossbar extends past left leg (ratio of height)
CROSSBAR_EXTEND_RIGHT = 0.04  # How far right edge extends into the A (0 = at inner hole edge, positive = further right)

# --- Gap (separates crossbar from left leg) ---
GAP_WIDTH = 0.03          # Gap width as ratio of height

# --- Flat top (optional) ---
FLAT_TOP = True           # If True, cut off the apex to make a flat top
FLAT_TOP_Y = 0.25         # Y position of flat cut (ratio from center, 0.5 = very top)


# =============================================================================
# Build Functions
# =============================================================================

def make_stylized_a_sketch(
    height: float = HEIGHT,
    width_ratio: float = WIDTH_RATIO,
    leg_thickness: float = LEG_THICKNESS,
    inner_apex_extra_drop: float = INNER_APEX_EXTRA_DROP,
    crossbar_top_y: float = CROSSBAR_TOP_Y,
    crossbar_bottom_y: float = CROSSBAR_BOTTOM_Y,
    crossbar_extend_left: float = CROSSBAR_EXTEND_LEFT,
    crossbar_extend_right: float = CROSSBAR_EXTEND_RIGHT,
    gap_width: float = GAP_WIDTH,
    flat_top: bool = FLAT_TOP,
    flat_top_y: float = FLAT_TOP_Y,
) -> Sketch:
    """
    Create the stylized A logo as a 2D Sketch.

    Use this for importing into other parts (maker coin, fidget bolt).
    All proportions use the module-level defaults, so just pass `height` to scale.

    Args:
        height: Overall height of the A (scales everything proportionally)

    Returns:
        Sketch containing the stylized A shape
    """
    import math

    h = height
    w = height * width_ratio

    # Key Y coordinates (0 = center, positive = up)
    top_y = h / 2
    bottom_y = -h / 2

    # Outer triangle vertices
    apex = (0, top_y)
    bottom_left = (-w / 2, bottom_y)
    bottom_right = (w / 2, bottom_y)

    # Helper functions for leg positions
    def x_on_left_leg(y):
        return -w / 2 + (w / 2) * (y - bottom_y) / h

    def x_on_right_leg(y):
        return w / 2 - (w / 2) * (y - bottom_y) / h

    # Calculate inset for leg thickness
    leg_angle = math.atan2(h, w / 2)
    inset = h * leg_thickness
    inner_apex_drop = inset / math.sin(leg_angle) + h * inner_apex_extra_drop
    inner_base_inset = inset / math.tan(leg_angle)

    # Inner triangle (hole) vertices
    # inner_apex_extra_drop lets you push the inner apex down further
    inner_apex = (0, top_y - inner_apex_drop)
    inner_bottom_left = (-w / 2 + inner_base_inset, bottom_y)
    inner_bottom_right = (w / 2 - inner_base_inset, bottom_y)

    # Crossbar vertices
    cb_top = h * crossbar_top_y
    cb_bottom = h * crossbar_bottom_y

    inner_right_top_x = x_on_right_leg(cb_top) - inset
    inner_right_bottom_x = x_on_right_leg(cb_bottom) - inset
    cb_right_top_x = inner_right_top_x + h * crossbar_extend_right
    cb_right_bottom_x = inner_right_bottom_x + h * crossbar_extend_right

    cb_left_top_x = x_on_left_leg(cb_top) - h * crossbar_extend_left
    cb_left_bottom_x = x_on_left_leg(cb_bottom) - h * crossbar_extend_left

    # Gap vertices
    gap_height = h * gap_width
    gap_top_y = cb_bottom
    gap_bottom_y = cb_bottom - gap_height

    # Build the sketch using 2D boolean operations
    with BuildSketch() as logo:
        # Step 1: Outer triangle
        Polygon(apex, bottom_left, bottom_right, align=None)

        # Step 2: Cut inner hole
        Polygon(inner_apex, inner_bottom_left, inner_bottom_right, align=None, mode=Mode.SUBTRACT)

        # Step 3: Add crossbar
        Polygon(
            (cb_right_top_x, cb_top),
            (cb_left_top_x, cb_top),
            (cb_left_bottom_x, cb_bottom),
            (cb_right_bottom_x, cb_bottom),
            align=None, mode=Mode.ADD
        )

        # Step 4: Cut gap
        Polygon(
            (cb_right_top_x, gap_top_y),
            (cb_left_bottom_x, gap_top_y),
            (cb_left_bottom_x - gap_height, gap_bottom_y),
            (cb_right_bottom_x, gap_bottom_y),
            align=None, mode=Mode.SUBTRACT
        )

        # Step 5: Flat top (optional) - cut off the apex
        if flat_top:
            flat_y = h * flat_top_y
            # Rectangle that cuts everything above flat_y
            # Make it wide enough to cover the whole A
            Polygon(
                (-w, flat_y),
                (w, flat_y),
                (w, top_y + h * 0.1),  # Above the apex
                (-w, top_y + h * 0.1),
                align=None, mode=Mode.SUBTRACT
            )

    return logo.sketch


def make_stylized_a_geometric(
    height: float = HEIGHT,
    thickness: float = THICKNESS,
) -> Part:
    """
    Create the stylized A logo as a 3D Part.

    This is a convenience function that extrudes the 2D sketch.
    For integration into other parts, use make_stylized_a_sketch() instead.

    Args:
        height: Overall height of the A (scales everything proportionally)
        thickness: Extrusion thickness

    Returns:
        Part containing the stylized A
    """
    sketch = make_stylized_a_sketch(height=height)

    with BuildPart() as part:
        with BuildSketch(Plane.XY):
            add(sketch)
        extrude(amount=thickness)

    return part.part


def main():
    """Generate and display the stylized A."""
    print("=" * 50)
    print("Stylized A Logo - Geometric Version")
    print("=" * 50)
    print(f"Height: {HEIGHT}mm")
    print(f"Width: {HEIGHT * WIDTH_RATIO}mm")
    print(f"Thickness: {THICKNESS}mm")
    print()

    result = make_stylized_a_geometric()

    print("Stylized A generated!")

    # Export to STL
    try:
        export_stl(result, "../stl/stylized_a_geometric.stl")
        print("Exported: ../stl/stylized_a_geometric.stl")
    except Exception as e:
        print(f"Could not export STL: {e}")

    # Show in viewer
    if HAS_VIEWER:
        print("Displaying in viewer...")
        show(result)
    else:
        print("(Install ocp_vscode for interactive viewing)")

    return result


if __name__ == "__main__":
    main()
