"""
Day 16 - Practice Problems (File 3 of 3)
Topic: async/await & asyncio + Mixed Challenges (all Day 16 concepts)

Cumulative scope: Days 1-16

Difficulty legend:
    🟢 Warm-up   - direct application of one concept
    🟡 Core      - combines a few ideas, slightly more logic
    🔴 Challenge - multi-step reasoning, edge cases

Section Index:
    Section F - async/await & asyncio (5 problems)
    Section G - Mixed Challenges (4 problems)

How to run:
    python day16_practise_problems_03_async_mixed.py
"""

import asyncio
import threading

# ════════════════════════════════════════════════════════════════
# SECTION F: async/await & asyncio
# ════════════════════════════════════════════════════════════════

# --------------------------------------------------------------
# Problem F1  🟢 Warm-up
# --------------------------------------------------------------
# Write an async function `say_hello(name)` that awaits
# asyncio.sleep(0.01) then returns f"Hello, {name}". Use
# asyncio.run() to call it with "Riya" and print the result.
# Expected output:
#   Hello, Riya

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# async def say_hello(name):
#     await asyncio.sleep(0.01)
#     return f"Hello, {name}"
#
# print(asyncio.run(say_hello("Riya")))

# --------------------------------------------------------------
# Problem F2  🟢 Warm-up
# --------------------------------------------------------------
# Write an async function `square_async(n)` that awaits
# asyncio.sleep(0.01) then returns n * n. Write another async
# function `main_f2()` that awaits square_async(6) and prints the
# result. Run main_f2() with asyncio.run().
# Expected output:
#   36

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# async def square_async(n):
#     await asyncio.sleep(0.01)
#     return n * n
#
# async def main_f2():
#     result = await square_async(6)
#     print(result)
#
# asyncio.run(main_f2())

# --------------------------------------------------------------
# Problem F3  🟡 Core
# --------------------------------------------------------------
# Write an async function `get_weather(city)` that awaits
# asyncio.sleep(0.02) then returns f"{city}: Sunny". Using
# asyncio.gather(), concurrently fetch weather for "Chennai" and
# "Kolkata", then print both results.
# Expected output:
#   Chennai: Sunny
#   Kolkata: Sunny

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# async def get_weather(city):
#     await asyncio.sleep(0.02)
#     return f"{city}: Sunny"
#
# async def main_f3():
#     results = await asyncio.gather(get_weather("Chennai"), get_weather("Kolkata"))
#     for r in results:
#         print(r)
#
# asyncio.run(main_f3())

# --------------------------------------------------------------
# Problem F4  🟡 Core
# --------------------------------------------------------------
# Write an async function `validate_pin(pin)` that awaits
# asyncio.sleep(0.01), then raises ValueError("PIN must be 4 digits")
# if len(str(pin)) != 4, otherwise returns "PIN accepted". Write
# `main_f4()` that tries validate_pin(123) inside a try/except,
# printing the caught error message.
# Expected output:
#   PIN must be 4 digits

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# async def validate_pin(pin):
#     await asyncio.sleep(0.01)
#     if len(str(pin)) != 4:
#         raise ValueError("PIN must be 4 digits")
#     return "PIN accepted"
#
# async def main_f4():
#     try:
#         result = await validate_pin(123)
#         print(result)
#     except ValueError as error:
#         print(error)
#
# asyncio.run(main_f4())

# --------------------------------------------------------------
# Problem F5  🔴 Challenge
# --------------------------------------------------------------
# Write an async function `fetch_review_score(product)` that awaits
# asyncio.sleep(0.01) then returns a hardcoded score from
# {"Phone": 4.5, "Laptop": 4.2, "Tablet": 3.9}. Using
# asyncio.gather(), fetch scores for all three products concurrently,
# then print the name of the product with the HIGHEST score using
# max() with a key function.
# Expected output:
#   Phone

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# async def fetch_review_score(product):
#     await asyncio.sleep(0.01)
#     scores = {"Phone": 4.5, "Laptop": 4.2, "Tablet": 3.9}
#     return product, scores[product]
#
# async def main_f5():
#     products = ["Phone", "Laptop", "Tablet"]
#     results = await asyncio.gather(*(fetch_review_score(p) for p in products))
#     best_product = max(results, key=lambda pair: pair[1])[0]
#     print(best_product)
#
# asyncio.run(main_f5())


# ════════════════════════════════════════════════════════════════
# SECTION G: Mixed Challenges (Threading + Multiprocessing + Asyncio)
# ════════════════════════════════════════════════════════════════

