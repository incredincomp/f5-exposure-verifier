"""F5 BIG-IP API client stub."""


class F5Client:
    """HTTP client for the F5 BIG-IP REST API.

    Not yet implemented.
    """

    def __init__(self, host: str, username: str, password: str, verify_tls: bool = True) -> None:
        self._host = host
        self._username = username
        self._password = password
        self._verify_tls = verify_tls

    def get_virtual_servers(self) -> list[dict]:
        """Return a list of virtual server objects from F5."""
        raise NotImplementedError("F5 virtual server fetch is not yet implemented.")

    def get_pool_members(self, pool_name: str) -> list[dict]:
        """Return pool members for the given pool."""
        raise NotImplementedError("F5 pool member fetch is not yet implemented.")
