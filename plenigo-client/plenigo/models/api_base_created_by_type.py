from enum import Enum


class ApiBaseCreatedByType(str, Enum):
    API = "API"
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"
    IMPORTER = "IMPORTER"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
