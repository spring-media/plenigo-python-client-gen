from enum import Enum


class GetCustomerMarkCustomerMark(str, Enum):
    WBZ = "WBZ"

    def __str__(self) -> str:
        return str(self.value)
