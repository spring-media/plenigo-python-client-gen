from enum import Enum


class CustomerSessionType(str, Enum):
    CUSTOMER_SESSION = "CUSTOMER_SESSION"

    def __str__(self) -> str:
        return str(self.value)
