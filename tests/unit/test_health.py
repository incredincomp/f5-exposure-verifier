"""Tests for health check endpoints."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz_returns_200() -> None:
    """GET /healthz must return 200 with status=ok."""
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_readyz_returns_200() -> None:
    """GET /readyz must return 200 with status=ok and a database field."""
    response = client.get("/readyz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "database" in data


def test_verify_stub_returns_501() -> None:
    """POST /api/v1/verify must return 501 (not yet implemented)."""
    response = client.post("/api/v1/verify", json={})
    assert response.status_code == 501


def test_inventory_stub_returns_501() -> None:
    """GET /api/v1/inventory must return 501 (not yet implemented)."""
    response = client.get("/api/v1/inventory")
    assert response.status_code == 501


def test_requests_stub_returns_501() -> None:
    """GET /api/v1/requests must return 501 (not yet implemented)."""
    response = client.get("/api/v1/requests")
    assert response.status_code == 501


def test_verdicts_stub_returns_501() -> None:
    """GET /api/v1/verdicts must return 501 (not yet implemented)."""
    response = client.get("/api/v1/verdicts")
    assert response.status_code == 501
