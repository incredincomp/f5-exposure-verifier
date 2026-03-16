"""F5 adapter data models."""

from dataclasses import dataclass


@dataclass
class F5VirtualServerData:
    """Raw virtual server data from the F5 API."""

    name: str
    partition: str
    ip_address: str
    port: int
    enabled: bool = True


@dataclass
class F5PoolMemberData:
    """Raw pool member data from the F5 API."""

    pool_name: str
    ip_address: str
    port: int
    enabled: bool = True
