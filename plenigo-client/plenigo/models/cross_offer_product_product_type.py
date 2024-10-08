from enum import Enum


class CrossOfferProductProductType(str, Enum):
    CROSS_CLIENT_SUBSCRIPTION_TIME_BASED = "CROSS_CLIENT_SUBSCRIPTION_TIME_BASED"
    SINGLE_PRODUCT = "SINGLE_PRODUCT"
    SINGLE_PRODUCT_CREDIT_BASED = "SINGLE_PRODUCT_CREDIT_BASED"
    SUBSCRIPTION_CREDIT_BASED = "SUBSCRIPTION_CREDIT_BASED"
    SUBSCRIPTION_CREDIT_TIME_BASED = "SUBSCRIPTION_CREDIT_TIME_BASED"
    SUBSCRIPTION_CREDIT_TRIGGER_BASED = "SUBSCRIPTION_CREDIT_TRIGGER_BASED"
    SUBSCRIPTION_ISSUE_BASED = "SUBSCRIPTION_ISSUE_BASED"
    SUBSCRIPTION_TIME_BASED = "SUBSCRIPTION_TIME_BASED"
    SUBSCRIPTION_TIME_CREDIT_BASED = "SUBSCRIPTION_TIME_CREDIT_BASED"
    VOUCHER_SALE = "VOUCHER_SALE"

    def __str__(self) -> str:
        return str(self.value)
