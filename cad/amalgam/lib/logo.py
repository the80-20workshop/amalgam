"""
Amalgam Logo Module

The official Amalgam brand mark: stylized geometric A in an octagon.
Based on the maker coin design, but without coin-specific features.

This is the single source of truth for the logo. Import this into:
- parts/victory/maker_coin.py (adds lanyard hole, bottom text)
- parts/victory/fidget_bolt.py (bolt head)
- parts/frame/*.py and other printer parts (branding)

Usage:
    from amalgam.lib.logo import make_logo

    # Get the logo at any size
    logo = make_logo(diameter=38, thickness=5)
"""

from build123d import *
import math

# Import the stylized A from same package
from amalgam.lib.stylized_a import make_stylized_a_sketch

# Try to import show for interactive viewing
try:
    from ocp_vscode import show
    HAS_VIEWER = True
except ImportError:
    HAS_VIEWER = False

# =============================================================================
# Logo Parameters (matching maker coin proportions)
# =============================================================================

# Octagon
DIAMETER = 27 * MM            # Default diameter (across flats)
THICKNESS = 3 * MM            # Default thickness
SIDES = 8
OCTAGON_ROTATION = 22.5       # Degrees (22.5 = flat edge at top)

# Logo dimensions (as ratios for scalability)
A_SIZE_RATIO = 0.65           # A height as ratio of diameter
RECESS_DEPTH_RATIO = 0.20     # Recess depth as ratio of thickness

# Circle creates the bulging sides
CIRCLE_DIAMETER_RATIO = 0.75  # Circle diameter as ratio of octagon diameter
CIRCLE_Y_OFFSET_RATIO = -0.0 # Offset down (negative = down)

# A positioning
A_Y_OFFSET_RATIO = 0.135           # Shift up to visually center (stylized A has more mass below)

# Rounded corners on the cutout A
CUTOUT_EXPAND = 0 * MM      # How much to expand cutout A (creates outline gap)

# Edge treatments (fixed values like maker coin)
OUTER_FILLET = 0.5 * MM           # Fillet on outer vertical edges
EDGE_CHAMFER = 0.4 * MM           # Chamfer on top/bottom horizontal edges


# =============================================================================
# Logo Function
# =============================================================================

