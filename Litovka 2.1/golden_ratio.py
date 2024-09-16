from methode import Method

class GoldenRatio(Method):
    at: float = (3 - 5 ** 0.5) / 2

    def __cal_val_at(self) -> float:
        return (self.b0 - self.a0) * self.at

    def calculate(self):
        val_at = self.__cal_val_at()
        x1, x2 = self.a0 + val_at, self.b0 - val_at
        xx1, yx1, xx2, yx2 = [], [], [], []
        count = 0
        while self.b0 - self.a0 >= self.eps:
            count += 1
            xx1.append(x1)
            yx1.append(self.func(x1))
            xx2.append(x2)
            yx2.append(self.func(x2))
            if self.func(x1) < self.func(x2):
                self.b0 = x2
                x2 = x1
                x1 = self.a0 + self.__cal_val_at()
            else:
                self.a0 = x1
                x1 = x2
                x2 = self.b0 - self.__cal_val_at()
        self.x.append(xx1)
        self.y.append(yx1)
        self.x.append(xx2)
        self.y.append(yx2)
        self.labels.extend(["The value of the golden ratio on the left", "The value of the golden ratio on the right"])
        return self.a0, count