from enum import Enum


class ApiMultiVoucherChangedByType(str, Enum):
    API = "API"
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
