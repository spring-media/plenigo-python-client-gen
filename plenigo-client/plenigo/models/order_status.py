from enum import Enum


class OrderStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    DONE = "DONE"

    def __str__(self) -> str:
        return str(self.value)
