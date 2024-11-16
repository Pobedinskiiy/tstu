import numpy as np

from penalty import Penalty, Barrier


a, b, c, d, alpha = 5, -1, 1, 3, 30


def func_ellipse(x: float, y: float) -> float:
    return ((((x - a) * np.cos(alpha) + (y - b) * np.sin(alpha)) / c) ** 2
            + (((y - b) * np.cos(alpha) - (x - a) * np.sin(alpha)) / d) ** 2)


def bound_func_1(x: float, y: float) -> float:
    return x ** 2 + 2 * y ** 3 - 8


def inv_bound_func_1(x: float) -> float:
    return np.cbrt((8 - x ** 2) / 2)


def bound_func_2(x: float, y: float) -> float:
    return x + y


def inv_bound_func_2(x: float) -> float:
    return -x


penalty = Penalty(func_ellipse,
                  [[bound_func_1, "<=" , 0], [bound_func_2, ">=", 0]],
                  [inv_bound_func_1, inv_bound_func_2],
                  Barrier.EXTERNAL,
                  7, -7)
print(*penalty.calculate())
penalty.plot([-2, 7], [-7, 2], 30)

penalty = Penalty(func_ellipse,
                  [[bound_func_1, "<=" , 0], [bound_func_2, ">=", 0]],
                  [inv_bound_func_1, inv_bound_func_2],
                  Barrier.INTERNAL,
                  7, -7)
print(*penalty.calculate())
penalty.plot([-2, 7], [-7, 2], 30)