from enum import Enum


class CreditUploadItemType(str, Enum):
    EXTERNAL_UPLOAD = "EXTERNAL_UPLOAD"
    SINGLE_PRODUCT = "SINGLE_PRODUCT"
    SUBSCRIPTION_ITEM = "SUBSCRIPTION_ITEM"

    def __str__(self) -> str:
        return str(self.value)
