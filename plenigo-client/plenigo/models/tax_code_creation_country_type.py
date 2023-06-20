from enum import Enum


class TaxCodeCreationCountryType(str, Enum):
    EU = "EU"
    EU_B2B = "EU_B2B"
    SINGLE_COUNTRY = "SINGLE_COUNTRY"
    WORLD = "WORLD"

    def __str__(self) -> str:
        return str(self.value)
