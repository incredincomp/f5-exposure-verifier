"""CrowdStrike webhook authentication stub."""


def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool:
    """Verify a CrowdStrike webhook HMAC signature.

    Not yet implemented.
    """
    raise NotImplementedError("CrowdStrike webhook auth is not yet implemented.")
