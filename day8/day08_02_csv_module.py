"""
Day 8 — File I/O
File 2 of 3: The csv Module — reading and writing tabular data

Covers:
    - Why CSV (Comma-Separated Values) is used for tabular data
    - csv.writer — writing rows to a CSV file
    - csv.reader — reading rows from a CSV file
    - csv.DictWriter / csv.DictReader — working with column names directly

Prerequisites:
    - Day 8, File 1: File Basics (open, with statement)
    - Day 6: Data Structures (lists, dictionaries)

How to run:
    python day08_02_csv_module.py
"""

import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day08_data")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# ════════════════════════════════════════════════════════════
# SECTION 1: Why CSV?
# ════════════════════════════════════════════════════════════
#
# CSV files store tabular data (rows and columns) as plain text, with
# commas separating each value. They open in Excel, Google Sheets, and
# any text editor — making them a universal format for exchanging data.
#
# Example of what a CSV file looks like on disk:
#   name,city,salary
#   Priya Sharma,Mumbai,65000
#   Arjun Mehta,Delhi,72000
#
# Python's built-in `csv` module handles all the tricky details for us
# (like commas inside values, quoting, and line endings).

print("── Concept: what a CSV file looks like ──")
print("name,city,salary")
print("Priya Sharma,Mumbai,65000")
print("Arjun Mehta,Delhi,72000")

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 2: csv.writer — writing rows
# ════════════════════════════════════════════════════════════
#
# csv.writer wraps a file object and gives us writerow() (one row) and
# writerows() (many rows at once). Always open CSV files with newline=""
# on write to avoid extra blank lines on Windows.

print("── Concept: csv.writer ──")

employees = [
    ["name", "city", "salary"],           # header row
    ["Priya Sharma", "Mumbai", 65000],
    ["Arjun Mehta", "Delhi", 72000],
    ["Riya Deshmukh", "Pune", 58000],
]

