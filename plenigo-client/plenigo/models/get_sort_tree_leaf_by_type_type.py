from enum import Enum


class GetSortTreeLeafByTypeType(str, Enum):
    OFFER = "OFFER"
    PRICE_ISSUE = "PRICE_ISSUE"

    def __str__(self) -> str:
        return str(self.value)
