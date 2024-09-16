from golden_ratio import GoldenRatio
from halving import Halving
from fibonacci import Fibonacci


def function(x: float) -> float:
    return x ** 3 - 13.5 * x ** 2 + 54 * x - 15

goldRatio = GoldenRatio(4.5, 9, function, 0.01)
print(goldRatio.calculate())
hal = Halving(4.5, 9, function, 0.01)
print(hal.calculate())
fib = Fibonacci(4.5, 9, function, 0.01)
print(fib.calculate())
