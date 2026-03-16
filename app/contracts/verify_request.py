"""Verification request contract."""

import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class ExposureTarget(BaseModel):
    """The target being verified."""

    model_config = ConfigDict(populate_by_name=True)

    ip_address: str = Field(..., description="Target IP address")
    port: int | None = Field(default=None, ge=1, le=65535)
    hostname: str | None = Field(default=None)
    protocol: str | None = Field(default=None, description="e.g. tcp, https")


class VerifyRequest(BaseModel):
    """Inbound exposure verification request."""

    model_config = ConfigDict(populate_by_name=True)

    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source: str = Field(..., description="Upstream source system identifier")
    target: ExposureTarget
    submitted_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    callback_url: str | None = Field(default=None)
    metadata: dict[str, str] = Field(default_factory=dict)
