from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.models import database, schemas
from app import deps

router = APIRouter()


@router.post("/", response_model=schemas.DebitCard)
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


@router.put("/{id}", response_model=schemas.DebitCardUpdate)
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


@router.get("/{id}", response_model=schemas.debit_card.DebitCard)
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


# @router.delete("/{id}", response_model=schemas.Item)
# def delete_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: database.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.remove(db=db, id=id)
#     return item