from enum import Enum


class SubscriptionChangeAddressAddressType(str, Enum):
    DELIVERY = "DELIVERY"
    INVOICE = "INVOICE"

    def __str__(self) -> str:
        return str(self.value)
