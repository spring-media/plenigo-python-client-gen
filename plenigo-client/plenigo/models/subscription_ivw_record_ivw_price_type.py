from enum import Enum


class SubscriptionIvwRecordIvwPriceType(str, Enum):
    ISSUE_BASED = "ISSUE_BASED"
    PERIOD_BASED = "PERIOD_BASED"

    def __str__(self) -> str:
        return str(self.value)
