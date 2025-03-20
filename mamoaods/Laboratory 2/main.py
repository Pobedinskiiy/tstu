import matplotlib.pyplot as plt


Tr, r, kt, F, ct = 90, 2.26 * 1e+6, 5000, 10, 4187

delta_t = 0.1               # с
t0, t1 = 0, 500             # с

sigma = 0.12                # кг
S = 0.75                    # м^2
P0, P1 = 7900, 7600         # кг/м^2

delta_Cent = 4              # %
delta_Ment = 3.2            # кг/м^2
delta_Tp = 9                # °C

c0, m0, T0 = 6, 3.8, 120


def get_C(c_in, m_in, t_in):
    return m_in * c_in / (kt * F * (t_in - Tr) / (ct * Tr - r) + m_in)

def M(m):
    return S * ((m / sigma) ** 2 + P1 - P0)

def m_out(M):
    return sigma * ((P0 + M / S - P1) ** 0.5)

def dCdt(c_in, c_out, dM, M, m_in):
    return (m_in * c_in - m_out(M) * c_out - c_out * dM) / M

def dMdt(M, m_in, T):
    return (r * m_in - r * m_out(M) - kt * F * (T - Tr) - (m_in - m_out(M)) * ct * Tr) / (r - ct * Tr)

def main_count(M0, C0, c_in, m_in, t_in, param):
    tao_i = t0

    C, tao, in_p = [C0], [t0], []

    if param == "C":
        in_p.append(c_in)
    elif param == "T":
        in_p.append(t_in)
    elif param == "m":
        in_p.append(m_in)

    while tao_i < t1:
        d_M = dMdt(M0, m_in, t_in)
        M1 = M0 + d_M * delta_t
        C1 = C0 + dCdt(c_in, C0, d_M, M0, m_in) * delta_t

        C.append(C1)
        tao.append(tao_i)

        if len(C) == 10:
            if param == "C":
                c_in += delta_Cent
            elif param == "T":
                t_in += delta_Tp
            elif param == "m":
                m_in += delta_Ment

        if param == "C":
            in_p.append(c_in)
        elif param == "T":
            in_p.append(t_in)
        elif param == "m":
            in_p.append(m_in)

        M0 = M1
        C0 = C1

        tao_i += delta_t

    return C, in_p, tao


if __name__ == "__main__":
    M0 = M(m0 - m0 * c0 / 100)
    C0 = get_C(c0, m0, T0)

    C1, C_input, tao1 = main_count(M0, C0, c0, m0, T0, "C")
    C2, T_input, tao2 = main_count(M0, C0, c0, m0, T0, "T")
    C3, m_input, tao3 = main_count(M0, C0, c0, m0, T0, "m")

    fig, ax = plt.subplots(3, ncols=2, figsize=(8, 10))

    ax[0][0].plot(tao1, C1, color="r")
    ax[0][0].set_xlabel("tao")
    ax[0][0].set_ylabel("C")
    ax[0][0].grid()

    ax[1][0].plot(tao2, C2, color="g")
    ax[1][0].set_xlabel("tao")
    ax[1][0].set_ylabel("C")
    ax[1][0].grid()

    ax[2][0].plot(tao3, C3, color="b")
    ax[2][0].set_xlabel("tao")
    ax[2][0].set_ylabel("C")
    ax[2][0].grid()

    ax[0][1].plot(tao1, C_input, color="r")
    ax[0][1].set_xlabel("tao")
    ax[0][1].set_ylabel("C_in")
    ax[0][1].grid()

    ax[1][1].plot(tao2, T_input, color="g")
    ax[1][1].set_xlabel("tao")
    ax[1][1].set_ylabel("T_in")
    ax[1][1].grid()

    ax[2][1].plot(tao3, m_input, color="b")
    ax[2][1].set_xlabel("tao")
    ax[2][1].set_ylabel("m_in")
    ax[2][1].grid()

    plt.show()