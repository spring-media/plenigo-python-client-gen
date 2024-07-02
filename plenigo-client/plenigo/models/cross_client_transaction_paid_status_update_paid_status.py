from enum import Enum


class CrossClientTransactionPaidStatusUpdatePaidStatus(str, Enum):
    OPEN = "OPEN"
    PAID = "PAID"

    def __str__(self) -> str:
        return str(self.value)
