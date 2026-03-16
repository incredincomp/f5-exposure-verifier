"""Inventory routes — not yet implemented."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/inventory")
def list_inventory() -> JSONResponse:
    """List F5 inventory snapshots.

    Not yet implemented.
    """
    return JSONResponse(
        status_code=501,
        content={"detail": "Not implemented.", "endpoint": "GET /api/v1/inventory"},
    )


@router.post("/inventory/refresh")
def refresh_inventory() -> JSONResponse:
    """Trigger an F5 inventory refresh.

    Not yet implemented.
    """
    return JSONResponse(
        status_code=501,
        content={
            "detail": "Not implemented.",
            "endpoint": "POST /api/v1/inventory/refresh",
        },
    )
