"""
Day 21 — Data & NumPy (Part 2 of 3)
Topic: Broadcasting Rules, Array Slicing & Indexing

What this file covers:
    - Broadcasting: how NumPy applies operations across arrays of
      different shapes without explicit loops
    - The broadcasting compatibility rule
    - 1D and 2D slicing syntax
    - Fancy indexing (using arrays/lists of indices)
    - Boolean indexing on 2D arrays

Prerequisites:
    - day21_01_numpy_arrays_basics.py (array creation, vectorized ops)
    - Day 6 : slicing syntax on lists

How to run:
    python day21_02_broadcasting_indexing.py
"""

import numpy as np

# ════════════════════════════════════════════════════════════════
# SECTION 1: What Is Broadcasting?
# ════════════════════════════════════════════════════════════════
# Broadcasting lets NumPy perform operations on arrays of DIFFERENT
# shapes by "stretching" the smaller array across the larger one,
# without actually copying data. This is why `array * scalar` works
# even though a scalar has no shape at all.

# ── Concept: Scalar broadcasting (simplest case, seen already) ──
mumbai_local_fares = np.array([10, 15, 20, 25])
hiked_fares = mumbai_local_fares + 5   # 5 is "broadcast" to every element
print("Original fares:", mumbai_local_fares)
print("After Rs 5 hike:", hiked_fares)
# Output: Original fares: [10 15 20 25]
# Output: After Rs 5 hike: [15 20 25 30]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: The Broadcasting Rule
# ════════════════════════════════════════════════════════════════
# Two shapes are compatible for broadcasting when, comparing dimensions
# from the RIGHT, each pair of dimensions is either:
#   (a) equal, or
#   (b) one of them is 1 (it gets stretched to match the other)
#
# Example: shape (3, 4) and shape (4,) -> compatible, because the
# trailing dimension 4 matches 4. The (4,) array is treated as if it
# were repeated across all 3 rows.

# ── Concept: 2D array + 1D array (row-wise broadcasting) ──
# Rows = 3 Zomato restaurants, Columns = 4 weeks of orders
zomato_weekly_orders = np.array([
    [120, 135, 110, 140],   # Restaurant A
    [80,  95,  70,  100],   # Restaurant B
    [200, 210, 190, 220],   # Restaurant C
])

# A per-week platform fee (one value per week/column) applied to ALL rows
weekly_platform_fee = np.array([5, 5, 8, 8])

orders_after_fee = zomato_weekly_orders - weekly_platform_fee
print("Orders before fee:\n", zomato_weekly_orders)
print("Weekly fee:", weekly_platform_fee)
print("Orders after fee:\n", orders_after_fee)
# Output: Orders before fee:
#  [[120 135 110 140]
#  [ 80  95  70 100]
#  [200 210 190 220]]
# Output: Weekly fee: [5 5 8 8]
# Output: Orders after fee:
#  [[115 130 102 132]
#  [ 75  90  62  92]
#  [195 205 182 212]]

print("-" * 50)

# ── Concept: Column vector broadcasting ──
# A per-restaurant bonus (one value per row) applied across all columns.
# Note: reshape(-1, 1) turns a flat array into a column vector.
restaurant_bonus = np.array([10, 5, 20]).reshape(-1, 1)
orders_with_bonus = zomato_weekly_orders + restaurant_bonus
print("Restaurant bonus (column vector):\n", restaurant_bonus)
print("Orders with bonus added:\n", orders_with_bonus)
# Output: Restaurant bonus (column vector):
#  [[10]
#  [ 5]
#  [20]]
# Output: Orders with bonus added:
#  [[130 145 120 150]
#  [ 85 100  75 105]
#  [220 230 210 240]]

print("-" * 50)

# ── Concept: Incompatible shapes raise a ValueError ──
try:
    bad_array = np.array([1, 2, 3])          # shape (3,)
    mismatched = zomato_weekly_orders + bad_array  # needs shape (4,) or (3,1)
except ValueError as e:
    print(f"Broadcasting failed as expected: {e}")
# Output: Broadcasting failed as expected: operands could not be broadcast
# together with shapes (3,4) (3,)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: 1D Slicing (Recap + NumPy-specific behavior)
# ════════════════════════════════════════════════════════════════
swiggy_ratings_last_10_orders = np.array(
    [4.5, 3.8, 4.1, 5.0, 4.7, 2.9, 4.4, 4.8, 3.5, 4.0]
)

print("All ratings:", swiggy_ratings_last_10_orders)
print("First 3 ratings:", swiggy_ratings_last_10_orders[:3])
print("Last 3 ratings:", swiggy_ratings_last_10_orders[-3:])
print("Every 2nd rating:", swiggy_ratings_last_10_orders[::2])
print("Reversed:", swiggy_ratings_last_10_orders[::-1])
# Output: All ratings: [4.5 3.8 4.1 5.  4.7 2.9 4.4 4.8 3.5 4. ]
# Output: First 3 ratings: [4.5 3.8 4.1]
# Output: Last 3 ratings: [4.8 3.5 4. ]
# Output: Every 2nd rating: [4.5 4.1 4.7 4.4 3.5]
# Output: Reversed: [4.  3.5 4.8 4.4 2.9 4.7 5.  4.1 3.8 4.5]

