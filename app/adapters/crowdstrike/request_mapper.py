"""CrowdStrike event to VerifyRequest mapper stub."""

from app.contracts.verify_request import VerifyRequest


def map_crowdstrike_event(event: dict) -> VerifyRequest:
    """Map a raw CrowdStrike event payload to a VerifyRequest contract.

    Not yet implemented.
    """
    raise NotImplementedError("CrowdStrike event mapping is not yet implemented.")
