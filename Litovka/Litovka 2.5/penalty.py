import numpy as np
from typing import Any

from visualization import Visualization


class Penalty(Visualization):
    def __init__(self, func: Any,
                 bounds: list,
                 inv_bounds: list,
                 x: float = 0, y: float = 0,
                 h: float = 1e-2, eps: float = 1e-2,
                 iterations: int = 100000) -> None:
        super().__init__(func, inv_bounds)
        self.bounds = bounds
        self.x, self.y = x, y
        self.h, self. eps = h, eps
        self.iterations = iterations
        self.x_stop, self.y_stop, self.z_stop = 0, 0, 0
        self.internal_penalty, self.end = False, False

    def __external(self, x: float, y: float) -> float:
        penalty, h = 0, 10
        for i in range(len(self.bounds)):
            func_val = self.bounds[i][0](x, y)
            if self.bounds[i][1] == "<" and func_val >= self.bounds[i][2]:
                penalty += h * func_val ** 2
            if self.bounds[i][1] == "<=" and func_val > self.bounds[i][2]:
                penalty += h * func_val ** 2
            if self.bounds[i][1] == ">" and func_val <= self.bounds[i][2]:
                penalty += h * func_val ** 2
            if self.bounds[i][1] == ">=" and func_val < self.bounds[i][2]:
                penalty += h * func_val ** 2
            if self.bounds[i][i] == "==" and func_val != self.bounds[i][2]:
                penalty += h * func_val ** 2
        return penalty

    def __internal(self, x: float, y: float) -> float:
        penalty, h = 0, 1e-3
        for i in range(len(self.bounds)):
            constrain_fz = self.bounds[i][0](x, y)
            if self.bounds[i][1] == "<" and constrain_fz >= self.bounds[i][2]:
                penalty += h / np.log(constrain_fz + 1e-10)
            if self.bounds[i][1] == "<=" and constrain_fz > self.bounds[i][2]:
                penalty += h / np.log(constrain_fz)
            if self.bounds[i][1] == ">" and constrain_fz <= self.bounds[i][2]:
                penalty += h / np.log(-constrain_fz - 1e-10)
            if self.bounds[i][1] == ">=" and constrain_fz < self.bounds[i][2]:
                penalty += h / np.log(-constrain_fz)
            if self.bounds[i][1] == "==":
                if constrain_fz < 0:
                    penalty += h / np.log(-constrain_fz)
                if constrain_fz > 0:
                    penalty += h / np.log(constrain_fz)
        return penalty

    def __func(self, x, y) -> float:
        return self.func(x, y) - self.__internal(x, y) + self.__external(x, y)

    def __estimate_gradient(self) -> (float, float):
        return ((self.__func(self.x + self.h, self.y) - self.__func(self.x, self.y)) / (2 * self.h),
                (self.__func(self.x, self.y + self.h) - self.__func(self.x, self.y)) / (2 * self.h))

    def calculate(self) -> (float, float, float):
        for _ in range(self.iterations):
            self.plot_x.append(self.x)
            self.plot_y.append(self.y)
            df_dx, df_dy = self.__estimate_gradient()
            if np.linalg.norm(np.array([df_dx, df_dy])) < self.eps:
                break
            self.x -= self.h * df_dx
            self.y -= self.h * df_dy
        return self.x, self.y, self.func(self.x, self.y)