"""Repository interface for F5 inventory snapshots."""

from sqlalchemy.orm import Session

from app.db.models.f5_inventory_snapshot import F5InventorySnapshot


class InventoryRepository:
    """Data access layer for F5InventorySnapshot records."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_latest(self, f5_host: str) -> F5InventorySnapshot | None:
        """Return the most recent snapshot for the given host."""
        raise NotImplementedError

    def save(self, snapshot: F5InventorySnapshot) -> F5InventorySnapshot:
        """Persist a new inventory snapshot."""
        raise NotImplementedError
