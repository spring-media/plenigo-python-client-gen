from enum import Enum


class ApiCampaignBaseVoucherType(str, Enum):
    MULTI = "MULTI"
    SINGLE = "SINGLE"

    def __str__(self) -> str:
        return str(self.value)
