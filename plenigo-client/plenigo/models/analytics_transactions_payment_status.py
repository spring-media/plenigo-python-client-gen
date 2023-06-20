from enum import Enum


class AnalyticsTransactionsPaymentStatus(str, Enum):
    FAILURE = "FAILURE"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
