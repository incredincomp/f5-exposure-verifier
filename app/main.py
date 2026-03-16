"""FastAPI application factory."""

from fastapi import FastAPI

from app.api.routes_health import router as health_router
from app.api.routes_inventory import router as inventory_router
from app.api.routes_requests import router as requests_router
from app.api.routes_verdicts import router as verdicts_router
from app.api.routes_verify import router as verify_router
from app.config.settings import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    application = FastAPI(
        title="F5 Exposure Verifier",
        description="Bounded external exposure verification and enrichment service.",
        version="0.1.0",
        docs_url="/docs" if settings.app_debug else None,
        redoc_url="/redoc" if settings.app_debug else None,
    )

    application.include_router(health_router, tags=["health"])
    application.include_router(verify_router, prefix="/api/v1", tags=["verify"])
    application.include_router(inventory_router, prefix="/api/v1", tags=["inventory"])
    application.include_router(requests_router, prefix="/api/v1", tags=["requests"])
    application.include_router(verdicts_router, prefix="/api/v1", tags=["verdicts"])

    return application


app = create_app()
