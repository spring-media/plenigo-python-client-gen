from enum import Enum


class ProductAnalogIvwRuleIvwType(str, Enum):
    ABONNEMENT = "ABONNEMENT"
    EINZELVERKAUF = "EINZELVERKAUF"
    STUDENTENABONNEMENT = "STUDENTENABONNEMENT"

    def __str__(self) -> str:
        return str(self.value)
