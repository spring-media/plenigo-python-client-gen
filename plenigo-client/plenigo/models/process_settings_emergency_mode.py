from enum import Enum


class ProcessSettingsEmergencyMode(str, Enum):
    CONTRACT_COMPANY_MODE = "CONTRACT_COMPANY_MODE"
    NONE = "NONE"
    PLENIGO_MODE = "PLENIGO_MODE"

    def __str__(self) -> str:
        return str(self.value)
