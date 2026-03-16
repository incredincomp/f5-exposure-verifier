"""Time utilities."""

from datetime import datetime, timezone


def utcnow() -> datetime:
    """Return the current UTC datetime (timezone-aware)."""
    return datetime.now(tz=timezone.utc)


def iso_utcnow() -> str:
    """Return the current UTC datetime as an ISO 8601 string."""
    return utcnow().isoformat()
