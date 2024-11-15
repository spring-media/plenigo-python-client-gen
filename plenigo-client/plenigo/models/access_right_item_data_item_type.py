from enum import Enum


class AccessRightItemDataItemType(str, Enum):
    EXTERNAL = "EXTERNAL"
    SINGLE_PRODUCT = "SINGLE_PRODUCT"
    SUBSCRIPTION_ITEM = "SUBSCRIPTION_ITEM"

    def __str__(self) -> str:
        return str(self.value)
