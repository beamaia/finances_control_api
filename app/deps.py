from typing import Generator
from app.models.database.base import Session


def get_db() -> Generator:
    try:
        db = Session()
        yield db
    finally:
        db.close()

