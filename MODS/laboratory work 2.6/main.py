import numpy as np
import warnings


def simplex(opt_type, A, B, C, D, M):
    (m, n) = A.shape
    basic_vars = []
    count = n
    R = np.eye(m)

    for i in range(m):
        basic_vars.append(count)
        if D[i] == 1:
            C = np.vstack((C, [[0]]))
            count += 1
        elif D[i] == 0:
            C = np.vstack((C, [[M if opt_type == 'min' else -M]]))
            count += 1
        elif D[i] == -1:
            C = np.vstack((C, [[0], [M if opt_type == 'min' else -M]]))
            R = repeatColumnNegative(R, count + 1 - n)
            count += 2

    A = np.hstack((A, R))
    st = np.vstack((np.hstack((-np.transpose(C), np.array([[0]]))), np.hstack((A, B))))
    z_optimal = C.T @ np.vstack((np.zeros((n, 1)), insertZeroToCol(B, count + 1 - n)))
    X = np.zeros((count, 1))

    if z_optimal != 0:
        for i in range(m):
            if D[i] in np.array([0, -1]):
                st[0, :] += [M if opt_type == 'min' else -M] * st[i + 1, :]

    while True:
        w = np.amax(st[0, :-1]) if opt_type == 'min' else np.amin(st[0, :-1])
        iw = np.argmax(st[0, :-1]) if opt_type == 'min' else np.argmin(st[0, :-1])

        if (w <= 0 and opt_type == 'min') or (w >= 0 and opt_type == 'max'):
            break

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            T = st[1:, -1] / st[1:, iw]

        R = np.logical_and(T != np.inf, T > 0)
        k, ik = minWithMask(T, R)

        cz = st[[0], :]

        pivot = st[ik + 1, iw]
        prow = st[ik + 1, :] / pivot

        st -= st[:, [iw]] * prow
        st[ik + 1, :] = prow

        basic_vars[ik] = iw
        basic = st[:, -1]

        for k in range(np.size(basic_vars) - 1):
            X[basic_vars[k]] = basic[k + 1]

        z_optimal = cz[0, -1] - cz[[0], :count] @ X
        st[0, -1] = z_optimal

    return X, z_optimal[0, 0]


def minWithMask(x, mask):
    masked_x = np.where(mask == 1, x, np.inf)
    return np.min(masked_x), np.argmin(masked_x)


def repeatColumnNegative(mat, h):
    return np.hstack((mat[:, :h - 1], -mat[:, [h - 1]], mat[:, h - 1:np.size(mat)]))


def insertZeroToCol(col, h):
    return np.vstack((col[:h - 1, [0]], np.array([[0]]), col[h - 1:np.size(col), [0]]))


solution, optimal_value = simplex("min",
                                  np.array([[2.4, 5.2],
                                            [1, 0],
                                            [34, 21.6]]),
                                  np.array([[48.1], [5], [375.3]]),
                                  np.array([[-23.1], [38.6]]),
                                  np.array([[-1], [1], [1]]),
                                  100)

print(f"Оптимальное решение: x1 = {solution[0, 0]:.4f}, x2 = {solution[1, 0]:.4f}")
print(f"Минимальное значение Z = {optimal_value:.4f}")
