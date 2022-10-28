from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.schemas import DebitCardCreate, DebitCardUpdate
from app.models.database.debit_card import DebitCard


class CrudDebitCard(CRUDBase[DebitCard, DebitCardCreate, DebitCardUpdate]):
    pass


debit_card = CrudDebitCard(DebitCard)