"""
Day 07 — Practice Problems (File 2 of 3)
Topic: split(), join(), strip(), replace() & Common Methods

Cumulative scope: Days 01-07

Difficulty legend:
    Warm-up
    Core
    Challenge

Section Index:
    Section C — String Methods (Problems 8-12)

How to run:
    python day07_practise_problems_02_string_methods.py
"""

# ════════════════════════════════════════════════════════════
# SECTION C: String Methods
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("SECTION C: String Methods")
print("=" * 50)

# Problem 8  Warm-up
# ----------------------------------------------------------------
# Split the sentence below into a list of individual words.
#
# Given:
sentence = "Priya loves learning Python every single day"
#
# Expected output:
# ['Priya', 'loves', 'learning', 'Python', 'every', 'single', 'day']

# YOUR CODE HERE


# SOLUTION:
# words = sentence.split()
# print(words)

print("-" * 50)

# Problem 9  Warm-up
# ----------------------------------------------------------------
# Clean the messy string below by stripping leading/trailing
# whitespace, then print it wrapped in square brackets.
#
# Given:
messy_name = "   Sanjay Verma   "  # simulating input() from a form
#
# Expected output:
# [Sanjay Verma]

# YOUR CODE HERE


# SOLUTION:
# print(f"[{messy_name.strip()}]")

print("-" * 50)

# Problem 10  Core
# ----------------------------------------------------------------
# Join the list of city names below into a single comma-separated
# string (no spaces after commas).
#
# Given:
cities = ["Mumbai", "Delhi", "Bengaluru", "Pune", "Hyderabad"]
#
# Expected output:
# Mumbai,Delhi,Bengaluru,Pune,Hyderabad

# YOUR CODE HERE


# SOLUTION:
# print(",".join(cities))

print("-" * 50)

# Problem 11  Core
# ----------------------------------------------------------------
# Replace every occurrence of "Rs." in the receipt line below
# with "INR", then print the updated line.
#
# Given:
receipt_line = "Item Total: Rs. 1200 | Delivery: Rs. 40 | Tax: Rs. 216"
#
# Expected output:
# Item Total: INR 1200 | Delivery: INR 40 | Tax: INR 216

# YOUR CODE HERE


# SOLUTION:
# print(receipt_line.replace("Rs.", "INR"))

print("-" * 50)

# Problem 12  Challenge
# ----------------------------------------------------------------
# Given a raw pipe-delimited student record, split it into fields,
# strip whitespace from each field, then join the cleaned fields
# back together with " | " as the separator.
#
# Given:
raw_record = "  Riya Deshmukh | 24 |  Pune  |Data Science  "
#
# Expected output:
# Riya Deshmukh | 24 | Pune | Data Science

# YOUR CODE HERE


# SOLUTION:
# fields = raw_record.split("|")
# cleaned_fields = [field.strip() for field in fields]
# print(" | ".join(cleaned_fields))


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file:
#   Section C — String Methods     (5 problems)
#
# Difficulty breakdown: 2 Warm-up, 2 Core, 1 Challenge
#
# Next file: day07_practise_problems_03_regex_mixed.py covers
# the `re` module and Mixed Challenges combining everything from
# Day 07 with concepts from earlier days.
