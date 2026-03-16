"""Idempotency service stub."""


class IdempotencyService:
    """Prevents duplicate processing of requests with the same ID.

    Not yet implemented.
    """

    def is_duplicate(self, request_id: str) -> bool:
        """Return True if the request_id has already been processed."""
        raise NotImplementedError("IdempotencyService.is_duplicate() is not yet implemented.")

    def mark_processed(self, request_id: str) -> None:
        """Mark the request_id as processed."""
        raise NotImplementedError("IdempotencyService.mark_processed() is not yet implemented.")
