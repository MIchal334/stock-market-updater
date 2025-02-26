from enum import Enum


class Action(Enum):
    SELL = "sell"
    BUY = "buy"

    @classmethod
    def of(cls, action_str: str):
        try:
            return cls(action_str.lower())
        except ValueError:
            raise ValueError(f"Invalid action: {action_str}")

    def apply(self, a: int, b: int) -> int:
        return a + b if self == Action.SELL else a - b
