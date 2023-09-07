# ExpenseTracker

Expense Tracker is a simple Python application that allows users to manage their expenses. You can list expenses, categorize them, add new expenses, search for expenses by category or date, delete expenses, and manage user profiles.

# Table of Contents 
 [Installation Instructions](#installation-instructions)  
 [Usage Information](#usage-information)  
 [Commands](#commands)
 [Contributing](#contributing)
 [Licenses](#licenses)

# To get started,
follow the installation and usage instructions below.

# Prerequisites
* Python 3
* Pipenv (optional but recommended for dependency management.)
* SQLite database (automatically created on installation)

# Installation

1. Clone this repository to your local machine using the `git clone` comman in your terminal

2. Navigate to project directory snf create a virtual env (`cd ~/ExpenseTracker-phase3`)

3. Install the required Python packages(`pip install -r requirements.txt
`)

# Usage
 Run the Expense tracker by running the command `python main.py
`

Follow the on-screen menu to excecute various commands and manage your expenses.

## Commands
Expense Tracker supports the following commands:

1. List Expenses: View a list of all expenses.
2. List Categories: View a list of expense categories.
3. Add Expense: Add a new expense to your account.
4. Search Expenses by Category: Search for expenses by category.
5. Search Expenses by Date: Search for expenses by date.
6. Delete Expense by ID: Delete an expense by its unique ID.
7. Delete User by ID: Delete a user profile by their ID.
8. Quit: Exit the Expense Tracker application

# Database
The application uses an SQLite database to store user profiles and expense data. The database file is created automatically when you run the application and is named expenses.db.

# Contributing
Contributions to this project are welcome. Feel free to open issues, suggest enhancements, or submit pull requests.

# License
This project is licensed under the MIT License