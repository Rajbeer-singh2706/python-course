"""
Day 23 — Mock REST API Server (Utility Module)
================================================
This is NOT a student concept file — it's a small local REST API that the
Day 23 concept files and practice problems talk to using `requests` / `httpx`.

WHY A LOCAL SERVER?
Public demo APIs (httpbin.org, jsonplaceholder, etc.) are great in class but
can rate-limit or go offline at the worst possible moment during a live
session. This module spins up a tiny, real HTTP server on 127.0.0.1 that
speaks genuine REST + JSON, so every file in this session runs identically
every time, with zero internet dependency.

It simulates "TiffinExpress" — a fictional Indian food delivery API — with
an /orders resource (GET/POST/PUT/DELETE), a /restaurants resource, and
two protected endpoints for authentication demos.

Usage in any concept/practice file:
    from day23_00_mock_server import start_server
    BASE_URL = start_server()          # e.g. "http://127.0.0.1:8731"
"""

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

# ── In-memory "database" ──────────────────────────────────────────────
_orders = [
    {"id": 1, "customer": "Priya Sharma", "restaurant": "Saravana Bhavan",
     "city": "Chennai", "item": "Masala Dosa", "amount": 180, "status": "delivered"},
    {"id": 2, "customer": "Arjun Mehta", "restaurant": "Bikanervala",
     "city": "Delhi", "item": "Chole Bhature", "amount": 220, "status": "preparing"},
    {"id": 3, "customer": "Riya Deshmukh", "restaurant": "Shree Thaali",
     "city": "Pune", "item": "Gujarati Thali", "amount": 350, "status": "out_for_delivery"},
    {"id": 4, "customer": "Sanjay Verma", "restaurant": "Paradise Biryani",
     "city": "Hyderabad", "item": "Chicken Biryani", "amount": 280, "status": "delivered"},
    {"id": 5, "customer": "Meera Iyer", "restaurant": "Saravana Bhavan",
     "city": "Chennai", "item": "Filter Coffee", "amount": 40, "status": "delivered"},
]

_restaurants = [
    {"id": 1, "name": "Saravana Bhavan", "city": "Chennai", "rating": 4.6, "cuisine": "South Indian"},
    {"id": 2, "name": "Bikanervala", "city": "Delhi", "rating": 4.3, "cuisine": "North Indian"},
    {"id": 3, "name": "Shree Thaali", "city": "Pune", "rating": 4.5, "cuisine": "Gujarati"},
    {"id": 4, "name": "Paradise Biryani", "city": "Hyderabad", "rating": 4.7, "cuisine": "Hyderabadi"},
]

_VALID_TOKEN = "tiffin-secret-token-123"
_VALID_API_KEY = "tex-live-key-9f8a"
_next_id = [6]


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence default request logging for clean session output

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        return json.loads(self.rfile.read(length))

    # ── GET ──
    def do_GET(self):
        parsed = urlparse(self.path)
        path, query = parsed.path, parse_qs(parsed.query)

        if path == "/orders":
            results = _orders
            if "status" in query:
                results = [o for o in results if o["status"] == query["status"][0]]
            if "city" in query:
                results = [o for o in results if o["city"] == query["city"][0]]
            self._send_json(results)

        elif path.startswith("/orders/"):
            order_id = int(path.split("/")[-1])
            match = next((o for o in _orders if o["id"] == order_id), None)
            if match:
                self._send_json(match)
            else:
                self._send_json({"error": "Order not found"}, 404)

        elif path == "/restaurants":
            self._send_json(_restaurants)

        elif path == "/protected/profile":
            auth = self.headers.get("Authorization", "")
            if auth == f"Bearer {_VALID_TOKEN}":
                self._send_json({"customer": "Priya Sharma", "loyalty_points": 1240, "tier": "Gold"})
            else:
                self._send_json({"error": "Unauthorized. Missing or invalid Bearer token."}, 401)

        elif path == "/protected/analytics":
            api_key = self.headers.get("X-API-Key", "")
            if api_key == _VALID_API_KEY:
                self._send_json({"total_orders": len(_orders), "total_revenue": sum(o["amount"] for o in _orders)})
            else:
                self._send_json({"error": "Unauthorized. Missing or invalid X-API-Key header."}, 401)

        else:
            self._send_json({"error": "Not found"}, 404)

    # ── POST ──
    def do_POST(self):
        if self.path == "/orders":
            data = self._body()
            new_order = {
                "id": _next_id[0],
                "customer": data.get("customer", "Unknown"),
                "restaurant": data.get("restaurant", "Unknown"),
                "city": data.get("city", "Unknown"),
                "item": data.get("item", "Unknown"),
                "amount": data.get("amount", 0),
                "status": "placed",
            }
            _next_id[0] += 1
            _orders.append(new_order)
            self._send_json(new_order, 201)
        else:
            self._send_json({"error": "Not found"}, 404)

    # ── PUT ──
    def do_PUT(self):
        if self.path.startswith("/orders/"):
            order_id = int(self.path.split("/")[-1])
            match = next((o for o in _orders if o["id"] == order_id), None)
            if not match:
                self._send_json({"error": "Order not found"}, 404)
                return
            data = self._body()
            match.update({k: v for k, v in data.items() if k in match})
            self._send_json(match)
        else:
            self._send_json({"error": "Not found"}, 404)

    # ── DELETE ──
    def do_DELETE(self):
        if self.path.startswith("/orders/"):
            order_id = int(self.path.split("/")[-1])
            global _orders
            before = len(_orders)
            _orders = [o for o in _orders if o["id"] != order_id]
            if len(_orders) < before:
                self._send_json({"message": f"Order {order_id} cancelled successfully"})
            else:
                self._send_json({"error": "Order not found"}, 404)
        else:
            self._send_json({"error": "Not found"}, 404)


_server_instance = {"url": None}


def start_server():
    """Start the mock API server once (idempotent) and return its base URL."""
    if _server_instance["url"] is not None:
        return _server_instance["url"]

    server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    _server_instance["url"] = f"http://127.0.0.1:{port}"
    return _server_instance["url"]


VALID_TOKEN = _VALID_TOKEN
VALID_API_KEY = _VALID_API_KEY

if __name__ == "__main__":
    url = start_server()
    print(f"TiffinExpress mock API running at {url}")
    print("Try: GET /orders, /orders/<id>, /restaurants, /protected/profile, /protected/analytics")
    threading.Event().wait()
