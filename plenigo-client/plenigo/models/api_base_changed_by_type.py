from enum import Enum


class ApiBaseChangedByType(str, Enum):
    API = "API"
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"
    IMPORTER = "IMPORTER"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
