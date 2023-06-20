from enum import Enum


class CheckoutAddressSettingsTakeOver(str, Enum):
    DELIVERY_ADDRESS_DEFAULT = "DELIVERY_ADDRESS_DEFAULT"
    INVOICE_ADDRESS_DEFAULT = "INVOICE_ADDRESS_DEFAULT"
    NO_ADDRESS_DEFAULT = "NO_ADDRESS_DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
