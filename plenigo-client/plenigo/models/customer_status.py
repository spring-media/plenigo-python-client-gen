from enum import Enum


class CustomerStatus(str, Enum):
    ACTIVATED = "ACTIVATED"
    BLOCKED = "BLOCKED"
    DEACTIVATED = "DEACTIVATED"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
