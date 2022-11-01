from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.schemas import CreditCardCreate, CreditCardUpdate
from app.models.database.credit_card import CreditCard


class CrudCreditCard(CRUDBase[CreditCard, CreditCardCreate, CreditCardUpdate]):
    pass


credit_card = CrudCreditCard(CreditCard)