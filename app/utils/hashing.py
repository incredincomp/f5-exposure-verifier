"""Hashing utilities."""

import hashlib


def sha256_hex(data: bytes) -> str:
    """Return the SHA-256 hex digest of the given bytes."""
    return hashlib.sha256(data).hexdigest()


def sha256_str(data: str) -> str:
    """Return the SHA-256 hex digest of a UTF-8 string."""
    return sha256_hex(data.encode("utf-8"))
