from enum import Enum


class MultiuserConditionsMultiuserPaymentVariant(str, Enum):
    COMPLETE = "COMPLETE"
    USER_BASED = "USER_BASED"
    USER_BASED_GRADUATED = "USER_BASED_GRADUATED"

    def __str__(self) -> str:
        return str(self.value)
