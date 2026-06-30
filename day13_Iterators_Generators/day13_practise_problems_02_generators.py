"""
Day 13 — Iterators & Generators
Practice Problem Set — File 2 of 4

Section Index:
    Section C — Generator Functions (yield)

Difficulty Legend:
    🟢 Warm-up   🟡 Core   🔴 Challenge

How to run:
    python day13_practise_problems_02_generators.py
"""

# ════════════════════════════════════════════════════════════════════════
# SECTION C — Generator Functions (yield)
# ════════════════════════════════════════════════════════════════════════

# Problem C1  🟢 Warm-up
# Write a generator function `count_up_to(n)` that yields integers from 1
# up to and including n.

# YOUR CODE HERE


# SOLUTION:
# def count_up_to(n):
#     for i in range(1, n + 1):
#         yield i
#
# print(list(count_up_to(5)))
# # Output: [1, 2, 3, 4, 5]

print("-" * 50)

# Problem C2  🟢 Warm-up
# Write a generator function `rupee_formatter(amounts)` that yields each
# amount in `amounts` formatted as a string with a ₹ prefix, e.g. "₹250".

# YOUR CODE HERE


# SOLUTION:
# def rupee_formatter(amounts):
#     for amt in amounts:
#         yield f"₹{amt}"
#
# print(list(rupee_formatter([250, 500, 750])))
# # Output: ['₹250', '₹500', '₹750']

print("-" * 50)

# Problem C3  🟡 Core
# Write a generator function `even_only(numbers)` that yields only the
# even numbers from the input list, in order.

# YOUR CODE HERE


# SOLUTION:
# def even_only(numbers):
#     for n in numbers:
#         if n % 2 == 0:
#             yield n
#
# print(list(even_only([3, 8, 15, 22, 7, 4])))
# # Output: [8, 22, 4]

print("-" * 50)

# Problem C4  🟡 Core
# Write a generator function `running_total(amounts)` that yields the
# cumulative running total of a list of order amounts (rupees), one yield
# per item added.

# YOUR CODE HERE


# SOLUTION:
# def running_total(amounts):
#     total = 0
#     for amt in amounts:
#         total += amt
#         yield total
#
# print(list(running_total([100, 250, 75, 400])))
# # Output: [100, 350, 425, 825]

print("-" * 50)

# Problem C5  🟡 Core
# Write a generator function `fibonacci(n)` that yields the first n
# numbers of the Fibonacci sequence, starting 0, 1, 1, 2, 3, 5, ...

# YOUR CODE HERE


# SOLUTION:
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# print(list(fibonacci(8)))
# # Output: [0, 1, 1, 2, 3, 5, 8, 13]

print("-" * 50)

# Problem C6  🔴 Challenge
# Write a generator function `batch(items, size)` that yields successive
# lists ("batches") of up to `size` items from `items`. The final batch
# may be smaller. Useful for processing large order lists in chunks.
# Example: batch([1,2,3,4,5], 2) -> [1,2], [2,3]... wait, careful: it
# should yield [1,2], [3,4], [5] (non-overlapping batches).

# YOUR CODE HERE


# SOLUTION:
# def batch(items, size):
#     current = []
#     for item in items:
#         current.append(item)
#         if len(current) == size:
#             yield current
#             current = []
#     if current:
#         yield current
#
# print(list(batch([1, 2, 3, 4, 5], 2)))
# # Output: [[1, 2], [3, 4], [5]]

print("-" * 50)

# Problem C7  🔴 Challenge
# Write a generator function `infinite_odd_numbers()` that yields odd
# numbers forever (1, 3, 5, 7, ...). Then, WITHOUT writing an infinite
# loop yourself, print just the first 6 odd numbers it produces (hint:
# you may use a manual counter with next(), since itertools.islice is
# covered in the next file).

# YOUR CODE HERE


# SOLUTION:
# def infinite_odd_numbers():
#     n = 1
#     while True:
#         yield n
#         n += 2
#
# gen = infinite_odd_numbers()
# first_six = [next(gen) for _ in range(6)]
# print(first_six)
# # Output: [1, 3, 5, 7, 9, 11]

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
# Section C: 7 problems — writing generator functions with yield
# Difficulty breakdown: 2x Warm-up, 3x Core, 2x Challenge
#
# Continue to File 3 of 4 for Section D — Generator Expressions.

if __name__ == "__main__":
    print("Day 13 Practice Set, File 2 — Generator Functions: file loaded successfully.")
