from enum import Enum


class AddressCreationType(str, Enum):
    DELIVERY = "DELIVERY"
    INVOICE = "INVOICE"

    def __str__(self) -> str:
        return str(self.value)
