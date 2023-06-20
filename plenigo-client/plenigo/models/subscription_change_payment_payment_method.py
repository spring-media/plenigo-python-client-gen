from enum import Enum


class SubscriptionChangePaymentPaymentMethod(str, Enum):
    AMAZON_PAY = "AMAZON_PAY"
    BANK_ACCOUNT = "BANK_ACCOUNT"
    BILLING = "BILLING"
    CREDIT_CARD = "CREDIT_CARD"
    PAYPAL = "PAYPAL"

    def __str__(self) -> str:
        return str(self.value)
