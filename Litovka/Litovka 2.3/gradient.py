import math
from typing import Any

from visualization import Visualization


class Gradient(Visualization):
    def __init__(self, func: Any, x0: float, y0: float, h0: float = 0.1, eps: float = 0.001, iterations: int = 1000) -> None:
        super().__init__(func)
        self.func = func
        self.x0 = x0
        self.y0 = y0
        self.h0 = h0
        self.eps = eps
        self.iterations = iterations

    def __estimate_gradient(self, x: float, y: float, h: float = 1e-6) -> (float, float):
        return ((self.func(x + h, y) - self.func(x - h, y)) / (2 * h),
                (self.func(x, y + h) - self.func(x, y - h)) / (2 * h))

    def calculate(self) -> (float, float):
        df_dx, df_dy = 0, 0
        for _ in range(self.iterations):
            self.plot_x.append(self.x0)
            self.plot_y.append(self.y0)
            if self.func(self.x0, self.y0) <= self.func(self.x0 - self.h0 * df_dx, self.y0 - self.h0 * df_dy):
                df_dx, df_dy = self.__estimate_gradient(self.x0, self.y0)
            if math.sqrt(df_dx ** 2 + df_dy ** 2) < self.eps:
                break
            self.x0 -= self.h0 * df_dx
            self.y0 -= self.h0 * df_dy
        return self.x0, self.y0