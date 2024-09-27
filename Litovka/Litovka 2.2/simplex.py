from typing import Any


class Simplex:
    def __init__(self, func: Any, x1: float, x2: float, eps: float = 0.01, h0: float = 0.001) -> None:
        self.func = func
        self.x1 = x1
        self.x2 = x2
        self.eps = eps
        self.h0 = h0
        self.x3 = x1 + h0
        self.x4 = x2
        self.x5 = x1
        self.x6 = x2 + h0
        self.fx0 = self.func(self.x1, self.x2)
        self.fx1 = self.func(self.x3, self.x4)
        self.fx2 = self.func(self.x5, self.x6)

    def calculate(self) -> (float, float, int):
        count, end = 0, 0
        fx0, fx1, fx2 = self.fx0, self.fx1, self.fx2
        while end != 2:
            if fx0 == self.fx0 or fx1 == self.fx1 or fx2 == self.fx2:
                if end == 1:
                    fx0, fx1, fx2 = self.fx0, self.fx1, self.fx2
                end += 1
            else:
                end = 0

            if self.fx0 > self.fx1 and self.fx0 > self.fx2:
                pass
            elif self.fx1 > self.fx2:
                pass
            else:
                pass

            self.fx0 = self.func(self.x1, self.x2)
            self.fx1 = self.func(self.x3, self.x4)
            self.fx2 = self.func(self.x5, self.x6)

            count += 1
        return self.x1, self.x2, count
