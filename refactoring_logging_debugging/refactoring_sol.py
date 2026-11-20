"""@CSE583-ers: This code was taken from: https://github.com/alan-turing-institute/bad-boids/blob/main/boids.py
- wherever we've added annotations they are prefixed with "CSE583"
- you should try to refactor the code below, either on your own or guided by the annotations we've added.
    Note: you might find it useful to add a random seed

A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random

from matplotlib import animation
from matplotlib import pyplot as plt

# Deliberately terrible code for teaching purposes

# CSE583: what do these numbers mean? 50? -450 ? It might be good to extract them into constants
# These random seemingly-arbitrary numbers are known as magic numbers and should be avoided
boids_x = [random.uniform(-450, 50.0) for x in range(50)]
boids_y = [random.uniform(300.0, 600.0) for x in range(50)]
boid_x_velocities = [random.uniform(0, 10.0) for x in range(50)]
boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(50)]
# CSE583: the following would be a great time for something like a namedtuple, a class, or dataclass. You won't NEED
#     to use any of them, but they are useful structures to keep in mind
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


def updateBoids(boids):
    xs, ys, xvs, yvs = boids
    # CSE583: Hmm.... we've defined something ~relative to~ Y, deltaYVs, in terms of `xs`. What assumption(s) are we making?
    deltaXVs = [0] * len(xs)
    deltaYVs = [0] * len(xs)

    """
    Fly towards the middle

    # CSE583: these next two blocks, where we are flying towards the middle look awfully similar...
    # indexing into ys but going over the length of xs
    """
    for i in range(len(xs)):
        for j in range(len(xs)):
            deltaXVs[i] = deltaXVs[i] + (xs[j] - xs[i]) * 0.01 / len(xs)
    for i in range(len(xs)):
        for j in range(len(xs)):
            deltaYVs[i] = deltaYVs[i] + (ys[j] - ys[i]) * 0.01 / len(xs)

    """
    Fly away from nearby boids
    # we've calculated the squared-Euclidean distance twice ... and there are a number of constants
    # appearing out of seemingly nowhere
    """
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 100:
                deltaXVs[i] = deltaXVs[i] + (xs[i] - xs[j])
                deltaYVs[i] = deltaYVs[i] + (ys[i] - ys[j])
    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 10000:
                deltaXVs[i] = deltaXVs[i] + (xvs[j] - xvs[i]) * 0.125 / len(xs)
                deltaYVs[i] = deltaYVs[i] + (yvs[j] - yvs[i]) * 0.125 / len(xs)
    """
    CSE583:
    the next two blocks do very similar things. 
    """
    # Update velocities
    for i in range(len(xs)):
        xvs[i] = xvs[i] + deltaXVs[i]
        yvs[i] = yvs[i] + deltaYVs[i]
    # Move according to velocities
    for i in range(len(xs)):
        xs[i] = xs[i] + xvs[i]
        ys[i] = ys[i] + yvs[i]


# CSE583: Hmm what do these numbers: -500, 1500 mean? I wish we had named some of these variables!
figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])


def ANIMATE(frame):
    updateBoids(boids)
    scatter.set_offsets(list(zip(boids[0], boids[1])))


anim = animation.FuncAnimation(figure, ANIMATE, frames=50, interval=50)

# CSE583: What is the purpose of the `if __name__ == "__main__":` ?
#      should we have moved some variables into it?
if __name__ == "__main__":
    plt.show()
