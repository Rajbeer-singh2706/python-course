"""
Day 5 — Functions & Scope — Practice Problems
File 1 of 3: Prior Days Review + Function Basics

Cumulative scope: Days 2-5 (variables, control flow, loops, functions)

Difficulty legend:
    🟢 Warm-up   — straightforward, single concept
    🟡 Core      — combines a couple of ideas
    🔴 Challenge — requires more careful thinking

Section index (this file):
    Section A — Prior Days Review (Days 2-4)
    Section B — Function Basics (def, params, return, defaults)

How to run:
    python day05_practise_problems_01_functions_basics.py
"""

# ════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════

# --------------------------------------------------------
# Problem A1  🟢 Warm-up
# --------------------------------------------------------
# Priya has a list of temperatures recorded in Mumbai over a week:
# [30, 32, 29, 31, 33, 28, 30]
# Using a for loop, print each temperature followed by " C".

temperatures = [30, 32, 29, 31, 33, 28, 30]

# YOUR CODE HERE


# SOLUTION:
# for temp in temperatures:
#     print(f"{temp} C")

print("-" * 50)

# --------------------------------------------------------
# Problem A2  🟢 Warm-up
# --------------------------------------------------------
# Arjun is checking if a number is even or odd using an if/else
# statement. Given the number below, print "Even" or "Odd".

number_to_check = 17

# YOUR CODE HERE


# SOLUTION:
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

print("-" * 50)

# --------------------------------------------------------
# Problem A3  🟡 Core
# --------------------------------------------------------
# Riya Deshmukh wants to find the sum of all multiples of 3 between
# 1 and 50 (inclusive) using a while loop. Print the final sum.

# YOUR CODE HERE


# SOLUTION:
# total = 0
# n = 1
# while n <= 50:
#     if n % 3 == 0:
#         total += n
#     n += 1
# print(total)

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION B — Function Basics
# ════════════════════════════════════════════════════════

# --------------------------------------------------------
# Problem B1  🟢 Warm-up
# --------------------------------------------------------
# Write a function `square(number)` that returns the square of a
# number. Call it with 7 and print the result.

# YOUR CODE HERE


# SOLUTION:
# def square(number):
#     return number ** 2
#
# print(square(7))  # Output: 49

print("-" * 50)

# --------------------------------------------------------
# Problem B2  🟢 Warm-up
# --------------------------------------------------------
# Write a function `greet_customer(name)` that prints:
# "Welcome to Mumbai Mart, <name>!"
# Call it for "Sanjay Verma".

# YOUR CODE HERE


# SOLUTION:
# def greet_customer(name):
#     print(f"Welcome to Mumbai Mart, {name}!")
#
# greet_customer("Sanjay Verma")

print("-" * 50)

# --------------------------------------------------------
# Problem B3  🟡 Core
# --------------------------------------------------------
# Write a function `calculate_area(length, width=5)` that returns the
# area of a rectangle. `width` should default to 5 if not provided.
# Test it once with only `length=10`, and once with `length=10, width=8`.

# YOUR CODE HERE


# SOLUTION:
# def calculate_area(length, width=5):
#     return length * width
#
# print(calculate_area(10))       # Output: 50
# print(calculate_area(10, 8))    # Output: 80

print("-" * 50)

# --------------------------------------------------------
# Problem B4  🟡 Core
# --------------------------------------------------------
# Write a function `is_eligible_to_vote(age)` that returns True if
# age is 18 or above, otherwise False. Test it with ages 16 and 21,
# printing the results.

# YOUR CODE HERE


# SOLUTION:
# def is_eligible_to_vote(age):
#     return age >= 18
#
# print(is_eligible_to_vote(16))  # Output: False
# print(is_eligible_to_vote(21))  # Output: True

print("-" * 50)

# --------------------------------------------------------
# Problem B5  🔴 Challenge
# --------------------------------------------------------
# Write a function `train_fare(distance_km, travel_class="Sleeper")`
# that calculates and returns a fare using these rules:
#   - Sleeper class: Rs. 0.50 per km
#   - AC 3 Tier: Rs. 1.20 per km
#   - AC 2 Tier: Rs. 1.80 per km
# If an unknown travel_class is given, return None.
# Test it for a 500 km journey in each of the three classes, and once
# with an invalid class like "First Class".

# YOUR CODE HERE


# SOLUTION:
# def train_fare(distance_km, travel_class="Sleeper"):
#     rates = {
#         "Sleeper": 0.50,
#         "AC 3 Tier": 1.20,
#         "AC 2 Tier": 1.80,
#     }
#     if travel_class not in rates:
#         return None
#     return distance_km * rates[travel_class]
#
# print(train_fare(500))                     # Output: 250.0
# print(train_fare(500, "AC 3 Tier"))         # Output: 600.0
# print(train_fare(500, "AC 2 Tier"))         # Output: 900.0
# print(train_fare(500, "First Class"))       # Output: None

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   A. Prior Days Review    — 3 problems (loops, conditionals)
#   B. Function Basics      — 5 problems (def, params, return, defaults)
#
# Difficulty breakdown: 4x 🟢 Warm-up, 3x 🟡 Core, 1x 🔴 Challenge
#
# Continue with File 2: day05_practise_problems_02_args_kwargs.py
