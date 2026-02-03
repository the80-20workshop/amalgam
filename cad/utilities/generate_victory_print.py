#!/usr/bin/env python3
"""
Generate Victory Print

Auto-generates the Amalgam maker coin with:
- Frame path from config.py (Scaffold/Mill/Lathe) + date, OR
- Random tagline if no config.py found

Usage:
    python generate_victory_print.py
"""

import sys
import random
from pathlib import Path
from datetime import datetime

# Add parent directory to path for config import
sys.path.insert(0, str(Path(__file__).parent.parent))

# Taglines for when no config.py exists (line1, line2)
TAGLINES = [
    ("Scavenger", "Built"),
    ("2 Donors", "1 Printer"),
    ("Built Not", "Bought"),
    ("RepRap", "Reborn"),
]

# Try to import config
try:
    import config
    HAS_CONFIG = True
except ImportError:
    HAS_CONFIG = False
    print("Warning: config.py not found, using default frame path")

# Import the maker coin
from parts.victory.amalgam_maker_coin import make_amalgam_coin
from build123d import export_stl

# Try to import show for interactive viewing
try:
    from ocp_vscode import show
    HAS_VIEWER = True
except ImportError:
    HAS_VIEWER = False


def detect_frame_path() -> str:
    """Detect frame path from config.py."""
    if not HAS_CONFIG:
        return "Amalgam"

    # Check for explicit FRAME_PATH setting
    frame_path = getattr(config, 'FRAME_PATH', None)
    if frame_path:
        return frame_path

    # Fallback: derive from DONOR_TYPE
    donor_type = getattr(config, 'DONOR_TYPE', None)
    if donor_type:
        donor_to_path = {
            'PRUSA_CLONE': 'Scaffold',
            'ANET_A8': 'Scaffold',
            'WANHAO': 'Scaffold',
            'ENDER_3': 'Mill',
            'CR_10': 'Mill',
            'AQUILA': 'Mill',
            'I3_MEGA': 'Lathe',
            'ARTILLERY': 'Lathe',
        }
        if donor_type.upper() in donor_to_path:
            return donor_to_path[donor_type.upper()]

    # Default
    return "Amalgam"


def get_date_string() -> str:
    """Get current date as YYYY-MM."""
    return datetime.now().strftime("%Y-%m")


def generate_victory_print(
    output_dir: Path = None,
    show_in_viewer: bool = True,
    use_tagline: bool = None,  # None = auto, True = force tagline, False = force path+date
) -> None:
    """Generate the victory print with auto-detected settings."""

    # Detect frame path and date
    frame_path = detect_frame_path()
    date_str = get_date_string()

    # Determine whether to use tagline or path+date
    if use_tagline is None:
        # Auto: use tagline if no config or frame_path is "Amalgam" (default)
        use_tagline = not HAS_CONFIG or frame_path == "Amalgam"

    if use_tagline:
        tagline = random.choice(TAGLINES)
        line1, line2 = tagline
        filename_base = f"amalgam_victory_coin_{date_str}"
    else:
        line1 = frame_path
        line2 = date_str
        filename_base = f"amalgam_victory_coin_{frame_path.lower()}_{date_str}"

    print("=" * 50)
    print("Amalgam Victory Print Generator")
    print("=" * 50)
    if use_tagline:
        print(f"Mode: Tagline (no config.py or default frame path)")
    else:
        print(f"Frame path: {frame_path}")
        print(f"Date: {date_str}")
    print(f"Bottom text: \"{line1}\" / \"{line2}\"")
    print()

    # Generate the coin
    print("Generating maker coin...")
    coin = make_amalgam_coin(
        bottom_text=line1,
        bottom_text_line2=line2,
        hole_enabled=True,  # Victory print should have lanyard hole
    )
    print("Coin generated successfully!")

    # Determine output path
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "stl"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Export to STL
    filename = f"{filename_base}.stl"
    stl_path = output_dir / filename

    try:
        export_stl(coin, str(stl_path))
        print(f"Exported: {stl_path}")
    except Exception as e:
        print(f"Could not export STL: {e}")

    # Show in viewer if available
    if show_in_viewer and HAS_VIEWER:
        print("Displaying in viewer...")
        show(coin)
    elif show_in_viewer:
        print("(Install ocp_vscode for interactive viewing)")

    return coin


if __name__ == "__main__":
    generate_victory_print()
