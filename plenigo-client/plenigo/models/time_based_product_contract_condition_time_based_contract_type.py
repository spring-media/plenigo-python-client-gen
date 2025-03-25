from enum import Enum


class TimeBasedProductContractConditionTimeBasedContractType(str, Enum):
    MULTIUSER_CORPORATE = "MULTIUSER_CORPORATE"
    MULTIUSER_FAMILY = "MULTIUSER_FAMILY"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
