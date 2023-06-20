from enum import Enum


class DownloadFileFileType(str, Enum):
    CSV = "CSV"
    PDF = "PDF"
    ZIP = "ZIP"

    def __str__(self) -> str:
        return str(self.value)
