"""
Day 23 — Web Requests & APIs — Practice Problems (2 of 3)
========================================================================
Day 23 Topic     : Web Requests & APIs
Cumulative Scope : Days 1–23
Difficulty Legend : 🟢 Warm-up   🟡 Core   🔴 Challenge

SECTION INDEX (this file)
    Section C — REST Verbs & JSON Parsing        (4 problems)
    Section D — Authentication Headers            (4 problems)

Other files in this set:
    day23_practise_problems_01_requests_get_post.py → Sections A, B
    day23_practise_problems_03_httpx_mixed.py       → Section E

HOW TO RUN
    python day23_practise_problems_02_json_auth.py
"""

import requests
from day23_00_mock_server import start_server, VALID_TOKEN, VALID_API_KEY

BASE_URL = start_server()

print("=" * 60)
print("DAY 23 PRACTICE — FILE 2: SECTIONS C & D")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION C — REST VERBS & JSON PARSING
# ════════════════════════════════════════════════════════════

# ── Problem C1 ──
# 🟢 Warm-up
# PUT an update to order id 2, changing its status to "delivered".
# Print the updated status.
print("\n── Problem C1 ──")

# YOUR CODE HERE
res = requests.put(f"{BASE_URL}/orders/2", json={"status": "delivered"})
print(res.json()["status"])
# Output: delivered

# SOLUTION:
# res = requests.put(f"{BASE_URL}/orders/2", json={"status": "delivered"})
# print(res.json()["status"])


print("-" * 50)

# ── Problem C2 ──
# 🟡 Core
# DELETE order id 5, then try to GET it again. Print both the
# delete confirmation message and the follow-up status code.
print("\n── Problem C2 ──")

# YOUR CODE HERE
delete_res = requests.delete(f"{BASE_URL}/orders/5")
print(delete_res.json()["message"])
followup = requests.get(f"{BASE_URL}/orders/5")
print(followup.status_code)
# Output:
# Order 5 cancelled successfully
# 404

# SOLUTION:
# delete_res = requests.delete(f"{BASE_URL}/orders/5")
# print(delete_res.json()["message"])
# followup = requests.get(f"{BASE_URL}/orders/5")
# print(followup.status_code)


print("-" * 50)

# ── Problem C3 ──
# 🟡 Core
# Given this nested dict (simulating an API response):
#   payment = {"order": {"id": 12, "payment": {"method": "UPI", "status": "success"}}}
# print the payment method and status using key access.
print("\n── Problem C3 ──")

# YOUR CODE HERE
payment = {"order": {"id": 12, "payment": {"method": "UPI", "status": "success"}}}
print(payment["order"]["payment"]["method"])
print(payment["order"]["payment"]["status"])
# Output:
# UPI
# success

# SOLUTION:
# payment = {"order": {"id": 12, "payment": {"method": "UPI", "status": "success"}}}
# print(payment["order"]["payment"]["method"])
# print(payment["order"]["payment"]["status"])


print("-" * 50)

# ── Problem C4 ──
# 🔴 Challenge
# Fetch /orders, classify each response you would expect from
# GET/POST/PUT/DELETE into its status-code family using
# `status // 100`. Given the codes [200, 201, 404, 401, 500],
# print a dict mapping each code to its family label using:
# {2: "Success", 4: "Client Error", 5: "Server Error"}.
print("\n── Problem C4 ──")

# YOUR CODE HERE
codes = [200, 201, 404, 401, 500]
labels = {2: "Success", 4: "Client Error", 5: "Server Error"}
result = {code: labels[code // 100] for code in codes}
print(result)
# Output: {200: 'Success', 201: 'Success', 404: 'Client Error', 401: 'Client Error', 500: 'Server Error'}

# SOLUTION:
# codes = [200, 201, 404, 401, 500]
# labels = {2: "Success", 4: "Client Error", 5: "Server Error"}
# result = {code: labels[code // 100] for code in codes}
# print(result)


# ════════════════════════════════════════════════════════════
# SECTION D — AUTHENTICATION HEADERS
# ════════════════════════════════════════════════════════════

print("\n" + "=" * 20 + " SECTION D " + "=" * 20)

# ── Problem D1 ──
# 🟢 Warm-up
# Call /protected/profile with no headers at all and print the
# status code you get back.
print("\n── Problem D1 ──")

# YOUR CODE HERE
res = requests.get(f"{BASE_URL}/protected/profile")
print(res.status_code)
# Output: 401

# SOLUTION:
# res = requests.get(f"{BASE_URL}/protected/profile")
# print(res.status_code)


print("-" * 50)

# ── Problem D2 ──
# 🟢 Warm-up
# Call /protected/profile with a correct Bearer token (VALID_TOKEN)
# and print the customer's loyalty tier.
print("\n── Problem D2 ──")

# YOUR CODE HERE
headers = {"Authorization": f"Bearer {VALID_TOKEN}"}
res = requests.get(f"{BASE_URL}/protected/profile", headers=headers)
print(res.json()["tier"])
# Output: Gold

# SOLUTION:
# headers = {"Authorization": f"Bearer {VALID_TOKEN}"}
# res = requests.get(f"{BASE_URL}/protected/profile", headers=headers)
# print(res.json()["tier"])


print("-" * 50)

# ── Problem D3 ──
# 🟡 Core
# Call /protected/analytics using the X-API-Key header with
# VALID_API_KEY, and print total_orders and total_revenue on
# separate lines.
print("\n── Problem D3 ──")

# YOUR CODE HERE
res = requests.get(f"{BASE_URL}/protected/analytics", headers={"X-API-Key": VALID_API_KEY})
data = res.json()
print(data["total_orders"])
print(data["total_revenue"])
# Output (reflects order 5 being deleted earlier in Problem C2):
# 4
# 1030

# SOLUTION:
# res = requests.get(f"{BASE_URL}/protected/analytics", headers={"X-API-Key": VALID_API_KEY})
# data = res.json()
# print(data["total_orders"])
# print(data["total_revenue"])


print("-" * 50)

# ── Problem D4 ──
# 🔴 Challenge
# Write a function `try_login(token)` that returns "Access granted"
# if the token is valid for /protected/profile and "Access denied"
# otherwise. Test it with VALID_TOKEN and with "fake-token".
print("\n── Problem D4 ──")

# YOUR CODE HERE
def try_login(token):
    res = requests.get(f"{BASE_URL}/protected/profile",
                        headers={"Authorization": f"Bearer {token}"})
    return "Access granted" if res.status_code == 200 else "Access denied"


print(try_login(VALID_TOKEN))
print(try_login("fake-token"))
# Output:
# Access granted
# Access denied

# SOLUTION:
# def try_login(token):
#     res = requests.get(f"{BASE_URL}/protected/profile",
#                         headers={"Authorization": f"Bearer {token}"})
#     return "Access granted" if res.status_code == 200 else "Access denied"
# print(try_login(VALID_TOKEN))
# print(try_login("fake-token"))


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections covered in this file: C (REST/JSON, 4 problems),
# D (auth headers, 4 problems) — 8 problems total.
# Difficulty breakdown: 4 🟢 Warm-up, 3 🟡 Core, 1 🔴 Challenge
#
# NEXT: day23_practise_problems_03_httpx_mixed.py — Section E,
# mixed challenges combining httpx + everything from Day 23.
