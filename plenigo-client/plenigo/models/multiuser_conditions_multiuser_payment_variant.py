from enum import Enum


class MultiuserConditionsMultiuserPaymentVariant(str, Enum):
    COMPLETE = "COMPLETE"
    FULL_PACKAGE = "FULL_PACKAGE"
    USER_BASED = "USER_BASED"
    USER_BASED_GRADUATED = "USER_BASED_GRADUATED"

    def __str__(self) -> str:
        return str(self.value)
