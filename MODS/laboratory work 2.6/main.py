import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    # Добавляем свободные переменные в матрицу ограничений
    tableau = np.hstack((A, np.eye(m), b.reshape(-1, 1)))  # Добавляем единичную матрицу для базисных переменных
    # Добавляем целевую функцию в виде -c
    tableau = np.vstack((tableau, np.hstack((-c, np.zeros(m + 1)))))  # Последняя строка - целевая функция

    while True:
        # Проверяем, есть ли отрицательные значения в последней строке (целевая функция)
        if all(x >= 0 for x in tableau[-1, :-1]):
            break  # Если все значения неотрицательные, выходим из цикла

        # Находим индекс столбца с наибольшим отрицательным значением (входящая переменная)
        entering = np.argmin(tableau[-1, :-1])

        # Вычисляем индексы, чтобы найти выходящую переменную
        ratios = np.full(m, np.inf)  # Инициализируем массив значениями бесконечности
        for i in range(m):
            if tableau[i, entering] > 0:  # Проверяем только положительные значения
                ratios[i] = tableau[i, -1] / tableau[i, entering]

        leaving = np.argmin(ratios)  # Находим строку с минимальным отношением

        # Обновляем симплекс-таблицу
        pivot = tableau[leaving, entering]
        tableau[leaving] /= pivot  # Нормализуем ведущую строку

        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i] -= tableau[i, entering] * tableau[leaving]

    # Получаем оптимальные значения переменных
    solution = np.zeros(n)
    for j in range(n):  # для всех переменных
        # Ищем, есть ли в базисе переменная j
        if np.any(tableau[:, j] == 1) and np.count_nonzero(tableau[:, j]) == 1:
            i = np.where(tableau[:, j] == 1)[0][0]  # Индекс строки с базисной переменной
            solution[j] = tableau[i, -1]  # Значение базисной переменной

    return solution, tableau[-1, -1]  # Возвращаем значения переменных и значение целевой функции

# Коэффициенты целевой функции (обратите внимание на знак)
c = np.array([23.1, -38.6])  # Знак изменен для минимизации

# Ограничения
A = np.array([
    [2.4, 5.2],
    [1, 0],
    [34, 21.6]
])

# Правая часть ограничений
b = np.array([48.1, 5, 375.3])

# Поиск оптимального решения
solution, optimal_value = simplex(c, A, b)

# Преобразуем значение целевой функции
optimal_value *= -1  # Так как мы максимизируем, а в коде используется минимизация

print(f"Оптимальное решение: x1 = {solution[0]:.4f}, x2 = {solution[1]:.4f}")
print(f"Максимальное значение Z = {optimal_value:.4f}")

