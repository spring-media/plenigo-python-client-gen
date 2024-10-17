from enum import Enum


class SubscriptionSuccessorReason(str, Enum):
    ACTION = "ACTION"
    AGE = "AGE"
    CANCELLATION = "CANCELLATION"
    CROSS_SELLING = "CROSS_SELLING"
    PRICE_PERIOD = "PRICE_PERIOD"
    PRODUCT_EOL = "PRODUCT_EOL"
    RELATION_RULE = "RELATION_RULE"

    def __str__(self) -> str:
        return str(self.value)
