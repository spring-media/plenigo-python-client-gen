from enum import Enum


class SubscriptionStatusOldStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"

    def __str__(self) -> str:
        return str(self.value)
