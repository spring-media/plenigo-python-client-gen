from enum import Enum


class AddressBaseValidationStatus(str, Enum):
    INVALID = "INVALID"
    NONE = "NONE"
    SUSPECT = "SUSPECT"
    VALID = "VALID"

    def __str__(self) -> str:
        return str(self.value)
