"""
Day 23 — Web Requests & APIs
File 2 of 4: REST API Concepts & JSON Response Parsing
========================================================================

WHAT THIS FILE COVERS
    - What "REST" actually means (resources, verbs, statelessness)
    - The four core HTTP verbs — GET, POST, PUT, DELETE
    - HTTP status code families (2xx, 4xx, 5xx) and what they mean
    - Parsing nested JSON structures from real responses
    - Turning a JSON API response into a Pandas DataFrame

PREREQUISITES
    - day23_01_requests_basics.py
    - Day 22 (Pandas) for the DataFrame section

HOW TO RUN
    python day23_02_rest_api_json.py
"""

import requests
import pandas as pd
from day23_00_mock_server import start_server

BASE_URL = start_server()

print("=" * 60)
print("DAY 23 — FILE 2: REST CONCEPTS & JSON PARSING")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION 1 — WHAT IS "REST"?
# ════════════════════════════════════════════════════════════
# REST (REpresentational State Transfer) is a style of API design
# built around "resources" — nouns like /orders or /restaurants —
# manipulated using standard HTTP verbs:
#
#   GET    /orders       → list all orders           (Read)
#   GET    /orders/3      → get one specific order    (Read)
#   POST   /orders       → create a new order         (Create)
#   PUT    /orders/3      → update an existing order  (Update)
#   DELETE /orders/3      → remove an order            (Delete)
#
# This "CRUD over HTTP verbs on a resource URL" pattern is why
# REST APIs feel predictable once you've used a few of them.
# REST APIs are also *stateless*: every request must carry all
# the information the server needs — the server doesn't remember
# your previous request.

print("\n── Section 1: CRUD Verbs in Action ──")

# CREATE
create_res = requests.post(f"{BASE_URL}/orders", json={
    "customer": "Riya Deshmukh", "restaurant": "Bikanervala",
    "city": "Delhi", "item": "Raj Kachori", "amount": 150,
})
new_id = create_res.json()["id"]
print(f"CREATE → new order id: {new_id}, status: {create_res.status_code}")   # Output: 201

# READ (one)
read_res = requests.get(f"{BASE_URL}/orders/{new_id}")
print(f"READ   → {read_res.json()}")

# UPDATE
update_res = requests.put(f"{BASE_URL}/orders/{new_id}", json={"status": "delivered"})
print(f"UPDATE → new status: {update_res.json()['status']}")   # Output: delivered

# DELETE
delete_res = requests.delete(f"{BASE_URL}/orders/{new_id}")
print(f"DELETE → {delete_res.json()}")
# Output: {'message': 'Order 8 cancelled successfully'}   (id will vary)


# ════════════════════════════════════════════════════════════
# SECTION 2 — HTTP STATUS CODE FAMILIES
# ════════════════════════════════════════════════════════════
#   1xx  Informational  (rarely seen directly)
#   2xx  Success          200 OK, 201 Created, 204 No Content
#   3xx  Redirection      301 Moved Permanently, 304 Not Modified
#   4xx  Client Error     400 Bad Request, 401 Unauthorized,
#                         403 Forbidden, 404 Not Found
#   5xx  Server Error     500 Internal Server Error, 503 Unavailable
#
# A simple rule of thumb: `status_code // 100` tells you the family.

print("\n── Section 2: Status Code Families ──")

samples = [
    requests.get(f"{BASE_URL}/orders"),          # 200
    requests.post(f"{BASE_URL}/orders", json={
        "customer": "Sanjay Verma", "restaurant": "Bikanervala",
        "city": "Delhi", "item": "Samosa Chaat", "amount": 90,
    }),   # 201
    requests.get(f"{BASE_URL}/orders/9999"),      # 404
]
for res in samples:
    family = res.status_code // 100
    label = {2: "Success", 4: "Client Error", 5: "Server Error"}.get(family, "Other")
    print(f"  {res.status_code} → family {family}xx → {label}")


# ════════════════════════════════════════════════════════════
# SECTION 3 — PARSING NESTED JSON
# ════════════════════════════════════════════════════════════
# Real-world API responses are rarely flat. You often need to dig
# into nested dicts/lists using normal Python indexing and loops.

