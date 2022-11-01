from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.models import database, schemas
from app import deps

router = APIRouter()

# TODO param not showing up
@router.post("/extract/{debit_id}", response_model=List[schemas.DebitExtract], tags=["Debit Extract"])
def create_debit_extract(
    *,
    db: Session = Depends(deps.get_db),
    debit_extract_schema: schemas.DebitExtractCreate,
) -> Any:
    """
    Create new debit extract.
    """
    debit_extract = crud.debit_extract.create(db=db, debit_id = debit_id, obj_in=debit_extract_schema)
    return debit_extract