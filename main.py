from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Expense, Category
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
    date_str = input("Enter Date (DD-MM-YYYY): ")

    try:
        date = datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        print("Invalid date format. Please use 'DD-MM-YYYY' format.")
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
        print('Error.')



def search_expenses_by_category():
    category = input("Enter Category to search for: ")
    session = Session()
    expenses = session.query(Expense).filter_by(category=category).all()

    if expenses:
        print(f"\nExpenses in Category '{category}':")
        for expense in expenses:
            print(
                f"ID: {expense.id}, User ID: {expense.user_id}, Amount: {expense.amount}, Date: {expense.date}")
    else:
        print(f'No expenses found for the category: {category}')


def search_expenses_by_date():
    date = input("Enter Date (DD-MM-YYYY) to search for: ")
    session = Session()
    expenses = session.query(Expense).filter_by(date=date).all()

    if expenses:
        print(f"\nExpenses on Date '{date}':")
        for expense in expenses:
            print(
                f"ID: {expense.id}, User ID: {expense.user_id}, Category: {expense.category}, Amount: {expense.amount}")
    else:
        print(f'No expenses found for the date: {date}')


def delete_expense():
    expense_id = int(input("Enter Expense ID to delete: "))
    session = Session()
    expense = session.query(Expense).filter_by(id=expense_id).first()

    if expense:
        session.delete(expense)
        session.commit()
        print('Expense deleted successfully.')
    else:
        print('Expense not found.')


def delete_user():
    user_id = int(input("Enter User ID to delete: "))
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        session.delete(user)
        session.commit()
        print('User deleted successfully.')
    else:
        print('User not found.')


def main():
    while True:
        print("\nExpense Tracker")
        print("Commands:")
        print("1. List Expenses")
        print("2. List Categories")
        print("3. Add Expense")
        print("4. Search Expenses by Category")
        print("5. Search Expenses by Date")
        print("6. Delete Expense by ID")
        print("7. Delete User by ID")
        print("8. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            list_expenses()
        elif choice == "2":
            list_categories()
        elif choice == "3":
            add_expense()
        elif choice == "4":
            search_expenses_by_category()
        elif choice == "5":
            search_expenses_by_date()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            delete_user()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
