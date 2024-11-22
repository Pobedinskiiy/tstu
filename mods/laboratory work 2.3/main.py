import numpy as np

from gradient import Gradient
from fastest_descent import FastestDescent


a, b, c, d, alpha = -6, -1, 2, 3, 20


def function_ellipse(x1: float, x2: float) -> float:
    return ((((x1-a)*np.cos(alpha) + (x2-b)*np.sin(alpha)) / c) ** 2
            + (((x2 - b)*np.cos(alpha) - (x1 - a)*np.sin(alpha)) / d) ** 2)


def function_rosenbrock(x1: float, x2: float) -> float:
    return 100 * (x2 - x1**2) ** 2 + (1 - x1) ** 2


gradient = Gradient(function_ellipse, 0, 0)
print(*gradient.calculate())
gradient.plot([-10, 0], [-5, 5], 30)
gradient = Gradient(function_rosenbrock, h=1e-3, iterations=100000)
print(*gradient.calculate())
gradient.plot([0, 2], [0, 2], 100)

fastest_descent = FastestDescent(function_ellipse, 0, 0)
print(*fastest_descent.calculate())
fastest_descent.plot([-10, 0], [-5, 5], 30)
fastest_descent = FastestDescent(function_rosenbrock, h=1e-3, iterations=100000)
print(*fastest_descent.calculate())
fastest_descent.plot([0, 2], [0, 2], 100)