from methode import Method

class GoldenRatio(Method):
    at: float = (3 - 5 ** 0.5) / 2

    def __cal_val_at(self) -> float:
        return (self.b0 - self.a0) * self.at

    def calculate(self) -> float:
        val_at = self.__cal_val_at()
        x1, x2 = self.a0 + val_at, self.b0 - val_at
        while self.b0 - self.a0 >= self.eps:
            if self.func(x1) < self.func(x2):
                self.b0 = x2
                x2 = x1
                x1 = self.a0 + self.__cal_val_at()
            else:
                self.a0 = x1
                x1 = x2
                x2 = self.b0 - self.__cal_val_at()
        return self.a0