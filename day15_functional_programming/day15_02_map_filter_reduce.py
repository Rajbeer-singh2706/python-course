"""
Day 15 — Functional Programming
File 2 of 3: map(), filter(), and reduce()

Covers:
    - map() — applying a function to every item in an iterable
    - filter() — keeping only items that satisfy a condition
    - functools.reduce() — combining all items into a single value
    - Chaining map() and filter() together
    - Comparing functional style to an equivalent for-loop / comprehension

Prerequisites:
    - day15_01_lambda_functions.py (lambda syntax)
    - Day 6 (Data Structures) — lists, list comprehensions

How to run:
    python day15_02_map_filter_reduce.py
"""

from functools import reduce

# ══════════════════════════════════════════════════════════════
# SECTION 1 — map(): Transform Every Item
# ══════════════════════════════════════════════════════════════
# map(function, iterable) applies "function" to every item in "iterable"
# and returns a lazy iterator (not a list!). Wrap it in list() to see
# the values immediately, or loop over it directly.

print("═" * 50)
print("SECTION 1: map()")
print("═" * 50)

cart_prices = [249, 499, 129, 899, 349]   # Arjun's Swiggy cart, in rupees

# Add 5% GST to every price
with_gst = list(map(lambda p: round(p * 1.05, 2), cart_prices))
print(with_gst)
# Output: [261.45, 523.95, 135.45, 943.95, 366.45]

# map() also works with an already-defined function (no lambda needed)
def add_delivery_fee(price):
    return price + 40

with_fee = list(map(add_delivery_fee, cart_prices))
print(with_fee)
# Output: [289, 539, 169, 939, 389]

# map() can take MORE than one iterable — it applies the function
# pairwise across both, stopping at the shorter one.
mrp = [300, 550, 150]
selling_price = [249, 499, 129]
savings = list(map(lambda m, s: m - s, mrp, selling_price))
print(savings)
# Output: [51, 51, 21]


# ══════════════════════════════════════════════════════════════
# SECTION 2 — filter(): Keep Only What Matches
# ══════════════════════════════════════════════════════════════
# filter(function, iterable) keeps only the items for which "function"
# returns True. Like map(), it returns a lazy iterator.

print()
print("═" * 50)
print("SECTION 2: filter()")
print("═" * 50)

# Keep only items priced above Rs 300
premium_items = list(filter(lambda p: p > 300, cart_prices))
print(premium_items)
# Output: [499, 899, 349]

# Filtering a list of dictionaries — students who passed (marks >= 40)
students = [
    {"name": "Arjun", "marks": 76},
    {"name": "Priya", "marks": 32},
    {"name": "Meera", "marks": 92},
    {"name": "Sanjay", "marks": 18},
]
passed = list(filter(lambda s: s["marks"] >= 40, students))
print([s["name"] for s in passed])
# Output: ['Arjun', 'Meera']

# filter(None, iterable) is a shortcut to remove "falsy" values
# (empty strings, 0, None, False, empty lists, etc.)
mixed_data = ["Riya", "", "Sanjay", None, "Meera", 0]
clean_data = list(filter(None, mixed_data))
print(clean_data)
# Output: ['Riya', 'Sanjay', 'Meera']


# ══════════════════════════════════════════════════════════════
# SECTION 3 — Chaining map() and filter()
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION 3: Chaining map() and filter()")
print("═" * 50)

# First filter premium items, then apply a 10% loyalty discount to them
discounted_premium = list(
    map(lambda p: round(p * 0.9, 2),
        filter(lambda p: p > 300, cart_prices))
)
print(discounted_premium)
# Output: [449.1, 809.1, 314.1]

# The equivalent list comprehension (often more readable for simple cases):
discounted_premium_comp = [round(p * 0.9, 2) for p in cart_prices if p > 300]
print(discounted_premium_comp)
# Output: [449.1, 809.1, 314.1]


# ══════════════════════════════════════════════════════════════
# SECTION 4 — reduce(): Combine Everything Into One Value
# ══════════════════════════════════════════════════════════════
# reduce(function, iterable, [initial]) repeatedly applies "function" to
# pairs of items, carrying forward a running result, until only one
# value remains. It lives in functools, not the builtins.

print()
print("═" * 50)
print("SECTION 4: reduce()")
print("═" * 50)

