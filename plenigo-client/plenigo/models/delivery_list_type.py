from enum import Enum


class DeliveryListType(str, Enum):
    ANALOG = "ANALOG"
    DIGITAL = "DIGITAL"

    def __str__(self) -> str:
        return str(self.value)
