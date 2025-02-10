from enum import Enum


class ApiVoucherStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
