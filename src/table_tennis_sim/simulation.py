"""Declare simulation coordination and result structures without implementing integration."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from .parameters import (
    InitialConditions,
    NumericalConfiguration,
    PhysicalParameters,
    TableNetGeometry,
)


@dataclass(frozen=True)
class SimulationResult:
    """Store time histories using arrays shaped as three rows by sample count."""

    time: NDArray[np.float64]
    position: NDArray[np.float64]
    velocity: NDArray[np.float64]
    acceleration: NDArray[np.float64]
    orientation: NDArray[np.float64]
    angular_velocity: NDArray[np.float64]
    angular_acceleration: NDArray[np.float64]


def generate_time_vector(configuration: NumericalConfiguration) -> NDArray[np.float64]:
    """Generate the time vector from zero through the configured duration in seconds."""
    raise NotImplementedError("Time vector generation is not implemented yet.")


def run_simulation(
    physical_parameters: PhysicalParameters,
    geometry: TableNetGeometry,
    initial_conditions: InitialConditions,
    numerical_configuration: NumericalConfiguration,
) -> SimulationResult:
    """Run the future simulation and return all translational and rotational histories."""
    raise NotImplementedError("The simulation integrator is not implemented yet.")
