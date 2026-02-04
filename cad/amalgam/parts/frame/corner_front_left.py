"""
Amalgam Front-Left Corner with Integrated Z1 Motor

Uses shared motorized corner component from amalgam.lib.corner
"""

import sys

from amalgam.lib.corner import make_motorized_corner
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
    print("Generating Corner: Front-Left with integrated Z1 motor mount...")

    # Generate front-left corner (default orientation, no mirror)
    corner_1 = make_motorized_corner(location="front_left", mirror=False)

    # Apply optional brand logo pad
    corner_1 = apply_logo_pad(corner_1, face="top")

    # Export using centralized export module
    print("\nExporting...")
    export_part(corner_1, "corner_front_left")

    # Print dimensions
    print(f"  Motor: NEMA17 (Z1)")
    print(f"  Bolt spacing: 31mm (standard)")
    print(f"  Export: corner_front_left.stl")
    print("Corner complete!")

    return corner_1


if __name__ == "__main__":
    main()
