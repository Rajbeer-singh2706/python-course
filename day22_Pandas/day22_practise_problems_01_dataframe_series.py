"""
Day 22 — Data & Pandas — Practice Problems (File 1 of 3)

Cumulative scope: Days 1-22 (review problems draw on prior days)
Section Index:
    A. Prior Days Review          (2 problems)
    B. DataFrame & Series Basics  (5 problems)

Difficulty legend:
    🟢 Warm-up   — straightforward application of one concept
    🟡 Core      — combines a couple of steps or concepts
    🔴 Challenge — requires more careful thinking / multiple concepts

Instructions for students:
    - Write your answer where you see "# YOUR CODE HERE"
    - Solutions are commented out below each problem — try it yourself first!
    - Uncomment a solution only after attempting the problem

How to run:
    python day22_practise_problems_01_dataframe_series.py
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("DAY 22 PRACTICE - FILE 1: REVIEW + DATAFRAME/SERIES BASICS")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION A: Prior Days Review
# ════════════════════════════════════════════════════════════

# --- Problem A1 ---------------------------------------------
# 🟢 Warm-up
# (Day 21 review) Given the NumPy array below, compute its mean,
# max, and min using NumPy methods.
scores_array = np.array([78, 85, 92, 60, 74, 88])

# YOUR CODE HERE


# SOLUTION:
# print("Mean:", scores_array.mean())
# print("Max:", scores_array.max())
# print("Min:", scores_array.min())
#
# Expected output:
# Mean: 79.5
# Max: 92
# Min: 60

print("-" * 50)

# --- Problem A2 ---------------------------------------------
# 🟡 Core
# (Day 9 review) Write a function `safe_divide(a, b)` that returns
# a / b, but catches ZeroDivisionError and returns None instead.
# Test it with safe_divide(10, 2) and safe_divide(5, 0).

# YOUR CODE HERE


# SOLUTION:
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None
#
# print(safe_divide(10, 2))
# print(safe_divide(5, 0))
#
# Expected output:
# 5.0
# None

print("-" * 50)

# ════════════════════════════════════════════════════════════
# SECTION B: DataFrame & Series Basics
# ════════════════════════════════════════════════════════════

# --- Problem B1 ---------------------------------------------
# 🟢 Warm-up
# Create a Pandas Series named `paytm_balances` from this dict:
#   {"Priya": 2500, "Arjun": 1800, "Riya": 3200, "Sanjay": 950}
# Print the Series, then print only Riya's balance.

# YOUR CODE HERE


# SOLUTION:
# paytm_balances = pd.Series({"Priya": 2500, "Arjun": 1800, "Riya": 3200, "Sanjay": 950})
# print(paytm_balances)
# print("Riya's balance:", paytm_balances["Riya"])
#
# Expected output:
# Priya     2500
# Arjun     1800
# Riya      3200
# Sanjay     950
# dtype: int64
# Riya's balance: 3200

print("-" * 50)

# --- Problem B2 ---------------------------------------------
# 🟢 Warm-up
# Create a DataFrame `movies` with columns "title", "genre", "rating"
# using this data (list of dicts):
#   [{"title": "Pathaan", "genre": "Action", "rating": 4.1},
#    {"title": "Jawan", "genre": "Action", "rating": 4.4},
#    {"title": "12th Fail", "genre": "Drama", "rating": 4.8}]
# Print the DataFrame and its shape.

# YOUR CODE HERE


# SOLUTION:
# movies = pd.DataFrame([
#     {"title": "Pathaan", "genre": "Action", "rating": 4.1},
#     {"title": "Jawan", "genre": "Action", "rating": 4.4},
#     {"title": "12th Fail", "genre": "Drama", "rating": 4.8},
# ])
# print(movies)
# print("Shape:", movies.shape)
#
# Expected output:
#        title   genre  rating
# 0    Pathaan  Action     4.1
# 1      Jawan  Action     4.4
# 2  12th Fail   Drama     4.8
# Shape: (3, 3)

print("-" * 50)

# --- Problem B3 ---------------------------------------------
# 🟡 Core
# Using a `movies` DataFrame like the one in B2, select and print
# only the movies with rating >= 4.4. Then print just the "title"
# column of that filtered result.

# YOUR CODE HERE


# SOLUTION:
# top_movies = movies[movies["rating"] >= 4.4]
# print(top_movies)
# print(top_movies["title"])
#
# Expected output:
#        title   genre  rating
# 1      Jawan  Action     4.4
# 2  12th Fail   Drama     4.8
# 1        Jawan
# 2    12th Fail
# Name: title, dtype: str

print("-" * 50)

# --- Problem B4 ---------------------------------------------
# 🟡 Core
# Using the `movies` DataFrame, add a new column "verdict" that is
# "Blockbuster" if rating >= 4.5, else "Hit" if rating >= 4.0,
# else "Average". Print the updated DataFrame.
# (Hint: use .apply() with a small helper function or lambda.)

# YOUR CODE HERE


# SOLUTION:
# def verdict(rating):
#     if rating >= 4.5:
#         return "Blockbuster"
#     elif rating >= 4.0:
#         return "Hit"
#     else:
#         return "Average"
#
# movies["verdict"] = movies["rating"].apply(verdict)
# print(movies)
#
# Expected output:
#        title   genre  rating      verdict
# 0    Pathaan  Action     4.1          Hit
# 1      Jawan  Action     4.4          Hit
# 2  12th Fail   Drama     4.8  Blockbuster

print("-" * 50)

# --- Problem B5 ---------------------------------------------
# 🔴 Challenge
# Create a DataFrame `wallet_txns` with columns "user", "type"
# ("credit"/"debit"), "amount" using this data:
#   user:   Priya, Priya, Arjun, Arjun, Riya
#   type:   credit, debit, credit, debit, credit
#   amount: 5000, 1200, 3000, 500, 2000
# Using .loc[], select all rows where type == "debit" and print
# only the "user" and "amount" columns. Then compute the NET
# balance (credits - debits) for the WHOLE table as a single number
# using boolean filtering and .sum().

# YOUR CODE HERE


# SOLUTION:
# wallet_txns = pd.DataFrame({
#     "user": ["Priya", "Priya", "Arjun", "Arjun", "Riya"],
#     "type": ["credit", "debit", "credit", "debit", "credit"],
#     "amount": [5000, 1200, 3000, 500, 2000],
# })
# debits = wallet_txns.loc[wallet_txns["type"] == "debit", ["user", "amount"]]
# print(debits)
#
# total_credits = wallet_txns.loc[wallet_txns["type"] == "credit", "amount"].sum()
# total_debits = wallet_txns.loc[wallet_txns["type"] == "debit", "amount"].sum()
# net_balance = total_credits - total_debits
# print("Net balance:", net_balance)
#
# Expected output:
#     user  amount
# 1  Priya    1200
# 3  Arjun     500
# Net balance: 8300

print("-" * 50)

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: A (Review, 2 problems), B (DataFrame/Series, 5 problems)
# Difficulty breakdown: 3x Warm-up, 3x Core, 1x Challenge
# Total problems in this file: 7
#
# Next file: day22_practise_problems_02_csv_groupby.py
# covers CSV I/O and groupby() aggregations.
