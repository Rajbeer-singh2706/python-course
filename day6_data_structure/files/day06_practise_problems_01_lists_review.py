"""
Day 6 — Data Structures — Practice Problems
File 1 of 4: Section A (Prior Days Review) + Section B (Lists)

Cumulative scope: Days 1-6 (Setup, Variables, Control Flow, Loops,
Functions & Scope, Data Structures)

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines two or more ideas
    🔴 Challenge — requires extra thought or edge-case handling

Section index (this file):
    A. Prior Days Review        (2 problems)
    B. Lists                    (4 problems)

How to run:
    python3 day06_practise_problems_01_lists_review.py
"""


# ════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════════

# --- Problem A1 -----------------------------------------------
# 🟢 Warm-up
# Write a function `is_even(number)` that returns True if a number
# is even, False otherwise. Test it on the number 46.
# Expected output: True

number_to_check = 46

# YOUR CODE HERE


# SOLUTION:
# def is_even(number):
#     return number % 2 == 0
#
# print(is_even(number_to_check))

print("-" * 50)


# --- Problem A2 -----------------------------------------------
# 🟡 Core
# Using a for loop and range(), print the multiplication table of
# 7 from 1 to 5 (i.e. 7x1, 7x2, ..., 7x5), one line per result.
# Expected output:
#   7 x 1 = 7
#   7 x 2 = 14
#   7 x 3 = 21
#   7 x 4 = 28
#   7 x 5 = 35

# YOUR CODE HERE


# SOLUTION:
# for i in range(1, 6):
#     print(f"7 x {i} = {7 * i}")

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION B — Lists
# ════════════════════════════════════════════════════════════

# --- Problem B1 -----------------------------------------------
# 🟢 Warm-up
# Given the list of vegetables below, append "spinach" to the end
# and print the updated list.
# Expected output:
#   ['potato', 'onion', 'tomato', 'spinach']

vegetables = ["potato", "onion", "tomato"]

# YOUR CODE HERE


# SOLUTION:
# vegetables.append("spinach")
# print(vegetables)

print("-" * 50)


# --- Problem B2 -----------------------------------------------
# 🟢 Warm-up
# Given the list of bus stop names below, use slicing to print
# only the first three stops.
# Expected output:
#   ['Andheri', 'Bandra', 'Dadar']

bus_stops = ["Andheri", "Bandra", "Dadar", "Worli", "Colaba"]

# YOUR CODE HERE


# SOLUTION:
# print(bus_stops[:3])

print("-" * 50)


# --- Problem B3 -----------------------------------------------
# 🟡 Core
# Given the list of daily sales figures (in rupees) below, remove
# the smallest value from the list and print both the removed
# value and the updated list.
# Expected output:
#   Removed: 320
#   Updated list: [1200, 950, 1800, 700]

daily_sales = [1200, 950, 320, 1800, 700]

# YOUR CODE HERE


# SOLUTION:
# smallest = min(daily_sales)
# daily_sales.remove(smallest)
# print("Removed:", smallest)
# print("Updated list:", daily_sales)

print("-" * 50)


# --- Problem B4 -----------------------------------------------
# 🔴 Challenge
# Given the list of temperatures (in Celsius) recorded over a week,
# write code that:
#   1. Sorts a COPY of the list (do not mutate the original)
#   2. Prints the original list (unchanged)
#   3. Prints the sorted copy
#   4. Prints the 3 hottest days using slicing on the sorted copy
# Expected output:
#   Original: [28, 33, 25, 30, 27, 35, 29]
#   Sorted copy: [25, 27, 28, 29, 30, 33, 35]
#   3 hottest: [30, 33, 35]

week_temperatures = [28, 33, 25, 30, 27, 35, 29]

# YOUR CODE HERE


# SOLUTION:
# sorted_copy = sorted(week_temperatures)   # sorted() returns a NEW list
# print("Original:", week_temperatures)
# print("Sorted copy:", sorted_copy)
# print("3 hottest:", sorted_copy[-3:])

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: A (Prior Review), B (Lists)
# Difficulty breakdown: 3x Warm-up, 2x Core, 1x Challenge
# Total problems in this file: 6
#
# Continue with: day06_practise_problems_02_tuples.py
