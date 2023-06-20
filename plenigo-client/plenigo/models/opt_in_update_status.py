from enum import Enum


class OptInUpdateStatus(str, Enum):
    DOUBLE_OPT_IN = "DOUBLE_OPT_IN"
    NONE = "NONE"
    OBJECTION_OPT_IN = "OBJECTION_OPT_IN"
    REVOKED_OPT_IN = "REVOKED_OPT_IN"
    SINGLE_OPT_IN = "SINGLE_OPT_IN"

    def __str__(self) -> str:
        return str(self.value)
