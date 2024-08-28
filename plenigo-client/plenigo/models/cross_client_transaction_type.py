from enum import Enum


class CrossClientTransactionType(str, Enum):
    LOSS = "LOSS"
    PAYMENT = "PAYMENT"
    REFUND = "REFUND"

    def __str__(self) -> str:
        return str(self.value)
