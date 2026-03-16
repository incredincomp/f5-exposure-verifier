"""Sensitive data redaction utilities."""

import re

_PATTERNS = [
    (re.compile(r"(?i)(password|secret|token|key|credential)\s*[:=]\s*\S+"), r"\1=<REDACTED>"),
]


def redact_sensitive(text: str) -> str:
    """Redact common sensitive patterns from a string."""
    result = text
    for pattern, replacement in _PATTERNS:
        result = pattern.sub(replacement, result)
    return result
