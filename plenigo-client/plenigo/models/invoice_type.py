from enum import Enum


class InvoiceType(str, Enum):
    CANCELLATION = "CANCELLATION"
    CANCELLATION_CORRECTION = "CANCELLATION_CORRECTION"
    CORRECTION = "CORRECTION"
    INVOICE = "INVOICE"

    def __str__(self) -> str:
        return str(self.value)
