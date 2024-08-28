from enum import Enum


class ActivityReason(str, Enum):
    DATA_CHANGED = "DATA_CHANGED"
    DATA_CREATED = "DATA_CREATED"
    DATA_DELETED = "DATA_DELETED"

    def __str__(self) -> str:
        return str(self.value)