def make_logo(
    diameter: float = DIAMETER,
    thickness: float = THICKNESS,
    recess_depth: float = None,
    cutout_expand: float = CUTOUT_EXPAND,
    outer_fillet: float = None,
    edge_chamfer: float = None,
    recess_fillet: float = None,
) -> Part:
    """
    Create the Amalgam logo as a 3D Part.

    This is the core logo: octagon with stylized A.
    Same approach as maker coin but without lanyard hole or bottom text.

    Args:
        diameter: Across-flats diameter of the octagon
        thickness: Total thickness
        recess_depth: Depth of the recess (default: thickness * 0.3)
        cutout_expand: How much to expand cutout A vs raised A (creates outline)
        outer_fillet: Fillet radius on outer vertical edges
        edge_chamfer: Chamfer on top and bottom horizontal edges
        recess_fillet: Fillet radius on internal recess edges

    Returns:
        Part containing the logo
    """
    # Calculate defaults based on size
    if recess_depth is None:
        recess_depth = thickness * RECESS_DEPTH_RATIO
    if outer_fillet is None:
        outer_fillet = OUTER_FILLET
    if edge_chamfer is None:
        edge_chamfer = EDGE_CHAMFER
        # Cap chamfer to 15% of thickness for thin parts
        edge_chamfer = min(edge_chamfer, thickness * 0.15)

    # Calculate dimensions
    inradius = diameter / 2
    circumradius = inradius / math.cos(math.pi / SIDES)

    a_size = diameter * A_SIZE_RATIO
    a_y_offset = diameter * A_Y_OFFSET_RATIO
    circle_diameter = diameter * CIRCLE_DIAMETER_RATIO
    circle_y_offset = diameter * CIRCLE_Y_OFFSET_RATIO

    # Get the stylized A sketch
    a_sketch = make_stylized_a_sketch(height=a_size)

    with BuildPart() as logo:
        # --- Base octagonal shape (full thickness) ---
        with BuildSketch(Plane.XY):
            RegularPolygon(
                radius=circumradius,
                side_count=SIDES,
                rotation=OCTAGON_ROTATION,
                align=(Align.CENTER, Align.CENTER)
            )
        extrude(amount=thickness)

        # --- Step 1: Cut the circle (creates bulging sides) ---
        with BuildSketch(Plane.XY.offset(thickness)):
            with Locations([(0, circle_y_offset)]):
                Circle(radius=circle_diameter / 2)
        extrude(amount=-recess_depth, mode=Mode.SUBTRACT)

        # --- Step 2: Cut the larger A with rounded corners ---
        # Expand the A outward to create the outline gap
        with BuildSketch(Plane.XY.offset(thickness)):
            with Locations([(0, a_y_offset)]):
                add(a_sketch)
            offset(amount=cutout_expand, kind=Kind.ARC)
        extrude(amount=-recess_depth, mode=Mode.SUBTRACT)

        # --- Step 3: Add the raised sharp A back on top ---
        with BuildSketch(Plane.XY.offset(thickness - recess_depth)):
            with Locations([(0, a_y_offset)]):
                add(a_sketch)
        extrude(amount=recess_depth, mode=Mode.ADD)

    # --- Apply edge treatments to the final part ---
    # Following maker coin approach: fillet first, then chamfers
    result = logo.part

    # Tolerances (matching maker coin)
    z_tolerance = thickness * 0.1
    outer_radius = (diameter / 2) * 0.8
    vertical_tolerance = thickness * 0.15
    min_edge_length = diameter * 0.3  # For filtering octagon edges from recess edges

    # 1. Chamfer top edges FIRST (only long octagon edges, not recess curves)
    try:
        top_edges = result.edges().filter_by(
            lambda e: (
                abs(e.center().Z - thickness) < z_tolerance and
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius and
                e.length > min_edge_length
            )
        )
        if top_edges:
            result = chamfer(top_edges, length=edge_chamfer)
            print(f"Chamfered {len(top_edges)} top edges")
        else:
            print("No top edges found for chamfer")
    except Exception as ex:
        print(f"Top chamfer failed: {ex}")

    # 2. Chamfer bottom edges
    try:
        bottom_edges = result.edges().filter_by(
            lambda e: (
                abs(e.center().Z) < z_tolerance and
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius
            )
        )
        if bottom_edges:
            result = chamfer(bottom_edges, length=edge_chamfer)
            print(f"Chamfered {len(bottom_edges)} bottom edges")
        else:
            print("No bottom edges found for chamfer")
    except Exception as ex:
        print(f"Bottom chamfer failed: {ex}")

    # 3. Fillet vertical edges LAST (after chamfers are done)
    # Vertical edges are now shorter due to chamfers
    try:
        vertical_edges = result.edges().filter_by(
            lambda e: (
                e.length > thickness * 0.5 and  # More lenient after chamfers
                math.sqrt(e.center().X**2 + e.center().Y**2) > outer_radius and
                abs(e.center().Z - thickness/2) < thickness * 0.6
            )
        )
        if vertical_edges:
            # Try progressively smaller radii until one works
            for radius in [outer_fillet, outer_fillet * 0.7, outer_fillet * 0.5, outer_fillet * 0.3]:
                try:
                    result = fillet(vertical_edges, radius=radius)
                    print(f"Filleted {len(vertical_edges)} vertical edges (radius={radius:.2f}mm)")
                    break
                except Exception:
                    continue
            else:
                print(f"Vertical fillet failed at all radii, skipping")
        else:
            print("No vertical edges found for fillet")
    except Exception as ex:
        print(f"Vertical fillet failed: {ex}")

    return result


# =============================================================================
# Main (for testing)
# =============================================================================

def main():
    """Test the logo generation."""
    print("=" * 50)
    print("Amalgam Logo Test")
    print("=" * 50)

    print(f"Diameter: {DIAMETER}mm")
    print(f"Thickness: {THICKNESS}mm")
    print()

    logo = make_logo()
    print("Logo generated!")

    # Export
    try:
        export_stl(logo, "../stl/amalgam_logo.stl")
        print("Exported: ../stl/amalgam_logo.stl")
    except Exception as e:
        print(f"Could not export: {e}")

    # Show
    if HAS_VIEWER:
        show(logo)
    else:
        print("(Install ocp_vscode for viewing)")

    return logo


if __name__ == "__main__":
    main()
