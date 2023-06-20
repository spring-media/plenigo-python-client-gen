from enum import Enum


class GetActiveSubscriptionsInterval(str, Enum):
    DAY = "DAY"
    HOUR = "HOUR"
    MONTH = "MONTH"
    WEEK = "WEEK"

    def __str__(self) -> str:
        return str(self.value)
