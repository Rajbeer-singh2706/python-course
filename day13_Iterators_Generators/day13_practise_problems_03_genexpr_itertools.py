"""
Day 13 — Iterators & Generators
Practice Problem Set — File 3 of 4

Section Index:
    Section D — Generator Expressions & itertools

Difficulty Legend:
    🟢 Warm-up   🟡 Core   🔴 Challenge

How to run:
    python day13_practise_problems_03_genexpr_itertools.py
"""

from itertools import chain, islice, product, cycle

# ════════════════════════════════════════════════════════════════════════
# SECTION D — Generator Expressions & itertools
# ════════════════════════════════════════════════════════════════════════

# Problem D1  🟢 Warm-up
# Given `prices = [199, 499, 999, 1499]`, use a generator expression with
# sum() to compute the total of all prices, without building a list.

# YOUR CODE HERE


# SOLUTION:
# prices = [199, 499, 999, 1499]
# total = sum(p for p in prices)
# print(total)
# # Output: 3196

print("-" * 50)

# Problem D2  🟢 Warm-up
# Given `names = ["priya", "arjun", "riya"]`, use a generator expression
# inside list() to produce a list of the names capitalized (e.g. "Priya").

# YOUR CODE HERE


# SOLUTION:
# names = ["priya", "arjun", "riya"]
# capitalized = list(name.capitalize() for name in names)
# print(capitalized)
# # Output: ['Priya', 'Arjun', 'Riya']

print("-" * 50)

# Problem D3  🟡 Core
# Given `marks = [45, 88, 32, 91, 67]`, use any() with a generator
# expression to check if any student failed (mark below 40), and all()
# with a generator expression to check if all students passed (mark >= 40).
# Print both results.

# YOUR CODE HERE


# SOLUTION:
# marks = [45, 88, 32, 91, 67]
# any_failed = any(m < 40 for m in marks)
# all_passed = all(m >= 40 for m in marks)
# print(f"Any failed? {any_failed}")
# print(f"All passed? {all_passed}")
# # Output:
# # Any failed? True
# # All passed? False

print("-" * 50)

# Problem D4  🟡 Core
# Use itertools.chain to combine three lists of product categories:
# electronics = ["Phone", "Laptop"], groceries = ["Rice", "Atta"],
# stationery = ["Pen", "Notebook"] into a single list, and print it.

# YOUR CODE HERE


# SOLUTION:
# electronics = ["Phone", "Laptop"]
# groceries = ["Rice", "Atta"]
# stationery = ["Pen", "Notebook"]
# all_products = list(chain(electronics, groceries, stationery))
# print(all_products)
# # Output: ['Phone', 'Laptop', 'Rice', 'Atta', 'Pen', 'Notebook']

print("-" * 50)

# Problem D5  🟡 Core
# Use itertools.product to print every combination of size ("S", "M", "L")
# and fabric ("Cotton", "Linen") as a formatted string like "S - Cotton".

# YOUR CODE HERE


# SOLUTION:
# sizes = ["S", "M", "L"]
# fabrics = ["Cotton", "Linen"]
# for size, fabric in product(sizes, fabrics):
#     print(f"{size} - {fabric}")
# # Output:
# # S - Cotton
# # S - Linen
# # M - Cotton
# # M - Linen
# # L - Cotton
# # L - Linen

print("-" * 50)

# Problem D6  🔴 Challenge
# Use itertools.cycle and itertools.islice to assign 10 customer support
# tickets round-robin to agents ["Meera", "Kabir"], printing each
# assignment as "TICKET-<n> -> <agent>" for n from 1 to 10.

# YOUR CODE HERE


# SOLUTION:
# agents = cycle(["Meera", "Kabir"])
# assigned_agents = list(islice(agents, 10))
# for i, agent in enumerate(assigned_agents, start=1):
#     print(f"TICKET-{i} -> {agent}")
# # Output:
# # TICKET-1 -> Meera
# # TICKET-2 -> Kabir
# # ... (alternating) ... TICKET-10 -> Kabir

print("-" * 50)

# Problem D7  🔴 Challenge
# Write a generator `infinite_squares()` yielding 1, 4, 9, 16, ... forever.
# Use itertools.islice to grab squares at index positions 5 through 8
# (0-indexed, i.e. the 6th through 9th squares produced).

# YOUR CODE HERE


# SOLUTION:
# def infinite_squares():
#     n = 1
#     while True:
#         yield n * n
#         n += 1
#
# result = list(islice(infinite_squares(), 5, 9))
# print(result)
# # Output: [36, 49, 64, 81]

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
# Section D: 7 problems — generator expressions, chain, product, cycle, islice
# Difficulty breakdown: 2x Warm-up, 3x Core, 2x Challenge
#
# Continue to File 4 of 4 for Section E — Mixed Challenges (combining
# today's concepts with Days 1-12).

if __name__ == "__main__":
    print("Day 13 Practice Set, File 3 — Genexpr & itertools: file loaded successfully.")
