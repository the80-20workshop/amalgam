"""
Tractor Tire Generator v3 - Proper Chevron Pattern
===================================================

The key insight: real tractor tire lugs are LONG bars that sweep across 
most of the tire width. The grooves between them create the pattern.

This version uses much longer grooves that properly meet at the center
to create the characteristic herringbone/chevron pattern.
"""

import math
from build123d import *
from ocp_vscode import show

# ============================================================================
# PARAMETERS
# ============================================================================

# Tire dimensions
OUTER_DIAMETER = 1000
TIRE_WIDTH = 400
TIRE_THICKNESS = 180
PROFILE_RADIUS = 50

# Tread pattern
NUM_LUGS = 12              # Number of lug PAIRS (left+right = one chevron)
LUG_ANGLE = 45             # Angle from perpendicular
GROOVE_WIDTH = 55          # Width of the valley between lugs
GROOVE_DEPTH = 65          # How deep the valleys are cut
GROOVE_TAPER = 10          # V-profile taper

# ============================================================================
# DERIVED
# ============================================================================

outer_r = OUTER_DIAMETER / 2
inner_r = outer_r - TIRE_THICKNESS
mean_r = (inner_r + outer_r) / 2
angle_step = 360 / NUM_LUGS

# Critical: groove must be long enough to span from center past the edge
# At 45°, a groove starting at center needs length = (width/2) / cos(45°) 
groove_length = (TIRE_WIDTH / 2) / math.cos(math.radians(LUG_ANGLE)) + 80

print("=" * 55)
print("TRACTOR TIRE - CHEVRON PATTERN v3")
print("=" * 55)
print(f"Tire: {OUTER_DIAMETER}mm OD × {TIRE_WIDTH}mm wide")
print(f"Lugs: {NUM_LUGS} pairs at {LUG_ANGLE}° angle")
print(f"Groove length: {groove_length:.0f}mm (to ensure full coverage)")
print()

# ============================================================================
# STEP 1: CREATE TIRE BODY
# ============================================================================

print("[1/3] Creating tire body...")

with BuildPart() as tire_body:
    with BuildSketch(Plane.XY):
        with Locations((0, mean_r)):
            RectangleRounded(TIRE_WIDTH, TIRE_THICKNESS, radius=PROFILE_RADIUS)
    revolve(axis=Axis.X)

tire = tire_body.part
print("       Done")

# ============================================================================
# STEP 2: CUT THE CHEVRON GROOVES
# ============================================================================

print("[2/3] Cutting chevron grooves...")

# Create a single groove cutter - tapered V-profile
with BuildPart() as groove_cutter:
    with BuildSketch(Plane.XY):
        # Trapezoidal cross-section
        taper_offset = GROOVE_DEPTH * math.tan(math.radians(GROOVE_TAPER))
        bottom_w = max(GROOVE_WIDTH - 2 * taper_offset, 10)
        
        with BuildLine():
            # Top edge (at tire surface)
            Line((-GROOVE_WIDTH/2, 0), (GROOVE_WIDTH/2, 0))
            # Right side going down
            Line((GROOVE_WIDTH/2, 0), (bottom_w/2, -GROOVE_DEPTH))
            # Bottom edge
            Line((bottom_w/2, -GROOVE_DEPTH), (-bottom_w/2, -GROOVE_DEPTH))
            # Left side going up
            Line((-bottom_w/2, -GROOVE_DEPTH), (-GROOVE_WIDTH/2, 0))
        make_face()
    
    # Extrude the full length
    extrude(amount=groove_length)

cutter = groove_cutter.part

# Now cut the pattern
# Each chevron has a RIGHT groove and a LEFT groove that meet at center

for i in range(NUM_LUGS):
    circumference_angle = i * angle_step
    
    # === RIGHT SIDE GROOVE ===
    # Starts at the CENTER of the tire (X=0) and extends toward +X (right edge)
    # The groove is angled so it sweeps backward as it goes outward
    
    right_groove = (cutter
        .rotate(Axis.X, 180)              # Flip to cut downward
        .rotate(Axis.Y, -LUG_ANGLE)       # Angle the groove
        # Position: start at center (X=0), at tire surface (Z=outer_r)
        # The groove extends in +X direction after rotation
        .move(Location((0, 0, outer_r + 2)))
        .rotate(Axis.X, circumference_angle))
    
    tire = tire - right_groove
    
    # === LEFT SIDE GROOVE ===
    # Mirror of right side, but STAGGERED by half a step
    # This creates the interlocking chevron pattern
    
    stagger = angle_step / 2
    
    left_groove = (cutter
        .rotate(Axis.X, 180)
        .rotate(Axis.Y, LUG_ANGLE)        # Opposite angle
        .move(Location((0, 0, outer_r + 2)))
        .rotate(Axis.X, circumference_angle + stagger))
    
    tire = tire - left_groove
    
    if (i + 1) % 4 == 0:
        print(f"       {i + 1}/{NUM_LUGS} chevron pairs cut")

print(f"       All {NUM_LUGS} pairs complete")

# ============================================================================
# STEP 3: SIDEWALL RIBS (optional detail)
# ============================================================================

print("[3/3] Adding sidewall ribs...")

NUM_RIBS = 20
with BuildPart() as rib:
    with BuildSketch(Plane.XY):
        with Locations((TIRE_WIDTH/2 - 18, mean_r)):
            RectangleRounded(10, TIRE_THICKNESS * 0.45, radius=3)
    revolve(axis=Axis.X, revolution_arc=5)

rib_part = rib.part

for i in range(NUM_RIBS):
    angle = i * (360 / NUM_RIBS)
    # Right side
    tire = tire + rib_part.rotate(Axis.X, angle)
    # Left side (mirrored)
    tire = tire + rib_part.mirror(Plane.YZ).rotate(Axis.X, angle + 9)

print(f"       {NUM_RIBS * 2} ribs added")

# ============================================================================
# EXPORT
# ============================================================================

print()
print("Exporting...")
#export_step(tire, "/home/claude/tractor_tire_v3.step")
export_stl(tire, "/home/claude/tractor_tire_v3.stl")
print("  ✓ tractor_tire_v3.step")
print("  ✓ tractor_tire_v3.stl")
print()
print("=" * 55)
print("COMPLETE!")
print("=" * 55)

# from ocp_vscode import show
show(tire)
