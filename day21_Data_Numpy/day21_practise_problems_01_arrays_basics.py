"""
Day 21 — Practice Problems (File 1 of 3)
Topic: Prior Days Review + NumPy Array Basics

Cumulative Scope: Days 1-21 (functions, OOP, file I/O, error handling,
decorators, type hints, context managers, and now NumPy fundamentals)

Difficulty Legend:
    🟢 Warm-up   — quick recall / direct application
    🟡 Core      — combines 2-3 ideas, needs some thought
    🔴 Challenge — multi-step reasoning or edge cases

Section Index (this file):
    Section A — Prior Days Review (context managers, type hints, closures)
    Section B — NumPy Array Creation
    Section C — Array Attributes & Vectorized Operations

(See day21_practise_problems_02_broadcasting_indexing.py and
day21_practise_problems_03_linalg_mixed.py for the remaining sections.)

How to run:
    python day21_practise_problems_01_arrays_basics.py
"""

import numpy as np
from contextlib import contextmanager

# ════════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════════════

# Problem A1 🟢 Warm-up
# Write a context manager (using @contextmanager) called
# `swiggy_order_session` that prints "Order session started" on enter
# and "Order session closed" on exit.
# Then use it in a `with` block and print "Placing order..." inside.
#
# Expected output:
#   Order session started
#   Placing order...
#   Order session closed

# YOUR CODE HERE


# SOLUTION:
# @contextmanager
# def swiggy_order_session():
#     print("Order session started")
#     yield
#     print("Order session closed")
#
# with swiggy_order_session():
#     print("Placing order...")

print("-" * 50)

# Problem A2 🟢 Warm-up
# Write a function `add_gst(amount: float) -> float` with type hints
# that adds 18% GST to `amount` and returns the result rounded to 2
# decimal places. Call it with amount=1000 and print the result.
#
# Expected output:
#   1180.0

# YOUR CODE HERE


# SOLUTION:
# def add_gst(amount: float) -> float:
#     return round(amount * 1.18, 2)
#
# print(add_gst(1000))

print("-" * 50)

# Problem A3 🟡 Core
# Write a decorator `log_call` that prints "Calling <function name>"
# before running the wrapped function, then runs it normally. Use
# `functools.wraps` to preserve the function's metadata. Apply it to
# a function `book_irctc_ticket()` that prints "Ticket booked!" and
# call the decorated function.
#
# Expected output:
#   Calling book_irctc_ticket
#   Ticket booked!

# YOUR CODE HERE


# SOLUTION:
# from functools import wraps
#
# def log_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_call
# def book_irctc_ticket():
#     print("Ticket booked!")
#
# book_irctc_ticket()

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION B — NumPy Array Creation
# ════════════════════════════════════════════════════════════════

# Problem B1 🟢 Warm-up
# Create a NumPy array `flipkart_cart` from the Python list
# [499, 1299, 250, 899] and print it along with its type.
#
# Expected output:
#   [ 499 1299  250  899]
#   <class 'numpy.ndarray'>

# YOUR CODE HERE
flipkart_cart_list = [499, 1299, 250, 899]

# SOLUTION:
# flipkart_cart = np.array(flipkart_cart_list)
# print(flipkart_cart)
# print(type(flipkart_cart))

print("-" * 50)

# Problem B2 🟢 Warm-up
# Use np.arange() to create an array of all odd numbers from 1 to 19
# (inclusive). Print it.
#
# Expected output:
#   [ 1  3  5  7  9 11 13 15 17 19]

# YOUR CODE HERE


# SOLUTION:
# odd_numbers = np.arange(1, 20, 2)
# print(odd_numbers)

print("-" * 50)

# Problem B3 🟡 Core
# Use np.linspace() to create 5 evenly spaced "loyalty tier" thresholds
# between 0 and 10000 rupees (inclusive of both ends). Print the array
# rounded to 0 decimal places using np.round().
#
# Expected output:
#   [    0.  2500.  5000.  7500. 10000.]

# YOUR CODE HERE


# SOLUTION:
# tiers = np.linspace(0, 10000, 5)
# print(np.round(tiers, 0))

print("-" * 50)

# Problem B4 🟡 Core
# Create a 3x3 array of zeros representing an empty IRCTC seat map
# for a small coach (using np.zeros with a shape tuple), then set the
# middle element (row 1, col 1) to 1 to mark it booked. Print the
# final array.
#
# Expected output:
#   [[0. 0. 0.]
#    [0. 1. 0.]
#    [0. 0. 0.]]

