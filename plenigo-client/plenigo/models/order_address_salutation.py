from enum import Enum


class OrderAddressSalutation(str, Enum):
    DIVERSE = "DIVERSE"
    MR = "MR"
    MRS = "MRS"
    NONE = "NONE"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
