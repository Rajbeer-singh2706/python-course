"""
Day 15 — Functional Programming — Practice Problem Set
File 2 of 2: Section D (zip/enumerate/sorted), Section E (Mixed Challenges)

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines a few steps, still single-concept
    🔴 Challenge — multi-step or combines several ideas

Section Index (this file):
    Section D — zip() / enumerate() / sorted(key=)   (5 problems)
    Section E — Mixed Challenges                      (3 problems)

(Section A — Prior Days Review, Section B — Lambda, and Section C —
 map()/filter()/reduce() are in
 day15_practise_problems_01_lambda_map_filter.py)

How to run:
    python day15_practise_problems_02_zip_enumerate_sorted.py
"""

from functools import reduce

# ══════════════════════════════════════════════════════════════
# SECTION D — zip() / enumerate() / sorted(key=)
# ══════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION D: zip() / enumerate() / sorted(key=)")
print("═" * 50)

# ── Problem D1 ──
# 🟢 Warm-up
# Use zip() to pair these two lists and print each pair as
# "<city>: Rs <fare>" on its own line.
#
# cities = ["Mumbai", "Pune", "Nashik"]
# bus_fares = [450, 320, 280]
#
# Expected output:
#   Mumbai: Rs 450
#   Pune: Rs 320
#   Nashik: Rs 280

cities = ["Mumbai", "Pune", "Nashik"]
bus_fares = [450, 320, 280]

# YOUR CODE HERE


# ── SOLUTION ──
# for city, fare in zip(cities, bus_fares):
#     print(f"{city}: Rs {fare}")
# Output: Mumbai: Rs 450
#         Pune: Rs 320
#         Nashik: Rs 280

print("-" * 50)

# ── Problem D2 ──
# 🟢 Warm-up
# Use enumerate() to print each item in this Swiggy order list numbered
# starting from 1, in the format "<number>. <item>".
#
# order_items = ["Butter Naan", "Paneer Tikka", "Gulab Jamun"]
#
# Expected output:
#   1. Butter Naan
#   2. Paneer Tikka
#   3. Gulab Jamun

order_items = ["Butter Naan", "Paneer Tikka", "Gulab Jamun"]

# YOUR CODE HERE


# ── SOLUTION ──
# for i, item in enumerate(order_items, start=1):
#     print(f"{i}. {item}")
# Output: 1. Butter Naan
#         2. Paneer Tikka
#         3. Gulab Jamun

print("-" * 50)

# ── Problem D3 ──
# 🟡 Core
# Use zip() to build a dictionary mapping product name → price from these
# two lists.
#
# product_names = ["Laptop Sleeve", "USB Cable", "Mouse Pad"]
# product_prices = [499, 149, 199]
#
# Expected output:
#   {'Laptop Sleeve': 499, 'USB Cable': 149, 'Mouse Pad': 199}

product_names = ["Laptop Sleeve", "USB Cable", "Mouse Pad"]
product_prices = [499, 149, 199]

# YOUR CODE HERE
price_lookup = {}

# ── SOLUTION ──
# price_lookup = dict(zip(product_names, product_prices))
# print(price_lookup)
# Output: {'Laptop Sleeve': 499, 'USB Cable': 149, 'Mouse Pad': 199}

print("-" * 50)

# ── Problem D4 ──
# 🟡 Core
# Use sorted() with key= to sort this list of employee dictionaries by
# "salary" in descending order. Print just the names in order.
#
# employees = [
#     {"name": "Sanjay", "salary": 65000},
#     {"name": "Riya", "salary": 92000},
#     {"name": "Arjun", "salary": 78000},
# ]
#
# Expected output:
#   ['Riya', 'Arjun', 'Sanjay']

employees = [
    {"name": "Sanjay", "salary": 65000},
    {"name": "Riya", "salary": 92000},
    {"name": "Arjun", "salary": 78000},
]

# YOUR CODE HERE
names_by_salary = []

# ── SOLUTION ──
# ranked = sorted(employees, key=lambda e: e["salary"], reverse=True)
# names_by_salary = [e["name"] for e in ranked]
# print(names_by_salary)   # Output: ['Riya', 'Arjun', 'Sanjay']

print("-" * 50)

