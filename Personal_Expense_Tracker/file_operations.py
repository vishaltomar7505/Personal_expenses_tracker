import csv
import os

FIELDS = ["Expense_ID", "Date", "Category", "Description", "Amount", "Payment_Mode"]

def load_expenses(filename):
    """Read project data from CSV using Python file handling."""
    if not os.path.exists(filename):
        return []
    records = []
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row["Expense_ID"] = int(row["Expense_ID"])
                row["Amount"] = float(row["Amount"])
                records.append(row)
            except (ValueError, KeyError):
                continue
    return records

def save_expenses(expenses, filename):
    """Write all records to CSV."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)
