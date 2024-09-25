from typing import Any


class Simplex:
    def __init__(self, func: Any, x1: float, x2: float, eps: float = 0.01) -> None:
        self.func = func
        self.x1 = x1
        self.x2 = x2
        self.eps = eps

    def calculate(self) -> (float, float, int):
        pass