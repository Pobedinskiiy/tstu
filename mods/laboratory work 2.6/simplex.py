import numpy as np
from enum import Enum

from visualization import Visualization


class OptType(Enum):
    MIN = "min"
    MAX = "max"


class Simplex(Visualization):
    def __init__(self, opt_type: OptType, a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray, m: float) -> None:
        super().__init__()
        self.opt_type = opt_type
        self.a, self.b, self.c, self.d, self.m = a, b, c, d, m

    def calculate(self) -> (np.ndarray, np.ndarray):
        (l, n) = self.a.shape
        basic_vars = []
        count = n
        valid_ratios_mask = np.eye(l)

        for i in range(l):
            basic_vars.append(count)
            if self.d[i] == 1:
                self.c = np.vstack((self.c, [[0]]))
                count += 1
            elif self.d[i] == 0:
                self.c = np.vstack((self.c, [[self.m if self.opt_type == OptType.MIN else -self.m]]))
                count += 1
            elif self.d[i] == -1:
                c = np.vstack((self.c, [[0], [self.m if self.opt_type == OptType.MIN else -self.m]]))
                valid_ratios_mask = self.__repeat_column_negative(valid_ratios_mask, count - n)
                count += 2

        tableau = np.vstack((np.hstack((-self.c.T, np.array([[0]]))), np.hstack((np.hstack((self.a, valid_ratios_mask)), self.b))))
        decision = np.zeros((count, 1))

        if self.c.T @ np.vstack((np.zeros((n, 1)), self.__insert_zero_to_col(self.b, count - n))) != 0:
            for i in range(l):
                if self.d[i] in np.array([0, -1]):
                    tableau[0, :] += [self.m if self.opt_type == OptType.MIN else -self.m] * tableau[i + 1, :]

        while True:
            w = np.amax(tableau[0, :-1]) if self.opt_type == OptType.MIN else np.amin(tableau[0, :-1])
            iw = np.argmax(tableau[0, :-1]) if self.opt_type == OptType.MIN else np.argmin(tableau[0, :-1])

            if (w <= 0 and self.opt_type == OptType.MIN) or (w >= 0 and self.opt_type == OptType.MAX):
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

    @staticmethod
    def __repeat_column_negative(mat, h) -> np.ndarray:
        return np.hstack((mat[:, :h], -mat[:, [h]], mat[:, h:np.size(mat)]))

    @staticmethod
    def __insert_zero_to_col(col, h) -> np.ndarray:
        return np.vstack((col[:h, [0]], np.array([[0]]), col[h:np.size(col), [0]]))
