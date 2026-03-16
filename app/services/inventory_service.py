"""Inventory management service stub."""

from app.contracts.inventory import InventorySnapshot


class InventoryService:
    """Manages F5 inventory snapshots.

    Not yet implemented.
    """

    def refresh(self) -> InventorySnapshot:
        """Pull fresh inventory from F5 and persist a snapshot.

        Not yet implemented.
        """
        raise NotImplementedError("InventoryService.refresh() is not yet implemented.")

    def get_latest(self) -> InventorySnapshot | None:
        """Return the most recent inventory snapshot.

        Not yet implemented.
        """
        raise NotImplementedError("InventoryService.get_latest() is not yet implemented.")
