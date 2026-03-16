"""Verdict summary text generation stub."""

from app.domain.reason_codes import ReasonCode


def generate_summary(code: ReasonCode) -> str:
    """Return a human-readable summary for a reason code.

    Not yet implemented for all codes.
    """
    summaries: dict[ReasonCode, str] = {
        ReasonCode.IN_APPROVED_INVENTORY: "Target is present in approved F5 inventory.",
        ReasonCode.NOT_IN_INVENTORY: "Target was not found in F5 inventory.",
        ReasonCode.INVENTORY_UNAVAILABLE: "F5 inventory was not available at verification time.",
        ReasonCode.POLICY_PASS: "Target passed all active policy checks.",
        ReasonCode.POLICY_VIOLATION: "Target violated one or more active policies.",
        ReasonCode.PROBE_UNREACHABLE: "Target was unreachable during probing.",
        ReasonCode.PROBE_REACHABLE: "Target was reachable during probing.",
        ReasonCode.PROBE_ERROR: "An error occurred during probing.",
        ReasonCode.SYSTEM_ERROR: "An internal system error occurred.",
        ReasonCode.NOT_IMPLEMENTED: "This feature is not yet implemented.",
    }
    return summaries.get(code, f"Unknown reason code: {code}")
