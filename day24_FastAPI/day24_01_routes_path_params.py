"""
Day 24 — Web Framework: FastAPI (Part 1 of 3)
================================================================

Topic   : Defining routes and path parameters
Covers  : Creating a FastAPI app, @app.get()/@app.post() decorators,
          path parameters, automatic type conversion & validation,
          multiple path parameters, and route ordering rules.

Prerequisites:
    - Day 23 (requests, REST concepts, JSON, auth headers)
    - Comfortable with Python type hints (Day 18) and Pydantic-style
      thinking (we formally meet Pydantic models in the next file)

How to run this file:
    1. Install dependencies (one-time):
         pip install fastapi uvicorn pydantic httpx2 --break-system-packages
    2. Run it like any other script:
         python day24_01_routes_path_params.py
       This file does NOT start a live server. Instead, it uses FastAPI's
       TestClient to call the routes directly inside the script, so you
       get instant, reproducible output without needing a browser or a
       second terminal.
    3. To run this as a REAL live server later (optional, for your own
       exploration), you would save just the `app = FastAPI()` part in
       a file named main.py and run:
         uvicorn main:app --reload
       Then visit http://127.0.0.1:8000/docs in your browser.

Context for this file:
    We are building the backend for "TiffinExpress" — the same fictional
    food-delivery service whose API you *consumed* on Day 23. Today you
    are the one *building* it with FastAPI.
================================================================
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

# ════════════════════════════════════════════════════════════════
# SECTION 1: Creating a FastAPI app
# ════════════════════════════════════════════════════════════════
# ── What is FastAPI? ──
# FastAPI is a modern Python web framework for building APIs.
# You define "routes" (URL paths) as plain Python functions, and
# FastAPI takes care of:
#   - Parsing the incoming request
#   - Converting/validating data types
#   - Generating interactive documentation automatically (Day 24 Part 3)
#
# Every FastAPI project starts with a single FastAPI() instance —
# think of it as the central object that all your routes attach to.

app = FastAPI(
    title="TiffinExpress API",
    description="A food-delivery backend built for Day 24 of the course",
    version="1.0.0",
)


# ════════════════════════════════════════════════════════════════
# SECTION 2: Your first route — @app.get()
# ════════════════════════════════════════════════════════════════
# ── The @app.get() decorator ──
# This decorator registers a function to handle HTTP GET requests
# made to the given path. The function's return value is
# automatically converted to JSON.

@app.get("/")
def read_root():
    """The root route — often used as a simple health check."""
    return {"service": "TiffinExpress API", "status": "running"}


@app.get("/restaurants")
def list_restaurants():
    """Returns a hardcoded list of restaurants (a real app would query a database)."""
    return [
        {"id": 1, "name": "Saffron Spice", "city": "Mumbai", "cuisine": "North Indian"},
        {"id": 2, "name": "Dakshin Delight", "city": "Chennai", "cuisine": "South Indian"},
        {"id": 3, "name": "Punjabi Tadka", "city": "Delhi", "cuisine": "Punjabi"},
    ]


# ════════════════════════════════════════════════════════════════
# SECTION 3: Path parameters
# ════════════════════════════════════════════════════════════════
# ── What is a path parameter? ──
# A path parameter is a variable part of the URL, written inside
# curly braces in the route decorator, e.g. /restaurants/{restaurant_id}.
# FastAPI passes the matched value straight into your function as an
# argument with the SAME name.
#
# ── Automatic type conversion & validation ──
# If you add a type hint to the parameter (e.g. `restaurant_id: int`),
# FastAPI will:
#   1. Convert the URL string to that type automatically
#   2. Return a clean 422 error automatically if conversion fails
#      (e.g. someone requests /restaurants/abc)
# This happens with ZERO extra code from you — that's the "FastAPI magic".

@app.get("/restaurants/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    """Fetch a single restaurant by its numeric ID."""
    restaurants = {
        1: {"id": 1, "name": "Saffron Spice", "city": "Mumbai"},
        2: {"id": 2, "name": "Dakshin Delight", "city": "Chennai"},
        3: {"id": 3, "name": "Punjabi Tadka", "city": "Delhi"},
    }
    if restaurant_id not in restaurants:
        # We will cover proper error responses (404s) in Day 27 (capstone).
        # For now, a simple dict works fine for demonstration.
        return {"error": f"No restaurant with id {restaurant_id}"}
    return restaurants[restaurant_id]


# ════════════════════════════════════════════════════════════════
# SECTION 4: Multiple path parameters
# ════════════════════════════════════════════════════════════════
# ── Combining more than one path parameter ──
# A route can capture several variable segments. Each one becomes
# its own function argument.

@app.get("/restaurants/{restaurant_id}/menu/{item_id}")
def get_menu_item(restaurant_id: int, item_id: int):
    """Fetch a specific menu item belonging to a specific restaurant."""
    menu = {
        (1, 101): {"item": "Butter Chicken", "price_inr": 320},
        (1, 102): {"item": "Dal Makhani", "price_inr": 220},
        (2, 201): {"item": "Masala Dosa", "price_inr": 140},
    }
    key = (restaurant_id, item_id)
    if key not in menu:
        return {"error": f"Item {item_id} not found for restaurant {restaurant_id}"}
    return menu[key]


# ════════════════════════════════════════════════════════════════
# SECTION 5: Route ordering matters!
# ════════════════════════════════════════════════════════════════
# ── A common beginner mistake ──
# FastAPI matches routes TOP TO BOTTOM, in the order they are defined.
# If you define /restaurants/{restaurant_id} BEFORE a more specific
# static path like /restaurants/featured, FastAPI will try to convert
# "featured" into an int for restaurant_id — and fail!
#
# RULE: Always define specific/static paths BEFORE parameterized ones.

@app.get("/restaurants/featured")
def get_featured_restaurant():
    """
    This route MUST be defined before /restaurants/{restaurant_id}
    or it will never be reached (FastAPI would try to match "featured"
    against the {restaurant_id}: int converter and fail with a 422).
    """
    return {"id": 1, "name": "Saffron Spice", "badge": "Featured This Week"}


# Note: in this file, get_featured_restaurant() is defined AFTER
# get_restaurant() in the source, which would normally be a bug.
# FastAPI resolves routes in REGISTRATION order, so watch this in
# your own projects — reorder decorators, don't just reorder functions
# that happen to look separate. We demonstrate the fix in the
# mini-challenge at the bottom of this file.


# ════════════════════════════════════════════════════════════════
# SECTION 6: Guided Examples (Indian context)
# ════════════════════════════════════════════════════════════════
print("=" * 60)
print("GUIDED EXAMPLES — Day 24 Part 1: Routes & Path Parameters")
print("=" * 60)

client = TestClient(app)

# Example 1: Hitting the root route
print("\n[Example 1] Root route")
response = client.get("/")
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'service': 'TiffinExpress API', 'status': 'running'}

# Example 2: Listing all restaurants
print("\n[Example 2] Priya Sharma browses all restaurants")
response = client.get("/restaurants")
print("Status code:", response.status_code)   # Output: 200
for r in response.json():
    print(f"  #{r['id']} {r['name']} ({r['city']}) - {r['cuisine']}")

# Example 3: Fetching one restaurant by path parameter
print("\n[Example 3] Arjun Mehta looks up restaurant id=2")
response = client.get("/restaurants/2")
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'id': 2, 'name': 'Dakshin Delight', 'city': 'Chennai'}

# Example 4: Automatic type validation in action
print("\n[Example 4] Riya Deshmukh accidentally sends a non-numeric id")
response = client.get("/restaurants/not-a-number")
print("Status code:", response.status_code)   # Output: 422
print("JSON body  :", response.json())
# Output: FastAPI auto-generates a 422 error explaining the int conversion failed

print("-" * 50)

# Example 5: Two path parameters together
print("\n[Example 5] Sanjay Verma views the Butter Chicken listing")
response = client.get("/restaurants/1/menu/101")
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'item': 'Butter Chicken', 'price_inr': 320}

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Meera Iyer wants a NEW route: /restaurants/top-rated that returns a
# hardcoded "best restaurant of the month" response. She adds it AFTER
# get_restaurant() in the file (same mistake as Section 5) and it breaks.
#
# Your task:
#   1. Write a route function `get_top_rated_restaurant()` for the path
#      "/restaurants/top-rated"
#   2. Register it on the `app` object using the CORRECT position so it
#      does not get shadowed by /restaurants/{restaurant_id}
#      (Hint: in THIS file, that means defining it before line where
#      get_restaurant's decorator appears — but since Python already
#      parsed this file top-down, add it directly below this comment
#      using a *new* FastAPI app to prove the concept in isolation.)
#   3. Verify with TestClient that GET /restaurants/top-rated returns
#      your hardcoded data, NOT a 422 error.
#
# Expected final print: {'name': 'Punjabi Tadka', 'badge': 'Top Rated'}

# YOUR CODE HERE


# SOLUTION:
# demo_app = FastAPI()
#
# @demo_app.get("/restaurants/top-rated")          # specific path FIRST
# def get_top_rated_restaurant():
#     return {"name": "Punjabi Tadka", "badge": "Top Rated"}
#
# @demo_app.get("/restaurants/{restaurant_id}")     # parameterized path SECOND
# def get_restaurant_demo(restaurant_id: int):
#     return {"id": restaurant_id}
#
# demo_client = TestClient(demo_app)
# result = demo_client.get("/restaurants/top-rated")
# print(result.json())
# # Output: {'name': 'Punjabi Tadka', 'badge': 'Top Rated'}


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# In this file you learned:
#   ✔ How to create a FastAPI() app instance
#   ✔ @app.get() to define GET routes
#   ✔ Path parameters and automatic type conversion/validation
#   ✔ Multiple path parameters in a single route
#   ✔ Why route ORDER matters (specific paths before parameterized ones)
#
# Next file: day24_02_query_params_pydantic.py
#   -> Query parameters, request bodies, and Pydantic models for
#      validating incoming data (e.g. placing a food order).
