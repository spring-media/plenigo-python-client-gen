from enum import Enum


class SearchCrossClientSubscriptionDeliveryDatesSort(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
