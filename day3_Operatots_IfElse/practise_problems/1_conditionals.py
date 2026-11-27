"""
Day 3 — Practice Problems (Part 1 of 2)
Topic: Control Flow — if/elif/else, comparison & logical operators, nesting

Cumulative scope: Day 2 (variables, data types, casting) + Day 3 concepts
covered in day03_01_conditionals_operators.py

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines 2+ ideas, requires some thought
    🔴 Challenge — multi-step reasoning, edge cases

Section index:
    A — Prior Days Review (Day 2: variables, types, casting)
    B — Comparison Operators
    C — if / elif / else
    D — Logical Operators & Nesting

How to run:
    python day03_practise_problems_01_conditionals.py
"""

# ════════════════════════════════════════════════════════
# SECTION A — Prior Days Review (Day 2)
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION A: Prior Days Review")
print("=" * 50)

# --- Problem A1 ---
# 🟢 Warm-up
# Priya's age is stored as a string "25". Convert it to an integer
# and print it added to 5 (i.e. her age 5 years from now).
# Expected output: 30

age_str = "25"

# YOUR CODE HERE


# SOLUTION:
# age_int = int(age_str)
# print(age_int + 5)

print("-" * 50)

# --- Problem A2 ---
# 🟢 Warm-up
# Given a float price, print its type using type().
# Expected output: <class 'float'>

price = 499.0

# YOUR CODE HERE


# SOLUTION:
# print(type(price))

print("-" * 50)

# --- Problem A3 ---
# 🟡 Core
# Arjun's name and city are stored separately. Combine them into a
# single f-string sentence: "Arjun lives in Pune."

name = "Arjun"
city = "Pune"

# YOUR CODE HERE


# SOLUTION:
# print(f"{name} lives in {city}.")


# ════════════════════════════════════════════════════════
# SECTION B — Comparison Operators
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION B: Comparison Operators")
print("=" * 50)

# --- Problem B1 ---
# 🟢 Warm-up
# Compare two bus ticket prices and print True if they are equal.
# Expected output: False

ticket_price_1 = 120
ticket_price_2 = 150

# YOUR CODE HERE


# SOLUTION:
# print(ticket_price_1 == ticket_price_2)

print("-" * 50)

# --- Problem B2 ---
# 🟢 Warm-up
# Print True if Riya's savings is greater than or equal to a laptop's price.
# Expected output: True

savings = 45000
laptop_price = 45000

# YOUR CODE HERE


# SOLUTION:
# print(savings >= laptop_price)

print("-" * 50)

# --- Problem B3 ---
# 🟡 Core
# Two pin codes are stored as strings. Print True if they are NOT equal.
# Expected output: True

pincode_a = "400001"
pincode_b = "110001"

# YOUR CODE HERE


# SOLUTION:
# print(pincode_a != pincode_b)

print("-" * 50)

# --- Problem B4 ---
# 🟡 Core
# Compare two product ratings (floats) and print which one is higher
# using an f-string: "Rating A is higher" or "Rating B is higher" or "Equal".
# Use if/elif/else for this (not just a bare comparison print).
# Expected output: Rating B is higher

rating_a = 4.2
rating_b = 4.6

# YOUR CODE HERE


# SOLUTION:
# if rating_a > rating_b:
#     print("Rating A is higher")
# elif rating_b > rating_a:
#     print("Rating B is higher")
# else:
#     print("Equal")


# ════════════════════════════════════════════════════════
# SECTION C — if / elif / else
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION C: if / elif / else")
print("=" * 50)

# --- Problem C1 ---
# 🟢 Warm-up
# If temperature is above 35, print "Heatwave alert". Otherwise print nothing logic needed,
# just print "Normal weather".
# Expected output: Heatwave alert

temperature = 38

# YOUR CODE HERE


# SOLUTION:
# if temperature > 35:
#     print("Heatwave alert")
# else:
#     print("Normal weather")

print("-" * 50)

# --- Problem C2 ---
# 🟡 Core
# Sanjay's monthly income decides his tax slab:
#   income <= 25000        -> "No tax"
#   25000 < income <= 50000 -> "5% tax"
#   income > 50000          -> "20% tax"
# Use if/elif/else.
# Expected output: 5% tax

income = 40000

# YOUR CODE HERE


# SOLUTION:
# if income <= 25000:
#     print("No tax")
# elif income <= 50000:
#     print("5% tax")
# else:
#     print("20% tax")

