from enum import Enum


class CrossSellingAccessStart(str, Enum):
    END_OF_TERM = "END_OF_TERM"
    NEXT_BOOKING = "NEXT_BOOKING"
    NOW = "NOW"

    def __str__(self) -> str:
        return str(self.value)
