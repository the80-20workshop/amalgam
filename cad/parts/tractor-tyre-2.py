"""
Tractor Tire Generator v2 - build123d
======================================

Creates a realistic agricultural tire with proper chevron (herringbone) tread.

Key improvement: The lugs now extend from the center outward and meet 
to form the characteristic "V" or arrow pattern seen on real tractor tires.

For OCP-VSCode: uncomment the show() line at the bottom
"""

import math
from build123d import *
from ocp_vscode import show

# ============================================================================
# PARAMETERS
# ============================================================================

# Overall dimensions
OUTER_DIAMETER = 1000      # Total tire diameter (mm)
TIRE_WIDTH = 400           # Width of tire (mm)  
TIRE_THICKNESS = 180       # Radial thickness 
PROFILE_RADIUS = 50        # Corner rounding

# Tread pattern - these create the chevron look
NUM_CHEVRONS = 14          # Number of V-patterns 
LUG_ANGLE = 45             # Angle from centerline (45° is classic)
GROOVE_WIDTH = 45          # Width of grooves (valleys)
GROOVE_DEPTH = 60          # Depth of grooves
GROOVE_TAPER = 12          # V-shape taper

# Lug dimensions
LUG_OVERLAP = 20           # How much lugs overlap at center (creates the V meeting point)

# Sidewall
NUM_RIBS = 18
RIB_WIDTH = 10
RIB_ARC = 5

# ============================================================================
# DERIVED VALUES
# ============================================================================

outer_r = OUTER_DIAMETER / 2
inner_r = outer_r - TIRE_THICKNESS
mean_r = (inner_r + outer_r) / 2
angle_step = 360 / NUM_CHEVRONS

# ============================================================================
# BUILD THE TIRE
# ============================================================================

print("=" * 50)
print("TRACTOR TIRE GENERATOR v2")
print("=" * 50)
print(f"Size: {OUTER_DIAMETER}mm × {TIRE_WIDTH}mm")
print(f"Pattern: {NUM_CHEVRONS} chevrons at {LUG_ANGLE}° angle")
print()

# --- STEP 1: Tire Body ---
print("[1/3] Creating tire body...")

with BuildPart() as tire_body:
    with BuildSketch(Plane.XY):
        with Locations((0, mean_r)):
            RectangleRounded(TIRE_WIDTH, TIRE_THICKNESS, radius=PROFILE_RADIUS)
    revolve(axis=Axis.X)

tire = tire_body.part

# --- STEP 2: Cut Grooves ---
print("[2/3] Cutting tread grooves...")

# The grooves should be longer and start closer to center
# so that the left and right grooves overlap/meet in the middle
groove_length = TIRE_WIDTH * 0.6 + LUG_OVERLAP

# Create V-shaped groove cutter
with BuildPart() as groove_cutter:
    with BuildSketch(Plane.XY):
        taper_offset = GROOVE_DEPTH * math.tan(math.radians(GROOVE_TAPER))
        bottom_width = max(GROOVE_WIDTH - 2 * taper_offset, 8)
        
        with BuildLine():
            Line((-GROOVE_WIDTH/2, 0), (GROOVE_WIDTH/2, 0))
            Line((GROOVE_WIDTH/2, 0), (bottom_width/2, -GROOVE_DEPTH))
            Line((bottom_width/2, -GROOVE_DEPTH), (-bottom_width/2, -GROOVE_DEPTH))
            Line((-bottom_width/2, -GROOVE_DEPTH), (-GROOVE_WIDTH/2, 0))
        make_face()
    extrude(amount=groove_length)

cutter_base = groove_cutter.part

# Cut the chevron pattern
for i in range(NUM_CHEVRONS):
    base_angle = i * angle_step
    
    # Right-side groove: starts near center, angles toward right edge
    # Position the start of the groove close to center (negative offset)
    center_offset = -LUG_OVERLAP / 2
    
    cutter_right = (cutter_base
        .rotate(Axis.X, 180)                           # Point cutting face down
        .rotate(Axis.Y, -LUG_ANGLE)                    # Angle toward right
        .move(Location((center_offset, 0, outer_r + 1)))  # Near center, at surface
        .rotate(Axis.X, base_angle))                   # Position around tire
    
    tire = tire - cutter_right
    
    # Left-side groove: opposite angle, staggered by half step
    stagger = angle_step / 2
    
    cutter_left = (cutter_base
        .rotate(Axis.X, 180)
        .rotate(Axis.Y, LUG_ANGLE)                     # Angle toward left
        .move(Location((-center_offset, 0, outer_r + 1)))
        .rotate(Axis.X, base_angle + stagger))
    
    tire = tire - cutter_left
    
    if (i + 1) % 5 == 0:
        print(f"       {i + 1}/{NUM_CHEVRONS} complete")

print(f"       All {NUM_CHEVRONS} chevrons cut")

# --- STEP 3: Sidewall Ribs ---
print("[3/3] Adding sidewall ribs...")

with BuildPart() as rib_template:
    with BuildSketch(Plane.XY):
        with Locations((TIRE_WIDTH/2 - 18, mean_r)):
            RectangleRounded(RIB_WIDTH, TIRE_THICKNESS * 0.5, radius=3)
    revolve(axis=Axis.X, revolution_arc=RIB_ARC)

rib = rib_template.part

for i in range(NUM_RIBS):
    angle = i * (360 / NUM_RIBS)
    tire = tire + rib.rotate(Axis.X, angle)
    tire = tire + rib.mirror(Plane.YZ).rotate(Axis.X, angle + 180/NUM_RIBS)

print(f"       {NUM_RIBS * 2} ribs added")

# ============================================================================
# EXPORT
# ============================================================================

print()
print("Exporting...")
#export_step(tire, "/home/claude/tractor_tire_v2.step")
export_stl(tire, "/home/claude/tractor_tire_v2.stl")
#print("  ✓ tractor_tire_v2.step")
print("  ✓ tractor_tire_v2.stl")

print()
print("=" * 50)
print("DONE! View in OCP-VSCode with:")
print("  from ocp_vscode import show")
print("  show(tire)")
print("=" * 50)

# from ocp_vscode import show
show(tire)
