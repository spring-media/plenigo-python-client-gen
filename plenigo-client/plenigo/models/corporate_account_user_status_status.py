from enum import Enum


class CorporateAccountUserStatusStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"

    def __str__(self) -> str:
        return str(self.value)
