from enum import Enum


class BonusAvailability(str, Enum):
    AVAILABLE = "AVAILABLE"
    LIMITED = "LIMITED"
    SOLD_OUT = "SOLD_OUT"
    WHEN_AVAILABLE = "WHEN_AVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
