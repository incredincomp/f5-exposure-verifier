"""Time utilities."""

from datetime import UTC, datetime


def utcnow() -> datetime:
    """Return the current UTC datetime (timezone-aware)."""
    return datetime.now(tz=UTC)


def iso_utcnow() -> str:
    """Return the current UTC datetime as an ISO 8601 string."""
    return utcnow().isoformat()
