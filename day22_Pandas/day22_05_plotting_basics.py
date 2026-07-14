"""
Day 22 — Data & Pandas
File 5 of 5: Basic Plotting with df.plot()

Covers:
    - How Pandas plotting sits on top of Matplotlib
    - Line plots, bar plots, pie charts, and histograms with df.plot()
    - Customizing titles, labels, colors, and figure size
    - Saving charts to image files (since this runs headless, no GUI window)

Prerequisites:
    - File 1-4 of Day 22
    - Basic familiarity with matplotlib is helpful but not required

How to run:
    python day22_05_plotting_basics.py

Note: This script uses the non-interactive "Agg" backend so it can run
      in any environment (including servers with no display) and saves
      charts as .png files instead of popping up a window.
"""

import matplotlib
matplotlib.use("Agg")  # non-interactive backend — must be set BEFORE importing pyplot
import matplotlib.pyplot as plt
import pandas as pd
import os

print("=" * 60)
print("DAY 22 - PANDAS: BASIC PLOTTING WITH df.plot()")
print("=" * 60)

# ════════════════════════════════════════════════════════════
# SECTION 1: Pandas Plotting is Matplotlib Under the Hood
# ════════════════════════════════════════════════════════════
# Every Pandas Series/DataFrame has a .plot() method. It's a thin
# wrapper around Matplotlib — great for quick, exploratory charts
# without importing matplotlib functions directly.

print("\n── Sample Data: Monthly Flipkart Sales (in Rs Lakhs) ──")

monthly_sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "electronics": [42, 38, 51, 60, 55, 66],
    "fashion": [30, 33, 29, 35, 40, 38],
    "groceries": [25, 27, 26, 28, 30, 31],
})
monthly_sales = monthly_sales.set_index("month")
print(monthly_sales)

# ════════════════════════════════════════════════════════════
# SECTION 2: Line Plot — Trends Over Time
# ════════════════════════════════════════════════════════════
print("\n── Line Plot ──")

ax = monthly_sales.plot(
    kind="line",
    title="Flipkart Monthly Sales by Category (2026)",
    ylabel="Sales (Rs Lakhs)",
    xlabel="Month",
    figsize=(8, 5),
    marker="o",
)
plt.tight_layout()
plt.savefig("chart_line_monthly_sales.png", dpi=100)
plt.close()
print("Saved chart_line_monthly_sales.png")
# Output: a line chart with 3 lines (electronics, fashion, groceries) over 6 months

# ════════════════════════════════════════════════════════════
# SECTION 3: Bar Plot — Comparing Categories
# ════════════════════════════════════════════════════════════
print("\n── Bar Plot ──")

category_totals = monthly_sales.sum().sort_values(ascending=False)
print("Total sales per category:")
print(category_totals)

ax = category_totals.plot(
    kind="bar",
    title="Total Sales by Category (Jan-Jun 2026)",
    ylabel="Sales (Rs Lakhs)",
    color=["#2563EB", "#F97316", "#10B981"],
    figsize=(7, 5),
)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_bar_category_totals.png", dpi=100)
plt.close()
print("Saved chart_bar_category_totals.png")

# ════════════════════════════════════════════════════════════
# SECTION 4: Horizontal Bar Plot — Long Category Names
# ════════════════════════════════════════════════════════════
print("\n── Horizontal Bar Plot ──")

city_orders = pd.Series(
    {"Mumbai": 4200, "Delhi": 3800, "Bengaluru": 4600, "Hyderabad": 2900, "Pune": 2400}
).sort_values()

ax = city_orders.plot(
    kind="barh",
    title="Total Orders by City",
    xlabel="Orders",
    color="#1E3A5F",
    figsize=(7, 5),
)
plt.tight_layout()
plt.savefig("chart_barh_city_orders.png", dpi=100)
plt.close()
print("Saved chart_barh_city_orders.png")

# ════════════════════════════════════════════════════════════
# SECTION 5: Pie Chart — Share of Total
# ════════════════════════════════════════════════════════════
print("\n── Pie Chart ──")

