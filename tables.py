from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models import User, Expense

# Create an SQLite database engine
engine = create_engine('sqlite:///expenses.db')

# Create a base class for declarative models
Base = declarative_base()

# Seed some sample data
Session = sessionmaker(bind=engine)
session = Session()

# Create users
user1 = User(username='john_doe')
user2 = User(username='jane_smith')

# Add users to the session
session.add_all([user1, user2])
session.commit()

# Create expenses
expense1 = Expense(user=user1, category='Food', amount=250, date='2023-09-03')
expense2 = Expense(user=user1, category='Transport', amount=50, date='2023-09-04')
expense3 = Expense(user=user2, category='Entertainment', amount=100, date='2023-09-03')

# Add expenses to the session
session.add_all([expense1, expense2, expense3])
session.commit()

Base.metadata.create_all(engine)