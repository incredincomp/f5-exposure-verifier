"""Verification result contract."""

import uuid
from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class VerdictCode(str, Enum):
    """High-level verdict codes."""

    APPROVED = "APPROVED"
    UNAPPROVED = "UNAPPROVED"
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"


class EvidenceSummary(BaseModel):
    """Summary of collected evidence."""

    model_config = ConfigDict(populate_by_name=True)

    probe_count: int = 0
    observations: list[str] = Field(default_factory=list)


class VerifyResult(BaseModel):
    """Outbound verification result."""

    model_config = ConfigDict(populate_by_name=True)

    result_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    request_id: str
    verdict: VerdictCode
    reason: str
    evidence: EvidenceSummary = Field(default_factory=EvidenceSummary)
    completed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
