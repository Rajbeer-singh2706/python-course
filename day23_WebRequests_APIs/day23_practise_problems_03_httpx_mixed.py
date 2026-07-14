"""
Day 23 — Web Requests & APIs — Practice Problems (3 of 3)
========================================================================
Day 23 Topic     : Web Requests & APIs
Cumulative Scope : Days 1–23
Difficulty Legend : 🟢 Warm-up   🟡 Core   🔴 Challenge

SECTION INDEX (this file)
    Section E — Mixed Challenges (requests + httpx + auth + pandas)  (4 problems)

Other files in this set:
    day23_practise_problems_01_requests_get_post.py → Sections A, B
    day23_practise_problems_02_json_auth.py         → Sections C, D

HOW TO RUN
    python day23_practise_problems_03_httpx_mixed.py
"""

import asyncio
import httpx
import pandas as pd
from day23_00_mock_server import start_server, VALID_TOKEN, VALID_API_KEY

BASE_URL = start_server()

print("=" * 60)
print("DAY 23 PRACTICE — FILE 3: SECTION E (MIXED CHALLENGES)")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION E — MIXED CHALLENGES
# ════════════════════════════════════════════════════════════

# ── Problem E1 ──
# 🟡 Core
# Using httpx (sync), fetch /orders, load into a Pandas DataFrame
# (Day 22 review), and print the total amount grouped by city.
print("\n── Problem E1 ──")

# YOUR CODE HERE
res = httpx.get(f"{BASE_URL}/orders")
df = pd.DataFrame(res.json())
print(df.groupby("city")["amount"].sum())
# Output (a Series: total amount per city, based on current server data)

# SOLUTION:
# res = httpx.get(f"{BASE_URL}/orders")
# df = pd.DataFrame(res.json())
# print(df.groupby("city")["amount"].sum())


print("-" * 50)

# ── Problem E2 ──
# 🟡 Core
# Write an async function `fetch_two(id_a, id_b)` using
# httpx.AsyncClient + asyncio.gather to fetch two orders
# concurrently, and print both items. Test with ids 1 and 4.
print("\n── Problem E2 ──")

# YOUR CODE HERE
async def fetch_two(id_a, id_b):
    async with httpx.AsyncClient() as client:
        res_a, res_b = await asyncio.gather(
            client.get(f"{BASE_URL}/orders/{id_a}"),
            client.get(f"{BASE_URL}/orders/{id_b}"),
        )
        return res_a.json()["item"], res_b.json()["item"]


item_a, item_b = asyncio.run(fetch_two(1, 4))
print(item_a)
print(item_b)
# Output:
# Masala Dosa
# Chicken Biryani

# SOLUTION:
# async def fetch_two(id_a, id_b):
#     async with httpx.AsyncClient() as client:
#         res_a, res_b = await asyncio.gather(
#             client.get(f"{BASE_URL}/orders/{id_a}"),
#             client.get(f"{BASE_URL}/orders/{id_b}"),
#         )
#         return res_a.json()["item"], res_b.json()["item"]
# item_a, item_b = asyncio.run(fetch_two(1, 4))
# print(item_a)
# print(item_b)


print("-" * 50)

# ── Problem E3 ──
# 🔴 Challenge
# Combine authentication + REST + error handling: write a function
# `place_order_for_gold_members(token, payload)` that:
#   1. Checks /protected/profile with the given token
#   2. If the tier is "Gold", POSTs the payload to /orders and
#      returns the new order id
#   3. Otherwise returns "Not eligible"
# Test it once with VALID_TOKEN and once with an invalid token.
print("\n── Problem E3 ──")

# YOUR CODE HERE
import requests


def place_order_for_gold_members(token, payload):
    profile_res = requests.get(f"{BASE_URL}/protected/profile",
                                headers={"Authorization": f"Bearer {token}"})
    if profile_res.status_code != 200:
        return "Not eligible"
    if profile_res.json().get("tier") != "Gold":
        return "Not eligible"
    order_res = requests.post(f"{BASE_URL}/orders", json=payload)
    return order_res.json()["id"]


test_payload = {"customer": "Priya Sharma", "restaurant": "Saravana Bhavan",
                 "city": "Chennai", "item": "Idli Sambar", "amount": 90}

print(place_order_for_gold_members(VALID_TOKEN, test_payload))
print(place_order_for_gold_members("bad-token", test_payload))
# Output:
# <some new integer id>
# Not eligible

# SOLUTION:
# def place_order_for_gold_members(token, payload):
#     profile_res = requests.get(f"{BASE_URL}/protected/profile",
#                                 headers={"Authorization": f"Bearer {token}"})
#     if profile_res.status_code != 200:
#         return "Not eligible"
#     if profile_res.json().get("tier") != "Gold":
#         return "Not eligible"
#     order_res = requests.post(f"{BASE_URL}/orders", json=payload)
#     return order_res.json()["id"]


print("-" * 50)

# ── Problem E4 ──
# 🔴 Challenge
# Cumulative challenge (Days 8, 22, 23): fetch all restaurants,
# convert to a DataFrame, write it to a CSV file named
# "restaurants_export.csv" (Day 8 file I/O + Day 22 pandas), then
# read the CSV back and print the number of rows.
print("\n── Problem E4 ──")

# YOUR CODE HERE
res = httpx.get(f"{BASE_URL}/restaurants")
rest_df = pd.DataFrame(res.json())
rest_df.to_csv("restaurants_export.csv", index=False)

reloaded = pd.read_csv("restaurants_export.csv")
print(len(reloaded))
# Output: 4

# SOLUTION:
# res = httpx.get(f"{BASE_URL}/restaurants")
# rest_df = pd.DataFrame(res.json())
# rest_df.to_csv("restaurants_export.csv", index=False)
# reloaded = pd.read_csv("restaurants_export.csv")
# print(len(reloaded))


# ════════════════════════════════════════════════════════════
# SUMMARY — FULL DAY 23 PROBLEM SET
# ════════════════════════════════════════════════════════════
# Section A — Prior Days Review .......... 3 problems
# Section B — requests GET/POST/params ... 5 problems
# Section C — REST verbs & JSON parsing ... 4 problems
# Section D — Authentication headers ..... 4 problems
# Section E — Mixed challenges (httpx) ... 4 problems
# ─────────────────────────────────────────────────
# TOTAL ................................... 20 problems
#
# Difficulty breakdown: 8 🟢 Warm-up, 8 🟡 Core, 4 🔴 Challenge
#
# NEXT: Day 24 — FastAPI: building your own REST API from scratch.
