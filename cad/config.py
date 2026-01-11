"""
Darwin-Neo Master Configuration
Parametric Logic for High-Mass, Low-Cost 3D Printing.
"""

# --- 1. DONOR & TRANSPARENCY ---
# Options: "PRUSA_CLONE", "ENDER_3", "SCAVENGED"
DONOR_TYPE = "ENDER_3"

# --- 2. THE SKELETON (M12 RODS) ---
M12_NOMINAL_DIA = 12.0
# Set 0.2 for Zinc, 0.5+ for Galvanized (The "Lumpy Factor")
LUMPY_FACTOR = 0.5
M12_FIT_DIA = M12_NOMINAL_DIA + LUMPY_FACTOR

# --- 3. MOTION FORK (SMOOTH RODS) ---
# 8.0 for salvage, 10.0 for "Neo" Standard
SMOOTH_ROD_DIA = 10.0
BEARING_TYPE = "LM10UU" if SMOOTH_ROD_DIA == 10.0 else "LM8UU"

# --- 4. TIER DEFINITIONS ---
TRIPLE_Z = True  # True = Independent 3-point Z-Tilt
EXTRUDER_TYPE = "WADE"  # The Signature 13:43 Geared Torque Monster
HOTEND_DONOR = "ENDER_MK8"

# --- 5. BUILD VOLUME ---
BUILD_VOLUME = {"X": 250, "Y": 250, "Z": 250}

# --- 6. DYNAMIC FRAME CALCULATIONS ---
# Greg's Wade requires a significant "Gear Overhang" on the X-axis
X_OVERHANG = 50.0 if EXTRUDER_TYPE == "WADE" else 25.0

# --- 6.1 FRAME GEOMETRY (Neo-Darwin M12 Frame) ---
# Frame has 8 vertical rods (4 front, 4 back) with horizontal top/bottom rods

# M12 SKELETON (Reduced height from 80 to 50 for efficiency)
SKELETON_X = BUILD_VOLUME["X"] + (X_OVERHANG * 2) + 40
SKELETON_Y = BUILD_VOLUME["Y"] + 120
SKELETON_Z = BUILD_VOLUME["Z"] + 50  # Reduced from 80

# Corner Design Parameters
CORNER_SIZE = 50.0              # Size of corner cube (mm)
WALL_THICKNESS = 5.0            # Wall thickness of corner parts (mm)
JAM_NUT_ACCESS_DIA = 20.0       # Diameter for jam nut access holes (mm)

# Vertical Rod Positions
FRONT_LEFT_V = True  # VFL
FRONT_CENTER_V = True  # VFC (optional center rod)
FRONT_RIGHT_V = True  # VFR
BACK_LEFT_V = True  # VBL
BACK_CENTER_V = True  # VBC
BACK_RIGHT_V = True  # VBR

# Z-System Mounting
TRIPLE_Z = True
Z_MOUNT_PATTERN = (
    "FRONT_CORNERS_BACK_BOTTOM"  # Front L+R integrated, Back Center on bottom rod
)

# Corner Count and Types
BOTTOM_CORNERS = 4  # 2 Z-mount + 2 standard
TOP_CORNERS = 4  # All standard (gantry)
TOTAL_CORNERS = 8

# Z-Motor Locations
Z1_LOCATION = "front_left_corner"  # Integrated into Corner 1
Z2_LOCATION = "front_right_corner"  # Integrated into Corner 2
Z3_LOCATION = "back_center_rod"  # Separate Z-puck on back bottom rod

# Corner Types
FRONT_LEFT_CORNER = "Z_MOUNT_INTEGRATED"
FRONT_RIGHT_CORNER = "Z_MOUNT_INTEGRATED"
BACK_LEFT_CORNER = "STANDARD"
BACK_RIGHT_CORNER = "STANDARD"

# Z-Clearances
BOTTOM_Z_CLEARANCE = 25  # Bed + spider + nut clearance from bottom frame
TOP_Z_CLEARANCE = 15  # Bed to gantry clearance
Z_TRAVEL_MAX = SKELETON_Z - BOTTOM_Z_CLEARANCE - TOP_Z_CLEARANCE  # = 260mm travel

# --- 6.2 SPIDER BED SUPPORT ---
SPIDER_ARM_LENGTH = 150
SPIDER_HUB_SIZE = 120
SPIDER_BOLT_PATTERN = "M6"
SPIDER_INTERLOCK = True
SPIDER_LEADSCREW_SPACING = 40  # Distance between leadscrews for hub


# --- 7. UTILITIES ---
def print_config_summary():
    """Manifesto Transparency Check"""
    print(f"--- Darwin-Neo Configuration: {DONOR_TYPE} Path ---")
    if DONOR_TYPE == "ENDER_3":
        print(
            f"!!! MOTION GAP: Ender rollers incompatible. Buy 6x {SMOOTH_ROD_DIA}mm rods."
        )
    print(f"Frame Dimensions: {SKELETON_X} x {SKELETON_Y} x {SKELETON_Z}")
    print(f"Z-Travel: {Z_TRAVEL_MAX}mm (Frame: {SKELETON_Z}mm)")
    print(f"Z-Motors: {Z1_LOCATION}, {Z2_LOCATION}, {Z3_LOCATION}")
    print(
        f"Parts: {BOTTOM_CORNERS} bottom corners + {TOP_CORNERS} top corners = {TOTAL_CORNERS} total"
    )
