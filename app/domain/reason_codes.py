"""Reason codes for verdicts and classifications."""

from enum import Enum


class ReasonCode(str, Enum):
    """Structured reason codes used in verdicts."""

    # Inventory classification
    IN_APPROVED_INVENTORY = "IN_APPROVED_INVENTORY"
    NOT_IN_INVENTORY = "NOT_IN_INVENTORY"
    INVENTORY_UNAVAILABLE = "INVENTORY_UNAVAILABLE"

    # Policy
    POLICY_PASS = "POLICY_PASS"
    POLICY_VIOLATION = "POLICY_VIOLATION"

    # Probe
    PROBE_UNREACHABLE = "PROBE_UNREACHABLE"
    PROBE_REACHABLE = "PROBE_REACHABLE"
    PROBE_ERROR = "PROBE_ERROR"

    # System
    SYSTEM_ERROR = "SYSTEM_ERROR"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
