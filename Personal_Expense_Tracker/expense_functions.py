from datetime import datetime

def add_expense(expenses):
    """Add one expense record to the list."""
    try:
        expense_id = max([item["Expense_ID"] for item in expenses], default=0) + 1
        date = input("Date (YYYY-MM-DD): ").strip()
        datetime.strptime(date, "%Y-%m-%d")
        category = input("Category (Food/Travel/Shopping/Bills/Other): ").strip().title()
        description = input("Description: ").strip()
        amount = float(input("Amount (Rs.): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return expenses
        payment = input("Payment mode (Cash/UPI/Card): ").strip().title()
        expenses.append({
            "Expense_ID": expense_id, "Date": date, "Category": category,
            "Description": description, "Amount": amount, "Payment_Mode": payment
        })
        print("Expense added successfully.")
    except ValueError:
        print("Invalid date or amount. Record was not added.")
    return expenses

def display_expenses(expenses):
    """Display all expense records."""
    if not expenses:
        print("No expense records found.")
        return
    for item in expenses:
        print(item)

def search_expense(expenses):
    """Search by expense ID or category."""
    term = input("Enter Expense ID or category: ").strip()
    results = [x for x in expenses if str(x["Expense_ID"]) == term or x["Category"].lower() == term.lower()]
    if results:
        for item in results:
            print(item)
    else:
        print("No matching expense found.")

def update_expense(expenses):
    """Update the description, category, or amount of a record."""
    try:
        expense_id = int(input("Enter Expense ID to update: "))
        for item in expenses:
            if item["Expense_ID"] == expense_id:
                print("Leave a field blank to keep its old value.")
                category = input(f'Category [{item["Category"]}]: ').strip()
                description = input(f'Description [{item["Description"]}]: ').strip()
                amount = input(f'Amount [{item["Amount"]}]: ').strip()
                if category:
                    item["Category"] = category.title()
                if description:
                    item["Description"] = description
                if amount:
                    new_amount = float(amount)
                    if new_amount <= 0:
                        print("Amount must be positive.")
                        return expenses
                    item["Amount"] = new_amount
                print("Expense updated successfully.")
                return expenses
        print("Expense ID not found.")
    except ValueError:
        print("Please enter a valid ID or amount.")
    return expenses

def delete_expense(expenses):
    """Delete a record using its expense ID."""
    try:
        expense_id = int(input("Enter Expense ID to delete: "))
        for item in expenses:
            if item["Expense_ID"] == expense_id:
                expenses.remove(item)
                print("Expense deleted successfully.")
                return expenses
        print("Expense ID not found.")
    except ValueError:
        print("Please enter a valid ID.")
    return expenses
