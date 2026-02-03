#!/usr/bin/env python3

"""
Part Selector for Amalgam Build System
Lists available parts dynamically from parts/ directory
"""

import os
import sys
from pathlib import Path


def get_parts():
    """Dynamically discover all Python parts in parts/ directory"""
    parts_dir = Path("parts")
    parts = []

    if not parts_dir.exists():
        print("Error: parts/ directory not found")
        return []

    # Find all Python files in parts/ and its subdirectories
    for py_file in parts_dir.rglob("*.py"):
        # Skip __pycache__ and __init__.py
        if "__pycache__" in str(py_file) or py_file.name == "__init__.py":
            continue
        name = py_file.stem
        parts.append(name)

    return sorted(set(parts))


def main():
    """Main function - list parts and optionally select"""
    parts = get_parts()

    if not parts:
        print("No parts found in parts/ directory")
        sys.exit(1)

    # Group parts by prefix (frame, extruder, bed, etc.)
    categories = {}
    for part in parts:
        prefix = part.split("_")[0] if "_" in part else "misc"
        if prefix not in categories:
            categories[prefix] = []
        categories[prefix].append(part)

    print(f"Available parts ({len(parts)} total):")
    print("=" * 50)

    for category, part_list in categories.items():
        print(f"\n{category.upper()}:")
        for part in part_list:
            print(f"  - {part}")

    print("\n" + "=" * 50)
    print("\nUsage:")
    print("  Build all:    ./build.sh build_all")
    print("  Build specific: ./build.sh build <part_name>")
    print("  Example:      ./build.sh build corner_front_left")
    print("\n  Multiple parts: ./build.sh build part1 part2 part3")
    print("  Example:      ./build.sh build corner_front_left corner_front_right")


def get_parts_for_build():
    """Get parts in format: name:file:args for build.sh"""
    parts = get_parts()
    for part in parts:
        print(f"{part}:{part}:")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--build-format":
        get_parts_for_build()
    else:
        main()
