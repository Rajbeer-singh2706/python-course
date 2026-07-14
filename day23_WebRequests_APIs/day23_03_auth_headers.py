"""
Day 23 — Web Requests & APIs
File 3 of 4: Authentication Headers — Bearer Tokens, API Keys, Sessions
========================================================================

WHAT THIS FILE COVERS
    - Why APIs require authentication
    - Bearer token authentication (Authorization header)
    - API key authentication (custom header)
    - Handling 401 Unauthorized responses gracefully
    - Reusing headers/cookies efficiently with requests.Session

PREREQUISITES
    - day23_01_requests_basics.py
    - day23_02_rest_api_json.py

HOW TO RUN
    python day23_03_auth_headers.py
"""

import requests
from day23_00_mock_server import start_server, VALID_TOKEN, VALID_API_KEY

BASE_URL = start_server()

print("=" * 60)
print("DAY 23 — FILE 3: AUTHENTICATION HEADERS")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION 1 — WHY AUTHENTICATION EXISTS
# ════════════════════════════════════════════════════════════
# Public endpoints (like /orders and /restaurants) can be called
# by anyone. But endpoints that expose personal data — like a
# customer's loyalty profile — need to know *who* is asking.
# APIs commonly use one of two header-based schemes:
#
#   1. Bearer Token  → Authorization: Bearer <token>
#   2. API Key       → X-API-Key: <key>   (header name varies by API)
#
# Both are just HTTP headers — no special magic, just a string
# the server checks before deciding whether to respond.

print("\n── Section 1: Calling a Protected Endpoint WITHOUT Credentials ──")

no_auth = requests.get(f"{BASE_URL}/protected/profile")
print("Status code:", no_auth.status_code)   # Output: 401
print("Error message:", no_auth.json()["error"])
# Output: Unauthorized. Missing or invalid Bearer token.


# ════════════════════════════════════════════════════════════
# SECTION 2 — BEARER TOKEN AUTHENTICATION
# ════════════════════════════════════════════════════════════
# The Authorization header format for Bearer auth is always:
#     Authorization: Bearer <token>
# The token itself is usually issued after a login step (not
# covered here) — we're using a fixed demo token for simplicity.

print("\n── Section 2: Bearer Token Authentication ──")

headers = {"Authorization": f"Bearer {VALID_TOKEN}"}
profile = requests.get(f"{BASE_URL}/protected/profile", headers=headers)

print("Status code:", profile.status_code)   # Output: 200
print("Profile data:", profile.json())
# Output: {'customer': 'Priya Sharma', 'loyalty_points': 1240, 'tier': 'Gold'}

# A wrong token still fails, just like a missing one
wrong_headers = {"Authorization": "Bearer wrong-token-000"}
wrong = requests.get(f"{BASE_URL}/protected/profile", headers=wrong_headers)
print("\nWrong token status:", wrong.status_code)   # Output: 401


# ════════════════════════════════════════════════════════════
# SECTION 3 — API KEY AUTHENTICATION
# ════════════════════════════════════════════════════════════
# Some APIs (analytics dashboards, payment gateways like Razorpay)
# prefer a dedicated custom header instead of the Authorization
# header. The header name is defined by that specific API's docs
# — here TiffinExpress uses `X-API-Key`.

print("\n── Section 3: API Key Authentication ──")

api_key_headers = {"X-API-Key": VALID_API_KEY}
analytics = requests.get(f"{BASE_URL}/protected/analytics", headers=api_key_headers)

print("Status code:", analytics.status_code)   # Output: 200
print("Analytics data:", analytics.json())
# Output: {'total_orders': 5, 'total_revenue': 1070}


# ════════════════════════════════════════════════════════════
# SECTION 4 — HANDLING 401s GRACEFULLY
# ════════════════════════════════════════════════════════════
# Production code should never assume a request succeeded. Check
# .status_code (or .ok) before trusting .json().

print("\n── Section 4: Graceful 401 Handling ──")


