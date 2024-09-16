from methode import Method

class Halving(Method):
    def calculate(self):
        x, y = [], []
        count = 0
        while self.b0 - self.a0 >= self.eps:
            count += 1
            x0 = (self.a0 + self.b0) / 2
            x.append(x0)
            y.append(self.func(x0))
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
        self.x.append([x])
        self.y.append([y])
        self.labels.append("Half of the segment")
        return self.a0, count