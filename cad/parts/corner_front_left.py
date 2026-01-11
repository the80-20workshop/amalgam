"""
Neo-Darwin Front-Left Corner with Integrated Z1 Motor

Uses shared motorized corner component from include/corner_components.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from include.corner_components import make_motorized_corner

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
    print("Generating Corner: Front-Left with integrated Z1 motor mount...")

    # Generate front-left corner (default orientation, no mirror)
    corner_1 = make_motorized_corner(location="front_left", mirror=False)

    # Export to STL
    from build123d import export_stl as export_stl_func

    export_stl_func(corner_1, "corner_front_left.stl")
    print("Exported: corner_front_left.stl")

    # Print dimensions
    print(f"  Motor: NEMA17 (Z1)")
    print(f"  Bolt spacing: 31mm (standard)")
    print(f"  Export: corner_front_left.stl")
    print("Corner complete!")

    return corner_1


if __name__ == "__main__":
    main()
