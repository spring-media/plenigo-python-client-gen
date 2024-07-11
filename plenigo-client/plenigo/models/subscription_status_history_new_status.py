from enum import Enum


class SubscriptionStatusHistoryNewStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"

    def __str__(self) -> str:
        return str(self.value)
