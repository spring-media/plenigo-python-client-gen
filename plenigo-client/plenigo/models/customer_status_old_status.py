from enum import Enum


class CustomerStatusOldStatus(str, Enum):
    ACTIVATED = "ACTIVATED"
    BLOCKED = "BLOCKED"
    DEACTIVATED = "DEACTIVATED"

    def __str__(self) -> str:
        return str(self.value)
