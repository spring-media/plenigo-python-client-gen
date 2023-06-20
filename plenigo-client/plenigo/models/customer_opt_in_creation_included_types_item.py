from enum import Enum


class CustomerOptInCreationIncludedTypesItem(str, Enum):
    EMAIL = "EMAIL"
    MESSENGER = "MESSENGER"
    PHONE = "PHONE"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
