from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.models import database, schemas
from app import deps

router = APIRouter()


@router.post("/extract/", response_model=schemas.DebitExtractCreate, tags=["Debit Extract"])
def create_debit_extract(
    *,
    db: Session = Depends(deps.get_db),
    debit_extract_schema: schemas.DebitExtractCreate,
) -> Any:
    """
    Create new debit extract.
    """
    debit_extract = crud.debit_extract.create(db=db, obj_in=debit_extract_schema)
    return debit_extract