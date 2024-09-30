import numpy as np
# from matplotlib import pyplot as plt

from powell import Powell
from simplex import Simplex

a, b, c, d, alpha = -6, -1, 2, 3, 20

def function_ellipse(x1: float, x2: float) -> float:
    return ((((x1-a)*np.cos(alpha) + (x2-b)*np.sin(alpha)) / c) ** 2
            + (((x2 - b)*np.cos(alpha) - (x1 - a)*np.sin(alpha)) / d) ** 2)

def function_rosenbrock(x1: float, x2: float) -> float:
    return 100 * (x2 - x1**2) ** 2 + (1 - x1) ** 2


powell = Powell(function_ellipse, 0, 0)
print(powell.calculate())
powell = Powell(function_rosenbrock, 0, 0, h0=0.0001)
print(powell.calculate())
simplex = Simplex(function_ellipse)
print(simplex.calculate())
simplex = Simplex(function_rosenbrock)
print(simplex.calculate())

# x, y = np.linspace(-10, 0, 1000), np.linspace(-5, 5, 1000)
# z = function_ellipse(*np.meshgrid(x, y))
# plt.figure(figsize=(8, 6))
# contour = plt.contour(x, y, z, levels=30, cmap="viridis")
# plt.colorbar(contour)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid()
# plt.show()

# x, y = np.linspace(0, 2, 1000), np.linspace(0, 2, 1000)
# z = function_rosenbrock(*np.meshgrid(x, y))
# plt.figure(figsize=(8, 6))
# contour = plt.contour(x, y, z, levels=100, cmap="viridis")
# plt.colorbar(contour)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid()
# plt.show()
