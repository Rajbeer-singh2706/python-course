"""
Day 15 — Functional Programming
File 3 of 3: zip(), enumerate(), and sorted() with key=

Covers:
    - zip() — pairing multiple iterables together
    - Building dictionaries from zip()
    - enumerate() — tracking index and value together
    - sorted() with a key= function for custom sort rules
    - Multi-key sorting and sorting dictionaries/tuples

Prerequisites:
    - day15_01_lambda_functions.py (lambda syntax)
    - day15_02_map_filter_reduce.py (functional style)
    - Day 13 (Iterators & Generators) — itertools basics

How to run:
    python day15_03_zip_enumerate_sorted.py
"""

# ══════════════════════════════════════════════════════════════
# SECTION 1 — zip(): Pairing Iterables Together
# ══════════════════════════════════════════════════════════════
# zip(iter1, iter2, ...) walks through multiple iterables in lockstep,
# producing tuples of corresponding items. It stops as soon as the
# SHORTEST iterable runs out.

print("═" * 50)
print("SECTION 1: zip()")
print("═" * 50)

students = ["Priya", "Arjun", "Meera"]
marks = [88, 76, 92]

# Pair names with marks
for name, mark in zip(students, marks):
    print(f"{name}: {mark}")
# Output: Priya: 88
#         Arjun: 76
#         Meera: 92

# zip() with three iterables
cities = ["Mumbai", "Delhi", "Bengaluru"]
for name, mark, city in zip(students, marks, cities):
    print(f"{name} ({city}): {mark}")
# Output: Priya (Mumbai): 88
#         Arjun (Delhi): 76
#         Meera (Bengaluru): 92

# zip() stops at the shortest iterable — no error, just fewer pairs
short_list = [1, 2]
long_list = [10, 20, 30, 40]
print(list(zip(short_list, long_list)))
# Output: [(1, 10), (2, 20)]


# ══════════════════════════════════════════════════════════════
# SECTION 2 — Building Dictionaries With zip()
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION 2: Building Dictionaries With zip()")
print("═" * 50)

# A very common pattern: two related lists → one dictionary
train_names = ["Rajdhani Express", "Shatabdi Express", "Duronto Express"]
platform_numbers = [4, 7, 2]

platform_lookup = dict(zip(train_names, platform_numbers))
print(platform_lookup)
# Output: {'Rajdhani Express': 4, 'Shatabdi Express': 7, 'Duronto Express': 2}

# Unzipping — the reverse operation, using zip(*pairs)
pairs = [("Priya", 88), ("Arjun", 76), ("Meera", 92)]
names_unzipped, marks_unzipped = zip(*pairs)
print(names_unzipped)   # Output: ('Priya', 'Arjun', 'Meera')
print(marks_unzipped)   # Output: (88, 76, 92)


# ══════════════════════════════════════════════════════════════
# SECTION 3 — enumerate(): Index and Value Together
# ══════════════════════════════════════════════════════════════
# enumerate(iterable, start=0) yields (index, value) tuples — no more
# range(len(...)) needed just to track position while looping.

print()
print("═" * 50)
print("SECTION 3: enumerate()")
print("═" * 50)

menu_items = ["Butter Chicken", "Paneer Tikka", "Dal Makhani"]

# Default start at 0
for index, item in enumerate(menu_items):
    print(f"{index}: {item}")
# Output: 0: Butter Chicken
#         1: Paneer Tikka
#         2: Dal Makhani

# Custom start — useful for human-friendly numbering
for rank, item in enumerate(menu_items, start=1):
    print(f"Item #{rank}: {item}")
# Output: Item #1: Butter Chicken
#         Item #2: Paneer Tikka
#         Item #3: Dal Makhani

# enumerate() combined with a list comprehension
numbered_menu = [f"{i}. {item}" for i, item in enumerate(menu_items, start=1)]
print(numbered_menu)
# Output: ['1. Butter Chicken', '2. Paneer Tikka', '3. Dal Makhani']


# ══════════════════════════════════════════════════════════════
# SECTION 4 — sorted() With key=
# ══════════════════════════════════════════════════════════════
# By default sorted() compares items directly. The key= argument lets
# you supply a function that extracts the value to compare BY, without
# changing what gets returned.

print()
print("═" * 50)
print("SECTION 4: sorted() With key=")
print("═" * 50)

transactions = [
    {"merchant": "Zomato", "amount": 450},
    {"merchant": "Ola", "amount": 180},
    {"merchant": "BookMyShow", "amount": 900},
]

# Sort by amount, ascending (default)
by_amount = sorted(transactions, key=lambda t: t["amount"])
print([t["merchant"] for t in by_amount])
# Output: ['Ola', 'Zomato', 'BookMyShow']

# Sort by amount, descending
by_amount_desc = sorted(transactions, key=lambda t: t["amount"], reverse=True)
print([t["merchant"] for t in by_amount_desc])
# Output: ['BookMyShow', 'Zomato', 'Ola']

# Sort strings by length instead of alphabetically
words = ["Bengaluru", "Pune", "Delhi", "Mumbai"]
by_length = sorted(words, key=len)
print(by_length)
# Output: ['Pune', 'Delhi', 'Mumbai', 'Bengaluru']

