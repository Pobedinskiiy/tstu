import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style

# Определение функционала
def functional(t):
    return 0.3 * t - 0.3 / t ** 2 + (t * np.log(t)) / 3

# Определение базисной функции
def basis_function(t, a, b):
    return a * t + b  # Линейная комбинация

# Определение функционала для метода Ритца
def ritz_functional(a, b, t):
    # Вычисляем интеграл функционала
    return np.trapz((basis_function(t, a, b) - functional(t)) ** 2, t)

# Оптимизация коэффициентов
def optimize_coefficients(t, tolerance=1e-6):
    a, b = 0.0, 0.0
    learning_rate = 0.01
    prev_value = ritz_functional(a, b, t)

    while True:  # Количество итераций
        # Вычисление градиента
        grad_a = (ritz_functional(a + learning_rate, b, t) - ritz_functional(a, b, t)) / learning_rate
        grad_b = (ritz_functional(a, b + learning_rate, t) - ritz_functional(a, b, t)) / learning_rate
        # Обновление коэффициентов
        a -= learning_rate * grad_a
        b -= learning_rate * grad_b

        # Вычисление нового значения функционала
        current_value = ritz_functional(a, b, t)

        # Проверка условия остановки
        if abs(current_value - prev_value) < tolerance:
            break

        prev_value = current_value
    return a, b

# Основной код
t = np.linspace(1, 2, 100)  # Интервал
a_opt, b_opt = optimize_coefficients(t)  # Оптимизация коэффициентов

# Построение графика
mpl_style(minor_ticks=False)
plt.plot(t, functional(t), label="Функционал")
plt.plot(t, basis_function(t, a_opt, b_opt), label="Решение методом Ритца", linestyle="--")
plt.xlabel("t")
plt.ylabel("x")
plt.title("Метод Ритца")
plt.grid(True)
plt.legend()
plt.show()

print(f"Оптимальные коэффициенты: a = {a_opt:.4f}, b = {b_opt:.4f}")
