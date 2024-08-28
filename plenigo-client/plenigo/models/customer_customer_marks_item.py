from enum import Enum


class CustomerCustomerMarksItem(str, Enum):
    WBZ = "WBZ"

    def __str__(self) -> str:
        return str(self.value)
