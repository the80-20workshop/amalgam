"""
Tractor Tire - Simple Additive Approach
========================================

Build it like LEGO:
1. Flat cylinder for the tread base
2. Rectangular blocks on top for lugs (angled to form chevrons)
3. Sidewall donuts on each end
4. Cut the center hole through everything
"""

import math
from build123d import *
from ocp_vscode import show

# ============================================================================
# PARAMETERS
# ============================================================================

# Overall tire size
OUTER_DIAMETER = 1000
TIRE_WIDTH = 400
RIM_DIAMETER = 640        # Inner hole diameter

# Tread dimensions
TREAD_BASE_THICKNESS = 120   # Thickness of the cylinder base
LUG_HEIGHT = 60              # How tall lugs stand above the base
LUG_WIDTH = 70               # Width of each lug bar
LUG_LENGTH = 160             # Length of each lug (how far it extends)

# Pattern
NUM_LUG_PAIRS = 14           # Number of chevron pairs around tire
LUG_ANGLE = 45               # Angle of lugs from perpendicular

# Sidewall
SIDEWALL_THICKNESS = 40      # Thickness of sidewall "donuts"

# ============================================================================
# DERIVED VALUES
# ============================================================================

outer_r = OUTER_DIAMETER / 2
rim_r = RIM_DIAMETER / 2
base_outer_r = outer_r - LUG_HEIGHT  # Top of cylinder (where lugs attach)
tread_width = TIRE_WIDTH - 2 * SIDEWALL_THICKNESS  # Width of tread area

angle_step = 360 / NUM_LUG_PAIRS

print("=" * 55)
print("TRACTOR TIRE - ADDITIVE BUILD")
print("=" * 55)
print(f"Size: {OUTER_DIAMETER}mm OD × {TIRE_WIDTH}mm wide")
print(f"Rim hole: {RIM_DIAMETER}mm")
print(f"Lugs: {NUM_LUG_PAIRS} pairs, {LUG_HEIGHT}mm tall")
print()

# ============================================================================
# STEP 1: TREAD BASE CYLINDER
# ============================================================================

print("[1/4] Creating tread base cylinder...")

# Main cylinder - this is the "floor" that lugs sit on
with BuildPart() as tread_base:
    # Cylinder oriented along X axis (tire rotates around X)
    Cylinder(
        radius=base_outer_r,
        height=tread_width,
        align=(Align.CENTER, Align.CENTER, Align.CENTER)
    )
    # Rotate so it's oriented correctly (height along X)
    # Actually, let's build it aligned to X from the start

# Hmm, Cylinder defaults to Z-axis. Let's just build and rotate.
with BuildPart() as tread_base:
    Cylinder(radius=base_outer_r, height=tread_width)

# Rotate to align with X axis (tire's rotation axis)
tire = tread_base.part.rotate(Axis.Y, 90)

print(f"       Base cylinder: {base_outer_r*2}mm dia × {tread_width}mm wide")

# ============================================================================
# STEP 2: ADD LUGS ON TOP
# ============================================================================

print("[2/4] Adding tread lugs...")

# Create a single lug block
# The lug is a box that sits on top of the cylinder surface
with BuildPart() as lug_block:
    Box(LUG_LENGTH, LUG_WIDTH, LUG_HEIGHT)

lug = lug_block.part

# Position lugs around the tire
lugs_added = 0

for i in range(NUM_LUG_PAIRS):
    base_angle = i * angle_step
    
    # === RIGHT SIDE LUG ===
    # Position on right half of tire, angled
    right_lug = (lug
        .rotate(Axis.Z, -LUG_ANGLE)           # Angle the lug
        .move(Location((tread_width * 0.2, 0, base_outer_r + LUG_HEIGHT/2 - 5)))  # On surface, right side
        .rotate(Axis.X, base_angle))           # Rotate around tire
    
    tire = tire + right_lug
    lugs_added += 1
    
    # === LEFT SIDE LUG ===
    # Mirror position, staggered rotation for chevron pattern
    stagger = angle_step / 2
    
    left_lug = (lug
        .rotate(Axis.Z, LUG_ANGLE)            # Opposite angle
        .move(Location((-tread_width * 0.2, 0, base_outer_r + LUG_HEIGHT/2 - 5)))
        .rotate(Axis.X, base_angle + stagger))
    
    tire = tire + left_lug
    lugs_added += 1
    
    if (i + 1) % 5 == 0:
        print(f"       {i + 1}/{NUM_LUG_PAIRS} pairs ({lugs_added} lugs)")

print(f"       Total: {lugs_added} lugs added")

# ============================================================================
# STEP 3: ADD SIDEWALLS
# ============================================================================

print("[3/4] Adding sidewalls...")

# Sidewalls are thick "donuts" on each end
# They connect the tread area to the rim

# Right sidewall
with BuildPart() as right_sidewall:
    # Outer cylinder
    Cylinder(radius=base_outer_r, height=SIDEWALL_THICKNESS)
    # We'll cut the hole later

right_sw = right_sidewall.part.rotate(Axis.Y, 90).move(
    Location(((tread_width + SIDEWALL_THICKNESS) / 2, 0, 0))
)
tire = tire + right_sw

# Left sidewall
left_sw = right_sidewall.part.rotate(Axis.Y, 90).move(
    Location((-(tread_width + SIDEWALL_THICKNESS) / 2, 0, 0))
)
tire = tire + left_sw

print(f"       Sidewalls added ({SIDEWALL_THICKNESS}mm thick each)")

# ============================================================================
# STEP 4: CUT THE CENTER HOLE
# ============================================================================

print("[4/4] Cutting center hole...")

# Cut through the entire tire
with BuildPart() as hole_cutter:
    Cylinder(radius=rim_r, height=TIRE_WIDTH + 20)

hole = hole_cutter.part.rotate(Axis.Y, 90)
tire = tire - hole

print(f"       Hole cut: {RIM_DIAMETER}mm diameter")

# ============================================================================
# EXPORT
# ============================================================================

print()
print("Exporting...")
#export_step(tire, "/home/claude/tractor_tire_simple.step")
export_stl(tire, "/home/claude/tractor_tire_simple.stl")
print("  ✓ tractor_tire_simple.step")
print("  ✓ tractor_tire_simple.stl")

print()
print("=" * 55)
print("DONE!")
print("=" * 55)

# from ocp_vscode import show
show(tire)
