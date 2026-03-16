"""Shared contract primitives."""

import uuid
from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


class TimestampedModel(BaseModel):
    """Base model with created_at timestamp."""

    model_config = ConfigDict(populate_by_name=True)

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class ErrorResponse(BaseModel):
    """Standard error response envelope."""

    model_config = ConfigDict(populate_by_name=True)

    detail: str
    code: str | None = None
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
