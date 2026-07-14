"""
Day 21 — Practice Problems (File 3 of 3)
Topic: Linear Algebra + Mixed Challenges

Cumulative Scope: Days 1-21 (this file combines NumPy linear algebra
with prior concepts: OOP, error handling, decorators, type hints)

Difficulty Legend:
    🟢 Warm-up   — quick recall / direct application
    🟡 Core      — combines 2-3 ideas, needs some thought
    🔴 Challenge — multi-step reasoning or edge cases

Section Index (this file):
    Section E — Linear Algebra (5 problems)
    Section F — Mixed Challenges (4 problems)

(See day21_practise_problems_01_arrays_basics.py for Sections A-C, and
day21_practise_problems_02_broadcasting_indexing.py for Section D.)

How to run:
    python day21_practise_problems_03_linalg_mixed.py
"""

import numpy as np

# ════════════════════════════════════════════════════════════════
# SECTION E — Linear Algebra
# ════════════════════════════════════════════════════════════════

# Problem E1 🟢 Warm-up
# Compute the dot product of `quantities = np.array([4, 1, 2])` and
# `prices = np.array([25, 500, 150])` using np.dot(). Print the result.
#
# Expected output:
#   Total: 900

quantities = np.array([4, 1, 2])
prices = np.array([25, 500, 150])

# YOUR CODE HERE


# SOLUTION:
# total = np.dot(quantities, prices)
# print("Total:", total)

print("-" * 50)

# Problem E2 🟡 Core
# Given `flipkart_qty = np.array([[3, 1], [2, 4]])` (2 orders x 2
# products) and `unit_prices = np.array([[200], [50]])` (column
# vector), compute the total cost per order using matrix
# multiplication (@). Print the result.
#
# Expected output:
#   [[650]
#    [600]]

flipkart_qty = np.array([[3, 1], [2, 4]])
unit_prices = np.array([[200], [50]])

# YOUR CODE HERE


# SOLUTION:
# order_totals = flipkart_qty @ unit_prices
# print(order_totals)

print("-" * 50)

# Problem E3 🟢 Warm-up
# Print the transpose of `routes = np.array([[1, 2, 3], [4, 5, 6]])`.
#
# Expected output:
#   [[1 4]
#    [2 5]
#    [3 6]]

routes = np.array([[1, 2, 3], [4, 5, 6]])

# YOUR CODE HERE


# SOLUTION:
# print(routes.T)

print("-" * 50)

# Problem E4 🟡 Core
# Compute the determinant of `matrix_a = np.array([[6, 2], [3, 4]])`
# using np.linalg.det(), and print it rounded to 2 decimal places.
# Then check whether the matrix is invertible (determinant != 0) and
# print "Invertible" or "Not invertible" accordingly.
#
# Expected output:
#   Determinant: 18.00
#   Invertible

matrix_a = np.array([[6, 2], [3, 4]])

# YOUR CODE HERE


# SOLUTION:
# det_a = np.linalg.det(matrix_a)
# print(f"Determinant: {det_a:.2f}")
# print("Invertible" if det_a != 0 else "Not invertible")

print("-" * 50)

# Problem E5 🔴 Challenge
# Meera splits her Rs 15000 monthly budget between two BigBasket combo
# subscriptions, buying some combination of Plan A and Plan B boxes:
#   2 * (Plan A count) + 3 * (Plan B count) = 26  (total boxes weighted)
#   1 * (Plan A count) + 1 * (Plan B count) = 10  (total boxes)
# Use np.linalg.solve() to find how many of each plan she bought.
# Print the result rounded to 0 decimal places.
#
# Expected output:
#   Plan counts [A, B]: [4. 6.]

coeffs = np.array([[2, 3], [1, 1]])
totals = np.array([26, 10])

# YOUR CODE HERE


# SOLUTION:
# plan_counts = np.linalg.solve(coeffs, totals)
# print("Plan counts [A, B]:", np.round(plan_counts, 0))

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION F — Mixed Challenges (combines Day 21 + prior days)
# ════════════════════════════════════════════════════════════════

# Problem F1 🔴 Challenge
# Write a custom exception `InvalidOrderError` (Day 9). Then write a
# function `validate_order(quantities: np.ndarray) -> np.ndarray`
# (Day 18 type hints) that raises `InvalidOrderError` if any quantity
# is negative (use `(quantities < 0).any()`), otherwise returns the
# array unchanged. Test it with
# `test_order = np.array([2, 5, -1, 3])` inside a try/except block
# and print the caught error message: "Invalid order: negative
# quantity detected".
#
# Expected output:
#   Invalid order: negative quantity detected

test_order = np.array([2, 5, -1, 3])

# YOUR CODE HERE


