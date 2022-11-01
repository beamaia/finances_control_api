from email.policy import default
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, Numeric, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.models.database.base import Base

import datetime

class CreditCard(Base):
    __tablename__ = 'credit_card'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    best_day_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    max_limit = Column(Numeric(10,2), nullable=False)

    def __init__(self, name:str, amount:float, best_day_date:datetime.date, due_date:datetime.date, max_limit:float):
        self.name = name
        self.amount = amount
        self.best_day_date = best_day_date
        self.due_date = due_date
        self.max_limit = max_limit
