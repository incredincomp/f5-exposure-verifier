"""F5InventorySnapshot ORM model."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class F5InventorySnapshot(Base):
    """Point-in-time snapshot of F5 inventory."""

    __tablename__ = "f5_inventory_snapshots"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    f5_host: Mapped[str] = mapped_column(String(255), nullable=False)
    virtual_server_count: Mapped[int] = mapped_column(Integer, default=0)
    pool_member_count: Mapped[int] = mapped_column(Integer, default=0)
    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
