"""Callback delivery contract."""

from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from app.contracts.verify_result import VerifyResult


class CallbackStatus(str, Enum):
    PENDING = "PENDING"
    DELIVERED = "DELIVERED"
    FAILED = "FAILED"


class CallbackPayload(BaseModel):
    """Payload delivered to a callback URL."""

    model_config = ConfigDict(populate_by_name=True)

    event: str = "verification.completed"
    result: VerifyResult
    delivered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
