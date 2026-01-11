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

# Voron-style names (optional alternative)
VORON_NAMES=(
    "z_motor_kit"
    "z_motor_bracket"
    "corner_bracket"
    "top_frame_corner"
)

# Help function
show_help() {
    echo "Neo-Darwin Master Build Script"
    echo ""
    echo "Usage: $0 [command] [args...]"
    echo ""
    echo "Commands:"
    echo "  build [PARTS...]    Build specified parts (chaining supported)"
    echo "  build_all              Build all parts"
    echo "  list                    List all available parts"
    echo "  clean                   Delete all STLs"
    echo ""
    echo "Parts available:"
    for part in "${PARTS[@]}"; do
        echo "    $part"
    done
    echo ""
    echo "Examples:"
    echo "  $0 build corner_front_left corner_front_right"
    echo "  $0 build_all"
    echo ""
    echo "Voron-style parts (not implemented yet):"
    for name in "${VORON_NAMES[@]}"; do
        echo "    $name"
    done

# List all parts
list_parts() {
    echo -e "${BLUE}Available parts:${NC}"
    for part in "${PARTS[@]}"; do
        echo "  - $part"
    done
}

# Build single part
build_part() {
    local part=$1

    echo -e "${BLUE}Building: $part${NC}"

    # Try motorized corner script first (supports location + mirror)
    if [[ $part == corner_* ]]; then
        # Extract location from name (front_left, front_right)
        if [[ $part == "corner_front_left" ]]; then
            python cad/parts/corner_motorized.py front_left
        elif [[ $part == "corner_front_right" ]]; then
            python cad/parts/corner_motorized.py front_right
        else
            echo -e "${YELLOW}Using basic part script${NC}"
            python cad/parts/${part}.py
    fi
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
    echo -e " Success: $success_count / $total${NC}"
    echo ""
    echo -e "${BLUE}STL location: $STL_DIR/${NC}"

    # Show what was generated
    ls -lh "$STL_DIR" 2>/dev/null | head -20
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