with open(path("employees.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(employees)   # writes all rows in one call

print("employees.csv written with", len(employees) - 1, "employee rows.")
# Output:
# employees.csv written with 3 employee rows.

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 3: csv.reader — reading rows
# ════════════════════════════════════════════════════════════
#
# csv.reader turns each line of the file into a list of strings.
# Note that every value comes back as a string, even numbers like salary —
# you must convert them yourself with int() or float() if needed.

print("── Concept: csv.reader ──")

with open(path("employees.csv"), "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)          # grab the header row separately
    print(f"Header: {header}")
    for row in reader:
        print(row)
# Output:
# Header: ['name', 'city', 'salary']
# ['Priya Sharma', 'Mumbai', '65000']
# ['Arjun Mehta', 'Delhi', '72000']
# ['Riya Deshmukh', 'Pune', '58000']

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 4: csv.DictWriter and csv.DictReader
# ════════════════════════════════════════════════════════════
#
# Working with plain lists means remembering column order by position
# (row[0], row[1], ...). DictWriter and DictReader let us work with
# column NAMES instead, using Python dictionaries — much more readable.

print("── Concept: csv.DictWriter ──")

fieldnames = ["name", "city", "salary"]
employee_dicts = [
    {"name": "Priya Sharma", "city": "Mumbai", "salary": 65000},
    {"name": "Arjun Mehta", "city": "Delhi", "salary": 72000},
    {"name": "Riya Deshmukh", "city": "Pune", "salary": 58000},
]

with open(path("employees_dict.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()          # writes the header row automatically
    writer.writerows(employee_dicts)

print("employees_dict.csv written using DictWriter.")
# Output:
# employees_dict.csv written using DictWriter.

print("-" * 50)

print("── Concept: csv.DictReader ──")

with open(path("employees_dict.csv"), "r", newline="") as f:
    reader = csv.DictReader(f)     # each row becomes a dict automatically
    for row in reader:
        print(f"{row['name']} works in {row['city']}, earning Rs {row['salary']}")
# Output:
# Priya Sharma works in Mumbai, earning Rs 65000
# Arjun Mehta works in Delhi, earning Rs 72000
# Riya Deshmukh works in Pune, earning Rs 58000

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 1: Total salary using csv.DictReader
# ════════════════════════════════════════════════════════════

print("── Guided Example 1: Total salary ──")

total_salary = 0
with open(path("employees_dict.csv"), "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_salary += int(row["salary"])   # convert string -> int

print(f"Total monthly salary payout: Rs {total_salary}")
# Output:
# Total monthly salary payout: Rs 195000

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 2: Filtering rows — employees in Mumbai only
# ════════════════════════════════════════════════════════════

print("── Guided Example 2: Filtering by city ──")

mumbai_employees = []
with open(path("employees_dict.csv"), "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["city"] == "Mumbai":
            mumbai_employees.append(row["name"])

print(f"Employees in Mumbai: {mumbai_employees}")
# Output:
# Employees in Mumbai: ['Priya Sharma']

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 3: Appending a new employee to an existing CSV
# ════════════════════════════════════════════════════════════

print("── Guided Example 3: Appending a new row ──")

new_employee = {"name": "Sanjay Verma", "city": "Bengaluru", "salary": 80000}

with open(path("employees_dict.csv"), "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(new_employee)   # appends without rewriting the header

with open(path("employees_dict.csv"), "r", newline="") as f:
    reader = csv.DictReader(f)
    all_names = [row["name"] for row in reader]

print(f"All employees now: {all_names}")
# Output:
# All employees now: ['Priya Sharma', 'Arjun Mehta', 'Riya Deshmukh', 'Sanjay Verma']

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 4: Handling values that contain commas
# ════════════════════════════════════════════════════════════
#
# The csv module automatically wraps values containing commas in quotes,
# so they don't get mistaken for column separators.

print("── Guided Example 4: Values with commas ──")

addresses = [
    ["name", "address"],
    ["Priya Sharma", "204, Marine Drive, Mumbai"],
    ["Arjun Mehta", "12, Connaught Place, Delhi"],
]

with open(path("addresses.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(addresses)

with open(path("addresses.csv"), "r", newline="") as f:
    for row in csv.reader(f):
        print(row)
# Output:
# ['name', 'address']
# ['Priya Sharma', '204, Marine Drive, Mumbai']
# ['Arjun Mehta', '12, Connaught Place, Delhi']

print("-" * 50)


# ════════════════════════════════════════════════════════════
# 🔴 MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Arjun runs a small electronics shop and wants a CSV of his products.
# Write code that:
#   1. Creates "products.csv" using DictWriter with columns:
#      "product", "price", "quantity"
#      and these three rows:
#        {"product": "USB Cable", "price": 199, "quantity": 50}
#        {"product": "Power Bank", "price": 899, "quantity": 20}
#        {"product": "Earphones", "price": 499, "quantity": 35}
#   2. Reads it back with DictReader and prints the total inventory
#      value (price * quantity, summed across all rows)
#
# Expected output:
# Total inventory value: Rs 43655

print("── Mini-Challenge: Product inventory value ──")

# YOUR CODE HERE


# SOLUTION:
# product_fields = ["product", "price", "quantity"]
# products = [
#     {"product": "USB Cable", "price": 199, "quantity": 50},
#     {"product": "Power Bank", "price": 899, "quantity": 20},
#     {"product": "Earphones", "price": 499, "quantity": 35},
# ]
#
# with open(path("products.csv"), "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=product_fields)
#     writer.writeheader()
#     writer.writerows(products)
#
# total_value = 0
# with open(path("products.csv"), "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         total_value += int(row["price"]) * int(row["quantity"])
#
# print(f"Total inventory value: Rs {total_value}")

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file we covered:
#   - Why CSV is used for tabular data
#   - csv.writer / csv.reader for list-based rows
#   - csv.DictWriter / csv.DictReader for dictionary-based rows
#   - Appending rows, filtering rows, and handling commas in values
#
# Next up (File 3 of 3): The `json` module — reading and writing
# structured data used by almost every web API.

if __name__ == "__main__":
    print("Day 8, File 2 of 3 (csv Module) ran successfully.")
