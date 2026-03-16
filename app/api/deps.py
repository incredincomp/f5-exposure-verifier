"""FastAPI dependency injection helpers."""

from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_session


def get_db() -> Generator[Session, None, None]:
    """Yield a database session."""
    yield from get_session()


DbSession = Annotated[Session, Depends(get_db)]
