"""Allowlist checker stub."""

from app.contracts.verify_request import ExposureTarget


def is_target_on_allowlist(target: ExposureTarget) -> bool:
    """Return True if the target is on the configured allowlist.

    Not yet implemented.
    """
    raise NotImplementedError("Allowlist checking is not yet implemented.")
