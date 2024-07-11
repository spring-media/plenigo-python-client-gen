from enum import Enum


class UpdateAddonTrackingDataStatus(str, Enum):
    CANCELLED = "CANCELLED"
    CONDITIONS_FULFILLED = "CONDITIONS_FULFILLED"
    DELIVERED = "DELIVERED"
    IN_DELIVERY = "IN_DELIVERY"
    OPEN = "OPEN"
    READY_FOR_DELIVERY = "READY_FOR_DELIVERY"

    def __str__(self) -> str:
        return str(self.value)
