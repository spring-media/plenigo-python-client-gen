from enum import Enum


class SubscriptionPauseAtPauseType(str, Enum):
    PAYMENT_ONLY = "PAYMENT_ONLY"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
