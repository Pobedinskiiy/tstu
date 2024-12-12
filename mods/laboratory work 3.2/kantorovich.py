import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style


def functional(t):
    return 0.3 * t - 0.3 / t ** 2 + (t * np.log(t)) / 3


def derivative(func, t, h=1e-5):
    return (func(t + h) - func(t - h)) / (2 * h)


def kantorovich(t1, x1, t2, x2, eps=1e-2, num_points=20):
    t_values = np.linspace(t1, t2, num_points)
    dt = t_values[1] - t_values[0]

    x_values = np.zeros(num_points)
    z_values = np.zeros(num_points)
    x_values[0] = x1
    z_values[0] = 0

    while abs(x_values[-1] - x2) > eps:
        if x_values[-1] < x2:
            z_values[0] += eps
        else:
            z_values[0] -= eps

        x_values[0] = x1
        for i in range(1, num_points):
            t = t_values[i - 1]
            x_values[i] = x_values[i - 1] + z_values[0] * dt
            z_values[i] = z_values[i - 1] + derivative(functional, t) * dt

    return t_values, x_values, x_values


mpl_style(minor_ticks=False)
plt.plot(np.linspace(1, 2, 100), functional(*np.meshgrid(np.linspace(1, 2, 100))), label="x(t)")
t_values, x_values, z_values = kantorovich(1, 0, 2, 1)
plt.plot(t_values, x_values, label="extreme", linestyle="--")
plt.xlabel("t")
plt.ylabel("x")
plt.title("Kantorovich method")
plt.grid(True)
plt.legend()
plt.show()
