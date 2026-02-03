#!/usr/bin/env python3
"""
Generate ACKNOWLEDGEMENTS.md by scanning the codebase for references.

Scans all documentation and code for:
- URLs and links
- Heritage references (RepRap, Voron, Prusa, etc.)
- Tool/technology mentions

Groups findings by source file and category.

Usage:
    python scripts/generate_acknowledgements.py
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# =============================================================================
# Configuration
# =============================================================================

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_FILE = REPO_ROOT / "ACKNOWLEDGEMENTS.md"

# File patterns to scan
SCAN_PATTERNS = [
    "**/*.md",
    "**/*.py",
    "**/*.qmd",
    "**/*.sh",
    "**/*.cfg",
]

# Directories to skip
SKIP_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules",
    ".pytest_cache", "build", "dist", "*.egg-info",
}

# =============================================================================
# URL and Reference Extraction
# =============================================================================

# Regex for URLs
URL_PATTERN = re.compile(
    r'https?://[^\s<>\"\'\)\]\}]+',
    re.IGNORECASE
)

# Regex for markdown links [text](url)
MD_LINK_PATTERN = re.compile(
    r'\[([^\]]+)\]\(([^)]+)\)',
    re.IGNORECASE
)

# Heritage/project keywords to look for
HERITAGE_KEYWORDS = {
    "reprap": "RepRap Project",
    "darwin": "RepRap Darwin",
    "mendel": "RepRap Mendel",
    "prusa": "Prusa Research",
    "voron": "Voron Design",
    "klipper": "Klipper Firmware",
    "marlin": "Marlin Firmware",
    "ender": "Creality Ender",
    "anet": "Anet",
    "e3d": "E3D",
    "openscad": "OpenSCAD",
    "build123d": "build123d",
}

# =============================================================================
# Scanning Functions
# =============================================================================

def should_skip(path: Path) -> bool:
    """Check if path should be skipped."""
    for part in path.parts:
        if part in SKIP_DIRS or part.endswith(".egg-info"):
            return True
    return False


def extract_urls(content: str) -> list[tuple[str, str]]:
    """Extract URLs from content. Returns list of (text, url) tuples."""
    results = []

    # First get markdown links with text
    for match in MD_LINK_PATTERN.finditer(content):
        text, url = match.groups()
        if url.startswith("http"):
            results.append((text.strip(), url.strip()))

    # Then get plain URLs (that aren't already in markdown links)
    md_urls = {url for _, url in results}
    for match in URL_PATTERN.finditer(content):
        url = match.group().rstrip(".,;:)")
        if url not in md_urls:
            # Try to get domain as text
            domain = re.search(r'https?://(?:www\.)?([^/]+)', url)
            text = domain.group(1) if domain else url
            results.append((text, url))

    return results


def extract_heritage_mentions(content: str) -> set[str]:
    """Find mentions of heritage projects."""
    found = set()
    content_lower = content.lower()
    for keyword, name in HERITAGE_KEYWORDS.items():
        if keyword in content_lower:
            found.add(name)
    return found


def scan_file(filepath: Path) -> dict:
    """Scan a single file for references."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"  Warning: Could not read {filepath}: {e}")
        return {}

    return {
        "urls": extract_urls(content),
        "heritage": extract_heritage_mentions(content),
    }


def scan_codebase() -> dict:
    """Scan entire codebase for references."""
    results = defaultdict(lambda: {"urls": [], "heritage": set()})

    for pattern in SCAN_PATTERNS:
        for filepath in REPO_ROOT.glob(pattern):
            if should_skip(filepath):
                continue

            rel_path = filepath.relative_to(REPO_ROOT)
            print(f"Scanning: {rel_path}")

            file_results = scan_file(filepath)
            if file_results.get("urls") or file_results.get("heritage"):
                results[str(rel_path)]["urls"].extend(file_results.get("urls", []))
                results[str(rel_path)]["heritage"].update(file_results.get("heritage", set()))

    return dict(results)


# =============================================================================
# Categorization
# =============================================================================

