"""Verification orchestration service stub."""

from app.contracts.verify_request import VerifyRequest
from app.contracts.verify_result import VerifyResult


class VerifyService:
    """Orchestrates the full verification workflow.

    Not yet implemented.
    """

    def run(self, request: VerifyRequest) -> VerifyResult:
        """Execute verification for the given request.

        Not yet implemented.
        """
        raise NotImplementedError("VerifyService.run() is not yet implemented.")
