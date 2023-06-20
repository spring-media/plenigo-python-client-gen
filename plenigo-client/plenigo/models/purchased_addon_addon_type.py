from enum import Enum


class PurchasedAddonAddonType(str, Enum):
    BONUS = "BONUS"

    def __str__(self) -> str:
        return str(self.value)
