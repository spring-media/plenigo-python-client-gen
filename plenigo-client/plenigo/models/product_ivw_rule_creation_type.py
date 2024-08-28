from enum import Enum


class ProductIvwRuleCreationType(str, Enum):
    ANALOG = "ANALOG"
    DIGITAL = "DIGITAL"

    def __str__(self) -> str:
        return str(self.value)
