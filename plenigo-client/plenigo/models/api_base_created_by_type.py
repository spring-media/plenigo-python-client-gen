from enum import Enum


class ApiBaseCreatedByType(str, Enum):
    API = "API"
    CUSTOMER = "CUSTOMER"
    IMPORTER = "IMPORTER"
    MERCHANT = "MERCHANT"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)