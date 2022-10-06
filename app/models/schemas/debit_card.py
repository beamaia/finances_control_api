from typing import Optional

from pydantic import BaseModel

# Shared properties
class DebitCardBase(BaseModel):
    name: str = None
    amount: float = 0
    id: int

    class Config:
        orm_mode = True


# Properties to receive on debit card creation
class DebitCardCreate(DebitCardBase):
    name: str
    amount: float = 0


# Properties to receive on debit card update
class DebitCardUpdate(DebitCardBase):
    name: str
    amount: float


# Properties shared by models stored in DB
class DebitCardInDBBase(DebitCardBase):
    name: str
    amount: float
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class DebitCard(DebitCardInDBBase):
    name: str
    amount: float


# Properties properties stored in DB
class DebitCardInDB(DebitCardInDBBase):
    pass