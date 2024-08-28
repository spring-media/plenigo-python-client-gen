from enum import Enum


class TransactionPaymentStatus(str, Enum):
    FAILURE = "FAILURE"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
