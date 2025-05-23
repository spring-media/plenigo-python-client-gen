from enum import Enum


class ApiCampaignBaseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    CREATING = "CREATING"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    UPDATING = "UPDATING"

    def __str__(self) -> str:
        return str(self.value)
