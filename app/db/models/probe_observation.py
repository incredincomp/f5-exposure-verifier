"""ProbeObservation ORM model."""

import uuid
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ProbeObservation(Base):
    """A single probe result recorded during a verification run."""

    __tablename__ = "probe_observations"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    run_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("verification_runs.id"), nullable=False
    )
    probe_type: Mapped[str] = mapped_column(String(32), nullable=False)
    target_ip: Mapped[str] = mapped_column(String(45), nullable=False)
    target_port: Mapped[int | None] = mapped_column(Integer, nullable=True)
    result: Mapped[str] = mapped_column(String(32), nullable=False)
    raw_output: Mapped[str | None] = mapped_column(Text, nullable=True)
    observed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
