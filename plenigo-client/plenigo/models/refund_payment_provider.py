from enum import Enum


class RefundPaymentProvider(str, Enum):
    AMAZON = "AMAZON"
    DATATRANS = "DATATRANS"
    PAYONE = "PAYONE"
    PAYPAL = "PAYPAL"
    SIX = "SIX"
    SOFORT = "SOFORT"
    STRIPE = "STRIPE"
    UNZER = "UNZER"
    WORLDPAY = "WORLDPAY"

    def __str__(self) -> str:
        return str(self.value)
