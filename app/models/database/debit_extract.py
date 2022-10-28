from email.policy import default
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, Numeric, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.models.database.base import Base
from app.models.database.category import Category
from app.models.database.debit_card import DebitCard

import datetime

class DebitExtract(Base):
    __tablename__ = 'debit_extract'
    id = Column(Integer, primary_key=True, autoincrement=True)
    debit_card_id = Column(Integer, ForeignKey('debit_card.id'), nullable=False)
    debit_card = relationship(DebitCard)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship(Category)
    
    amount = Column(Numeric(10,2), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(50), nullable=False)
    if_realized = Column(Boolean, nullable=False)
    income = Column(Boolean, nullable=False)

    def __init__(self, debit_card_id:int, category_id:int, amount:float, date:datetime.date, description:str, if_realized:bool=True, income:bool=False):
        self.debit_card_id = debit_card_id
        self.category_id = category_id
        self.amount = amount
        self.date = date
        self.description = description
        self.if_realized = if_realized
        self.income = income