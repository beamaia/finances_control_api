from typing import Optional

from pydantic import BaseModel

class CreditExtract(BaseModel):
    credit_card_id: int
    category_id: int
    amount: float
    date: str
    description: str
    if_realized: bool

    class Config:
        orm_mode = True