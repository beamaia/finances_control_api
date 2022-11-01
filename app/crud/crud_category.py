from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.schemas import CategoryCreate, CategoryUpdate
from app.models.database.category import Category


class CrudCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass


category = CrudCategory(Category)