from enum import Enum


class InvoicePaymentStatusChangeStatus(str, Enum):
    NOT_PAID = "NOT_PAID"
    PAID = "PAID"

    def __str__(self) -> str:
        return str(self.value)
