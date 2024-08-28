from enum import Enum


class SubscriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    IGNORED = "IGNORED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
