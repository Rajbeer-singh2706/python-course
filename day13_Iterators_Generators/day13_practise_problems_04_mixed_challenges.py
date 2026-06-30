"""
Day 13 — Iterators & Generators
Practice Problem Set — File 4 of 4

Section Index:
    Section E — Mixed Challenges (combines Day 13 + Days 1-12)

Difficulty Legend:
    🟢 Warm-up   🟡 Core   🔴 Challenge

How to run:
    python day13_practise_problems_04_mixed_challenges.py
"""

from itertools import islice, chain

# ════════════════════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges
# ════════════════════════════════════════════════════════════════════════

# Problem E1  🟡 Core
# Combine OOP (Day 10-11) with generators: write a class `Inventory` that
# stores a dict of {item_name: quantity}. Add a method `low_stock(threshold)`
# that is a GENERATOR yielding item names whose quantity is below the
# threshold.

# YOUR CODE HERE


# SOLUTION:
# class Inventory:
#     def __init__(self, stock):
#         self.stock = stock
#
#     def low_stock(self, threshold):
#         for item, qty in self.stock.items():
#             if qty < threshold:
#                 yield item
#
# shop = Inventory({"Notebook": 5, "Pen": 50, "Eraser": 2, "Ruler": 30})
# print(list(shop.low_stock(10)))
# # Output: ['Notebook', 'Eraser']

print("-" * 50)

# Problem E2  🟡 Core
# Combine file I/O concepts (Day 8) with generators: write a generator
# function `parse_csv_lines(lines)` that takes a list of strings like
# "Priya,250" and yields tuples (name, int(amount)). Simulate the file
# content as a list instead of actually reading a file.

# YOUR CODE HERE


# SOLUTION:
# def parse_csv_lines(lines):
#     for line in lines:
#         name, amount = line.split(",")
#         yield name, int(amount)
#
# raw_lines = ["Priya,250", "Arjun,500", "Riya,1200"]
# for name, amount in parse_csv_lines(raw_lines):
#     print(f"{name}: Rs.{amount}")
# # Output:
# # Priya: Rs.250
# # Arjun: Rs.500
# # Riya: Rs.1200

print("-" * 50)

# Problem E3  🟡 Core
# Combine error handling (Day 9) with generators: write a generator
# function `safe_divide_all(pairs)` that takes a list of (a, b) tuples and
# yields a / b for each pair, but yields None instead of crashing when b
# is 0 (use try/except inside the generator).

# YOUR CODE HERE


# SOLUTION:
# def safe_divide_all(pairs):
#     for a, b in pairs:
#         try:
#             yield a / b
#         except ZeroDivisionError:
#             yield None
#
# data = [(10, 2), (8, 0), (9, 3)]
# print(list(safe_divide_all(data)))
# # Output: [5.0, None, 3.0]

print("-" * 50)

# Problem E4  🔴 Challenge
# Build a custom iterator class `PaginatedResults` (combining Day 10-11
# OOP with Day 13 iterator protocol) that takes a list of items and a
# page_size, and iterates page-by-page (each __next__ call returns one
# full page as a list, not one item).

# YOUR CODE HERE


# SOLUTION:
# class PaginatedResults:
#     def __init__(self, items, page_size):
#         self.items = items
#         self.page_size = page_size
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.items):
#             raise StopIteration
#         page = self.items[self.index:self.index + self.page_size]
#         self.index += self.page_size
#         return page
#
# search_results = [f"Item-{i}" for i in range(1, 8)]
# for page in PaginatedResults(search_results, page_size=3):
#     print(page)
# # Output:
# # ['Item-1', 'Item-2', 'Item-3']
# # ['Item-4', 'Item-5', 'Item-6']
# # ['Item-7']

print("-" * 50)

# Problem E5  🔴 Challenge
# Combine strings (Day 7), modules (Day 12 — datetime), and generator
# expressions: given a list of order timestamps as strings in "YYYY-MM-DD"
# format, use a generator expression with the `datetime` module to yield
# only the orders placed in the year 2025, then collect them into a list.
# orders = ["2024-11-02", "2025-01-15", "2025-06-20", "2023-09-10"]

# YOUR CODE HERE


# SOLUTION:
# from datetime import datetime
# orders = ["2024-11-02", "2025-01-15", "2025-06-20", "2023-09-10"]
# orders_2025 = list(
#     o for o in orders if datetime.strptime(o, "%Y-%m-%d").year == 2025
# )
# print(orders_2025)
# # Output: ['2025-01-15', '2025-06-20']

print("-" * 50)

# Problem E6  🔴 Challenge
# Final boss: combine EVERYTHING — write a generator function
# `process_orders(orders)` where each order is a dict like
# {"customer": "Sanjay Verma", "amount": 750, "city": "Mumbai"}. The
# generator should yield a formatted string for each order, but SKIP
# (not yield) any order with amount <= 0, and should stop completely
# (early return) after yielding 3 valid orders, even if more remain.
# Then use itertools.islice defensively as a safety net when consuming it
# (limit to 5, even though the generator stops itself at 3).

# YOUR CODE HERE


# SOLUTION:
# def process_orders(orders):
#     yielded = 0
#     for order in orders:
#         if order["amount"] <= 0:
#             continue
#         yield f"{order['customer']} ({order['city']}): Rs.{order['amount']}"
#         yielded += 1
#         if yielded == 3:
#             return
#
# all_orders = [
#     {"customer": "Sanjay Verma", "amount": 750, "city": "Mumbai"},
#     {"customer": "Priya", "amount": -50, "city": "Delhi"},
#     {"customer": "Arjun", "amount": 1200, "city": "Mumbai"},
#     {"customer": "Riya Deshmukh", "amount": 300, "city": "Delhi"},
#     {"customer": "Meera", "amount": 900, "city": "Mumbai"},
# ]
# results = list(islice(process_orders(all_orders), 5))
# for line in results:
#     print(line)
# # Output:
# # Sanjay Verma (Mumbai): Rs.750
# # Arjun (Mumbai): Rs.1200
# # Riya Deshmukh (Delhi): Rs.300

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SUMMARY — Day 13 Practice Set (All Files)
# ════════════════════════════════════════════════════════════════════════
# File 1 — Section A (Review, 3 problems) + Section B (Iterator Basics, 5 problems)
# File 2 — Section C (Generator Functions, 7 problems)
# File 3 — Section D (Generator Expressions & itertools, 7 problems)
# File 4 — Section E (Mixed Challenges, 6 problems)
#
# Total problems: 28 across 4 files
# Difficulty breakdown: 5x Warm-up, 13x Core, 10x Challenge
#
# Next session: Day 14 — Decorators & Closures. The next practice set will
# build on first-class functions and the wrapping pattern, reusing today's
# generator and iterator concepts where relevant.

if __name__ == "__main__":
    print("Day 13 Practice Set, File 4 — Mixed Challenges: file loaded successfully.")
