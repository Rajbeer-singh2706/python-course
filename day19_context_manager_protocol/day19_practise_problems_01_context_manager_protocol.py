"""
Day 19 · Practice Problems — Part 1: Prior Days Review + Context Manager Protocol

Cumulative scope: This problem set reviews concepts from Days 1-18 and tests
Day 19's class-based context manager protocol (__enter__ / __exit__).

Difficulty legend:
    🟢 Warm-up   — quick recall / direct application
    🟡 Core      — combines a few ideas, needs some thought
    🔴 Challenge — multi-step, closer to a real-world mini-project

Section index (this file):
    Section A — Prior Days Review           (3 problems)
    Section B — with Statement Basics       (5 problems)
    Section C — Class-Based Context Managers (5 problems)

(Section D, E and Mixed Challenges continue in
 day19_practise_problems_02_contextlib.py)

How to run:
    python day19_practise_problems_01_context_manager_protocol.py
"""

import os

# ════════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════════════

print("═" * 50)
print("SECTION A: Prior Days Review")
print("═" * 50)

# ── Problem A1 🟢 ──
# (Day 17/18 review) Create a @dataclass called `Student` with fields
# `name: str` and `marks: list[int]`, then write a type-hinted function
# `average(marks: list[int]) -> float` that returns the average of the marks.
# Test it with Priya Sharma's marks: [88, 92, 79, 95]

# YOUR CODE HERE


# SOLUTION:
# from dataclasses import dataclass
#
# @dataclass
# class Student:
#     name: str
#     marks: list[int]
#
# def average(marks: list[int]) -> float:
#     return sum(marks) / len(marks)
#
# priya = Student(name="Priya Sharma", marks=[88, 92, 79, 95])
# print(f"{priya.name}'s average: {average(priya.marks):.2f}")
# Expected output: Priya Sharma's average: 88.50

print("-" * 50)

# ── Problem A2 🟢 ──
# (Day 13 review) Write a generator function `even_numbers(limit)` that
# yields even numbers from 0 up to (but not including) `limit`.
# Print the first 5 even numbers below 20.

# YOUR CODE HERE


# SOLUTION:
# def even_numbers(limit):
#     for n in range(0, limit, 2):
#         yield n
#
# result = list(even_numbers(20))[:5]
# print(f"First 5 even numbers below 20: {result}")
# Expected output: First 5 even numbers below 20: [0, 2, 4, 6, 8]

print("-" * 50)

# ── Problem A3 🟡 ──
# (Day 9 + Day 11 review) Create a custom exception `InsufficientStockError`
# that inherits from Exception. Write a function `purchase(item, stock, qty)`
# that raises this exception (with a message including item name) if
# qty > stock, otherwise returns the remaining stock. Test with
# item="Rice bag", stock=5, qty=8 — catch and print the error message.

# YOUR CODE HERE


# SOLUTION:
# class InsufficientStockError(Exception):
#     pass
#
# def purchase(item, stock, qty):
#     if qty > stock:
#         raise InsufficientStockError(f"Not enough stock for {item}: requested {qty}, have {stock}")
#     return stock - qty
#
# try:
#     purchase("Rice bag", stock=5, qty=8)
# except InsufficientStockError as e:
#     print(f"Error: {e}")
# Expected output: Error: Not enough stock for Rice bag: requested 8, have 5

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION B — with Statement Basics
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SECTION B: with Statement Basics")
print("═" * 50)

# ── Problem B1 🟢 ──
# Use `with open(...)` to write the single line "Meera Iyer joined Pune branch"
# to a file called "b1_temp.txt", then re-open it with `with` to read and
# print its contents.

# YOUR CODE HERE


# SOLUTION:
# with open("b1_temp.txt", "w") as f:
#     f.write("Meera Iyer joined Pune branch")
#
# with open("b1_temp.txt", "r") as f:
#     print(f.read())
# os.remove("b1_temp.txt")
# Expected output: Meera Iyer joined Pune branch

print("-" * 50)

# ── Problem B2 🟢 ──
# Demonstrate what happens to a file handle if an exception occurs inside
# a `with` block: open "b2_temp.txt" for writing inside a `with`, raise a
# ValueError inside the block, catch it outside, and confirm f.closed is True.

