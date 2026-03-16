"""Integration test stubs for the inventory refresh API."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_inventory_list_is_wired() -> None:
    """GET /api/v1/inventory should be reachable (returns 501 until implemented)."""
    response = client.get("/api/v1/inventory")
    assert response.status_code == 501
    data = response.json()
    assert "detail" in data


def test_inventory_refresh_is_wired() -> None:
    """POST /api/v1/inventory/refresh should be reachable (returns 501 until implemented)."""
    response = client.post("/api/v1/inventory/refresh")
    assert response.status_code == 501
    data = response.json()
    assert "detail" in data
