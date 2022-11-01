from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.models import database, schemas
from app import deps

router = APIRouter()


@router.post("/debit_card/", response_model=schemas.DebitCard, tags=["Debit Card"])
def create_debit_card(
    *,
    db: Session = Depends(deps.get_db),
    debit_card_schema: schemas.DebitCardCreate,
) -> Any:
    """
    Create new debit card.
    """
    debit_card = crud.debit_card.create(db=db, obj_in=debit_card_schema)
    return debit_card


@router.put("/debit_card/{id}", response_model=schemas.DebitCardUpdate, tags=["Debit Card"])
def update_debit_card(
    *,
    db: Session = Depends(deps.get_db),
    debit_card_obj: schemas.DebitCardUpdate,
    id: int,
) -> Any:
    """
    Updates a debit card.
    """
    debit_card = crud.debit_card.get(db=db, id=id)
    if not debit_card:
        raise HTTPException(status_code=404, detail="Debit card not found")
    
    debit_card = crud.debit_card.update(db=db, obj_in=debit_card_obj, id=id)
    return debit_card

@router.get("/debit_card/{id}", response_model=schemas.DebitCard, tags=["Debit Card"])
def read_debit_card(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get debit card by ID.
    """
    debit_card = crud.debit_card.get(db=db, id=id)
    if not debit_card:
        raise HTTPException(status_code=404, detail="Debit card not found")
    return debit_card


@router.delete("/debit_card/{id}", response_model=schemas.DebitCard, tags=["Debit Card"])
def delete_debit_card(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a debit card.
    """
    debit_card = crud.debit_card.get(db=db, id=id)
    if not debit_card:
        raise HTTPException(status_code=404, detail="Debit card not found")

    debit_card = crud.debit_card.remove(db=db, id=id)
    return debit_card