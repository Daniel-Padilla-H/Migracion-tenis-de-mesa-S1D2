"""Define parameter structures while preserving the original MATLAB units."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PhysicalParameters:
    """Store ball and force parameters in grams, millimeters, seconds, and radians."""

    ball_mass: float = 2.7  # g
    ball_radius: float = 20.25  # mm
    ball_rotational_inertia: float = 2.0 / 3.0 * 2.7 * 20.25**2  # g mm^2
    table_restitution: float = 0.77
    net_restitution: float = 0.5
    linear_drag: float = 2.7  # mN / (mm/s)
    rotational_drag: float = 350.0  # mN mm / (rad/s)
    magnus_coefficient: float = 0.01  # mN / (mm/s^2)
    table_friction: float = 0.25
    gravitational_acceleration: float = 9800.0  # mm/s^2


@dataclass(frozen=True)
class TableNetGeometry:
    """Store table and net dimensions in millimeters."""

    table_length: float = 2740.0
    table_width: float = 1525.0
    table_height: float = 760.0
    net_height: float = 152.5
    net_extra: float = 180.0


@dataclass(frozen=True)
class InitialConditions:
    """Store initial translational and rotational states in MATLAB-compatible units."""

    position: tuple[float, float, float] = (0.0, 762.5, 1065.0)  # mm
    velocity: tuple[float, float, float] = (7000.0, -3000.0, -3000.0)  # mm/s
    angular_velocity: tuple[float, float, float] = (0.0, 0.0, 75.0 * 2.0 * 3.141592653589793)  # rad/s


@dataclass(frozen=True)
class NumericalConfiguration:
    """Store numerical settings using seconds and radians where applicable."""

    time_step: float = 0.005  # s
    duration: float = 1.5  # s
    animate: bool = True
    plot_period: int = 5  # simulation steps
    yaw: float = -45.0  # degrees
    pitch: float = 23.5  # degrees; interpreted from the intended MATLAB value
