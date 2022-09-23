from typing import Optional

from pydantic import BaseModel

# Shared properties
class Category(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True