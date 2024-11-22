from typing import Any

from visualization import Visualization


class Method(Visualization):
    def __init__(self, a0: float, b0: float, func: Any, eps: float) -> None:
        if a0 > b0:
            a0, b0 = b0, a0
        super().__init__(a0, b0, func, eps)
        self.a0 = a0
        self.b0 = b0
        self.func = func
        self.eps = eps

    def calculate(self) -> (float, int):
        pass