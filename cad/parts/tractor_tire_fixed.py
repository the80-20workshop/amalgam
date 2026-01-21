"""
Tractor Tire - Fixed Sidewalls
==============================

Simple additive approach:
1. Tread base cylinder (full width)
2. Thin sidewall rings on each end
3. Chamfered lugs on top
4. Cut center hole
"""

import math
from build123d import *
from ocp_vscode import show

# ============================================================================
# PARAMETERS
# ============================================================================

OUTER_DIAMETER = 1000
TIRE_WIDTH = 400
RIM_DIAMETER = 640

LUG_HEIGHT = 60
LUG_WIDTH = 65
LUG_LENGTH = 200
LUG_CHAMFER = 8

NUM_LUG_PAIRS = 14
LUG_ANGLE = 45

SIDEWALL_WIDTH = 40    # Width of sidewall section on each side

# ============================================================================
# DERIVED VALUES
# ============================================================================

outer_r = OUTER_DIAMETER / 2           # 500
rim_r = RIM_DIAMETER / 2               # 320
base_outer_r = outer_r - LUG_HEIGHT    # 440 - where lugs sit
tread_width = TIRE_WIDTH - 2 * SIDEWALL_WIDTH  # 320
angle_step = 360 / NUM_LUG_PAIRS

print("=" * 55)
print("TRACTOR TIRE GENERATOR")
print("=" * 55)
print(f"Size: {OUTER_DIAMETER}mm OD × {TIRE_WIDTH}mm wide")
print(f"Lugs: {NUM_LUG_PAIRS} pairs at {LUG_ANGLE}°")
print()

# ============================================================================
# BUILD
# ============================================================================

# 1. Create chamfered lug template
print("[1/5] Creating lug template...")
with BuildPart() as lug_b:
    Box(LUG_LENGTH, LUG_WIDTH, LUG_HEIGHT)
    chamfer(lug_b.edges(), length=LUG_CHAMFER)
lug = lug_b.part

# 2. Main tread cylinder - full width at base radius
print("[2/5] Creating tread base...")
with BuildPart() as tread_b:
    Cylinder(radius=base_outer_r, height=TIRE_WIDTH, rotation=(0, 90, 0))
tire = tread_b.part

# 3. Add thin sidewall rings on each end
print("[3/5] Adding sidewall rings...")
with BuildPart() as sw_b:
    Cylinder(radius=outer_r, height=SIDEWALL_WIDTH, rotation=(0, 90, 0))

# Right sidewall - positioned at right edge
right_sw = sw_b.part.move(Location(((TIRE_WIDTH - SIDEWALL_WIDTH) / 2, 0, 0)))
tire = tire + right_sw

# Left sidewall - positioned at left edge
left_sw = sw_b.part.move(Location((-(TIRE_WIDTH - SIDEWALL_WIDTH) / 2, 0, 0)))
tire = tire + left_sw

# 4. Add lugs around the tire
print("[4/5] Adding lugs...")
for i in range(NUM_LUG_PAIRS):
    base_angle = i * angle_step
    
    # Right side lug
    right_lug = (lug
        .rotate(Axis.Z, -LUG_ANGLE)
        .move(Location((tread_width * 0.25, 0, base_outer_r + LUG_HEIGHT/2 - 10)))
        .rotate(Axis.X, base_angle))
    tire = tire + right_lug
    
    # Left side lug (staggered for chevron pattern)
    left_lug = (lug
        .rotate(Axis.Z, LUG_ANGLE)
        .move(Location((-tread_width * 0.25, 0, base_outer_r + LUG_HEIGHT/2 - 10)))
        .rotate(Axis.X, base_angle + angle_step/2))
    tire = tire + left_lug

# 5. Cut center hole and trim
print("[5/5] Cutting hole and trimming...")

# Cut rim hole
with BuildPart() as hole_b:
    Cylinder(radius=rim_r, height=TIRE_WIDTH + 50, rotation=(0, 90, 0))
tire = tire - hole_b.part

# Helper to extract single solid
def get_solid(shape):
    if isinstance(shape, Solid):
        return shape
    elif hasattr(shape, 'solids'):
        solids = list(shape.solids())
        return solids[0] if solids else shape
    return shape

tire = get_solid(tire)

# Trim flush with tire width
with BuildPart() as bounds:
    Box(TIRE_WIDTH, OUTER_DIAMETER + 200, OUTER_DIAMETER + 200)
tire = tire.intersect(bounds.part)
tire = get_solid(tire)

# ============================================================================
# EXPORT
# ============================================================================

print()
print("Exporting...")
#export_step(tire, "tractor_tire.step")
export_stl(tire, "tractor_tire.stl")
print("  ✓ tractor_tire.step")
print("  ✓ tractor_tire.stl")
print()
print("=" * 55)
print("COMPLETE!")
print("=" * 55)

# Uncomment for OCP-VSCode:
# from ocp_vscode import show
show(tire)
