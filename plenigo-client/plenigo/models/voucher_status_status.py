from enum import Enum


class VoucherStatusStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
