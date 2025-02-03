from enum import Enum


class ProductTagCreationCategory(str, Enum):
    ANALYTICS = "ANALYTICS"
    CUSTOM = "CUSTOM"
    FLOW = "FLOW"
    PAYWALL = "PAYWALL"
    RULE = "RULE"

    def __str__(self) -> str:
        return str(self.value)
