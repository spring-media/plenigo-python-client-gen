from enum import Enum


class SubscriptionSubscriptionType(str, Enum):
    CREDIT_BASED = "CREDIT_BASED"
    CREDIT_TIME_BASED = "CREDIT_TIME_BASED"
    CREDIT_TRIGGER_BASED = "CREDIT_TRIGGER_BASED"
    CROSS_COMPANY_TIME_BASED = "CROSS_COMPANY_TIME_BASED"
    ISSUE_BASED = "ISSUE_BASED"
    TIME_BASED = "TIME_BASED"
    TIME_CREDIT_BASED = "TIME_CREDIT_BASED"
    VOUCHER_CREDIT_BASED = "VOUCHER_CREDIT_BASED"
    VOUCHER_CREDIT_TIME_BASED = "VOUCHER_CREDIT_TIME_BASED"
    VOUCHER_CREDIT_TRIGGER_BASED = "VOUCHER_CREDIT_TRIGGER_BASED"
    VOUCHER_ISSUE_BASED = "VOUCHER_ISSUE_BASED"
    VOUCHER_TIME_BASED = "VOUCHER_TIME_BASED"
    VOUCHER_TIME_CREDIT_BASED = "VOUCHER_TIME_CREDIT_BASED"

    def __str__(self) -> str:
        return str(self.value)