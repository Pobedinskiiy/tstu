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

def get_c(c_in, m_in, t_in):
    return (m_in * c_in) / (m_in + ((k_t * F * (t_in - temp_r)) / (c_t * t_in - r)))


if __name__ == "__main__":
    C0_values, C_exC0_values = [], []
    m0_values, C_exm0_values = [], []
    T0_values, C_exT0_values = [], []

    while c_0 < c_1:
        C_ex = get_c(c_0, m_ent, temp_p)
        C0_values.append(c_0)
        C_exC0_values.append(C_ex)
        c_0 += delta_c

    while m_0 < m_1:
        C_ex = get_c(c_ent, m_0, temp_p)
        m0_values.append(m_0)
        C_exm0_values.append(C_ex)
        m_0 += delta_m

    while temp_0 < temp_1:
        C_ex = get_c(c_ent, m_ent, temp_0)
        T0_values.append(temp_0)
        C_exT0_values.append(C_ex)
        temp_0 += d_temp

    mpl_style(minor_ticks=False)
    fig = plt.figure("Laboratory 1", figsize=(16, 9))
    axs = fig.subplots(nrows=3, ncols=1)
    axs[0].plot(C0_values, C_exC0_values, color="r")
    axs[0].set_xlabel("C0")
    axs[0].set_ylabel("C_ex")
    axs[0].grid(True)

    axs[1].plot(m0_values, C_exm0_values, color="g")
    axs[1].set_xlabel("m0")
    axs[1].set_ylabel("C_ex")
    axs[1].grid(True)

    axs[2].plot(T0_values, C_exT0_values, color="b")
    axs[2].set_xlabel("T0")
    axs[2].set_ylabel("C_ex")
    axs[2].grid(True)

    plt.show()
