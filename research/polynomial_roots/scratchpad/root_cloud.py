"""
A degree N polynomial with coefficients in the complex plane has exactly N roots
in the complex plane. Fixing the leading degree N term's coefficient to 1, you
may use those N roots to create a new set of polynomials where each root is used
as a coefficient in the new polynomial and a new polynomial is created for each
possible mapping of roots to coefficients (ordered permutations of the roots).

For example:

Let P0 = x**2 - x - 6 = (x - 3) * (x + 2).
P0 has roots of 3 and -2.

Use the ordered permutations of those roots to create P1 and P2:
P1 = x**2 + 3*x - 2
P2 = X**2 - 2*x + 3

Find the roots of P1, use them to create P3 and P4.
Find the roots of P2, use them to create P5 and P6.
And so on.

This program plots the roots found in this way on the complex plane.

Notice that the roots are confined to a particular region of the complex plane,
that there is structure and symmetry in the shape, and that there are variations
in the density of points. I call the set of points generated in this way a
polynomial's "root cloud".
"""

from itertools import permutations

import random
import numpy as np
import matplotlib.pyplot as plt

ENGAGE_RANDOMIZER = False

def estimateMaxPoints(n):
    #return sum(2**i for i in range(1, n + 1))
    return ((1<<n)<<1) - 1 - 1
MAX_POINTS_16 = estimateMaxPoints(16)

def generateRootCloud(initial_poly, MAX_POINTS = MAX_POINTS_16):
    queue = [initial_poly]
    points = []
    while len(points) < MAX_POINTS:
        if ENGAGE_RANDOMIZER and len(points) > 1:
            i = random.randint(0, len(points) - 1)
            points[i], points[0] = points[0], points[i]
        poly = queue[0]
        queue[:] = queue[1:]
        roots = np.roots(poly)
        points.extend(roots)
        for perm in permutations(roots):
            next_poly = np.concatenate(([1.0 + 0.0j], perm))
            queue.append(next_poly)
    return points

def plotPoints(points):
    xs = [np.real(x) for x in points]
    ys = [np.imag(x) for x in points]
    plt.scatter(xs, ys, marker='.', s=1)

def main():
    points2 = generateRootCloud([1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j])
    #points3 = generateRootCloud([1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j])
    #points4 = generateRootCloud([1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.j], MAX_POINTS = 40000)

    plt.figure(figsize=(8,8))

    plotPoints(points2)
    #plotPoints(points3)
    #plotPoints(points4)

    plt.show()

if __name__ == '__main__':
    main()
