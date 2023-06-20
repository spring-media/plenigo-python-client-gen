from enum import Enum


class RefundStatusChangeStatus(str, Enum):
    CLOSED = "CLOSED"
    IGNORED = "IGNORED"
    OPEN = "OPEN"
    PROCESSING = "PROCESSING"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
