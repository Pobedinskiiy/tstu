from math import  pi, exp, ceil
import matplotlib.pyplot as plt
from qbstyles import mpl_style


R, E1, E2, A1, A2, ro, D, dL = 8.31, 251e3, 297e3, 2e11, 8e12, 1.4, 0.1, 0.5

m, L, T = 2.0, 200, 1300
c_0, c_1, = 25, 37
dC = 0.05 * (c_1 - c_0)

mu = m / ((ro * pi * D ** 2) / 4)


def k(A, E, T):
    return A * exp(-E / (R * T))


def dC1(T, C1):
    return (-k(A1, E1, T) * C1) / mu


def dC2(T, C1, C2):
    return (k(A1, E1, T) * C1 - k(A2, E2, T) * C2) / mu


def count():
    GRAPH = []
    Ci = c_0
    while Ci <= c_1:
        C10 = Ci * ro / (100 * 0.028)
        C20 = 0
        li = 0
        c1 = [C10]
        c2 = [C20]
        l = [li]
        while li <= L:
            dc1 = dC1(T, C10)
            C1 = C10 + dc1 * dL
            dc2 = dC2(T, C1, C20)
            C2 = C20 + dc2 * dL

            c1.append(C1)
            c2.append(C2)
            l.append(li)

            C10 = C1
            C20 = C2
            li += dL

        GRAPH.append((l, c1, c2, Ci))
        Ci = round(Ci + dC, 2)

    return GRAPH


if __name__ == "__main__":
    GRAPH = count()
    mpl_style(minor_ticks=False)
    fig = plt.figure("Laboratory 3", figsize=(16, 9))
    axs = fig.subplots(nrows=1, ncols=2)

    cp = 0.0
    for gr in GRAPH:
        l, c1, c2, Ti = gr
        axs[0].plot(l, c1, color=(1.0, cp, 0.0), label=f"C ent = {round(Ti, 2)}")
        axs[1].plot(l, c2, color=(0.0, cp, 1.0), label=f"C ent = {round(Ti, 2)}")
        cp += 1 / len(GRAPH)

    axs[0].set(xlabel="L", ylabel="C1")
    axs[1].set(xlabel="L", ylabel="C2")

    axs[0].grid(True)
    axs[1].grid(True)

    axs[0].legend()
    axs[1].legend()

    plt.show()
