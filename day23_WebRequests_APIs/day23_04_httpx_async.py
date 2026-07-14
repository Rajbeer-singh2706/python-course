"""
Day 23 — Web Requests & APIs
File 4 of 4: httpx — The Async HTTP Client
========================================================================

WHAT THIS FILE COVERS
    - Why an async HTTP client exists (concurrency vs. one-at-a-time)
    - httpx's synchronous API (a drop-in-feeling requests replacement)
    - httpx.AsyncClient with async/await
    - Running many requests concurrently with asyncio.gather()
    - Measuring the speed-up vs sequential requests

PREREQUISITES
    - day23_01_requests_basics.py through day23_03_auth_headers.py
    - Day 16 (Concurrency Basics) — async/await syntax, asyncio.run()
    - `pip install httpx --break-system-packages`

HOW TO RUN
    python day23_04_httpx_async.py
"""

import asyncio
import time

import httpx
from day23_00_mock_server import start_server

BASE_URL = start_server()

print("=" * 60)
print("DAY 23 — FILE 4: httpx ASYNC HTTP CLIENT")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION 1 — httpx AS A SYNC CLIENT (FEELS LIKE requests)
# ════════════════════════════════════════════════════════════
# httpx supports a synchronous API almost identical to requests,
# which makes it an easy drop-in when you later need async too.

print("\n── Section 1: httpx Synchronous API ──")

response = httpx.get(f"{BASE_URL}/orders")
print("Status code:", response.status_code)   # Output: 200
print("Order count:", len(response.json()))    # Output: 5

post_response = httpx.post(f"{BASE_URL}/orders", json={
    "customer": "Meera Iyer", "restaurant": "Saravana Bhavan",
    "city": "Chennai", "item": "Rava Kesari", "amount": 60,
})
print("POST status:", post_response.status_code)   # Output: 201


# ════════════════════════════════════════════════════════════
# SECTION 2 — WHY ASYNC MATTERS FOR NETWORK CALLS
# ════════════════════════════════════════════════════════════
# Network requests spend most of their time *waiting* for a
# response, not using the CPU. Async lets your program start many
# requests and let them all wait "at the same time" instead of
# one after another — this is I/O-bound concurrency, the same
# idea introduced in Day 16.

print("\n── Section 2: Sequential vs Concurrent Timing ──")

order_ids = [1, 2, 3, 4, 5]


def fetch_sequential():
    start = time.perf_counter()
    for oid in order_ids:
        httpx.get(f"{BASE_URL}/orders/{oid}")
    return time.perf_counter() - start


sequential_time = fetch_sequential()
print(f"Sequential (5 requests, one-by-one): {sequential_time:.4f}s")


# ════════════════════════════════════════════════════════════
# SECTION 3 — httpx.AsyncClient WITH async/await
# ════════════════════════════════════════════════════════════
# AsyncClient is used inside `async def` functions with `await`.
# It should be created with `async with` so it's properly closed.

print("\n── Section 3: A Single Async Request ──")


async def fetch_one_order(order_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/orders/{order_id}")
        return response.json()


result = asyncio.run(fetch_one_order(1))
print("Fetched order 1 via async client:", result["item"])
# Output: Masala Dosa


# ════════════════════════════════════════════════════════════
# SECTION 4 — CONCURRENT REQUESTS WITH asyncio.gather()
# ════════════════════════════════════════════════════════════
# asyncio.gather() runs a list of coroutines concurrently and
# waits for all of them to finish, returning results in order.

print("\n── Section 4: Concurrent Requests ──")


async def fetch_all_orders_concurrently(ids):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(f"{BASE_URL}/orders/{oid}") for oid in ids]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]


start = time.perf_counter()
concurrent_results = asyncio.run(fetch_all_orders_concurrently(order_ids))
concurrent_time = time.perf_counter() - start

print(f"Concurrent (5 requests, gathered): {concurrent_time:.4f}s")
print("Items fetched:", [o["item"] for o in concurrent_results])

print(f"\nSpeed-up factor: {sequential_time / concurrent_time:.1f}x faster")
# Output: some speed-up factor > 1.0 (exact value varies by machine)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian Context
# ════════════════════════════════════════════════════════════
print("\n── Guided Examples ──")


