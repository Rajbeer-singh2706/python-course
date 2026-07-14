"""
Day 23 — Web Requests & APIs — Practice Problems (1 of 3)
========================================================================
Day 23 Topic     : Web Requests & APIs
Cumulative Scope : Days 1–23 (functions, dicts, files, OOP, pandas, requests)
Difficulty Legend : 🟢 Warm-up   🟡 Core   🔴 Challenge

SECTION INDEX (this file)
    Section A — Prior Days Review                     (3 problems)
    Section B — requests: GET, POST, Query Parameters  (5 problems)

Other files in this set:
    day23_practise_problems_02_json_auth.py   → Sections C, D
    day23_practise_problems_03_httpx_mixed.py → Section E

HOW TO RUN
    python day23_practise_problems_01_requests_get_post.py
"""

import requests
from day23_00_mock_server import start_server

BASE_URL = start_server()

print("=" * 60)
print("DAY 23 PRACTICE — FILE 1: SECTIONS A & B")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION A — PRIOR DAYS REVIEW
# ════════════════════════════════════════════════════════════

# ── Problem A1 ──
# 🟢 Warm-up
# Write a function `average(numbers)` that returns the mean of a
# list of numbers (Day 5/6 review). Test it on [180, 220, 350, 280, 40].
print("\n── Problem A1 ──")

# YOUR CODE HERE
def average(numbers):
    return sum(numbers) / len(numbers)


print(average([180, 220, 350, 280, 40]))
# Output: 214.0

# SOLUTION:
# def average(numbers):
#     return sum(numbers) / len(numbers)
# print(average([180, 220, 350, 280, 40]))


print("-" * 50)

# ── Problem A2 ──
# 🟢 Warm-up
# Given a dict {"name": "Priya Sharma", "amount": 180}, use a
# try/except (Day 9 review) to safely access a missing key "tax"
# and print "N/A" instead of crashing.
print("\n── Problem A2 ──")

# YOUR CODE HERE
order = {"name": "Priya Sharma", "amount": 180}
try:
    print(order["tax"])
except KeyError:
    print("N/A")
# Output: N/A

# SOLUTION:
# order = {"name": "Priya Sharma", "amount": 180}
# try:
#     print(order["tax"])
# except KeyError:
#     print("N/A")


print("-" * 50)

# ── Problem A3 ──
# 🟡 Core
# Write a class `Order` (Day 10 review) with attributes `item` and
# `amount`, and a method `summary()` returning "<item>: ₹<amount>".
# Create one instance and print its summary.
print("\n── Problem A3 ──")

# YOUR CODE HERE
class Order:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def summary(self):
        return f"{self.item}: ₹{self.amount}"


o = Order("Masala Dosa", 120)
print(o.summary())
# Output: Masala Dosa: ₹120

# SOLUTION:
# class Order:
#     def __init__(self, item, amount):
#         self.item = item
#         self.amount = amount
#     def summary(self):
#         return f"{self.item}: ₹{self.amount}"
# o = Order("Masala Dosa", 120)
# print(o.summary())


# ════════════════════════════════════════════════════════════
# SECTION B — requests: GET, POST, QUERY PARAMETERS
# ════════════════════════════════════════════════════════════

print("\n" + "=" * 20 + " SECTION B " + "=" * 20)

# ── Problem B1 ──
# 🟢 Warm-up
# Send a GET request to /orders and print how many orders came back.
print("\n── Problem B1 ──")

# YOUR CODE HERE
res = requests.get(f"{BASE_URL}/orders")
print(len(res.json()))
# Output: 5

# SOLUTION:
# res = requests.get(f"{BASE_URL}/orders")
# print(len(res.json()))


print("-" * 50)

# ── Problem B2 ──
# 🟢 Warm-up
# Send a GET request to /orders/3 and print just the "item" field.
print("\n── Problem B2 ──")

# YOUR CODE HERE
res = requests.get(f"{BASE_URL}/orders/3")
print(res.json()["item"])
# Output: Gujarati Thali

# SOLUTION:
# res = requests.get(f"{BASE_URL}/orders/3")
# print(res.json()["item"])


print("-" * 50)

# ── Problem B3 ──
# 🟡 Core
# Use `params=` to fetch only orders with status "delivered" and
# print the customer name for each one.
print("\n── Problem B3 ──")

# YOUR CODE HERE
res = requests.get(f"{BASE_URL}/orders", params={"status": "delivered"})
for order in res.json():
    print(order["customer"])
# Output:
# Priya Sharma
# Sanjay Verma
# Meera Iyer

# SOLUTION:
# res = requests.get(f"{BASE_URL}/orders", params={"status": "delivered"})
# for order in res.json():
#     print(order["customer"])


print("-" * 50)

# ── Problem B4 ──
# 🟡 Core
# POST a new order for customer "Riya Deshmukh" at "Bikanervala" in
# "Delhi" for "Aloo Tikki" costing 100. Print the new order's id and
# its status.
print("\n── Problem B4 ──")

# YOUR CODE HERE
payload = {"customer": "Riya Deshmukh", "restaurant": "Bikanervala",
           "city": "Delhi", "item": "Aloo Tikki", "amount": 100}
res = requests.post(f"{BASE_URL}/orders", json=payload)
data = res.json()
print(data["id"], data["status"])
# Output: 6 placed

# SOLUTION:
# payload = {"customer": "Riya Deshmukh", "restaurant": "Bikanervala",
#            "city": "Delhi", "item": "Aloo Tikki", "amount": 100}
# res = requests.post(f"{BASE_URL}/orders", json=payload)
# data = res.json()
# print(data["id"], data["status"])


print("-" * 50)

# ── Problem B5 ──
# 🔴 Challenge
# Fetch all orders for city "Chennai", compute their total amount,
# and print it as "Chennai total: ₹<amount>".
print("\n── Problem B5 ──")

# YOUR CODE HERE
res = requests.get(f"{BASE_URL}/orders", params={"city": "Chennai"})
total = sum(order["amount"] for order in res.json())
print(f"Chennai total: ₹{total}")
# Output: Chennai total: ₹220

# SOLUTION:
# res = requests.get(f"{BASE_URL}/orders", params={"city": "Chennai"})
# total = sum(order["amount"] for order in res.json())
# print(f"Chennai total: ₹{total}")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections covered in this file: A (review, 3 problems), B (requests
# GET/POST/params, 5 problems) — 8 problems total.
# Difficulty breakdown: 4 🟢 Warm-up, 3 🟡 Core, 1 🔴 Challenge
#
# NEXT: day23_practise_problems_02_json_auth.py — Sections C (REST +
# JSON parsing) and D (authentication headers).
