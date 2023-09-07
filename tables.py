from sqlalchemy import create_engine
from models import Base

DB_URL = 'sqlite:///expenses.db'
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)