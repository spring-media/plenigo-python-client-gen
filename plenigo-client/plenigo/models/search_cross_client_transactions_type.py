from enum import Enum


class SearchCrossClientTransactionsType(str, Enum):
    LOSS = "LOSS"
    PAYMENT = "PAYMENT"
    REFUND = "REFUND"

    def __str__(self) -> str:
        return str(self.value)
