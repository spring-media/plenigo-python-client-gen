from enum import Enum


class GetVouchersChannelsChannelIdVouchersVoucherStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
