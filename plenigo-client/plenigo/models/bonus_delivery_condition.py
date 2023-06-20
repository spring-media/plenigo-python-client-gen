from enum import Enum


class BonusDeliveryCondition(str, Enum):
    AFTER_PAYMENT = "AFTER_PAYMENT"
    IMMEDIATELY = "IMMEDIATELY"

    def __str__(self) -> str:
        return str(self.value)
