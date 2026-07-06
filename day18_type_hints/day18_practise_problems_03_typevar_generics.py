"""
Day 18 — Practice Problems
File 3 of 3: TypeVar, Generics & Mixed Challenges

Cumulative scope: Days 1-18.
Difficulty legend: 🟢 Warm-up | 🟡 Core | 🔴 Challenge

Section index:
    D — TypeVar & Generics (5 problems)
    E — Mixed Challenges (3 problems, combining all of Day 18)

How to run:
    python day18_practise_problems_03_typevar_generics.py
"""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")

print("=" * 50)
print("SECTION D: TypeVar & Generics")
print("=" * 50)

# ──────────────────────────────────────────────────────────
# D1. 🟢 Warm-up
# Declare a TypeVar T and write a generic function
# `last_item(items: list[T]) -> T` returning the last element of any list.
# Test with [10, 20, 30] and with ["Delhi", "Chennai"].
# Expected output:
#   30
#   Chennai
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def last_item(items: list[T]) -> T:
#     return items[-1]
#
# print(last_item([10, 20, 30]))
# print(last_item(["Delhi", "Chennai"]))
# Output:
# 30
# Chennai


# ──────────────────────────────────────────────────────────
# D2. 🟢 Warm-up
# Write a generic function `duplicate(value: T) -> tuple[T, T]` that
# returns the given value twice in a tuple. Test with "Namaste" and 7.
# Expected output:
#   ('Namaste', 'Namaste')
#   (7, 7)
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def duplicate(value: T) -> tuple[T, T]:
#     return (value, value)
#
# print(duplicate("Namaste"))
# print(duplicate(7))
# Output:
# ('Namaste', 'Namaste')
# (7, 7)


# ──────────────────────────────────────────────────────────
# D3. 🟡 Core
# Write a generic class `Queue(Generic[T])` with methods
# `enqueue(self, item: T) -> None`, `dequeue(self) -> T` (removes and
# returns the OLDEST item), and `__len__(self) -> int`.
# Create a Queue[str], enqueue "Priya", "Arjun", "Riya" in that order,
# then dequeue once and print both the dequeued value and the new length.
# Expected output:
#   Priya
#   2
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# class Queue(Generic[T]):
#     def __init__(self) -> None:
#         self._items: list[T] = []
#
#     def enqueue(self, item: T) -> None:
#         self._items.append(item)
#
#     def dequeue(self) -> T:
#         return self._items.pop(0)
#
#     def __len__(self) -> int:
#         return len(self._items)
#
# queue: Queue[str] = Queue()
# queue.enqueue("Priya")
# queue.enqueue("Arjun")
# queue.enqueue("Riya")
# print(queue.dequeue())
# print(len(queue))
# Output:
# Priya
# 2


# ──────────────────────────────────────────────────────────
# D4. 🟡 Core
# Write a generic function `map_values(items: list[T], transform) -> list[T]`
# that applies `transform` to every item in the list and returns a new
# list (the transform function itself does not need a type hint here).
# Test with items = [100.0, 200.0, 300.0] and transform = lambda x: x * 1.18
# (adding 18% GST). Round each result to 2 decimals before returning.
# Expected output:
#   [118.0, 236.0, 354.0]
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def map_values(items: list[T], transform) -> list[T]:  # type: ignore[no-untyped-def]
#     return [transform(item) for item in items]
#
# gst_prices = map_values([100.0, 200.0, 300.0], lambda x: round(x * 1.18, 2))
# print(gst_prices)
# Output:
# [118.0, 236.0, 354.0]


# ──────────────────────────────────────────────────────────
# D5. 🔴 Challenge
# Write a generic class `Cache(Generic[T])` with:
#   - __init__(self) -> None, storing an internal dict[str, T]
#   - set(self, key: str, value: T) -> None
#   - get(self, key: str) -> Optional[T]  (None if the key is missing)
# Create Cache[int](), set "orders_today" to 42, then print get() for
# both "orders_today" and a missing key "orders_yesterday".
# Expected output:
#   42
#   None
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# class Cache(Generic[T]):
#     def __init__(self) -> None:
#         self._store: dict[str, T] = {}
#
#     def set(self, key: str, value: T) -> None:
#         self._store[key] = value
#
#     def get(self, key: str) -> Optional[T]:
#         return self._store.get(key)
#
# cache: Cache[int] = Cache()
# cache.set("orders_today", 42)
# print(cache.get("orders_today"))
# print(cache.get("orders_yesterday"))
# Output:
# 42
# None


