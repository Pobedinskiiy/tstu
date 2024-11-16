import numpy as np

from penalty import Penalty


a, b, c, d, alpha = -2, -1, 2, 3, 80


def func_ellipse(x: float, y: float) -> float:
    return ((((x - a) * np.cos(alpha) + (y - b) * np.sin(alpha)) / c) ** 2
            + (((y - b) * np.cos(alpha) - (x - a) * np.sin(alpha)) / d) ** 2)


def bound_func_1(x: float, y: float) -> float:
    return y ** 2 - 7 * x + 2 * x * y + 3


def inv_bound_func_1(y: float) -> float:
    return (-y ** 2 - 3) / (-7 + 2 * y)


def bound_func_2(x: float, y: float) -> float:
    return x + y


def inv_bound_func_2(y: float) -> float:
    return -y


penalty = Penalty(func_ellipse,
                  [[bound_func_1, "<=" , 0], [bound_func_2, "==", 0]],
                  [inv_bound_func_1, inv_bound_func_2],
                  6, -4)
print(*penalty.calculate())
penalty.plot([-2, 6], [-6, 2], 30)
