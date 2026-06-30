"""
Day 13 — Iterators & Generators
File 3 of 4: Generator Expressions

Covers:
    - Generator expression syntax: (expr for item in iterable)
    - How they differ from list/dict/set comprehensions
    - Generator exhaustion (can only be consumed once)
    - Passing generator expressions directly into functions like sum(), any()

Prerequisites:
    - Day 6: List/dict/set comprehensions
    - Day 13, File 2: Generator functions (yield)

How to run:
    python day13_03_generator_expressions.py
"""

# ════════════════════════════════════════════════════════════════════════
# SECTION A — List Comprehension vs Generator Expression
# ════════════════════════════════════════════════════════════════════════
# Same syntax shape, different brackets:
#   [expr for item in iterable]   -> list comprehension (builds full list NOW)
#   (expr for item in iterable)   -> generator expression (builds values LAZILY)

prices = [499, 1299, 250, 899, 1999]

discounted_list = [p * 0.9 for p in prices]    # computed immediately, all at once
print(discounted_list)
print(type(discounted_list))
# Output (float math can show tiny rounding artifacts, e.g. 1169.1000000000001):
# [449.1, 1169.1..., 225.0, 809.1, 1799.1...]
# <class 'list'>

discounted_gen = (p * 0.9 for p in prices)     # NOT computed yet — lazy
print(discounted_gen)
print(type(discounted_gen))
# Output:
# <generator object <genexpr> at 0x...>
# <class 'generator'>

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION B — Generators Can Only Be Consumed Once
# ════════════════════════════════════════════════════════════════════════

discounted_gen = (p * 0.9 for p in prices)
print("First sum:", sum(discounted_gen))   # Output: First sum: 4451.400000000001
print("Second sum:", sum(discounted_gen))  # Output: Second sum: 0  (already exhausted!)

# To reuse, you must create a NEW generator expression:
discounted_gen_fresh = (p * 0.9 for p in prices)
print("Fresh sum:", sum(discounted_gen_fresh))  # Output: Fresh sum: 4451.400000000001

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION C — Generator Expressions Inside Function Calls
# ════════════════════════════════════════════════════════════════════════
# When a generator expression is the SOLE argument to a function, you can
# drop the extra parentheses.

amounts = [120, 450, 999, 75, 1500]

# Without extra parens (preferred, cleaner):
total_above_100 = sum(amt for amt in amounts if amt > 100)
print(f"Total above ₹100: ₹{total_above_100}")
# Output: Total above ₹100: ₹3069

has_big_order = any(amt > 1000 for amt in amounts)
print(f"Has an order above ₹1000? {has_big_order}")
# Output: Has an order above ₹1000? True

all_orders_paid = all(amt > 0 for amt in amounts)
print(f"All orders have a positive amount? {all_orders_paid}")
# Output: All orders have a positive amount? True

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION D — Guided Examples
# ════════════════════════════════════════════════════════════════════════

# Example 1: Memory-efficient processing of a large list of names
names = ["Priya", "Arjun", "Riya", "Sanjay", "Meera", "Kabir"]
short_names_gen = (name for name in names if len(name) <= 5)
print("Example 1 — Names with 5 or fewer letters:")
for n in short_names_gen:
    print(f"  {n}")
# Output:
#   Priya
#   Arjun
#   Riya
#   Meera
print("-" * 50)


# Example 2: Combine a generator expression with f-strings to build labels lazily
order_ids = [101, 102, 103]
labels_gen = (f"ORDER-MUM-{oid}" for oid in order_ids)
print("Example 2 — Lazily built Mumbai order labels:")
for label in labels_gen:
    print(f"  {label}")
print("-" * 50)


# Example 3: Nested generator expression (like a flattened double loop)
sections = ["A", "B"]
seat_numbers = [1, 2, 3]
seat_codes_gen = (f"{sec}{num}" for sec in sections for num in seat_numbers)
print("Example 3 — Cinema seat codes for a Mumbai theatre booking:")
for code in seat_codes_gen:
    print(f"  {code}")
# Output:
#   A1
#   A2
#   A3
#   B1
#   B2
#   B3
print("-" * 50)


# Example 4: Converting a generator expression to other container types
expenses = [200, 450, 80, 999, 1500, 60]
# tuple() and set() both fully consume a generator into a new container
above_100_tuple = tuple(e for e in expenses if e > 100)
unique_first_digits = set(str(e)[0] for e in expenses)
print("Example 4 — Converting generator expressions to containers:")
print(f"  Expenses above ₹100 (tuple): {above_100_tuple}")
print(f"  Unique leading digits (set): {unique_first_digits}")
# Output:
#   Expenses above ₹100 (tuple): (200, 450, 999, 1500)
#   Unique leading digits (set): a set containing '2','4','8','9','1','6' (set order is not guaranteed)

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════════════
# Given the list `temperatures = [28, 33, 41, 19, 36, 45]` (Celsius readings
# from sensors across Delhi), use a generator expression with sum() to find
# the total of all readings above 30°C, without building an intermediate list.
#
# Expected output: Total above 30C: 155

temperatures = [28, 33, 41, 19, 36, 45]

# YOUR CODE HERE


# SOLUTION:
# total_above_30 = sum(t for t in temperatures if t > 30)
# print(f"Total above 30C: {total_above_30}")


# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
# - Generator expressions use () instead of [] — same filtering/mapping
#   syntax as comprehensions, but values are produced lazily.
# - They can only be consumed ONCE; create a new one to reuse.
# - When passed as the sole argument to a function, the extra parentheses
#   can be dropped: sum(x for x in y).
# - Use tuple()/set()/list() to fully materialize a generator expression
#   into a concrete container when you need to reuse the values.
#
# Next up (File 4 of 4): The itertools module — chain, islice, product,
# and cycle for combining and slicing iterators efficiently.

if __name__ == "__main__":
    print("Day 13, File 3 — Generator Expressions: all demonstrations ran successfully.")
