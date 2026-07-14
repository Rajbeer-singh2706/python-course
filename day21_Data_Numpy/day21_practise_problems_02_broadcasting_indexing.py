"""
Day 21 — Practice Problems (File 2 of 3)
Topic: Broadcasting & Indexing

Cumulative Scope: Days 1-21

Difficulty Legend:
    🟢 Warm-up   — quick recall / direct application
    🟡 Core      — combines 2-3 ideas, needs some thought
    🔴 Challenge — multi-step reasoning or edge cases

Section Index (this file):
    Section D — Broadcasting & Indexing (7 problems)

(See day21_practise_problems_01_arrays_basics.py for Sections A-C, and
day21_practise_problems_03_linalg_mixed.py for Sections E-F.)

How to run:
    python day21_practise_problems_02_broadcasting_indexing.py
"""

import numpy as np

# ════════════════════════════════════════════════════════════════
# SECTION D — Broadcasting & Indexing
# ════════════════════════════════════════════════════════════════

# Problem D1 🟢 Warm-up
# Given `zomato_bills = np.array([250, 480, 690, 320])`, add a flat
# Rs 20 packaging fee to every bill using broadcasting, and print
# the result.
#
# Expected output:
#   [270 500 710 340]

zomato_bills = np.array([250, 480, 690, 320])

# YOUR CODE HERE


# SOLUTION:
# bills_with_fee = zomato_bills + 20
# print(bills_with_fee)

print("-" * 50)

# Problem D2 🟡 Core
# Given a 2D array `swiggy_sales` with shape (3, 4) — 3 restaurants,
# 4 weeks of sales — and a 1D array `weekly_bonus` of shape (4,),
# add the bonus to every restaurant's row using broadcasting.
#
# swiggy_sales = np.array([[100, 120, 90, 130],
#                          [80, 95, 70, 100],
#                          [150, 160, 140, 170]])
# weekly_bonus = np.array([5, 5, 10, 10])
#
# Expected output:
#   [[105 125 100 140]
#    [ 85 100  80 110]
#    [155 165 150 180]]

swiggy_sales = np.array([
    [100, 120, 90, 130],
    [80, 95, 70, 100],
    [150, 160, 140, 170],
])
weekly_bonus = np.array([5, 5, 10, 10])

# YOUR CODE HERE


# SOLUTION:
# sales_with_bonus = swiggy_sales + weekly_bonus
# print(sales_with_bonus)

print("-" * 50)

# Problem D3 🟡 Core
# Using the same `swiggy_sales` array, apply a PER-RESTAURANT discount
# using a column vector: discount = np.array([10, 0, 20]).reshape(-1, 1)
# Subtract it from every row and print the result.
#
# Expected output:
#   [[ 90 110  80 120]
#    [ 80  95  70 100]
#    [130 140 120 150]]

# YOUR CODE HERE


# SOLUTION:
# discount = np.array([10, 0, 20]).reshape(-1, 1)
# discounted_sales = swiggy_sales - discount
# print(discounted_sales)

print("-" * 50)

# Problem D4 🟢 Warm-up
# Given `irctc_seats = np.array([5, 12, 3, 20, 8, 15])`, use slicing
# to print the first 4 elements and then the last 2 elements.
#
# Expected output:
#   First 4: [ 5 12  3 20]
#   Last 2: [ 8 15]

irctc_seats = np.array([5, 12, 3, 20, 8, 15])

# YOUR CODE HERE


# SOLUTION:
# print("First 4:", irctc_seats[:4])
# print("Last 2:", irctc_seats[-2:])

print("-" * 50)

# Problem D5 🟡 Core
# Given a 2D fare matrix:
#   fares = np.array([[300, 800, 1500],
#                     [250, 700, 1300],
#                     [400, 900, 1700]])
# Print: (a) the element at row 2, column 1 (0-indexed), (b) the
# entire second row, (c) the entire last column.
#
# Expected output:
#   Element [2,1]: 900
#   Second row: [ 250  700 1300]
#   Last column: [1500 1300 1700]

fares = np.array([
    [300, 800, 1500],
    [250, 700, 1300],
    [400, 900, 1700],
])

# YOUR CODE HERE


# SOLUTION:
# print("Element [2,1]:", fares[2, 1])
# print("Second row:", fares[1, :])
# print("Last column:", fares[:, -1])

print("-" * 50)

# Problem D6 🔴 Challenge
# Given `paytm_txns = np.array([120, 4500, 60, 8900, 300, 15000, 45])`,
# use fancy indexing with a list of positions [1, 3, 5] to select the
# "big" transactions, then separately use boolean indexing to find ALL
# transactions above Rs 1000 (without hardcoding positions). Print both
# results, labeled.
#
# Expected output:
#   Fancy-indexed big txns: [ 4500  8900 15000]
#   Boolean-filtered big txns: [ 4500  8900 15000]

paytm_txns = np.array([120, 4500, 60, 8900, 300, 15000, 45])

# YOUR CODE HERE


# SOLUTION:
# fancy_selected = paytm_txns[[1, 3, 5]]
# boolean_selected = paytm_txns[paytm_txns > 1000]
# print("Fancy-indexed big txns:", fancy_selected)
# print("Boolean-filtered big txns:", boolean_selected)

print("-" * 50)

# Problem D7 🔴 Challenge
# Given a 2D array of BigBasket order quantities:
#   orders = np.array([[2, 0, 5], [1, 3, 0], [0, 0, 4]])
# Replace every 0 with the value -1 using boolean indexing (to mark
# "not ordered"), then print the modified array. Do this on a COPY so
# the original stays unchanged, and print the original afterward to
# prove it wasn't modified.
#
# Expected output:
#   Modified: [[ 2 -1  5]
#    [ 1  3 -1]
#    [-1 -1  4]]
#   Original unchanged: [[2 0 5]
#    [1 3 0]
#    [0 0 4]]

orders = np.array([[2, 0, 5], [1, 3, 0], [0, 0, 4]])

# YOUR CODE HERE


# SOLUTION:
# orders_copy = orders.copy()
# orders_copy[orders_copy == 0] = -1
# print("Modified:", orders_copy)
# print("Original unchanged:", orders)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY (File 2 of 3)
# ════════════════════════════════════════════════════════════════
# Section D — Broadcasting & Indexing (7 problems: 2 warm-up, 3 core, 2 challenge)
#
# Total this file: 7 problems
# Running total (Files 1-2): 19 problems
#
# Continue with:
#   day21_practise_problems_03_linalg_mixed.py (Section E — Linear
#   Algebra, Section F — Mixed Challenges)

if __name__ == "__main__":
    print("Day 21 Practice — File 2 complete.")
