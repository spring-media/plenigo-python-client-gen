from enum import Enum


class CorporateAccountUserStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"

    def __str__(self) -> str:
        return str(self.value)
