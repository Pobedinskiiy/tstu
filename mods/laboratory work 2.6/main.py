import numpy as np

def simplex(opt_type, A, B, C, D, M):
    (m, n) = A.shape
    basic_vars = []
    count = n
    valid_ratios_mask = np.eye(m)

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
            valid_ratios_mask = repeatColumnNegative(valid_ratios_mask, count - n)
            count += 2

    tableau = np.vstack((np.hstack((-C.T, np.array([[0]]))), np.hstack((np.hstack((A, valid_ratios_mask)), B))))
    decision = np.zeros((count, 1))

    if C.T @ np.vstack((np.zeros((n, 1)), insertZeroToCol(B, count - n))) != 0:
        for i in range(m):
            if D[i] in np.array([0, -1]):
                tableau[0, :] += [M if opt_type == 'min' else -M] * tableau[i + 1, :]

    while True:
        w = np.amax(tableau[0, :-1]) if opt_type == 'min' else np.amin(tableau[0, :-1])
        iw = np.argmax(tableau[0, :-1]) if opt_type == 'min' else np.argmin(tableau[0, :-1])

        if (w <= 0 and opt_type == 'min') or (w >= 0 and opt_type == 'max'):
            break

        with np.errstate(divide='ignore', invalid='ignore'):
            ratios = np.divide(tableau[1:, -1], tableau[1:, iw])

        valid_ratios_mask = (ratios > 0) & (~np.isinf(ratios))
        ik = np.argmin(np.where(valid_ratios_mask == 1, ratios, np.inf))

        cz = tableau[[0], :]

        pivot = tableau[ik + 1, iw]
        prow = tableau[ik + 1, :] / pivot

        tableau -= tableau[:, [iw]] * prow
        tableau[ik + 1, :] = prow

        basic_vars[ik] = iw

        for k in range(np.size(basic_vars) - 1):
            decision[basic_vars[k]] = tableau[:, -1][k + 1]

        tableau[0, -1] = cz[0, -1] - cz[[0], :count] @ decision

    return decision, tableau[0, -1]


def repeatColumnNegative(mat, h):
    return np.hstack((mat[:, :h], -mat[:, [h]], mat[:, h:np.size(mat)]))


def insertZeroToCol(col, h):
    return np.vstack((col[:h, [0]], np.array([[0]]), col[h:np.size(col), [0]]))


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