from build123d import *

# --- Parameters (Make it easy to tweak) ---
body_w, body_h, body_d = 40, 25, 30
cab_w, cab_h, cab_d = 20, 20, 28
front_wheel_rad = 7
back_wheel_rad = 12
wheel_width = 8
chimney_rad, chimney_h = 3, 15

with BuildPart() as tractor:
    # 1. Main Body (Engine block area)
    with BuildPart() as body:
        Box(body_w, body_h, body_d, align=(Align.MIN, Align.CENTER, Align.MIN))
    
    # 2. The Cab (Driver area)
    # We position it on top of the back half of the body
    with BuildPart(Plane.XY.offset(body_h)) as cab:
        with Locations((5, 0, 0)): # Shift it slightly back
            Box(cab_w, cab_h, cab_d, align=(Align.MIN, Align.CENTER, Align.MIN))
    
    # 3. Exhaust Chimney
    # Positioned on the front top of the body
    with BuildPart(Plane.XY.offset(body_h)) as chimney:
        with Locations((body_w - 10, 0, 0)):
            Cylinder(radius=chimney_rad, height=chimney_h, align=(Align.CENTER, Align.CENTER, Align.MIN))
            
    # 4. Rear Wheels (Large)
    # Placed on both sides of the back
    with BuildPart() as rear_wheels:
        # Move to the back and out to the sides
        with Locations((10, body_d/2 + wheel_width/2, back_wheel_rad), 
                       (10, -body_d/2 - wheel_width/2, back_wheel_rad)):
            Rot(Y=90) * Cylinder(radius=back_wheel_rad, height=wheel_width)

    # 5. Front Wheels (Small)
    with BuildPart() as front_wheels:
        # Move to the front and out to the sides
        with Locations((body_w - 10, body_d/2 + wheel_width/2, front_wheel_rad), 
                       (body_w - 10, -body_d/2 - wheel_width/2, front_wheel_rad)):
            Rot(Y=90) * Cylinder(radius=front_wheel_rad, height=wheel_width)

# If using a viewer like OCP CAD Viewer, you would use:
# show(tractor)
