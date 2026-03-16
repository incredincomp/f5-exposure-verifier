"""CrowdStrike callback client stub."""

from app.contracts.verify_result import VerifyResult


class CrowdStrikeCallbackClient:
    """Delivers verification results back to CrowdStrike.

    Not yet implemented.
    """

    def __init__(self, callback_url: str, timeout_seconds: int = 10) -> None:
        self._callback_url = callback_url
        self._timeout_seconds = timeout_seconds

    def deliver(self, result: VerifyResult) -> None:
        """Deliver the verification result to the callback URL."""
        raise NotImplementedError("CrowdStrike callback delivery is not yet implemented.")
