"""
Day 22 — Data & Pandas — Practice Problems (File 3 of 3)

Cumulative scope: Days 1-22
Section Index:
    E. merge() / join()      (2 problems)
    F. Mixed Challenges      (3 problems)

Difficulty legend:
    🟢 Warm-up   — straightforward application of one concept
    🟡 Core      — combines a couple of steps or concepts
    🔴 Challenge — requires more careful thinking / multiple concepts

Instructions for students:
    - Write your answer where you see "# YOUR CODE HERE"
    - Solutions are commented out below each problem — try it yourself first!
    - Uncomment a solution only after attempting the problem

How to run:
    python day22_practise_problems_03_merge_mixed.py
"""

import pandas as pd

print("=" * 60)
print("DAY 22 PRACTICE - FILE 3: MERGE/JOIN + MIXED CHALLENGES")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION E: merge() / join()
# ════════════════════════════════════════════════════════════

# Sample tables used by problems E1-E2
riders = pd.DataFrame({
    "rider_id": [1, 2, 3, 4],
    "name": ["Priya", "Arjun", "Riya", "Sanjay"],
    "city": ["Mumbai", "Delhi", "Pune", "Jaipur"],
})
rides = pd.DataFrame({
    "ride_id": ["R1", "R2", "R3", "R4", "R5"],
    "rider_id": [1, 2, 1, 5, 3],  # rider_id 5 doesn't exist in riders!
    "fare": [180, 220, 95, 310, 150],
})

# --- Problem E1 ---------------------------------------------
# 🟢 Warm-up
# Using `riders` and `rides`, perform an INNER merge on "rider_id"
# and print the result.

# YOUR CODE HERE


# SOLUTION:
# inner = pd.merge(riders, rides, on="rider_id", how="inner")
# print(inner)
#
# Expected output:
#    rider_id   name    city ride_id  fare
# 0         1  Priya  Mumbai      R1   180
# 1         1  Priya  Mumbai      R3    95
# 2         2  Arjun   Delhi      R2   220
# 3         3   Riya    Pune      R5   150

print("-" * 50)

# --- Problem E2 ---------------------------------------------
# 🟡 Core
# Using `riders` and `rides`, perform a LEFT merge (riders as the
# left table) on "rider_id". Then print only the riders who have
# NEVER taken a ride (i.e., their fare/ride_id is missing/NaN).
# (Hint: use .isna() on the "ride_id" column after merging.)

# YOUR CODE HERE


# SOLUTION:
# left = pd.merge(riders, rides, on="rider_id", how="left")
# no_rides = left[left["ride_id"].isna()]
# print(no_rides)
#
# Expected output:
#    rider_id    name    city ride_id  fare
# 4         4  Sanjay  Jaipur     NaN   NaN

print("-" * 50)

# ════════════════════════════════════════════════════════════
# SECTION F: Mixed Challenges (Combines File 1, 2, 3 Concepts)
# ════════════════════════════════════════════════════════════

# --- Problem F1 ---------------------------------------------
# 🟡 Core
# You are given two DataFrames about a college's students and
# their exam results:
#   students = DataFrame({"student_id": [1,2,3,4],
#                          "name": ["Priya","Arjun","Riya","Meera"],
#                          "branch": ["CSE","ECE","CSE","ME"]})
#   results  = DataFrame({"student_id": [1,2,3,4],
#                          "marks": [88,72,95,60]})
# 1. Merge the two on "student_id" (inner join)
# 2. Group the merged result by "branch" and find the average marks
#    per branch

# YOUR CODE HERE


# SOLUTION:
# students = pd.DataFrame({
#     "student_id": [1, 2, 3, 4],
#     "name": ["Priya", "Arjun", "Riya", "Meera"],
#     "branch": ["CSE", "ECE", "CSE", "ME"],
# })
# results = pd.DataFrame({
#     "student_id": [1, 2, 3, 4],
#     "marks": [88, 72, 95, 60],
# })
# merged = pd.merge(students, results, on="student_id", how="inner")
# avg_marks_by_branch = merged.groupby("branch")["marks"].mean()
# print(avg_marks_by_branch)
#
# Expected output:
# branch
# CSE    91.5
# ECE    72.0
# ME     60.0
# Name: marks, dtype: float64