# YOUR CODE HERE


# SOLUTION:
# f_ref = None
# try:
#     with open("b2_temp.txt", "w") as f:
#         f_ref = f
#         raise ValueError("Simulated failure")
# except ValueError as e:
#     print(f"Caught: {e}")
# print(f"File closed even though an error occurred? {f_ref.closed}")
# os.remove("b2_temp.txt")
# Expected output:
# Caught: Simulated failure
# File closed even though an error occurred? True

print("-" * 50)

# ── Problem B3 🟡 ──
# Open two files at once in a single `with` statement: "b3_a.txt" (write
# "Delhi") and "b3_b.txt" (write "Mumbai"). Then reopen both to read and
# print "City 1: <a>, City 2: <b>".

# YOUR CODE HERE


# SOLUTION:
# with open("b3_a.txt", "w") as fa, open("b3_b.txt", "w") as fb:
#     fa.write("Delhi")
#     fb.write("Mumbai")
#
# with open("b3_a.txt") as fa, open("b3_b.txt") as fb:
#     print(f"City 1: {fa.read()}, City 2: {fb.read()}")
#
# os.remove("b3_a.txt")
# os.remove("b3_b.txt")
# Expected output: City 1: Delhi, City 2: Mumbai

print("-" * 50)

# ── Problem B4 🟡 ──
# Loop over 3 filenames ["b4_1.txt", "b4_2.txt", "b4_3.txt"]. For each,
# write "Branch report" to it inside its own `with` block, then read all
# 3 back and print how many files were successfully read.

# YOUR CODE HERE


# SOLUTION:
# filenames = ["b4_1.txt", "b4_2.txt", "b4_3.txt"]
# for name in filenames:
#     with open(name, "w") as f:
#         f.write("Branch report")
#
# read_count = 0
# for name in filenames:
#     with open(name) as f:
#         f.read()
#         read_count += 1
#
# print(f"Files successfully read: {read_count}")
# for name in filenames:
#     os.remove(name)
# Expected output: Files successfully read: 3

print("-" * 50)

# ── Problem B5 🔴 ──
# Try to open a file that doesn't exist ("b5_missing.txt") inside a `with`
# statement, wrapped in try/except FileNotFoundError. Print an appropriate
# message, then print "Continuing after handled error." to show the
# program continues normally.

# YOUR CODE HERE


# SOLUTION:
# try:
#     with open("b5_missing.txt") as f:
#         f.read()
# except FileNotFoundError:
#     print("File not found — skipping this report.")
# print("Continuing after handled error.")
# Expected output:
# File not found — skipping this report.
# Continuing after handled error.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION C — Class-Based Context Managers
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SECTION C: Class-Based Context Managers")
print("═" * 50)

# ── Problem C1 🟢 ──
# Write a class `Greeting` with __enter__ that prints "Namaste!" and
# returns self, and __exit__ that prints "Alvida!" and returns False.
# Use it in a `with` block.

# YOUR CODE HERE


# SOLUTION:
# class Greeting:
#     def __enter__(self):
#         print("Namaste!")
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Alvida!")
#         return False
#
# with Greeting():
#     print("(inside the block)")
# Expected output:
# Namaste!
# (inside the block)
# Alvida!

print("-" * 50)

# ── Problem C2 🟡 ──
# Write a class `StopwatchLap` that records elapsed time (using
# time.perf_counter) for a single lap. __enter__ starts the clock and
# returns self; __exit__ computes self.lap_time and prints it rounded to
# 4 decimal places. Use it to time a loop that sums range(500_000).

# YOUR CODE HERE


# SOLUTION:
# import time
# class StopwatchLap:
#     def __enter__(self):
#         self.start = time.perf_counter()
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.lap_time = time.perf_counter() - self.start
#         print(f"Lap time: {self.lap_time:.4f}s")
#         return False
#
# with StopwatchLap():
#     total = sum(range(500_000))
# Expected output (timing will vary): Lap time: 0.00XXs

print("-" * 50)