# Total cart value
total = reduce(lambda acc, price: acc + price, cart_prices)
print(total)
# Output: 2125

# reduce() with an initial value (useful when starting from a non-zero base,
# e.g. adding a flat Rs 50 packaging fee before summing)
total_with_fee = reduce(lambda acc, price: acc + price, cart_prices, 50)
print(total_with_fee)
# Output: 2175

# Finding the most expensive item using reduce()
most_expensive = reduce(lambda a, b: a if a > b else b, cart_prices)
print(most_expensive)
# Output: 899

# NOTE: For sums, Python's built-in sum() is simpler than reduce().
# reduce() is most valuable when the combining logic is NOT a simple
# sum/max/min (those already have built-ins) — e.g. building a running
# string, merging dictionaries, or custom accumulation logic.
order_ids = ["ORD1", "ORD2", "ORD3"]
combined_id = reduce(lambda acc, oid: acc + "-" + oid, order_ids)
print(combined_id)
# Output: ORD1-ORD2-ORD3


# ══════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1 — Convert a list of city names to uppercase using map().
cities = ["mumbai", "delhi", "bengaluru"]
upper_cities = list(map(str.upper, cities))
print(f"Example 1: {upper_cities}")
# Output: Example 1: ['MUMBAI', 'DELHI', 'BENGALURU']
print("-" * 50)

# Example 2 — Filter out IRCTC bookings that are not "Confirmed".
bookings = [
    {"pnr": "PNR001", "status": "Confirmed"},
    {"pnr": "PNR002", "status": "Waitlisted"},
    {"pnr": "PNR003", "status": "Confirmed"},
]
confirmed = list(filter(lambda b: b["status"] == "Confirmed", bookings))
print(f"Example 2: {[b['pnr'] for b in confirmed]}")
# Output: Example 2: ['PNR001', 'PNR003']
print("-" * 50)

# Example 3 — Use reduce() to find the total distance of a multi-leg train trip.
leg_distances = [120, 340, 89, 210]   # km
total_distance = reduce(lambda acc, d: acc + d, leg_distances)
print(f"Example 3: {total_distance} km")
# Output: Example 3: 759 km
print("-" * 50)

# Example 4 — Chain map + filter to get discounted prices of Flipkart
# electronics that are above Rs 1000.
electronics = [850, 1200, 2500, 999, 4300]
discounted_expensive = list(
    map(lambda p: round(p * 0.85, 2), filter(lambda p: p > 1000, electronics))
)
print(f"Example 4: {discounted_expensive}")
# Output: Example 4: [1020.0, 2125.0, 3655.0]
print("-" * 50)

# Example 5 — Use reduce() to merge multiple dictionaries of Zomato order counts.
daily_counts = [{"Zomato": 3}, {"Zomato": 5}, {"Zomato": 2}]
total_orders = reduce(lambda acc, d: acc + d["Zomato"], daily_counts, 0)
print(f"Example 5: {total_orders}")
# Output: Example 5: 10
print("-" * 50)


# ══════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ══════════════════════════════════════════════════════════════
# Given a list of temperatures in Celsius, use map() to convert them all
# to Fahrenheit, then use filter() to keep only the ones above 90°F.
#
# temperatures_c = [25, 32, 18, 40, 22]
#
# Expected output:
#   [95.0, 104.0]

temperatures_c = [25, 32, 18, 40, 22]

# YOUR CODE HERE
hot_days_f = []   # replace with your map()/filter() chain

# ── Solution (uncomment to check your work) ──
# fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, temperatures_c))
# hot_days_f = list(filter(lambda f: f > 90, fahrenheit))
# print(hot_days_f)   # Output: [95.0, 104.0]


# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
# In this file you learned:
#   - map(fn, iterable) transforms every item, returns a lazy iterator
#   - filter(fn, iterable) keeps only items where fn returns True
#   - reduce(fn, iterable, [init]) collapses an iterable into one value
#   - map() and filter() chain naturally; comprehensions are often clearer
#     for simple cases
#   - reduce() needs "from functools import reduce"
#
# Next file: day15_03_zip_enumerate_sorted.py
#   → Pairing iterables with zip(), tracking index+value with enumerate(),
#     and custom sorting with sorted(key=...).
