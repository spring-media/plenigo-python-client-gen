from enum import Enum


class ApiVoucherChangedByType(str, Enum):
    API = "API"
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
