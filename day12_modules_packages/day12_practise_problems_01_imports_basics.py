"""
Day 12 — Practice Problems (File 1 of 3)
==========================================

Topic         : Import statements, from...import, and packages
Cumulative    : Covers Days 1-12 (review section included)
Difficulty    : 🟢 Warm-up | 🟡 Core | 🔴 Challenge
Section Index :
    A — Prior Days Review (Days 1-11)
    B — Import Basics & Aliasing (Day 12)

Run with: python day12_practise_problems_01_imports_basics.py
All input() calls are simulated using pre-assigned variables.
"""

import math

print("=" * 60)
print("SECTION A — PRIOR DAYS REVIEW")
print("=" * 60)

# ── Problem A1 — 🟢 Warm-up ──
# Write a function `is_even(n)` (Day 5: functions) that returns True if
# n is even, False otherwise. Test it with n = 14.

# YOUR CODE HERE


# SOLUTION:
# def is_even(n):
#     return n % 2 == 0
#
# print(is_even(14))  # Expected: True

print("-" * 50)

# ── Problem A2 — 🟢 Warm-up ──
# Create a dictionary (Day 6) representing a student:
# {"name": "Anika", "marks": [88, 76, 92]}. Print the average of marks.

# YOUR CODE HERE


# SOLUTION:
# student = {"name": "Anika", "marks": [88, 76, 92]}
# average = sum(student["marks"]) / len(student["marks"])
# print(f"{student['name']}'s average: {average:.2f}")  # Expected: 85.33

print("-" * 50)

# ── Problem A3 — 🟡 Core ──
# Using try/except (Day 9), write code that attempts to convert the
# string "abc123" to an integer and prints a friendly error message if
# it fails, instead of crashing.

# YOUR CODE HERE


# SOLUTION:
# raw_value = "abc123"
# try:
#     converted = int(raw_value)
#     print(f"Converted value: {converted}")
# except ValueError:
#     print(f"Could not convert '{raw_value}' to an integer.")

print("-" * 50)

print("=" * 60)
print("SECTION B — IMPORT BASICS & ALIASING")
print("=" * 60)

# ── Problem B1 — 🟢 Warm-up ──
# Import the `math` module (already done above) and print the value of
# math.tau (tau = 2*pi).

# YOUR CODE HERE


# SOLUTION:
# print(math.tau)  # Expected: 6.283185307179586

print("-" * 50)

# ── Problem B2 — 🟢 Warm-up ──
# Use `from math import pow` to import only the pow function, then use
# it to calculate 5 raised to the power 3.

# YOUR CODE HERE


# SOLUTION:
# from math import pow
# result = pow(5, 3)
# print(result)  # Expected: 125.0

print("-" * 50)

# ── Problem B3 — 🟡 Core ──
# Import the `random` module with the alias `rnd`. Generate a random
# integer between 1 and 100 (inclusive) and store it in `lucky_number`.
# Print "Your lucky number is: <lucky_number>".

# YOUR CODE HERE


# SOLUTION:
# import random as rnd
# lucky_number = rnd.randint(1, 100)
# print(f"Your lucky number is: {lucky_number}")

print("-" * 50)

# ── Problem B4 — 🟡 Core ──
# Import `datetime` with the alias `dt`. Create a date object for
# 26 January 2026 (Republic Day) and print it in the format
# "26-01-2026" using strftime.

# YOUR CODE HERE


# SOLUTION:
# import datetime as dt
# republic_day = dt.date(2026, 1, 26)
# print(republic_day.strftime("%d-%m-%Y"))  # Expected: 26-01-2026

print("-" * 50)

# ── Problem B5 — 🔴 Challenge ──
# Using `from math import sqrt, pow as power`, write a function
# `hypotenuse(a, b)` that returns the length of the hypotenuse of a
# right triangle with legs a and b, using sqrt and power (NOT a**2).
# Test with a=6, b=8.

# YOUR CODE HERE


# SOLUTION:
# from math import sqrt, pow as power
#
# def hypotenuse(a, b):
#     return sqrt(power(a, 2) + power(b, 2))
#
# print(hypotenuse(6, 8))  # Expected: 10.0

print("-" * 50)

# ── Problem B6 — 🔴 Challenge ──
# A teammate wrote: `from os import *` at the top of their file and
# now their own variable named `path` keeps disappearing/behaving
# strangely. Without writing import * yourself, write 2-3 lines of
# comments explaining WHY this happens and how to fix their import.

# YOUR CODE HERE


# SOLUTION:
# # `from os import *` pulls every public name from the os module into
# # the current namespace, including a name like `path` (os.path module).
# # This silently overwrites the teammate's own `path` variable.
# # Fix: use `import os` and access it as `os.path`, or import only the
# # specific names needed, e.g. `from os import getcwd`.

print("-" * 50)

print("=" * 60)
print("Section A: 3 problems | Section B: 6 problems | Total: 9")
print("Next file: day12_practise_problems_02_main_guard.py")
print("=" * 60)

if __name__ == "__main__":
    print("\nDay 12 Practice — File 1 (Imports & Packages) complete!")
