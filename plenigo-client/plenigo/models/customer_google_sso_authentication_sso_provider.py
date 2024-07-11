from enum import Enum


class CustomerGoogleSsoAuthenticationSsoProvider(str, Enum):
    GOOGLE = "GOOGLE"

    def __str__(self) -> str:
        return str(self.value)
