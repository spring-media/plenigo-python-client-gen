from enum import Enum


class CrossSellingAccessStart(str, Enum):
    END_OF_TERM = "END_OF_TERM"
    LAST_BOOKING = "LAST_BOOKING"
    NEXT_BOOKING = "NEXT_BOOKING"
    NOW = "NOW"
    NOW_WITH_INVOICING = "NOW_WITH_INVOICING"

    def __str__(self) -> str:
        return str(self.value)
