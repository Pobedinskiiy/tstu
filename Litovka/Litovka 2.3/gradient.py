import math
from typing import Any

from visualization import Visualization


class Gradient(Visualization):
    def __init__(self, func: Any,
                 x: float = 0, y: float = 0,
                 h: float = 1e-1, eps: float = 1e-3,
                 iterations: int = 1000) -> None:
        super().__init__(func)
        self.x, self.y = x, y
        self.h, self.eps = h, eps
        self.iterations = iterations

    def __estimate_gradient(self) -> (float, float):
        return ((self.func(self.x + self.h, self.y) - self.func(self.x - self.h, self.y)) / (2 * self.h),
                (self.func(self.x, self.y + self.h) - self.func(self.x, self.y - self.h)) / (2 * self.h))

    def calculate(self) -> (float, float):
        for _ in range(self.iterations):
            self.plot_x.append(self.x)
            self.plot_y.append(self.y)
            df_dx, df_dy = self.__estimate_gradient()
            if math.sqrt(df_dx ** 2 + df_dy ** 2) < self.eps:
                break
            self.x -= self.h * df_dx
            self.y -= self.h * df_dy
        return self.x, self.y