#!/bin/bash

# Amalgam Setup Wizard
# Full setup for new users: environment setup, configuration, and building
# Supports Linux, macOS, and Windows (via Git Bash/WSL)

set -e  # Exit on error

# Colors for output
if [ -t 1 ]; then
    GREEN='\033[0;32m'
    BLUE='\033[0;34m'
    YELLOW='\033[1;33m'
    RED='\033[0;31m'
    NC='\033[0m' # No Color
else
    GREEN=''
    BLUE=''
    YELLOW=''
    RED=''
    NC=''
fi

# Paths
VENV_DIR=".venv"
REQUIREMENTS_FILE="requirements.txt"
CONFIG_SCRIPT="configure.py"
BUILD_SCRIPT="build.sh"
USE_UV=false

print_header() {
    echo ""
    echo "${BLUE}========================================${NC}"
    echo "  $1"
    echo "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

detect_os() {
    case "$(uname -s)" in
        Linux*)     OS="Linux";;
        Darwin*)    OS="macOS";;
        CYGWIN*)    OS="Windows";;
        MINGW*)     OS="Windows";;
        MSYS*)      OS="Windows";;
        *)          OS="Unknown";;
    esac
    echo "$OS"
}

print_python_install_instructions() {
    local os="$1"
    print_error "Python 3.9 or higher not found"

    echo ""
    echo "Please install Python 3.9+ for your platform:"
    echo ""

    case "$os" in
        "macOS")
            echo "  Option 1 (Homebrew):"
            echo "    brew install python@3.11"
            echo ""
            echo "  Option 2 (Official installer):"
            echo "    https://www.python.org/downloads/"
            ;;
        "Linux")
            echo "  Ubuntu/Debian:"
            echo "    sudo apt update"
            echo "    sudo apt install python3 python3-venv python3-pip"
            echo ""
            echo "  Fedora/RHEL:"
            echo "    sudo dnf install python3 python3-venv python3-pip"
            echo ""
            echo "  Arch Linux:"
            echo "    sudo pacman -S python python-pip"
            ;;
        "Windows")
            echo "  Option 1 (Python.org):"
            echo "    https://www.python.org/downloads/"
            echo "    Check 'Add Python to PATH' during installation"
            echo ""
            echo "  Option 2 (Microsoft Store):"
            echo "    Search for 'Python 3.11' in the Microsoft Store"
            echo ""
            echo "  After installation, restart your terminal and run this script again"
            ;;
    esac

    echo ""
    echo ""
    echo "Note: This script does NOT install Python automatically."
    echo "      Python is a large download (~100-200MB) and should be installed"
    echo "      via your system package manager or official installer."
    echo ""
    echo "Alternatively, you can use our web interface to generate STLs:"
    echo "  https://amalgam.reprap.org (coming soon)"
    exit 1
}

check_python() {
    print_header "Checking Python Installation"

    PYTHON_CMD=""

    # Try python3 first
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    # Try python on Windows
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        print_python_install_instructions "$(detect_os)"
    fi

    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
    MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

    print_success "Found Python $PYTHON_VERSION"

    if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 9 ]); then
        print_error "Python 3.9 or higher required (found $PYTHON_VERSION)"
        exit 1
    fi

    print_success "Python version meets requirements"
    export PYTHON_CMD
}

check_uv() {
    if command -v uv &> /dev/null; then
        print_success "Found uv (fast package manager)"
        return 0
    else
        print_warning "uv not found (optional for faster setup)"
        return 1
    fi
}

 install_uv() {
    if ask_yes_no "Install uv for faster package management? (Optional)"; then
        print_header "Installing uv (fast package manager)"
        print_warning "Note: uv is a small tool (~5MB) for faster package installs."
        print_warning "      It does NOT install Python itself."

        case "$(detect_os)" in
            "Linux"|"macOS")
                curl -LsSf https://astral.sh/uv/install.sh | sh
                export PATH="$HOME/.local/bin:$PATH"
                ;;
            "Windows")
                powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
                print_warning "Please restart your terminal after uv installation"
                exit 0
                ;;
        esac

        if command -v uv &> /dev/null; then
            print_success "uv installed successfully"
            USE_UV=true
        else
            print_warning "uv installation may have failed, using pip instead"
            USE_UV=false
        fi
    fi
}

