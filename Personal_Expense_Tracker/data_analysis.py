import numpy as np
import pandas as pd

def generate_report(filename):
    """Use Pandas and NumPy to analyse the expense dataset."""
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("Dataset file not found.")
        return

    if df.empty:
        print("No data available for analysis.")
        return

    # Handle missing values
    df["Category"] = df["Category"].fillna("Other")
    df["Description"] = df["Description"].fillna("Not provided")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Amount"] = df["Amount"].fillna(df["Amount"].median())

    # Create a DataFrame, select rows/columns, filter and sort
    print("\n--- First five records ---")
    print(df.head())
    print("\n--- Selected columns ---")
    print(df[["Date", "Category", "Amount"]].head())
    print("\n--- Expenses above Rs. 500 ---")
    print(df[df["Amount"] > 500].to_string(index=False))
    print("\n--- Expenses sorted by amount (highest first) ---")
    print(df.sort_values(by="Amount", ascending=False).head(10).to_string(index=False))

    # GroupBy operation
    print("\n--- Total expense by category ---")
    print(df.groupby("Category")["Amount"].sum().sort_values(ascending=False))

    # NumPy 1D and 2D arrays, indexing and slicing
    amounts = df["Amount"].to_numpy()
    expense_matrix = df[["Expense_ID", "Amount"]].to_numpy()
    print("\n--- NumPy 1D array (amounts) ---")
    print(amounts)
    print("First amount (index 0):", amounts[0])
    print("First five amounts (slice):", amounts[:5])
    print("\n--- NumPy 2D array (ID and amount) ---")
    print(expense_matrix[:5])

    print("\n--- NumPy statistical analysis ---")
    print("Total expense:", np.sum(amounts))
    print("Average expense:", np.mean(amounts))
    print("Maximum expense:", np.max(amounts))
    print("Minimum expense:", np.min(amounts))
    print("Standard deviation:", np.std(amounts))

    print("\n--- Pandas statistical analysis ---")
    print(df["Amount"].describe())

    total = df["Amount"].sum()
    highest_category = df.groupby("Category")["Amount"].sum().idxmax()
    print("\n========== SUMMARY INSIGHTS ==========")
    print("Number of records:", len(df))
    print(f"Total spending: Rs. {total:.2f}")
    print(f"Average spending per record: Rs. {df['Amount'].mean():.2f}")
    print("Highest spending category:", highest_category)
    print("This report is generated from the current CSV dataset.")
