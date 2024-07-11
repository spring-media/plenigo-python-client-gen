from enum import Enum


class RelationRuleBaseIdentityCheckType(str, Enum):
    ADULT = "ADULT"
    DEFAULT = "DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
