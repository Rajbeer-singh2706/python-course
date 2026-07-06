"""
Day 16 - Practice Problems (File 1 of 3)
Topic: The `threading` Module

Cumulative scope: Days 1-16

Difficulty legend:
    🟢 Warm-up   - direct application of one concept
    🟡 Core      - combines a few ideas, slightly more logic
    🔴 Challenge - multi-step reasoning, edge cases

Section Index:
    Section A - Prior Days Review (3 problems)
    Section B - Threads, start()/join() (3 problems)
    Section C - Race Conditions & Locks (4 problems)

How to run:
    python day16_practise_problems_01_threading.py
"""

import threading
import time

# ════════════════════════════════════════════════════════════════
# SECTION A: Prior Days Review
# ════════════════════════════════════════════════════════════════

# --------------------------------------------------------------
# Problem A1  🟢 Warm-up
# --------------------------------------------------------------
# Write a decorator (Day 14) `timed` that prints "Task finished" after
# calling the wrapped function, then returns its result unchanged.
# Apply it to a function `add_numbers(a, b)` returning a + b. Call it
# with (7, 8).
# Expected output:
#   Task finished
#   15

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def timed(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print("Task finished")
#         return result
#     return wrapper
#
# @timed
# def add_numbers(a, b):
#     return a + b
#
# print(add_numbers(7, 8))

# --------------------------------------------------------------
# Problem A2  🟢 Warm-up
# --------------------------------------------------------------
# Write a generator function (Day 13) `countdown(n)` that yields
# values from n down to 1. Print the values produced by
# list(countdown(4)).
# Expected output:
#   [4, 3, 2, 1]

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def countdown(n):
#     while n >= 1:
#         yield n
#         n -= 1
#
# print(list(countdown(4)))

# --------------------------------------------------------------
# Problem A3  🟡 Core
# --------------------------------------------------------------
# Write a class `Stack` (Day 10/11 OOP) with push(self, item),
# pop(self), and a __len__ dunder method returning the number of
# items. Push 10, 20, 30, then print len(stack) and stack.pop().
# Expected output:
#   3
#   30

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def __len__(self):
#         return len(self.items)
#
#
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(len(stack))
# print(stack.pop())


# ════════════════════════════════════════════════════════════════
# SECTION B: Threads, start()/join()
# ════════════════════════════════════════════════════════════════

# --------------------------------------------------------------
# Problem B1  🟢 Warm-up
# --------------------------------------------------------------
# Write a function `print_city(city_name)` that just prints
# f"Visiting {city_name}". Create and start a single thread targeting
# this function with "Jaipur", then join it.
# Expected output:
#   Visiting Jaipur

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def print_city(city_name):
#     print(f"Visiting {city_name}")
#
# city_thread = threading.Thread(target=print_city, args=("Jaipur",))
# city_thread.start()
# city_thread.join()

# --------------------------------------------------------------
# Problem B2  🟡 Core
# --------------------------------------------------------------
# Write a function `fetch_price(product, prices_dict)` that stores
# a fixed price into prices_dict[product] (simulate: Rice=50, Dal=90).
# Create two threads, one per product, using a SHARED dictionary
# passed by reference. Join both, then print
# sorted(prices_dict.items()).
# Expected output:
#   [('Dal', 90), ('Rice', 50)]

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def fetch_price(product, prices_dict):
#     fixed_prices = {"Rice": 50, "Dal": 90}
#     prices_dict[product] = fixed_prices[product]
#
# shared_prices = {}
# t1 = threading.Thread(target=fetch_price, args=("Rice", shared_prices))
# t2 = threading.Thread(target=fetch_price, args=("Dal", shared_prices))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(sorted(shared_prices.items()))

# --------------------------------------------------------------
# Problem B3  🟡 Core
# --------------------------------------------------------------
# Write a function `is_alive_check()` that creates a thread running
# time.sleep(0.05), checks and returns a tuple of
# (is_alive_before_join, is_alive_after_join) - True/False for whether
# the thread .is_alive() before and after calling .join(). Print the
# returned tuple.
# Expected output:
#   (True, False)

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def is_alive_check():
#     def sleep_task():
#         time.sleep(0.05)
#
#     t = threading.Thread(target=sleep_task)
#     t.start()
#     before = t.is_alive()
#     t.join()
#     after = t.is_alive()
#     return (before, after)
#
# print(is_alive_check())


# ════════════════════════════════════════════════════════════════
# SECTION C: Race Conditions & Locks
# ════════════════════════════════════════════════════════════════

# --------------------------------------------------------------
# Problem C1  🟡 Core
# --------------------------------------------------------------
# Using threading.Lock, write a function `safe_append(shared_list,
# value, lock)` that appends `value` to `shared_list` while holding
# `lock`. Spawn 4 threads appending 1, 2, 3, 4 respectively to a
# shared list, join them, then print sorted(shared_list).
# Expected output:
#   [1, 2, 3, 4]

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# def safe_append(shared_list, value, lock):
#     with lock:
#         shared_list.append(value)
#
# append_lock = threading.Lock()
# shared_data = []
# append_threads = [
#     threading.Thread(target=safe_append, args=(shared_data, v, append_lock))
#     for v in [1, 2, 3, 4]
# ]
# for t in append_threads:
#     t.start()
# for t in append_threads:
#     t.join()
# print(sorted(shared_data))

# --------------------------------------------------------------
# Problem C2  🟡 Core
# --------------------------------------------------------------
# Demonstrate a race condition on a shared "stock" variable. Write
# `sell_unsafe(times)` that, `times` times, reads a global
# `stock_unsafe`, sleeps 0 seconds (time.sleep(0)) to force a yield,
# then decrements it by 1 and writes it back. Start with
# stock_unsafe = 2000. Run 4 threads each calling sell_unsafe(500),
# join them, then print whether the final stock_unsafe EQUALS 0
# (print True or False). Because of the race, this should print
# False (the lost updates mean it does NOT reach exactly 0).
# Expected output:
#   False

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# stock_unsafe = 2000
#
# def sell_unsafe(times):
#     global stock_unsafe
#     for _ in range(times):
#         current = stock_unsafe
#         time.sleep(0)
#         stock_unsafe = current - 1
#
# sell_threads = [threading.Thread(target=sell_unsafe, args=(500,)) for _ in range(4)]
# for t in sell_threads:
#     t.start()
# for t in sell_threads:
#     t.join()
# print(stock_unsafe == 0)

# --------------------------------------------------------------
# Problem C3  🟡 Core
# --------------------------------------------------------------
# Fix Problem C2 using a threading.Lock so the final stock reaches
# EXACTLY 0. Start with stock_safe = 2000, use the same pattern
# (read, sleep(0), write) but wrap it in `with lock:`. Run 4 threads
# each calling sell_safe(500), join, then print stock_safe.
# Expected output:
#   0

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# stock_safe = 2000
# stock_lock = threading.Lock()
#
# def sell_safe(times):
#     global stock_safe
#     for _ in range(times):
#         with stock_lock:
#             current = stock_safe
#             time.sleep(0)
#             stock_safe = current - 1
#
# safe_sell_threads = [threading.Thread(target=sell_safe, args=(500,)) for _ in range(4)]
# for t in safe_sell_threads:
#     t.start()
# for t in safe_sell_threads:
#     t.join()
# print(stock_safe)

# --------------------------------------------------------------
# Problem C4  🔴 Challenge
# --------------------------------------------------------------
# Write a class `TicketCounter` with __init__(self, available_tickets)
# storing it and creating a self.lock = threading.Lock(). Add a
# method book(self, passenger_name) that, while holding self.lock,
# checks if self.available_tickets > 0; if so decrements it and
# returns f"{passenger_name}: CONFIRMED", else returns
# f"{passenger_name}: WAITLISTED". Create a TicketCounter with 2
# tickets, spawn 4 threads for passengers "P1", "P2", "P3", "P4" that
# each call counter.book() and store results in a shared list (also
# protected by the same lock), join all threads, then print how many
# results contain "CONFIRMED" and how many contain "WAITLISTED".
# Expected output:
#   Confirmed: 2, Waitlisted: 2

# YOUR CODE HERE


print("-" * 50)

# SOLUTION:
# class TicketCounter:
#     def __init__(self, available_tickets):
#         self.available_tickets = available_tickets
#         self.lock = threading.Lock()
#
#     def book(self, passenger_name):
#         with self.lock:
#             if self.available_tickets > 0:
#                 self.available_tickets -= 1
#                 return f"{passenger_name}: CONFIRMED"
#             return f"{passenger_name}: WAITLISTED"
#
#
# booking_results = []
# results_lock = threading.Lock()
# counter = TicketCounter(2)
#
# def book_and_record(passenger_name):
#     outcome = counter.book(passenger_name)
#     with results_lock:
#         booking_results.append(outcome)
#
# passenger_threads = [
#     threading.Thread(target=book_and_record, args=(name,))
#     for name in ["P1", "P2", "P3", "P4"]
# ]
# for t in passenger_threads:
#     t.start()
# for t in passenger_threads:
#     t.join()
#
# confirmed = sum(1 for r in booking_results if "CONFIRMED" in r)
# waitlisted = sum(1 for r in booking_results if "WAITLISTED" in r)
# print(f"Confirmed: {confirmed}, Waitlisted: {waitlisted}")


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Sections in this file:
#   A - Prior Days Review              (3 problems)
#   B - Threads, start()/join()        (3 problems)
#   C - Race Conditions & Locks        (4 problems)
# Total: 10 problems | 🟢 3  🟡 6  🔴 1
#
# Next file: day16_practise_problems_02_multiprocessing.py
#   - multiprocessing.Process, Queue, and ProcessPoolExecutor

if __name__ == "__main__":
    print("\nDay 16, Practice File 1 loaded. Fill in the YOUR CODE HERE sections!")
