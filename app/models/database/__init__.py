from app.models.database.category import Category
from app.models.database.credit_card import CreditCard
from app.models.database.credit_extract import CreditExtract
from app.models.database.debit_card import DebitCard
from app.models.database.debit_extract import DebitExtract
from app.models.database.base import Base, engine
Base.metadata.create_all(engine)
