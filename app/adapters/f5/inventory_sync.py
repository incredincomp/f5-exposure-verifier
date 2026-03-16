"""F5 inventory synchronization stub."""

from app.adapters.f5.client import F5Client
from app.contracts.inventory import InventorySnapshot


def sync_inventory(client: F5Client) -> InventorySnapshot:
    """Pull current inventory from F5 and return a snapshot contract.

    Not yet implemented.
    """
    raise NotImplementedError("F5 inventory sync is not yet implemented.")
