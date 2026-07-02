"""
Day 5 — Functions & Scope — Practice Problems
File 2 of 3: *args and **kwargs

Difficulty legend:
    🟢 Warm-up   — straightforward, single concept
    🟡 Core      — combines a couple of ideas
    🔴 Challenge — requires more careful thinking

Section index (this file):
    Section C — *args and **kwargs

How to run:
    python day05_practise_problems_02_args_kwargs.py
"""

# ════════════════════════════════════════════════════════
# SECTION C — *args and **kwargs
# ════════════════════════════════════════════════════════

# --------------------------------------------------------
# Problem C1  🟢 Warm-up
# --------------------------------------------------------
# Write a function `add_all(*numbers)` that returns the sum of any
# number of arguments passed to it. Test it with (2, 4, 6) and with
# (10, 20, 30, 40).

# YOUR CODE HERE


# SOLUTION:
# def add_all(*numbers):
#     return sum(numbers)
#
# print(add_all(2, 4, 6))          # Output: 12
# print(add_all(10, 20, 30, 40))   # Output: 100

print("-" * 50)

# --------------------------------------------------------
# Problem C2  🟢 Warm-up
# --------------------------------------------------------
# Write a function `list_subjects(*subjects)` that prints each
# subject on its own line, numbered starting from 1.
# Test with "Maths", "Science", "Hindi".

# YOUR CODE HERE


# SOLUTION:
# def list_subjects(*subjects):
#     for index, subject in enumerate(subjects, start=1):
#         print(f"{index}. {subject}")
#
# list_subjects("Maths", "Science", "Hindi")

print("-" * 50)

# --------------------------------------------------------
# Problem C3  🟡 Core
# --------------------------------------------------------
# Write a function `print_profile(**info)` that prints each key-value
# pair of student info as "key: value". Test it with:
# name="Priya", city="Mumbai", course="Python Bootcamp"

# YOUR CODE HERE


# SOLUTION:
# def print_profile(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")
#
# print_profile(name="Priya", city="Mumbai", course="Python Bootcamp")

print("-" * 50)

# --------------------------------------------------------
# Problem C4  🟡 Core
# --------------------------------------------------------
# Write a function `average_marks(*marks)` that returns the average
# of any number of marks passed in. If no marks are given, return 0
# (to avoid a divide-by-zero error).
# Test it with (80, 90, 70) and with no arguments at all.

# YOUR CODE HERE


# SOLUTION:
# def average_marks(*marks):
#     if not marks:
#         return 0
#     return sum(marks) / len(marks)
#
# print(average_marks(80, 90, 70))  # Output: 80.0
# print(average_marks())            # Output: 0

print("-" * 50)

# --------------------------------------------------------
# Problem C5  🔴 Challenge
# --------------------------------------------------------
# Write a function `order_summary(customer_name, *items, **charges)`
# that:
#   - Prints the customer name and the list of items ordered
#   - Sums up all the values in `charges` (e.g. delivery_fee=30,
#     packaging_fee=10) and prints the total extra charges
#   - Returns the total extra charges
#
# Test it with:
#   order_summary("Arjun", "Rice", "Dal", "Oil",
#                  delivery_fee=30, packaging_fee=10, gst=15)

# YOUR CODE HERE


# SOLUTION:
# def order_summary(customer_name, *items, **charges):
#     print(f"Customer: {customer_name}")
#     print(f"Items: {', '.join(items)}")
#     total_charges = sum(charges.values())
#     print(f"Total extra charges: Rs. {total_charges}")
#     return total_charges
#
# order_summary("Arjun", "Rice", "Dal", "Oil",
#                delivery_fee=30, packaging_fee=10, gst=15)
# # Output:
# # Customer: Arjun
# # Items: Rice, Dal, Oil
# # Total extra charges: Rs. 55

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   C. *args and **kwargs — 5 problems
#
# Difficulty breakdown: 2x 🟢 Warm-up, 2x 🟡 Core, 1x 🔴 Challenge
#
# Continue with File 3: day05_practise_problems_03_scope_mixed.py
