from enum import Enum


class InvoiceAddressSalutation(str, Enum):
    DIVERSE = "DIVERSE"
    MR = "MR"
    MRS = "MRS"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
