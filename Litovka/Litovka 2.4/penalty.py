import math
from typing import Any
from enum import Enum

from visualization import Visualization

class Barrier(Enum):
    EXTERNAL = 1
    INTERNAL = 2

class Penalty(Visualization):
    def __init__(self, func: Any, constraints: list,
                 x: float = 0, y: float = 0,
                 h: float = 1e-1, eps: float = 1e-3,
                 iterations: int = 10000) -> None:
        super().__init__(func, constraints)
        self.x, self.y = x, y
        self.h, self. eps = h, eps
        self.iterations = iterations

    def __external(self) -> float:
        penalty = 0
        for i in range(len(self.constraints)):
            func_val = self.constraints[i][0](self.x, self.y)
            if self.constraints[i][1] == "<" and func_val >= self.constraints[i][2]:
                penalty += self.h * func_val ** 2
            if self.constraints[i][1] == "<=" and func_val > self.constraints[i][2]:
                penalty += self.h * func_val ** 2
            if self.constraints[i][1] == ">" and func_val <= self.constraints[i][2]:
                penalty += self.h * func_val ** 2
            if self.constraints[i][1] == ">=" and func_val < self.constraints[i][2]:
                penalty += self.h * func_val ** 2
        return penalty

    def __internal(self) -> float:
        penalty = 0
        for i in range(len(self.constraints)):
            func_val = self.constraints[i][0](self.x, self.y)
            if self.constraints[i][1] == "<" and func_val > self.constraints[i][2]:
                penalty -= self.h / (func_val + 1e-6)
            if self.constraints[i][1] == "<=" and func_val >= self.constraints[i][2]:
                penalty -= self.h / (func_val + 1e-6)
            if self.constraints[i][1] == ">" and func_val < self.constraints[i][2]:
                penalty -= self.h / (func_val + 1e-6)
            if self.constraints[i][1] == ">=" and func_val <= self.constraints[i][2]:
                penalty -= self.h / (func_val + 1e-6)
        return penalty

    def __estimate_gradient(self) -> (float, float):
        return ((self.func(self.x + self.h, self.y) - self.func(self.x - self.h, self.y)) / (2 * self.h),
                (self.func(self.x, self.y + self.h) - self.func(self.x, self.y - self.h)) / (2 * self.h))

    def calculate(self, barrier: Barrier) -> (float, float):
        penalty = 0
        for _ in range(self.iterations):
            self.plot_x.append(self.x)
            self.plot_y.append(self.y)
            if barrier == Barrier.EXTERNAL:
                penalty = self.__external()
            else:
                penalty = self.__internal()
            df_dx, df_dy = self.__estimate_gradient()
            df_dx += penalty
            df_dy += penalty
            if math.sqrt(df_dx ** 2 + df_dy ** 2) < self.eps:
                break
            self.x -= self.h * df_dx
            self.y -= self.h * df_dy
        return self.x, self.y