# --------------------------------------------------------------
# Problem G1  🔴 Challenge
# --------------------------------------------------------------
# Combine closures (Day 14) with threading. Write
# `make_thread_safe_logger()` that returns an inner function `log(msg)`
# which appends msg to an internal list while holding an internal
# Lock (both created in the enclosing scope). Also give the closure
# a way to retrieve all logs: have make_thread_safe_logger() return
# a TUPLE (log, get_logs) where get_logs() returns the internal list.
# Spawn 3 threads logging "Event-1", "Event-2", "Event-3", join them,
# then print sorted(get_logs()).
# Expected output:
#   ['Event-1', 'Event-2', 'Event-3']

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def make_thread_safe_logger():
#     logs = []
#     lock = threading.Lock()
#
#     def log(msg):
#         with lock:
#             logs.append(msg)
#
#     def get_logs():
#         return logs
#
#     return log, get_logs
#
# log, get_logs = make_thread_safe_logger()
# log_threads = [
#     threading.Thread(target=log, args=(f"Event-{i}",)) for i in [1, 2, 3]
# ]
# for t in log_threads:
#     t.start()
# for t in log_threads:
#     t.join()
# print(sorted(get_logs()))

# --------------------------------------------------------------
# Problem G2  🟡 Core
# --------------------------------------------------------------
# Write a decorator (Day 14) `async_timer` that wraps an ASYNC
# function: the wrapper is itself `async def`, awaits the wrapped
# coroutine, and after it completes prints "Async task complete"
# before returning the result. Apply it to an async function
# `load_dashboard()` that awaits asyncio.sleep(0.01) and returns
# "Dashboard loaded". Run it with asyncio.run().
# Expected output:
#   Async task complete
#   Dashboard loaded

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# import functools
#
# def async_timer(func):
#     @functools.wraps(func)
#     async def wrapper(*args, **kwargs):
#         result = await func(*args, **kwargs)
#         print("Async task complete")
#         return result
#     return wrapper
#
# @async_timer
# async def load_dashboard():
#     await asyncio.sleep(0.01)
#     return "Dashboard loaded"
#
# print(asyncio.run(load_dashboard()))

# --------------------------------------------------------------
# Problem G3  🔴 Challenge
# --------------------------------------------------------------
# Write a class (Day 10/11) `EventLog` with a @property (Day 14)
# `summary` that returns f"{len(self._events)} event(s) logged", and
# a method `add_event(self, event_lock, event)` that appends `event`
# to self._events while holding event_lock (a threading.Lock passed
# in). Create an EventLog, a shared threading.Lock, spawn 3 threads
# each calling add_event with a different event string
# ("Login", "Purchase", "Logout"), join them, then print
# event_log.summary.
# Expected output:
#   3 event(s) logged

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# class EventLog:
#     def __init__(self):
#         self._events = []
#
#     @property
#     def summary(self):
#         return f"{len(self._events)} event(s) logged"
#
#     def add_event(self, event_lock, event):
#         with event_lock:
#             self._events.append(event)
#
#
# event_log = EventLog()
# shared_lock = threading.Lock()
# event_threads = [
#     threading.Thread(target=event_log.add_event, args=(shared_lock, e))
#     for e in ["Login", "Purchase", "Logout"]
# ]
# for t in event_threads:
#     t.start()
# for t in event_threads:
#     t.join()
# print(event_log.summary)

# --------------------------------------------------------------
# Problem G4  🔴 Challenge
# --------------------------------------------------------------
# Final capstone-style problem for Day 16. Write an async function
# `process_order(order_id, prep_seconds)` that awaits
# asyncio.sleep(prep_seconds) then returns f"Order {order_id} ready
# in {prep_seconds}s". Using asyncio.gather(), concurrently process
# THREE orders: ("A1", 0.03), ("A2", 0.01), ("A3", 0.02). Then, using
# a LIST COMPREHENSION (Day 6) and sorted() with a key= function
# (Day 15 concept, but sorted() itself is built-in since Day 6),
# print the results sorted by prep_seconds ascending (fastest order
# first), extracting prep_seconds by parsing the string is NOT
# required - instead have process_order return a tuple
# (order_id, prep_seconds, message) and sort on index 1.
# Expected output:
#   Order A2 ready in 0.01s
#   Order A3 ready in 0.02s
#   Order A1 ready in 0.03s

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# async def process_order(order_id, prep_seconds):
#     await asyncio.sleep(prep_seconds)
#     return (order_id, prep_seconds, f"Order {order_id} ready in {prep_seconds}s")
#
# async def main_g4():
#     orders = [("A1", 0.03), ("A2", 0.01), ("A3", 0.02)]
#     results = await asyncio.gather(*(process_order(oid, secs) for oid, secs in orders))
#     for order_id, prep_seconds, message in sorted(results, key=lambda r: r[1]):
#         print(message)
#
# asyncio.run(main_g4())


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Sections in this file:
#   F - async/await & asyncio          (5 problems)
#   G - Mixed Challenges               (4 problems)
# Total: 9 problems | 🟢 2  🟡 3  🔴 4
#
# Day 16 practice problem set complete!
# Combined across all 3 files: 26 problems
#   File 1 (Threading):                10 problems
#   File 2 (Multiprocessing):           7 problems
#   File 3 (Async + Mixed):             9 problems
#
# Next up: Day 17 - Advanced OOP
#   - Abstract base classes with ABCMeta, metaclasses, Protocol classes,
#     the @dataclass decorator

if __name__ == "__main__":
    print("\nDay 16, Practice File 3 loaded. Fill in the YOUR CODE HERE sections!")
