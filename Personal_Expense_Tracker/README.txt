# Personal Expense Tracker

## Project overview
A beginner-friendly Python project that stores personal expenses in a CSV file and provides add, display, search, update, delete, and analysis features.

## Requirements
- Python 3
- pandas
- numpy

Install libraries in the VS Code terminal:
    python -m pip install pandas numpy

## Run
1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Run:
       python main.py

## Files
- main.py: menu and main program
- expense_functions.py: add, display, search, update, delete functions
- file_operations.py: CSV read/write using Python file handling
- data_analysis.py: NumPy and Pandas analysis
- expenses.csv: starter dataset with 50 records

## Included implementation requirements
1. Dataset: 50 starter records.
2. Data structures: list, dictionary, tuple-like record fields? The project uses lists and dictionaries, and list methods such as append/remove; it also uses sets nowhere. For the viva, add a set and tuple example in the main program if your instructor expects five distinct concepts.
3. User-defined functions: more than five.
4. NumPy: 1D/2D arrays, indexing, slicing, sum, mean, max, min, standard deviation.
5. Pandas: DataFrame from CSV, selected rows/columns, filtering, sorting, GroupBy, missing values, statistical analysis.
6. Modules: three imported project modules.
7. File handling: CSV read and write.
8. CRUD and summary report.
9. Insights: spending total, average and highest-spending category.
10. Output: terminal menu and printed report.

Note: The sample CSV contains demonstration data. Replace it with your own expense records if required by your instructor. The report handles missing values in the analysis step; the CSV starter file is complete.
