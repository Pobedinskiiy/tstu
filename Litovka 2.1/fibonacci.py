import math as m
from methode import Method

class Fibonacci(Method):
    @staticmethod
    def __fib(n):
        return m.pow((1 + m.sqrt(5)) / 2, n) - m.pow((1 - m.sqrt(5)) / 2, n) / m.sqrt(5)

    def calculate(self) -> float:
        num = int(m.ceil(m.log((2 * m.sqrt(5) * (self.b0 - self.a0)) / (self.eps * (3 + m.sqrt(5))), (1 + m.sqrt(5)) / 2)))
        xx1 = self.a0 + self.__fib(num) * (self.b0 - self.a0) / self.__fib(num + 2)
        xx2 = self.a0 + self.__fib(num + 1) * (self.b0 - self.a0) / self.__fib(num + 2)
        f2 = self.func(xx2)
        f1 = self.func(xx1)
        for k in range(1, num + 1):
            if f1 > f2:
                self.a0 = xx1
                xx1 = xx2
                f1 = f2
                xx2 = self.a0 + self.__fib(num - k + 2) * (self.b0 - self.a0) / self.__fib(num - k + 3)
                f2 = self.func(xx2)
            if f1 < f2:
                self.b0 = xx2
                xx2 = xx1
                f2 = f1
                xx1 = self.a0 + self.__fib(num - k + 1) * (self.b0 - self.a0) / self.__fib(num - k + 3)
                f1 = self.func(xx1)
        return self.a0