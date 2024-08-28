from enum import Enum


class OfferTranslationImageImageType(str, Enum):
    PRODUCT_CHECKOUT = "PRODUCT_CHECKOUT"
    PRODUCT_PRESENTATION = "PRODUCT_PRESENTATION"

    def __str__(self) -> str:
        return str(self.value)
