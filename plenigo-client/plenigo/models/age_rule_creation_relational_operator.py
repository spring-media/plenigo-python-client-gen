from enum import Enum


class AgeRuleCreationRelationalOperator(str, Enum):
    ABOVE = "ABOVE"
    BELOW = "BELOW"
    EQUAL = "EQUAL"

    def __str__(self) -> str:
        return str(self.value)
