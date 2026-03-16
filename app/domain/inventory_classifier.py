"""Inventory classifier stub."""

from app.contracts.inventory import InventorySnapshot
from app.contracts.verify_request import ExposureTarget


def classify_target(target: ExposureTarget, snapshot: InventorySnapshot) -> str:
    """Classify whether the target is in approved F5 inventory.

    Returns a classification string such as 'IN_INVENTORY' or 'NOT_IN_INVENTORY'.
    Not yet implemented.
    """
    raise NotImplementedError("Inventory classification is not yet implemented.")
