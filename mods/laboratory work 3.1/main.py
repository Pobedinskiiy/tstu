import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style


def functional(t):
    return 0.3 * t - 0.3 / t ** 2 + (t * np.log(t)) / 3


def derivative(func, t, h=1e-2):
    return (func(t + h) - func(t - h)) / (2 * h)


def shooting_method(slope):
    num_steps = 30
    h = (t2 - t1) / num_steps
    t_values = np.linspace(t1, t2, num_steps + 1)

    x_values = np.zeros(num_steps + 1)
    x_values[0] = x1

    for i in range(num_steps):
        x_values[i + 1] = x_values[i] + h * (slope + derivative(functional, t_values[i]))

    return x_values[-1]


def extreme(target_x2, slope = 0.0, tolerance=1e-2):
    while True:
        error = shooting_method(slope) - target_x2

        if abs(error) < tolerance:
            break

        slope -= error * 1e-2

    return slope


t1, x1, t2, x2 = 1, 0, 2, 1

# Находим экстремум
optimal_slope = extreme(x2)

# Вычисляем значение функционала в точке экстремума
optimal_value = functional(t2)
print(optimal_value)

mpl_style(minor_ticks=False)
fig = plt.figure("3.1 visualization", figsize=(16, 9))
ax = fig.subplots()
ax.set_title("Решение краевой задачи с использованием метода пристрелки")
ax.plot(np.linspace(t1, t2, 5), [functional(t) for t in np.linspace(t1, t2, 5)], label="x(t)")
ax.plot(np.linspace(t1, t2, 5), [extreme(t) for t in np.linspace(t1, t2, 5)], label="экстремаль", linestyle="--")
ax.set_xlabel("t")
ax.set_ylabel("x")
ax.legend()
ax.grid(True)
plt.show()
