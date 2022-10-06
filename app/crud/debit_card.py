from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.schemas.debit_card import DebitCardCreate, DebitCardUpdate
from app.models.database.debit_card import DebitCard


class CrudDebitCard(CRUDBase[DebitCard, DebitCardCreate, DebitCardUpdate]):
    def create(
        self, db: Session, *, obj_in: DebitCardCreate, id: int
    ) -> DebitCard:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, id=id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, obj_in: DebitCardCreate, id: int):
        db_obj = db.query(self.model).filter(DebitCard.id == id).first()
        if db_obj:
            if obj_in.name:
                db_obj.name = obj_in.name
            if obj_in.amount:
                db_obj.amount = obj_in.amount
            db.commit()
            db.refresh(db_obj)
            return db_obj
        else:
            return None

debit_card = CrudDebitCard(DebitCard)