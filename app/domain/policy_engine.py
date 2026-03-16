"""Policy engine stub."""

from app.contracts.verify_request import ExposureTarget


def evaluate_policies(target: ExposureTarget) -> list[str]:
    """Evaluate active policy expectations against the target.

    Returns a list of policy violation codes.
    Not yet implemented.
    """
    raise NotImplementedError("Policy evaluation is not yet implemented.")
