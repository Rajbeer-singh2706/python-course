"""
Day 07 — Practice Problems (File 3 of 3)
Topic: re Module Basics + Mixed Challenges

Cumulative scope: Days 01-07

Difficulty legend:
    Warm-up
    Core
    Challenge

Section Index:
    Section D — re Module Basics       (Problems 13-16)
    Section E — Mixed Challenges       (Problems 17-20)

How to run:
    python day07_practise_problems_03_regex_mixed.py
"""

import re

# ════════════════════════════════════════════════════════════
# SECTION D: re Module Basics
# ════════════════════════════════════════════════════════════
print("=" * 50)
print("SECTION D: re Module Basics")
print("=" * 50)

# Problem 13  Warm-up
# ----------------------------------------------------------------
# Use re.search() to find the first sequence of digits in the
# string below and print it.
#
# Given:
message = "Your OTP for login is 4821, valid for 5 minutes"
#
# Expected output:
# 4821

# YOUR CODE HERE


# SOLUTION:
# match = re.search(r"\d+", message)
# print(match.group())

print("-" * 50)

# Problem 14  Warm-up
# ----------------------------------------------------------------
# Use re.match() to check whether the given order code starts
# with the letters "DEL" (case-sensitive). Print True or False.
#
# Given:
order_code = "DEL20260093"
#
# Expected output:
# True

# YOUR CODE HERE


# SOLUTION:
# result = bool(re.match(r"DEL", order_code))
# print(result)

print("-" * 50)

# Problem 15  Core
# ----------------------------------------------------------------
# Use re.findall() to extract all 10-digit phone numbers from
# the text below.
#
# Given:
contact_sheet = "Priya: 9876543210, Arjun: 8123456789, Office: 02226578900"
#
# Expected output:
# ['9876543210', '8123456789']
#
# Hint: 10-digit numbers should not match longer sequences —
# use \b (word boundary) around the pattern.

# YOUR CODE HERE


# SOLUTION:
# numbers = re.findall(r"\b\d{10}\b", contact_sheet)
# print(numbers)

print("-" * 50)

# Problem 16  Challenge
# ----------------------------------------------------------------
# Validate the list of usernames below. A valid username contains
# only lowercase letters, digits, and underscores, and must be at
# least 4 characters long. Print each username with True/False.
#
# Given:
usernames = ["priya_99", "AR", "sanjay_verma_1", "riya!k"]
#
# Expected output:
# priya_99: True
# AR: False
# sanjay_verma_1: True
# riya!k: False

# YOUR CODE HERE


# SOLUTION:
# for uname in usernames:
#     is_valid = bool(re.match(r"^[a-z0-9_]{4,}$", uname))
#     print(f"{uname}: {is_valid}")

print("=" * 50)

# ════════════════════════════════════════════════════════════
# SECTION E: Mixed Challenges
# ════════════════════════════════════════════════════════════
print("SECTION E: Mixed Challenges")
print("=" * 50)

# Problem 17  Challenge
# ----------------------------------------------------------------
# Combine loops (Day 04), string formatting (Day 07), and
# dictionaries (Day 06): given a dictionary of product prices,
# print each line as an aligned, formatted price list.
#
# Given:
product_prices = {
    "Notebook": 45.5,
    "Ballpoint Pen": 10.0,
    "Backpack": 899.99,
}
#
# Expected output:
# Notebook             Rs.    45.50
# Ballpoint Pen        Rs.    10.00
# Backpack             Rs.   899.99

# YOUR CODE HERE


# SOLUTION:
# for product, price in product_prices.items():
#     print(f"{product:<20}Rs. {price:>8.2f}")

print("-" * 50)

# Problem 18  Challenge
# ----------------------------------------------------------------
# Given a raw log line, use split() to isolate the message part,
# then use re.findall() to extract every email address in it.
#
# Given:
log_line = "2026-06-30 | INFO | Notify priya@example.com, arjun@company.in"
#
# Expected output:
# ['priya@example.com', 'arjun@company.in']

# YOUR CODE HERE


# SOLUTION:
# message_part = log_line.split("| INFO |")[1]
# emails = re.findall(r"[\w.]+@[\w.]+", message_part)
# print(emails)

print("-" * 50)

# Problem 19  Challenge
# ----------------------------------------------------------------
# Write a function (Day 05) called `summarize_order` that takes a
# customer name and a list of item prices, and returns a formatted
# string using an f-string: "<name>'s order total: Rs. <total,
# 2 decimals>". Use it on the data below.
#
# Given:
customer = "Riya Deshmukh"
item_prices = [349.0, 129.5, 899.0]
#
# Expected output:
# Riya Deshmukh's order total: Rs. 1377.50

# YOUR CODE HERE


# SOLUTION:
# def summarize_order(name, prices):
#     total = sum(prices)
#     return f"{name}'s order total: Rs. {total:.2f}"
#
# print(summarize_order(customer, item_prices))

print("-" * 50)

# Problem 20  Challenge
# ----------------------------------------------------------------
# Full pipeline: given raw feedback text, (1) strip it, (2) use
# re.findall() to pull out every 10-digit phone number, (3) join
# them into a single comma-separated string, and (4) print a
# formatted summary line.
#
# Given:
raw_feedback = (
    "   Customer Sanjay Verma can be reached at 9876543210 "
    "or alternate number 8123456789 for follow-up.   "
)
#
# Expected output:
# Contact numbers found: 9876543210, 8123456789

# YOUR CODE HERE


# SOLUTION:
# cleaned_feedback = raw_feedback.strip()
# phone_numbers = re.findall(r"\b\d{10}\b", cleaned_feedback)
# print(f"Contact numbers found: {', '.join(phone_numbers)}")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file:
#   Section D — re Module Basics     (4 problems)
#   Section E — Mixed Challenges     (4 problems)
#
# Difficulty breakdown: 2 Warm-up, 2 Core, 4 Challenge
#
# Day 07 problem set complete — 20 problems across 3 files.
# Next session (Day 08) covers File I/O: reading, writing, CSV,
# and JSON.
