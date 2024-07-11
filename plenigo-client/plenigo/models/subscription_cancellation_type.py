from enum import Enum


class SubscriptionCancellationType(str, Enum):
    CREDIT_BASED = "CREDIT_BASED"
    ISSUE_BASED = "ISSUE_BASED"
    ISSUE_BASED_REGULAR = "ISSUE_BASED_REGULAR"
    TIME_BASED = "TIME_BASED"

    def __str__(self) -> str:
        return str(self.value)
