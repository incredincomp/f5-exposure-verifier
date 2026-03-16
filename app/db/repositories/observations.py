"""Repository interface for probe observations."""

from sqlalchemy.orm import Session

from app.db.models.probe_observation import ProbeObservation


class ObservationsRepository:
    """Data access layer for ProbeObservation records."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def list_by_run(self, run_id: str) -> list[ProbeObservation]:
        """Return all observations for the given run ID."""
        raise NotImplementedError

    def save(self, observation: ProbeObservation) -> ProbeObservation:
        """Persist a new probe observation."""
        raise NotImplementedError
