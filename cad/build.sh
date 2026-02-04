#!/bin/bash

# Amalgam Build Script
# Build CAD parts for the Amalgam project

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Config
PARTS_DIR="amalgam/parts"
EXPORTS_DIR="exports"
STL_DIR="$EXPORTS_DIR/stl"  # Default format location
VENV_DIR=".venv"
PYPROJECT_FILE="pyproject.toml"
PARTS_LIST_SCRIPT="utilities/list.py"

# Export format (can be overridden with --format flag)
# Options: stl, step, 3mf, brep, gltf, all
EXPORT_FORMAT="${EXPORT_FORMAT:-stl}"
EXPORT_DRAWINGS="${EXPORT_DRAWINGS:-false}"

# Testing mode (use only corner parts for initial testing)
TEST_MODE="${TEST_MODE:-false}"

# Parts to build (each part: name:path:args)
# Format: "display_name:relative_path:cli_args"
# These are fallback values if list.py is not available
PARTS=(
    "corner_front_left:frame/corner_front_left:"
    "corner_standard:frame/corner_standard:"
)

# Help function
show_help() {
    echo "Amalgam Build Script"
    echo ""
    echo "Usage: $0 [command] [options] [args...]"
    echo ""
    echo "Setup:"
    echo "  First time? Run: ./setup.sh"
    echo ""
    echo "Commands:"
    echo "  build [PARTS...]    Build specified parts"
    echo "  build_all           Build all parts"
    echo "  list                List all available parts"
    echo "  clean               Delete all exported files"
    echo "  formats             Show available export formats"
    echo "  help                Show this help"
    echo ""
    echo "Export Options:"
    echo "  --format FORMAT     Export format: stl, step, 3mf, brep, gltf, all"
    echo "  --drawings          Also generate technical drawings (SVG/PDF)"
    echo ""
    echo "The script automatically:"
    echo "  - Checks for and activates .venv"
    echo "  - Installs dependencies if missing"
    echo "  - Discovers parts dynamically from amalgam/parts/ directory"
    echo ""
    echo "Output Directory:"
    echo "  exports/stl/        STL files (3D printing)"
    echo "  exports/step/       STEP files (CAD interchange)"
    echo "  exports/3mf/        3MF files (modern slicers)"
    echo "  exports/brep/       BREP files (build123d native)"
    echo "  exports/gltf/       glTF files (web/3D viewers)"
    echo "  exports/drawings/   Technical drawings (SVG/PDF)"
    echo ""
    echo "Environment Variables:"
    echo "  EXPORT_FORMAT=step  Set default export format"
    echo "  EXPORT_DRAWINGS=true  Always generate drawings"
    echo "  TEST_MODE=true      Only use test part list"
    echo ""
    echo "Parts available:"
    list_parts
    echo ""
    echo "Examples:"
    echo "  ./build.sh build maker_coin                    # Default format (STL)"
    echo "  ./build.sh build maker_coin --format step      # Export as STEP"
    echo "  ./build.sh build maker_coin --format all       # All formats"
    echo "  ./build.sh build_all --format step --drawings  # STEP + drawings"
}

