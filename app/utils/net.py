"""Network utilities."""

import ipaddress
import socket


def is_valid_ip(address: str) -> bool:
    """Return True if the string is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


def is_private_ip(address: str) -> bool:
    """Return True if the address is in a private/reserved range."""
    try:
        return ipaddress.ip_address(address).is_private
    except ValueError:
        return False


def resolve_hostname(hostname: str) -> str | None:
    """Resolve a hostname to its first IP address, or None on failure."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None
