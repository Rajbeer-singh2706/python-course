"""
Day 02 — Practice Problems (Part 2: Input/Output, Casting & Mixed Challenges)
================================================================================

Day 02 cumulative scope: variables, int/float/str/bool, type(),
input()/print(), type casting.

Difficulty legend: 🟢 Warm-up   🟡 Core   🔴 Challenge

Section index:
    C — input() and print() formatting
    D — Type Casting
    E — Mixed Challenges (combines C + D + Day 1 + Section B)

How to run:
    $ python day02_practise_problems_02_io_and_mixed.py
"""

# ════════════════════════════════════════════════════════════════
# SECTION C — input() and print() Formatting
# ════════════════════════════════════════════════════════════════
# NOTE: All input() calls are SIMULATED with pre-assigned variables.

# --- Problem C1 ---
# 🟢 Warm-up
# Simulate user_name = input("Enter name: ") with the value "Priya".
# Print: "Welcome, Priya!"

# YOUR CODE HERE


# SOLUTION:
# user_name = "Priya"  # simulating input("Enter name: ")
# print(f"Welcome, {user_name}!")

print("-" * 50)

# --- Problem C2 ---
# 🟢 Warm-up
# Print "Mumbai", "Delhi", and "Pune" on ONE line separated by " - ".
# Expected output: Mumbai - Delhi - Pune

# YOUR CODE HERE


# SOLUTION:
# print("Mumbai", "Delhi", "Pune", sep=" - ")

print("-" * 50)

# --- Problem C3 ---
# 🟡 Core
# Simulate raw_age = input("Enter age: ") with "21" (a string!).
# Print its type, then print "Age (text): 21" using an f-string.
# Expected output:
#   <class 'str'>
#   Age (text): 21

# YOUR CODE HERE


# SOLUTION:
# raw_age = "21"  # simulating input("Enter age: ")
# print(type(raw_age))
# print(f"Age (text): {raw_age}")

print("-" * 50)

# --- Problem C4 ---
# 🟡 Core
# Use print() with end="" to print "Processing" then "...Complete"
# on the SAME line in two separate print() calls.
# Expected output: Processing...Complete

# YOUR CODE HERE


# SOLUTION:
# print("Processing", end="")
# print("...Complete")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION D — Type Casting
# ════════════════════════════════════════════════════════════════

# --- Problem D1 ---
# 🟢 Warm-up
# Cast the string "45" to an int and add 5 to it. Print the result.
# Expected output: 50

# YOUR CODE HERE


# SOLUTION:
# value = int("45")
# print(value + 5)

print("-" * 50)

# --- Problem D2 ---
# 🟡 Core
# Simulate raw_price = input("Price: ") with "199.99". Cast it to
# float, then print double the price using an f-string.
# Expected output: Double price: Rs. 399.98

# YOUR CODE HERE


# SOLUTION:
# raw_price = "199.99"  # simulating input("Price: ")
# price = float(raw_price)
# print(f"Double price: Rs. {price * 2}")

print("-" * 50)

# --- Problem D3 ---
# 🔴 Challenge
# Simulate two inputs: raw_a = "12", raw_b = "8" (both strings
# representing integers). Cast both to int, then print their sum,
# difference, and product on three separate lines.
# Expected output:
#   20
#   4
#   96

# YOUR CODE HERE


# SOLUTION:
# raw_a = "12"
# raw_b = "8"
# a = int(raw_a)
# b = int(raw_b)
# print(a + b)
# print(a - b)
# print(a * b)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges
# ════════════════════════════════════════════════════════════════

# --- Problem E1 ---
# 🔴 Challenge
# Simulate a chai-stall order: raw_cups = "4" (str), price_per_cup
# = 15.0 (float, already correct type). Cast raw_cups to int,
# calculate total cost, then print:
#   "<name> ordered <cups> cups for Rs. <total>"
# using the name "Sanjay Verma".
# Expected output:
#   Sanjay Verma ordered 4 cups for Rs. 60.0

# YOUR CODE HERE


# SOLUTION:
# name = "Sanjay Verma"
# raw_cups = "4"
# price_per_cup = 15.0
# cups = int(raw_cups)
# total = cups * price_per_cup
# print(f"{name} ordered {cups} cups for Rs. {total}")

print("-" * 50)

# --- Problem E2 ---
# 🔴 Challenge
# Create variables for a Delhi metro trip:
#   passenger (str) = "Riya Deshmukh"
#   raw_distance = "15.5" (str, simulating input)
#   rate_per_km (float) = 2.0
# Cast raw_distance to float, calculate fare = distance * rate,
# and print using type() to confirm raw_distance was originally
# a string, followed by the final fare message.
# Expected output:
#   <class 'str'>
#   Riya Deshmukh's fare: Rs. 31.0

# YOUR CODE HERE


# SOLUTION:
# passenger = "Riya Deshmukh"
# raw_distance = "15.5"
# rate_per_km = 2.0
# print(type(raw_distance))
# distance = float(raw_distance)
# fare = distance * rate_per_km
# print(f"{passenger}'s fare: Rs. {fare}")

print("-" * 50)

# --- Problem E3 ---
# 🔴 Challenge
# Combine everything: create a bool `is_student` = True, an int
# `base_fare` = 40, and apply a 50% discount if is_student is True
# (just use an arithmetic calculation, no if-statements yet —
# those come on Day 3). Print the final fare as a float using an
# f-string: "Final fare: Rs. <fare>"
# Expected output: Final fare: Rs. 20.0
# (Hint: discount_multiplier = 0.5 if is_student else 1.0 is a
# preview of Day 3 — for now just hardcode the multiplier as 0.5)

# YOUR CODE HERE


# SOLUTION:
# is_student = True
# base_fare = 40
# discount_multiplier = 0.5
# final_fare = base_fare * discount_multiplier
# print(f"Final fare: Rs. {final_fare}")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SUMMARY (Part 2 of 2)
# ════════════════════════════════════════════════════════════════
# Sections in this file: C (Input/Output), D (Type Casting),
# E (Mixed Challenges)
# Difficulty breakdown so far (this file): 2x Warm-up, 4x Core, 3x Challenge
# Combined with Part 1: 6x Warm-up, 6x Core, 4x Challenge = 16 problems total
#
# Next problem set: Day 3 — Control Flow (if/elif/else, comparison
# and logical operators, nested conditions, match statement).

if __name__ == "__main__":
    pass
