import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style
from typing import Any

class Visualization:
    def __init__(self, func: Any, constraints: list) -> None:
        mpl_style(minor_ticks=False)
        self.func, self.constraints = func, constraints
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
        fx_c, fy_c = [], []
        for i in range(len(fx)):
            for j in range(len(fy)):
                if -0.06 < self.constraints[0][0](fx[i], fy[j]) < 0:
                    fx_c.append(fx[i])
                    fy_c.append(fy[j])
        ax.plot(fx_c, fy_c, color="grey")
        fx_c, fy_c = [], []
        for i in range(len(fx)):
            for j in range(len(fy)):
                if 0 <= self.constraints[1][0](fx[i], fy[j]) <= 1e-2:
                    fx_c.append(fx[i])
                    fy_c.append(fy[j])
        ax.plot(fx_c, fy_c, color="grey")
        ax.plot(self.plot_x, self.plot_y, color="g")
        plt.show()