# SOLUTION:
# class InvalidOrderError(Exception):
#     pass
#
# def validate_order(quantities: np.ndarray) -> np.ndarray:
#     if (quantities < 0).any():
#         raise InvalidOrderError("Invalid order: negative quantity detected")
#     return quantities
#
# try:
#     validate_order(test_order)
# except InvalidOrderError as e:
#     print(e)

print("-" * 50)

# Problem F2 🔴 Challenge
# Define a class `DeliveryFleet` (Day 10/11 OOP) with an `__init__`
# that stores a NumPy array of distances (km) traveled by each of its
# vehicles, and a method `total_fuel_cost(rate_per_km: float) -> float`
# that returns the total fuel cost (vectorized: distances.sum() * rate).
# Create an instance with distances = np.array([120, 85, 200, 60]) and
# print the total fuel cost at Rs 8.5 per km, rounded to 2 decimals.
#
# Expected output:
#   Total fuel cost: Rs 3952.50

# YOUR CODE HERE


# SOLUTION:
# class DeliveryFleet:
#     def __init__(self, distances: np.ndarray) -> None:
#         self.distances = distances
#
#     def total_fuel_cost(self, rate_per_km: float) -> float:
#         return round(float(self.distances.sum()) * rate_per_km, 2)
#
# fleet = DeliveryFleet(np.array([120, 85, 200, 60]))
# print(f"Total fuel cost: Rs {fleet.total_fuel_cost(8.5):.2f}")

print("-" * 50)

# Problem F3 🔴 Challenge
# Write a decorator `time_it` (Day 14 closures/decorators) that prints
# how long a function took to run using `time.perf_counter()`, in the
# format "Ran in X.Xs" (rounded to 4 decimals is fine for demonstration,
# but only print the label — since actual runtime varies, we only
# check the label appears). Apply it to a function
# `compute_large_dot_product()` that computes the dot product of two
# NumPy arrays of 100,000 random-like sequential integers
# (np.arange(100000)) with itself, and prints the result.
#
# Expected output (timing value will vary machine to machine):
#   Dot product result: 333328333350000
#   Ran in <some time>s

import time
from functools import wraps

# YOUR CODE HERE


# SOLUTION:
# def time_it(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         elapsed = time.perf_counter() - start
#         print(f"Ran in {elapsed:.4f}s")
#         return result
#     return wrapper
#
# @time_it
# def compute_large_dot_product():
#     arr = np.arange(100000)
#     result = int(np.dot(arr, arr))
#     print("Dot product result:", result)
#     return result
#
# compute_large_dot_product()

print("-" * 50)

# Problem F4 🔴 Challenge (Capstone-style, ties into upcoming Pandas day)
# Priya's bakery tracks daily sales for 3 items across a 5-day week as
# a 2D array (rows=items, columns=days):
#   sales = np.array([[500, 600, 450, 700, 650],   # Cakes
#                     [200, 250, 180, 300, 220],    # Pastries
#                     [900, 850, 950, 1000, 970]])  # Bread
# Using only NumPy (no loops):
#   1. Compute total sales per item (row-wise sum, axis=1).
#   2. Compute total sales per day (column-wise sum, axis=0).
#   3. Find which item had the highest total sales (print its row
#      index using np.argmax()).
#
# Expected output:
#   Per-item totals: [2900 1150 4670]
#   Per-day totals: [1600 1700 1580 2000 1840]
#   Highest-selling item index: 2

sales = np.array([
    [500, 600, 450, 700, 650],
    [200, 250, 180, 300, 220],
    [900, 850, 950, 1000, 970],
])

# YOUR CODE HERE


# SOLUTION:
# per_item_totals = sales.sum(axis=1)
# per_day_totals = sales.sum(axis=0)
# highest_item_index = np.argmax(per_item_totals)
# print("Per-item totals:", per_item_totals)
# print("Per-day totals:", per_day_totals)
# print("Highest-selling item index:", highest_item_index)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY — Day 21 Practice Problem Set (Complete)
# ════════════════════════════════════════════════════════════════
# Section A — Prior Days Review         : 3 problems
# Section B — Array Creation            : 5 problems
# Section C — Attributes & Vectorized Ops: 4 problems
# Section D — Broadcasting & Indexing    : 7 problems
# Section E — Linear Algebra             : 5 problems
# Section F — Mixed Challenges           : 4 problems
#
# TOTAL: 28 problems across 3 files
# Difficulty breakdown: 8 Warm-up, 12 Core, 8 Challenge
#
# Next up: Day 22 — Data & Pandas
#   - DataFrame and Series objects
#   - read_csv() / to_csv()
#   - groupby() aggregations
#   - merge() and join()
#   - Basic plotting with df.plot()
#
# Pandas is built directly on top of NumPy arrays, so everything
# learned in Day 21 (vectorization, broadcasting, boolean masking)
# transfers directly into DataFrame operations.

if __name__ == "__main__":
    print("Day 21 Practice — File 3 complete. Full problem set done!")
