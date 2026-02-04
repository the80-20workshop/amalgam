"""
Board Registry for Amalgam

Defines supported control boards and their capabilities.
Each board entry contains metadata used by:
- Wizard: to guide configuration choices
- Docs: to generate board-specific wiring guides
- Analysis: to validate configuration feasibility
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class BoardSpec:
    """Specification for a control board."""

    id: str                     # Internal identifier (e.g., "SKR_MINI_E3_V3")
    name: str                   # Display name (e.g., "BTT SKR Mini E3 V3")
    manufacturer: str           # BTT, MKS, etc.

    # Capabilities
    stepper_drivers: int        # Number of stepper driver slots
    has_canbus: bool            # CAN bus support
    integrated_host: bool       # Has onboard Linux (like SKIPR)
    voltage: int                # Input voltage (12 or 24)

    # Klipper compatibility
    klipper_mcu: str            # MCU type for Klipper config

    # Sourcing
    typical_price_aud: float    # Approximate cost
    donor_common: bool          # Often found in donor printers

    # Documentation
    docs_folder: str            # Folder name in docs/boards/
    notes: list[str]            # Important notes for builders

    # Tier compatibility
    min_tier: int               # Minimum tier this board supports
    max_tier: int               # Maximum tier this board supports


# =============================================================================
# BOARD DEFINITIONS
# =============================================================================

BOARDS = {
    # -------------------------------------------------------------------------
    # Donor-sourced boards (Tier 1-2)
    # -------------------------------------------------------------------------
    "CREALITY_V4": BoardSpec(
        id="CREALITY_V4",
        name="Creality V4.2.x",
        manufacturer="Creality",
        stepper_drivers=4,
        has_canbus=False,
        integrated_host=False,
        voltage=24,
        klipper_mcu="stm32f103",
        typical_price_aud=0,  # From donor
        donor_common=True,
        docs_folder="creality-v4",
        notes=[
            "Common in Ender 3 V2, CR-6 SE",
            "4 drivers sufficient for Tier 1 (belt-driven Z)",
            "Needs separate Klipper host (Pi/CB1/old laptop)",
        ],
        min_tier=1,
        max_tier=1,
    ),

    "SKR_MINI_E3_V3": BoardSpec(
        id="SKR_MINI_E3_V3",
        name="BTT SKR Mini E3 V3",
        manufacturer="BigTreeTech",
        stepper_drivers=4,
        has_canbus=False,
        integrated_host=False,
        voltage=24,
        klipper_mcu="stm32g0b1",
        typical_price_aud=45,
        donor_common=True,
        docs_folder="skr-mini-e3",
        notes=[
            "Direct Ender 3 replacement",
            "TMC2209 drivers onboard",
            "4 drivers = Tier 1 only (belt Z)",
        ],
        min_tier=1,
        max_tier=1,
    ),

    # -------------------------------------------------------------------------
    # Multi-MCU capable boards (Tier 2)
    # -------------------------------------------------------------------------
    "SKR_PICO": BoardSpec(
        id="SKR_PICO",
        name="BTT SKR Pico",
        manufacturer="BigTreeTech",
        stepper_drivers=4,
        has_canbus=False,
        integrated_host=False,
        voltage=24,
        klipper_mcu="rp2040",
        typical_price_aud=25,
        donor_common=False,
        docs_folder="skr-pico",
        notes=[
            "Compact RP2040-based board",
            "Good as secondary MCU for Triple-Z",
            "Use with donor board for 6+ drivers total",
        ],
        min_tier=2,
        max_tier=2,
    ),

    "BTT_OCTOPUS": BoardSpec(
        id="BTT_OCTOPUS",
        name="BTT Octopus",
        manufacturer="BigTreeTech",
        stepper_drivers=8,
        has_canbus=True,
        integrated_host=False,
        voltage=24,
        klipper_mcu="stm32f446",
        typical_price_aud=80,
        donor_common=False,
        docs_folder="btt-octopus",
        notes=[
            "8 driver slots - handles Triple-Z solo",
            "CAN bus for toolhead boards",
            "Overkill for most builds, but future-proof",
        ],
        min_tier=2,
        max_tier=3,
    ),

    # -------------------------------------------------------------------------
    # Reference Spec board (Tier 3)
    # -------------------------------------------------------------------------
    "MKS_SKIPR": BoardSpec(
        id="MKS_SKIPR",
        name="MKS SKIPR",
        manufacturer="Makerbase",
        stepper_drivers=6,
        has_canbus=True,
        integrated_host=True,
        voltage=24,
        klipper_mcu="stm32f407",
        typical_price_aud=120,
        donor_common=False,
        docs_folder="mks-skipr",
        notes=[
            "REFERENCE SPEC: Integrated Klipper host",
            "6 drivers = perfect for Triple-Z (X, Y, Z×3, E)",
            "No separate Pi/CB1 needed",
            "Allwinner H616 runs Armbian + Klipper",
        ],
        min_tier=3,
        max_tier=3,
    ),
}


def get_board(board_id: str) -> Optional[BoardSpec]:
    """Get a board specification by ID."""
    return BOARDS.get(board_id)


def get_boards_for_tier(tier: int) -> list[BoardSpec]:
    """Get all boards compatible with a specific tier."""
    return [
        board for board in BOARDS.values()
        if board.min_tier <= tier <= board.max_tier
    ]


def get_donor_boards() -> list[BoardSpec]:
    """Get boards commonly found in donor printers."""
    return [board for board in BOARDS.values() if board.donor_common]


def boards_can_combine_for_drivers(board_ids: list[str], required: int) -> bool:
    """Check if a combination of boards provides enough drivers."""
    total = sum(BOARDS[bid].stepper_drivers for bid in board_ids if bid in BOARDS)
    return total >= required
