"""
Day 23 — Web Requests & APIs
File 1 of 4: `requests` Basics — GET, POST, Headers, Query Parameters
========================================================================

WHAT THIS FILE COVERS
    - Installing and importing the `requests` library
    - Making a GET request and inspecting the Response object
    - Sending query parameters with `params=`
    - Making a POST request with a JSON body
    - Reading status codes, headers, and response text/json

PREREQUISITES
    - Day 22 (Pandas) — comfort reading tabular/JSON-shaped data helps here
    - `pip install requests --break-system-packages`

HOW TO RUN
    python day23_01_requests_basics.py

NOTE ON THE API USED IN THIS FILE
    All demos below talk to a local mock API called "TiffinExpress" (a
    fictional food delivery service) that we start automatically at the
    top of the file. This means the file runs identically every time,
    with no dependency on the public internet or a live server.
"""

import requests
from day23_00_mock_server import start_server

BASE_URL = start_server()

print("=" * 60)
print("DAY 23 — FILE 1: requests BASICS")
print(f"Mock TiffinExpress API running at: {BASE_URL}")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION 1 — YOUR FIRST GET REQUEST
# ════════════════════════════════════════════════════════════
# `requests.get(url)` sends an HTTP GET request and returns a
# `Response` object. GET is used to *retrieve* data — it should
# never change anything on the server.

print("\n── Section 1: Your First GET Request ──")

response = requests.get(f"{BASE_URL}/orders")

print("Status code:", response.status_code)   # Output: 200
print("Content-Type header:", response.headers["Content-Type"])
# Output: application/json

# .json() automatically parses the response body from a JSON
# string into a Python list/dict.
orders = response.json()
print("Type of parsed body:", type(orders))   # Output: <class 'list'>
print("Number of orders:", len(orders))        # Output: 5
print("First order:", orders[0])
# Output: {'id': 1, 'customer': 'Priya Sharma', ...}


# ════════════════════════════════════════════════════════════
# SECTION 2 — THE Response OBJECT IN DETAIL
# ════════════════════════════════════════════════════════════
# Every requests call returns a Response object with useful
# attributes: .status_code, .headers, .text, .json(), .ok, .url

print("\n── Section 2: The Response Object ──")

response = requests.get(f"{BASE_URL}/orders/2")

print("URL requested:", response.url)
print("response.ok (True if status < 400):", response.ok)   # Output: True
print("response.text (raw string body):")
print(response.text)
# Output: {"id": 2, "customer": "Arjun Mehta", ...}  (as a raw JSON string)

# A 404 example — requesting an order that does not exist
missing = requests.get(f"{BASE_URL}/orders/999")
print("\nRequesting a non-existent order (id=999):")
print("Status code:", missing.status_code)   # Output: 404
print("response.ok:", missing.ok)             # Output: False
print("Error body:", missing.json())          # Output: {'error': 'Order not found'}


# ════════════════════════════════════════════════════════════
# SECTION 3 — QUERY PARAMETERS WITH `params=`
# ════════════════════════════════════════════════════════════
# Instead of manually building "?status=delivered&city=Chennai"
# strings, pass a dictionary to `params=` and requests builds
# the query string (and URL-encodes it) for you.

print("\n── Section 3: Query Parameters ──")

filtered = requests.get(f"{BASE_URL}/orders", params={"status": "delivered"})
print("Filtered URL:", filtered.url)
# Output: http://127.0.0.1:PORT/orders?status=delivered
print("Delivered orders count:", len(filtered.json()))   # Output: 3

# Multiple filters at once
chennai_delivered = requests.get(
    f"{BASE_URL}/orders",
    params={"status": "delivered", "city": "Chennai"}
)
print("Chennai + delivered:", len(chennai_delivered.json()))   # Output: 2


# ════════════════════════════════════════════════════════════
# SECTION 4 — SENDING DATA WITH POST
# ════════════════════════════════════════════════════════════
# POST is used to *create* something new. Pass a Python dict to
# `json=` and requests will serialize it to JSON and set the
# Content-Type header automatically.

