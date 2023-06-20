from enum import Enum


class CheckoutPreparationGiftOption(str, Enum):
    FORCE_GIFT_OPTION = "FORCE_GIFT_OPTION"
    HIDE_GIFT_OPTION = "HIDE_GIFT_OPTION"
    PRESELECT_GIFT_OPTION = "PRESELECT_GIFT_OPTION"
    SHOW_GIFT_OPTION = "SHOW_GIFT_OPTION"

    def __str__(self) -> str:
        return str(self.value)
