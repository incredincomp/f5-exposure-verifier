"""F5 inventory cache hook stub."""


class InventoryCache:
    """Optional Redis-backed cache for F5 inventory.

    Not yet implemented. Hook point for future Redis integration.
    """

    def get(self, key: str) -> bytes | None:
        """Return cached value or None."""
        raise NotImplementedError("Inventory cache is not yet implemented.")

    def set(self, key: str, value: bytes, ttl_seconds: int = 300) -> None:
        """Store a value with an optional TTL."""
        raise NotImplementedError("Inventory cache is not yet implemented.")
