"""
Day 8 — Practice Problems
File 2 of 3: Section C (csv Module)

Cumulative scope: Days 2-8, focused on the csv module.

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines a couple of ideas
    🔴 Challenge — multi-step, closer to a real task

Section index (across all 3 files):
    A. Prior Days Review        (day08_practise_problems_01_file_basics.py)
    B. File Basics               (day08_practise_problems_01_file_basics.py)
    C. csv Module                 (this file)
    D. json Module                (day08_practise_problems_03_json_module.py)
    E. Mixed Challenges           (day08_practise_problems_03_json_module.py)

How to run:
    python day08_practise_problems_02_csv_module.py
"""

import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day08_data")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# ════════════════════════════════════════════════════════════
# SECTION C — csv Module
# ════════════════════════════════════════════════════════════

# --- Problem C1 --- 🟢 Warm-up
# Use csv.writer to create "fruits.csv" with header ["fruit", "price_per_kg"]
# and rows: ["Mango", 120], ["Banana", 40], ["Apple", 180].
# Then read it back with csv.reader and print every row.
# Expected output:
# ['fruit', 'price_per_kg']
# ['Mango', '120']
# ['Banana', '40']
# ['Apple', '180']

# YOUR CODE HERE


# SOLUTION:
# rows = [["fruit", "price_per_kg"], ["Mango", 120], ["Banana", 40], ["Apple", 180]]
# with open(path("fruits.csv"), "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)
#
# with open(path("fruits.csv"), "r", newline="") as f:
#     for row in csv.reader(f):
#         print(row)

print("-" * 50)


# --- Problem C2 --- 🟢 Warm-up
# Using csv.DictReader on "fruits.csv" from C1, print each fruit's name
# and price in the format "Mango costs Rs 120 per kg".
# Expected output:
# Mango costs Rs 120 per kg
# Banana costs Rs 40 per kg
# Apple costs Rs 180 per kg

# YOUR CODE HERE


# SOLUTION:
# with open(path("fruits.csv"), "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"{row['fruit']} costs Rs {row['price_per_kg']} per kg")

print("-" * 50)


# --- Problem C3 --- 🟡 Core
# Write a function average_price(filename) that uses csv.DictReader to
# read a CSV with a "price_per_kg" column and returns the average price
# rounded to 2 decimal places. Test it on "fruits.csv" from C1.
# Expected output: 113.33

# YOUR CODE HERE


# SOLUTION:
# def average_price(filename):
#     total = 0
#     count = 0
#     with open(filename, "r", newline="") as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             total += int(row["price_per_kg"])
#             count += 1
#     return round(total / count, 2)
#
# print(average_price(path("fruits.csv")))

print("-" * 50)


# --- Problem C4 --- 🟡 Core
# Meera runs a small stationery shop. Write code that:
#   1. Uses csv.DictWriter to create "stationery.csv" with columns
#      "item", "quantity" and rows:
#        {"item": "Notebook", "quantity": 30}
#        {"item": "Pen", "quantity": 100}
#        {"item": "Eraser", "quantity": 45}
#   2. Reads it back and prints the item with the HIGHEST quantity.
# Expected output: Pen has the highest quantity: 100

# YOUR CODE HERE


# SOLUTION:
# stationery_fields = ["item", "quantity"]
# stationery = [
#     {"item": "Notebook", "quantity": 30},
#     {"item": "Pen", "quantity": 100},
#     {"item": "Eraser", "quantity": 45},
# ]
# with open(path("stationery.csv"), "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=stationery_fields)
#     writer.writeheader()
#     writer.writerows(stationery)
#
# top_item = None
# top_qty = -1
# with open(path("stationery.csv"), "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         qty = int(row["quantity"])
#         if qty > top_qty:
#             top_qty = qty
#             top_item = row["item"]
#
# print(f"{top_item} has the highest quantity: {top_qty}")

print("-" * 50)


# --- Problem C5 --- 🔴 Challenge
# Riya has "orders.csv" with columns "customer", "city", "amount". Write
# code that:
#   1. Creates orders.csv (DictWriter) with rows:
#        {"customer": "Priya", "city": "Mumbai", "amount": 500}
#        {"customer": "Arjun", "city": "Delhi", "amount": 750}
#        {"customer": "Sanjay", "city": "Mumbai", "amount": 300}
#        {"customer": "Meera", "city": "Chennai", "amount": 450}
#   2. Reads it back and prints the TOTAL amount spent by customers in
#      Mumbai only.
# Expected output: Total spent in Mumbai: Rs 800

# YOUR CODE HERE


# SOLUTION:
# order_fields = ["customer", "city", "amount"]
# order_rows = [
#     {"customer": "Priya", "city": "Mumbai", "amount": 500},
#     {"customer": "Arjun", "city": "Delhi", "amount": 750},
#     {"customer": "Sanjay", "city": "Mumbai", "amount": 300},
#     {"customer": "Meera", "city": "Chennai", "amount": 450},
# ]
# with open(path("orders.csv"), "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=order_fields)
#     writer.writeheader()
#     writer.writerows(order_rows)
#
# mumbai_total = 0
# with open(path("orders.csv"), "r", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row["city"] == "Mumbai":
#             mumbai_total += int(row["amount"])
#
# print(f"Total spent in Mumbai: Rs {mumbai_total}")

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections covered in this file:
#   C. csv Module — 5 problems (csv.writer, csv.reader, DictWriter, DictReader)
#
# Difficulty breakdown: 2x 🟢 Warm-up | 2x 🟡 Core | 1x 🔴 Challenge
#
# Next up: day08_practise_problems_03_json_module.py — Section D (json module)
# and Section E (Mixed Challenges)

if __name__ == "__main__":
    print("Day 8 Practice — File 2 of 3 (Section C) ran successfully.")
