"""
This is one possible solution amonst many many solutions.

Note: this took longer than the ~20 minutes of in-class active-learning time but was meant to show you as many of the possible refactoring options you had
"""

import random

from matplotlib import animation
from matplotlib import pyplot as plt
import json
import logging
import logging.config
from pathlib import Path
from dataclasses import dataclass

# Boids and Initialization
NUM_BOIDS = 50
NEARBY_BOID_TOO_CLOSE_THRESH = 100
NEARBY_BOID_MATCH_SPEED_THRESH = 10_000
X_POS_INIT_RANGE = (-450.0, 50.0)
Y_POS_INIT_RANGE = (300.0, 600.0)
X_VEL_INIT_RANGE = (0.0, 10.0)
Y_VEL_INIT_RANGE = (-20.0, 20.0)

# Animation bounds
X_AXIS_BOUNDS = (-500, 1500)
Y_AXIS_BOUNDS = (-500, 1500)

# Run the animation
NUM_ANIMATION_FRAMES = 50
ANIMATION_INTERVAL = 50

# Constants for updating the positions and velocities
SCALE_RATE_TOWARDS_MIDDLE = 0.01 / NUM_BOIDS
SCALE_SPEED_MATCH_NEARBY = 0.125 / NUM_BOIDS


def configure_logging(config_path: Path) -> None:
    logging.config.dictConfig(json.loads(config_path.read_text()))


@dataclass
class BoidInformation:
    x_pos: list[float]
    y_pos: list[float]
    x_vel: list[float]
    y_vel: list[float]

    def add_boid(self, x: float, y: float, x_vel: float, y_vel: float):
        self.x_pos.append(x)
        self.y_pos.append(y)
        self.x_vel.append(x_vel)
        self.y_vel.append(y_vel)

    def __init__(
        self, x_pos_list: list[float], y_pos_list: list[float], x_vel_list: list[float], y_vel_list: list[float]
    ):
        self.x_pos = x_pos_list
        self.y_pos = y_pos_list
        self.x_vel = x_vel_list
        self.y_vel = y_vel_list

    @classmethod
    def init_empty(cls) -> "BoidInformation":
        return cls([], [], [], [])


def initialize_boids(
    num_boids: int,
    x_pos_lim: tuple[int, int] = X_POS_INIT_RANGE,
    y_pos_lim: tuple[int, int] = Y_POS_INIT_RANGE,
    x_vel_lim: tuple[int, int] = X_VEL_INIT_RANGE,
    y_vel_lim: tuple[int, int] = Y_VEL_INIT_RANGE,
) -> BoidInformation:
    boids = BoidInformation.init_empty()

    for _ in range(num_boids):
        x_pos = random.uniform(*x_pos_lim)
        y_pos = random.uniform(*y_pos_lim)
        x_vel = random.uniform(*x_vel_lim)
        y_vel = random.uniform(*y_vel_lim)
        boids.add_boid(x=x_pos, y=y_pos, x_vel=x_vel, y_vel=y_vel)

    return boids


def sq_l2_distance(x1: float, x2: float, y1: float, y2: float) -> float:
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def update_rule(curr_delta_vel: float, sub_from: float, sub_by: float, scaling: float = 1.0) -> float:
    return curr_delta_vel + (sub_from - sub_by) * scaling


def update_boids(boids: BoidInformation):
    """
    Update the boid positions according to the original rules.

    Note:
        we kept the original update formulas where relevant for you to reference
    """
    x_pos, y_pos, x_vels, y_vels = boids.x_pos, boids.y_pos, boids.x_vel, boids.y_vel
    delta_x_vels = [0] * NUM_BOIDS
    delta_y_vels = [0] * NUM_BOIDS

    for i in range(NUM_BOIDS):
        for j in range(NUM_BOIDS):
            # Fly towards the middle
            delta_x_vels[i] = update_rule(
                delta_x_vels[i], sub_from=x_pos[j], sub_by=x_pos[i], scaling=SCALE_RATE_TOWARDS_MIDDLE
            )
            delta_y_vels[i] = update_rule(
                delta_y_vels[i], sub_from=y_pos[j], sub_by=y_pos[i], scaling=SCALE_RATE_TOWARDS_MIDDLE
            )
            # delta_x_vels[i] = delta_x_vels[i] + (x_pos[j] - x_pos[i]) * DELTA_SCALE / len(x_pos)
            # delta_y_vels[i] = delta_y_vels[i] + (y_pos[j] - y_pos[i]) * DELTA_SCALE / len(x_pos)

            # Fly away from nearby boids
            if sq_l2_distance(x_pos[i], x_pos[j], y_pos[i], y_pos[j]) < NEARBY_BOID_TOO_CLOSE_THRESH:
                delta_x_vels[i] = update_rule(delta_x_vels[i], sub_from=x_pos[i], sub_by=x_pos[j])
                delta_y_vels[i] = update_rule(delta_y_vels[i], sub_from=y_pos[i], sub_by=y_pos[j])

                # delta_x_vels[i] = delta_x_vels[i] + (x_pos[i] - x_pos[j])
                # delta_y_vels[i] = delta_y_vels[i] + (y_pos[i] - y_pos[j])

            # Try to match speed with nearby boids
            if sq_l2_distance(x_pos[i], x_pos[j], y_pos[i], y_pos[j]) < NEARBY_BOID_MATCH_SPEED_THRESH:
                delta_x_vels[i] = update_rule(
                    delta_x_vels[i], sub_from=x_pos[j], sub_by=x_pos[i], scaling=SCALE_SPEED_MATCH_NEARBY
                )

                delta_y_vels[i] = update_rule(
                    delta_y_vels[i], sub_from=y_pos[j], sub_by=y_pos[i], scaling=SCALE_SPEED_MATCH_NEARBY
                )
                # delta_x_vels[i] = delta_x_vels[i] + (x_vels[j] - x_vels[i]) * 0.125 / len(x_pos)
                # delta_y_vels[i] = delta_y_vels[i] + (y_vels[j] - y_vels[i]) * 0.125 / len(x_pos)
    # Finally update their velocities and positions
    for i in range(NUM_BOIDS):
        # First calculate the velocity change
        x_vels[i] += delta_x_vels[i]
        y_vels[i] += delta_y_vels[i]

    # Then using the new velocity, modify the pos
    for i in range(len(x_pos)):
        x_pos[i] += x_vels[i]
        y_pos[i] += y_vels[i]


def animate(frame):
    update_boids(boids)
    scatter.set_offsets(list(zip(boids.x_pos, boids.y_pos)))


if __name__ == "__main__":
    # Set up logging
    config_path = Path(__file__).parent / "logging_config.json"
    configure_logging(config_path)

    boids = initialize_boids(num_boids=NUM_BOIDS)
    # Set up the figure,
    figure = plt.figure()
    axes = plt.axes(xlim=X_AXIS_BOUNDS, ylim=Y_AXIS_BOUNDS)
    scatter = axes.scatter(boids.x_pos, boids.y_pos)

    anim = animation.FuncAnimation(figure, animate, frames=NUM_ANIMATION_FRAMES, interval=ANIMATION_INTERVAL)
    plt.show()
