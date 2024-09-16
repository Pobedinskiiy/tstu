from methode import Method

class Halving(Method):
    def calculate(self) -> float:
        while self.b0 - self.a0 >= self.eps:
            x0 = (self.a0 + self.b0) / 2
            if self.func(self.a0) * self.func(self.b0) > 0:
                if self.func(x0) > self.func(x0 + self.eps):
                    self.a0 = x0
                else:
                    self.b0 = x0
            else:
                if self.func(self.a0) * self.func(x0) >= 0:
                    self.a0 = x0
                else:
                    self.b0 = x0
        return self.a0