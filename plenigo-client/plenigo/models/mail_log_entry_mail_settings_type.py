from enum import Enum


class MailLogEntryMailSettingsType(str, Enum):
    DELEGATION = "DELEGATION"
    EXTERNAL = "EXTERNAL"
    INTERN = "INTERN"

    def __str__(self) -> str:
        return str(self.value)
