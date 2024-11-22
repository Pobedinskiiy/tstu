import numpy as np
from typing import Any

from visualization import Visualization


class Simplex(Visualization):
    def __init__(self, func: Any, simplex: list = None, eps: float = 0.001, max_repeats: int = 1000) -> None:
        super().__init__(func)
        self.func = func
        if simplex is None:
            self.simplex = np.array([[0, 0], [0.1, 0.1], [0, 0.1]])
        self.eps = eps
        self.max_repeats = max_repeats


    def calculate(self) -> (float, float, int):
        for i in range(self.max_repeats):
            self.x1_.extend([self.simplex[0][0], self.simplex[1][0], self.simplex[2][0]])
            self.x2_.extend([self.simplex[0][1], self.simplex[1][1], self.simplex[2][1]])
            func_vertices = np.array([self.func(*vertex) for vertex in self.simplex])

            sorted_indices = np.argsort(func_vertices)
            self.simplex = self.simplex[sorted_indices]

            worst = self.simplex[-1]

            centroid = np.mean(self.simplex[:-1], axis=0)

            reflection = centroid + (centroid - worst)
            reflection_value = self.func(*reflection)

            if func_vertices[0] <= reflection_value < func_vertices[-2]:
                self.simplex[-1] = reflection
            elif reflection_value < func_vertices[0]:
                expansion = centroid + 2 * (centroid - worst)
                expansion_value = self.func(*expansion)
                if expansion_value < reflection_value:
                    self.simplex[-1] = expansion
                else:
                    self.simplex[-1] = reflection
            else:
                contraction = centroid - 0.5 * (centroid - worst)
                contraction_value = self.func(*contraction)
                if contraction_value < func_vertices[-1]:
                    self.simplex[-1] = contraction
                else:
                    self.simplex[1:] = self.simplex[0] + 0.5 * (self.simplex[1:] - self.simplex[0])

            if np.max(np.abs(func_vertices - func_vertices[0])) < self.eps:
                return *self.simplex[0], i
        return *self.simplex[0], self.max_repeats