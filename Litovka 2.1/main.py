import numpy as np
import matplotlib.pyplot as plt

from golden_ratio import GoldenRatio
from halving import Halving
from fibonacci import Fibonacci


def function(x: float) -> float:
    return x ** 3 - 13.5 * x ** 2 + 54 * x - 15

a0, b0, eps = 4.5, 9, 0.01
func_x = list(np.arange(a0, b0+eps, eps))
func_y = [function(x) for x in func_x]
goldRatio = GoldenRatio(a0, b0, function, eps)
print(goldRatio.calculate())
plt.plot(func_x, func_y)
plt.show()
hal = Halving(a0, b0, function, eps)
print(hal.calculate())
fib = Fibonacci(a0, b0, function, eps)
print(fib.calculate())
