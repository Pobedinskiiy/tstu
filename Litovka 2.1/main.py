from golden_ratio import GoldenRatio
from halving import Halving
from fibonacci import Fibonacci


def function(x: float) -> float:
    return x ** 3 - 13.5 * x ** 2 + 54 * x - 15

a0, b0, eps = 4.5, 9, 0.01
hal = Halving(a0, b0, function, eps)
print(hal.calculate())
hal.plot()
goldRatio = GoldenRatio(a0, b0, function, eps)
print(goldRatio.calculate())
goldRatio.plot()
fib = Fibonacci(a0, b0, function, eps)
print(fib.calculate())
fib.plot()
