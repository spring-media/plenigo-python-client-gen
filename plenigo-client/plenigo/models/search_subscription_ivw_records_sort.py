from enum import Enum


class SearchSubscriptionIvwRecordsSort(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