print("\n── Section 4: POST Requests ──")

new_order_payload = {
    "customer": "Meera Iyer",
    "restaurant": "Paradise Biryani",
    "city": "Hyderabad",
    "item": "Veg Biryani",
    "amount": 240,
}

created = requests.post(f"{BASE_URL}/orders", json=new_order_payload)

print("Status code:", created.status_code)   # Output: 201  (Created)
print("Server-assigned order:", created.json())
# Output: {'id': 6, 'customer': 'Meera Iyer', ..., 'status': 'placed'}


# ════════════════════════════════════════════════════════════
# SECTION 5 — CUSTOM REQUEST HEADERS
# ════════════════════════════════════════════════════════════
# Headers carry metadata about a request — content type,
# authentication tokens, user agent, etc. Pass a dict to
# `headers=` on any request method.

print("\n── Section 5: Custom Headers ──")

custom_headers = {
    "User-Agent": "TiffinExpress-Student-Client/1.0",
    "Accept": "application/json",
}
res = requests.get(f"{BASE_URL}/restaurants", headers=custom_headers)
print("Status:", res.status_code)             # Output: 200
print("Restaurant count:", len(res.json()))    # Output: 4


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian Context
# ════════════════════════════════════════════════════════════
print("\n── Guided Examples ──")

# Example 1: Fetch all restaurants and print their names + ratings
print("\nExample 1 — Restaurant directory:")
restaurants = requests.get(f"{BASE_URL}/restaurants").json()
for r in restaurants:
    print(f"  {r['name']} ({r['city']}) — {r['rating']}⭐ — {r['cuisine']}")

# Example 2: Fetch only orders that are still "preparing"
print("\nExample 2 — Orders currently being prepared:")
preparing = requests.get(f"{BASE_URL}/orders", params={"status": "preparing"}).json()
for o in preparing:
    print(f"  Order #{o['id']}: {o['item']} for {o['customer']} in {o['city']}")

# Example 3: Place an order for Sanjay Verma and confirm it was created
print("\nExample 3 — Placing a new order for Sanjay Verma:")
sanjay_order = requests.post(f"{BASE_URL}/orders", json={
    "customer": "Sanjay Verma",
    "restaurant": "Shree Thaali",
    "city": "Pune",
    "item": "Undhiyu Thali",
    "amount": 300,
})
print(f"  Created order #{sanjay_order.json()['id']} — status: {sanjay_order.json()['status']}")

# Example 4: Check how many orders now exist after the two POSTs above
print("\nExample 4 — Total orders after new placements:")
all_orders = requests.get(f"{BASE_URL}/orders").json()
print(f"  Total orders: {len(all_orders)}")   # Output: 7


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Fetch all orders from Delhi, print the customer name and item
# for each, then print the total amount spent across those orders.
#
# Expected output (given current data):
#   Arjun Mehta ordered Chole Bhature
#   Delhi total spend: 220

print("\n── Mini-Challenge ──")

# YOUR CODE HERE
delhi_orders = requests.get(f"{BASE_URL}/orders", params={"city": "Delhi"}).json()
total_spend = 0
for order in delhi_orders:
    print(f"  {order['customer']} ordered {order['item']}")
    total_spend += order["amount"]
print(f"  Delhi total spend: {total_spend}")

# SOLUTION (reference — matches the block above):
# delhi_orders = requests.get(f"{BASE_URL}/orders", params={"city": "Delhi"}).json()
# total_spend = sum(o["amount"] for o in delhi_orders)
# for order in delhi_orders:
#     print(f"{order['customer']} ordered {order['item']}")
# print(f"Delhi total spend: {total_spend}")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file you learned:
#   ✔ requests.get() and requests.post() basics
#   ✔ Reading .status_code, .headers, .text, .json(), .ok
#   ✔ Sending query parameters with params=
#   ✔ Sending a JSON body with json=
#   ✔ Sending custom headers with headers=
#
# NEXT: day23_02_rest_api_json.py — REST concepts, HTTP verbs,
# status code families, and working with nested JSON structures.
