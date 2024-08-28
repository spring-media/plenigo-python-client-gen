from enum import Enum


class SortTreeLeafType(str, Enum):
    OFFER = "OFFER"
    PRICE_ISSUE = "PRICE_ISSUE"
    PRODUCT_CONTRACT = "PRODUCT_CONTRACT"
    TEXT_MODULE = "TEXT_MODULE"

    def __str__(self) -> str:
        return str(self.value)
