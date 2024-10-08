from enum import Enum


class CrossOfferPdfTemplateUsage(str, Enum):
    B2B = "B2B"
    B2C = "B2C"
    EVENT_B2B = "EVENT_B2B"
    EVENT_B2C = "EVENT_B2C"

    def __str__(self) -> str:
        return str(self.value)
