from enum import Enum


class DownloadDownloadType(str, Enum):
    ANALOG_INVOICE_LIST = "ANALOG_INVOICE_LIST"
    DELIVERY_LIST = "DELIVERY_LIST"
    DELIVERY_NOTE_LIST = "DELIVERY_NOTE_LIST"
    IVW_LIST = "IVW_LIST"

    def __str__(self) -> str:
        return str(self.value)
