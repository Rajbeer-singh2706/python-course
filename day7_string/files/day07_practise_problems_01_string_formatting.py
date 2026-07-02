"""
Day 07 — Practice Problems (File 1 of 3)
Topic: Prior Days Review + String Formatting

Cumulative scope: Days 01-07 (variables, control flow, loops,
functions, data structures, string formatting/f-strings)

Difficulty legend:
    Warm-up
    Core
    Challenge

Section Index:
    Section A — Prior Days Review          (Problems 1-3)
    Section B — String Formatting          (Problems 4-7)

How to run:
    python day07_practise_problems_01_string_formatting.py
"""

# ════════════════════════════════════════════════════════════
# SECTION A: Prior Days Review
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("SECTION A: Prior Days Review")
print("=" * 50)

# Problem 1  Warm-up
# ----------------------------------------------------------------
# Given a list of daily sales figures (Day 06 topic), calculate
# and print the total and average sale.
#
# Given:
daily_sales = [1200, 1500, 980, 2100, 1750]
#
# Expected output:
# Total: 7530
# Average: 1506.0

# YOUR CODE HERE


# SOLUTION:
# total = sum(daily_sales)
# average = total / len(daily_sales)
# print(f"Total: {total}")
# print(f"Average: {average}")

print("-" * 50)

# Problem 2  Warm-up
# ----------------------------------------------------------------
# Write a function (Day 05 topic) called `is_even` that takes a
# number and returns True if it is even, False otherwise. Test it
# on the numbers 14 and 27.
#
# Expected output:
# 14 is even: True
# 27 is even: False

# YOUR CODE HERE


# SOLUTION:
# def is_even(number):
#     return number % 2 == 0
#
# print(f"14 is even: {is_even(14)}")
# print(f"27 is even: {is_even(27)}")

print("-" * 50)

# Problem 3  Core
# ----------------------------------------------------------------
# Using a for loop (Day 04 topic) and an if/elif/else chain
# (Day 03 topic), classify each score in the list below as
# "Pass" (>= 40) or "Fail" (< 40).
#
# Given:
scores = [55, 32, 78, 12, 40]
#
# Expected output:
# 55: Pass
# 32: Fail
# 78: Pass
# 12: Fail
# 40: Pass

# YOUR CODE HERE


# SOLUTION:
# for score in scores:
#     if score >= 40:
#         print(f"{score}: Pass")
#     else:
#         print(f"{score}: Fail")

print("=" * 50)

# ════════════════════════════════════════════════════════════
# SECTION B: String Formatting
# ════════════════════════════════════════════════════════════
print("SECTION B: String Formatting")
print("=" * 50)

# Problem 4  Warm-up
# ----------------------------------------------------------------
# Use an f-string to print a greeting using the variables below.
#
# Given:
customer_name = "Arjun Mehta"
order_total = 2450
#
# Expected output:
# Hi Arjun Mehta, your order total is Rs. 2450.

# YOUR CODE HERE


# SOLUTION:
# print(f"Hi {customer_name}, your order total is Rs. {order_total}.")

print("-" * 50)

# Problem 5  Warm-up
# ----------------------------------------------------------------
# Format the given float to exactly 2 decimal places using an
# f-string format specifier.
#
# Given:
weight_kg = 3.14159
#
# Expected output:
# Weight: 3.14 kg

# YOUR CODE HERE


# SOLUTION:
# print(f"Weight: {weight_kg:.2f} kg")

print("-" * 50)

# Problem 6  Core
# ----------------------------------------------------------------
# Given a large rupee amount, print it with a thousands separator
# and 2 decimal places using an f-string.
#
# Given:
account_balance = 1245789.5
#
# Expected output:
# Balance: Rs. 1,245,789.50

# YOUR CODE HERE


# SOLUTION:
# print(f"Balance: Rs. {account_balance:,.2f}")

print("-" * 50)

# Problem 7  Challenge
# ----------------------------------------------------------------
# Print an aligned mini table of three employees and their
# salaries using format specifiers. Names should be left-aligned
# in a field of width 15; salaries should be right-aligned in a
# field of width 10 with a thousands separator and 2 decimals.
#
# Given:
employees = [
    ("Riya Deshmukh", 78500.0),
    ("Sanjay Verma", 92300.75),
    ("Priya Shah", 65000.0),
]
#
# Expected output:
# Riya Deshmukh    Rs.  78,500.00
# Sanjay Verma     Rs.  92,300.75
# Priya Shah       Rs.  65,000.00

# YOUR CODE HERE


# SOLUTION:
# for emp_name, emp_salary in employees:
#     print(f"{emp_name:<17}Rs. {emp_salary:>9,.2f}")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file:
#   Section A — Prior Days Review     (3 problems)
#   Section B — String Formatting     (4 problems)
#
# Difficulty breakdown: 3 Warm-up, 3 Core, 1 Challenge
#
# Next file: day07_practise_problems_02_string_methods.py covers
# split(), join(), strip(), and replace().
