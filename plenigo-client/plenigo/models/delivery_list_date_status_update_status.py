from enum import Enum


class DeliveryListDateStatusUpdateStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    SOLD_OUT = "SOLD_OUT"

    def __str__(self) -> str:
        return str(self.value)
