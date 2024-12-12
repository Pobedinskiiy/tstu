import matplotlib.pyplot as plt
from qbstyles import mpl_style
import numpy as np


def functional(t):
    return 0.3 * t - 0.3 / t ** 2 + (t * np.log(t)) / 3


def runge_kutty(t1: float, x1: float, t2: float, x2: float, eps: float = 1e-2) -> (list, list, float):
    z0 = 0.0

    while True:
        t_array, x_array = [t1], [x1]
        t, x, z = t1, x1, z0

        while t < t2:
            x += z * eps
            z -= z / t * eps
            t += eps
            t_array.append(t)
            x_array.append(x)

        if abs(x - x2) <= eps:
            return t_array, x_array, z0

        if x < x2:
            z0 += eps
        else:
            z0 -= eps

t_values, x_values, optimal_slope = runge_kutty(1, 0, 2, 1)
print(f"Оптимальный наклон: {optimal_slope:.4f}")

mpl_style(minor_ticks=False)
plt.plot(np.linspace(1, 2, 100), functional(*np.meshgrid(np.linspace(1, 2, 100))), label="x(t)")
plt.plot(t_values, x_values, label="extreme", linestyle="--")
plt.xlabel("t")
plt.ylabel("x")
plt.title("Runge-Kutty")
plt.grid(True)
plt.legend()
plt.show()
