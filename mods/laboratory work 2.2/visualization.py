import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style
from typing import Any

class Visualization:
    def __init__(self, func: Any):
        mpl_style(minor_ticks=False)
        self.func = func
        self.x1_, self.x2_ = [], []

    def plot(self, x_border: list, y_border: list, levels: int) -> None:
        x, y = np.linspace(*x_border, 1000), np.linspace(*y_border, 1000)
        z = self.func(*np.meshgrid(x, y))
        fig = plt.figure("mods 2.2 visualization", figsize=(16, 9))
        ax = fig.subplots()
        fig.colorbar(ax.contour(x, y, z, levels=levels, cmap="viridis"))
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid()
        ax.plot(self.x1_, self.x2_, color="g")
        plt.show()