from typing import Any


class Powell:
    def __init__(self, func: Any, x1: float = 0, x2: float = 0, eps: float = 0.01, h0: float = 1) -> None:
        self.func = func
        self.x1 = x1
        self.x2 = x2
        self.eps = eps
        self.fx0 = func(x1, x2)
        self.h0 = h0

    def __calculate_direction(self) -> (float, float):
        x1, x2 = self.x1, self.x2
        fx1 = self.func(x1 + self.h0 * self.eps, x2)
        if self.func(x1, x2) > fx1:
            x1 += self.h0 * self.eps
        else:
            x1 -= self.h0 * self.eps
            fx1 = self.func(x1 + self.h0 * self.eps, x2)
        if fx1 > self.func(x1, x2 + self.h0 * self.eps):
            x2 += self.h0 * self.eps
        else:
            x2 -= self.h0 * self.eps
        return x1 - self.x1, x2 - self.x2

    def calculate(self) -> (float, float, int):
        del_x1, del_x2 = self.__calculate_direction()
        count, end = 0, 0
        while end != 3:
            fx1 = self.func(self.x1 + del_x1, self.x2 + del_x2)
            if self.fx0 > fx1:
                self.x1 += del_x1
                self.x2 += del_x2
                self.fx0 = fx1
                end = 0
            else:
                del_t1, del_t2 = self.__calculate_direction()
                if del_t1 == del_x1 and del_t2 == del_x2:
                    break
                del_x1, del_x2 = del_t1, del_t2
                end += 1
            count += 1
        return self.x1, self.x2, count
