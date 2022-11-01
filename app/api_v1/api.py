from fastapi import APIRouter

from app.api_v1.endpoints import debit_card
from app.api_v1.endpoints import debit_extract
from app.api_v1.endpoints import category
from app.api_v1.endpoints import credit_card

api_router = APIRouter()

api_router.include_router(category.router)
api_router.include_router(debit_card.router)
api_router.include_router(debit_extract.router)
api_router.include_router(credit_card.router)
