from enum import Enum


class BonusReceiver(str, Enum):
    PAYER = "PAYER"
    RECIPIENT = "RECIPIENT"

    def __str__(self) -> str:
        return str(self.value)
