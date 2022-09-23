from email.policy import default
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, Numeric, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.models.database.base import Base
from app.models.database.models.category import Category
from app.models.database.models.credit_card import CreditCard

import datetime

class CreditExtract(Base):
    __tablename__ = 'credit_extract'
    id = Column(Integer, primary_key=True, autoincrement=True)
    credit_card_id = Column(Integer, ForeignKey('credit_card.id'), nullable=False)
    credit_card = relationship(CreditCard)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship(Category)

    amount = Column(Numeric(10,2), nullable=False)
    date = Column(Date, nullable=False, default=datetime.datetime.utcnow)
    description = Column(String(50), nullable=False)
    if_realized = Column(Boolean, nullable=False, default=True)

    def __init__(self, credit_card_id:int, category_id:int, amount:float, description:str, date:datetime.date=datetime.datetime.utcnow(), if_realized:bool=True):
        self.credit_card_id = credit_card_id
        self.category_id = category_id
        self.amount = amount
        self.date = date
        self.description = description
        self.if_realized = if_realized
