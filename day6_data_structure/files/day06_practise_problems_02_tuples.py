"""
Day 6 — Data Structures — Practice Problems
File 2 of 4: Section C (Tuples)

Cumulative scope: Days 1-6

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines two or more ideas
    🔴 Challenge — requires extra thought or edge-case handling

Section index (this file):
    C. Tuples                   (3 problems)

How to run:
    python3 day06_practise_problems_02_tuples.py
"""


# ════════════════════════════════════════════════════════════
# SECTION C — Tuples
# ════════════════════════════════════════════════════════════

# --- Problem C1 -----------------------------------------------
# 🟢 Warm-up
# Given the tuple of exam scores below, print the second score
# using indexing.
# Expected output: 78

exam_scores = (92, 78, 65, 88)

# YOUR CODE HERE


# SOLUTION:
# print(exam_scores[1])

print("-" * 50)


# --- Problem C2 -----------------------------------------------
# 🟡 Core
# Given the tuple below representing a movie ticket booking
# (movie_name, theatre, show_time, price_in_rupees), unpack it
# into four variables and print a single formatted sentence.
# Expected output:
#   Booked '3 Idiots' at PVR Phoenix for the 7:00 PM show at Rs.250.

ticket_booking = ("3 Idiots", "PVR Phoenix", "7:00 PM", 250)

# YOUR CODE HERE


# SOLUTION:
# movie_name, theatre, show_time, price_in_rupees = ticket_booking
# print(f"Booked '{movie_name}' at {theatre} for the {show_time} show at Rs.{price_in_rupees}.")

print("-" * 50)


# --- Problem C3 -----------------------------------------------
# 🔴 Challenge
# Given the tuple of five monthly expenses below, use star-unpacking
# to capture the FIRST value, the LAST value, and all the "middle"
# values as a list. Then print all three.
# Expected output:
#   First: 1200
#   Middle: [3400, 900, 1500]
#   Last: 600

monthly_expenses = (1200, 3400, 900, 1500, 600)

# YOUR CODE HERE


# SOLUTION:
# first, *middle, last = monthly_expenses
# print("First:", first)
# print("Middle:", middle)
# print("Last:", last)

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: C (Tuples)
# Difficulty breakdown: 1x Warm-up, 1x Core, 1x Challenge
# Total problems in this file: 3
#
# Continue with: day06_practise_problems_03_dictionaries.py
