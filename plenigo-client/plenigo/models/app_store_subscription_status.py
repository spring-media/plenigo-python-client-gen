from enum import Enum


class AppStoreSubscriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    IGNORED = "IGNORED"
    INACTIVE = "INACTIVE"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
