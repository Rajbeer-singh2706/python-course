"""
Day 21 — Data & NumPy (Part 3 of 3)
Topic: np.linalg — Linear Algebra Basics

What this file covers:
    - Dot products (1D and 2D)
    - Matrix multiplication with @ and np.matmul
    - Transpose
    - Determinant with np.linalg.det
    - Matrix inverse with np.linalg.inv
    - Solving a system of linear equations with np.linalg.solve

Prerequisites:
    - day21_01_numpy_arrays_basics.py
    - day21_02_broadcasting_indexing.py

How to run:
    python day21_03_linalg_basics.py
"""

import numpy as np

# ════════════════════════════════════════════════════════════════
# SECTION 1: Dot Products
# ════════════════════════════════════════════════════════════════
# The dot product of two 1D arrays multiplies corresponding elements
# and sums the results. It's the mathematical foundation behind
# "weighted totals" — like a shopping bill.

# ── Concept: 1D dot product — bill calculation ──
item_quantities = np.array([3, 2, 5])            # 3 rice bags, 2 oil bottles, 5 soaps
item_prices = np.array([450, 180, 40])           # price per unit in rupees

total_bill = np.dot(item_quantities, item_prices)
print("Quantities:", item_quantities)
print("Prices:    ", item_prices)
print("Total bill (dot product):", total_bill)
# Output: Quantities: [3 2 5]
# Output: Prices:     [450 180  40]
# Output: Total bill (dot product): 1910

# The @ operator does exactly the same thing for dot products
total_bill_at_operator = item_quantities @ item_prices
print("Total bill using @:", total_bill_at_operator)
# Output: Total bill using @: 1910

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: Matrix Multiplication
# ════════════════════════════════════════════════════════════════
# For 2D arrays, @ performs true matrix multiplication (not element-wise).
# Rule: (m x n) @ (n x p) -> (m x p). Inner dimensions must match.

# 3 IRCTC routes, quantities of 2 ticket classes purchased (Sleeper, AC3)
tickets_purchased = np.array([
    [4, 2],   # Route 1: 4 Sleeper, 2 AC3
    [1, 5],   # Route 2: 1 Sleeper, 5 AC3
    [3, 3],   # Route 3: 3 Sleeper, 3 AC3
])

# Price per class: Sleeper = Rs 450, AC3 = Rs 1200 (as a column vector)
class_prices = np.array([[450], [1200]])

route_totals = tickets_purchased @ class_prices
print("Tickets purchased (rows=routes, cols=[Sleeper, AC3]):\n", tickets_purchased)
print("Class prices (column vector):\n", class_prices)
print("Total cost per route:\n", route_totals)
# Output: Tickets purchased (rows=routes, cols=[Sleeper, AC3]):
#  [[4 2]
#  [1 5]
#  [3 3]]
# Output: Class prices (column vector):
#  [[ 450]
#  [1200]]
# Output: Total cost per route:
#  [[4200]
#  [6450]
#  [4950]]

print("-" * 50)

# ── Concept: np.matmul() is equivalent to @ for 2D arrays ──
alt_totals = np.matmul(tickets_purchased, class_prices)
print("Same result using np.matmul:\n", alt_totals)
print("Are they equal?", np.array_equal(route_totals, alt_totals))
# Output: Same result using np.matmul:
#  [[4200]
#  [6450]
#  [4950]]
# Output: Are they equal? True

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: Transpose
# ════════════════════════════════════════════════════════════════
# Transpose flips rows and columns: shape (m, n) becomes (n, m).
# Use `.T` or np.transpose().

print("Original tickets_purchased (3x2):\n", tickets_purchased)
print("Transposed (2x3):\n", tickets_purchased.T)
# Output: Original tickets_purchased (3x2):
#  [[4 2]
#  [1 5]
#  [3 3]]
# Output: Transposed (2x3):
#  [[4 1 3]
#  [2 5 3]]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 4: Determinant
# ════════════════════════════════════════════════════════════════
# The determinant is a single scalar that describes properties of a
# SQUARE matrix — for example, whether it can be inverted (det != 0
# means invertible).

