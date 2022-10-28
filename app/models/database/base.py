from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from app.core.config import DBVariables

# create an engine
address = f"postgresql://{DBVariables.user}:{DBVariables.password}@{DBVariables.host}:{DBVariables.port}/{DBVariables.database}"

engine = create_engine(address)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# create a base class for declarative class definitions
Base = declarative_base()