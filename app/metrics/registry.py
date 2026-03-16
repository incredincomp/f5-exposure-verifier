"""Prometheus metrics registry stub."""

from prometheus_client import Counter, Gauge, Histogram

verifications_total = Counter(
    "f5_verifier_verifications_total",
    "Total number of verification requests received",
    ["status"],
)

verification_duration_seconds = Histogram(
    "f5_verifier_verification_duration_seconds",
    "Duration of verification runs in seconds",
)

inventory_snapshot_age_seconds = Gauge(
    "f5_verifier_inventory_snapshot_age_seconds",
    "Age of the most recent F5 inventory snapshot in seconds",
)
