"""Application settings via Pydantic Settings."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All configuration loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_env: str = Field(default="development")
    app_secret_key: str = Field(default="change-me-in-production")
    app_debug: bool = Field(default=False)
    app_log_level: str = Field(default="INFO")
    app_host: str = Field(default="0.0.0.0")
    app_port: int = Field(default=8000)

    # Database
    database_url: str = Field(
        default="postgresql+psycopg://verifier:verifier@localhost:5432/verifier"
    )

    # Redis (optional hook)
    redis_url: str | None = Field(default=None)

    # F5 BIG-IP
    f5_host: str | None = Field(default=None)
    f5_username: str | None = Field(default=None)
    f5_password: str | None = Field(default=None)
    f5_verify_tls: bool = Field(default=True)

    # CrowdStrike
    crowdstrike_client_id: str | None = Field(default=None)
    crowdstrike_client_secret: str | None = Field(default=None)
    crowdstrike_webhook_secret: str | None = Field(default=None)

    # API Auth
    api_key_header: str = Field(default="X-Api-Key")
    api_key: str = Field(default="change-me")

    # Callback
    callback_timeout_seconds: int = Field(default=10)
    callback_max_retries: int = Field(default=3)


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()
