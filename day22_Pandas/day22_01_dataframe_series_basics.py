"""
Day 22 — Data & Pandas
File 1 of 5: DataFrame and Series Basics

Covers:
    - What Pandas is and why we use it
    - Creating a Series (1-D labelled array)
    - Creating a DataFrame (2-D labelled table)
    - Indexing with .loc[] and .iloc[]
    - Inspecting data: .head(), .tail(), .info(), .describe(), .shape, .columns, .dtypes
    - Selecting columns and rows
    - Adding and modifying columns

Prerequisites:
    - Day 6 (Data Structures — lists, dicts)
    - Day 21 (NumPy — ndarrays, since Pandas is built on top of NumPy)

How to run:
    python day22_01_dataframe_series_basics.py
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("DAY 22 - PANDAS: DATAFRAME & SERIES BASICS")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION 1: Why Pandas?
# ════════════════════════════════════════════════════════════
# NumPy (Day 21) is great for numerical arrays, but real-world
# data usually comes with LABELS — column names, row names,
# mixed data types (text + numbers + dates).
#
# Pandas gives us two core structures:
#   Series    -> a single labelled column (1-D)
#   DataFrame -> a labelled table made of many Series (2-D)
#
# Think of a DataFrame like an Excel sheet or a SQL table,
# except you can manipulate it entirely in Python.

print("\n── Why Pandas? ──")
print("Pandas = Panel Data. Built on top of NumPy for fast, labelled data.")

# ════════════════════════════════════════════════════════════
# SECTION 2: Creating a Series
# ════════════════════════════════════════════════════════════
print("\n── Creating a Series ──")

# A Series is like a single column with an index attached.
fares = pd.Series([45, 60, 30, 100, 75])
print(fares)
# Output:
# 0     45
# 1     60
# 2     30
# 3    100
# 4     75
# dtype: int64

# We can give it a custom index instead of 0,1,2...
auto_fares = pd.Series(
    [45, 60, 30, 100, 75],
    index=["MG Road", "Koramangala", "Indiranagar", "Whitefield", "HSR Layout"],
    name="Auto Fare (Rs)",
)
print("\nNamed Series with custom index:")
print(auto_fares)
# Output:
# MG Road         45
# Koramangala     60
# Indiranagar     30
# Whitefield     100
# HSR Layout      75
# Name: Auto Fare (Rs), dtype: int64

# Access by label
print("\nFare to Whitefield:", auto_fares["Whitefield"])
# Output: Fare to Whitefield: 100

# A Series can also be built from a dictionary — keys become the index
population = pd.Series({"Mumbai": 12442373, "Delhi": 11007835, "Bengaluru": 8443675})
print("\nSeries from dict:")
print(population)

# ════════════════════════════════════════════════════════════
# SECTION 3: Creating a DataFrame
# ════════════════════════════════════════════════════════════
print("\n── Creating a DataFrame ──")

# Method 1: from a dictionary of lists (most common)
students = pd.DataFrame({
    "name": ["Priya Sharma", "Arjun Mehta", "Riya Deshmukh", "Sanjay Verma", "Meera Iyer"],
    "city": ["Mumbai", "Delhi", "Pune", "Jaipur", "Chennai"],
    "marks": [88, 76, 92, 65, 81],
    "attendance_pct": [95.5, 88.0, 99.0, 72.5, 91.0],
})
print(students)
# Output: a 5-row x 4-column table with a default 0..4 index

# Method 2: from a list of dictionaries (row-wise)
orders = pd.DataFrame([
    {"order_id": "ORD1001", "item": "Kurta", "price": 899},
    {"order_id": "ORD1002", "item": "Jeans", "price": 1499},
    {"order_id": "ORD1003", "item": "Saree", "price": 2499},
])
print("\nOrders built row-wise:")
print(orders)

# Method 3: from a NumPy array (numeric grid with labels on top)
marks_grid = pd.DataFrame(
    np.array([[80, 90, 70], [60, 75, 85], [95, 88, 92]]),
    columns=["Maths", "Science", "English"],
    index=["Priya", "Arjun", "Riya"],
)
print("\nDataFrame from NumPy array:")
print(marks_grid)

# ════════════════════════════════════════════════════════════
# SECTION 4: Inspecting a DataFrame
# ════════════════════════════════════════════════════════════
print("\n── Inspecting a DataFrame ──")

print("Shape (rows, columns):", students.shape)
# Output: Shape (rows, columns): (5, 4)

print("\nColumn names:", list(students.columns))
# Output: Column names: ['name', 'city', 'marks', 'attendance_pct']

print("\nData types per column:")
print(students.dtypes)

print("\nFirst 3 rows (.head(3)):")
print(students.head(3))

print("\nLast 2 rows (.tail(2)):")
print(students.tail(2))

print("\nQuick statistical summary (.describe()):")
print(students.describe())
# Output: count/mean/std/min/25%/50%/75%/max for numeric columns only

print("\n.info() summary:")
students.info()

# ════════════════════════════════════════════════════════════
# SECTION 5: Selecting Columns and Rows
# ════════════════════════════════════════════════════════════
print("\n── Selecting Columns ──")

# Single column -> returns a Series
print("Just the 'name' column:")
print(students["name"])

# Multiple columns -> returns a DataFrame (note the double brackets)
print("\n'name' and 'marks' columns:")
print(students[["name", "marks"]])

print("\n── Selecting Rows: .loc[] vs .iloc[] ──")
# .loc[]  -> select by LABEL (index name)
# .iloc[] -> select by POSITION (integer, like list indexing)

print("Row at label 2 (.loc[2]):")
print(students.loc[2])

print("\nRow at position 0 (.iloc[0]):")
print(students.iloc[0])

print("\nSlice of rows 1 to 3 by position (.iloc[1:4]):")
print(students.iloc[1:4])

print("\nSpecific cell — marks of student at position 2 (.iloc[2, 2]):")
print(students.iloc[2, 2])
# Output: 92

print("\nSpecific cell by label — 'marks' column, row label 2 (.loc[2, 'marks']):")
print(students.loc[2, "marks"])
# Output: 92

# ════════════════════════════════════════════════════════════
# SECTION 6: Boolean Filtering (Conditional Selection)
# ════════════════════════════════════════════════════════════
print("\n── Boolean Filtering ──")

# Students who scored above 80
toppers = students[students["marks"] > 80]
print("Students with marks > 80:")
print(toppers)

# Combine conditions with & (and) / | (or) — each condition in parentheses!
good_attendance_toppers = students[(students["marks"] > 75) & (students["attendance_pct"] > 90)]
print("\nMarks > 75 AND attendance > 90:")
print(good_attendance_toppers)

# ════════════════════════════════════════════════════════════
# SECTION 7: Adding and Modifying Columns
# ════════════════════════════════════════════════════════════
print("\n── Adding and Modifying Columns ──")

# Add a new column computed from existing ones
students["grade"] = students["marks"].apply(
    lambda m: "A" if m >= 85 else ("B" if m >= 70 else "C")
)
print(students)

# Modify an existing column (e.g., round attendance to nearest integer)
students["attendance_pct"] = students["attendance_pct"].round(0)
print("\nAfter rounding attendance:")
print(students)

# Drop a column (returns a new DataFrame unless inplace=True)
students_no_city = students.drop(columns=["city"])
print("\nAfter dropping 'city' column:")
print(students_no_city)

# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Build a DataFrame named `swiggy_orders` with columns:
#   "restaurant" -> ["Sagar Ratna", "Behrouz Biryani", "Domino's"]
#   "city"       -> ["Delhi", "Hyderabad", "Mumbai"]
#   "order_value"-> [450, 620, 399]
# Then:
#   1. Print only rows where order_value > 400
#   2. Add a new column "gst" = order_value * 0.05
#   3. Print the final DataFrame

# YOUR CODE HERE
swiggy_orders = pd.DataFrame({
    "restaurant": ["Sagar Ratna", "Behrouz Biryani", "Domino's"],
    "city": ["Delhi", "Hyderabad", "Mumbai"],
    "order_value": [450, 620, 399],
})
print("\n── Mini-Challenge: Swiggy Orders ──")
print(swiggy_orders[swiggy_orders["order_value"] > 400])
swiggy_orders["gst"] = swiggy_orders["order_value"] * 0.05
print(swiggy_orders)
# Expected output: rows for Sagar Ratna & Behrouz Biryani printed first (order_value > 400),
# then the full table with a new 'gst' column added.

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# - Series = labelled 1-D array; DataFrame = labelled 2-D table
# - Create DataFrames from dicts of lists, lists of dicts, or NumPy arrays
# - Inspect with .head(), .tail(), .info(), .describe(), .shape, .dtypes
# - Select columns with df["col"] or df[["col1", "col2"]]
# - Select rows with .loc[] (by label) and .iloc[] (by position)
# - Filter rows with boolean conditions: df[df["col"] > value]
# - Add columns by assignment; drop columns with .drop(columns=[...])
#
# Next: File 2 covers reading and writing real CSV files with Pandas.
