"""
Day 6 — Data Structures — Practice Problems
File 3 of 4: Section D (Dictionaries)

Cumulative scope: Days 1-6

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines two or more ideas
    🔴 Challenge — requires extra thought or edge-case handling

Section index (this file):
    D. Dictionaries              (4 problems)

How to run:
    python3 day06_practise_problems_03_dictionaries.py
"""


# ════════════════════════════════════════════════════════════
# SECTION D — Dictionaries
# ════════════════════════════════════════════════════════════

# --- Problem D1 -----------------------------------------------
# 🟢 Warm-up
# Given the dictionary of fruit prices (in rupees per kg) below,
# add a new entry "grapes" priced at 90, then print the dictionary.
# Expected output:
#   {'apple': 180, 'banana': 60, 'mango': 120, 'grapes': 90}

fruit_prices = {"apple": 180, "banana": 60, "mango": 120}

# YOUR CODE HERE


# SOLUTION:
# fruit_prices["grapes"] = 90
# print(fruit_prices)

print("-" * 50)


# --- Problem D2 -----------------------------------------------
# 🟢 Warm-up
# Given the dictionary below, safely look up the price of "kiwi"
# using .get() with a default value of -1 (since it's not in the
# dictionary).
# Expected output: -1

# YOUR CODE HERE


# SOLUTION:
# print(fruit_prices.get("kiwi", -1))

print("-" * 50)


# --- Problem D3 -----------------------------------------------
# 🟡 Core
# Given the dictionary of student attendance counts below, loop
# over it with .items() and print each student who attended fewer
# than 20 classes, in the format "Name: count".
# Expected output:
#   Sanjay: 15
#   Kavita: 18

attendance = {"Priya": 25, "Sanjay": 15, "Arjun": 22, "Kavita": 18}

# YOUR CODE HERE


# SOLUTION:
# for name, count in attendance.items():
#     if count < 20:
#         print(f"{name}: {count}")

print("-" * 50)


# --- Problem D4 -----------------------------------------------
# 🔴 Challenge
# Given the two dictionaries below representing product stock in
# two different warehouses (Mumbai and Delhi), merge them into a
# single dictionary where, if a product exists in both, the
# QUANTITIES ARE ADDED TOGETHER (not overwritten).
# Expected output:
#   {'rice': 150, 'wheat': 80, 'sugar': 120, 'tea': 40}

mumbai_stock = {"rice": 100, "wheat": 80, "sugar": 50}
delhi_stock = {"rice": 50, "sugar": 70, "tea": 40}

# YOUR CODE HERE


# SOLUTION:
# combined_stock = mumbai_stock.copy()
# for product, quantity in delhi_stock.items():
#     combined_stock[product] = combined_stock.get(product, 0) + quantity
# print(combined_stock)

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: D (Dictionaries)
# Difficulty breakdown: 2x Warm-up, 1x Core, 1x Challenge
# Total problems in this file: 4
#
# Continue with: day06_practise_problems_04_sets_comprehensions_mixed.py
