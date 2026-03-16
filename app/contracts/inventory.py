"""Inventory snapshot contract."""

import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class VirtualServerSummary(BaseModel):
    """Summary of a single F5 virtual server."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    ip_address: str
    port: int
    partition: str = "Common"


class InventorySnapshot(BaseModel):
    """Point-in-time snapshot of F5 inventory."""

    model_config = ConfigDict(populate_by_name=True)

    snapshot_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    f5_host: str
    virtual_servers: list[VirtualServerSummary] = Field(default_factory=list)
    captured_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
