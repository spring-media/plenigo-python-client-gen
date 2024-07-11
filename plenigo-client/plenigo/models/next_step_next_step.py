from enum import Enum


class NextStepNextStep(str, Enum):
    ADDITIONAL_DATA = "ADDITIONAL_DATA"
    RESET_PASSWORD = "RESET_PASSWORD"
    TWO_FACTOR = "TWO_FACTOR"

    def __str__(self) -> str:
        return str(self.value)
