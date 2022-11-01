from typing import List, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.schemas import DebitExtractCreate, DebitExtractUpdate
from app.models.database.debit_extract import DebitExtract


class CrudDebitCard(CRUDBase[DebitExtract, DebitExtractCreate, DebitExtractUpdate]):
    def get_filtered(self, db: Session, extract_dict: Any) -> List[DebitExtract]:
        filtered_extract = db.query(self.model)
        for attr, value in extract_dict.items():
            filtered_extract = filtered_extract.filter(getattr(self.model, attr).like("%%%s%%" % value))
        return filtered_extract.all()


debit_extract = CrudDebitCard(DebitExtract)