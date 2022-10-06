from fastapi import APIRouter

from app.api_v1.endpoints import debit_card

api_router = APIRouter()
api_router.include_router(debit_card.router)
