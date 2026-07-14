"""
Day 22 — Data & Pandas — Practice Problems (File 2 of 3)

Cumulative scope: Days 1-22
Section Index:
    C. CSV Read/Write            (4 problems)
    D. groupby() Aggregations    (4 problems)

Difficulty legend:
    🟢 Warm-up   — straightforward application of one concept
    🟡 Core      — combines a couple of steps or concepts
    🔴 Challenge — requires more careful thinking / multiple concepts

Instructions for students:
    - Write your answer where you see "# YOUR CODE HERE"
    - Solutions are commented out below each problem — try it yourself first!
    - Uncomment a solution only after attempting the problem

How to run:
    python day22_practise_problems_02_csv_groupby.py
"""

import pandas as pd
import os

print("=" * 60)
print("DAY 22 PRACTICE - FILE 2: CSV I/O + GROUPBY AGGREGATIONS")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION C: CSV Read/Write
# ════════════════════════════════════════════════════════════

# --- Problem C1 ---------------------------------------------
# 🟢 Warm-up
# Create a DataFrame `flipkart_orders` with columns "order_id",
# "item", "price":
#   order_id: ["FK1001", "FK1002", "FK1003"]
#   item:     ["Mixer Grinder", "Bluetooth Speaker", "Yoga Mat"]
#   price:    [2499, 1899, 599]
# Save it to "flipkart_orders.csv" without writing the row index.

# YOUR CODE HERE


# SOLUTION:
# flipkart_orders = pd.DataFrame({
#     "order_id": ["FK1001", "FK1002", "FK1003"],
#     "item": ["Mixer Grinder", "Bluetooth Speaker", "Yoga Mat"],
#     "price": [2499, 1899, 599],
# })
# flipkart_orders.to_csv("flipkart_orders.csv", index=False)
# print("Saved flipkart_orders.csv")
#
# Expected output:
# Saved flipkart_orders.csv

print("-" * 50)

# --- Problem C2 ---------------------------------------------
# 🟢 Warm-up
# Read "flipkart_orders.csv" (created in C1) back into a DataFrame
# and print it, along with its column dtypes.

# YOUR CODE HERE


# SOLUTION:
# reloaded = pd.read_csv("flipkart_orders.csv")
# print(reloaded)
# print(reloaded.dtypes)
#
# Expected output:
#   order_id               item  price
# 0   FK1001      Mixer Grinder   2499
# 1   FK1002  Bluetooth Speaker   1899
# 2   FK1003           Yoga Mat    599
# order_id      str
# item          str
# price       int64
# dtype: object

print("-" * 50)

# --- Problem C3 ---------------------------------------------
# 🟡 Core
# The CSV text below (already written to "raw_txns.csv" for you)
# represents Paytm transactions with some missing values marked
# as "MISSING". Read it in, treating "MISSING" as NaN, then fill
# missing amounts with 0 and print the cleaned DataFrame.
with open("raw_txns.csv", "w") as _f:
    _f.write("txn_id,user,amount\n")
    _f.write("T1,Priya,500\n")
    _f.write("T2,Arjun,MISSING\n")
    _f.write("T3,Riya,750\n")

# YOUR CODE HERE


# SOLUTION:
# txns = pd.read_csv("raw_txns.csv", na_values=["MISSING"])
# txns["amount"] = txns["amount"].fillna(0)
# print(txns)
#
# Expected output:
#   txn_id   user  amount
# 0     T1  Priya   500.0
# 1     T2  Arjun     0.0
# 2     T3   Riya   750.0

print("-" * 50)

# --- Problem C4 ---------------------------------------------
# 🔴 Challenge
# Using the `flipkart_orders.csv` file from C1, read it in, filter
# to only items priced above Rs 1000, add a new column "gst_18pct"
# (price * 0.18), and save the result to
# "flipkart_orders_premium.csv" without the index. Then read that
# new file back and print it to confirm it saved correctly.

# YOUR CODE HERE


# SOLUTION:
# df = pd.read_csv("flipkart_orders.csv")
# premium = df[df["price"] > 1000].copy()
# premium["gst_18pct"] = premium["price"] * 0.18
# premium.to_csv("flipkart_orders_premium.csv", index=False)
#
# check = pd.read_csv("flipkart_orders_premium.csv")
# print(check)
#
# Expected output:
#    order_id               item  price  gst_18pct
# 0  FK1001      Mixer Grinder    2499     449.82
# 1  FK1002  Bluetooth Speaker    1899     341.82

