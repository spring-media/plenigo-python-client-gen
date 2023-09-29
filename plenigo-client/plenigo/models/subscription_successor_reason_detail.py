from enum import Enum


class SubscriptionSuccessorReasonDetail(str, Enum):
    ACTION_PERIOD = "ACTION_PERIOD"
    AGE = "AGE"
    CROSS_SELLING = "CROSS_SELLING"
    PRICE_PERIOD = "PRICE_PERIOD"
    NEXT_BOOKING = "NEXT_BOOKING"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
