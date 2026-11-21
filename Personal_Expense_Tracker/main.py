import pandas as pd
from expense_functions import add_expense, display_expenses, search_expense, update_expense, delete_expense
from file_operations import load_expenses, save_expenses
from data_analysis import generate_report

FILE_NAME = "expenses.csv"

def main():
    expenses = load_expenses(FILE_NAME)

    while True:
        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add new expense")
        print("2. Display all expenses")
        print("3. Search expense")
        print("4. Update expense")
        print("5. Delete expense")
        print("6. Generate summary report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            expenses = add_expense(expenses)
            save_expenses(expenses, FILE_NAME)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            search_expense(expenses)
        elif choice == "4":
            expenses = update_expense(expenses)
            save_expenses(expenses, FILE_NAME)
        elif choice == "5":
            expenses = delete_expense(expenses)
            save_expenses(expenses, FILE_NAME)
        elif choice == "6":
            generate_report(FILE_NAME)
        elif choice == "7":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter 1 to 7.")

if __name__ == "__main__":
    main()
