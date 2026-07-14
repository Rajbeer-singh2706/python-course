"""
Day 24 — Web Framework: FastAPI (Part 2 of 3)
================================================================

Topic   : Query parameters, request bodies, and Pydantic models
Covers  : Optional/required query parameters, default values,
          Query() constraints, POST request bodies, Pydantic
          BaseModel for validation, Field() constraints, combining
          path + query + body in one route.

Prerequisites:
    - day24_01_routes_path_params.py (this file continues that app)

How to run this file:
    pip install fastapi uvicorn pydantic httpx2 --break-system-packages
    python day24_02_query_params_pydantic.py
    (Uses TestClient — no live server needed, same approach as Part 1.)
================================================================
"""

from typing import Optional

from fastapi import FastAPI, Query
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title="TiffinExpress API - Part 2")


# ════════════════════════════════════════════════════════════════
# SECTION 1: Query parameters
# ════════════════════════════════════════════════════════════════
# ── What is a query parameter? ──
# Query parameters appear AFTER a "?" in a URL, e.g.
#   /restaurants/search?city=Mumbai&min_rating=4
# Unlike path parameters, they are NOT part of the route pattern.
# Any function parameter that is NOT named in the path automatically
# becomes a query parameter in FastAPI.

@app.get("/restaurants/search")
def search_restaurants(city: str, cuisine: Optional[str] = None):
    """
    'city' is REQUIRED (no default value given).
    'cuisine' is OPTIONAL — if the client doesn't send it, it defaults
    to None, and we skip filtering by cuisine.
    """
    restaurants = [
        {"name": "Saffron Spice", "city": "Mumbai", "cuisine": "North Indian"},
        {"name": "Dakshin Delight", "city": "Chennai", "cuisine": "South Indian"},
        {"name": "Bombay Bites", "city": "Mumbai", "cuisine": "Street Food"},
    ]
    results = [r for r in restaurants if r["city"] == city]
    if cuisine:
        results = [r for r in results if r["cuisine"] == cuisine]
    return {"count": len(results), "results": results}


# ── Query() for validation constraints ──
# Just like path parameters, query parameters can carry validation.
# Use Query(...) to set defaults, minimum/maximum length, numeric
# ranges, and descriptions (the description shows up in the docs — Part 3).

@app.get("/restaurants/nearby")
def nearby_restaurants(
    max_results: int = Query(default=5, ge=1, le=20, description="How many results to return"),
    min_rating: float = Query(default=0.0, ge=0.0, le=5.0),
):
    """ge = 'greater than or equal', le = 'less than or equal' — FastAPI
    rejects out-of-range values automatically with a 422 response."""
    all_restaurants = [
        {"name": "Saffron Spice", "rating": 4.5},
        {"name": "Dakshin Delight", "rating": 4.2},
        {"name": "Punjabi Tadka", "rating": 3.8},
    ]
    filtered = [r for r in all_restaurants if r["rating"] >= min_rating]
    return filtered[:max_results]


# ════════════════════════════════════════════════════════════════
# SECTION 2: Pydantic models for request bodies
# ════════════════════════════════════════════════════════════════
# ── Why not just use a dict for incoming data? ──
# You COULD accept a raw dict, but then you get zero validation and
# zero auto-documentation. Pydantic models give you:
#   - Automatic type checking/conversion
#   - Required vs optional fields
#   - Custom constraints via Field()
#   - Clean error messages when data is invalid
#
# A Pydantic model is a class that inherits from BaseModel, with
# type-hinted class attributes describing each field.

class OrderItem(BaseModel):
    """A single item within an order."""
    item_name: str
    quantity: int = Field(gt=0, description="Must order at least 1 of this item")
    price_inr: float = Field(gt=0)


class OrderCreate(BaseModel):
    """The full request body for placing a new order."""
    customer_name: str
    restaurant_id: int
    items: list[OrderItem]
    delivery_instructions: Optional[str] = None  # optional field, defaults to None


# ════════════════════════════════════════════════════════════════
# SECTION 3: POST routes and request bodies
# ════════════════════════════════════════════════════════════════
# ── @app.post() with a Pydantic model parameter ──
# When a function parameter's type hint is a Pydantic model (not a
# primitive like int/str), FastAPI knows to look for it in the
# REQUEST BODY (as JSON) instead of the URL.

orders_db = []  # in-memory "database" for this demo


@app.post("/orders")
def place_order(order: OrderCreate):
    """
    FastAPI automatically:
      1. Parses the incoming JSON body
      2. Validates it against the OrderCreate model
      3. Returns a clean 422 error if anything is missing/invalid
      4. Gives us a fully-typed `order` object to work with — no
         manual json.loads() or key-checking required!
    """
    total = sum(item.quantity * item.price_inr for item in order.items)
    order_record = {
        "order_id": len(orders_db) + 1,
        "customer_name": order.customer_name,
        "restaurant_id": order.restaurant_id,
        "item_count": len(order.items),
        "total_inr": total,
    }
    orders_db.append(order_record)
    return order_record


