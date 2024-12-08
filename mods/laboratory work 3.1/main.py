import numpy as np
import matplotlib.pyplot as plt

# Определим параметры
a = -1  # Начальная точка
b = 0   # Конечная точка
N = 100  # Количество узлов
h = (b - a) / N  # Шаг

# Создадим матрицу для метода прогонки
A = np.zeros((N+1, N+1))
d = np.zeros(N+1)

# Задать уравнение x^{(4)} = 120
for i in range(2, N):
    A[i, i-2] = 1          # x''(i) = x(i-2)
    A[i, i] = -4           # x''(i) = x(i)
    A[i, i+2] = 1          # x''(i) = x(i+2)
    d[i] = 120 * h**4      # Правые части

# Граничные условия
# Задаем уравнения на границах системы линейных уравнений
# 1. x(-1) = 1
A[0, 0] = 1
d[0] = 1

# 2. x(0) = 0
A[1, 1] = 1
d[1] = 0

# 3. x'(-1) = -4.5
A[2, 0] = -1 / h
A[2, 1] = 1 / h
d[2] = -4.5

# 4. x'(0) = 0
A[3, -1] = -1 / h
A[3, -2] = 1 / h
d[3] = 0

# 5. x''(-1) = 16
A[4, 0] = 2 / h**2
A[4, 1] = -4 / h**2
A[4, 2] = 2 / h**2
d[4] = 16

# 6. x''(0) = 0
A[5, -3] = 2 / h**2
A[5, -2] = -4 / h**2
A[5, -1] = 2 / h**2
d[5] = 0

# Прямой ход для прогонки
c = np.zeros(N+1)
b = np.zeros(N+1)

c[0] = A[0, 0]
b[0] = d[0] / c[0]

for i in range(1, N+1):
    c[i] = A[i, i] - A[i, i-1] * A[i-1, i] / c[i-1]
    b[i] = (d[i] - A[i, i-1] * b[i-1]) / c[i]

# Обратный ход для прогонки
x = np.zeros(N+1)
x[-1] = b[-1]

for i in range(N-1, -1, -1):
    x[i] = b[i] - A[i, i+1] * x[i+1] / c[i]

# Узлы
t = np.linspace(a, b, N+1)

# Визуализация решения
plt.plot(t, x, label='x(t)', color='blue')
plt.title("Решение дифференциального уравнения")
plt.xlabel("t")
plt.ylabel("x")
plt.grid()
plt.legend()
plt.show()