from sqlmodel import SQLModel

from app.config import DATA_DIR
from app.db import engine

# Import models so SQLModel registers them
import app.domain.models  # noqa: F401


def init_db() -> None:
    """Create data directory and all database tables."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    SQLModel.metadata.create_all(engine)
