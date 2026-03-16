"""Repository interface for verification requests."""

from sqlalchemy.orm import Session

from app.db.models.verification_request import VerificationRequest


class RequestsRepository:
    """Data access layer for VerificationRequest records."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, request_id: str) -> VerificationRequest | None:
        """Return the request with the given ID, or None if not found."""
        raise NotImplementedError

    def create(self, request: VerificationRequest) -> VerificationRequest:
        """Persist a new verification request."""
        raise NotImplementedError

    def update_status(self, request_id: str, status: str) -> None:
        """Update the status of an existing request."""
        raise NotImplementedError
