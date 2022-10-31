from email.policy import default
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, Numeric, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

from app.models.database.base import Base

class DebitCard(Base):
    __tablename__ = 'debit_card'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    UniqueConstraint('name')

    def __init__(self, name:str, amount:float):
        self.name = name
        self.amount = amount