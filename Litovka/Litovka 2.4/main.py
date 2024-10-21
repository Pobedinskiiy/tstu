import numpy as np


a, b, c, d, alpha = -6, -1, 2, 3, 20

def function_ellipse(x: float, y: float) -> float:
    return ((((x - a) * np.cos(alpha) + (y - b) * np.sin(alpha)) / c) ** 2
            + (((y - b) * np.cos(alpha) - (x - a) * np.sin(alpha)) / d) ** 2)

def constraint_function_1(x: float, y: float) -> float:
    return x ** 2 + 2 * y ** 3 - 8

def constraint_function_2(x: float, y: float) -> float:
    return x + y



"""
import numpy as np
import matplotlib.pyplot as plt

# Определяем целевую функцию
def objective_function(x, y):
    return (x - 1) ** 2 + (y - 2) ** 2

# Функции ограничений
def g1(x, y):
    return x + y - 3  # g1(x, y) <= 0

def g2(x, y):
    return x - 1.5   # g2(x, y) <= 0

# Внешняя штрафная функция
def external_penalty(x, y, penalty_factor):
    penalty = 0
    if g1(x, y) > 0:
        penalty += penalty_factor * (g1(x, y) ** 2)
    if g2(x, y) > 0:
        penalty += penalty_factor * (g2(x, y) ** 2)
    return penalty

# Внутренняя штрафная функция
def internal_barrier(x, y, barrier_factor):
    penalty = 0
    if g1(x, y) >= 0:
        penalty -= barrier_factor / (g1(x, y) + 1e-6)  # Используем небольшой сдвиг, чтобы избежать деления на ноль
    if g2(x, y) >= 0:
        penalty -= barrier_factor / (g2(x, y) + 1e-6)
    return penalty

# Метод штрафных функций
def penalty_method(x0, y0, penalty_factor, barrier_factor, max_iterations):
    x, y = x0, y0
    history = []

    for _ in range(max_iterations):
        # Модифицированная функция
        modified_function = (objective_function(x, y) + 
                              external_penalty(x, y, penalty_factor) +
                              internal_barrier(x, y, barrier_factor))
        
        history.append((x, y, modified_function))

        # Применим градиентный спуск для нахождения минимума
        gradient_x = 2 * (x - 1) + 2 * penalty_factor * (g1(x, y) if g1(x, y) > 0 else 0) \
                      - (barrier_factor / (g1(x, y) + 1e-6) ** 2 if g1(x, y) > 0 else 0)
        
        gradient_y = 2 * (y - 2) + 2 * penalty_factor * (g2(x, y) if g2(x, y) > 0 else 0) \
                      - (barrier_factor / (g2(x, y) + 1e-6) ** 2 if g2(x, y) > 0 else 0)

        # Обновление переменных
        x -= 0.01 * gradient_x  # Шаг по x
        y -= 0.01 * gradient_y  # Шаг по y

    return x, y, history

# Параметры
x0 = 0.0
y0 = 0.0
penalty_factor = 1000
barrier_factor = 1000
max_iterations = 100

# Поиск минимума
min_x, min_y, history = penalty_method(x0, y0, penalty_factor, barrier_factor, max_iterations)

print("Минимум достигается в точке (x, y): ({:.2f}, {:.2f})".format(min_x, min_y))
print("Минимальное значение функции: {:.2f}".format(objective_function(min_x, min_y)))

# Визуализация процесса
x_vals = [point[0] for point in history]
y_vals = [point[1] for point in history]
z_vals = [point[2] for point in history]

plt.plot(x_vals, y_vals, marker='o')
plt.title('Сходимость метода штрафных функций')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
"""