# YOUR CODE HERE


# SOLUTION:
# seat_map = np.zeros((3, 3))
# seat_map[1, 1] = 1
# print(seat_map)

print("-" * 50)

# Problem B5 🔴 Challenge
# Riya wants an array of the first 10 multiples of 7 (7, 14, 21, ...70)
# created WITHOUT using np.arange's step argument directly for
# multiples — instead, use np.arange(1, 11) and multiply it by 7
# (vectorized operation). Print the result.
#
# Expected output:
#   [ 7 14 21 28 35 42 49 56 63 70]

# YOUR CODE HERE


# SOLUTION:
# multiples_of_7 = np.arange(1, 11) * 7
# print(multiples_of_7)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION C — Array Attributes & Vectorized Operations
# ════════════════════════════════════════════════════════════════

# Problem C1 🟢 Warm-up
# Given `bigbasket_matrix = np.array([[1,2,3],[4,5,6]])`, print its
# shape, ndim, and size.
#
# Expected output:
#   Shape: (2, 3)
#   Ndim: 2
#   Size: 6

bigbasket_matrix = np.array([[1, 2, 3], [4, 5, 6]])

# YOUR CODE HERE


# SOLUTION:
# print("Shape:", bigbasket_matrix.shape)
# print("Ndim:", bigbasket_matrix.ndim)
# print("Size:", bigbasket_matrix.size)

print("-" * 50)

# Problem C2 🟡 Core
# Sanjay has an array of monthly rents (in rupees) across 4 months:
# rents = np.array([12000, 12000, 12500, 13000]). Compute and print
# the total paid, the average rent, and the increase from the first
# to the last month.
#
# Expected output:
#   Total: 49500
#   Average: 12375.0
#   Increase: 1000

rents = np.array([12000, 12000, 12500, 13000])

# YOUR CODE HERE


# SOLUTION:
# total = rents.sum()
# average = rents.mean()
# increase = rents[-1] - rents[0]
# print("Total:", total)
# print("Average:", average)
# print("Increase:", increase)

print("-" * 50)

# Problem C3 🟡 Core
# Meera has Paytm cashback amounts: cashback = np.array([10, 25, 5, 40, 15]).
# Create a boolean array for cashback amounts greater than or equal to 15,
# then use it to print only the qualifying cashback values.
#
# Expected output:
#   Qualifying mask: [False  True False  True  True]
#   Qualifying cashback: [25 40 15]

cashback = np.array([10, 25, 5, 40, 15])

# YOUR CODE HERE


# SOLUTION:
# qualifying_mask = cashback >= 15
# qualifying_cashback = cashback[qualifying_mask]
# print("Qualifying mask:", qualifying_mask)
# print("Qualifying cashback:", qualifying_cashback)

print("-" * 50)

# Problem C4 🔴 Challenge
# Arjun tracks daily Zomato delivery times (minutes) for a week:
# times = np.array([32, 45, 28, 55, 40, 60, 35])
# Compute: (a) the average delivery time rounded to 1 decimal, (b) how
# many days had a delivery time over 40 minutes, and (c) the fastest
# and slowest delivery times as a tuple (fastest, slowest).
#
# Expected output:
#   Average: 42.1
#   Days over 40 min: 3
#   Fastest/Slowest: (28, 60)

times = np.array([32, 45, 28, 55, 40, 60, 35])

# YOUR CODE HERE


# SOLUTION:
# average_time = round(times.mean(), 1)
# days_over_40 = (times > 40).sum()
# fastest_slowest = (int(times.min()), int(times.max()))
# print("Average:", average_time)
# print("Days over 40 min:", days_over_40)
# print("Fastest/Slowest:", fastest_slowest)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY (File 1 of 3)
# ════════════════════════════════════════════════════════════════
# Sections in this file:
#   A — Prior Days Review          (3 problems: 2 warm-up, 1 core)
#   B — NumPy Array Creation       (5 problems: 2 warm-up, 2 core, 1 challenge)
#   C — Attributes & Vectorized Ops (4 problems: 1 warm-up, 2 core, 1 challenge)
#
# Total this file: 12 problems
#
# Continue with:
#   day21_practise_problems_02_broadcasting_indexing.py (Section D)
#   day21_practise_problems_03_linalg_mixed.py (Section E, F — Mixed Challenges)

if __name__ == "__main__":
    print("Day 21 Practice — File 1 complete.")
