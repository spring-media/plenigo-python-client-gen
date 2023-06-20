from enum import Enum


class AnalyticsPaymentPeriodsFailureReason(str, Enum):
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
