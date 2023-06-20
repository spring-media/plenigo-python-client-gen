from enum import Enum


class SubscriptionSuccessorReason(str, Enum):
    ACTION = "ACTION"
    CROSS_SELLING = "CROSS_SELLING"
    RULE = "RULE"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
