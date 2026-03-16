"""HTTP probe stub."""

from dataclasses import dataclass


@dataclass
class HttpProbeResult:
    """Result of an HTTP probe."""

    status_code: int | None
    server_header: str | None = None
    redirect_url: str | None = None


def probe_http(
    url: str, timeout_seconds: float = 5.0, follow_redirects: bool = False
) -> HttpProbeResult:
    """Perform an HTTP request and collect response metadata.

    Not yet implemented.
    """
    raise NotImplementedError("HTTP probe is not yet implemented.")
