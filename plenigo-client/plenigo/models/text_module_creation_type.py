from enum import Enum


class TextModuleCreationType(str, Enum):
    HTML_TEXT = "HTML_TEXT"
    LINK = "LINK"
    PLAIN_TEXT = "PLAIN_TEXT"

    def __str__(self) -> str:
        return str(self.value)