ax = category_totals.plot(
    kind="pie",
    title="Category Share of Total Sales",
    autopct="%1.1f%%",
    figsize=(6, 6),
    ylabel="",  # hides the default y-axis label pandas adds for pie charts
)
plt.tight_layout()
plt.savefig("chart_pie_category_share.png", dpi=100)
plt.close()
print("Saved chart_pie_category_share.png")

# ════════════════════════════════════════════════════════════
# SECTION 6: Histogram — Distribution of a Numeric Column
# ════════════════════════════════════════════════════════════
print("\n── Histogram ──")

order_amounts = pd.Series(
    [220, 450, 310, 890, 670, 120, 540, 990, 430, 610, 380, 720, 260, 810, 500]
)
print("Order amounts:")
print(order_amounts.describe())

ax = order_amounts.plot(
    kind="hist",
    bins=6,
    title="Distribution of Order Amounts (Rs)",
    xlabel="Order Amount (Rs)",
    color="#7C3AED",
    edgecolor="white",
    figsize=(7, 5),
)
plt.tight_layout()
plt.savefig("chart_hist_order_amounts.png", dpi=100)
plt.close()
print("Saved chart_hist_order_amounts.png")

# ════════════════════════════════════════════════════════════
# SECTION 7: Combining groupby() + plot() (Common Real Pattern)
# ════════════════════════════════════════════════════════════
print("\n── groupby() + plot() Together ──")

orders = pd.DataFrame({
    "city": ["Mumbai", "Delhi", "Mumbai", "Bengaluru", "Delhi", "Mumbai", "Bengaluru"],
    "amount": [450, 320, 610, 275, 540, 390, 460],
})

avg_by_city = orders.groupby("city")["amount"].mean().sort_values(ascending=False)
print(avg_by_city)

ax = avg_by_city.plot(
    kind="bar",
    title="Average Order Amount by City",
    ylabel="Avg Amount (Rs)",
    color="#DC2626",
    figsize=(7, 5),
)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_bar_avg_by_city.png", dpi=100)
plt.close()
print("Saved chart_bar_avg_by_city.png")

# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Given a Series of daily active users for a food-delivery app over
# one week, create a line plot titled "Daily Active Users - This Week"
# and save it as "chart_challenge_dau.png"

# YOUR CODE HERE
daily_active_users = pd.Series(
    [12000, 12500, 11800, 13200, 15600, 18400, 17100],
    index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
)
ax = daily_active_users.plot(
    kind="line",
    title="Daily Active Users - This Week",
    ylabel="Active Users",
    xlabel="Day",
    marker="o",
    color="#2563EB",
    figsize=(7, 5),
)
plt.tight_layout()
plt.savefig("chart_challenge_dau.png", dpi=100)
plt.close()
print("\n── Mini-Challenge ──")
print("Saved chart_challenge_dau.png")
# Expected output: "Saved chart_challenge_dau.png" printed, and a line chart
# file created showing DAU rising toward the weekend (Fri-Sun peak)

# ════════════════════════════════════════════════════════════
# CLEANUP (keeps the folder tidy when re-running this script)
# ════════════════════════════════════════════════════════════
for chart_file in [
    "chart_line_monthly_sales.png", "chart_bar_category_totals.png",
    "chart_barh_city_orders.png", "chart_pie_category_share.png",
    "chart_hist_order_amounts.png", "chart_bar_avg_by_city.png",
    "chart_challenge_dau.png",
]:
    if os.path.exists(chart_file):
        os.remove(chart_file)

# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# - df.plot(kind="line"/"bar"/"barh"/"pie"/"hist") covers most quick charts
# - Customize with title=, xlabel=, ylabel=, color=, figsize=
# - plt.savefig("name.png") saves the chart; plt.close() frees memory
# - groupby() + plot() is one of the most common real-world combos
# - matplotlib.use("Agg") lets charts render without a display (servers/CI)
#
# This completes Day 22 concept files. Next: the practice problem sets.
