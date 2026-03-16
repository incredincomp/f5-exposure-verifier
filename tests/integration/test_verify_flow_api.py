"""Integration test stubs for the verify flow API."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_verify_endpoint_is_wired() -> None:
    """POST /api/v1/verify should be reachable (returns 501 until implemented)."""
    response = client.post(
        "/api/v1/verify",
        json={"source": "test", "target": {"ip_address": "1.2.3.4"}},
    )
    assert response.status_code == 501
    data = response.json()
    assert "detail" in data