print("\n── Section 3: Nested JSON ──")

# Simulate a richer, nested response shape (as many real APIs return)
nested_response = {
    "restaurant": {"name": "Saravana Bhavan", "city": "Chennai"},
    "order": {
        "id": 101,
        "customer": {"name": "Priya Sharma", "loyalty_tier": "Gold"},
        "items": [
            {"name": "Masala Dosa", "price": 120},
            {"name": "Filter Coffee", "price": 40},
        ],
    },
}

print("Restaurant name:", nested_response["restaurant"]["name"])
print("Customer name:", nested_response["order"]["customer"]["name"])
print("Loyalty tier:", nested_response["order"]["customer"]["loyalty_tier"])

item_total = sum(item["price"] for item in nested_response["order"]["items"])
print("Item names:", [item["name"] for item in nested_response["order"]["items"]])
print("Order total:", item_total)   # Output: 160


# ════════════════════════════════════════════════════════════
# SECTION 4 — FROM JSON RESPONSE TO PANDAS DATAFRAME
# ════════════════════════════════════════════════════════════
# A list of flat dicts (like our /orders response) converts
# directly into a DataFrame with pd.DataFrame(list_of_dicts).

print("\n── Section 4: JSON → DataFrame ──")

orders_json = requests.get(f"{BASE_URL}/orders").json()
df = pd.DataFrame(orders_json)
print(df[["id", "customer", "city", "amount", "status"]])

print("\nTotal revenue across all orders:", df["amount"].sum())
print("\nOrders per city:")
print(df.groupby("city")["id"].count())


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian Context
# ════════════════════════════════════════════════════════════
print("\n── Guided Examples ──")

# Example 1: Average order amount by restaurant
print("\nExample 1 — Average order amount per restaurant:")
orders_json = requests.get(f"{BASE_URL}/orders").json()
df2 = pd.DataFrame(orders_json)
print(df2.groupby("restaurant")["amount"].mean().round(2))

# Example 2: Update an order's status and verify via a fresh GET
print("\nExample 2 — Update then verify:")
target_id = orders_json[0]["id"]
requests.put(f"{BASE_URL}/orders/{target_id}", json={"status": "delivered"})
verify = requests.get(f"{BASE_URL}/orders/{target_id}").json()
print(f"  Order #{target_id} status is now: {verify['status']}")

# Example 3: Count orders by status family
print("\nExample 3 — Orders grouped by status:")
df3 = pd.DataFrame(requests.get(f"{BASE_URL}/orders").json())
print(df3["status"].value_counts())

# Example 4: Find the highest-value order and who placed it
print("\nExample 4 — Highest value order:")
top_order = df3.loc[df3["amount"].idxmax()]
print(f"  {top_order['customer']} spent ₹{top_order['amount']} at {top_order['restaurant']}")


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Fetch all restaurants, build a DataFrame, and print the name
# of the highest-rated restaurant along with its rating.
#
# Expected output (given current data):
#   Highest rated: Paradise Biryani (4.7)

print("\n── Mini-Challenge ──")

# YOUR CODE HERE
restaurants_json = requests.get(f"{BASE_URL}/restaurants").json()
rest_df = pd.DataFrame(restaurants_json)
best = rest_df.loc[rest_df["rating"].idxmax()]
print(f"  Highest rated: {best['name']} ({best['rating']})")

# SOLUTION (reference — matches the block above):
# restaurants_json = requests.get(f"{BASE_URL}/restaurants").json()
# rest_df = pd.DataFrame(restaurants_json)
# best = rest_df.loc[rest_df["rating"].idxmax()]
# print(f"Highest rated: {best['name']} ({best['rating']})")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file you learned:
#   ✔ REST resources + the CRUD-to-HTTP-verb mapping
#   ✔ HTTP status code families (2xx/4xx/5xx) and what they signal
#   ✔ Navigating nested JSON with plain Python indexing
#   ✔ Converting a JSON list response into a Pandas DataFrame
#
# NEXT: day23_03_auth_headers.py — Bearer tokens, API keys, and
# authenticated requests.
