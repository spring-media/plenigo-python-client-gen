from enum import Enum


class CallbackLogEntryCallbackType(str, Enum):
    CANCELLATION = "CANCELLATION"
    CHANGE = "CHANGE"
    CONDITIONS_FULFILLED = "CONDITIONS_FULFILLED"
    CREATION = "CREATION"
    DELETION = "DELETION"
    ENDED = "ENDED"
    FINISHED = "FINISHED"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    PAYMENT_REVOKED = "PAYMENT_REVOKED"
    UNDO_CANCELLATION = "UNDO_CANCELLATION"

    def __str__(self) -> str:
        return str(self.value)
