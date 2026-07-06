"""
Day 15 — Functional Programming — Practice Problem Set
File 1 of 2: Section A (Prior Days Review), Section B (Lambda), Section C (map/filter/reduce)

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines a few steps, still single-concept
    🔴 Challenge — multi-step or combines several ideas

Section Index (this file):
    Section A — Prior Days Review               (2 problems)
    Section B — Lambda Expressions               (4 problems)
    Section C — map() / filter() / reduce()      (5 problems)

(Section D — zip()/enumerate()/sorted() and Section E — Mixed Challenges
 continue in day15_practise_problems_02_zip_enumerate_sorted.py)

How to run:
    python day15_practise_problems_01_lambda_map_filter.py
"""

# ══════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ══════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION A: Prior Days Review")
print("═" * 50)

# ── Problem A1 ──
# 🟢 Warm-up
# Write a generator function (Day 13) called "count_up_to" that yields
# numbers from 1 up to and including n.
#
# Expected output (for n=5):
#   [1, 2, 3, 4, 5]

# YOUR CODE HERE


# ── SOLUTION ──
# def count_up_to(n):
#     current = 1
#     while current <= n:
#         yield current
#         current += 1
#
# print(list(count_up_to(5)))   # Output: [1, 2, 3, 4, 5]

print("-" * 50)

# ── Problem A2 ──
# 🟡 Core
# Write a decorator (Day 14) called "log_call" that prints
# "Calling <function name>" before running the wrapped function, then
# returns the function's result unchanged. Use functools.wraps.
#
# Expected output (when calling greet("Riya")):
#   Calling greet
#   Hello, Riya!

# YOUR CODE HERE


# ── SOLUTION ──
# from functools import wraps
#
# def log_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_call
# def greet(name):
#     return f"Hello, {name}!"
#
# print(greet("Riya"))
# Output: Calling greet
#         Hello, Riya!

print("-" * 50)


# ══════════════════════════════════════════════════════════════
# SECTION B — Lambda Expressions
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION B: Lambda Expressions")
print("═" * 50)

# ── Problem B1 ──
# 🟢 Warm-up
# Write a lambda called "cube" that returns the cube of a number.
#
# Expected output (for cube(3)):
#   27

# YOUR CODE HERE
cube = None   # replace with your lambda

# ── SOLUTION ──
# cube = lambda x: x ** 3
# print(cube(3))   # Output: 27

print("-" * 50)

# ── Problem B2 ──
# 🟢 Warm-up
# Write a lambda called "is_even" that returns True if a number is even.
#
# Expected output:
#   True
#   False

# YOUR CODE HERE
is_even = None   # replace with your lambda

# ── SOLUTION ──
# is_even = lambda n: n % 2 == 0
# print(is_even(10))   # Output: True
# print(is_even(7))    # Output: False

print("-" * 50)

# ── Problem B3 ──
# 🟡 Core
# Write a lambda called "irctc_fare" that takes base_fare and passenger_count
# and returns base_fare * passenger_count, with a flat Rs 20 booking fee added.
#
# Expected output (for irctc_fare(450, 3)):
#   1370

# YOUR CODE HERE
irctc_fare = None   # replace with your lambda

# ── SOLUTION ──
# irctc_fare = lambda base_fare, passenger_count: (base_fare * passenger_count) + 20
# print(irctc_fare(450, 3))   # Output: 1370

print("-" * 50)

# ── Problem B4 ──
# 🔴 Challenge
# Write a lambda called "classify_txn" that takes a Paytm transaction amount
# and returns "Large" if amount > 5000, "Medium" if amount > 1000, else "Small".
#
# Expected output:
#   Large
#   Medium
#   Small

# YOUR CODE HERE
classify_txn = None   # replace with your lambda

# ── SOLUTION ──
# classify_txn = lambda amount: "Large" if amount > 5000 else ("Medium" if amount > 1000 else "Small")
# print(classify_txn(6000))   # Output: Large
# print(classify_txn(2000))   # Output: Medium
# print(classify_txn(500))    # Output: Small

print("-" * 50)