def categorize_url(url: str) -> str:
    """Categorize a URL by its domain/purpose."""
    url_lower = url.lower()

    if "github.com" in url_lower:
        if "klipper" in url_lower:
            return "Firmware"
        elif "voron" in url_lower:
            return "3D Printer Projects"
        elif "ellis" in url_lower or "print-tuning" in url_lower:
            return "Calibration & Tuning"
        elif "build123d" in url_lower:
            return "CAD Tools"
        elif "3dbenchy" in url_lower:
            return "Calibration & Tuning"
        else:
            return "GitHub Projects"
    elif "klipper3d.org" in url_lower:
        return "Firmware"
    elif "prusa" in url_lower:
        return "3D Printer Projects"
    elif "voron" in url_lower:
        return "3D Printer Projects"
    elif "reprap" in url_lower:
        return "Heritage"
    elif "aliexpress" in url_lower or "amazon" in url_lower:
        return "Suppliers"
    elif "printables" in url_lower or "thingiverse" in url_lower:
        return "Model Repositories"
    elif "youtube" in url_lower or "youtu.be" in url_lower:
        return "Educational"
    elif "ellis3dp" in url_lower or "teachingtech" in url_lower:
        return "Calibration & Tuning"
    elif "quarto" in url_lower:
        return "Documentation Tools"
    else:
        return "Other"


def dedupe_urls(all_urls: list[tuple[str, str]]) -> dict[str, list[tuple[str, str]]]:
    """Deduplicate URLs and categorize them."""
    seen = {}
    for text, url in all_urls:
        # Normalize URL
        url_clean = url.rstrip("/")
        if url_clean not in seen:
            seen[url_clean] = text

    # Categorize
    categorized = defaultdict(list)
    for url, text in seen.items():
        category = categorize_url(url)
        categorized[category].append((text, url))

    # Sort each category
    for category in categorized:
        categorized[category].sort(key=lambda x: x[0].lower())

    return dict(categorized)


# =============================================================================
# Output Generation
# =============================================================================

