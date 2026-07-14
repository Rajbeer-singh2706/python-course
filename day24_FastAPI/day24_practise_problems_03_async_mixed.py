"""
Day 24 — Practice Problems (File 3 of 3)
================================================================
Topic          : Section E (Async Endpoints) + Section F (Mixed Challenges)
Difficulty key : 🟢 Warm-up   🟡 Core   🔴 Challenge

How to run: python day24_practise_problems_03_async_mixed.py
================================================================
"""

import asyncio
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

print("=" * 60)
print("DAY 24 PRACTICE — FILE 3: Async Endpoints & Mixed Challenges")
print("=" * 60)

app = FastAPI()
client = TestClient(app)


# ════════════════════════════════════════════════════════════════
# SECTION E: Async Endpoints
# ════════════════════════════════════════════════════════════════

# --- Problem E1 🟢 Warm-up ---
# Write an async route "/ping-async" using `async def` that awaits
# asyncio.sleep(0.01) then returns {"message": "pong"}.

# YOUR CODE HERE


# SOLUTION:
# @app.get("/ping-async")
# async def ping_async():
#     await asyncio.sleep(0.01)
#     return {"message": "pong"}
#
# response = client.get("/ping-async")
# print(response.json())
# # Output: {'message': 'pong'}
print("-" * 50)


# --- Problem E2 🟡 Core ---
# Write an async helper function `fetch_order_status(order_id)` that
# awaits asyncio.sleep(0.01) and returns a status from a hardcoded
# dict {1: "Preparing", 2: "Out for Delivery", 3: "Delivered"},
# defaulting to "Unknown" for missing ids. Wire it up to an async
# route "/orders/{order_id}/status". Test with order_id=2 and order_id=99.

# YOUR CODE HERE


# SOLUTION:
# async def fetch_order_status(order_id: int) -> str:
#     await asyncio.sleep(0.01)
#     statuses = {1: "Preparing", 2: "Out for Delivery", 3: "Delivered"}
#     return statuses.get(order_id, "Unknown")
#
# @app.get("/orders/{order_id}/status")
# async def get_order_status(order_id: int):
#     status = await fetch_order_status(order_id)
#     return {"order_id": order_id, "status": status}
#
# print(client.get("/orders/2/status").json())
# # Output: {'order_id': 2, 'status': 'Out for Delivery'}
# print(client.get("/orders/99/status").json())
# # Output: {'order_id': 99, 'status': 'Unknown'}
print("-" * 50)


# --- Problem E3 🔴 Challenge ---
# Write an async route "/restaurants/{restaurant_id}/full-details" that
# awaits TWO separate async helper functions concurrently using
# asyncio.gather(): one that fetches the restaurant name (hardcoded
# dict) and one that fetches its current queue length (hardcoded dict,
# default 0). Combine both results into one response dict.
# Test with restaurant_id=1.

# YOUR CODE HERE


# SOLUTION:
# async def fetch_restaurant_name(restaurant_id: int) -> str:
#     await asyncio.sleep(0.01)
#     names = {1: "Saffron Spice", 2: "Dakshin Delight"}
#     return names.get(restaurant_id, "Unknown Restaurant")
#
# async def fetch_queue_length(restaurant_id: int) -> int:
#     await asyncio.sleep(0.01)
#     queues = {1: 4, 2: 2}
#     return queues.get(restaurant_id, 0)
#
# @app.get("/restaurants/{restaurant_id}/full-details")
# async def get_full_details(restaurant_id: int):
#     name, queue_length = await asyncio.gather(
#         fetch_restaurant_name(restaurant_id),
#         fetch_queue_length(restaurant_id),
#     )
#     return {"restaurant_id": restaurant_id, "name": name, "queue_length": queue_length}
#
# response = client.get("/restaurants/1/full-details")
# print(response.json())
# # Output: {'restaurant_id': 1, 'name': 'Saffron Spice', 'queue_length': 4}
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION F: Mixed Challenges (combines Day 24 concepts end-to-end)
# ════════════════════════════════════════════════════════════════

# --- Problem F1 🟡 Core ---
# Build a small "cart" feature combining path params + Pydantic models:
#   - Pydantic model `CartItemAdd`: item_name: str, quantity: int = Field(gt=0)
#   - POST route "/carts/{cart_id}/items" accepting a CartItemAdd body,
#     returning {"cart_id": cart_id, "added": item_name, "quantity": quantity}
# Test with cart_id=10 and a valid item.

# YOUR CODE HERE


# SOLUTION:
# class CartItemAdd(BaseModel):
#     item_name: str
#     quantity: int = Field(gt=0)
#
# @app.post("/carts/{cart_id}/items")
# def add_to_cart(cart_id: int, item: CartItemAdd):
#     return {"cart_id": cart_id, "added": item.item_name, "quantity": item.quantity}
#
# response = client.post("/carts/10/items", json={"item_name": "Gulab Jamun", "quantity": 3})
# print(response.json())
# # Output: {'cart_id': 10, 'added': 'Gulab Jamun', 'quantity': 3}
print("-" * 50)


# --- Problem F2 🟡 Core ---
# Combine query params + Pydantic validation error handling:
# Create a GET route "/discounts/eligible" with a Query()-constrained
# `order_total: float = Query(ge=0)`. Return
# {"eligible": True, "discount_percent": 10} if order_total >= 500,
# else {"eligible": False, "discount_percent": 0}.
# Test with order_total=750 and order_total=-5 (expect 422 for negative).

# YOUR CODE HERE


