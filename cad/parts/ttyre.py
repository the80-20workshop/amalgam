import copy
from build123d import *
from ocp_vscode import show

# --- 1. Parameters ---
wheel_diameter = 1000 * MM
tire_width = 400 * MM
tire_thickness = 100 * MM
lug_height = 40 * MM
lug_angle = 35
num_lugs = 20

# --- 2. Create the Tire Body ---
with BuildPart() as tire_body:
    with BuildSketch(Plane.XY) as tire_profile:
        with BuildLine():
            l1 = Line((-tire_width / 2, wheel_diameter / 2), (tire_width / 2, wheel_diameter / 2))
            l2 = Line(l1 @ 1, (tire_width / 2, wheel_diameter / 2 - tire_thickness))
            l3 = Line(l2 @ 1, (-tire_width / 2, wheel_diameter / 2 - tire_thickness))
            l4 = Line(l3 @ 1, l1 @ 0)
        make_face()
        fillet(tire_profile.vertices(), radius=20)
    revolve(axis=Axis.X)

# --- 3. Create a Single "Master Lug" ---
with BuildPart() as lug_part:
    # We build the lug directly at the top of the tire
    with BuildSketch(Plane.XY.offset(wheel_diameter / 2)) as lug_sketch:
        # One half of the V-shape
        with Locations((tire_width / 4, 0)):
            Rectangle(60, tire_width * 0.5, rotation=-lug_angle)
    # Extrude it outwards from the tire surface
    extrude(amount=lug_height)

# --- 4. Distribute the Lugs (Staggered V-Pattern) ---
lugs = []
angle_step = 360 / num_lugs

for i in range(num_lugs):
    # Right side lug
    l_right = lug_part.part.rotate(Axis.X, i * angle_step)
    lugs.append(l_right)
    
    # Left side lug (mirrored and staggered)
    l_left = lug_part.part.mirror(Plane.YZ).rotate(Axis.X, i * angle_step + (angle_step / 2))
    lugs.append(l_left)

# Combine all parts
tractor_tire = tire_body.part + lugs

show(tractor_tire)