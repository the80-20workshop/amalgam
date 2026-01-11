#!/bin/bash

# Neo-Darwin Build Script
# Build CAD parts for the Neo-Darwin project

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Config
CAD_DIR="parts"
STL_DIR="stl"
VENV_DIR=".venv"
PYPROJECT_FILE="pyproject.toml"
PARTS_LIST_SCRIPT="parts/list.py"

# Testing mode (use only corner_motorized.py for initial testing)
TEST_MODE="${TEST_MODE:-false}"

# Parts to build (each part: name:file:args)
# Format: "display_name:python_file:cli_args"
# These are fallback values if list.py is not available
PARTS=(
    "corner_front_left:corner_motorized:front_left"
    "corner_front_right:corner_motorized:front_right"
)

# Help function
show_help() {
    echo "Neo-Darwin Build Script"
    echo ""
    echo "Usage: $0 [command] [args...]"
    echo ""
    echo "Setup:"
    echo "  First time? Run: ./setup.sh"
    echo ""
    echo "Commands:"
    echo "  build [PARTS...]    Build specified parts"
    echo "  build_all              Build all parts"
    echo "  list                    List all available parts"
    echo "  clean                   Delete all STLs"
    echo "  help                    Show this help"
    echo ""
    echo "The script automatically:"
    echo "  - Checks for and activates .venv"
    echo "  - Installs dependencies if missing"
    echo "  - Discovers parts dynamically from parts/ directory"
    echo ""
    echo "Advanced options:"
    echo "  TEST_MODE=true        Only use corner_motorized.py (for testing)"
    echo ""
    echo "Parts available:"
    list_parts
    echo ""
    echo "Examples:"
    echo "  ./build.sh build corner_front_left"
    echo "  ./build.sh build corner_front_left corner_front_right"
    echo "  ./build.sh build corner_motorized:front_left"
    echo ""
    echo "  CLI args for parts: python <part_name>.py [args]"
    echo "  (Use this when not using build.sh wrapper)"
}

# Load dynamic parts list
load_parts_list() {
    PARTS=()

    # In test mode, only use corner_motorized.py
    if [ "$TEST_MODE" = "true" ]; then
        PARTS=(
            "corner_front_left:corner_motorized:front_left"
            "corner_front_right:corner_motorized:front_right"
        )
        echo -e "${YELLOW}Test mode: Using only corner_motorized.py${NC}"
        return
    fi

    # Try dynamic discovery
    if [ -f "$PARTS_LIST_SCRIPT" ]; then
        # Parse output from parts/list.py
        while IFS= read -r part_spec; do
            [[ "$part_spec" =~ ^[A-Za-z_].*: ]] && PARTS+=("$part_spec")
        done < <($PYTHON_CMD "$PARTS_LIST_SCRIPT" 2>/dev/null)
    fi

    # If dynamic list is empty, use hardcoded fallback
    if [ ${#PARTS[@]} -eq 0 ]; then
        echo -e "${YELLOW}No parts found in parts/, using fallback list${NC}"
        PARTS=(
            "corner_front_left:corner_motorized:front_left"
            "corner_front_right:corner_motorized:front_right"
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

# Install dependencies if needed
ensure_dependencies() {
    if ! python -c "import build123d" 2>/dev/null; then
        echo -e "${YELLOW}Dependencies not found, installing...${NC}"

        # Try uv first if available
        if command -v uv &> /dev/null; then
            # uv prefers pyproject.toml (modern standard)
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

# Build single part
build_part() {
    local part_spec="$1"
    local display_name="${part_spec%%:*}"
    local remaining="${part_spec#*:}"
    local python_file="${remaining%%:*}"
    local cli_args="${remaining#*:}"

    echo -e "${BLUE}Building: $display_name${NC}"

    # Check if file exists
    if [ ! -f "$CAD_DIR/${python_file}.py" ]; then
        echo -e "${RED}Error: File not found: $CAD_DIR/${python_file}.py${NC}"
        return 1
    fi

    # Change to parts directory
    cd "$CAD_DIR" || return 1

    # Run Python script with arguments
    $PYTHON_CMD "${python_file}.py" $cli_args
    local exit_code=$?

    # Check if STL was created
    if [ -f "../$STL_DIR/${display_name}.stl" ]; then
        echo -e "${GREEN}Success: ${display_name}.stl created${NC}"
        local stl_size=$(du -h "../$STL_DIR/${display_name}.stl" | cut -f1)
        echo -e "  Size: $stl_size${NC}"
    else
        echo -e "${RED}Failed: ${display_name}.stl not created${NC}"
        exit_code=1
    fi

    cd - > /dev/null
    return $exit_code
}

# Build all parts
build_all() {
    echo -e "${BLUE}Building all parts...${NC}"

    load_parts_list

    local success_count=0
    local total=${#PARTS[@]}

    for part in "${PARTS[@]}"; do
        build_part "$part"

        if [ $? -eq 0 ]; then
            success_count=$((success_count + 1))
        fi
    done

    echo ""
    echo -e "${GREEN}Build summary:${NC}"
    echo -e "  Success: $success_count / $total${NC}"
    echo ""
    echo -e "${BLUE}STL files location: $STL_DIR/${NC}"
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

# Clean all STLs
clean_all() {
    echo -e "${YELLOW}Cleaning all STLs...${NC}"
    rm -f ${STL_DIR}/*.stl
    echo -e "${GREEN}Done!${NC}"
}

# Create STL directory if not exists
mkdir -p "$STL_DIR"

# Main execution
case "${1:-help}" in
    build)
        shift
        setup_environment
        load_parts_list
        if [ $# -eq 0 ]; then
            build_all
        else
            build_specific "$@"
        fi
        ;;
    build_all)
        setup_environment
        build_all
        ;;
    list)
        list_parts
        ;;
    clean)
        clean_all
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        show_help
        exit 1
        ;;
esac