# SOLUTION:
# @app.get("/discounts/eligible")
# def check_discount_eligibility(order_total: float = Query(ge=0)):
#     if order_total >= 500:
#         return {"eligible": True, "discount_percent": 10}
#     return {"eligible": False, "discount_percent": 0}
#
# print(client.get("/discounts/eligible", params={"order_total": 750}).json())
# # Output: {'eligible': True, 'discount_percent': 10}
# print(client.get("/discounts/eligible", params={"order_total": -5}).status_code)
# # Output: 422
print("-" * 50)


# --- Problem F3 🔴 Challenge ---
# Build an end-to-end async route combining path param + query param +
# Pydantic body + an awaited helper function:
#   - Pydantic model `RatingSubmit`: stars: int = Field(ge=1, le=5), comment: Optional[str] = None
#   - async helper `notify_restaurant_owner(restaurant_id, stars)` that
#     awaits asyncio.sleep(0.01) and returns True if stars <= 2 (flags a
#     low rating for owner attention), else False
#   - async POST route "/restaurants/{restaurant_id}/ratings" accepting
#     RatingSubmit body and a `notify: bool = Query(default=True)` param.
#     If notify is True AND the helper returns True, include
#     "owner_notified": True in the response; otherwise "owner_notified": False.
# Test with a 1-star rating (notify default True) and a 5-star rating.

# YOUR CODE HERE


# SOLUTION:
# class RatingSubmit(BaseModel):
#     stars: int = Field(ge=1, le=5)
#     comment: Optional[str] = None
#
# async def notify_restaurant_owner(restaurant_id: int, stars: int) -> bool:
#     await asyncio.sleep(0.01)
#     return stars <= 2
#
# @app.post("/restaurants/{restaurant_id}/ratings")
# async def submit_rating(restaurant_id: int, rating: RatingSubmit, notify: bool = Query(default=True)):
#     should_flag = await notify_restaurant_owner(restaurant_id, rating.stars)
#     owner_notified = notify and should_flag
#     return {"restaurant_id": restaurant_id, "stars": rating.stars, "owner_notified": owner_notified}
#
# response = client.post("/restaurants/1/ratings", json={"stars": 1, "comment": "Order was very late"})
# print(response.json())
# # Output: {'restaurant_id': 1, 'stars': 1, 'owner_notified': True}
#
# response = client.post("/restaurants/1/ratings", json={"stars": 5})
# print(response.json())
# # Output: {'restaurant_id': 1, 'stars': 5, 'owner_notified': False}
print("-" * 50)


# --- Problem F4 🔴 Challenge ---
# Build a mini "restaurant onboarding" flow tying together everything
# from Days 23-24:
#   - Pydantic model `RestaurantOnboard`: name: str, city: str,
#     cuisine: str, opening_hour: int = Field(ge=0, le=23)
#   - A module-level list `onboarded_restaurants = []` acting as a
#     fake database
#   - POST route "/admin/restaurants" accepting RestaurantOnboard,
#     appending a dict with an auto-incremented "id" (len + 1) to
#     onboarded_restaurants, and returning that dict
#   - GET route "/admin/restaurants" with an optional query param
#     `city: Optional[str] = None` that filters onboarded_restaurants
#     by city if provided, else returns all
# Test by onboarding two restaurants in different cities, then
# filtering the GET route by one of those cities.

# YOUR CODE HERE


# SOLUTION:
# class RestaurantOnboard(BaseModel):
#     name: str
#     city: str
#     cuisine: str
#     opening_hour: int = Field(ge=0, le=23)
#
# onboarded_restaurants = []
#
# @app.post("/admin/restaurants")
# def onboard_restaurant(restaurant: RestaurantOnboard):
#     record = restaurant.model_dump()
#     record["id"] = len(onboarded_restaurants) + 1
#     onboarded_restaurants.append(record)
#     return record
#
# @app.get("/admin/restaurants")
# def list_onboarded_restaurants(city: Optional[str] = None):
#     if city:
#         return [r for r in onboarded_restaurants if r["city"] == city]
#     return onboarded_restaurants
#
# client.post("/admin/restaurants", json={
#     "name": "Coastal Curry House", "city": "Kochi", "cuisine": "Seafood", "opening_hour": 11
# })
# client.post("/admin/restaurants", json={
#     "name": "Himalayan Kitchen", "city": "Dehradun", "cuisine": "Tibetan", "opening_hour": 10
# })
# response = client.get("/admin/restaurants", params={"city": "Kochi"})
# print(response.json())
# # Output: [{'name': 'Coastal Curry House', 'city': 'Kochi', 'cuisine': 'Seafood',
# #           'opening_hour': 11, 'id': 1}]
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY — Day 24 Practice Set complete!
# ════════════════════════════════════════════════════════════════
# File 3 covered:
#   Section E: 3 problems (async routes, awaited helpers, asyncio.gather)
#   Section F: 4 problems (mixed end-to-end challenges combining
#              path/query/body/async from across all three concept files)
# Difficulty breakdown: 1x 🟢 Warm-up | 3x 🟡 Core | 3x 🔴 Challenge
#
# ── Full Day 24 problem set summary (all 3 files) ──
#   Section A (Review)              : 3 problems
#   Section B (Routes & Path Params): 5 problems
#   Section C (Query & Bodies)      : 5 problems
#   Section D (Pydantic Models)     : 4 problems
#   Section E (Async Endpoints)     : 3 problems
#   Section F (Mixed Challenges)    : 4 problems
#   -----------------------------------------
#   TOTAL                           : 24 problems
#   Difficulty: 6x 🟢 Warm-up | 12x 🟡 Core | 6x 🔴 Challenge
#
# Next: Day 25 — Databases & Packaging
#   -> SQLite, SQLAlchemy ORM, pyproject.toml, and Docker basics
