from enum import Enum


class ArchiveSettingsArchiveType(str, Enum):
    BLOCK = "BLOCK"
    DEFAULT = "DEFAULT"
    SUCCESSOR = "SUCCESSOR"

    def __str__(self) -> str:
        return str(self.value)
