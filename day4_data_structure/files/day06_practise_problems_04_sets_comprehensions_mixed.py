"""
Day 6 — Data Structures — Practice Problems
File 4 of 4: Section E (Sets & Comprehensions) + Section F (Mixed Challenges)

Cumulative scope: Days 1-6

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines two or more ideas
    🔴 Challenge — requires extra thought or edge-case handling

Section index (this file):
    E. Sets & Comprehensions      (4 problems)
    F. Mixed Challenges           (3 problems)

How to run:
    python3 day06_practise_problems_04_sets_comprehensions_mixed.py
"""


# ════════════════════════════════════════════════════════════
# SECTION E — Sets & Comprehensions
# ════════════════════════════════════════════════════════════

# --- Problem E1 -----------------------------------------------
# 🟢 Warm-up
# Given the list of cities visited by a traveller (with duplicates),
# convert it to a set to get only the unique cities visited, then
# print it.
# Expected output (order may vary):
#   {'Mumbai', 'Delhi', 'Pune'}

cities_visited = ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi", "Mumbai"]

# YOUR CODE HERE


# SOLUTION:
# unique_cities = set(cities_visited)
# print(unique_cities)

print("-" * 50)


# --- Problem E2 -----------------------------------------------
# 🟡 Core
# Given two sets of subjects offered by two different colleges,
# print the subjects offered by BOTH colleges (intersection) and
# the subjects offered by EITHER college (union).
# Expected output:
#   Common subjects: {'Physics', 'Chemistry'}
#   All subjects offered: {'Physics', 'Chemistry', 'Biology', 'Math', 'Economics'}

college_a_subjects = {"Physics", "Chemistry", "Biology"}
college_b_subjects = {"Physics", "Chemistry", "Math", "Economics"}

# YOUR CODE HERE


# SOLUTION:
# common_subjects = college_a_subjects & college_b_subjects
# all_subjects = college_a_subjects | college_b_subjects
# print("Common subjects:", common_subjects)
# print("All subjects offered:", all_subjects)

print("-" * 50)


# --- Problem E3 -----------------------------------------------
# 🟡 Core
# Using a single list comprehension, build a list of squares of
# only the EVEN numbers from 1 to 10 (inclusive).
# Expected output:
#   [4, 16, 36, 64, 100]

# YOUR CODE HERE


# SOLUTION:
# even_squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]
# print(even_squares)

print("-" * 50)


# --- Problem E4 -----------------------------------------------
# 🔴 Challenge
# Given the dictionary of product prices in rupees below, use a
# dict comprehension to build a NEW dictionary containing only the
# products priced under 100, with prices converted to a 10% discount
# price.
# Expected output:
#   {'pen': 9.0, 'notebook': 54.0, 'eraser': 4.5}

product_prices = {"pen": 10, "notebook": 60, "eraser": 5, "bag": 450, "bottle": 150}

# YOUR CODE HERE


# SOLUTION:
# discounted_cheap_items = {
#     product: price * 0.9
#     for product, price in product_prices.items()
#     if price < 100
# }
# print(discounted_cheap_items)

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION F — Mixed Challenges (combines Days 1-6)
# ════════════════════════════════════════════════════════════

# --- Problem F1 -----------------------------------------------
# 🟡 Core
# Given a list of student tuples (name, marks), write a loop that
# builds a dictionary mapping name -> marks, then print only the
# students who scored 80 or above using a dict comprehension on
# the result.
# Expected output:
#   {'Priya': 91, 'Riya': 88}

student_tuples = [("Priya", 91), ("Sanjay", 74), ("Riya", 88), ("Arjun", 67)]

# YOUR CODE HERE


# SOLUTION:
# student_dict = {}
# for name, marks in student_tuples:
#     student_dict[name] = marks
# top_students = {name: marks for name, marks in student_dict.items() if marks >= 80}
# print(top_students)

print("-" * 50)


# --- Problem F2 -----------------------------------------------
# 🔴 Challenge
# Given the list of daily expenses (in rupees) for a week, write a
# function `weekly_summary(expenses)` that returns a tuple of
# (total, average, highest, lowest). Call it and print each value
# on its own line, formatted to 2 decimal places for the average.
# Expected output:
#   Total: 6300
#   Average: 900.00
#   Highest: 1800
#   Lowest: 300

week_expenses = [900, 1200, 300, 1800, 700, 850, 550]

# YOUR CODE HERE


# SOLUTION:
# def weekly_summary(expenses):
#     total = sum(expenses)
#     average = total / len(expenses)
#     highest = max(expenses)
#     lowest = min(expenses)
#     return total, average, highest, lowest
#
# total, average, highest, lowest = weekly_summary(week_expenses)
# print(f"Total: {total}")
# print(f"Average: {average:.2f}")
# print(f"Highest: {highest}")
# print(f"Lowest: {lowest}")

print("-" * 50)


# --- Problem F3 -----------------------------------------------
# 🔴 Challenge
# Given the list of orders below, where each order is a dictionary
# with 'customer', 'city', and 'amount' keys, write code that:
#   1. Builds a set of all unique cities that placed orders
#   2. Builds a dict mapping each city to its TOTAL order amount
#      using a loop (comprehensions alone can't easily accumulate)
# Expected output:
#   Unique cities: {'Mumbai', 'Delhi'}
#   City totals: {'Mumbai': 1450, 'Delhi': 600}

orders = [
    {"customer": "Priya", "city": "Mumbai", "amount": 950},
    {"customer": "Sanjay", "city": "Delhi", "amount": 600},
    {"customer": "Riya", "city": "Mumbai", "amount": 500},
]

# YOUR CODE HERE


# SOLUTION:
# unique_cities = {order["city"] for order in orders}
# city_totals = {}
# for order in orders:
#     city = order["city"]
#     city_totals[city] = city_totals.get(city, 0) + order["amount"]
# print("Unique cities:", unique_cities)
# print("City totals:", city_totals)

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: E (Sets & Comprehensions), F (Mixed Challenges)
# Difficulty breakdown: 1x Warm-up, 3x Core, 3x Challenge
# Total problems in this file: 7
#
# ─── Day 6 Practice Set — Full Overview ───
#   File 1: Section A (Prior Review) + Section B (Lists)     — 6 problems
#   File 2: Section C (Tuples)                                — 3 problems
#   File 3: Section D (Dictionaries)                          — 4 problems
#   File 4: Section E (Sets/Comprehensions) + F (Mixed)       — 7 problems
#   TOTAL: 20 problems across 6 sections
#
# Next up: Day 7 practice problems will cover Strings & String Methods.
