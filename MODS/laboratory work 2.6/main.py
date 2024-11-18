import numpy as np


def simplex(c, A, b):
    m, n = A.shape
    # Объединяем A и b в одну матрицу с добавлением свободных переменных
    tableau = np.hstack((A, np.eye(m), b.reshape(-1, 1)))  # добавляем бюджетные переменные
    tableau = np.vstack((tableau, np.hstack((c, np.zeros(m + 1)))))

    while True:
        # Проверяем, есть ли отрицательные значения в последней строке (целевая функция)
        if all(x >= 0 for x in tableau[-1, :-1]):
            break

        # Находим индекс столбца с наибольшим отрицательным значением (входящая переменная)
        entering = np.argmin(tableau[-1, :-1])

        # Вычисляем индексы, чтобы найти выходящую переменную
        ratios = tableau[:-1, -1] / tableau[:-1, entering]
        ratios[ratios <= 0] = np.inf  # игнорируем неактивные переменные
        leaving = np.argmin(ratios)

        # Обновляем симплекс-таблицу
        pivot = tableau[leaving, entering]
        tableau[leaving] /= pivot  # Нормализуем ведущую строку

        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i] -= tableau[i, entering] * tableau[leaving]

    # Получаем оптимальные значения переменных
    solution = np.zeros(n)
    for i in range(m):
        if np.count_nonzero(tableau[i, :-1]) == 1:  # если есть только одна единица в строке
            j = np.where(tableau[i, :-1] == 1)[0][0]
            solution[j] = tableau[i, -1]

    return solution, tableau[-1, -1]


# Коэффициенты целевой функции
c = np.array([5, 3])

# Ограничения
A = np.array([
    [2, 1],
    [1, 2]
])

# Правая часть ограничений
b = np.array([8, 10])

# Поиск оптимального решения
solution, optimal_value = simplex(c, A, b)
print(f"Оптимальное решение: x1 = {solution[0]:.4f}, x2 = {solution[1]:.4f}")
print(f"Максимальное значение Z = {optimal_value:.4f}")
