"""
Amalgam Standard Corner
Basic corner with 4 M12 rod clamps and jam nut access
"""

import sys

from amalgam.lib.corner import make_standard_corner
from amalgam.lib.export import export_part
from amalgam.lib.logo_pad import apply_logo_pad

try:
    from config import *
except ImportError:
    print("ERROR: config.py not found")
    print("")
    print("Please run: ./configure.py")
    print("This will create config.py with your build parameters")
    print("")
    sys.exit(1)


def main():
    print("Generating Standard Corner...")

    corner = make_standard_corner(
        corner_size=CORNER_SIZE,
        m12_fit_dia=M12_FIT_DIA,
        wall_thickness=WALL_THICKNESS,
        jam_nut_access_dia=JAM_NUT_ACCESS_DIA,
    )

    # Apply optional brand logo pad
    corner = apply_logo_pad(corner, face="top")

    # Export using centralized export module
    print("\nExporting...")
    export_part(corner, "corner_standard")

    print("Standard corner complete!")
    return corner


if __name__ == "__main__":
    main()
