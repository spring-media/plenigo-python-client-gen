from enum import Enum


class OrderImportManagedBy(str, Enum):
    EXTERNAL = "EXTERNAL"
    WBZ = "WBZ"

    def __str__(self) -> str:
        return str(self.value)
