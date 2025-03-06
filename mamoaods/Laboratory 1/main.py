import matplotlib.pyplot as plt


C0, C1 = 6, 12
C_ent = 9
d_C = 0.4
m0, m1 = 3.8, 5.4
m_ent = 4.2
d_m = 0.2
T0, T1 = 120, 140
Tp = 130
d_T = 0.5

Tr, r, kt, F, c1 = 90, 2.26 * 10 ** 6, 5000, 10, 4187


def func(C_ent, m_ent, T_P):
    return (m_ent * C_ent) / (m_ent - ((kt * F * (T_P - Tr)) / (r - c1 * T_P)))


C0_values, C_exC0_values = [], []
m0_values, C_exm0_values = [], []
T0_values, C_exT0_values = [], []

while C0 < C1:
    C_ex = func(C0, m0, Tp)
    C0_values.append(C0)
    C_exC0_values.append(C_ex)
    C0 += d_C

while m0 < m1:
    C_ex = func(C_ent, m0, Tp)
    m0_values.append(m0)
    C_exm0_values.append(C_ex)
    m0 += d_m

while T0 < T1:
    C_ex = func(C_ent, m0, T0)
    T0_values.append(T0)
    C_exT0_values.append(C_ex)
    T0 += d_T


fig, axs = plt.subplots(3, 1, figsize=(9, 16))
axs[0].plot(C0_values, C_exC0_values)
axs[0].set_xlabel("C0")
axs[0].set_ylabel("C_ex")
axs[0].set_title("График зависимости C_ex от C0")
axs[0].grid(True)

axs[1].plot(m0_values, C_exm0_values)
axs[1].set_xlabel("m0")
axs[1].set_ylabel("m_ex")
axs[1].set_title("График зависимости C_ex от m0")
axs[1].grid(True)

axs[2].plot(T0_values, C_exT0_values)
axs[2].set_xlabel("T0")
axs[2].set_ylabel("T_ex")
axs[2].set_title("График зависимости C_ex от T0")
axs[2].grid(True)

plt.show()
