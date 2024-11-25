import numpy as np
import matplotlib.pyplot as plt
from qbstyles import mpl_style


class Visualization:
    def __init__(self, c: np.ndarray) -> None:
        mpl_style(minor_ticks=False)
        self.c = c
        self.x, self.y = 0, 0

    @staticmethod
    def __func(fx: float, fy: float, cx: float, cy: float) -> float:
        return fx * cx + fy * cy

    @staticmethod
    def __func_bound(fx: float, cx: float, cy: float, fz: float) -> float:
        return (fz - fx * cx) / cy

    def plot(self, x_border: list, y_border: list, levels: int) -> None:
        fig = plt.figure("mods 2.2 visualization", figsize=(16, 9))
        ax = fig.subplots()
        fx, fy = np.linspace(*x_border, 1000), np.linspace(*y_border, 1000)
        fz =  self.__func(*np.meshgrid(fx, fy), float(self.c[0][0]), float(self.c[1][0]))
        fig.colorbar(ax.contour(fx, fy, fz, levels=levels, cmap="viridis"))
        fx = np.linspace(*x_border, 1000)
        fy = self.__func_bound(*np.meshgrid(fx), 2.4, 5.2, 48.1)
        ax.plot(fx, fy)
        ax.plot([5, 5], y_border)
        fy = np.linspace(*x_border, 1000)
        fx = self.__func_bound(*np.meshgrid(fy), 21.6, 34, 375.3)
        ax.plot(fx, fy)
        ax.scatter(self.x, self.y, color="blue")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid()
        plt.show()