from enum import Enum


class PaymentMethodsBlockedPaymentMethodsItem(str, Enum):
    AMAZON_PAY = "AMAZON_PAY"
    APPLE_PAY = "APPLE_PAY"
    BANK_ACCOUNT = "BANK_ACCOUNT"
    BILLING = "BILLING"
    CREDIT_CARD = "CREDIT_CARD"
    GOOGLE_PAY = "GOOGLE_PAY"
    IDEAL = "IDEAL"
    PAYPAL = "PAYPAL"
    POSTFINANCE = "POSTFINANCE"
    SOFORT = "SOFORT"
    TWINT = "TWINT"

    def __str__(self) -> str:
        return str(self.value)
