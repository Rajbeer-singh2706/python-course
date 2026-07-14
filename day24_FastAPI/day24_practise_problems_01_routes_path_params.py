"""
Day 24 — Practice Problems (File 1 of 3)
================================================================
Topic          : Section A (Prior Days Review) + Section B (Routes & Path Params)
Cumulative     : Draws on Day 9 (errors), Day 18 (type hints), Day 23 (requests/JSON)
Difficulty key : 🟢 Warm-up   🟡 Core   🔴 Challenge

Section index for the full Day 24 problem set (across all 3 files):
    A. Prior Days Review ................. this file  (3 problems)
    B. Routes & Path Parameters ........... this file  (5 problems)
    C. Query Params & Request Bodies ...... file 2     (5 problems)
    D. Pydantic Models & Validation ....... file 2     (4 problems)
    E. Async Endpoints ..................... file 3    (3 problems)
    F. Mixed Challenges ................... file 3     (4 problems)
    ------------------------------------------------------------
    Total: 24 problems across 3 files

How to run: python day24_practise_problems_01_routes_path_params.py
================================================================
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

print("=" * 60)
print("DAY 24 PRACTICE — FILE 1: Review + Routes & Path Parameters")
print("=" * 60)


# ════════════════════════════════════════════════════════════════
# SECTION A: Prior Days Review
# ════════════════════════════════════════════════════════════════

# --- Problem A1 🟢 Warm-up ---
# Write a function `safe_divide(a, b)` that returns a / b, but
# catches ZeroDivisionError and returns the string "Cannot divide by zero"
# instead (Day 9 review). Test it with safe_divide(10, 0).

# YOUR CODE HERE


# SOLUTION:
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#
# print(safe_divide(10, 0))
# # Output: Cannot divide by zero
print("-" * 50)


# --- Problem A2 🟢 Warm-up ---
# Write a type-hinted function (Day 18) `format_price(amount: float) -> str`
# that returns the amount formatted as an Indian Rupee string, e.g.
# format_price(320.5) -> "₹320.50"

# YOUR CODE HERE


# SOLUTION:
# def format_price(amount: float) -> str:
#     return f"\u20b9{amount:.2f}"
#
# print(format_price(320.5))
# # Output: ₹320.50
print("-" * 50)


# --- Problem A3 🟡 Core ---
# Using the `requests`-style pattern from Day 23 (but simulated — do NOT
# make a real network call), write a function `parse_json_response(raw)`
# that takes a dict simulating a parsed JSON response like
# {"status": "ok", "data": {"id": 1, "name": "Saffron Spice"}}
# and returns just the "name" value from inside "data", or None if
# either key is missing.

# YOUR CODE HERE


# SOLUTION:
# def parse_json_response(raw):
#     return raw.get("data", {}).get("name")
#
# sample = {"status": "ok", "data": {"id": 1, "name": "Saffron Spice"}}
# print(parse_json_response(sample))
# # Output: Saffron Spice
# print(parse_json_response({"status": "error"}))
# # Output: None
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION B: Routes & Path Parameters
# ════════════════════════════════════════════════════════════════

app = FastAPI()
client = TestClient(app)


# --- Problem B1 🟢 Warm-up ---
# Create a GET route "/health" that returns {"status": "ok"}.
# Test it with TestClient and print the JSON response.

# YOUR CODE HERE


# SOLUTION:
# @app.get("/health")
# def health_check():
#     return {"status": "ok"}
#
# response = client.get("/health")
# print(response.json())
# # Output: {'status': 'ok'}
print("-" * 50)


# --- Problem B2 🟢 Warm-up ---
# Create a GET route "/drivers/{driver_id}" where driver_id is an int.
# It should return {"driver_id": driver_id, "name": "Assigned Driver"}.
# Test with driver_id=7.

# YOUR CODE HERE


# SOLUTION:
# @app.get("/drivers/{driver_id}")
# def get_driver(driver_id: int):
#     return {"driver_id": driver_id, "name": "Assigned Driver"}
#
# response = client.get("/drivers/7")
# print(response.json())
# # Output: {'driver_id': 7, 'name': 'Assigned Driver'}
print("-" * 50)


# --- Problem B3 🟡 Core ---
# Create a GET route "/orders/{order_id}/items/{item_index}" with TWO
# int path parameters. Return a dict with both values plus a hardcoded
# "item_name": "Sample Item". Test with order_id=5, item_index=2.

# YOUR CODE HERE


# SOLUTION:
# @app.get("/orders/{order_id}/items/{item_index}")
# def get_order_item(order_id: int, item_index: int):
#     return {"order_id": order_id, "item_index": item_index, "item_name": "Sample Item"}
#
# response = client.get("/orders/5/items/2")
# print(response.json())
# # Output: {'order_id': 5, 'item_index': 2, 'item_name': 'Sample Item'}
print("-" * 50)


# --- Problem B4 🟡 Core ---
# Demonstrate the "route ordering" trap from the concept file:
# Create a NEW FastAPI app `demo_app`. Register a route
# "/drivers/{driver_id}" (int) BEFORE a route "/drivers/available".
# Show (by testing GET /drivers/available) that it FAILS with a 422
# because "available" cannot convert to int. Then fix it by re-creating
# a second app with the correct order and show it succeeds with 200.

# YOUR CODE HERE


# SOLUTION:
# from fastapi import FastAPI as _FastAPI
#
# broken_app = _FastAPI()
#
# @broken_app.get("/drivers/{driver_id}")
# def get_driver_broken(driver_id: int):
#     return {"driver_id": driver_id}
#
# @broken_app.get("/drivers/available")
# def list_available_drivers_broken():
#     return {"available": True}
#
# broken_client = TestClient(broken_app)
# response = broken_client.get("/drivers/available")
# print("Broken order status:", response.status_code)
# # Output: Broken order status: 422
#
# fixed_app = _FastAPI()
#
# @fixed_app.get("/drivers/available")
# def list_available_drivers_fixed():
#     return {"available": True}
#
# @fixed_app.get("/drivers/{driver_id}")
# def get_driver_fixed(driver_id: int):
#     return {"driver_id": driver_id}
#
# fixed_client = TestClient(fixed_app)
# response = fixed_client.get("/drivers/available")
# print("Fixed order status:", response.status_code)
# # Output: Fixed order status: 200
print("-" * 50)


# --- Problem B5 🔴 Challenge ---
# Create a GET route "/restaurants/{restaurant_id}/reviews/{review_id}"
# with both params as int. Maintain a hardcoded dict keyed by
# (restaurant_id, review_id) tuples with review text, e.g.
#   (1, 1): "Great food, quick delivery!"
#   (1, 2): "A bit spicy for my taste."
#   (2, 1): "Loved the dosas!"
# Return {"error": "Review not found"} for missing keys (do NOT raise
# an exception - use a plain dict return like the concept file did).
# Test with (1, 1), (2, 1), and (9, 9) [missing].

# YOUR CODE HERE


# SOLUTION:
# reviews = {
#     (1, 1): "Great food, quick delivery!",
#     (1, 2): "A bit spicy for my taste.",
#     (2, 1): "Loved the dosas!",
# }
#
# @app.get("/restaurants/{restaurant_id}/reviews/{review_id}")
# def get_review(restaurant_id: int, review_id: int):
#     key = (restaurant_id, review_id)
#     if key not in reviews:
#         return {"error": "Review not found"}
#     return {"restaurant_id": restaurant_id, "review_id": review_id, "text": reviews[key]}
#
# print(client.get("/restaurants/1/reviews/1").json())
# # Output: {'restaurant_id': 1, 'review_id': 1, 'text': 'Great food, quick delivery!'}
# print(client.get("/restaurants/2/reviews/1").json())
# # Output: {'restaurant_id': 2, 'review_id': 1, 'text': 'Loved the dosas!'}
# print(client.get("/restaurants/9/reviews/9").json())
# # Output: {'error': 'Review not found'}
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# File 1 covered:
#   Section A: 3 problems (exception handling, type hints, JSON parsing review)
#   Section B: 5 problems (routes, path parameters, route ordering)
# Difficulty breakdown: 3x 🟢 Warm-up | 4x 🟡 Core | 1x 🔴 Challenge
#
# Next: day24_practise_problems_02_query_pydantic.py
#   -> Section C (Query Params & Request Bodies) and
#      Section D (Pydantic Models & Validation)