# ══════════════════════════════════════════════════════════════
# SECTION C — map() / filter() / reduce()
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION C: map() / filter() / reduce()")
print("═" * 50)

# ── Problem C1 ──
# 🟢 Warm-up
# Use map() to convert this list of Mumbai temperatures (Celsius) to
# Fahrenheit.
#
# temps_c = [20, 25, 30, 35]
#
# Expected output:
#   [68.0, 77.0, 86.0, 95.0]

temps_c = [20, 25, 30, 35]

# YOUR CODE HERE
temps_f = []

# ── SOLUTION ──
# temps_f = list(map(lambda c: (c * 9 / 5) + 32, temps_c))
# print(temps_f)   # Output: [68.0, 77.0, 86.0, 95.0]

print("-" * 50)

# ── Problem C2 ──
# 🟢 Warm-up
# Use filter() to keep only the Flipkart order amounts greater than Rs 1000.
#
# order_amounts = [450, 1200, 899, 2500, 300]
#
# Expected output:
#   [1200, 2500]

order_amounts = [450, 1200, 899, 2500, 300]

# YOUR CODE HERE
big_orders = []

# ── SOLUTION ──
# big_orders = list(filter(lambda amt: amt > 1000, order_amounts))
# print(big_orders)   # Output: [1200, 2500]

print("-" * 50)

# ── Problem C3 ──
# 🟡 Core
# Use functools.reduce() to find the total number of Swiggy orders across
# these daily counts.
#
# daily_orders = [12, 18, 9, 25, 14]
#
# Expected output:
#   78

daily_orders = [12, 18, 9, 25, 14]

# YOUR CODE HERE
total_orders = None

# ── SOLUTION ──
# from functools import reduce
# total_orders = reduce(lambda acc, count: acc + count, daily_orders)
# print(total_orders)   # Output: 78

print("-" * 50)

# ── Problem C4 ──
# 🟡 Core
# Use map() and filter() together: from this list of student dictionaries,
# get the names (only) of students who scored 75 or above.
#
# students = [
#     {"name": "Arjun", "marks": 82},
#     {"name": "Priya", "marks": 68},
#     {"name": "Meera", "marks": 91},
# ]
#
# Expected output:
#   ['Arjun', 'Meera']

students = [
    {"name": "Arjun", "marks": 82},
    {"name": "Priya", "marks": 68},
    {"name": "Meera", "marks": 91},
]

# YOUR CODE HERE
top_names = []

# ── SOLUTION ──
# passed = filter(lambda s: s["marks"] >= 75, students)
# top_names = list(map(lambda s: s["name"], passed))
# print(top_names)   # Output: ['Arjun', 'Meera']

print("-" * 50)

# ── Problem C5 ──
# 🔴 Challenge
# Use functools.reduce() to find the Swiggy restaurant with the highest
# rating from this list of (name, rating) tuples. Return just the name.
#
# restaurant_ratings = [
#     ("Punjabi Tadka", 4.2), ("South Spice", 4.7), ("Bengal Bites", 4.4)
# ]
#
# Expected output:
#   South Spice

restaurant_ratings = [
    ("Punjabi Tadka", 4.2), ("South Spice", 4.7), ("Bengal Bites", 4.4)
]

# YOUR CODE HERE
top_restaurant = None

# ── SOLUTION ──
# from functools import reduce
# best = reduce(lambda a, b: a if a[1] > b[1] else b, restaurant_ratings)
# top_restaurant = best[0]
# print(top_restaurant)   # Output: South Spice

print("-" * 50)


# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
# Sections completed in this file:
#   Section A — Prior Days Review           (2 problems: 1 🟢, 1 🟡)
#   Section B — Lambda Expressions           (4 problems: 2 🟢, 1 🟡, 1 🔴)
#   Section C — map()/filter()/reduce()      (5 problems: 2 🟢, 2 🟡, 1 🔴)
#
# Total so far: 11 problems
#
# Continue in day15_practise_problems_02_zip_enumerate_sorted.py for:
#   Section D — zip() / enumerate() / sorted(key=)   (5 problems)
#   Section E — Mixed Challenges                      (3 problems)
