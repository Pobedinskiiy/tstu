import numpy as np
from typing import Any
from enum import Enum

from visualization import Visualization

class Barrier(Enum):
    EXTERNAL = 1
    INTERNAL = 2

class Penalty(Visualization):
    def __init__(self, func: Any, constraints: list, inv_bound: list,
                 barrier: Barrier = Barrier.EXTERNAL,
                 x: float = 0, y: float = 0,
                 h: float = 1e-2, eps: float = 1e-2,
                 iterations: int = 100000) -> None:
        super().__init__(func, constraints, inv_bound)
        self.x, self.y = x, y
        self.barrier = barrier
        self.h, self. eps = h, eps
        self.iterations = iterations
        self.x_stop, self.y_stop, self.z_stop = 0, 0, 0
        self.internal_penalty, self.end = False, False

    def __external(self, x: float, y: float) -> float:
        penalty, h = 0, 1e-1
        for i in range(len(self.constraints)):
            func_val = self.constraints[i][0](x, y)
            if self.constraints[i][1] == "<" and func_val >= self.constraints[i][2]:
                penalty += h * func_val ** 2
            if self.constraints[i][1] == "<=" and func_val > self.constraints[i][2]:
                penalty += h * func_val ** 2
            if self.constraints[i][1] == ">" and func_val <= self.constraints[i][2]:
                penalty += h * func_val ** 2
            if self.constraints[i][1] == ">=" and func_val < self.constraints[i][2]:
                penalty += h * func_val ** 2
        return penalty

    def __internal(self, x: float, y: float) -> float:
        penalty, h = 0, 1e-2
        for i in range(len(self.constraints)):
            constrain_fz = self.constraints[i][0](x, y)
            if self.constraints[i][1] == "<" and constrain_fz >= self.constraints[i][2]:
                penalty += h / np.log(constrain_fz + 1e-10)
            if self.constraints[i][1] == "<=" and constrain_fz > self.constraints[i][2]:
                penalty += h / np.log(constrain_fz)
            if self.constraints[i][1] == ">" and constrain_fz <= self.constraints[i][2]:
                penalty += h / np.log(-constrain_fz - 1e-10)
            if self.constraints[i][1] == ">=" and constrain_fz < self.constraints[i][2]:
                penalty += h / np.log(-constrain_fz)
        return penalty

    def __func(self, x, y) -> float:
        if self.barrier == Barrier.EXTERNAL:
            penalty = self.__external(x, y)
        else:
            penalty = -self.__internal(x, y)
        return self.func(x, y) + penalty

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