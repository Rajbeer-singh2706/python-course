"""
Day 22 — Data & Pandas
File 3 of 5: groupby() Aggregations

Covers:
    - The "split-apply-combine" idea behind groupby()
    - Grouping by a single column and aggregating
    - Grouping by multiple columns
    - Using .agg() with multiple functions at once
    - .value_counts() as a quick groupby shortcut
    - Sorting grouped results

Prerequisites:
    - File 1 and File 2 of Day 22

How to run:
    python day22_03_groupby_aggregations.py
"""

import pandas as pd

print("=" * 60)
print("DAY 22 - PANDAS: GROUPBY AGGREGATIONS")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION 1: Sample Data — Swiggy Orders Across Cities
# ════════════════════════════════════════════════════════════
print("\n── Sample Dataset ──")

swiggy = pd.DataFrame({
    "order_id": [f"ORD{1000 + i}" for i in range(10)],
    "city": ["Mumbai", "Delhi", "Mumbai", "Bengaluru", "Delhi",
             "Mumbai", "Bengaluru", "Delhi", "Mumbai", "Bengaluru"],
    "restaurant_type": ["North Indian", "South Indian", "Chinese", "North Indian",
                         "Chinese", "South Indian", "South Indian", "North Indian",
                         "North Indian", "Chinese"],
    "order_value": [450, 320, 610, 275, 540, 390, 460, 300, 700, 385],
    "rating": [4.2, 3.9, 4.6, 4.0, 4.4, 4.1, 4.5, 3.8, 4.7, 4.3],
})
print(swiggy)

# ════════════════════════════════════════════════════════════
# SECTION 2: The Split-Apply-Combine Idea
# ════════════════════════════════════════════════════════════
# groupby() works in 3 steps:
#   1. SPLIT  — break the DataFrame into groups (e.g., by city)
#   2. APPLY  — apply a function to each group (e.g., mean, sum)
#   3. COMBINE — stitch results back into a single DataFrame/Series
print("\n── Grouping by a Single Column ──")

city_groups = swiggy.groupby("city")
print("Type of a groupby object:", type(city_groups))
# Output: <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
# Note: nothing is computed yet until we apply an aggregation!

avg_order_by_city = city_groups["order_value"].mean()
print("\nAverage order value by city:")
print(avg_order_by_city)
# Output: mean order_value per city, sorted alphabetically by city

total_orders_by_city = city_groups["order_value"].sum()
print("\nTotal order value by city:")
print(total_orders_by_city)

count_by_city = city_groups.size()
print("\nNumber of orders per city (.size()):")
print(count_by_city)

# ════════════════════════════════════════════════════════════
# SECTION 3: Grouping by Multiple Columns
# ════════════════════════════════════════════════════════════
print("\n── Grouping by Multiple Columns ──")

city_type_avg = swiggy.groupby(["city", "restaurant_type"])["order_value"].mean()
print(city_type_avg)
# Output: a MultiIndex Series — one average per (city, restaurant_type) pair

# Convert the MultiIndex Series back into a flat DataFrame for easier reading
city_type_avg_df = city_type_avg.reset_index()
print("\nFlattened with .reset_index():")
print(city_type_avg_df)

# ════════════════════════════════════════════════════════════
# SECTION 4: Multiple Aggregations at Once with .agg()
# ════════════════════════════════════════════════════════════
print("\n── Multiple Aggregations with .agg() ──")

summary = swiggy.groupby("city")["order_value"].agg(["mean", "sum", "min", "max", "count"])
print(summary)
# Output: one row per city, with mean/sum/min/max/count columns

# Different aggregations for different columns
custom_summary = swiggy.groupby("city").agg(
    avg_order_value=("order_value", "mean"),
    total_orders=("order_id", "count"),
    avg_rating=("rating", "mean"),
)
print("\nCustom named aggregations:")
print(custom_summary)
# Output: columns named exactly as we specified — avg_order_value, total_orders, avg_rating

# ════════════════════════════════════════════════════════════
# SECTION 5: Sorting Grouped Results
# ════════════════════════════════════════════════════════════
print("\n── Sorting Grouped Results ──")

top_cities = custom_summary.sort_values("avg_order_value", ascending=False)
print("Cities ranked by average order value (highest first):")
print(top_cities)

# ════════════════════════════════════════════════════════════
# SECTION 6: .value_counts() — A Quick Groupby Shortcut
# ════════════════════════════════════════════════════════════
print("\n── .value_counts() ──")

# Equivalent to groupby("restaurant_type").size(), but simpler to write
type_counts = swiggy["restaurant_type"].value_counts()
print(type_counts)
# Output: counts of each restaurant_type, sorted descending by default

type_percentages = swiggy["restaurant_type"].value_counts(normalize=True) * 100
print("\nAs percentages:")
print(type_percentages.round(1))

# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Using the `swiggy` DataFrame:
#   1. Find the total order_value per restaurant_type
#   2. Find which restaurant_type has the highest average rating
#   3. Print both results

# YOUR CODE HERE
print("\n── Mini-Challenge ──")
total_by_type = swiggy.groupby("restaurant_type")["order_value"].sum()
print("Total order value by restaurant type:")
print(total_by_type)

avg_rating_by_type = swiggy.groupby("restaurant_type")["rating"].mean().sort_values(ascending=False)
print("\nAverage rating by restaurant type (highest first):")
print(avg_rating_by_type)
print("\nHighest-rated restaurant type:", avg_rating_by_type.index[0])
# Expected output: "Chinese" as the highest-rated type (avg of 4.6, 4.4, 4.3 = 4.43)

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# - groupby() follows split -> apply -> combine
# - df.groupby("col")["target"].mean()/.sum()/.count() for single aggregations
# - df.groupby(["col1", "col2"]) groups by multiple keys (MultiIndex result)
# - .agg([...]) applies several functions at once
# - .agg(name=("col", "func")) gives custom output column names
# - .value_counts() is a quick shortcut for counting unique values
#
# Next: File 4 covers merge() and join() for combining multiple DataFrames.
