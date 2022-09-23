from typing import Optional

from pydantic import BaseModel

class DebitCard(BaseModel):
    name: str
    amount: float
    id: int

    class Config:
        orm_mode = True