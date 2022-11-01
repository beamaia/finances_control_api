from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.models import database, schemas
from app import deps

router = APIRouter()


@router.post("/credit_card/", response_model=schemas.CreditCard, tags=["Credit Card"])
def create_credit_card(
    *,
    db: Session = Depends(deps.get_db),
    credit_card_schema: schemas.CreditCardCreate,
) -> Any:
    """
    Create new credit card.
    """
    credit_card = crud.credit_card.create(db=db, obj_in=credit_card_schema)
    return credit_card


@router.put("/credit_card/{id}", response_model=schemas.CreditCardUpdate, tags=["Credit Card"])
def update_credit_card(
    *,
    db: Session = Depends(deps.get_db),
    credit_card_obj: schemas.CreditCardUpdate,
    id: int,
) -> Any:
    """
    Updates a credit card.
    """
    credit_card = crud.credit_card.get(db=db, id=id)
    if not credit_card:
        raise HTTPException(status_code=404, detail="Debit card not found")
    
    credit_card = crud.credit_card.update(db=db, obj_in=credit_card_obj, id=id)
    return credit_card

# TODO add debit/
@router.get("/credit_card/{id}", response_model=schemas.CreditCard, tags=["Credit Card"])
def read_credit_card(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get credit card by ID.
    """
    credit_card = crud.credit_card.get(db=db, id=id)
    if not credit_card:
        raise HTTPException(status_code=404, detail="Debit card not found")
    return credit_card


@router.delete("/credit_card/{id}", response_model=schemas.CreditCard, tags=["Credit Card"])
def delete_credit_card(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a credit card.
    """
    credit_card = crud.credit_card.get(db=db, id=id)
    if not credit_card:
        raise HTTPException(status_code=404, detail="Debit card not found")

    credit_card = crud.credit_card.remove(db=db, id=id)
    return credit_card