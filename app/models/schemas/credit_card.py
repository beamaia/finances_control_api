from typing import Optional

from pydantic import BaseModel

class CreditCard(BaseModel):
    name: str
    amount: float
    best_day_date: str
    due_date: str
    max_limit: float
    total_limit_used: float
    id: int

    class Config:
        orm_mode = True