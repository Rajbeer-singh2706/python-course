"""
Day 24 — Web Framework: FastAPI (Part 3 of 3)
================================================================

Topic   : Async endpoints and auto-generated Swagger UI (/docs)
Covers  : async def routes, why async matters for I/O-bound work,
          awaiting async calls inside a route, the OpenAPI schema,
          Swagger UI (/docs) and ReDoc (/redoc), and putting
          everything from Parts 1-2 together in one final mini app.

Prerequisites:
    - day24_01_routes_path_params.py
    - day24_02_query_params_pydantic.py
    - Day 16 (asyncio basics — async/await, asyncio.run())

How to run this file:
    pip install fastapi uvicorn pydantic httpx2 --break-system-packages
    python day24_03_async_swagger_docs.py

    This script demonstrates everything via TestClient, exactly like
    Parts 1 and 2. To actually SEE the Swagger UI in your browser
    (highly recommended once!), save the `app` object from this file
    into main.py and run:
        uvicorn main:app --reload
    then open http://127.0.0.1:8000/docs
================================================================
"""

import asyncio
import time
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(
    title="TiffinExpress API",
    description="Full food-delivery backend - Day 24 capstone-prep app",
    version="1.0.0",
)


# ════════════════════════════════════════════════════════════════
# SECTION 1: Why async matters
# ════════════════════════════════════════════════════════════════
# ── Sync vs async routes ──
# A normal ("sync") route function blocks the whole worker while it
# runs. If your route waits on something slow — a database query,
# a call to another API, reading a large file — that worker can't
# handle any OTHER request in the meantime.
#
# An "async def" route lets FastAPI pause that specific request while
# it's waiting on I/O (using `await`), and handle OTHER incoming
# requests during the wait. This is exactly the same event-loop idea
# from Day 16 (asyncio) — FastAPI is built on top of it.
#
# RULE OF THUMB:
#   - Route does no I/O waiting (pure computation)  -> either works
#   - Route awaits something (DB call, HTTP call)    -> use async def
#     and await the operation, so FastAPI can juggle other requests

@app.get("/sync-slow")
def sync_slow_endpoint():
    """A SYNC route that blocks for 0.1s — simulates a slow DB call
    done the wrong way (blocking). We keep this short for demo speed."""
    time.sleep(0.1)  # blocking sleep - freezes this worker
    return {"message": "Finished the slow (blocking) operation"}


@app.get("/async-slow")
async def async_slow_endpoint():
    """An ASYNC route that 'awaits' a delay — this yields control back
    to the event loop, letting other requests be served meanwhile."""
    await asyncio.sleep(0.1)  # non-blocking - other requests can proceed
    return {"message": "Finished the slow (non-blocking) operation"}


# ── Simulating an async database/network call ──
async def fetch_delivery_partner_eta(restaurant_id: int) -> int:
    """
    Pretend this reaches out to a delivery-partner service over the
    network (like the requests/httpx calls from Day 23, but async).
    We use asyncio.sleep() to simulate that network wait time.
    """
    await asyncio.sleep(0.05)
    eta_lookup = {1: 25, 2: 30, 3: 20}
    return eta_lookup.get(restaurant_id, 35)


@app.get("/restaurants/{restaurant_id}/eta")
async def get_delivery_eta(restaurant_id: int):
    """An async route that awaits our simulated async helper function."""
    eta_minutes = await fetch_delivery_partner_eta(restaurant_id)
    return {"restaurant_id": restaurant_id, "eta_minutes": eta_minutes}


# ════════════════════════════════════════════════════════════════
# SECTION 2: The auto-generated OpenAPI schema
# ════════════════════════════════════════════════════════════════
# ── Where does /docs come from? ──
# Every FastAPI app automatically builds a machine-readable spec of
# your entire API called the "OpenAPI schema" (JSON), available at
# /openapi.json. It is generated purely from:
#   - Your route decorators (@app.get, @app.post, ...)
#   - Your type hints (path/query parameter types)
#   - Your Pydantic models (request/response body shapes)
#
# FastAPI then feeds that schema into two ready-made UIs:
#   /docs   -> Swagger UI (interactive - you can try requests live)
#   /redoc  -> ReDoc (clean, read-only reference documentation)
#
# You never write these pages by hand — they update automatically
# whenever you change a route or a Pydantic model.

class MenuItemOut(BaseModel):
    """Pydantic models used in responses also show up in /docs,
    documenting exactly what shape of JSON clients should expect back."""
    item_name: str
    price_inr: float = Field(gt=0)


@app.get("/restaurants/{restaurant_id}/featured-item", response_model=MenuItemOut)
def get_featured_item(restaurant_id: int):
    """
    `response_model=MenuItemOut` tells FastAPI (and therefore /docs)
    exactly what the response JSON will look like, and FastAPI will
    filter/validate the returned data against it automatically.
    """
    featured = {
        1: {"item_name": "Butter Chicken", "price_inr": 320},
        2: {"item_name": "Masala Dosa", "price_inr": 140},
    }
    return featured.get(restaurant_id, {"item_name": "Chef's Special", "price_inr": 199})


