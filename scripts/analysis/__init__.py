"""
Amalgam Engineering Analysis Tools

This package provides engineering calculations for assessing
Amalgam build configurations before construction.
"""

from .rod_sag import calculate_rod_sag, RodSagResult
from .frame_sizing import calculate_frame_size, FrameSizeResult
from .acceleration import calculate_max_acceleration, AccelerationResult

__all__ = [
    "calculate_rod_sag",
    "RodSagResult",
    "calculate_frame_size",
    "FrameSizeResult",
    "calculate_max_acceleration",
    "AccelerationResult",
]
