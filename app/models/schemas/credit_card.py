from typing import Optional
import datetime

from pydantic import BaseModel

class CreditCard(BaseModel):
    name: str
    amount: float
    best_day_date: datetime.date
    due_date: datetime.date
    max_limit: float

    class Config:
        orm_mode = True


# Shared properties
class CreditCardBase(BaseModel):
    name: str = None
    amount: float = 0
    best_day_date: datetime.date
    due_date: datetime.date
    max_limit: float


# Properties to receive on credit card creation
class CreditCardCreate(CreditCardBase):
    pass


# Properties to receive on credit card update
class CreditCardUpdate(CreditCardBase):
    name: Optional[str]
    amount: Optional[float]
    best_day_date: Optional[datetime.date]
    due_date: Optional[datetime.date]
    max_limit: Optional[float]


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