"""F5 virtual server operations stub."""

from app.adapters.f5.client import F5Client
from app.adapters.f5.models import F5VirtualServerData


def list_virtual_servers(client: F5Client) -> list[F5VirtualServerData]:
    """Retrieve and parse virtual servers from F5.

    Not yet implemented.
    """
    raise NotImplementedError("F5 virtual server listing is not yet implemented.")
