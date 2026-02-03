#!/usr/bin/env python3
"""
Download standard calibration STL files for printer calibration.

These are external community models used in the calibration process.
Amalgam-specific prints (maker coin, fidget bolt) are built with build123d.

Usage:
    python utilities/download_calibration.py
    # or
    ./utilities/download_calibration.py

Downloads to: cad/calibration/ (gitignored)
"""

import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

# =============================================================================
# Configuration
# =============================================================================

# Output directory (relative to cad/)
OUTPUT_DIR = Path("calibration")

# Calibration models with download URLs
# Priority: GitHub-hosted (stable), then fallback instructions
# Note: Thingiverse/Printables block automated downloads, so we use GitHub sources
CALIBRATION_MODELS = {
    # --- Klipper official test prints ---
    "ringing_tower": {
        "filename": "ringing_tower.stl",
        "description": "Ringing/ghosting test tower for Input Shaper",
        "purpose": "Tune Klipper Input Shaper settings",
        "urls": [
            "https://raw.githubusercontent.com/Klipper3d/klipper/master/docs/prints/ringing_tower.stl",
        ],
        "fallback_info": "Klipper GitHub: klipper/docs/prints/ringing_tower.stl",
    },
    "square_tower": {
        "filename": "square_tower.stl",
        "description": "Square tower for Pressure Advance tuning",
        "purpose": "Tune Klipper Pressure Advance settings",
        "urls": [
            "https://raw.githubusercontent.com/Klipper3d/klipper/master/docs/prints/square_tower.stl",
        ],
        "fallback_info": "Klipper GitHub: klipper/docs/prints/square_tower.stl",
    },
    # --- Voron Design test prints ---
    "voron_cube": {
        "filename": "voron_design_cube.stl",
        "description": "Voron Design Cube - calibration cube",
        "purpose": "Dimensional accuracy verification",
        "urls": [
            "https://raw.githubusercontent.com/VoronDesign/Voron-2/Voron2.4/STLs/Test_Prints/Voron_Design_Cube_v7.stl",
        ],
        "fallback_info": "Voron GitHub: VoronDesign/Voron-2/STLs/Test_Prints/",
    },
    # --- Ellis Print Tuning Guide test prints ---
    "first_layer_patch": {
        "filename": "first_layer_patch_0.2mm.stl",
        "description": "Ellis first layer patch (0.2mm layer height)",
        "purpose": "First layer calibration and bed level verification",
        "urls": [
            "https://raw.githubusercontent.com/AndrewEllis93/Print-Tuning-Guide/main/test_prints/first_layer_patches/First_Layer_Patch-0.2mm.stl",
        ],
        "fallback_info": "Ellis GitHub: AndrewEllis93/Print-Tuning-Guide/test_prints/",
    },
    "extrusion_multiplier_cube": {
        "filename": "extrusion_multiplier_cube.stl",
        "description": "Ellis extrusion multiplier test cube",
        "purpose": "Flow rate / extrusion multiplier calibration",
        "urls": [
            "https://raw.githubusercontent.com/AndrewEllis93/Print-Tuning-Guide/main/test_prints/extrusion_multiplier_cubes/EM_Cube-Unlabeled.stl",
        ],
        "fallback_info": "Ellis GitHub: AndrewEllis93/Print-Tuning-Guide/test_prints/",
    },
    # --- Manual downloads (no GitHub source) ---
    "benchy": {
        "filename": "3DBenchy.stl",
        "description": "3D Benchy - the classic torture test",
        "purpose": "Comprehensive print validation",
        "urls": [],  # Website requires JavaScript
        "fallback_info": "Download from https://www.3dbenchy.com/ (click Download)",
        "manual_only": True,
    },
    "temperature_tower": {
        "filename": "temperature_tower_pla.stl",
        "description": "Temperature tower for PLA (180-220C)",
        "purpose": "Find optimal printing temperature",
        "urls": [],  # Thingiverse blocks automated downloads
        "fallback_info": "Printables: printables.com/model/39810 (Smart Compact Temp Tower)",
        "manual_only": True,
    },
    "retraction_tower": {
        "filename": "retraction_test.stl",
        "description": "Retraction test tower",
        "purpose": "Tune retraction distance and speed",
        "urls": [],  # Thingiverse blocks automated downloads
        "fallback_info": "Printables: printables.com/model/46846 or search 'retraction test'",
        "manual_only": True,
    },
}

# =============================================================================
# Download Functions
# =============================================================================

