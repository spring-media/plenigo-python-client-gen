""" A client library for accessing plenigo API v3 """
from enum import StrEnum

from .client import AuthenticatedClient, Client


class Environment(StrEnum):
    STAGING = STAGE = "https://api.plenigo-stage.com/api/v3.0"
    PRODUCTION = PROD = LIVE = "https://api.plenigo.com/api/v3.0"


__all__ = (
    "AuthenticatedClient",
    "Client",
)
