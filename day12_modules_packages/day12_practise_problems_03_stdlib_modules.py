"""
Day 12 — Practice Problems (File 3 of 3)
==========================================

Topic         : Standard library modules + Mixed Challenges
Cumulative    : Days 1-12 (full course so far)
Difficulty    : 🟢 Warm-up | 🟡 Core | 🔴 Challenge
Section Index :
    D — Standard Library Modules (os, sys, math, datetime, pathlib)
    E — Mixed Challenges (Day 12 + all prior days)

Run with: python day12_practise_problems_03_stdlib_modules.py
All input() calls are simulated using pre-assigned variables.
"""

import os
import sys
import math
import datetime
from pathlib import Path

print("=" * 60)
print("SECTION D — STANDARD LIBRARY MODULES")
print("=" * 60)

# ── Problem D1 — 🟢 Warm-up ──
# Print the current working directory using the `os` module.

# YOUR CODE HERE


# SOLUTION:
# print(os.getcwd())

print("-" * 50)

# ── Problem D2 — 🟢 Warm-up ──
# Using `math`, print the ceiling and floor of 19.3.

# YOUR CODE HERE


# SOLUTION:
# print(math.ceil(19.3), math.floor(19.3))  # Expected: 20 19

print("-" * 50)

# ── Problem D3 — 🟡 Core ──
# Use `pathlib.Path` to build a path that joins the current working
# directory with a folder called "invoices" and a file called
# "march_invoice.pdf". Print the full path and print just its `.name`.

# YOUR CODE HERE


# SOLUTION:
# invoice_path = Path(os.getcwd()) / "invoices" / "march_invoice.pdf"
# print(invoice_path)
# print(invoice_path.name)  # Expected: march_invoice.pdf

print("-" * 50)

# ── Problem D4 — 🟡 Core ──
# Using `datetime`, calculate how many days are between
# 1 January 2026 and 30 June 2026 (today). Print the result.

# YOUR CODE HERE


# SOLUTION:
# new_year = datetime.date(2026, 1, 1)
# today = datetime.date(2026, 6, 30)
# difference = (today - new_year).days
# print(difference)  # Expected: 180

print("-" * 50)

# ── Problem D5 — 🟡 Core ──
# Use `sys.platform` to print which platform the script is running on,
# and use an if/elif/else (Day 3) to print a friendly OS name:
# "linux" -> "Linux", "darwin" -> "macOS", "win32" -> "Windows",
# else -> "Unknown OS".

# YOUR CODE HERE


# SOLUTION:
# platform_code = sys.platform
# if platform_code == "linux":
#     friendly_name = "Linux"
# elif platform_code == "darwin":
#     friendly_name = "macOS"
# elif platform_code == "win32":
#     friendly_name = "Windows"
# else:
#     friendly_name = "Unknown OS"
# print(friendly_name)

print("-" * 50)

# ── Problem D6 — 🔴 Challenge ──
# Write a function `next_weekday(date_obj)` that returns the next
# Monday on or after the given date, using `datetime.timedelta`.
# Hint: date_obj.weekday() returns 0 for Monday ... 6 for Sunday.
# Test with date_obj = datetime.date(2026, 7, 2) (a Thursday).

# YOUR CODE HERE


# SOLUTION:
# def next_weekday(date_obj, target_weekday=0):
#     days_ahead = target_weekday - date_obj.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return date_obj + datetime.timedelta(days=days_ahead)
#
# print(next_weekday(datetime.date(2026, 7, 2)))  # Expected: 2026-07-06

print("-" * 50)

print("=" * 60)
print("SECTION E — MIXED CHALLENGES (Day 12 + Prior Days)")
print("=" * 60)

# ── Problem E1 — 🔴 Challenge ──
# Build a small "delivery slip generator". Define a function
# `make_delivery_slip(customer, items, distance_km)` (Day 5: functions)
# that:
#   - Uses a dictionary (Day 6) to store item:price pairs for items =
#     {"Rice 5kg": 350, "Atta 5kg": 280, "Oil 1L": 180}
#   - Calculates subtotal using sum() and a loop or comprehension
#   - Adds delivery fare = math.ceil(distance_km) * 8
#   - Returns a formatted string with customer, subtotal, fare, and total
# Only print a demo call inside the `if __name__ == "__main__":` guard,
# using customer="Sanjay Verma", items as above, distance_km=6.7.

# YOUR CODE HERE


