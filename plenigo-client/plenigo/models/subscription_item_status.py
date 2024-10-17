from enum import Enum


class SubscriptionItemStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
