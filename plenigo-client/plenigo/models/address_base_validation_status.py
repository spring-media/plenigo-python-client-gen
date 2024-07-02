from enum import Enum


class AddressBaseValidationStatus(str, Enum):
    INVALID = "INVALID"
    NONE = "NONE"
    OVERRIDDEN = "OVERRIDDEN"
    SUSPECT = "SUSPECT"
    VALID = "VALID"

    def __str__(self) -> str:
        return str(self.value)
