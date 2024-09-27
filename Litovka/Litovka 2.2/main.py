import numpy as np
from powell import Powell

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