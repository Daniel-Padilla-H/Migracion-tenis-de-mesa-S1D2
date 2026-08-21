"""Declare the physics operations used by the future simulation integrator."""

from typing import TypeAlias

import numpy as np
from numpy.typing import NDArray

from .parameters import PhysicalParameters, TableNetGeometry

Vector: TypeAlias = NDArray[np.float64]


def gravity_force(parameters: PhysicalParameters) -> Vector:
    """Return the gravitational force vector in millinewtons."""
    raise NotImplementedError("Gravity force calculation is not implemented yet.")


def linear_drag_force(velocity: Vector, parameters: PhysicalParameters) -> Vector:
    """Return the linear aerodynamic drag force in millinewtons."""
    raise NotImplementedError("Linear drag calculation is not implemented yet.")


def magnus_force(
    angular_velocity: Vector, velocity: Vector, parameters: PhysicalParameters
) -> Vector:
    """Return the Magnus force vector in millinewtons."""
    raise NotImplementedError("Magnus force calculation is not implemented yet.")


def angular_dynamics(
    angular_velocity: Vector, parameters: PhysicalParameters
) -> tuple[Vector, Vector]:
    """Return rotational drag torque and angular acceleration vectors."""
    raise NotImplementedError("Angular dynamics calculation is not implemented yet.")


def table_bounce(
    position: Vector,
    velocity: Vector,
    angular_velocity: Vector,
    parameters: PhysicalParameters,
    geometry: TableNetGeometry,
) -> tuple[Vector, Vector, Vector]:
    """Return the state after a possible table bounce."""
    raise NotImplementedError("Table bounce handling is not implemented yet.")


def net_collision(
    position: Vector,
    velocity: Vector,
    angular_velocity: Vector,
    parameters: PhysicalParameters,
    geometry: TableNetGeometry,
) -> tuple[Vector, Vector]:
    """Return velocity and angular velocity after a possible net collision."""
    raise NotImplementedError("Net collision handling is not implemented yet.")
