from enum import Enum


class CrossClientTransactionPaidStatus(str, Enum):
    OPEN = "OPEN"
    PAID = "PAID"

    def __str__(self) -> str:
        return str(self.value)
