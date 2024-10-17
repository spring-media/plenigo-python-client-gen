from enum import Enum


class SubscriptionCancellationPeriodTimeSpan(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"
    NONE = "NONE"
    WEEK = "WEEK"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
