class Method:
    def __init__(self, a0, b0, func, eps) -> None:
        if a0 > b0:
            a0, b0 = b0, a0
        self.a0 = a0
        self.b0 = b0
        self.func = func
        self.eps = eps

    def calculate(self) -> float:
        pass