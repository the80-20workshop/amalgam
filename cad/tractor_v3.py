from build123d import *

# --- Parameters ---
L, W, H = 60, 30, 12
wheel_r_back, wheel_r_front = 14, 9
wheel_thick = 10
cab_size = 26
chimney_h, chimney_r = 18, 3

with BuildPart() as tractor:
    # 1. Main Chassis & Hood
    # We build the whole base and then cut the "hood" step
    Box(L, W, H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    with BuildSketch(tractor.faces().sort_by(Axis.Z)[-1]):
        Rectangle(L/2, W, align=(Align.MIN, Align.CENTER))
    extrude(amount=-H/2, mode=Mode.SUBTRACT)

    # 2. The Cab (Solid Block first)
    # Positioned at the rear
    with BuildSketch(tractor.faces().sort_by(Axis.Z)[-1].sort_by(Axis.X)[0]):
        Rectangle(cab_size, W)
    extrude(amount=cab_size)

    # 3. Window Cuts (The Bridge Test)
    # Side Windows - cutting all the way through the Y-axis
    with BuildSketch(Plane.XZ) as side_win:
        with Locations((-L/4, H + cab_size/1.8)):
            Rectangle(cab_size - 8, cab_size - 10)
    extrude(amount=W, both=True, mode=Mode.SUBTRACT)

    # Front/Back Windows - cutting all the way through the X-axis
    with BuildSketch(Plane.YZ.offset(-L/4)) as front_win:
        with Locations((0, H + cab_size/1.8)):
            Rectangle(W - 8, cab_size - 10)
    extrude(amount=cab_size, both=True, mode=Mode.SUBTRACT)

    # 4. Fenders (The Overhang Test)
    # These give it the iconic tractor silhouette
    for x_pos, r in [(-L/3, wheel_r_back + 2), (L/3, wheel_r_front + 2)]:
        with BuildSketch(Plane.XZ.offset(W/2)):
            with Locations((x_pos, H/2)):
                # Create a semi-circle arch
                SlotOverall(r*2.2, r*2, rotation=90)
        extrude(amount=wheel_thick + 2, mode=Mode.ADD)
    # Mirror fenders to the other side
    mirror(about=Plane.XZ)

    # 5. Wheels
    # We place these slightly outward so they don't merge into the body 
    for side in [-1, 1]:
        # Back Wheels
        with BuildSketch(Plane.YZ.offset(side * (W/2 + wheel_thick/2))):
            with Locations((0, wheel_r_back)): # Y in YZ plane is vertical
                Circle(wheel_r_back)
                Circle(wheel_r_back - 4, mode=Mode.SUBTRACT)
        extrude(amount=wheel_thick, both=True)
        
        # Front Wheels
        with BuildSketch(Plane.YZ.offset(side * (W/2 + wheel_thick/2))):
            with Locations((L/1.5, wheel_r_front)): 
                Circle(wheel_r_front)
                Circle(wheel_r_front - 3, mode=Mode.SUBTRACT)
        extrude(amount=wheel_thick, both=True)

    # 6. The Chimney
    with BuildSketch(tractor.faces().filter_by(Axis.Z).sort_by(Axis.X)[-1]):
        with Locations((L/8, 0)):
            Circle(chimney_r)
    extrude(amount=chimney_h)

# --- Export ---
export_stl(tractor.part, "tractor_v4.stl")