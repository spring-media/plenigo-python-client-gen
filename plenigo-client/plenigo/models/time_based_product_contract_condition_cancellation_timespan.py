from enum import Enum


class TimeBasedProductContractConditionCancellationTimespan(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"
    NONE = "NONE"
    WEEK = "WEEK"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