# Example 1: Fetch all restaurants concurrently with their orders
async def restaurant_and_orders():
    async with httpx.AsyncClient() as client:
        restaurants_task = client.get(f"{BASE_URL}/restaurants")
        orders_task = client.get(f"{BASE_URL}/orders")
        restaurants_res, orders_res = await asyncio.gather(restaurants_task, orders_task)
        return restaurants_res.json(), orders_res.json()


print("\nExample 1 — Fetching restaurants + orders concurrently:")
restaurants, orders = asyncio.run(restaurant_and_orders())
print(f"  {len(restaurants)} restaurants, {len(orders)} orders — both fetched in one gather()")


# Example 2: Concurrently fetch profile (Bearer) and analytics (API key)
async def dashboard_data(token, api_key):
    async with httpx.AsyncClient() as client:
        profile_task = client.get(f"{BASE_URL}/protected/profile",
                                   headers={"Authorization": f"Bearer {token}"})
        analytics_task = client.get(f"{BASE_URL}/protected/analytics",
                                     headers={"X-API-Key": api_key})
        profile_res, analytics_res = await asyncio.gather(profile_task, analytics_task)
        return profile_res.json(), analytics_res.json()


from day23_00_mock_server import VALID_TOKEN, VALID_API_KEY   # noqa: E402

print("\nExample 2 — Concurrent authenticated dashboard load:")
profile, analytics = asyncio.run(dashboard_data(VALID_TOKEN, VALID_API_KEY))
print(f"  Profile: {profile['customer']} ({profile['tier']})")
print(f"  Analytics: {analytics['total_orders']} orders, ₹{analytics['total_revenue']} revenue")


# Example 3: Place three orders concurrently
async def place_orders_concurrently(payloads):
    async with httpx.AsyncClient() as client:
        tasks = [client.post(f"{BASE_URL}/orders", json=p) for p in payloads]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]


print("\nExample 3 — Placing 3 orders concurrently:")
new_orders_payload = [
    {"customer": "Arjun Mehta", "restaurant": "Bikanervala", "city": "Delhi", "item": "Pav Bhaji", "amount": 130},
    {"customer": "Riya Deshmukh", "restaurant": "Shree Thaali", "city": "Pune", "item": "Dhokla", "amount": 80},
    {"customer": "Sanjay Verma", "restaurant": "Paradise Biryani", "city": "Hyderabad", "item": "Haleem", "amount": 200},
]
placed = asyncio.run(place_orders_concurrently(new_orders_payload))
for order in placed:
    print(f"  Order #{order['id']}: {order['item']} for {order['customer']}")

# Example 4: Handle one failing request inside a gather() without crashing
async def fetch_with_one_bad_id(ids):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(f"{BASE_URL}/orders/{oid}") for oid in ids]
        responses = await asyncio.gather(*tasks)
        return responses


print("\nExample 4 — One of the ids (999) does not exist:")
mixed_results = asyncio.run(fetch_with_one_bad_id([1, 999, 3]))
for res in mixed_results:
    if res.status_code == 200:
        print(f"  Found: {res.json()['item']}")
    else:
        print(f"  Not found (status {res.status_code})")


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Write an async function `fetch_items(ids)` that concurrently
# fetches the given order ids and returns a list of just the
# `item` field for each. Call it with ids [1, 4, 5].
#
# Expected output:
#   ['Masala Dosa', 'Chicken Biryani', 'Filter Coffee']

print("\n── Mini-Challenge ──")

# YOUR CODE HERE
async def fetch_items(ids):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(f"{BASE_URL}/orders/{oid}") for oid in ids]
        responses = await asyncio.gather(*tasks)
        return [r.json()["item"] for r in responses]


print(asyncio.run(fetch_items([1, 4, 5])))

# SOLUTION (reference — matches the block above):
# async def fetch_items(ids):
#     async with httpx.AsyncClient() as client:
#         tasks = [client.get(f"{BASE_URL}/orders/{oid}") for oid in ids]
#         responses = await asyncio.gather(*tasks)
#         return [r.json()["item"] for r in responses]
# print(asyncio.run(fetch_items([1, 4, 5])))


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file you learned:
#   ✔ httpx's requests-like synchronous API
#   ✔ Why I/O-bound network calls benefit from concurrency
#   ✔ httpx.AsyncClient inside async def functions
#   ✔ asyncio.gather() to run many requests at once
#
# NEXT: Day 24 — FastAPI: building your own REST API from scratch
# (routes, path/query parameters, Pydantic models, async endpoints).

if __name__ == "__main__":
    pass
