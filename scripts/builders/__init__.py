"""
Amalgam Build Orchestration

Modules for building different outputs from configuration:
- config_builder: Generate config.py from inventory
- stl_builder: Build STL files from CAD scripts
- docs_builder: Generate documentation with Quarto
- analysis_runner: Run engineering analysis

Usage:
    from builders import build_all, build_stls, build_docs, run_analysis

Each builder can run independently or be orchestrated together.
"""

from .config_builder import generate_config, save_config
from .stl_builder import build_stls, list_parts, clean_stls
from .docs_builder import export_quarto_vars, build_docs, preview_docs
from .analysis_runner import run_full_analysis, AnalysisReport

__all__ = [
    # Config
    "generate_config",
    "save_config",
    # STLs
    "build_stls",
    "list_parts",
    "clean_stls",
    # Docs
    "export_quarto_vars",
    "build_docs",
    "preview_docs",
    # Analysis
    "run_full_analysis",
    "AnalysisReport",
]
