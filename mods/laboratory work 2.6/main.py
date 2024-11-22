import numpy as np

from simplex import Simplex, OptType


simplex = Simplex(OptType.MIN,
                  np.array([[2.4, 5.2],
                            [1, 0],
                            [34, 21.6]]),
                  np.array([[48.1], [5], [375.3]]),
                  np.array([[-23.1], [38.6]]),
                  np.array([[-1], [1], [1]]),
                  100)

solution, optimal_value = simplex.calculate()

print(f"Оптимальное решение: x1 = {solution[0, 0]:.4f}, x2 = {solution[1, 0]:.4f}")
print(f"Минимальное значение Z = {optimal_value:.4f}")

simplex.plot()
