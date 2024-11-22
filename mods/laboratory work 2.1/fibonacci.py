import math as m
from methode import Method

class Fibonacci(Method):
    @staticmethod
    def __fib(n):
        return m.pow((1 + m.sqrt(5)) / 2, n) - m.pow((1 - m.sqrt(5)) / 2, n) / m.sqrt(5)

    def calculate(self):
        num = int(m.ceil(m.log((2 * m.sqrt(5) * (self.b0 - self.a0)) / (self.eps * (3 + m.sqrt(5))), (1 + m.sqrt(5)) / 2)))
        x1 = self.a0 + self.__fib(num) * (self.b0 - self.a0) / self.__fib(num + 2)
        x2 = self.a0 + self.__fib(num + 1) * (self.b0 - self.a0) / self.__fib(num + 2)
        f2 = self.func(x2)
        f1 = self.func(x1)
        xx1, yx1, xx2, yx2 = [], [], [], []
        for k in range(1, num + 1):
            xx1.append(x1)
            yx1.append(self.func(x1))
            xx2.append(x2)
            yx2.append(self.func(x2))
            if f1 > f2:
                self.a0 = x1
                x1 = x2
                f1 = f2
                x2 = self.a0 + self.__fib(num - k + 2) * (self.b0 - self.a0) / self.__fib(num - k + 3)
                f2 = self.func(x2)
            if f1 < f2:
                self.b0 = x2
                x2 = x1
                f2 = f1
                x1 = self.a0 + self.__fib(num - k + 1) * (self.b0 - self.a0) / self.__fib(num - k + 3)
                f1 = self.func(x1)
        self.x.append(xx1)
        self.y.append(yx1)
        self.x.append(xx2)
        self.y.append(yx2)
        self.labels.extend(["Fibonacci values on the left", "Fibonacci values on the right"])
        return self.a0, num