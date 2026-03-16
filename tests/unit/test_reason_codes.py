"""Tests for reason codes and summaries."""

from app.domain.reason_codes import ReasonCode
from app.domain.summaries import generate_summary


def test_all_reason_codes_have_summaries() -> None:
    """Every ReasonCode must have a non-empty summary."""
    for code in ReasonCode:
        summary = generate_summary(code)
        assert summary, f"Missing summary for {code}"
        assert "Unknown reason code" not in summary, f"No summary for {code}"


def test_reason_codes_are_strings() -> None:
    """ReasonCode values must be usable as plain strings."""
    assert ReasonCode.IN_APPROVED_INVENTORY == "IN_APPROVED_INVENTORY"
    assert ReasonCode.SYSTEM_ERROR == "SYSTEM_ERROR"


def test_generate_summary_for_known_code() -> None:
    """generate_summary should return correct text for known codes."""
    summary = generate_summary(ReasonCode.NOT_IN_INVENTORY)
    assert "inventory" in summary.lower()
