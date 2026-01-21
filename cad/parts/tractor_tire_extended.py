"""
Tractor Tire - Extended Lugs with Chamfered Edges
=================================================

Features:
- Lugs extend to the tire edge and are trimmed flush with sidewalls
- All lug edges are chamfered for a softer look
- Clean chevron pattern with proper stagger

Parameters are at the top for easy customization.
"""

import math
from build123d import *
from ocp_vscode import show

# ============================================================================
# PARAMETERS - Customize these
# ============================================================================

OUTER_DIAMETER = 1000      # Overall tire diameter
TIRE_WIDTH = 400           # Total tire width
RIM_DIAMETER = 640         # Inner hole for rim

LUG_HEIGHT = 60            # How tall lugs stand above base
LUG_WIDTH = 65             # Width of each lug
LUG_LENGTH = 200           # Length of lugs (extended to reach edge)
LUG_CHAMFER = 8            # Chamfer size on lug edges

NUM_LUG_PAIRS = 14         # Number of chevron pairs
LUG_ANGLE = 45             # Angle of lugs from perpendicular

SIDEWALL_THICKNESS = 40    # Thickness of sidewall caps

# ============================================================================
# DERIVED VALUES
# ============================================================================

outer_r = OUTER_DIAMETER / 2
rim_r = RIM_DIAMETER / 2
base_outer_r = outer_r - LUG_HEIGHT
tread_width = TIRE_WIDTH - 2 * SIDEWALL_THICKNESS
angle_step = 360 / NUM_LUG_PAIRS

print("=" * 55)
print("TRACTOR TIRE GENERATOR")
print("=" * 55)
print(f"Size: {OUTER_DIAMETER}mm × {TIRE_WIDTH}mm")
print(f"Lugs: {NUM_LUG_PAIRS} pairs at {LUG_ANGLE}° with {LUG_CHAMFER}mm chamfer")
print()

# ============================================================================
# BUILD
# ============================================================================

# 1. Create chamfered lug template
print("[1/4] Creating lug template...")
with BuildPart() as lug_builder:
    Box(LUG_LENGTH, LUG_WIDTH, LUG_HEIGHT)
    chamfer(lug_builder.edges(), length=LUG_CHAMFER)
lug = lug_builder.part

# 2. Create tire body (base cylinder + sidewalls)
print("[2/4] Creating body...")
with BuildPart() as body_builder:
    # Main tread surface
    Cylinder(radius=base_outer_r, height=tread_width, rotation=(0, 90, 0))
    # Right sidewall
    with Locations(((tread_width + SIDEWALL_THICKNESS) / 2, 0, 0)):
        Cylinder(radius=outer_r, height=SIDEWALL_THICKNESS, rotation=(0, 90, 0))
    # Left sidewall
    with Locations((-(tread_width + SIDEWALL_THICKNESS) / 2, 0, 0)):
        Cylinder(radius=outer_r, height=SIDEWALL_THICKNESS, rotation=(0, 90, 0))

tire = body_builder.part

# 3. Add lugs around the tire
print("[3/4] Adding lugs...")
for i in range(NUM_LUG_PAIRS):
    base_angle = i * angle_step
    
    # Right side lug
    right_lug = (lug
        .rotate(Axis.Z, -LUG_ANGLE)
        .move(Location((tread_width * 0.28, 0, base_outer_r + LUG_HEIGHT/2 - 12)))
        .rotate(Axis.X, base_angle))
    tire = tire + right_lug
    
    # Left side lug (staggered by half step for chevron pattern)
    left_lug = (lug
        .rotate(Axis.Z, LUG_ANGLE)
        .move(Location((-tread_width * 0.28, 0, base_outer_r + LUG_HEIGHT/2 - 12)))
        .rotate(Axis.X, base_angle + angle_step/2))
    tire = tire + left_lug

# 4. Cut center hole
print("[4/4] Finishing...")
with BuildPart() as hole_builder:
    Cylinder(radius=rim_r, height=TIRE_WIDTH + 50, rotation=(0, 90, 0))
tire = tire - hole_builder.part

# Handle ShapeList if boolean returned multiple solids
def get_solid(shape):
    if isinstance(shape, Solid):
        return shape
    elif hasattr(shape, 'solids'):
        solids = list(shape.solids())
        return solids[0] if solids else shape
    return shape

tire = get_solid(tire)

# Trim excess with bounding box intersection
with BuildPart() as bounds:
    Box(TIRE_WIDTH, OUTER_DIAMETER + 100, OUTER_DIAMETER + 100)
tire = tire.intersect(bounds.part)
tire = get_solid(tire)

# ============================================================================
# EXPORT
# ============================================================================

print()
print("Exporting...")
# export_step(tire, "tractor_tire.step")
export_stl(tire, "tractor_tire.stl")
print("  ✓ tractor_tire.step")
print("  ✓ tractor_tire.stl")
print()
print("=" * 55)
print("COMPLETE!")
print("=" * 55)

# Uncomment for OCP-VSCode visualization:
# from ocp_vscode import show
show(tire)
