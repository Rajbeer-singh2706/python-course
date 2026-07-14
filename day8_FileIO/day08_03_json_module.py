"""
Day 8 — File I/O
File 3 of 3: The json Module — reading and writing structured data

Covers:
    - What JSON is and why it's used everywhere (APIs, configs, storage)
    - json.dump() / json.load() — writing/reading JSON files
    - json.dumps() / json.loads() — converting to/from JSON strings
    - Nested JSON structures (dicts inside lists inside dicts)

Prerequisites:
    - Day 8, File 1: File Basics (open, with statement)
    - Day 6: Data Structures (lists, dictionaries)

How to run:
    python day08_03_json_module.py
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day08_data")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# ════════════════════════════════════════════════════════════
# SECTION 1: What is JSON?
# ════════════════════════════════════════════════════════════
#
# JSON (JavaScript Object Notation) is a lightweight, text-based format
# for storing structured data. It maps almost perfectly onto Python's
# dictionaries and lists, which is why it's the standard format used by
# nearly every web API (Swiggy, IRCTC, Flipkart, etc.).
#
# Python type  <->  JSON type
#   dict       <->  object   { "key": "value" }
#   list       <->  array    [1, 2, 3]
#   str        <->  string   "hello"
#   int/float  <->  number   42
#   True/False <->  true/false
#   None       <->  null

print("── Concept: Python <-> JSON mapping ──")
print('dict -> {"key": "value"},  list -> [1, 2, 3],  None -> null')

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 2: json.dump() — writing a Python object to a JSON file
# ════════════════════════════════════════════════════════════

print("── Concept: json.dump() ──")

customer = {
    "name": "Priya Sharma",
    "city": "Mumbai",
    "is_prime_member": True,
    "orders_this_month": 4,
}

with open(path("customer.json"), "w") as f:
    json.dump(customer, f, indent=4)   # indent=4 makes it human-readable

print("customer.json written.")
# Output:
# customer.json written.

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 3: json.load() — reading a JSON file back into Python
# ════════════════════════════════════════════════════════════

print("── Concept: json.load() ──")

with open(path("customer.json"), "r") as f:
    loaded_customer = json.load(f)

print(f"Type: {type(loaded_customer)}")
print(f"Name: {loaded_customer['name']}")
print(f"Prime member? {loaded_customer['is_prime_member']}")
# Output:
# Type: <class 'dict'>
# Name: Priya Sharma
# Prime member? True

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION 4: json.dumps() and json.loads() — working with strings
# ════════════════════════════════════════════════════════════
#
# The 's' in dumps/loads stands for "string". Use these when you need
# JSON as a string in memory (e.g. sending it over a network) rather
# than writing it straight to a file.

print("── Concept: json.dumps() and json.loads() ──")

order = {"order_id": "SW1042", "item": "Masala Dosa", "price": 180}

json_string = json.dumps(order)              # Python dict -> JSON string
print(f"JSON string: {json_string}")

parsed_back = json.loads(json_string)        # JSON string -> Python dict
print(f"Parsed back item: {parsed_back['item']}")
# Output:
# JSON string: {"order_id": "SW1042", "item": "Masala Dosa", "price": 180}
# Parsed back item: Masala Dosa

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 1: Nested JSON — a list of orders
# ════════════════════════════════════════════════════════════

print("── Guided Example 1: Nested structures ──")

orders_data = {
    "customer": "Arjun Mehta",
    "city": "Delhi",
    "orders": [
        {"item": "Paneer Butter Masala", "price": 220},
        {"item": "Butter Naan", "price": 45},
        {"item": "Sweet Lassi", "price": 60},
    ],
}

with open(path("orders.json"), "w") as f:
    json.dump(orders_data, f, indent=4)

with open(path("orders.json"), "r") as f:
    loaded = json.load(f)

for order_item in loaded["orders"]:
    print(f"{order_item['item']}: Rs {order_item['price']}")
# Output:
# Paneer Butter Masala: Rs 220
# Butter Naan: Rs 45
# Sweet Lassi: Rs 60

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 2: Calculating a bill total from nested JSON
# ════════════════════════════════════════════════════════════

print("── Guided Example 2: Bill total ──")

with open(path("orders.json"), "r") as f:
    loaded = json.load(f)

bill_total = sum(order_item["price"] for order_item in loaded["orders"])
print(f"{loaded['customer']}'s total bill: Rs {bill_total}")
# Output:
# Arjun Mehta's total bill: Rs 325

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 3: A list of records (like an API response)
# ════════════════════════════════════════════════════════════

print("── Guided Example 3: List of records ──")

students = [
    {"name": "Riya Deshmukh", "city": "Pune", "marks": 88},
    {"name": "Sanjay Verma", "city": "Bengaluru", "marks": 91},
    {"name": "Meera", "city": "Chennai", "marks": 76},
]

with open(path("students.json"), "w") as f:
    json.dump(students, f, indent=4)

with open(path("students.json"), "r") as f:
    loaded_students = json.load(f)

topper = max(loaded_students, key=lambda s: s["marks"])
print(f"Topper: {topper['name']} with {topper['marks']} marks")
# Output:
# Topper: Sanjay Verma with 91 marks

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 4: Handling a missing key safely with .get()
# ════════════════════════════════════════════════════════════

print("── Guided Example 4: Safe key access with .get() ──")

partial_record = {"name": "Meera", "city": "Chennai"}   # no "marks" key

# Using square brackets here would raise a KeyError since "marks" is missing.
marks = partial_record.get("marks", "Not available")
print(f"{partial_record['name']}'s marks: {marks}")
# Output:
# Meera's marks: Not available

print("-" * 50)


# ════════════════════════════════════════════════════════════
# 🔴 MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
#
# Sanjay wants to save his IRCTC train booking as JSON. Write code that:
#   1. Creates a dict called "booking" with:
#        "pnr": "4521367890"
#        "passenger": "Sanjay Verma"
#        "train": "Rajdhani Express"
#        "from_city": "Delhi"
#        "to_city": "Mumbai"
#        "fare": 1850
#   2. Writes it to "booking.json" using json.dump() with indent=4
#   3. Reads it back with json.load() and prints:
#      "Sanjay Verma's PNR 4521367890: Delhi -> Mumbai (Rs 1850)"
#
# Expected output:
# Sanjay Verma's PNR 4521367890: Delhi -> Mumbai (Rs 1850)

print("── Mini-Challenge: IRCTC booking JSON ──")

# YOUR CODE HERE


# SOLUTION:
# booking = {
#     "pnr": "4521367890",
#     "passenger": "Sanjay Verma",
#     "train": "Rajdhani Express",
#     "from_city": "Delhi",
#     "to_city": "Mumbai",
#     "fare": 1850,
# }
#
# with open(path("booking.json"), "w") as f:
#     json.dump(booking, f, indent=4)
#
# with open(path("booking.json"), "r") as f:
#     loaded_booking = json.load(f)
#
# print(
#     f"{loaded_booking['passenger']}'s PNR {loaded_booking['pnr']}: "
#     f"{loaded_booking['from_city']} -> {loaded_booking['to_city']} "
#     f"(Rs {loaded_booking['fare']})"
# )

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
#
# In this file we covered:
#   - What JSON is and how Python types map to JSON types
#   - json.dump() / json.load() for files
#   - json.dumps() / json.loads() for strings
#   - Nested JSON structures and safe access with .get()
#
# This completes Day 8 — File I/O. You now know how to work with plain
# text files, CSV spreadsheets, and JSON — the three most common data
# formats you'll encounter as a Python developer.
#
# Next up: Day 9 — Error Handling (try/except, custom exceptions, logging).

if __name__ == "__main__":
    print("Day 8, File 3 of 3 (json Module) ran successfully.")
