from enum import Enum


class OrderType(str, Enum):
    CROSS_SELLING = "CROSS_SELLING"
    ORDER = "ORDER"

    def __str__(self) -> str:
        return str(self.value)
