from enum import Enum


class CreditCardChangeCardType(str, Enum):
    AMERICAN_EXPRESS = "AMERICAN_EXPRESS"
    DINERS_CLUB = "DINERS_CLUB"
    DISCOVER = "DISCOVER"
    JCB = "JCB"
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"

    def __str__(self) -> str:
        return str(self.value)