# A 2x2 "conversion matrix" for two Flipkart warehouses' stock ratios
warehouse_matrix = np.array([
    [4.0, 2.0],
    [1.0, 3.0],
])

det_value = np.linalg.det(warehouse_matrix)
print("Warehouse matrix:\n", warehouse_matrix)
print(f"Determinant: {det_value:.2f}")
# Output: Warehouse matrix:
#  [[4. 2.]
#  [1. 3.]]
# Output: Determinant: 10.00

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 5: Matrix Inverse
# ════════════════════════════════════════════════════════════════
# The inverse of matrix A (written A^-1) satisfies A @ A^-1 = Identity.
# Only square matrices with a non-zero determinant have an inverse.

inverse_matrix = np.linalg.inv(warehouse_matrix)
print("Inverse of warehouse matrix:\n", np.round(inverse_matrix, 3))
# Output: Inverse of warehouse matrix:
#  [[ 0.3 -0.2]
#  [-0.1  0.4]]

# Verify: A @ A_inverse should give (approximately) the identity matrix
identity_check = warehouse_matrix @ inverse_matrix
print("A @ A_inverse (should be identity):\n", np.round(identity_check, 3))
# Output: A @ A_inverse (should be identity):
#  [[ 1.  0.]
#  [-0.  1.]]
# (the -0. is a harmless floating-point rounding artifact)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 6: Solving Systems of Linear Equations
# ════════════════════════════════════════════════════════════════
# np.linalg.solve(A, b) solves the equation A @ x = b for x, without
# manually computing the inverse (which is faster and more numerically
# stable).
#
# Real-world example: Meera bought a mix of two BigBasket combo packs.
#   Combo A has 2 kg rice + 1 kg dal.
#   Combo B has 1 kg rice + 3 kg dal.
#   She ended up with 8 kg rice total and 9 kg dal total.
#   How many of each combo did she buy?
#
#   2*a + 1*b = 8   (rice)
#   1*a + 3*b = 9   (dal)

coefficients = np.array([
    [2, 1],
    [1, 3],
])
totals = np.array([8, 9])

combo_counts = np.linalg.solve(coefficients, totals)
print("Coefficient matrix:\n", coefficients)
print("Totals vector:", totals)
print("Solved combo counts [A, B]:", np.round(combo_counts, 2))
# Output: Coefficient matrix:
#  [[2 1]
#  [1 3]]
# Output: Totals vector: [8 9]
# Output: Solved combo counts [A, B]: [3. 2.]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 1: Priya's bakery — dot product for total cost
# ════════════════════════════════════════════════════════════════
ingredient_amounts = np.array([2.5, 1.0, 0.5])       # kg of flour, sugar, butter
ingredient_cost_per_kg = np.array([45, 60, 400])     # rupees per kg

total_ingredient_cost = ingredient_amounts @ ingredient_cost_per_kg
print("Priya Sharma's bakery — total ingredient cost")
print("Amounts (kg):  ", ingredient_amounts)
print("Cost per kg:   ", ingredient_cost_per_kg)
print(f"Total cost: Rs {total_ingredient_cost:.2f}")
# Output:
# Priya Sharma's bakery — total ingredient cost
# Amounts (kg):   [2.5 1.  0.5]
# Cost per kg:    [ 45  60 400]
# Total cost: Rs 372.50

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 2: Arjun's investment portfolio — matrix multiply
# ════════════════════════════════════════════════════════════════
# 2 portfolios x 3 stocks (number of shares held)
shares_held = np.array([
    [10, 5, 8],    # Portfolio 1
    [3, 12, 2],    # Portfolio 2
])
# Share price for each of the 3 stocks (column vector)
share_prices = np.array([[1500], [800], [2200]])

