"""Health check endpoints."""

from fastapi import APIRouter
from pydantic import BaseModel

from app.db.session import check_db_connectivity

router = APIRouter()


class HealthResponse(BaseModel):
    status: str


class ReadinessResponse(BaseModel):
    status: str
    database: str


@router.get("/healthz", response_model=HealthResponse)
def healthz() -> HealthResponse:
    """Liveness probe — returns 200 if the process is running."""
    return HealthResponse(status="ok")


@router.get("/readyz", response_model=ReadinessResponse)
def readyz() -> ReadinessResponse:
    """Readiness probe — returns 200 if the service is ready to handle requests."""
    db_status = "ok" if check_db_connectivity() else "unavailable"
    return ReadinessResponse(status="ok", database=db_status)
