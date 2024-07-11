from enum import Enum


class SubscriptionManagedBy(str, Enum):
    EXTERNAL = "EXTERNAL"
    PLENIGO = "PLENIGO"
    WBZ = "WBZ"

    def __str__(self) -> str:
        return str(self.value)
