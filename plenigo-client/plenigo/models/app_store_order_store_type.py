from enum import Enum


class AppStoreOrderStoreType(str, Enum):
    AMAZON = "AMAZON"
    APPSTORE = "APPSTORE"
    PLAYSTORE = "PLAYSTORE"

    def __str__(self) -> str:
        return str(self.value)
