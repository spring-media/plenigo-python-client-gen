from enum import Enum


class SearchRefundsStatus(str, Enum):
    CLOSED = "CLOSED"
    IGNORED = "IGNORED"
    OPEN = "OPEN"
    PROCESSING = "PROCESSING"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