# Load dynamic parts list
load_parts_list() {
    PARTS=()

    # In test mode, only use corner parts
    if [ "$TEST_MODE" = "true" ]; then
        PARTS=(
            "corner_front_left:frame/corner_front_left:"
        )
        echo -e "${YELLOW}Test mode: Using test part list${NC}"
        return
    fi

    # Try dynamic discovery
    if [ -f "$PARTS_LIST_SCRIPT" ]; then
        # Parse output from utilities/list.py in build format
        while IFS= read -r part_spec; do
            [[ "$part_spec" =~ ^[A-Za-z_].*: ]] && PARTS+=("$part_spec")
        done < <($PYTHON_CMD "$PARTS_LIST_SCRIPT" --build-format 2>/dev/null)
    fi

    # If dynamic list is empty, use hardcoded fallback
    if [ ${#PARTS[@]} -eq 0 ]; then
        echo -e "${YELLOW}No parts found, using fallback list${NC}"
        PARTS=(
            "corner_front_left:frame/corner_front_left:"
        )
    fi
}

# Check and activate venv
check_venv() {
    # Check if already in venv
    if [ -n "$VIRTUAL_ENV" ]; then
        echo -e "${GREEN}Virtual environment already active${NC}"
        PYTHON_CMD="python"
        return 0
    fi

    # Check if venv exists
    if [ -f "$VENV_DIR/bin/activate" ]; then
        source "$VENV_DIR/bin/activate"
        echo -e "${GREEN}Activated virtual environment${NC}"
        PYTHON_CMD="python"
        return 0
    fi

    # No venv found
    return 1
}

# Setup environment (venv + dependencies)
setup_environment() {
    # Try to activate existing venv
    if ! check_venv; then
        echo -e "${YELLOW}No virtual environment found${NC}"
        echo -e "${YELLOW}Run ./setup.sh to create one${NC}"
        exit 1
    fi

    # Ensure dependencies are installed
    ensure_dependencies
}

# Install dependencies if needed
ensure_dependencies() {
    if ! python -c "import build123d" 2>/dev/null; then
        echo -e "${YELLOW}Dependencies not found, installing...${NC}"

        # Try uv first if available
        if command -v uv &> /dev/null; then
            if [ -f "$PYPROJECT_FILE" ]; then
                uv pip install -q -e .
            else
                echo -e "${RED}Error: $PYPROJECT_FILE not found${NC}"
                exit 1
            fi
        else
            # Fallback to pip with pyproject.toml
            if [ -f "$PYPROJECT_FILE" ]; then
                pip install -q -e .
            else
                echo -e "${RED}Error: $PYPROJECT_FILE not found${NC}"
                exit 1
            fi
        fi

        echo -e "${GREEN}Dependencies installed${NC}"
    else
        echo -e "${GREEN}Dependencies already installed${NC}"
    fi
}

# List all parts (dynamic or fallback)
list_parts() {
    echo -e "${BLUE}Available parts:${NC}"

    # Try dynamic discovery first
    if [ -f "$PARTS_LIST_SCRIPT" ]; then
        $PYTHON_CMD "$PARTS_LIST_SCRIPT"
        return
    fi

    # Fallback to hardcoded list
    for part in "${PARTS[@]}"; do
        name="${part%%:*}"
        echo "  - $name"
    done
}

# Show available export formats
show_formats() {
    echo -e "${BLUE}Available Export Formats:${NC}"
    echo ""
    echo "3D Formats:"
    echo "  stl    Standard 3D printing format (mesh)"
    echo "  step   CAD interchange - Fusion 360, FreeCAD, SolidWorks (BREP)"
    echo "  3mf    Modern slicer format with metadata (mesh)"
    echo "  brep   build123d native format (exact geometry)"
    echo "  gltf   Web/3D viewer format (binary .glb)"
    echo "  all    Export all 3D formats"
    echo ""
    echo "Technical Drawings (with --drawings flag):"
    echo "  SVG    Vector graphics, scalable"
    echo "  PDF    Print-ready (requires cairosvg, inkscape, or rsvg-convert)"
    echo ""
    echo "Current default: $EXPORT_FORMAT"
    echo ""
    echo "Set default in config.py:"
    echo "  EXPORT_FORMAT = \"step\""
    echo "  EXPORT_DRAWINGS = True"
}

# Parse command line options (call before processing commands)
parse_options() {
    PARTS_ARGS=()

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --format)
                shift
                if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
                    EXPORT_FORMAT="$1"
                    shift
                else
                    echo -e "${RED}Error: --format requires a value${NC}"
                    exit 1
                fi
                ;;
            --format=*)
                EXPORT_FORMAT="${1#*=}"
                shift
                ;;
            --drawings)
                EXPORT_DRAWINGS="true"
                shift
                ;;
            *)
                PARTS_ARGS+=("$1")
                shift
                ;;
        esac
    done

    # Export these as environment variables for Python scripts
    export EXPORT_FORMAT
    export EXPORT_DRAWINGS
}

# Build single part
build_part() {
    local part_spec="$1"
    local display_name="${part_spec%%:*}"
    local remaining="${part_spec#*:}"
    local rel_path="${remaining%%:*}"
    local cli_args="${remaining#*:}"

    echo -e "${BLUE}Building: $display_name (format: $EXPORT_FORMAT)${NC}"

    local full_path="${PARTS_DIR}/${rel_path}.py"

    # Check if file exists
    if [ ! -f "$full_path" ]; then
        echo -e "${RED}Error: File not found: $full_path${NC}"
        return 1
    fi

    # Run Python script from cad/ directory (so package imports work)
    # PYTHONPATH=. ensures config.py and amalgam package are importable
    # EXPORT_FORMAT and EXPORT_DRAWINGS are passed via environment
    PYTHONPATH=. $PYTHON_CMD "$full_path" $cli_args
    local exit_code=$?

    # Check for exported files in the new exports/ directory structure
    local found_exports=false

    # Check STL (default)
    if [ -f "$EXPORTS_DIR/stl/${display_name}.stl" ]; then
        found_exports=true
        local file_size=$(du -h "$EXPORTS_DIR/stl/${display_name}.stl" | cut -f1)
        echo -e "${GREEN}  STL: ${display_name}.stl ($file_size)${NC}"
    fi

    # Check STEP
    if [ -f "$EXPORTS_DIR/step/${display_name}.step" ]; then
        found_exports=true
        local file_size=$(du -h "$EXPORTS_DIR/step/${display_name}.step" | cut -f1)
        echo -e "${GREEN}  STEP: ${display_name}.step ($file_size)${NC}"
    fi

    # Check 3MF
    if [ -f "$EXPORTS_DIR/3mf/${display_name}.3mf" ]; then
        found_exports=true
        local file_size=$(du -h "$EXPORTS_DIR/3mf/${display_name}.3mf" | cut -f1)
        echo -e "${GREEN}  3MF: ${display_name}.3mf ($file_size)${NC}"
    fi

    # Check BREP
    if [ -f "$EXPORTS_DIR/brep/${display_name}.brep" ]; then
        found_exports=true
        local file_size=$(du -h "$EXPORTS_DIR/brep/${display_name}.brep" | cut -f1)
        echo -e "${GREEN}  BREP: ${display_name}.brep ($file_size)${NC}"
    fi

    # Check glTF
    if [ -f "$EXPORTS_DIR/gltf/${display_name}.glb" ]; then
        found_exports=true
        local file_size=$(du -h "$EXPORTS_DIR/gltf/${display_name}.glb" | cut -f1)
        echo -e "${GREEN}  glTF: ${display_name}.glb ($file_size)${NC}"
    fi

    # Check drawings
    if [ -f "$EXPORTS_DIR/drawings/${display_name}_drawing.svg" ]; then
        found_exports=true
        echo -e "${GREEN}  Drawing: ${display_name}_drawing.svg${NC}"
    fi

    if [ "$found_exports" = false ]; then
        echo -e "${YELLOW}  Note: No exports found in expected locations${NC}"
    fi

    return $exit_code
}

