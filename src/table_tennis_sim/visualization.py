"""Declare visualization entry points for simulation results."""

from .parameters import TableNetGeometry
from .simulation import SimulationResult


def plot_3d_trajectory(result: SimulationResult, geometry: TableNetGeometry) -> None:
    """Plot the three-dimensional ball trajectory together with the table geometry."""
    raise NotImplementedError("Three-dimensional trajectory plotting is not implemented yet.")


def plot_time_series(result: SimulationResult) -> None:
    """Plot temporal position, velocity, orientation, and angular velocity histories."""
    raise NotImplementedError("Time-series plotting is not implemented yet.")


def animate_simulation(result: SimulationResult, geometry: TableNetGeometry) -> None:
    """Animate a future three-dimensional rendering of the simulation state."""
    raise NotImplementedError("Simulation animation is not implemented yet.")
