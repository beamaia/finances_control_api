from typing import Optional
import datetime

from pydantic import BaseModel

# Shared properties
class DebitExtractBase(BaseModel):
    amount: float
    category_id: int
    date: Optional[str] = datetime.datetime.now()
    description: Optional[str] = ""
    if_realized: Optional[bool] = True
    income: Optional[bool] = False

# Properties to receive on debit extract creation
class DebitExtractCreate(DebitExtractBase):
    pass

# Properties to receive on debit extract update
class DebitExtractUpdate(DebitExtractBase):
    category_id: Optional[int]
    amount: Optional[float]
    date: Optional[str]
    description: Optional[str]
    if_realized: Optional[bool]
    income: Optional[bool]

# Properties shared by models stored in DB
class DebitExtractInDBBase(DebitExtractBase):
    id: int
    debit_card_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class DebitExtract(DebitExtractInDBBase):
    pass

# Properties properties stored in DB
class DebitExtractInDB(DebitExtractInDBBase):
    pass