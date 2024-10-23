import numpy as np

from penalty import Penalty, Barrier


a, b, c, d, alpha = -6, -1, 2, 3, 20

def function_ellipse(x: float, y: float) -> float:
    return ((((x - a) * np.cos(alpha) + (y - b) * np.sin(alpha)) / c) ** 2
            + (((y - b) * np.cos(alpha) - (x - a) * np.sin(alpha)) / d) ** 2)

def constraint_function_1(x: float, y: float) -> float:
    return x ** 2 + 2 * y ** 3 - 8

def constraint_function_2(x: float, y: float) -> float:
    return x + y

penalty = Penalty(function_ellipse, [[constraint_function_1, "<=" , 0], [constraint_function_2, ">=", 0]])
print(*penalty.calculate(Barrier.INTERNAL))
penalty.plot([-10, 0], [-5, 5], 30)
