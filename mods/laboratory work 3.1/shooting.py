import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style

def functional(t):
    return 0.3 * t - 0.3 / t ** 2 + (t * np.log(t)) / 3


def derivative(func, t, h=1e-5):
    return (func(t + h) - func(t - h)) / (2 * h)


def shooting_method(slope, t1, x1, t2):
    num_steps = 100
    h = (t2 - t1) / num_steps
    t_values = np.linspace(t1, t2, num_steps + 1)

    x_values = np.zeros(num_steps + 1)
    x_values[0] = x1
    z = slope

    for i in range(num_steps):
        x_values[i + 1] = x_values[i] + h * z
        z -= (z / t_values[i]) * h

    return x_values[-1]

def find_slope(t1, x1, t2, x2, tolerance=1e-2):
    slope = 0.0
    while True:
        x_final = shooting_method(slope, t1, x1, t2)
        error = x_final - x2

        if abs(error) < tolerance:
            break

        slope -= error * 0.1  # Корректировка наклона

    return slope


t1, x1, t2, x2 = 1, 0, 2, 1

optimal_slope = find_slope(t1, x1, t2, x2)

t_values = np.linspace(t1, t2, 100)
x_values = np.zeros_like(t_values)
z = optimal_slope

for i in range(len(t_values) - 1):
    x_values[i + 1] = x_values[i] + (t_values[i + 1] - t_values[i]) * z
    z -= (z / t_values[i]) * (t_values[i + 1] - t_values[i])  # Обновление производной

print(f"Оптимальный наклон: {optimal_slope:.4f}")

mpl_style(minor_ticks=False)
plt.plot(t_values, [functional(t) for t in t_values], label="x(t)")
plt.plot(np.linspace(t1, t2, len(x_values)), x_values, label="extreme", linestyle="--")
plt.xlabel("t")
plt.ylabel("x")
plt.title("Shooting")
plt.grid(True)
plt.legend()
plt.show()