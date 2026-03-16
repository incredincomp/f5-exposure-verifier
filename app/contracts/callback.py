"""Callback delivery contract."""

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field

from app.contracts.verify_result import VerifyResult


class CallbackPayload(BaseModel):
    """Payload delivered to a callback URL."""

    model_config = ConfigDict(populate_by_name=True)

    event: str = "verification.completed"
    result: VerifyResult
    delivered_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
