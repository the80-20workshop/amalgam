"""
Neo-Darwin Standard Corner
Basic corner with 4 M12 rod clamps and jam nut access
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from include.corner_components import make_standard_corner

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

    # Export to STL
    from build123d import export_stl as export_stl_func

    stl_path = "../stl/corner_standard.stl"
    export_stl_func(corner, stl_path)
    print(f"Exported: {stl_path}")

    print("Standard corner complete!")
    return corner


if __name__ == "__main__":
    main()
