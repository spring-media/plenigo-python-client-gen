from enum import Enum


class DisputeStatusChangeStatus(str, Enum):
    LOST = "LOST"
    NEEDS_RESPONSE = "NEEDS_RESPONSE"
    UNDER_REVIEW = "UNDER_REVIEW"
    WARNING_CLOSED = "WARNING_CLOSED"
    WARNING_NEEDS_RESPONSE = "WARNING_NEEDS_RESPONSE"
    WARNING_UNDER_REVIEW = "WARNING_UNDER_REVIEW"
    WON = "WON"

    def __str__(self) -> str:
        return str(self.value)
