from email.policy import default
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, Numeric, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.models.database.base import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name:str):
        self.name = name
