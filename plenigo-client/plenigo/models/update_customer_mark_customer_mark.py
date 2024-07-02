from enum import Enum


class UpdateCustomerMarkCustomerMark(str, Enum):
    WBZ = "WBZ"

    def __str__(self) -> str:
        return str(self.value)
