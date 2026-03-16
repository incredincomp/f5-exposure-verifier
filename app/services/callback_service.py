"""Callback delivery service stub."""

from app.contracts.verify_result import VerifyResult


class CallbackService:
    """Manages callback delivery to upstream systems.

    Not yet implemented.
    """

    def deliver(self, result: VerifyResult, callback_url: str) -> None:
        """Deliver a verification result to the given callback URL.

        Not yet implemented.
        """
        raise NotImplementedError("CallbackService.deliver() is not yet implemented.")