print("-" * 50)

# --- Problem F2 ---------------------------------------------
# 🔴 Challenge
# You have two months of Zomato order data:
#   april = DataFrame({"restaurant": ["Truffles","Empire","Meghana"],
#                       "orders": [120, 95, 140]})
#   may   = DataFrame({"restaurant": ["Truffles","Empire","Meghana"],
#                       "orders": [135, 110, 128]})
# 1. Add a "month" column to each ("Apr" and "May" respectively)
# 2. Combine both into one DataFrame using pd.concat()
# 3. Group by "restaurant" and find the TOTAL orders across both
#    months, sorted highest to lowest
# 4. Save the final sorted summary to "zomato_2month_summary.csv"
#    (without the index), then read it back and print it to confirm

# YOUR CODE HERE


# SOLUTION:
# import os
#
# april = pd.DataFrame({"restaurant": ["Truffles", "Empire", "Meghana"], "orders": [120, 95, 140]})
# may = pd.DataFrame({"restaurant": ["Truffles", "Empire", "Meghana"], "orders": [135, 110, 128]})
# april["month"] = "Apr"
# may["month"] = "May"
#
# combined = pd.concat([april, may], ignore_index=True)
# totals = combined.groupby("restaurant")["orders"].sum().sort_values(ascending=False)
# totals_df = totals.reset_index()
#
# totals_df.to_csv("zomato_2month_summary.csv", index=False)
# check = pd.read_csv("zomato_2month_summary.csv")
# print(check)
#
# os.remove("zomato_2month_summary.csv")
#
# Expected output:
#   restaurant  orders
# 0    Meghana     268
# 1   Truffles     255
# 2     Empire     205

print("-" * 50)

# --- Problem F3 ---------------------------------------------
# 🔴 Challenge
# Given the IRCTC-style DataFrame below:
#   bookings = DataFrame({
#       "passenger": ["Priya","Arjun","Riya","Sanjay","Meera","Karan"],
#       "class":     ["3A","SL","2A","SL","3A","2A"],
#       "fare":      [1750, 890, 2100, 630, 1820, 1950],
#       "status":    ["Confirmed","Waitlisted","Confirmed",
#                      "Confirmed","Waitlisted","Confirmed"],
#   })
# 1. Filter to only "Confirmed" bookings
# 2. Group the filtered data by "class" and compute both the total
#    fare and passenger count (use .agg() with custom names
#    "total_fare" and "passengers")
# 3. Sort the result by "total_fare" descending and print it

# YOUR CODE HERE


# SOLUTION:
# bookings = pd.DataFrame({
#     "passenger": ["Priya", "Arjun", "Riya", "Sanjay", "Meera", "Karan"],
#     "class": ["3A", "SL", "2A", "SL", "3A", "2A"],
#     "fare": [1750, 890, 2100, 630, 1820, 1950],
#     "status": ["Confirmed", "Waitlisted", "Confirmed", "Confirmed", "Waitlisted", "Confirmed"],
# })
# confirmed = bookings[bookings["status"] == "Confirmed"]
# class_summary = confirmed.groupby("class").agg(
#     total_fare=("fare", "sum"),
#     passengers=("passenger", "count"),
# ).sort_values("total_fare", ascending=False)
# print(class_summary)
#
# Expected output:
#        total_fare  passengers
# class
# 2A           4050           2
# 3A           1750           1
# SL            630           1

print("-" * 50)

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: E (merge/join, 2 problems), F (Mixed, 3 problems)
# Difficulty breakdown: 1x Warm-up, 2x Core, 2x Challenge
# Total problems in this file: 5
#
# Grand total across all 3 files for Day 22: 7 + 8 + 5 = 20 problems
#
# This completes the Day 22 practice problem set.
# Next: Day 23 — Web Requests & APIs