# Build all parts
build_all() {
    echo -e "${BLUE}Building all parts...${NC}"
    echo -e "  Format: $EXPORT_FORMAT"
    if [ "$EXPORT_DRAWINGS" = "true" ]; then
        echo -e "  Drawings: enabled"
    fi
    echo ""

    load_parts_list

    local success_count=0
    local total=${#PARTS[@]}

    for part in "${PARTS[@]}"; do
        if build_part "$part"; then
            success_count=$((success_count + 1))
        fi
    done

    echo ""
    echo -e "${GREEN}Build summary:${NC}"
    echo -e "  Success: $success_count / $total"
    echo -e "  Format: $EXPORT_FORMAT"
    echo ""
    echo -e "${BLUE}Export location: $EXPORTS_DIR/${NC}"
}

# Build specific parts
build_specific() {
    local parts_to_build=("$@")
    local found=0

    for target in "${parts_to_build[@]}"; do
        for part in "${PARTS[@]}"; do
            local display_name="${part%%:*}"
            if [ "$display_name" = "$target" ]; then
                build_part "$part"
                found=1
                break
            fi
        done

        if [ $found -eq 0 ]; then
            echo -e "${RED}Error: Part '$target' not found${NC}"
            list_parts
            exit 1
        fi
        found=0
    done
}

# Clean all exported files
clean_all() {
    echo -e "${YELLOW}Cleaning all exports...${NC}"

    if [ -d "$EXPORTS_DIR" ]; then
        rm -f "$EXPORTS_DIR/stl"/*.stl 2>/dev/null
        rm -f "$EXPORTS_DIR/step"/*.step 2>/dev/null
        rm -f "$EXPORTS_DIR/3mf"/*.3mf 2>/dev/null
        rm -f "$EXPORTS_DIR/brep"/*.brep 2>/dev/null
        rm -f "$EXPORTS_DIR/gltf"/*.glb 2>/dev/null
        rm -f "$EXPORTS_DIR/drawings"/*.svg 2>/dev/null
        rm -f "$EXPORTS_DIR/drawings"/*.pdf 2>/dev/null
        echo -e "  Cleaned: $EXPORTS_DIR/"
    fi

    echo -e "${GREEN}Done!${NC}"
}

# Create export directories
mkdir -p "$EXPORTS_DIR/stl"
mkdir -p "$EXPORTS_DIR/step"
mkdir -p "$EXPORTS_DIR/3mf"
mkdir -p "$EXPORTS_DIR/brep"
mkdir -p "$EXPORTS_DIR/gltf"
mkdir -p "$EXPORTS_DIR/drawings"

# Main execution
COMMAND="${1:-help}"
shift 2>/dev/null || true

# Parse options from remaining arguments
parse_options "$@"

case "$COMMAND" in
    build)
        setup_environment
        load_parts_list
        if [ ${#PARTS_ARGS[@]} -eq 0 ]; then
            echo -e "${RED}Error: No parts specified${NC}"
            echo "Usage: ./build.sh build PART_NAME [--format FORMAT]"
            list_parts
            exit 1
        else
            build_specific "${PARTS_ARGS[@]}"
        fi
        ;;
    build_all)
        setup_environment
        build_all
        ;;
    list)
        setup_environment
        list_parts
        ;;
    formats)
        show_formats
        ;;
    clean)
        clean_all
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown command: $COMMAND${NC}"
        show_help
        exit 1
        ;;
esac
