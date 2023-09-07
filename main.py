from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Expense
from datetime import datetime


engine = create_engine('sqlite:///expenses.db')
Session = sessionmaker(bind=engine)


def list_expenses():
    session = Session()
    expenses = session.query(Expense).all()

    print("\nList of Expenses:")
    for expense in expenses:
        print(f"ID: {expense.id}, User ID: {expense.user_id}, Category: {expense.category}, Amount: {expense.amount}, Date: {expense.date}")


def list_categories():
    session = Session()
    all_categories = session.query(Expense.category).distinct().all()
    categories = set(category[0] for category in all_categories)

    print("\nList of Categories:")
    for category in categories:
        print(category)

