from enum import Enum


class CrossOfferManagedBy(str, Enum):
    EXTERNAL = "EXTERNAL"
    PLENIGO = "PLENIGO"
    WBZ = "WBZ"

    def __str__(self) -> str:
        return str(self.value)
