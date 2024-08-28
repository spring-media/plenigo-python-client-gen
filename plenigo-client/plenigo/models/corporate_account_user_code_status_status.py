from enum import Enum


class CorporateAccountUserCodeStatusStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"

    def __str__(self) -> str:
        return str(self.value)
