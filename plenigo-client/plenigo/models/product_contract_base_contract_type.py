from enum import Enum


class ProductContractBaseContractType(str, Enum):
    CREDIT_BASED = "CREDIT_BASED"
    ISSUE_BASED = "ISSUE_BASED"
    TIME_BASED = "TIME_BASED"

    def __str__(self) -> str:
        return str(self.value)