print("-" * 50)

# --- Problem C3 ---
# 🟡 Core
# A student's attendance percentage decides eligibility:
#   >= 75   -> "Eligible for exam"
#   60-74   -> "Condonation required"
#   < 60    -> "Not eligible"
# Expected output: Condonation required

attendance_percent = 68

# YOUR CODE HERE


# SOLUTION:
# if attendance_percent >= 75:
#     print("Eligible for exam")
# elif attendance_percent >= 60:
#     print("Condonation required")
# else:
#     print("Not eligible")

print("-" * 50)

# --- Problem C4 ---
# 🔴 Challenge
# Build an auto-rickshaw fare calculator:
#   First 2 km: flat Rs.30
#   Each additional km: Rs.12/km (round UP to nearest whole km if fractional)
# Given distance_km = 7.5, calculate and print total fare using if/elif/else
# structure (handle the "distance <= 2" case separately).
# Expected output: Total fare: Rs.96
# (Hint: extra_km = distance_km - 2 = 5.5 -> round up to 6 -> 6*12 = 72 + 30 = 102)
# NOTE: recompute carefully — use math.ceil for rounding up.

import math

distance_km = 7.5

# YOUR CODE HERE


# SOLUTION:
# if distance_km <= 2:
#     fare = 30
# else:
#     extra_km = math.ceil(distance_km - 2)
#     fare = 30 + (extra_km * 12)
# print(f"Total fare: Rs.{fare}")


# ════════════════════════════════════════════════════════
# SECTION D — Logical Operators & Nesting
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION D: Logical Operators & Nesting")
print("=" * 50)

# --- Problem D1 ---
# 🟢 Warm-up
# Print True only if both has_voter_id and age >= 18 are true (use 'and').
# Expected output: True

has_voter_id = True
age = 19

# YOUR CODE HERE


# SOLUTION:
# print(has_voter_id and age >= 18)

print("-" * 50)

# --- Problem D2 ---
# 🟡 Core
# A movie ticket counter gives a discount if it's a weekday OR the
# customer is a student. Print "Discount applied" or "Full price".
# Expected output: Discount applied

is_weekday = False
is_student = True

# YOUR CODE HERE


# SOLUTION:
# if is_weekday or is_student:
#     print("Discount applied")
# else:
#     print("Full price")

print("-" * 50)

# --- Problem D3 ---
# 🟡 Core
# Use 'not' to print "Shop is open" if is_closed is False.
# Expected output: Shop is open

is_closed = False

# YOUR CODE HERE


# SOLUTION:
# if not is_closed:
#     print("Shop is open")

print("-" * 50)

# --- Problem D4 ---
# 🔴 Challenge
# Nested condition: A bank loan is approved only if:
#   - credit_score >= 700 AND
#     - (monthly_income >= 50000  OR  has_collateral is True)
# Print "Loan approved" or "Loan rejected" using nested if statements
# (an outer if for credit_score, an inner if for the income/collateral check).
# Expected output: Loan approved

credit_score = 740
monthly_income = 35000
has_collateral = True

# YOUR CODE HERE


# SOLUTION:
# if credit_score >= 700:
#     if monthly_income >= 50000 or has_collateral:
#         print("Loan approved")
#     else:
#         print("Loan rejected")
# else:
#     print("Loan rejected")

print("-" * 50)

# --- Problem D5 ---
# 🔴 Challenge
# Riya wants to book a Mumbai-Delhi flight. The booking is allowed only if:
#   - she has a valid ID AND
#   - (age >= 18 OR traveling_with_guardian is True) AND
#   - NOT is_blacklisted
# Print "Booking allowed" or "Booking denied".
# Expected output: Booking denied

has_valid_id = True
age = 16
traveling_with_guardian = False
is_blacklisted = False

# YOUR CODE HERE


# SOLUTION:
# if has_valid_id and (age >= 18 or traveling_with_guardian) and not is_blacklisted:
#     print("Booking allowed")
# else:
#     print("Booking denied")


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   A — Prior Days Review (3 problems)
#   B — Comparison Operators (4 problems)
#   C — if / elif / else (4 problems)
#   D — Logical Operators & Nesting (5 problems)
#
# Difficulty breakdown: 5 Warm-up | 6 Core | 5 Challenge (16 total)
#
# Next file: day03_practise_problems_02_match_mixed.py
#   (match statement problems + Mixed Challenges combining Day 2 + Day 3)
