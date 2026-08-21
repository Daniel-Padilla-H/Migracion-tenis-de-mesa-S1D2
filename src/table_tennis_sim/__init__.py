"""Provide the public interface for the table tennis simulation package."""

from .parameters import (
    InitialConditions,
    NumericalConfiguration,
    PhysicalParameters,
    TableNetGeometry,
)
from .simulation import SimulationResult, generate_time_vector, run_simulation

__all__ = [
    "InitialConditions",
    "NumericalConfiguration",
    "PhysicalParameters",
    "SimulationResult",
    "TableNetGeometry",
    "generate_time_vector",
    "run_simulation",
]
