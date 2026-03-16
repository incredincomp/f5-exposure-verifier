"""Repository interface for verification verdicts."""

from sqlalchemy.orm import Session

from app.db.models.verification_verdict import VerificationVerdict


class VerdictsRepository:
    """Data access layer for VerificationVerdict records."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_request_id(self, request_id: str) -> VerificationVerdict | None:
        """Return the verdict for the given request ID."""
        raise NotImplementedError

    def save(self, verdict: VerificationVerdict) -> VerificationVerdict:
        """Persist a verification verdict."""
        raise NotImplementedError
