"""Verdict engine stub."""

from app.contracts.verify_result import VerdictCode


def compute_verdict(
    classification: str,
    policy_violations: list[str],
    probe_results: list[dict],
) -> tuple[VerdictCode, str]:
    """Compute the final verdict from classification, policy, and probe data.

    Returns a (VerdictCode, reason) tuple.
    Not yet implemented.
    """
    raise NotImplementedError("Verdict computation is not yet implemented.")