print("-" * 50)

# ════════════════════════════════════════════════════════════
# SECTION D: groupby() Aggregations
# ════════════════════════════════════════════════════════════

# Sample dataset used by problems D1-D5
irctc_travel = pd.DataFrame({
    "passenger": ["Priya", "Arjun", "Riya", "Sanjay", "Meera", "Karan", "Ananya", "Vikram"],
    "class": ["3A", "SL", "2A", "SL", "3A", "2A", "SL", "3A"],
    "route": ["Mumbai-Delhi", "Chennai-Bengaluru", "Howrah-Delhi", "Delhi-Bhopal",
              "Mumbai-Pune", "Chennai-Bengaluru", "Delhi-Bhopal", "Mumbai-Delhi"],
    "fare": [1750, 890, 2100, 630, 540, 950, 610, 1820],
})

# --- Problem D1 ---------------------------------------------
# 🟢 Warm-up
# Using `irctc_travel`, find the average fare per "class".

# YOUR CODE HERE


# SOLUTION:
# avg_fare_by_class = irctc_travel.groupby("class")["fare"].mean()
# print(avg_fare_by_class)
#
# Expected output:
# class
# 2A    1525.0
# 3A    1370.0
# SL     710.0
# Name: fare, dtype: float64

print("-" * 50)

# --- Problem D2 ---------------------------------------------
# 🟡 Core
# Using `irctc_travel`, group by "route" and compute BOTH the
# total fare and the number of passengers per route, using .agg()
# with custom column names "total_fare" and "passenger_count".

# YOUR CODE HERE


# SOLUTION:
# route_summary = irctc_travel.groupby("route").agg(
#     total_fare=("fare", "sum"),
#     passenger_count=("passenger", "count"),
# )
# print(route_summary)
#
# Expected output:
#                     total_fare  passenger_count
# route
# Chennai-Bengaluru         1840                2
# Delhi-Bhopal               1240                2
# Howrah-Delhi                2100                1
# Mumbai-Delhi                3570                2
# Mumbai-Pune                  540                1

print("-" * 50)

# --- Problem D3 ---------------------------------------------
# 🟡 Core
# Using `irctc_travel`, find which "class" has the HIGHEST total
# fare collected, and print just that class name and amount.
# (Hint: groupby + sum + sort_values, then take the top row.)

# YOUR CODE HERE


# SOLUTION:
# total_by_class = irctc_travel.groupby("class")["fare"].sum().sort_values(ascending=False)
# top_class = total_by_class.index[0]
# top_amount = total_by_class.iloc[0]
# print(f"Highest-earning class: {top_class} (Rs {top_amount})")
#
# Expected output:
# Highest-earning class: 3A (Rs 4110)

print("-" * 50)

# --- Problem D4 ---------------------------------------------
# 🔴 Challenge
# Using `irctc_travel`, group by BOTH "class" and "route", and
# compute the average fare for each (class, route) combination.
# Then reset the index so the result is a flat DataFrame with
# columns "class", "route", "fare".

# YOUR CODE HERE


# SOLUTION:
# grouped = irctc_travel.groupby(["class", "route"])["fare"].mean().reset_index()
# print(grouped)
#
# Expected output:
#   class              route    fare
# 0    2A  Chennai-Bengaluru   950.0
# 1    2A       Howrah-Delhi  2100.0
# 2    3A       Mumbai-Delhi  1785.0
# 3    3A        Mumbai-Pune   540.0
# 4    SL  Chennai-Bengaluru   890.0
# 5    SL       Delhi-Bhopal   620.0

print("-" * 50)

# ════════════════════════════════════════════════════════════
# CLEANUP (keeps the folder tidy when re-running this script)
# ════════════════════════════════════════════════════════════
for temp_file in ["flipkart_orders.csv", "raw_txns.csv", "flipkart_orders_premium.csv"]:
    if os.path.exists(temp_file):
        os.remove(temp_file)

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: C (CSV I/O, 4 problems), D (groupby, 4 problems)
# Difficulty breakdown: 3x Warm-up, 3x Core, 2x Challenge
# Total problems in this file: 8
#
# Next file: day22_practise_problems_03_merge_mixed.py
# covers merge()/join() and Mixed Challenges combining all Day 22 concepts.
