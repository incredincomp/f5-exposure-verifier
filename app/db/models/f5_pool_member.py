"""F5PoolMember ORM model."""

import uuid

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class F5PoolMember(Base):
    """An F5 pool member entry within an inventory snapshot."""

    __tablename__ = "f5_pool_members"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    snapshot_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("f5_inventory_snapshots.id"), nullable=False
    )
    pool_name: Mapped[str] = mapped_column(String(255), nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    port: Mapped[int] = mapped_column(Integer, nullable=False)
    enabled: Mapped[bool] = mapped_column(default=True)