setup_environment() {
    print_header "Setting Up Python Environment"

    if [ "$USE_UV" = true ]; then
        # Use uv (faster, simpler)
        if [ -f "pyproject.toml" ]; then
            uv sync
            print_success "Environment created with uv"
        else
            uv venv "$VENV_DIR"
            print_success "Virtual environment created with uv"
        fi
    else
        # Use standard venv
        if [ -d "$VENV_DIR" ]; then
            print_warning "Virtual environment already exists"
            if ask_yes_no "Recreate virtual environment?"; then
                rm -rf "$VENV_DIR"
                $PYTHON_CMD -m venv "$VENV_DIR"
                print_success "Virtual environment recreated"
            else
                print_success "Using existing virtual environment"
                return 0
            fi
        else
            $PYTHON_CMD -m venv "$VENV_DIR"
            print_success "Virtual environment created"
        fi
    fi
}

activate_environment() {
    print_header "Activating Python Environment"

    if [ "$USE_UV" = true ]; then
        # uv handles activation implicitly
        print_success "Using uv environment"
        return 0
    fi

    if [ ! -f "$VENV_DIR/bin/activate" ]; then
        print_error "Virtual environment not found"
        exit 1
    fi

    source "$VENV_DIR/bin/activate"
    print_success "Virtual environment activated"
}

install_dependencies() {
    print_header "Installing Dependencies"

    if [ ! -f "$REQUIREMENTS_FILE" ]; then
        print_warning "requirements.txt not found, creating minimal version"
        cat > "$REQUIREMENTS_FILE" << 'EOF'
build123d>=0.2.0
numpy>=1.20.0
EOF
    fi

    if [ "$USE_UV" = true ]; then
        uv pip install -r "$REQUIREMENTS_FILE"
    else
        pip install --upgrade pip
        pip install -r "$REQUIREMENTS_FILE"
    fi

    print_success "Dependencies installed"
}

run_configure() {
    print_header "Configuration Wizard"

    if [ ! -f "$CONFIG_SCRIPT" ]; then
        print_error "Configuration script not found: $CONFIG_SCRIPT"
        exit 1
    fi

    $PYTHON_CMD "$CONFIG_SCRIPT"
}

build_parts() {
    print_header "Building Parts"

    if [ ! -f "$BUILD_SCRIPT" ]; then
        print_error "Build script not found: $BUILD_SCRIPT"
        exit 1
    fi

    chmod +x "$BUILD_SCRIPT"
    ./"$BUILD_SCRIPT" build_all
}

ask_yes_no() {
    local prompt="$1"
    local default="${2:-n}"
    local default_str

    if [ "$default" = "y" ]; then
        default_str="[Y/n]"
    else
        default_str="[y/N]"
    fi

    while true; do
        read -p "$prompt $default_str: " response
        response=${response:-$default}
        case $response in
            [Yy]*)
                return 0
                ;;
            [Nn]*)
                return 1
                ;;
            *)
                echo "Please answer yes or no."
                ;;
        esac
    done
}

main() {
    print_header "Amalgam Setup Wizard"

    local os_name=$(detect_os)
    echo "Detected OS: $os_name"
    echo ""
    echo "This wizard will guide you through:"
    echo "  1. Checking Python installation"
    echo "  2. Setting up Python environment"
    echo "  3. Installing required packages"
    echo "  4. Running configuration wizard"
    echo "  5. Building all parts"
    echo ""

    if ! ask_yes_no "Continue?"; then
        echo "Setup cancelled."
        exit 0
    fi

    # Step 1: Check Python
    check_python

    # Step 2: Check for uv
    if check_uv; then
        USE_UV=true
    else
        install_uv
    fi

    # Step 3: Setup environment
    setup_environment

    # Step 4: Activate environment
    activate_environment

    # Step 5: Install dependencies
    install_dependencies

    # Step 6: Run configuration
    run_configure

    # Step 7: Build parts
    if ask_yes_no "Build all parts now?"; then
        build_parts
    fi

    print_header "Setup Complete"

    echo ""
    echo "Your Amalgam environment is ready!"
    echo ""
    echo "Exports are in the 'exports' directory"
    echo ""

    if [ "$USE_UV" = false ]; then
        echo "To build parts in the future:"
        echo "  1. Activate environment: source $VENV_DIR/bin/activate"
        echo "  2. Build parts: ./$BUILD_SCRIPT build_all"
        echo ""
        echo "For faster builds, consider installing uv:"
        echo "  https://docs.astral.sh/uv/getting-started/installation/"
    else
        echo "To build parts in the future:"
        echo "  ./$BUILD_SCRIPT build_all"
    fi

    echo ""
    print_success "Happy building!"
}

main "$@"
