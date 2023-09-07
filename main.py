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

def add_expense():
    user_id = int(input("Enter User ID: "))
    category = str(input("Enter Category: "))
    amount = int(input("Enter Amount: "))
    date_str = input("Enter Date (YYYY-MM-DD): ")

    try:
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD' format.")
        return

    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        expense = Expense(
            user=user,
            category=category,
            amount=amount,
            date=date
        )
        session.add(expense)
        session.commit()
        print('Expense added successfully.')
    else:
        print('User not found.')