"""F5VirtualServer ORM model."""

import uuid

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class F5VirtualServer(Base):
    """An F5 virtual server entry within an inventory snapshot."""

    __tablename__ = "f5_virtual_servers"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    snapshot_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("f5_inventory_snapshots.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    partition: Mapped[str] = mapped_column(String(128), default="Common")
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    port: Mapped[int] = mapped_column(Integer, nullable=False)
    enabled: Mapped[bool] = mapped_column(default=True)
