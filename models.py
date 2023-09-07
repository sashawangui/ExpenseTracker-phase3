from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

engine = create_engine('sqlite:///expenses.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    expenses = relationship('Expense', back_populates='user')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)  

    expenses = relationship('Expense', back_populates='category')

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False, default=func.now())

    user = relationship('User', back_populates='expenses')
    category = relationship ("Category", back_populates='expenses')

Base.metadata.create_all(engine)
