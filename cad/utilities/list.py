#!/usr/bin/env python3

"""
Part Selector for Amalgam Build System
Lists available parts dynamically from amalgam/parts/ directory
"""

import sys
from pathlib import Path


def get_parts():
    """Dynamically discover all Python parts in amalgam/parts/ directory"""
    parts_dir = Path("amalgam/parts")
    parts = []

    if not parts_dir.exists():
        print("Error: amalgam/parts/ directory not found")
        return []

    # Find all Python files in amalgam/parts/ and its subdirectories
    for py_file in parts_dir.rglob("*.py"):
        # Skip __pycache__ and __init__.py
        if "__pycache__" in str(py_file) or py_file.name == "__init__.py":
            continue

        # Get relative path from amalgam/parts/
        rel_path = py_file.relative_to(parts_dir)
        name = py_file.stem

        # Store as (name, relative_path_without_extension)
        path_str = str(rel_path.with_suffix(''))
        parts.append((name, path_str))

    return sorted(set(parts), key=lambda x: x[0])


def main():
    """Main function - list parts and optionally select"""
    parts = get_parts()

    if not parts:
        print("No parts found in amalgam/parts/ directory")
        sys.exit(1)

    # Group parts by subdirectory
    categories = {}
    for name, path in parts:
        # Get category from path (first directory)
        category = path.split('/')[0] if '/' in path else "misc"
        if category not in categories:
            categories[category] = []
        categories[category].append(name)

    print(f"Available parts ({len(parts)} total):")
    print("=" * 50)

    for category in sorted(categories.keys()):
        part_list = categories[category]
        print(f"\n{category.upper()}:")
        for part in sorted(part_list):
            print(f"  - {part}")

    print("\n" + "=" * 50)
    print("\nUsage:")
    print("  Build all:    ./build.sh build_all")
    print("  Build specific: ./build.sh build <part_name>")
    print("  Example:      ./build.sh build corner_front_left")
    print("\n  Multiple parts: ./build.sh build part1 part2 part3")
    print("  Example:      ./build.sh build corner_front_left corner_standard")


def get_parts_for_build():
    """Get parts in format: name:path:args for build.sh"""
    parts = get_parts()
    for name, path in parts:
        # Output format: display_name:relative_path:args
        print(f"{name}:{path}:")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--build-format":
        get_parts_for_build()
    else:
        main()
