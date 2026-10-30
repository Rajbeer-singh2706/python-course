"""
Day 02 — Practice Problems (Part 1: Core Data Types)
=======================================================

Day 02 cumulative scope: variables, int/float/str/bool, type(),
input()/print(), type casting.

Difficulty legend: 🟢 Warm-up   🟡 Core   🔴 Challenge

Section index:
    A — Prior Days Review (Day 1: setup/print basics)
    B — Core Data Types & type()

(Sections C-E continue in day02_practise_problems_02_io_and_mixed.py)

How to run:
    $ python day02_practise_problems_01_data_types.py
"""

# ════════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review (Day 1)
# ════════════════════════════════════════════════════════════════

# --- Problem A1 ---
# 🟢 Warm-up
# Print a single line that says: "Hello from Day 2!"
# Expected output: Hello from Day 2!

# YOUR CODE HERE


# SOLUTION:
# print("Hello from Day 2!")

print("-" * 50)

# --- Problem A2 ---
# 🟢 Warm-up
# Print your name and the current course day number on two separate
# print() calls. Use any name you like, e.g. "Arjun" and 2.
# Expected output (2 lines):
#   Arjun
#   2

# YOUR CODE HERE


# SOLUTION:
# print("Arjun")
# print(2)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION B — Core Data Types & type()
# ════════════════════════════════════════════════════════════════

# --- Problem B1 ---
# 🟢 Warm-up
# Create a variable `city` set to "Mumbai" and print its type.
# Expected output: <class 'str'>

# YOUR CODE HERE


# SOLUTION:
# city = "Mumbai"
# print(type(city))

print("-" * 50)

# --- Problem B2 ---
# 🟢 Warm-up
# Create an int variable `rupees` = 500 and a float variable
# `dollars` = 6.25. Print both types.
# Expected output:
#   <class 'int'>
#   <class 'float'>

# YOUR CODE HERE


# SOLUTION:
# rupees = 500
# dollars = 6.25
# print(type(rupees))
# print(type(dollars))

print("-" * 50)

# --- Problem B3 ---
# 🟡 Core
# Create a bool variable `is_diwali_today` set to False, then print
# a sentence using it, e.g. "Is it Diwali today? False"

# YOUR CODE HERE


# SOLUTION:
# is_diwali_today = False
# print("Is it Diwali today?", is_diwali_today)

print("-" * 50)

# --- Problem B4 ---
# 🟡 Core
# Create four variables describing a Mumbai vada pav stall:
#   stall_name (str) = "Ashok Vada Pav"
#   price (float) = 25.0
#   plates_sold (int) = 80
#   is_famous (bool) = True
# Print each variable's type on its own line (4 lines total).

# YOUR CODE HERE


# SOLUTION:
# stall_name = "Ashok Vada Pav"
# price = 25.0
# plates_sold = 80
# is_famous = True
# print(type(stall_name))
# print(type(price))
# print(type(plates_sold))
# print(type(is_famous))

print("-" * 50)

# --- Problem B5 ---
# 🔴 Challenge
# Take this existing variable:
#   value = 100
# Rebind `value` first to a float (100.5), then to a string ("100.5"),
# printing type(value) after each rebinding (3 lines total).
# Expected output:
#   <class 'int'>
#   <class 'float'>
#   <class 'str'>

# YOUR CODE HERE


# SOLUTION:
# value = 100
# print(type(value))
# value = 100.5
# print(type(value))
# value = "100.5"
# print(type(value))

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY (Part 1 of 2)
# ════════════════════════════════════════════════════════════════
# Sections in this file: A (Prior Review), B (Data Types & type())
# Difficulty breakdown so far: 4x Warm-up, 2x Core, 1x Challenge
# Continue with Section C-E in:
#   day02_practise_problems_02_io_and_mixed.py

if __name__ == "__main__":
    pass
