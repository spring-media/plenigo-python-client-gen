from enum import Enum


class ProcessSettingsTokenType(str, Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"

    def __str__(self) -> str:
        return str(self.value)
