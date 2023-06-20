from enum import Enum


class RefundPaymentProvider(str, Enum):
    AMAZON = "AMAZON"
    APPLE = "APPLE"
    DATATRANS = "DATATRANS"
    GOOGLE = "GOOGLE"
    PAYONE = "PAYONE"
    PAYPAL = "PAYPAL"
    STRIPE = "STRIPE"
    WIRECARD_LEGACY = "WIRECARD_LEGACY"

    def __str__(self) -> str:
        return str(self.value)