# ── Problem D5 ──
# 🔴 Challenge
# Use sorted() with a multi-key key= to sort these IRCTC bookings first by
# "status" (alphabetically), then by "fare" descending within each status.
#
# bookings = [
#     {"pnr": "PNR001", "status": "Confirmed", "fare": 1200},
#     {"pnr": "PNR002", "status": "Waitlisted", "fare": 450},
#     {"pnr": "PNR003", "status": "Confirmed", "fare": 800},
#     {"pnr": "PNR004", "status": "Waitlisted", "fare": 600},
# ]
#
# Expected output (list of PNRs in sorted order):
#   ['PNR001', 'PNR003', 'PNR004', 'PNR002']

bookings = [
    {"pnr": "PNR001", "status": "Confirmed", "fare": 1200},
    {"pnr": "PNR002", "status": "Waitlisted", "fare": 450},
    {"pnr": "PNR003", "status": "Confirmed", "fare": 800},
    {"pnr": "PNR004", "status": "Waitlisted", "fare": 600},
]

# YOUR CODE HERE
sorted_pnrs = []

# ── SOLUTION ──
# sorted_bookings = sorted(bookings, key=lambda b: (b["status"], -b["fare"]))
# sorted_pnrs = [b["pnr"] for b in sorted_bookings]
# print(sorted_pnrs)   # Output: ['PNR001', 'PNR003', 'PNR004', 'PNR002']

print("-" * 50)


# ══════════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION E: Mixed Challenges")
print("═" * 50)

# ── Problem E1 ──
# 🔴 Challenge
# Combine map(), filter(), and sorted(): from this list of Flipkart order
# amounts, apply a 10% discount to orders above Rs 1000 using map()+filter(),
# then sort the discounted amounts in ascending order.
#
# order_amounts = [850, 1500, 2200, 999, 3000]
#
# Expected output:
#   [1350.0, 1980.0, 2700.0]

order_amounts = [850, 1500, 2200, 999, 3000]

# YOUR CODE HERE
sorted_discounted = []

# ── SOLUTION ──
# discounted = list(map(lambda a: round(a * 0.9, 2), filter(lambda a: a > 1000, order_amounts)))
# sorted_discounted = sorted(discounted)
# print(sorted_discounted)   # Output: [1350.0, 1980.0, 2700.0]

print("-" * 50)

# ── Problem E2 ──
# 🔴 Challenge
# Combine zip() and reduce(): given two lists of match scores for two
# cricket teams across 3 matches, use zip() to pair the scores per match,
# then use reduce() to find the total combined score across all matches
# and all teams.
#
# team_a_scores = [180, 210, 165]
# team_b_scores = [175, 190, 200]
#
# Expected output:
#   1120

team_a_scores = [180, 210, 165]
team_b_scores = [175, 190, 200]

# YOUR CODE HERE
grand_total = None

# ── SOLUTION ──
# match_totals = [a + b for a, b in zip(team_a_scores, team_b_scores)]
# grand_total = reduce(lambda acc, total: acc + total, match_totals)
# print(grand_total)   # Output: 1120

print("-" * 50)

# ── Problem E3 ──
# 🔴 Challenge
# Combine enumerate() and sorted(): given a list of Zomato restaurant
# names in the order a delivery agent visited them, print a numbered list
# (starting at 1) of the restaurant names sorted alphabetically.
#
# visited = ["South Spice", "Bengal Bites", "Punjabi Tadka", "Amritsari Dhaba"]
#
# Expected output:
#   1. Amritsari Dhaba
#   2. Bengal Bites
#   3. Punjabi Tadka
#   4. South Spice

visited = ["South Spice", "Bengal Bites", "Punjabi Tadka", "Amritsari Dhaba"]

# YOUR CODE HERE


# ── SOLUTION ──
# for i, name in enumerate(sorted(visited), start=1):
#     print(f"{i}. {name}")
# Output: 1. Amritsari Dhaba
#         2. Bengal Bites
#         3. Punjabi Tadka
#         4. South Spice

print("-" * 50)


# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
# Sections completed in this file:
#   Section D — zip()/enumerate()/sorted(key=)   (5 problems: 2 🟢, 2 🟡, 1 🔴)
#   Section E — Mixed Challenges                  (3 problems: 3 🔴)
#
# Combined with day15_practise_problems_01_lambda_map_filter.py:
#   Section A — Prior Days Review           2 problems
#   Section B — Lambda Expressions          4 problems
#   Section C — map()/filter()/reduce()     5 problems
#   Section D — zip()/enumerate()/sorted()  5 problems
#   Section E — Mixed Challenges            3 problems
#   ─────────────────────────────────────────────────
#   TOTAL: 19 problems (7 🟢, 6 🟡, 6 🔴)
#
# Next up: Day 16 — Concurrency Basics
#   threading, multiprocessing, and async/await with asyncio.run()
