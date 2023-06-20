from enum import Enum


class CustomerStatusChangeStatus(str, Enum):
    ACTIVATED = "ACTIVATED"
    BLOCKED = "BLOCKED"
    DEACTIVATED = "DEACTIVATED"

    def __str__(self) -> str:
        return str(self.value)
