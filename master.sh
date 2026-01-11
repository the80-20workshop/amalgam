#!/bin/bash

# Neo-Darwin Master Build Script
# Supports chaining: ./master.sh corner_1 corner_2 corner_3
# Or building all: ./master.sh all
# Follows Voron-style naming conventions where possible

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Config
CAD_DIR="cad/parts"
STL_DIR="cad/stl"

# Parts to build
PARTS=(
    "corner_front_left"
    "corner_front_right"
    "corner_back_left"
    "corner_back_right"
    "z_puck_back_center"
    "spider_hub"
    "spider_arm"
    "top_corner_tl"
    "top_corner_tr"
    "top_corner_bl"
    "top_corner_br"
)

# Help function
show_help() {
    echo "Neo-Darwin Master Build Script"
    echo ""
    echo "Usage: $0 [command] [args...]"
    echo ""
    echo "Commands:"
    echo "  build [PARTS...]    Build specified parts"
    echo "  build_all              Build all parts"
    echo "  list                    List all available parts"
    echo "  clean                   Delete all STLs"
    echo ""
    echo "Parts available:"
    for part in "${PARTS[@]}"; do
        echo "  $part"
    done
}

# List all parts
list_parts() {
    echo -e "${BLUE}Available parts:${NC}"
    for part in "${PARTS[@]}"; do
        echo "  - $part"
    done
}

# Build single part
build_part() {
    local part="$1"

    echo -e "${BLUE}Building: $part${NC}"

    # Check if file exists
    if [ ! -f "$CAD_DIR/${part}.py" ]; then
        echo -e "${RED}Error: File not found: $CAD_DIR/${part}.py${NC}"
        return 1
    fi

    # Change to cad directory
    cd "$(dirname "$CAD_DIR/${part}.py")" || return 1

    # Run Python script
    python "${part}.py"

    # Check if STL was created
    if [ -f "../../$STL_DIR/${part}.stl" ]; then
        echo -e "${GREEN}Success: ${part}.stl created${NC}"
        local stl_size=$(du -h "../../$STL_DIR/${part}.stl" | cut -f1)
        echo -e "  Size: $stl_size${NC}"
    else
        echo -e "${RED}Failed: ${part}.stl not created${NC}"
        return 1
    fi

    cd - > /dev/null
}

# Build all parts
build_all() {
    echo -e "${BLUE}Building all parts...${NC}"

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

# Clean all STLs
clean_all() {
    echo -e "${YELLOW}Cleaning all STLs...${NC}"
    rm -f ${STL_DIR}/*.stl
    echo -e "${GREEN}Done!${NC}"
}

# Main execution
case "${1:-help}" in
    build)
        shift
        if [ $# -eq 0 ]; then
            echo -e "${RED}Error: build requires at least one part${NC}"
            show_help
            exit 1
        fi
        build_all
        ;;
    list)
        list_parts
        ;;
    clean)
        clean_all
        ;;
    help|*)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        show_help
        exit 1
        ;;
esac