# ── Problem C3 🟡 ──
# Write a class `InventoryLock` for a Flipkart-style warehouse item. On
# __enter__, print "Locking item: <name>" and return self. Add a method
# `reduce_stock(qty)` that raises ValueError if qty is negative. On
# __exit__, if a ValueError occurred, print "Stock update failed for
# <name>" and suppress it (return True); otherwise print "Stock updated
# successfully for <name>". Test with name="Wireless Mouse", trying to
# reduce stock by -3.

# YOUR CODE HERE


# SOLUTION:
# class InventoryLock:
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print(f"Locking item: {self.name}")
#         return self
#     def reduce_stock(self, qty):
#         if qty < 0:
#             raise ValueError("Quantity cannot be negative")
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is ValueError:
#             print(f"Stock update failed for {self.name}")
#             return True
#         print(f"Stock updated successfully for {self.name}")
#         return False
#
# with InventoryLock("Wireless Mouse") as item:
#     item.reduce_stock(-3)
# Expected output:
# Locking item: Wireless Mouse
# Stock update failed for Wireless Mouse

print("-" * 50)

# ── Problem C4 🔴 ──
# Write a class `MultiCitySession` that accepts a list of city names in
# __init__. __enter__ prints "Starting session for: <city1, city2, ...>"
# and returns the list. __exit__ prints "Ending session <status>. Cities
# visited: <count>" where status depends on whether an error occurred
# (always return False — do not suppress). Test with cities=["Mumbai",
# "Pune", "Nagpur"], raising and catching a RuntimeError inside the block.

# YOUR CODE HERE


# SOLUTION:
# class MultiCitySession:
#     def __init__(self, cities):
#         self.cities = cities
#     def __enter__(self):
#         print(f"Starting session for: {', '.join(self.cities)}")
#         return self.cities
#     def __exit__(self, exc_type, exc_value, traceback):
#         status = "with an error" if exc_type else "successfully"
#         print(f"Ending session {status}. Cities visited: {len(self.cities)}")
#         return False
#
# try:
#     with MultiCitySession(["Mumbai", "Pune", "Nagpur"]) as cities:
#         raise RuntimeError("Connectivity issue")
# except RuntimeError as e:
#     print(f"Caught outside: {e}")
# Expected output:
# Starting session for: Mumbai, Pune, Nagpur
# Ending session with an error. Cities visited: 3
# Caught outside: Connectivity issue

print("-" * 50)

# ── Problem C5 🔴 ──
# Write a class `ReusableConnection` that can only be used by ONE `with`
# block at a time using a class-level flag `in_use`. __enter__ should
# raise RuntimeError("Connection already in use!") if `in_use` is True,
# otherwise set it True and print "Connection opened." __exit__ should
# always set `in_use` back to False and print "Connection closed."
# Demonstrate: open it once successfully, then (still inside that block)
# manually call __enter__ on a second instance to show the RuntimeError,
# and catch it.

# YOUR CODE HERE


# SOLUTION:
# class ReusableConnection:
#     in_use = False
#     def __enter__(self):
#         if ReusableConnection.in_use:
#             raise RuntimeError("Connection already in use!")
#         ReusableConnection.in_use = True
#         print("Connection opened.")
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         ReusableConnection.in_use = False
#         print("Connection closed.")
#         return False
#
# with ReusableConnection() as conn:
#     second = ReusableConnection()
#     try:
#         second.__enter__()
#     except RuntimeError as e:
#         print(f"Second attempt failed: {e}")
# Expected output:
# Connection opened.
# Second attempt failed: Connection already in use!
# Connection closed.

print("-" * 50)

print()
print("═" * 50)
print("END OF FILE 1 — continue with")
print("day19_practise_problems_02_contextlib.py")
print("═" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Sections in this file:
#   A. Prior Days Review            — 3 problems (dataclasses, generators, custom exceptions)
#   B. with Statement Basics        — 5 problems (single/multiple files, error safety)
#   C. Class-Based Context Managers — 5 problems (__enter__/__exit__, suppression, locking)
#
# Difficulty breakdown: 5 🟢 Warm-up, 5 🟡 Core, 3 🔴 Challenge (13 problems)
#
# Next file (day19_practise_problems_02_contextlib.py) covers:
#   D. @contextmanager Decorator
#   E. contextlib Utilities (suppress, ExitStack, redirect_stdout, nullcontext)
#   Mixed Challenges — combining Day 19 with all prior days
