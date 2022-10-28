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


# Shared properties
class CreditCardBase(BaseModel):
    name: str = None
    amount: float = 0
    best_day_date: str
    due_date: str
    max_limit: float
    total_limit_used: float


# Properties to receive on credit card creation
class CreditCardCreate(CreditCardBase):
    pass


# Properties to receive on credit card update
class CreditCardUpdate(CreditCardBase):
    name: Optional[str]
    amount: Optional[float]
    best_day_date: Optional[str]
    due_date: Optional[str]
    max_limit: Optional[float]
    total_limit_used: Optional[float]


# Properties shared by models stored in DB
class CreditCardInDBBase(CreditCardBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class CreditCard(CreditCardInDBBase):
    pass

# Properties properties stored in DB
class CreditCardInDB(CreditCardInDBBase):
    pass