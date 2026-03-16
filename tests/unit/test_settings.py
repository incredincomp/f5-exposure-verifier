"""Tests for application settings."""

import pytest

from app.config.settings import Settings, get_settings


def test_settings_defaults() -> None:
    """Settings should load with default values."""
    s = Settings()
    assert s.app_env == "development"
    assert s.app_port == 8000
    assert s.app_debug is False


def test_settings_env_override(monkeypatch: pytest.MonkeyPatch) -> None:
    """Settings should pick up environment variable overrides."""
    monkeypatch.setenv("APP_PORT", "9000")
    monkeypatch.setenv("APP_DEBUG", "true")
    s = Settings()
    assert s.app_port == 9000
    assert s.app_debug is True


def test_get_settings_returns_settings_instance() -> None:
    """get_settings() should return a Settings instance."""
    # Clear cache to get a fresh instance
    get_settings.cache_clear()
    s = get_settings()
    assert isinstance(s, Settings)
