from enum import Enum


class ActivityJsonObjectType(str, Enum):
    ACCESS_RIGHT_ITEM = "ACCESS_RIGHT_ITEM"
    AMAZON_PAY = "AMAZON_PAY"
    BANK_ACCOUNT = "BANK_ACCOUNT"
    CREDIT_CARD = "CREDIT_CARD"
    CUSTOMER = "CUSTOMER"
    DELIVERY_ADDRESS = "DELIVERY_ADDRESS"
    INVOICE = "INVOICE"
    INVOICE_ADDRESS = "INVOICE_ADDRESS"
    ORDER = "ORDER"
    PAYPAL = "PAYPAL"
    SUBSCRIPTION = "SUBSCRIPTION"

    def __str__(self) -> str:
        return str(self.value)
