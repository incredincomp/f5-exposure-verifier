"""TLS probe stub."""

from dataclasses import dataclass


@dataclass
class TlsProbeResult:
    """Result of a TLS probe."""

    connected: bool
    cert_subject: str | None = None
    cert_expiry: str | None = None
    protocol_version: str | None = None


def probe_tls(ip_address: str, port: int, timeout_seconds: float = 5.0) -> TlsProbeResult:
    """Perform a TLS handshake and collect certificate metadata.

    Not yet implemented.
    """
    raise NotImplementedError("TLS probe is not yet implemented.")