def fetch_profile(token):
    res = requests.get(f"{BASE_URL}/protected/profile",
                        headers={"Authorization": f"Bearer {token}"})
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 401:
        print("  Access denied — please check your credentials.")
        return None
    else:
        print(f"  Unexpected error: {res.status_code}")
        return None


print("With valid token:", fetch_profile(VALID_TOKEN))
print("With invalid token:")
fetch_profile("not-a-real-token")


# ════════════════════════════════════════════════════════════
# SECTION 5 — REUSING HEADERS WITH requests.Session
# ════════════════════════════════════════════════════════════
# When making many calls to the same authenticated API, a Session
# object lets you set headers once and reuse them (and connection
# pooling) across every request — cleaner and faster than repeating
# headers= on every call.

print("\n── Section 5: requests.Session ──")

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {VALID_TOKEN}"})

# Now every call through `session` automatically includes the header
profile_via_session = session.get(f"{BASE_URL}/protected/profile")
print("Session call status:", profile_via_session.status_code)   # Output: 200
print("Session call data:", profile_via_session.json())

session.close()


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian Context
# ════════════════════════════════════════════════════════════
print("\n── Guided Examples ──")

# Example 1: Build headers dynamically from a "logged in" variable
print("\nExample 1 — Dynamic header construction:")
logged_in_token = VALID_TOKEN   # simulating a token stored after login
auth_header = {"Authorization": f"Bearer {logged_in_token}"}
result = requests.get(f"{BASE_URL}/protected/profile", headers=auth_header)
print(f"  Welcome, {result.json()['customer']} — {result.json()['tier']} tier")

# Example 2: Try both auth schemes on the wrong endpoints to see them fail safely
print("\nExample 2 — Using the wrong scheme on the wrong endpoint:")
wrong_scheme = requests.get(f"{BASE_URL}/protected/analytics",
                            headers={"Authorization": f"Bearer {VALID_TOKEN}"})
print("  /protected/analytics with a Bearer token instead of X-API-Key:",
      wrong_scheme.status_code)   # Output: 401

# Example 3: A reusable authenticated client function
print("\nExample 3 — Reusable authenticated client function:")


def get_analytics(api_key):
    return requests.get(f"{BASE_URL}/protected/analytics",
                         headers={"X-API-Key": api_key})


print("  ", get_analytics(VALID_API_KEY).json())

# Example 4: Session used for two different protected calls
print("\nExample 4 — One Session, two protected calls:")
shared_session = requests.Session()
shared_session.headers.update({"Authorization": f"Bearer {VALID_TOKEN}"})
p = shared_session.get(f"{BASE_URL}/protected/profile").json()
print(f"  Profile via session: {p['customer']}, {p['loyalty_points']} points")
shared_session.close()


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Write a function `safe_get_analytics(key)` that returns the
# analytics dict on success, or the string "ACCESS DENIED" on a
# 401. Test it once with the correct key and once with a wrong one.
#
# Expected output:
#   {'total_orders': ..., 'total_revenue': ...}
#   ACCESS DENIED

print("\n── Mini-Challenge ──")

# YOUR CODE HERE
def safe_get_analytics(key):
    res = requests.get(f"{BASE_URL}/protected/analytics", headers={"X-API-Key": key})
    if res.status_code == 401:
        return "ACCESS DENIED"
    return res.json()


print(safe_get_analytics(VALID_API_KEY))
print(safe_get_analytics("wrong-key"))

# SOLUTION (reference — matches the block above):
# def safe_get_analytics(key):
#     res = requests.get(f"{BASE_URL}/protected/analytics", headers={"X-API-Key": key})
#     if res.status_code == 401:
#         return "ACCESS DENIED"
#     return res.json()


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file you learned:
#   ✔ Why protected endpoints need authentication
#   ✔ Bearer token auth via the Authorization header
#   ✔ API key auth via a custom header (X-API-Key)
#   ✔ Handling 401 Unauthorized responses without crashing
#   ✔ requests.Session for reusing headers across many calls
#
# NEXT: day23_04_httpx_async.py — the async httpx client and
# making multiple requests concurrently.
