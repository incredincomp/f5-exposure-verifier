"""F5 pool member operations stub."""

from app.adapters.f5.client import F5Client
from app.adapters.f5.models import F5PoolMemberData


def list_pool_members(client: F5Client, pool_name: str) -> list[F5PoolMemberData]:
    """Retrieve and parse pool members from F5.

    Not yet implemented.
    """
    raise NotImplementedError("F5 pool member listing is not yet implemented.")