# Sort tuples by their second element
scores = [("Arjun", 76), ("Priya", 88), ("Meera", 92)]
by_score = sorted(scores, key=lambda pair: pair[1], reverse=True)
print(by_score)
# Output: [('Meera', 92), ('Priya', 88), ('Arjun', 76)]


# ══════════════════════════════════════════════════════════════
# SECTION 5 — Multi-Key Sorting
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION 5: Multi-Key Sorting")
print("═" * 50)

# key= can return a TUPLE — Python compares tuples element by element,
# so this sorts by the first value, then breaks ties with the second.
orders = [
    {"city": "Mumbai", "amount": 500},
    {"city": "Delhi", "amount": 800},
    {"city": "Mumbai", "amount": 300},
    {"city": "Delhi", "amount": 200},
]

# Sort by city (A–Z), then by amount (high to low) within each city
sorted_orders = sorted(orders, key=lambda o: (o["city"], -o["amount"]))
for o in sorted_orders:
    print(o)
# Output: {'city': 'Delhi', 'amount': 800}
#         {'city': 'Delhi', 'amount': 200}
#         {'city': 'Mumbai', 'amount': 500}
#         {'city': 'Mumbai', 'amount': 300}


# ══════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1 — zip() two lists into a dictionary of product → price.
product_names = ["Notebook", "Pen", "Backpack"]
product_prices = [60, 10, 899]
catalog = dict(zip(product_names, product_prices))
print(f"Example 1: {catalog}")
# Output: Example 1: {'Notebook': 60, 'Pen': 10, 'Backpack': 899}
print("-" * 50)

# Example 2 — enumerate() to build a numbered attendance sheet.
attendees = ["Sanjay", "Riya", "Arjun"]
sheet = [f"{i}) {name}" for i, name in enumerate(attendees, start=1)]
print(f"Example 2: {sheet}")
# Output: Example 2: ['1) Sanjay', '2) Riya', '3) Arjun']
print("-" * 50)

# Example 3 — sorted() to rank Swiggy restaurants by rating (desc).
restaurants = [("South Spice", 4.7), ("Punjabi Tadka", 4.2), ("Bengal Bites", 4.4)]
ranked = sorted(restaurants, key=lambda r: r[1], reverse=True)
print(f"Example 3: {ranked}")
# Output: Example 3: [('South Spice', 4.7), ('Bengal Bites', 4.4), ('Punjabi Tadka', 4.2)]
print("-" * 50)

# Example 4 — zip() three lists to print a formatted IRCTC ticket summary.
passengers = ["Meera", "Arjun"]
seat_numbers = ["B2-45", "B2-46"]
statuses = ["Confirmed", "Confirmed"]
for p, s, st in zip(passengers, seat_numbers, statuses):
    print(f"Example 4: {p} — Seat {s} ({st})")
# Output: Example 4: Meera — Seat B2-45 (Confirmed)
#         Example 4: Arjun — Seat B2-46 (Confirmed)
print("-" * 50)

# Example 5 — Multi-key sort: Flipkart orders by status, then amount desc.
flipkart_orders = [
    {"status": "Delivered", "amount": 1200},
    {"status": "Pending", "amount": 450},
    {"status": "Delivered", "amount": 3000},
]
sorted_flipkart = sorted(flipkart_orders, key=lambda o: (o["status"], -o["amount"]))
print(f"Example 5: {sorted_flipkart}")
# Output: Example 5: [{'status': 'Delivered', 'amount': 3000},
#                     {'status': 'Delivered', 'amount': 1200},
#                     {'status': 'Pending', 'amount': 450}]
print("-" * 50)


# ══════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ══════════════════════════════════════════════════════════════
# Given two lists — auto_names and auto_fares — use zip() and enumerate()
# together to print a numbered fare list like:
#   1. Ola: Rs 180
#   2. Uber: Rs 210
#   3. Rapido: Rs 95
#
# auto_names = ["Ola", "Uber", "Rapido"]
# auto_fares = [180, 210, 95]

auto_names = ["Ola", "Uber", "Rapido"]
auto_fares = [180, 210, 95]

# YOUR CODE HERE


# ── Solution (uncomment to check your work) ──
# for i, (name, fare) in enumerate(zip(auto_names, auto_fares), start=1):
#     print(f"{i}. {name}: Rs {fare}")
# Output: 1. Ola: Rs 180
#         2. Uber: Rs 210
#         3. Rapido: Rs 95


# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
# In this file you learned:
#   - zip() pairs multiple iterables together, stopping at the shortest
#   - dict(zip(keys, values)) is a fast way to build a lookup dictionary
#   - enumerate() gives (index, value) pairs, with an optional start=
#   - sorted(iterable, key=fn) sorts using a custom comparison rule
#   - key= can return a tuple for multi-level sorting (with negation for
#     descending numeric sub-keys)
#
# This completes Day 15's concept files. Next: the practice problem set
# in day15_practise_problems_01_lambda_map_filter.py and
# day15_practise_problems_02_zip_enumerate_sorted.py.
#
# Tomorrow (Day 16): Concurrency Basics — threading, multiprocessing,
# and async/await with asyncio.run().
