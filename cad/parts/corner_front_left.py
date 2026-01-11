"""
Neo-Darwin Front-Left Corner with Integrated Z1 Motor

Uses shared motorized corner component from include/corner_components.py
"""

import sys

sys.path.insert(0, "..")

from include.corner_components import make_motorized_corner

try:
    from config import *

    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False
    print("Warning: config.py not found, using fallback values")


def main():
    print("Generating Corner: Front-Left with integrated Z1 motor mount...")

    # Generate front-left corner (default orientation, no mirror)
    corner_1 = make_motorized_corner(location="front_left", mirror=False)

    # Export to STL
    if CONFIG_AVAILABLE:
        from build123d import export_stl as export_stl_func

        export_stl_func(corner_1, "corner_front_left.stl")
        print("Exported: corner_front_left.stl")
    else:
        print("Warning: build123d not available, skipping STL export")

    # Print dimensions
    print(f"  Motor: NEMA17 (Z1)")
    print(f"  Bolt spacing: 31mm (standard)")
    print(f"  Export: corner_front_left.stl")
    print("Corner complete!")

    return corner_1


if __name__ == "__main__":
    main()
