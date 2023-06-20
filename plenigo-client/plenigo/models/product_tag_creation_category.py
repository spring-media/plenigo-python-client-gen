from enum import Enum


class ProductTagCreationCategory(str, Enum):
    ANALYTICS = "ANALYTICS"
    CUSTOM = "CUSTOM"
    FLOW = "FLOW"
    RULE = "RULE"

    def __str__(self) -> str:
        return str(self.value)
