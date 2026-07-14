"""
Day 22 — Data & Pandas
File 4 of 5: merge() and join()

Covers:
    - Why we need to combine DataFrames (relational data, like SQL tables)
    - pd.merge() — inner, left, right, and outer joins
    - Merging on differently-named columns (left_on / right_on)
    - .join() — merging on the index instead of a column
    - pd.concat() — stacking DataFrames (bonus, related concept)

Prerequisites:
    - File 1-3 of Day 22

How to run:
    python day22_04_merge_join.py
"""

import pandas as pd

print("=" * 60)
print("DAY 22 - PANDAS: MERGE() AND JOIN()")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION 1: Why Combine DataFrames?
# ════════════════════════════════════════════════════════════
# Real data is often split across multiple tables, just like a
# relational database (SQL). For example:
#   - one table of customers
#   - one table of orders (linked to customers by customer_id)
# We need to JOIN them to answer questions like
# "which city placed the most orders?"

print("\n── Two Related Tables ──")

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "name": ["Priya Sharma", "Arjun Mehta", "Riya Deshmukh", "Sanjay Verma"],
    "city": ["Mumbai", "Delhi", "Pune", "Jaipur"],
})
print("customers:")
print(customers)

orders = pd.DataFrame({
    "order_id": ["ORD1", "ORD2", "ORD3", "ORD4", "ORD5"],
    "customer_id": [101, 102, 101, 105, 103],  # note: 105 doesn't exist in customers!
    "amount": [1200, 850, 430, 990, 670],
})
print("\norders:")
print(orders)
# Note: customer 104 (Sanjay Verma) has no orders,
#       and order ORD4 belongs to customer_id 105 who isn't in `customers`.
#       This mismatch is exactly what different join types handle differently.

# ════════════════════════════════════════════════════════════
# SECTION 2: Inner Join (default) — Only Matching Rows
# ════════════════════════════════════════════════════════════
print("\n── Inner Join (how='inner', the default) ──")

inner_result = pd.merge(customers, orders, on="customer_id", how="inner")
print(inner_result)
# Output: only customer_ids present in BOTH tables (101, 102, 103) —
# Sanjay Verma (104, no orders) and customer 105 (no matching customer) are dropped

# ════════════════════════════════════════════════════════════
# SECTION 3: Left Join — Keep All Rows From the Left Table
# ════════════════════════════════════════════════════════════
print("\n── Left Join (how='left') ──")

left_result = pd.merge(customers, orders, on="customer_id", how="left")
print(left_result)
# Output: every customer appears at least once; Sanjay Verma (104) shows up
# with NaN order columns since he has no orders

# ════════════════════════════════════════════════════════════
# SECTION 4: Right Join — Keep All Rows From the Right Table
# ════════════════════════════════════════════════════════════
print("\n── Right Join (how='right') ──")

right_result = pd.merge(customers, orders, on="customer_id", how="right")
print(right_result)
# Output: every order appears; the order from customer_id 105 shows up
# with NaN name/city since that customer doesn't exist in `customers`

# ════════════════════════════════════════════════════════════
# SECTION 5: Outer Join — Keep Everything From Both Sides
# ════════════════════════════════════════════════════════════
print("\n── Outer Join (how='outer') ──")

outer_result = pd.merge(customers, orders, on="customer_id", how="outer")
print(outer_result.sort_values("customer_id").reset_index(drop=True))
# Output: union of both tables — Sanjay Verma appears with NaN order info,
# and customer_id 105's order appears with NaN customer info

# ════════════════════════════════════════════════════════════
# SECTION 6: Merging on Differently-Named Columns
# ════════════════════════════════════════════════════════════
print("\n── Merging with Different Column Names ──")

# Suppose the orders table uses "cust_id" instead of "customer_id"
orders_renamed = orders.rename(columns={"customer_id": "cust_id"})
print("orders_renamed columns:", list(orders_renamed.columns))

merged_diff_names = pd.merge(
    customers, orders_renamed,
    left_on="customer_id", right_on="cust_id",
    how="inner",
)
print(merged_diff_names)
# Output: same result as before, but both 'customer_id' and 'cust_id' columns
# appear in the output since they had different names

# ════════════════════════════════════════════════════════════
# SECTION 7: .join() — Merging on the Index
# ════════════════════════════════════════════════════════════
print("\n── .join() — Merging by Index ──")

# .join() is a shortcut for merging when one/both DataFrames use
# their index as the join key, instead of a regular column.
customers_indexed = customers.set_index("customer_id")
orders_indexed = orders.set_index("customer_id")

joined = customers_indexed.join(orders_indexed, how="inner", lsuffix="_cust", rsuffix="_ord")
print(joined)
# Output: joined on the shared index (customer_id), same rows as the inner merge

# ════════════════════════════════════════════════════════════
# SECTION 8: pd.concat() — Stacking DataFrames (Bonus)
# ════════════════════════════════════════════════════════════
print("\n── pd.concat() — Stacking Rows ──")

# concat() is for STACKING (like appending), not matching keys.
# Useful when combining, e.g., January and February sales into one table.
jan_sales = pd.DataFrame({"month": ["Jan"] * 2, "revenue": [50000, 62000]})
feb_sales = pd.DataFrame({"month": ["Feb"] * 2, "revenue": [58000, 71000]})

combined_sales = pd.concat([jan_sales, feb_sales], ignore_index=True)
print(combined_sales)
# Output: 4 rows total, Jan rows followed by Feb rows, with a fresh 0..3 index

# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Given:
#   products = DataFrame with columns "product_id", "product_name"
#       [(1, "Notebook"), (2, "Pen"), (3, "Backpack")]
#   sales    = DataFrame with columns "product_id", "units_sold"
#       [(1, 120), (2, 300), (4, 50)]   <- product_id 4 doesn't exist in products!
#
# 1. Do a LEFT join of products with sales on "product_id"
# 2. Do an OUTER join of products with sales on "product_id"
# 3. Print both results

# YOUR CODE HERE
products = pd.DataFrame({
    "product_id": [1, 2, 3],
    "product_name": ["Notebook", "Pen", "Backpack"],
})
sales = pd.DataFrame({
    "product_id": [1, 2, 4],
    "units_sold": [120, 300, 50],
})

print("\n── Mini-Challenge: Left Join ──")
left_join_result = pd.merge(products, sales, on="product_id", how="left")
print(left_join_result)
# Expected: Backpack (id 3) appears with NaN units_sold; product_id 4 is dropped

print("\n── Mini-Challenge: Outer Join ──")
outer_join_result = pd.merge(products, sales, on="product_id", how="outer")
print(outer_join_result)
# Expected: Backpack (id 3, NaN units_sold) AND product_id 4 (NaN product_name) both appear

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# - pd.merge(df1, df2, on="key", how="inner"/"left"/"right"/"outer")
# - inner  -> only matching rows from both tables
# - left   -> all rows from the left table, matched where possible
# - right  -> all rows from the right table, matched where possible
# - outer  -> all rows from both tables (union), unmatched become NaN
# - left_on / right_on -> merge when column names differ between tables
# - .join() -> merge using the DataFrame's index instead of a column
# - pd.concat() -> stack DataFrames on top of each other (not key-based)
#
# Next: File 5 covers basic plotting with df.plot().
