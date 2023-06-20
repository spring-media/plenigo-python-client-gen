from enum import Enum


class SearchDownloadsDownloadType(str, Enum):
    ANALOG_INVOICE_LIST = "ANALOG_INVOICE_LIST"
    DELIVERY_LIST = "DELIVERY_LIST"
    DELIVERY_NOTE_LIST = "DELIVERY_NOTE_LIST"

    def __str__(self) -> str:
        return str(self.value)
