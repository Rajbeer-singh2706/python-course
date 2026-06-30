"""
Day 02 — Variables & Data Types (Part 1: Core Data Types)
===========================================================

What this file covers:
    - Python's four core built-in data types: int, float, str, bool
    - Declaring variables and Python's dynamic typing
    - Using type() to inspect the type of any value

Prerequisites:
    - Day 01: Python environment set up, can run a .py file

How to run:
    $ python day02_01_data_types_basics.py
"""

# ════════════════════════════════════════════════════════════════
# SECTION 1: Variables — Labelled Boxes for Values
# ════════════════════════════════════════════════════════════════
# A variable is just a name that points to a value stored in memory.
# Python does NOT require you to declare a type up front — the type
# is decided automatically based on the value you assign. This is
# called "dynamic typing".

# ── Creating variables ──
student_name = "Priya"
student_age = 23
course_fee = 4999.00
is_enrolled = True

print(student_name)
print(student_age)
print(course_fee)
print(is_enrolled)
# Output:
# Priya
# 23
# 4999.0
# True

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: The Four Core Data Types
# ════════════════════════════════════════════════════════════════

# ── int (whole numbers) ──
# Used for counts, ages, quantities — anything without a decimal point.
mumbai_population_lakhs = 124
print("Population (lakhs):", mumbai_population_lakhs)

# ── float (decimal numbers) ──
# Used for prices, measurements, percentages — anything needing precision.
auto_fare = 87.50
print("Auto fare: Rs.", auto_fare)

# ── str (text) ──
# Any sequence of characters wrapped in quotes (single or double).
city = "Mumbai"
greeting = 'Namaste, Arjun!'
print(city, greeting)

# ── bool (True/False) ──
# Represents a binary state — used heavily in decision-making (Day 3).
has_ticket = False
print("Has ticket:", has_ticket)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: type() — Inspecting What You Have
# ════════════════════════════════════════════════════════════════
# type() tells you exactly what kind of value a variable holds.
# This is invaluable for debugging "why isn't this working" bugs.

print(type(student_name))   # <class 'str'>
print(type(student_age))    # <class 'int'>
print(type(course_fee))     # <class 'float'>
print(type(is_enrolled))    # <class 'bool'>

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════

# Example 1: A simple student profile
student1_name = "Riya Deshmukh"
student1_age = 21
student1_city = "Pune"
student1_active = True
print(f"{student1_name}, {student1_age}, lives in {student1_city}. Active: {student1_active}")

print("-" * 50)

# Example 2: Checking types of mixed values
values = ["Mumbai", 19.99, 42, False]
for v in values:
    print(v, "->", type(v))

print("-" * 50)

# Example 3: Rebinding a variable to a new type (legal in Python!)
mystery = 10          # currently int
print(type(mystery))  # <class 'int'>
mystery = "ten"        # now a str — Python allows this
print(type(mystery))  # <class 'str'>

print("-" * 50)

# Example 4: A small shopping cart total using int and float together
item_count = 3            # int
price_per_item = 249.0    # float
total_cost = item_count * price_per_item
print(f"Total cost for {item_count} items: Rs. {total_cost}")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Create four variables describing a chai stall in Delhi:
#   stall_name (str), cups_sold_today (int),
#   price_per_cup (float), is_open_now (bool)
# Then print each variable's type using type().
#
# Expected output (4 lines), something like:
#   <class 'str'>
#   <class 'int'>
#   <class 'float'>
#   <class 'bool'>

# YOUR CODE HERE


# SOLUTION:
# stall_name = "Sharma Chai Corner"
# cups_sold_today = 142
# price_per_cup = 12.50
# is_open_now = True
# print(type(stall_name))
# print(type(cups_sold_today))
# print(type(price_per_cup))
# print(type(is_open_now))

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Covered today (Part 1):
#   - Python's 4 core data types: int, float, str, bool
#   - Dynamic typing — Python infers type from the assigned value
#   - type() to inspect any variable
#
# Next up (Part 2): input(), print() formatting, and type casting.

if __name__ == "__main__":
    pass