def generate_acknowledgements(scan_results: dict) -> str:
    """Generate the ACKNOWLEDGEMENTS.md content."""

    # Collect all URLs and heritage mentions
    all_urls = []
    all_heritage = set()
    files_with_refs = []

    for filepath, data in sorted(scan_results.items()):
        all_urls.extend(data["urls"])
        all_heritage.update(data["heritage"])
        if data["urls"] or data["heritage"]:
            files_with_refs.append(filepath)

    categorized_urls = dedupe_urls(all_urls)

    # Build the document
    lines = []

    lines.append("# Acknowledgements")
    lines.append("")
    lines.append("Amalgam stands on the shoulders of giants. This project would not be possible")
    lines.append("without the incredible work of the open source community, makers, and pioneers")
    lines.append("who came before us.")
    lines.append("")
    lines.append(f"*Auto-generated on {datetime.now().strftime('%Y-%m-%d')} by scanning the codebase.*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Heritage section
    lines.append("## Heritage & Inspiration")
    lines.append("")
    lines.append("Amalgam is a 2026 RepRap-inspired reference specification. We acknowledge")
    lines.append("the pioneering work of these projects and communities:")
    lines.append("")

    heritage_descriptions = {
        "RepRap Project": "The original self-replicating 3D printer project that started it all (2005)",
        "RepRap Darwin": "First RepRap design - box frame with threaded rod skeleton",
        "RepRap Mendel": "Introduced the 'plough' X-carriage design we use",
        "Prusa Research": "Josef Prusa's contributions to i3 design and the maker community",
        "Voron Design": "Modern CoreXY designs, dual rod motion, and excellent documentation",
        "Klipper Firmware": "Advanced firmware with Input Shaper and Pressure Advance",
        "E3D": "V6 hotend and innovations in extrusion technology",
        "Creality Ender": "Popularized affordable 3D printing, common donor printers",
        "Anet": "A8 and other printers that serve as donor sources",
        "build123d": "Modern Python CAD library we use for parametric parts",
    }

    for name in sorted(all_heritage):
        desc = heritage_descriptions.get(name, "")
        if desc:
            lines.append(f"- **{name}**: {desc}")
        else:
            lines.append(f"- **{name}**")
    lines.append("")

    # Tools & Technologies section
    lines.append("---")
    lines.append("")
    lines.append("## Tools & Technologies")
    lines.append("")
    lines.append("Amalgam is built with these excellent open source tools:")
    lines.append("")
    lines.append("### CAD & Design")
    lines.append("- **[build123d](https://github.com/gumyr/build123d)**: Python BREP CAD library for parametric parts")
    lines.append("- **[OpenCASCADE](https://www.opencascade.com/)**: Geometry kernel behind build123d")
    lines.append("")
    lines.append("### Firmware & Control")
    lines.append("- **[Klipper](https://www.klipper3d.org/)**: Advanced 3D printer firmware")
    lines.append("- **[Moonraker](https://github.com/Arksine/moonraker)**: API for Klipper")
    lines.append("- **[Mainsail](https://docs.mainsail.xyz/)** / **[Fluidd](https://docs.fluidd.xyz/)**: Web interfaces")
    lines.append("")
    lines.append("### Documentation")
    lines.append("- **[Quarto](https://quarto.org/)**: Scientific publishing system for docs")
    lines.append("- **[MkDocs](https://www.mkdocs.org/)**: Documentation site generator")
    lines.append("")
    lines.append("### Development")
    lines.append("- **[Python](https://www.python.org/)**: Primary language for CAD and scripts")
    lines.append("- **[uv](https://github.com/astral-sh/uv)**: Fast Python package manager")
    lines.append("- **[Git](https://git-scm.com/)**: Version control")
    lines.append("")
    lines.append("### AI Assistance")
    lines.append("- **[Claude](https://www.anthropic.com/claude)** (Anthropic): Primary AI assistant for development")
    lines.append("- **[ChatGPT](https://openai.com/chatgpt)** (OpenAI): Research and brainstorming")
    lines.append("- **[Gemini](https://gemini.google.com/)** (Google): Additional research")
    lines.append("")

    # External Resources by category
    lines.append("---")
    lines.append("")
    lines.append("## External Resources")
    lines.append("")
    lines.append("Links referenced throughout the documentation and code:")
    lines.append("")

    # Define category order
    category_order = [
        "Heritage",
        "3D Printer Projects",
        "Firmware",
        "Calibration & Tuning",
        "CAD Tools",
        "Documentation Tools",
        "Model Repositories",
        "GitHub Projects",
        "Educational",
        "Suppliers",
        "Other",
    ]

    for category in category_order:
        if category in categorized_urls:
            lines.append(f"### {category}")
            lines.append("")
            for text, url in categorized_urls[category]:
                # Clean up text
                text_clean = text[:60] + "..." if len(text) > 60 else text
                lines.append(f"- [{text_clean}]({url})")
            lines.append("")

    # Files scanned section
    lines.append("---")
    lines.append("")
    lines.append("## Source Files")
    lines.append("")
    lines.append(f"References extracted from {len(files_with_refs)} files:")
    lines.append("")
    lines.append("<details>")
    lines.append("<summary>Click to expand file list</summary>")
    lines.append("")
    for filepath in sorted(files_with_refs):
        lines.append(f"- `{filepath}`")
    lines.append("")
    lines.append("</details>")
    lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("If we've missed crediting your work, please open an issue or PR.")
    lines.append("We want to give proper attribution to everyone whose work we build upon.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append('*"If I have seen further, it is by standing on the shoulders of giants."*')
    lines.append("— Isaac Newton (and Bernard of Chartres)")
    lines.append("")

    return "\n".join(lines)


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 60)
    print("Generating ACKNOWLEDGEMENTS.md")
    print("=" * 60)
    print()

    print("Scanning codebase...")
    results = scan_codebase()

    print()
    print(f"Found references in {len(results)} files")

    print()
    print("Generating acknowledgements...")
    content = generate_acknowledgements(results)

    print(f"Writing to {OUTPUT_FILE}")
    OUTPUT_FILE.write_text(content)

    print()
    print("Done!")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
