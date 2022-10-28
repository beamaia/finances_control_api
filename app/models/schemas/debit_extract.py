from typing import Optional

from pydantic import BaseModel

class DebitExtract(BaseModel):
    debit_card_id: int
    category_id: int
    amount: float
    date: str
    description: str
    if_realized: bool

    class Config:
        orm_mode = True

# Shared properties
class DebitExtractBase(BaseModel):
    debit_card_id: int
    category_id: int
    amount: float
    date: str
    description: Optional[str]
    if_realized: bool
    income: bool

# Properties to receive on debit extract creation
class DebitExtractCreate(DebitExtractBase):
    pass


# Properties to receive on debit extract update
class DebitExtractUpdate(DebitExtractBase):
    debit_card_id: int
    category_id: Optional[int]
    amount: Optional[float]
    date: Optional[str]
    description: Optional[str]
    if_realized: Optional[bool]
    income: Optional[bool]

# Properties shared by models stored in DB
class DebitExtractInDBBase(DebitExtractBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class DebitExtract(DebitExtractInDBBase):
    pass

# Properties properties stored in DB
class DebitExtractInDB(DebitExtractInDBBase):
    pass