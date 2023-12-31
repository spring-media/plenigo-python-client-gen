from enum import Enum


class SubscriptionPrecursorReason(str, Enum):
    ACTION = "ACTION"
    CROSS_SELLING = "CROSS_SELLING"
    RULE = "RULE"
    RELATION_RULE = "RELATION_RULE"
    NEXT_BOOKING = "NEXT_BOOKING"
    NOW_WITH_INVOICING = "NOW_WITH_INVOICING"
    NOW = "NOW"
    VALUE_3 = ""
    AGE = "AGE"

    def __str__(self) -> str:
        return str(self.value)
