from enum import Enum


class IssueBasedProductContractConditionCancellationType(str, Enum):
    ISSUE_BASED = "ISSUE_BASED"
    ISSUE_BASED_REGULAR = "ISSUE_BASED_REGULAR"

    def __str__(self) -> str:
        return str(self.value)
