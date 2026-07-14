"""
Day 24 — Practice Problems (File 2 of 3)
================================================================
Topic          : Section C (Query Params & Request Bodies) +
                 Section D (Pydantic Models & Validation)
Difficulty key : 🟢 Warm-up   🟡 Core   🔴 Challenge

How to run: python day24_practise_problems_02_query_pydantic.py
================================================================
"""

from typing import Optional

from fastapi import FastAPI, Query
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

print("=" * 60)
print("DAY 24 PRACTICE — FILE 2: Query Params & Pydantic Models")
print("=" * 60)

app = FastAPI()
client = TestClient(app)


# ════════════════════════════════════════════════════════════════
# SECTION C: Query Parameters & Request Bodies
# ════════════════════════════════════════════════════════════════

# --- Problem C1 🟢 Warm-up ---
# Create a GET route "/menu" with an optional query parameter
# `veg_only: bool = False`. If veg_only is True, filter a hardcoded
# menu list down to items where item["is_veg"] is True; otherwise
# return the full list.

# YOUR CODE HERE


# SOLUTION:
# menu_items = [
#     {"name": "Paneer Tikka", "is_veg": True},
#     {"name": "Chicken Curry", "is_veg": False},
#     {"name": "Veg Biryani", "is_veg": True},
# ]
#
# @app.get("/menu")
# def get_menu(veg_only: bool = False):
#     if veg_only:
#         return [item for item in menu_items if item["is_veg"]]
#     return menu_items
#
# print(client.get("/menu").json())
# # Output: all 3 items
# print(client.get("/menu", params={"veg_only": True}).json())
# # Output: [{'name': 'Paneer Tikka', 'is_veg': True}, {'name': 'Veg Biryani', 'is_veg': True}]
print("-" * 50)


# --- Problem C2 🟢 Warm-up ---
# Create a GET route "/orders/filter" with a REQUIRED query parameter
# `status: str`. Return {"filtering_by": status}.
# Test calling it WITHOUT the parameter and confirm you get a 422.

# YOUR CODE HERE


# SOLUTION:
# @app.get("/orders/filter")
# def filter_orders(status: str):
#     return {"filtering_by": status}
#
# print(client.get("/orders/filter", params={"status": "delivered"}).json())
# # Output: {'filtering_by': 'delivered'}
# print(client.get("/orders/filter").status_code)
# # Output: 422
print("-" * 50)


# --- Problem C3 🟡 Core ---
# Create a GET route "/restaurants/top" using Query() to constrain a
# `limit: int` parameter between 1 and 10 (inclusive), default 3.
# Return the first `limit` names from a hardcoded list of 10 restaurant
# names. Test with the default, then with limit=15 to see the 422.

# YOUR CODE HERE


# SOLUTION:
# top_restaurants = [f"Restaurant {i}" for i in range(1, 11)]
#
# @app.get("/restaurants/top")
# def get_top_restaurants(limit: int = Query(default=3, ge=1, le=10)):
#     return top_restaurants[:limit]
#
# print(client.get("/restaurants/top").json())
# # Output: ['Restaurant 1', 'Restaurant 2', 'Restaurant 3']
# print(client.get("/restaurants/top", params={"limit": 15}).status_code)
# # Output: 422
print("-" * 50)


# --- Problem C4 🟡 Core ---
# Create a POST route "/support-tickets" that accepts a raw dict body
# (no Pydantic model yet — just to contrast with Section D). Use
# type hint `ticket: dict`. Return {"received_keys": list(ticket.keys())}.
# Test by POSTing {"subject": "Late delivery", "order_id": 12}.

# YOUR CODE HERE


# SOLUTION:
# @app.post("/support-tickets")
# def create_ticket(ticket: dict):
#     return {"received_keys": list(ticket.keys())}
#
# response = client.post("/support-tickets", json={"subject": "Late delivery", "order_id": 12})
# print(response.json())
# # Output: {'received_keys': ['subject', 'order_id']}
print("-" * 50)


# --- Problem C5 🔴 Challenge ---
# Create a GET route "/restaurants/search-advanced" combining:
#   - required query param `city: str`
#   - optional query param `min_price: Optional[float] = None`
#   - Query()-constrained param `page: int = Query(default=1, ge=1)`
# Return a dict echoing back all three values. Test with just city,
# then with all three params supplied.

# YOUR CODE HERE


