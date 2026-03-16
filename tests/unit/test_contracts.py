"""Tests for contract schema validation."""

import json
from pathlib import Path

import pytest

from app.contracts.verify_request import ExposureTarget, VerifyRequest
from app.contracts.verify_result import EvidenceSummary, VerdictCode, VerifyResult

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def test_verify_request_valid() -> None:
    """A valid VerifyRequest should parse without errors."""
    raw = json.loads((FIXTURES_DIR / "verify_request.json").read_text())
    req = VerifyRequest.model_validate(raw)
    assert req.source == "crowdstrike"
    assert req.target.ip_address == "10.0.0.1"
    assert req.target.port == 443


def test_verify_request_requires_ip() -> None:
    """A VerifyRequest without an ip_address must fail validation."""
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        ExposureTarget.model_validate({"port": 443})


def test_verify_result_valid() -> None:
    """A valid VerifyResult should parse without errors."""
    raw = json.loads((FIXTURES_DIR / "verify_result.json").read_text())
    result = VerifyResult.model_validate(raw)
    assert result.verdict == VerdictCode.UNKNOWN
    assert result.evidence.probe_count == 0


def test_verdict_codes_are_strings() -> None:
    """VerdictCode values should be usable as strings."""
    assert VerdictCode.APPROVED == "APPROVED"
    assert VerdictCode.UNAPPROVED == "UNAPPROVED"


def test_evidence_summary_defaults() -> None:
    """EvidenceSummary should have sensible defaults."""
    ev = EvidenceSummary()
    assert ev.probe_count == 0
    assert ev.observations == []
