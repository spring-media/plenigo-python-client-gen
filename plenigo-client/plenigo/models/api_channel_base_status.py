from enum import Enum


class ApiChannelBaseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    UPDATING = "UPDATING"

    def __str__(self) -> str:
        return str(self.value)