# SOLUTION:
# def make_delivery_slip(customer, items, distance_km):
#     subtotal = sum(items.values())
#     fare = math.ceil(distance_km) * 8
#     total = subtotal + fare
#     return (
#         f"Slip for {customer}: Subtotal Rs.{subtotal}, "
#         f"Delivery Rs.{fare}, Total Rs.{total}"
#     )
#
# if __name__ == "__main__":
#     sample_items = {"Rice 5kg": 350, "Atta 5kg": 280, "Oil 1L": 180}
#     print(make_delivery_slip("Sanjay Verma", sample_items, 6.7))
#     # Expected: Slip for Sanjay Verma: Subtotal Rs.810, Delivery Rs.56, Total Rs.866

print("-" * 50)

# ── Problem E2 — 🔴 Challenge ──
# Using try/except (Day 9), `pathlib` (Day 12), and a function (Day 5),
# write `safe_read_lines(path)` that:
#   - Tries to open and read all lines from the given Path
#   - Returns a list of stripped lines on success
#   - Catches FileNotFoundError and returns an empty list, printing
#     "File not found: <path>" instead of crashing
# Test it with a Path that does NOT exist, e.g.
# Path(os.getcwd()) / "does_not_exist.txt"

# YOUR CODE HERE


# SOLUTION:
# def safe_read_lines(path):
#     try:
#         with open(path, "r") as f:
#             return [line.strip() for line in f.readlines()]
#     except FileNotFoundError:
#         print(f"File not found: {path}")
#         return []
#
# if __name__ == "__main__":
#     missing_path = Path(os.getcwd()) / "does_not_exist.txt"
#     result = safe_read_lines(missing_path)
#     print(f"Lines read: {result}")  # Expected: [] (after the not-found message)

print("-" * 50)

# ── Problem E3 — 🔴 Challenge ──
# Combine OOP (Day 10-11), datetime, and math into a `Subscription`
# class with:
#   - __init__(self, plan_name, monthly_price, start_date)
#   - a method `months_active(self, as_of_date)` returning the number
#     of full months between start_date and as_of_date (use
#     (as_of_date.year - start_date.year) * 12 + (as_of_date.month -
#     start_date.month))
#   - a method `total_billed(self, as_of_date)` returning
#     monthly_price * months_active(as_of_date)
# Test with plan_name="Premium", monthly_price=499,
# start_date=datetime.date(2026,1,15), as_of_date=datetime.date(2026,6,30).

# YOUR CODE HERE


# SOLUTION:
# class Subscription:
#     def __init__(self, plan_name, monthly_price, start_date):
#         self.plan_name = plan_name
#         self.monthly_price = monthly_price
#         self.start_date = start_date
#
#     def months_active(self, as_of_date):
#         return ((as_of_date.year - self.start_date.year) * 12
#                  + (as_of_date.month - self.start_date.month))
#
#     def total_billed(self, as_of_date):
#         return self.monthly_price * self.months_active(as_of_date)
#
# if __name__ == "__main__":
#     sub = Subscription("Premium", 499, datetime.date(2026, 1, 15))
#     check_date = datetime.date(2026, 6, 30)
#     print(f"Months active: {sub.months_active(check_date)}")  # Expected: 5
#     print(f"Total billed: Rs.{sub.total_billed(check_date)}")  # Expected: Rs.2495

print("-" * 50)

# ── Problem E4 — 🔴 Challenge ──
# Write a function `project_file_report(folder_path)` that uses
# pathlib + a dict comprehension (Day 6) to count how many files of
# each extension exist directly inside folder_path (non-recursive).
# Return a dictionary like {".py": 3, ".txt": 1}. Test it on the
# current working directory.

# YOUR CODE HERE


# SOLUTION:
# def project_file_report(folder_path):
#     folder = Path(folder_path)
#     extensions = [f.suffix for f in folder.iterdir() if f.is_file() and f.suffix]
#     return {ext: extensions.count(ext) for ext in set(extensions)}
#
# if __name__ == "__main__":
#     report = project_file_report(os.getcwd())
#     print(report)

print("-" * 50)

print("=" * 60)
print("SUMMARY — Day 12 Practice Problems")
print("=" * 60)
print("Section A (Prior Days Review):     3 problems")
print("Section B (Import Basics):          6 problems")
print("Section C (__main__ Guard):         6 problems")
print("Section D (Standard Library):       6 problems")
print("Section E (Mixed Challenges):       4 problems")
print("TOTAL:                              25 problems across 3 files")
print()
print("Difficulty breakdown: 7x 🟢 Warm-up | 9x 🟡 Core | 9x 🔴 Challenge")
print()
print("Next session (Day 13) preview: Iterators & Generators — the")
print("__iter__/__next__ protocol, yield, generator expressions, and")
print("the itertools module (chain, islice, product, cycle).")
print("=" * 60)

if __name__ == "__main__":
    print("\nDay 12 Practice — File 3 (Standard Library + Mixed) complete!")
    print("Day 12 — Full Practice Problem Set complete!")
