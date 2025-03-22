import matplotlib.pyplot as plt
from qbstyles import mpl_style


c_0, c_1 = 6, 12
c_ent = 9
delta_c = 0.4
m_0, m_1 = 3.8, 5.4
m_ent = 4.2
delta_m = 0.2
temp_0, temp_1 = 120, 140
temp_p = 130
d_temp = 0.5

temp_r, r, k_t, F, c_t = 90, 2.26 * 1e+6, 5000, 10, 4187

m_vt = -k_t * F * (temp_p - temp_r) / (c_t * temp_p - r)

delta_time = 0.1
time_0, time_1 = 0, 500

sigma = 0.12                                                # кг
S = 0.75                                                    # м^2
P0, P1 = 7900, 7600                                         # кг/м^2

delta_c_ent = 4                                             # %
delta_m_ent = 3.2                                           # кг/м^2
delta_temp_p = 9                                            # °C


def get_c(c_in, m_in, t_in):
    return m_in * c_in / (m_in + k_t * F * (t_in - temp_r) / (c_t * temp_r - r))

def m_out(M):
    return sigma * ((P0 + M / S - P1) ** 0.5)

def dCdt(c_in, c_out, dM, M, m_in):
    return (m_in * c_in - m_out(M) * c_out - c_out * dM) / M

def dMdt(M, m_in, T):
    return (r * m_in - r * m_out(M) - k_t * F * (T - temp_r) - (m_in - m_out(M)) * c_t * temp_r) / (r - c_t * temp_r)

def main_count(M_0, C_0, c_in, m_in, t_in, param_in):
    time_i = time_0
    arr_c, arr_time, arr_param_in = [], [], []

    while time_i < time_1:
        arr_c.append(C_0)
        arr_time.append(time_i)

        if param_in == "C":
            if len(arr_c) == 2:
                c_in += delta_c_ent
            arr_param_in.append(c_in)
        elif param_in == "m":
            if len(arr_c) == 2:
                m_in += delta_m_ent
            arr_param_in.append(m_in)
        elif param_in == "T":
            if len(arr_c) == 2:
                t_in += delta_temp_p
            arr_param_in.append(t_in)

        d_M = dMdt(M_0, m_in, t_in)
        M_1 = M_0 + d_M * delta_time
        C_0 += dCdt(c_in, C_0, d_M, M_0, m_in) * delta_time
        M_0 = M_1

        time_i += delta_time

    return arr_c, arr_param_in, arr_time


if __name__ == "__main__":
    M0 = S * (((m_0 - m_vt) / sigma) ** 2 + P1 - P0)
    C0 = get_c(c_0, m_0, temp_0)

    C_ex_c, C_input, time_c = main_count(M0, C0, c_0, m_0, temp_0, "C")
    C_ex_m, m_input, time_m = main_count(M0, C0, c_0, m_0, temp_0, "m")
    C_ex_T, T_input, time_T = main_count(M0, C0, c_0, m_0, temp_0, "T")

    mpl_style(minor_ticks=False)
    fig = plt.figure("Laboratory 2", figsize=(16, 9))
    axs = fig.subplots(nrows=3, ncols=2)

    axs[0][0].plot(time_c, C_ex_c, color="r")
    axs[0][0].set_xlabel("time")
    axs[0][0].set_ylabel("C_ex")
    axs[0][0].grid(True)

    axs[0][1].plot(time_c, C_input, color="r")
    axs[0][1].set_xlabel("time")
    axs[0][1].set_ylabel("C_ent")
    axs[0][1].grid(True)

    axs[1][0].plot(time_m, C_ex_m, color="g")
    axs[1][0].set_xlabel("time")
    axs[1][0].set_ylabel("C_ex")
    axs[1][0].grid(True)

    axs[1][1].plot(time_m, m_input, color="g")
    axs[1][1].set_xlabel("time")
    axs[1][1].set_ylabel("m_ent")
    axs[1][1].grid(True)

    axs[2][0].plot(time_T, C_ex_T, color="b")
    axs[2][0].set_xlabel("time")
    axs[2][0].set_ylabel("C_ex")
    axs[2][0].grid(True)

    axs[2][1].plot(time_T, T_input, color="b")
    axs[2][1].set_xlabel("time")
    axs[2][1].set_ylabel("T_ent")
    axs[2][1].grid(True)

    plt.show()