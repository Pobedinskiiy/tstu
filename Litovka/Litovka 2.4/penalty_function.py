from typing import Any

from visualization import Visualization

class PenaltyFunction(Visualization):
    def __init__(self, func: Any) -> None:
        super().__init__(func)
        pass

    def __external_penalty(self) -> float:
        pass

    def __internal_barrier(self) -> float:
        pass

    def calculate(self) -> (float, float):
        pass