portfolio_values = shares_held @ share_prices
print("Arjun Mehta's portfolio valuation")
print("Shares held:\n", shares_held)
print("Share prices:\n", share_prices)
print("Portfolio values:\n", portfolio_values)
# Output:
# Arjun Mehta's portfolio valuation
# Shares held:
#  [[10  5  8]
#  [ 3 12  2]]
# Share prices:
#  [[1500]
#  [ 800]
#  [2200]]
# Portfolio values:
#  [[36600]
#  [18500]]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 3: Riya's transport network — transpose
# ════════════════════════════════════════════════════════════════
# Rows = 2 depots, Columns = 3 delivery zones (packages routed)
routing_matrix = np.array([
    [12, 8, 5],
    [4, 15, 9],
])
print("Riya Deshmukh's routing matrix (depots x zones):\n", routing_matrix)
print("Transposed (zones x depots):\n", routing_matrix.T)
# Output:
# Riya Deshmukh's routing matrix (depots x zones):
#  [[12  8  5]
#  [ 4 15  9]]
# Transposed (zones x depots):
#  [[12  4]
#  [ 8 15]
#  [ 5  9]]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 4: Sanjay's ration shop — solving equations
# ════════════════════════════════════════════════════════════════
# Sanjay sells two ration kits:
#   Kit X: 3 kg rice + 2 kg wheat
#   Kit Y: 1 kg rice + 4 kg wheat
# Total sold in a day: 25 kg rice, 38 kg wheat. How many of each kit?
#   3x + 1y = 25
#   2x + 4y = 38

kit_coefficients = np.array([
    [3, 1],
    [2, 4],
])
kit_totals = np.array([25, 38])
kits_sold = np.linalg.solve(kit_coefficients, kit_totals)
print("Sanjay Verma's ration shop — kits sold")
print("Coefficients:\n", kit_coefficients)
print("Totals:", kit_totals)
print("Kits sold [X, Y]:", np.round(kits_sold, 2))
# Output:
# Sanjay Verma's ration shop — kits sold
# Coefficients:
#  [[3 1]
#  [2 4]]
# Totals: [25 38]
# Kits sold [X, Y]: [6.2 6.4]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Meera Iyer is comparing two Paytm cashback plans using a system of
# equations. She knows:
#   3 transactions on Plan A + 2 transactions on Plan B = Rs 190 cashback
#   1 transaction on Plan A + 4 transactions on Plan B = Rs 140 cashback
#
# Tasks:
#   1. Build the coefficient matrix and totals vector as NumPy arrays.
#   2. Use np.linalg.solve() to find the cashback per transaction for
#      Plan A and Plan B.
#   3. Print the determinant of the coefficient matrix first, to check
#      the system is solvable (non-zero determinant).
#
# Expected output:
#   Determinant: 10.00
#   Cashback per transaction [A, B]: [42. 32.]

# YOUR CODE HERE
plan_coefficients = np.array([[3, 2], [1, 4]])
plan_totals = np.array([190, 140])

# SOLUTION:
# det_val = np.linalg.det(plan_coefficients)
# cashback_per_transaction = np.linalg.solve(plan_coefficients, plan_totals)
# print(f"Determinant: {det_val:.2f}")
# print("Cashback per transaction [A, B]:", np.round(cashback_per_transaction, 2))

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file you learned:
#   - Dot products with np.dot() and the @ operator
#   - True matrix multiplication with @ / np.matmul()
#   - Transpose with .T
#   - Determinant with np.linalg.det()
#   - Matrix inverse with np.linalg.inv()
#   - Solving linear systems with np.linalg.solve()
#
# This wraps up Day 21 concept files. Next: the Day 21 practice
# problem set (day21_practise_problems_*.py), then Day 22 moves on
# to Pandas DataFrames and Series, built directly on these NumPy
# foundations.

if __name__ == "__main__":
    print("Day 21, Part 3 complete: NumPy Linear Algebra Basics.")