def download_file(url: str, dest_path: Path, timeout: int = 30) -> bool:
    """
    Download a file from URL to destination path.
    Returns True on success, False on failure.
    """
    try:
        print(f"  Trying: {url[:60]}...")

        # Create request with browser-like headers
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; Amalgam-Calibration-Downloader/1.0)",
                "Accept": "*/*",
            }
        )

        with urllib.request.urlopen(request, timeout=timeout) as response:
            content = response.read()

            # Verify we got something that looks like an STL
            if len(content) < 100:
                print(f"  Warning: Downloaded file is suspiciously small ({len(content)} bytes)")
                return False

            # Check if it starts with 'solid' (ASCII STL) or is binary
            is_ascii_stl = content[:5].lower() == b"solid"
            is_binary_stl = len(content) > 84  # Minimum binary STL size

            if not (is_ascii_stl or is_binary_stl):
                # Might be HTML error page
                if b"<html" in content.lower() or b"<!doctype" in content.lower():
                    print(f"  Got HTML instead of STL (probably error page)")
                    return False

            # Write the file
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            with open(dest_path, "wb") as f:
                f.write(content)

            size_kb = len(content) / 1024
            print(f"  Success: {size_kb:.1f} KB")
            return True

    except urllib.error.HTTPError as e:
        print(f"  HTTP Error {e.code}: {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"  URL Error: {e.reason}")
        return False
    except TimeoutError:
        print(f"  Timeout after {timeout}s")
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False


def download_model(name: str, config: dict, output_dir: Path) -> tuple[bool, bool]:
    """
    Download a single calibration model, trying multiple URLs.
    Returns (success, is_manual) tuple.
    """
    dest_path = output_dir / config["filename"]
    is_manual = config.get("manual_only", False)

    print(f"\n{config['description']}")
    print(f"  Purpose: {config['purpose']}")

    # Skip if already downloaded
    if dest_path.exists():
        size_kb = dest_path.stat().st_size / 1024
        print(f"  Already exists: {dest_path.name} ({size_kb:.1f} KB)")
        return True, is_manual

    # Manual-only models
    if is_manual:
        print(f"  Manual download: {config['fallback_info']}")
        print(f"  Save to: {dest_path}")
        return False, True

    # Try each URL
    for url in config["urls"]:
        if download_file(url, dest_path):
            return True, False

    # All URLs failed
    print(f"  FAILED - Manual download needed:")
    print(f"  {config['fallback_info']}")
    print(f"  Save as: {dest_path}")
    return False, False


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 60)
    print("Amalgam Calibration STL Downloader")
    print("=" * 60)
    print()
    print("Downloads standard calibration models for printer tuning.")
    print("See docs/guides/calibration-guide.md for usage instructions.")
    print()

    # Determine output directory
    # Script can be run from cad/ or repo root
    if Path("amalgam").is_dir():
        # Running from cad/
        output_dir = OUTPUT_DIR
    elif Path("cad/amalgam").is_dir():
        # Running from repo root
        output_dir = Path("cad") / OUTPUT_DIR
    else:
        print("ERROR: Cannot determine project root.")
        print("Run from either 'cad/' or repository root directory.")
        sys.exit(1)

    print(f"Output directory: {output_dir}/")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Download each model
    results = {}
    for name, config in CALIBRATION_MODELS.items():
        results[name] = download_model(name, config, output_dir)

    # Summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)

    auto_success = sum(1 for ok, manual in results.values() if ok and not manual)
    already_have = sum(1 for ok, manual in results.values() if ok)
    manual_needed = sum(1 for ok, manual in results.values() if manual and not ok)
    failed = sum(1 for ok, manual in results.values() if not ok and not manual)

    auto_total = sum(1 for config in CALIBRATION_MODELS.values() if not config.get("manual_only"))
    manual_total = sum(1 for config in CALIBRATION_MODELS.values() if config.get("manual_only"))

    print(f"\nAuto-downloaded: {auto_success}/{auto_total} models")
    print(f"Already present: {already_have}/{len(results)} models")
    print(f"Manual download: {manual_needed} models need manual download")

    if manual_needed > 0:
        print("\nManual downloads needed (copy to calibration/ folder):")
        for name, (ok, manual) in results.items():
            if manual and not ok:
                config = CALIBRATION_MODELS[name]
                print(f"  - {config['filename']}")
                print(f"    {config['fallback_info']}")

    if failed > 0:
        print("\nFailed auto-downloads:")
        for name, (ok, manual) in results.items():
            if not ok and not manual:
                config = CALIBRATION_MODELS[name]
                print(f"  - {config['filename']}: {config['fallback_info']}")

    print()
    print("Next steps:")
    print("  1. Download any manual models listed above")
    print("  2. Slice and print calibration models")
    print("  3. Follow docs/guides/calibration-guide.md")
    print("  4. Print your victory prints: ./build.sh build maker_coin fidget_bolt")
    print()

    # Exit 0 if auto-downloads succeeded (manual ones are expected)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