# ════════════════════════════════════════════════════════════════
# SECTION 4: Combining path + query + body in ONE route
# ════════════════════════════════════════════════════════════════
@app.post("/restaurants/{restaurant_id}/orders")
def place_order_for_restaurant(
    restaurant_id: int,                       # path parameter
    order: OrderCreate,                       # request body (Pydantic model)
    priority: bool = Query(default=False),    # query parameter
):
    """
    FastAPI tells these apart AUTOMATICALLY based on where each
    parameter's name appears:
      - restaurant_id -> matches {restaurant_id} in the path
      - order         -> a Pydantic model, so it must be the body
      - priority      -> a plain bool with a default, so it's a query param
    """
    total = sum(item.quantity * item.price_inr for item in order.items)
    return {
        "restaurant_id": restaurant_id,
        "customer_name": order.customer_name,
        "priority_delivery": priority,
        "total_inr": total,
    }


# ════════════════════════════════════════════════════════════════
# SECTION 5: Guided Examples (Indian context)
# ════════════════════════════════════════════════════════════════
print("=" * 60)
print("GUIDED EXAMPLES — Day 24 Part 2: Query Params & Pydantic")
print("=" * 60)

client = TestClient(app)

# Example 1: Required + optional query parameters
print("\n[Example 1] Priya Sharma searches Mumbai restaurants")
response = client.get("/restaurants/search", params={"city": "Mumbai"})
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'count': 2, 'results': [Saffron Spice, Bombay Bites]}

print("-" * 50)

# Example 2: Adding the optional cuisine filter
print("\n[Example 2] Arjun Mehta narrows the search by cuisine")
response = client.get(
    "/restaurants/search", params={"city": "Mumbai", "cuisine": "Street Food"}
)
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'count': 1, 'results': [Bombay Bites]}

print("-" * 50)

# Example 3: Query() constraint violation
print("\n[Example 3] Riya Deshmukh requests 100 results (max allowed is 20)")
response = client.get("/restaurants/nearby", params={"max_results": 100})
print("Status code:", response.status_code)   # Output: 422
print("Error detail present:", "detail" in response.json())
# Output: True (FastAPI rejects it before our function code ever runs)

print("-" * 50)

# Example 4: Placing a valid order (POST with Pydantic body)
print("\n[Example 4] Sanjay Verma places an order")
order_payload = {
    "customer_name": "Sanjay Verma",
    "restaurant_id": 1,
    "items": [
        {"item_name": "Butter Chicken", "quantity": 2, "price_inr": 320},
        {"item_name": "Naan", "quantity": 4, "price_inr": 40},
    ],
    "delivery_instructions": "Ring the bell twice",
}
response = client.post("/orders", json=order_payload)
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'order_id': 1, 'customer_name': 'Sanjay Verma', ..., 'total_inr': 800.0}

print("-" * 50)

# Example 5: Invalid order body (Pydantic validation failure)
print("\n[Example 5] Meera Iyer sends an order with a negative quantity")
bad_payload = {
    "customer_name": "Meera Iyer",
    "restaurant_id": 2,
    "items": [{"item_name": "Masala Dosa", "quantity": -1, "price_inr": 140}],
}
response = client.post("/orders", json=bad_payload)
print("Status code:", response.status_code)   # Output: 422
print("Validation caught it:", response.status_code == 422)
# Output: True -> Field(gt=0) rejected the -1 before our code ran

print("-" * 50)

# Example 6: Path + query + body together
print("\n[Example 6] Combining path, query, and body in one call")
response = client.post(
    "/restaurants/3/orders",
    params={"priority": "true"},
    json={
        "customer_name": "Priya Sharma",
        "restaurant_id": 3,
        "items": [{"item_name": "Chole Bhature", "quantity": 1, "price_inr": 150}],
    },
)
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'restaurant_id': 3, ..., 'priority_delivery': True, 'total_inr': 150.0}

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Build a Pydantic model `FeedbackCreate` with fields:
#   - restaurant_id: int
#   - rating: float, constrained between 1 and 5 (inclusive) using Field
#   - comment: Optional[str] = None
# Then add a route:
#   @app.post("/feedback")
#   def submit_feedback(feedback: FeedbackCreate): ...
# that simply returns the feedback data back as confirmation.
# Test it with TestClient using a rating of 4.5 (valid) and then 7 (invalid).
# Expected: valid rating -> 200, rating of 7 -> 422

# YOUR CODE HERE


# SOLUTION:
# class FeedbackCreate(BaseModel):
#     restaurant_id: int
#     rating: float = Field(ge=1, le=5)
#     comment: Optional[str] = None
#
# @app.post("/feedback")
# def submit_feedback(feedback: FeedbackCreate):
#     return feedback.model_dump()
#
# response = client.post(
#     "/feedback", json={"restaurant_id": 1, "rating": 4.5, "comment": "Great food!"}
# )
# print(response.status_code)   # Output: 200
#
# response = client.post("/feedback", json={"restaurant_id": 1, "rating": 7})
# print(response.status_code)   # Output: 422


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file you learned:
#   ✔ Query parameters — required, optional, and default values
#   ✔ Query() for numeric/length constraints on query parameters
#   ✔ Pydantic BaseModel for defining request body shapes
#   ✔ Field() for per-field constraints (gt, ge, le, etc.)
#   ✔ How FastAPI distinguishes path vs query vs body parameters
#     purely from type hints and where names appear
#
# Next file: day24_03_async_swagger_docs.py
#   -> async def endpoints and the auto-generated Swagger UI (/docs)
