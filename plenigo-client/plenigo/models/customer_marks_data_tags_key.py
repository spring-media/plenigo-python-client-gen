from enum import Enum


class CustomerMarksDataTagsKey(str, Enum):
    WBZ = "WBZ"

    def __str__(self) -> str:
        return str(self.value)
