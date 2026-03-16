"""Authentication configuration stub."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthConfig:
    """Holds authentication configuration values."""

    api_key: str
    api_key_header: str = "X-Api-Key"
