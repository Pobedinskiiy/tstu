import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style
from typing import Any

class Visualization:
    def __init__(self, func: Any, constraints: list, inv_bound: list) -> None:
        mpl_style(minor_ticks=False)
        self.func, self.constraints = func, constraints
        self.inv_bound = inv_bound
        self.plot_x, self.plot_y = [], []

    def plot(self, x_border: list, y_border: list, levels: int) -> None:
        fx, fy = np.linspace(*x_border, 1000), np.linspace(*y_border, 1000)
        fz = self.func(*np.meshgrid(fx, fy))
        fig = plt.figure("Litovka 2.2 visualization", figsize=(16, 9))
        ax = fig.subplots()
        fig.colorbar(ax.contour(fx, fy, fz, levels=levels, cmap="viridis"))
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid()
        for i in range(len(self.inv_bound)):
            fx_bound, fy_bound = fx, fy
            for j in range(len(fx_bound)):
                fy_bound[j] = self.inv_bound[i](fx_bound[j])
            ax.plot(fx_bound, fy_bound, color="grey")
        ax.plot(self.plot_x, self.plot_y, color="g")
        plt.show()