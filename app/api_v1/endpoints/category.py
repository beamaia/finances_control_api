from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.models import database, schemas
from app import deps

router = APIRouter()


@router.post("/category/", response_model=schemas.Category, tags=["Category"])
def create_category(
    *,
    db: Session = Depends(deps.get_db),
    category_schema: schemas.CategoryCreate
) -> Any:
    """
    Create new category.
    """
    category = crud.category.create(db=db, obj_in=category_schema)
    return category


@router.put("/category/{id}", response_model=schemas.CategoryUpdate, tags=["Category"])
def update_category(
    *,
    db: Session = Depends(deps.get_db),
    category_obj: schemas.CategoryUpdate,
    id: int,
) -> Any:
    """
    Updates a category.
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category = crud.category.update(db=db, obj_in=category_obj, id=id)
    return category

@router.get("/category/{id}", response_model=schemas.Category, tags=["Category"])
def read_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get category by ID.
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/category/{id}", response_model=schemas.Category, tags=["Category"])
def delete_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a category.
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category = crud.category.remove(db=db, id=id)
    return category