# NOTE: A NumPy slice is a VIEW, not a copy! Modifying a slice modifies
# the original array — a key difference from ordinary Python lists.
ratings_view = swiggy_ratings_last_10_orders[:3]
ratings_view[0] = 1.0
print("After modifying the slice, original array:", swiggy_ratings_last_10_orders)
# Output: After modifying the slice, original array: [1.  3.8 4.1 5.  4.7 2.9 4.4 4.8 3.5 4. ]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 4: 2D Slicing & Indexing
# ════════════════════════════════════════════════════════════════
# For 2D arrays, index with array[row_selector, column_selector]

irctc_fare_matrix = np.array([
    #  Sleeper  AC3   AC2   AC1
    [   450,   1200, 1800, 2600],   # Delhi -> Mumbai
    [   380,   1050, 1600, 2300],   # Delhi -> Pune
    [   520,   1350, 2000, 2900],   # Delhi -> Bengaluru
])

print("Full fare matrix:\n", irctc_fare_matrix)

# Single element: row 0, column 2 (Delhi->Mumbai, AC2 fare)
print("Delhi->Mumbai AC2 fare:", irctc_fare_matrix[0, 2])
# Output: Delhi->Mumbai AC2 fare: 1800

# Entire row: all fares for Delhi -> Pune
print("Delhi->Pune all fares:", irctc_fare_matrix[1, :])
# Output: Delhi->Pune all fares: [ 380 1050 1600 2300]

# Entire column: Sleeper fares for all routes
print("All Sleeper fares:", irctc_fare_matrix[:, 0])
# Output: All Sleeper fares: [450 380 520]

# Sub-matrix: first two rows, last two columns (AC2 and AC1 fares)
print("AC2/AC1 fares for first 2 routes:\n", irctc_fare_matrix[:2, 2:])
# Output: AC2/AC1 fares for first 2 routes:
#  [[1800 2600]
#  [1600 2300]]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 5: Fancy Indexing
# ════════════════════════════════════════════════════════════════
# Fancy indexing means passing a LIST or ARRAY of indices, instead of
# a single index or slice. This always returns a COPY, not a view.

flipkart_order_ids = np.array([1001, 1002, 1003, 1004, 1005, 1006, 1007])

# Select specific, non-contiguous positions
selected_positions = [0, 2, 5]
print("Selected order IDs:", flipkart_order_ids[selected_positions])
# Output: Selected order IDs: [1001 1003 1006]

# Fancy indexing on a 2D array: pick specific rows
selected_routes = irctc_fare_matrix[[0, 2]]   # Delhi->Mumbai and Delhi->Bengaluru
print("Selected routes:\n", selected_routes)
# Output: Selected routes:
#  [[ 450 1200 1800 2600]
#  [ 520 1350 2000 2900]]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 6: Boolean Indexing on 2D Arrays
# ════════════════════════════════════════════════════════════════
expensive_fares = irctc_fare_matrix[irctc_fare_matrix > 2000]
print("All fares above Rs 2000:", expensive_fares)
# Output: All fares above Rs 2000: [2600 2300 2900]

# Setting values conditionally (very common data-cleaning pattern)
fare_matrix_copy = irctc_fare_matrix.copy()
fare_matrix_copy[fare_matrix_copy < 500] = 0   # zero-out cheap fares
print("Fares below Rs 500 zeroed out:\n", fare_matrix_copy)
# Output: Fares below Rs 500 zeroed out:
#  [[   0 1200 1800 2600]
#  [   0 1050 1600 2300]
#  [ 520 1350 2000 2900]]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 1: Priya's Zomato tip calculation (broadcasting)
# ════════════════════════════════════════════════════════════════
order_totals = np.array([450, 890, 320, 1200])
tip_percentages = np.array([0.10, 0.12, 0.08, 0.15])

tips = order_totals * tip_percentages
print("Priya Sharma's Zomato order tips")
print("Order totals:", order_totals)
print("Tip %:       ", tip_percentages)
print("Tip amounts: ", np.round(tips, 2))
# Output:
# Priya Sharma's Zomato order tips
# Order totals: [ 450  890  320 1200]
# Tip %:        [0.1  0.12 0.08 0.15]
# Tip amounts:  [ 45.   106.8   25.6  180. ]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 2: Arjun's BigBasket cart — row/column broadcasting
# ════════════════════════════════════════════════════════════════
# Rows = 3 items, Columns = 4 quantities purchased across 4 weeks
item_unit_prices = np.array([40, 120, 60]).reshape(-1, 1)   # column vector
weekly_quantities = np.array([
    [2, 3, 1, 4],   # Milk packets
    [1, 1, 2, 1],   # Cooking oil bottles
    [5, 4, 6, 3],   # Vegetables (kg)
])

