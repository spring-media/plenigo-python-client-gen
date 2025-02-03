from enum import Enum


class AccessRightItemDataItemType(str, Enum):
    APP_STORE_PRODUCT = "APP_STORE_PRODUCT"
    APP_STORE_SUBSCRIPTION = "APP_STORE_SUBSCRIPTION"
    CORPORATE_ACCOUNT = "CORPORATE_ACCOUNT"
    EXTERNAL = "EXTERNAL"
    SINGLE_PRODUCT = "SINGLE_PRODUCT"
    SUBSCRIPTION = "SUBSCRIPTION"
    SUBSCRIPTION_ITEM = "SUBSCRIPTION_ITEM"

    def __str__(self) -> str:
        return str(self.value)