print("\n" + "=" * 50)
print("SECTION E: Mixed Challenges (Day 18 end-to-end)")
print("=" * 50)

# ──────────────────────────────────────────────────────────
# E1. 🟡 Core
# Combine Optional + a typed class: write `find_cheapest(prices: dict[str, float]) -> Optional[tuple[str, float]]`
# that returns the (item_name, price) pair with the lowest price, or
# None if the dict is empty.
# Test with {"Thali": 150.0, "Biryani": 220.0, "Dosa": 90.0} and with {}.
# Expected output:
#   ('Dosa', 90.0)
#   None
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def find_cheapest(prices: dict[str, float]) -> Optional[tuple[str, float]]:
#     if not prices:
#         return None
#     cheapest_name = min(prices, key=lambda name: prices[name])
#     return cheapest_name, prices[cheapest_name]
#
# print(find_cheapest({"Thali": 150.0, "Biryani": 220.0, "Dosa": 90.0}))
# print(find_cheapest({}))
# Output:
# ('Dosa', 90.0)
# None


# ──────────────────────────────────────────────────────────
# E2. 🟡 Core
# Combine a generic Stack (Day 18 file 3 concept) with Union input:
# write a function `process_ids(raw_ids: list[int | str]) -> list[str]`
# that normalises every ID to a zero-padded 6-digit string using
# str(x).zfill(6), pushes each onto a Stack[str] (reuse the Stack
# class idea inline, or a plain list), and returns them in REVERSE
# order (last pushed first) as a list.
# Test with raw_ids = [45, "1023", 7].
# Expected output:
#   ['000007', '001023', '000045']
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def process_ids(raw_ids: list[int | str]) -> list[str]:
#     stack: list[str] = []
#     for raw_id in raw_ids:
#         stack.append(str(raw_id).zfill(6))
#     return list(reversed(stack))
#
# print(process_ids([45, "1023", 7]))
# Output:
# ['000007', '001023', '000045']


# ──────────────────────────────────────────────────────────
# E3. 🔴 Challenge
# Write a fully type-hinted function
# `summarise_orders(orders: list[dict[str, float | str]]) -> dict[str, Optional[float]]`
# that takes a list of order dicts each shaped like
# {"customer": str, "amount": float}, and returns a summary dict with
# keys "total" (sum of all amounts) and "highest_amount" (the max
# amount, or None if the list is empty).
# Test with:
#   [{"customer": "Sanjay Verma", "amount": 450.0},
#    {"customer": "Meera Iyer", "amount": 899.0}]
# Expected output:
#   {'total': 1349.0, 'highest_amount': 899.0}
# ──────────────────────────────────────────────────────────
# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def summarise_orders(orders: list[dict[str, float | str]]) -> dict[str, Optional[float]]:
#     if not orders:
#         return {"total": 0.0, "highest_amount": None}
#     amounts = [float(order["amount"]) for order in orders]
#     return {"total": sum(amounts), "highest_amount": max(amounts)}
#
# sample_orders = [
#     {"customer": "Sanjay Verma", "amount": 450.0},
#     {"customer": "Meera Iyer", "amount": 899.0},
# ]
# print(summarise_orders(sample_orders))
# Output:
# {'total': 1349.0, 'highest_amount': 899.0}


# ════════════════════════════════════════════════════════════
# SUMMARY — Day 18 Practice Problems (all 3 files)
# ════════════════════════════════════════════════════════════
# File 1 — Section A (Prior Days Review): 2 problems
#          Section B (Type Hints Basics): 5 problems
# File 2 — Section C (Optional & Union):  5 problems
# File 3 — Section D (TypeVar & Generics): 5 problems
#          Section E (Mixed Challenges):   3 problems
#
# Difficulty breakdown: 6 Warm-up 🟢 | 8 Core 🟡 | 6 Challenge 🔴
# Total problems this day: 20
#
# Preview of Day 19 problem set: custom context managers using
# __enter__/__exit__, contextlib.contextmanager, and resource-cleanup
# patterns (file handles, database connections, timers).

if __name__ == "__main__":
    pass