weekly_cost = item_unit_prices * weekly_quantities
print("Arjun Mehta's BigBasket weekly cost breakdown")
print("Unit prices (column):\n", item_unit_prices)
print("Quantities:\n", weekly_quantities)
print("Weekly cost:\n", weekly_cost)
print("Total cost per week:", weekly_cost.sum(axis=0))
# Output:
# Arjun Mehta's BigBasket weekly cost breakdown
# Unit prices (column):
#  [[ 40]
#  [120]
#  [ 60]]
# Quantities:
#  [[2 3 1 4]
#  [1 1 2 1]
#  [5 4 6 3]]
# Weekly cost:
#  [[ 80 120  40 160]
#  [120 120 240 120]
#  [300 240 360 180]]
# Total cost per week: [500 480 640 460]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 3: Riya's Swiggy — filtering low-rated restaurants
# ════════════════════════════════════════════════════════════════
restaurant_names = np.array(["Spice Villa", "Curry House", "Tandoor Express", "Wok On"])
restaurant_ratings = np.array([3.2, 4.6, 2.8, 4.1])

good_ratings_mask = restaurant_ratings >= 4.0
print("Riya Deshmukh filtering good Swiggy restaurants (rating >= 4.0)")
print("Names:  ", restaurant_names)
print("Ratings:", restaurant_ratings)
print("Good restaurants:", restaurant_names[good_ratings_mask])
# Output:
# Riya Deshmukh filtering good Swiggy restaurants (rating >= 4.0)
# Names:   ['Spice Villa' 'Curry House' 'Tandoor Express' 'Wok On']
# Ratings: [3.2 4.6 2.8 4.1]
# Good restaurants: ['Curry House' 'Wok On']

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLE 4: Sanjay's Paytm — fancy indexing on transaction IDs
# ════════════════════════════════════════════════════════════════
transaction_ids = np.array([5001, 5002, 5003, 5004, 5005, 5006])
transaction_amounts = np.array([200, 1500, 75, 3200, 450, 90])

# Sanjay wants to review only transactions at positions 1, 3, 4
review_positions = [1, 3, 4]
print("Sanjay Verma reviewing selected Paytm transactions")
print("Selected IDs:    ", transaction_ids[review_positions])
print("Selected amounts:", transaction_amounts[review_positions])
# Output:
# Sanjay Verma reviewing selected Paytm transactions
# Selected IDs:     [5002 5004 5005]
# Selected amounts: [1500 3200  450]

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Meera Iyer manages an IRCTC coach layout with 2 coaches x 5 seats.
# seat_status = np.array([[1, 0, 1, 1, 0], [0, 0, 1, 0, 1]])  # 1=booked
#
# Tasks:
#   1. Print how many seats are booked in total (hint: .sum()).
#   2. Print the booking status of coach 2 only (row index 1).
#   3. Use boolean indexing on `seat_status` to count free seats (== 0).
#   4. A price adjustment of +50 applies to coach 1 only, and +30 to
#      coach 2 only. Use a column-vector broadcast to compute an
#      "adjusted seat status" array (seat_status + adjustment).
#
# Expected output:
#   Total booked seats: 5
#   Coach 2 status: [0 0 1 0 1]
#   Free seats: 5
#   Adjusted status:
#    [[51 50 51 51 50]
#    [30 30 31 30 31]]

# YOUR CODE HERE
seat_status = np.array([[1, 0, 1, 1, 0], [0, 0, 1, 0, 1]])

# SOLUTION:
# total_booked = seat_status.sum()
# coach_2_status = seat_status[1, :]
# free_seats = (seat_status == 0).sum()
# adjustment = np.array([50, 30]).reshape(-1, 1)
# adjusted_status = seat_status + adjustment
# print("Total booked seats:", total_booked)
# print("Coach 2 status:", coach_2_status)
# print("Free seats:", free_seats)
# print("Adjusted status:\n", adjusted_status)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file you learned:
#   - Broadcasting: how NumPy stretches smaller arrays to match
#     larger ones (scalar-to-array, row vector, column vector)
#   - The broadcasting compatibility rule (dimensions must match or
#     be 1, compared from the right)
#   - 1D and 2D slicing, including the "slices are views" gotcha
#   - Fancy indexing with lists/arrays of indices (always a copy)
#   - Boolean indexing for filtering and conditional assignment
#
# Next up: day21_03_linalg_basics.py
#   - np.linalg — dot products, matrix multiplication, determinants,
#     inverses, and solving systems of linear equations

if __name__ == "__main__":
    print("Day 21, Part 2 complete: Broadcasting & Indexing.")
