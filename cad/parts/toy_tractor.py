"""
Toy Tractor - Converted from OpenSCAD to build123d
==================================================

Original: toys_tractor.scad
This is a simplified conversion showing the main structure.

Parts:
- Wheels (torus tire + hub disc)
- Axles
- Hood/bonnet
- Cabin
- Rear hitch hook
"""

from build123d import *

# ============================================================================
# PARAMETERS
# ============================================================================

essieu_r = 3  # Axle radius

# ============================================================================
# HELPER
# ============================================================================

def get_solid(shape):
    if isinstance(shape, Solid):
        return shape
    if hasattr(shape, 'solids'):
        solids = list(shape.solids())
        if solids:
            return solids[0]
    return shape

# ============================================================================
# WHEEL (roue)
# ============================================================================

def roue(d, e):
    """
    Create a wheel
    d = diameter
    e = tire thickness
    """
    with BuildPart() as wheel:
        # Tire - torus shape via revolve of ellipse
        with BuildSketch(Plane.XZ):
            with Locations((d/2 - e/2, 0)):
                Ellipse(e/2, e/2 * 1.2)  # Slightly taller than wide
        revolve(axis=Axis.Z)
        
        # Hub disc
        Cylinder(radius=d/2 - e/2, height=e, 
                 align=(Align.CENTER, Align.CENTER, Align.CENTER))
        
        # Axle hole (subtract)
        Cylinder(radius=essieu_r + 0.3, height=e + 2, 
                 align=(Align.CENTER, Align.CENTER, Align.CENTER), 
                 mode=Mode.SUBTRACT)
    
    return wheel.part

# ============================================================================
# AXLE (essieu)
# ============================================================================

def essieu(l, d_e):
    """
    Create an axle
    l = length
    d_e = end offset
    """
    with BuildPart() as axle:
        # Main shaft
        Cylinder(radius=essieu_r, height=l + d_e, rotation=(0, 90, 0))
        # Wider center section
        Cylinder(radius=essieu_r + 1, height=l - d_e, rotation=(0, 90, 0))
    
    return axle.part.move(Location((0, 0, 2)))

# ============================================================================
# HOOD (capot)
# ============================================================================

def capot():
    """Create the tractor hood/bonnet"""
    with BuildPart() as hood:
        # Base
        Box(10, 30, 10, align=(Align.CENTER, Align.MIN, Align.MIN))
        # Raised top section
        with Locations((0, 15, 10)):
            Box(10, 28, 6, align=(Align.CENTER, Align.CENTER, Align.MIN))
    
    return hood.part

# ============================================================================
# CABIN (cabine)
# ============================================================================

def cabine():
    """Create the tractor cabin"""
    with BuildPart() as cab:
        # Lower section
        Box(22, 24, 10, align=(Align.CENTER, Align.MIN, Align.MIN))
        # Middle section
        with Locations((0, 0, 10)):
            Box(24, 24, 10, align=(Align.CENTER, Align.MIN, Align.MIN))
        # Upper section
        with Locations((0, 0, 20)):
            Box(24, 22, 15, align=(Align.CENTER, Align.MIN, Align.MIN))
        # Roof
        with Locations((0, 11, 35)):
            Box(20, 18, 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
    
    return cab.part

# ============================================================================
# HITCH (crochet)
# ============================================================================

def crochet(l):
    """Create rear hitch hook"""
    with BuildPart() as hook:
        # Base plate
        Box(l, 1, 3, align=(Align.CENTER, Align.MIN, Align.MIN))
        # Ring
        with Locations((0, -8, 0)):
            Cylinder(radius=4, height=7)
            # Hole in ring
            Cylinder(radius=3, height=9, mode=Mode.SUBTRACT)
    
    return hook.part

# ============================================================================
# ASSEMBLE TRACTOR
# ============================================================================

def build_tractor():
    """Build the complete toy tractor"""
    print("Building toy tractor...")
    
    # Create individual parts
    print("  Creating parts...")
    wheel_rear = roue(25, 6)
    wheel_front = roue(20, 5)
    axle_r = essieu(31, 7)
    axle_f = essieu(31, 6)
    hood = capot()
    cabin = cabine()
    hook = crochet(22)
    
    # Assemble
    print("  Assembling...")
    with BuildPart() as tractor:
        x = 13  # Y offset
        z = 8   # Z offset (ground clearance)
        
        # Axles
        add(axle_r.move(Location((0, x, z + 2))))
        add(axle_f.move(Location((0, x + 40, z))))
        
        # Hood
        add(hood.move(Location((0, x + 15, z))))
        
        # Cabin
        add(cabin.move(Location((0, x - 5, z))))
        
        # Hook
        add(hook.move(Location((0, x - 5, z))))
        
        # Wheels (rotated 90° to mount on axles)
        wr = wheel_rear.rotate(Axis.Y, 90)
        wf = wheel_front.rotate(Axis.Y, 90)
        
        # Rear wheels (larger, diameter 25)
        add(wr.move(Location((18, x, z + 4))))
        add(wr.move(Location((-18, x, z + 4))))
        
        # Front wheels (smaller, diameter 20)
        add(wf.move(Location((18, x + 40, z + 2))))
        add(wf.move(Location((-18, x + 40, z + 2))))
    
    return tractor.part

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    tractor = build_tractor()
    print(f"    Volume: {tractor.volume:.0f}")
    
    print("\nExporting...")
    #export_step(tractor, "toy_tractor.step")
    export_stl(tractor, "toy_tractor.stl")
    print("  ✓ toy_tractor.step")
    print("  ✓ toy_tractor.stl")
    print("\nDone!")
    
    # Uncomment for OCP-VSCode:
    from ocp_vscode import show
    show(tractor)