# ════════════════════════════════════════════════════════════════
# SECTION 3: Guided Examples (Indian context)
# ════════════════════════════════════════════════════════════════
print("=" * 60)
print("GUIDED EXAMPLES — Day 24 Part 3: Async & Swagger Docs")
print("=" * 60)

client = TestClient(app)

# Example 1: Comparing sync vs async response times
print("\n[Example 1] Priya Sharma times the sync vs async slow routes")
start = time.perf_counter()
client.get("/sync-slow")
sync_duration = time.perf_counter() - start

start = time.perf_counter()
client.get("/async-slow")
async_duration = time.perf_counter() - start

print(f"Sync route took ~{sync_duration:.2f}s, async route took ~{async_duration:.2f}s")
# Output: both take about the same time when called ALONE, one after
# another. The real benefit of async shows up under CONCURRENT load —
# many requests at once — which is what Day 25+ deployment scenarios
# involve, not something a single-request demo like this can show.

print("-" * 50)

# Example 2: Awaiting a simulated async helper
print("\n[Example 2] Arjun Mehta checks delivery ETA for restaurant 2")
response = client.get("/restaurants/2/eta")
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'restaurant_id': 2, 'eta_minutes': 30}

print("-" * 50)

# Example 3: Unknown restaurant falls back to default ETA
print("\n[Example 3] Riya Deshmukh checks an unregistered restaurant id")
response = client.get("/restaurants/99/eta")
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'restaurant_id': 99, 'eta_minutes': 35}

print("-" * 50)

# Example 4: response_model in action
print("\n[Example 4] Sanjay Verma fetches the featured item")
response = client.get("/restaurants/1/featured-item")
print("Status code:", response.status_code)   # Output: 200
print("JSON body  :", response.json())
# Output: {'item_name': 'Butter Chicken', 'price_inr': 320.0}

print("-" * 50)

# Example 5: Inspecting the auto-generated OpenAPI schema
print("\n[Example 5] Meera Iyer inspects the auto-generated API schema")
response = client.get("/openapi.json")
schema = response.json()
print("Status code:", response.status_code)   # Output: 200
print("API title  :", schema["info"]["title"])
# Output: TiffinExpress API
print("Registered paths:", list(schema["paths"].keys())[:5])
# Output: a list including '/sync-slow', '/async-slow',
#         '/restaurants/{restaurant_id}/eta', etc.

print("-" * 50)

# Example 6: Confirming /docs and /redoc exist
print("\n[Example 6] Confirming Swagger UI and ReDoc are being served")
docs_response = client.get("/docs")
redoc_response = client.get("/redoc")
print("Status code /docs :", docs_response.status_code)   # Output: 200
print("Status code /redoc:", redoc_response.status_code)  # Output: 200
print("(In a real browser, /docs shows an interactive 'Try it out' UI)")

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Write an ASYNC route:
#   @app.get("/restaurants/{restaurant_id}/rating")
#   async def get_restaurant_rating(restaurant_id: int): ...
#
# It should:
#   1. Define (or reuse) an async helper `fetch_rating(restaurant_id)`
#      that awaits asyncio.sleep(0.02) then returns a hardcoded rating
#      from a dict, defaulting to 4.0 for unknown ids.
#   2. Return {"restaurant_id": restaurant_id, "rating": <value>}
#   3. Test it with restaurant_id=1 (should return a specific rating)
#      and restaurant_id=42 (should return the 4.0 default)

# YOUR CODE HERE


# SOLUTION:
# async def fetch_rating(restaurant_id: int) -> float:
#     await asyncio.sleep(0.02)
#     ratings = {1: 4.5, 2: 4.2, 3: 3.8}
#     return ratings.get(restaurant_id, 4.0)
#
# @app.get("/restaurants/{restaurant_id}/rating")
# async def get_restaurant_rating(restaurant_id: int):
#     rating = await fetch_rating(restaurant_id)
#     return {"restaurant_id": restaurant_id, "rating": rating}
#
# response = client.get("/restaurants/1/rating")
# print(response.json())    # Output: {'restaurant_id': 1, 'rating': 4.5}
#
# response = client.get("/restaurants/42/rating")
# print(response.json())    # Output: {'restaurant_id': 42, 'rating': 4.0}


# ════════════════════════════════════════════════════════════════
# SUMMARY — Day 24 complete!
# ════════════════════════════════════════════════════════════════
# Across all three files today you learned:
#   ✔ Creating a FastAPI app and defining GET/POST routes
#   ✔ Path parameters with automatic type conversion/validation
#   ✔ Query parameters (required, optional, constrained with Query())
#   ✔ Pydantic BaseModel + Field() for validating request bodies
#   ✔ async def routes and awaiting async helper functions
#   ✔ How /docs (Swagger UI) and /redoc are auto-generated from your
#     routes, type hints, and Pydantic models — zero manual writing
#
# Next up: Day 25 — Databases & Packaging
#   -> SQLite + SQLAlchemy ORM to replace our in-memory dicts/lists
#      with a real persistent database, plus pyproject.toml packaging
#      and Docker basics. This directly sets up the Day 26-30 capstone
#      project (the full Task Manager API).
