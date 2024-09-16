from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style

class Visualization:
    def __init__(self, a0: float, b0: float, func, eps: float) -> None:
        mpl_style(minor_ticks=False)
        self.fig = plt.figure("Litovka 2.1 visualization", figsize=(16, 9))
        self.ax = self.fig.subplots()
        self.x: list = []
        self.y: list = []
        self.labels: list = []
        self.func_x = list(np.arange(a0, b0 + eps, eps))
        self.func_y = [func(x) for x in self.func_x]

    def plot(self) -> None:
        self.ax.plot(self.func_x, self.func_y, color=np.random.rand(3,), label="Function")
        for i in range(len(self.x)):
            self.ax.scatter(self.x[i], self.y[i], color=np.random.rand(3,), label=self.labels[i])
        self.ax.legend(frameon=True, loc="upper left", fontsize=12)
        self.fig.show()
        plt.pause(60)
        plt.close("all")