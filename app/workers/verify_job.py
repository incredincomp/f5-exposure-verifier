"""Verification background job stub."""

from app.contracts.verify_request import VerifyRequest


def run_verify_job(request: VerifyRequest) -> None:
    """Execute a verification job asynchronously.

    Async job processing is not yet implemented.
    This function is a hook point for future worker integration.
    """
    raise NotImplementedError("Async verification jobs are not yet implemented.")