# SOLUTION:
# @app.get("/restaurants/search-advanced")
# def search_advanced(city: str, min_price: Optional[float] = None, page: int = Query(default=1, ge=1)):
#     return {"city": city, "min_price": min_price, "page": page}
#
# print(client.get("/restaurants/search-advanced", params={"city": "Pune"}).json())
# # Output: {'city': 'Pune', 'min_price': None, 'page': 1}
# print(client.get("/restaurants/search-advanced",
#       params={"city": "Pune", "min_price": 200, "page": 2}).json())
# # Output: {'city': 'Pune', 'min_price': 200.0, 'page': 2}
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION D: Pydantic Models & Validation
# ════════════════════════════════════════════════════════════════

# --- Problem D1 🟢 Warm-up ---
# Define a Pydantic model `CustomerCreate` with fields:
#   name: str, phone: str, city: str = "Unknown" (default value)
# Create a POST route "/customers" accepting this model and returning
# it back via .model_dump(). Test with a payload missing "city".

# YOUR CODE HERE


# SOLUTION:
# class CustomerCreate(BaseModel):
#     name: str
#     phone: str
#     city: str = "Unknown"
#
# @app.post("/customers")
# def create_customer(customer: CustomerCreate):
#     return customer.model_dump()
#
# response = client.post("/customers", json={"name": "Priya Sharma", "phone": "9876543210"})
# print(response.json())
# # Output: {'name': 'Priya Sharma', 'phone': '9876543210', 'city': 'Unknown'}
print("-" * 50)


# --- Problem D2 🟡 Core ---
# Define a Pydantic model `DiscountCoupon` with fields:
#   code: str
#   percent_off: float = Field(gt=0, le=100)
# Create a POST route "/coupons" accepting this model and returning it.
# Test with percent_off=150 and confirm you get a 422.

# YOUR CODE HERE


# SOLUTION:
# class DiscountCoupon(BaseModel):
#     code: str
#     percent_off: float = Field(gt=0, le=100)
#
# @app.post("/coupons")
# def create_coupon(coupon: DiscountCoupon):
#     return coupon.model_dump()
#
# response = client.post("/coupons", json={"code": "FESTIVE10", "percent_off": 150})
# print(response.status_code)
# # Output: 422
print("-" * 50)


# --- Problem D3 🟡 Core ---
# Define a Pydantic model `Address` with fields: street: str, city: str,
# pincode: str. Then define `CustomerWithAddress` with fields:
#   name: str
#   address: Address   (a NESTED Pydantic model!)
# Create a POST route "/customers-full" accepting CustomerWithAddress.
# Test with a nested JSON payload and print the parsed city.

# YOUR CODE HERE


# SOLUTION:
# class Address(BaseModel):
#     street: str
#     city: str
#     pincode: str
#
# class CustomerWithAddress(BaseModel):
#     name: str
#     address: Address
#
# @app.post("/customers-full")
# def create_customer_full(customer: CustomerWithAddress):
#     return {"name": customer.name, "city": customer.address.city}
#
# payload = {
#     "name": "Arjun Mehta",
#     "address": {"street": "MG Road", "city": "Bengaluru", "pincode": "560001"},
# }
# response = client.post("/customers-full", json=payload)
# print(response.json())
# # Output: {'name': 'Arjun Mehta', 'city': 'Bengaluru'}
print("-" * 50)


# --- Problem D4 🔴 Challenge ---
# Define a Pydantic model `BulkOrderItem` with fields:
#   item_name: str
#   quantity: int = Field(gt=0, le=50)
# Create a POST route "/bulk-orders" accepting `items: list[BulkOrderItem]`
# directly as the body (a LIST of models, not wrapped in another model).
# Return {"total_items": sum of all quantities}.
# Test with 2 valid items, then with one item having quantity=100 (422).

# YOUR CODE HERE


# SOLUTION:
# class BulkOrderItem(BaseModel):
#     item_name: str
#     quantity: int = Field(gt=0, le=50)
#
# @app.post("/bulk-orders")
# def create_bulk_order(items: list[BulkOrderItem]):
#     return {"total_items": sum(item.quantity for item in items)}
#
# valid_payload = [
#     {"item_name": "Samosa", "quantity": 10},
#     {"item_name": "Jalebi", "quantity": 5},
# ]
# response = client.post("/bulk-orders", json=valid_payload)
# print(response.json())
# # Output: {'total_items': 15}
#
# invalid_payload = [{"item_name": "Samosa", "quantity": 100}]
# response = client.post("/bulk-orders", json=invalid_payload)
# print(response.status_code)
# # Output: 422
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# File 2 covered:
#   Section C: 5 problems (query params - optional, required, Query() constraints)
#   Section D: 4 problems (Pydantic models - defaults, Field constraints, nesting, lists)
# Difficulty breakdown: 2x 🟢 Warm-up | 4x 🟡 Core | 2x 🔴 Challenge
#
# Next: day24_practise_problems_03_async_mixed.py
#   -> Section E (Async Endpoints) and Section F (Mixed Challenges)
