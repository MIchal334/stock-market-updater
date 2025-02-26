from enum import Enum


class Action(Enum):
    SELL = "SELL"
    BUY = "BUY"

    @classmethod
    def of(cls, action_str: str):
        try:
            return cls(action_str)
        except ValueError:
            raise ValueError(f"Invalid action: {action_str}")

    def apply(self, a: int, b: int) -> int:
        if self == Action.SELL:
            result = a - b
            return max(result, 0)
        else:
            return a + b
