"""
Day 19 · Context Managers — Part 1: The `with` Protocol

What this file covers:
    - Why context managers exist (the resource cleanup problem)
    - The `with` statement and what happens "under the hood"
    - The `__enter__` / `__exit__` protocol
    - Writing your own class-based context managers
    - Handling exceptions inside `__exit__`
    - Nesting multiple context managers in one `with` statement

Prerequisites:
    - Day 9  (try/except/finally, custom exceptions)
    - Day 10 (classes, __init__, self)
    - Day 11 (dunder/magic methods)

How to run:
    python day19_01_context_manager_protocol.py
"""

# ════════════════════════════════════════════════════════════════
# SECTION 1 — The Problem: Manual Resource Cleanup
# ════════════════════════════════════════════════════════════════

# ── Why do we need context managers? ──
# Whenever we open a resource (a file, a network connection, a database
# session, a lock), we need to guarantee it gets closed/released again —
# even if something goes wrong in the middle. Doing this manually with
# try/finally works, but it's easy to forget, and it gets repetitive.

print("═" * 50)
print("SECTION 1: The Problem")
print("═" * 50)

# The "manual" way — works, but verbose and easy to get wrong.
report_file = open("mumbai_sales_report.txt", "w")
try:
    report_file.write("Sales report for Mumbai branch\n")
    report_file.write("Priya Sharma — Rs 45,000\n")
finally:
    report_file.close()

print(f"File closed after manual cleanup? {report_file.closed}")
# Output: File closed after manual cleanup? True

# ── The `with` statement solves this automatically ──
with open("mumbai_sales_report.txt", "a") as report_file:
    report_file.write("Arjun Mehta — Rs 38,500\n")

print(f"File closed after 'with' block? {report_file.closed}")
# Output: File closed after 'with' block? True
# Python guarantees close() runs even if an exception happens inside the block.


# ════════════════════════════════════════════════════════════════
# SECTION 2 — What `with` Actually Does
# ════════════════════════════════════════════════════════════════

# ── The protocol ──
# `with EXPR as VAR:` roughly translates to:
#
#     mgr = EXPR
#     VAR = mgr.__enter__()
#     try:
#         ... block body ...
#     finally:
#         mgr.__exit__(exc_type, exc_value, traceback)
#
# Any object that implements BOTH __enter__ and __exit__ is a
# "context manager" and can be used after `with`.

print()
print("═" * 50)
print("SECTION 2: The Protocol")
print("═" * 50)


class Announcer:
    """A minimal context manager that just prints when it enters/exits."""

    def __enter__(self):
        print("Entering the block...")
        return self  # whatever is returned here becomes the 'as' variable

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the block...")
        return False  # False/None means: don't suppress exceptions


with Announcer() as a:
    print(f"Inside the block, got back: {a}")
# Output:
# Entering the block...
# Inside the block, got back: <__main__.Announcer object at ...>
# Exiting the block...


# ════════════════════════════════════════════════════════════════
# SECTION 3 — A Real Class-Based Context Manager
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SECTION 3: A Real Example — Timing a Block")
print("═" * 50)

import time


class Timer:
    """Times how long the code inside the `with` block took to run."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self  # let the caller access .elapsed later

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"Block took {self.elapsed:.6f} seconds")
        return False


with Timer() as timer:
    total = sum(range(1_000_000))

print(f"Sum computed: {total}")
# Output:
# Block took 0.0XXXXX seconds
# Sum computed: 499999500000


# ════════════════════════════════════════════════════════════════
# SECTION 4 — __exit__ and Exception Handling
# ════════════════════════════════════════════════════════════════

# ── The three arguments to __exit__ ──
# If an exception happens inside the `with` block, Python calls
# __exit__(exc_type, exc_value, traceback) with details of that exception.
# If no exception happened, all three are None.
#
# - Returning False (or None, the default) lets the exception propagate.
# - Returning True SUPPRESSES the exception — use this carefully!

print()
print("═" * 50)
print("SECTION 4: Handling Exceptions in __exit__")
print("═" * 50)


class DatabaseSession:
    """
    Simulates a database session for a fictional Bengaluru retail app.
    Commits on success, rolls back automatically if an error occurs.
    """

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def __enter__(self):
        print(f"Opening DB session for {self.customer_name}...")
        self.transaction_open = True
        return self

    def execute(self, statement):
        print(f"  Executing: {statement}")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("No errors — committing transaction.")
        else:
            print(f"Error detected ({exc_type.__name__}: {exc_value}) — rolling back!")
        self.transaction_open = False
        return False  # do not suppress the exception — let caller know it failed


# Case 1: everything succeeds
with DatabaseSession("Riya Deshmukh") as session:
    session.execute("INSERT INTO orders VALUES ('Riya Deshmukh', 2500)")
# Output:
# Opening DB session for Riya Deshmukh...
#   Executing: INSERT INTO orders VALUES ('Riya Deshmukh', 2500)
# No errors — committing transaction.

print()

# Case 2: something goes wrong inside the block
try:
    with DatabaseSession("Sanjay Verma") as session:
        session.execute("INSERT INTO orders VALUES ('Sanjay Verma', -100)")
        raise ValueError("Negative order amount is not allowed")
except ValueError as e:
    print(f"Caught outside the 'with' block: {e}")
# Output:
# Opening DB session for Sanjay Verma...
#   Executing: INSERT INTO orders VALUES ('Sanjay Verma', -100)
# Error detected (ValueError: Negative order amount is not allowed) — rolling back!
# Caught outside the 'with' block: Negative order amount is not allowed


# ════════════════════════════════════════════════════════════════
# SECTION 5 — Suppressing Exceptions on Purpose
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SECTION 5: Deliberately Suppressing Exceptions")
print("═" * 50)


class IgnoreMissingKey:
    """Swallows KeyError inside the block — useful for optional lookups."""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is KeyError:
            print(f"Ignored a missing key: {exc_value}")
            return True  # suppress the KeyError
        return False  # let any other exception propagate normally


meera_profile = {"city": "Chennai", "plan": "Premium"}

with IgnoreMissingKey():
    discount = meera_profile["discount_code"]  # this key does not exist
    print(f"Discount: {discount}")  # never reached

print("Program continues normally after the suppressed KeyError.")
# Output:
# Ignored a missing key: 'discount_code'
# Program continues normally after the suppressed KeyError.


# ════════════════════════════════════════════════════════════════
# SECTION 6 — Multiple Context Managers in One `with`
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SECTION 6: Multiple Context Managers Together")
print("═" * 50)

# You can open several context managers in a single `with` statement,
# separated by commas. They enter left-to-right and exit right-to-left.

with open("mumbai_sales_report.txt", "r") as infile, \
     open("mumbai_sales_report_copy.txt", "w") as outfile:
    contents = infile.read()
    outfile.write(contents)

print("Copied report file using two context managers at once.")
# Output: Copied report file using two context managers at once.


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian Context
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1: A simple "connection" context manager for a Swiggy-style order API
class SwiggyConnection:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name

    def __enter__(self):
        print(f"Connecting to {self.restaurant_name}'s kitchen system...")
        return self

    def place_order(self, item, price):
        print(f"  Order placed: {item} — Rs {price}")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from {self.restaurant_name}'s kitchen system.")
        return False


with SwiggyConnection("Delhi Darbar") as conn:
    conn.place_order("Butter Chicken", 320)
    conn.place_order("Garlic Naan", 60)
# Output:
# Connecting to Delhi Darbar's kitchen system...
#   Order placed: Butter Chicken — Rs 320
#   Order placed: Garlic Naan — Rs 60
# Disconnecting from Delhi Darbar's kitchen system.

print()

# Example 2: A "resource lock" context manager, e.g. for an IRCTC-style
# ticket booking counter that only one customer can use at a time
class BookingCounter:
    is_locked = False

    def __enter__(self):
        if BookingCounter.is_locked:
            raise RuntimeError("Counter is already in use!")
        BookingCounter.is_locked = True
        print("Booking counter locked for this customer.")
        return self

    def book_ticket(self, passenger, train):
        print(f"  Booking ticket for {passenger} on {train}")

    def __exit__(self, exc_type, exc_value, traceback):
        BookingCounter.is_locked = False
        print("Booking counter released.")
        return False


with BookingCounter() as counter:
    counter.book_ticket("Arjun Mehta", "Rajdhani Express")
# Output:
# Booking counter locked for this customer.
#   Booking ticket for Arjun Mehta on Rajdhani Express
# Booking counter released.

print()

# Example 3: A context manager that tracks rupee totals and validates them
class ExpenseTracker:
    def __init__(self, budget):
        self.budget = budget
        self.total = 0

    def __enter__(self):
        print(f"Starting expense tracking with budget Rs {self.budget}")
        return self

    def add_expense(self, label, amount):
        self.total += amount
        print(f"  Added expense: {label} — Rs {amount} (running total: Rs {self.total})")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.total > self.budget:
            print(f"WARNING: Over budget by Rs {self.total - self.budget}!")
        else:
            print(f"Within budget. Rs {self.budget - self.total} remaining.")
        return False


with ExpenseTracker(budget=1000) as tracker:
    tracker.add_expense("Auto rickshaw", 150)
    tracker.add_expense("Lunch (Zomato)", 420)
    tracker.add_expense("Movie ticket", 250)
# Output:
# Starting expense tracking with budget Rs 1000
#   Added expense: Auto rickshaw — Rs 150 (running total: Rs 150)
#   Added expense: Lunch (Zomato) — Rs 570 (running total: Rs 570)
#   Added expense: Movie ticket — Rs 250 (running total: Rs 820)
# Within budget. Rs 180 remaining.


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("MINI-CHALLENGE")
print("═" * 50)

# Write a class-based context manager called `PaytmWallet` that:
#   1. Takes a starting balance in __init__
#   2. On __enter__, prints "Wallet opened. Balance: Rs <balance>" and returns self
#   3. Has a method `debit(amount)` that reduces the balance
#   4. If a debit would make the balance negative, raise a ValueError
#      inside debit() (do NOT check this in __exit__)
#   5. On __exit__, if a ValueError occurred, print
#      "Transaction failed — balance unchanged at Rs <balance>" and
#      SUPPRESS the exception (return True) so the program keeps running
#   6. If no exception occurred, print "Wallet closed. Final balance: Rs <balance>"

# YOUR CODE HERE


# ── Commented Solution ──
# class PaytmWallet:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def __enter__(self):
#         print(f"Wallet opened. Balance: Rs {self.balance}")
#         return self
#
#     def debit(self, amount):
#         if self.balance - amount < 0:
#             raise ValueError("Insufficient balance")
#         self.balance -= amount
#         print(f"  Debited Rs {amount}. New balance: Rs {self.balance}")
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is ValueError:
#             print(f"Transaction failed — balance unchanged at Rs {self.balance}")
#             return True
#         print(f"Wallet closed. Final balance: Rs {self.balance}")
#         return False
#
# with PaytmWallet(balance=500) as wallet:
#     wallet.debit(200)
#     wallet.debit(1000)  # this raises ValueError, gets suppressed
#
# print("Program continues after the wallet block.")
# Expected output:
# Wallet opened. Balance: Rs 500
#   Debited Rs 200. New balance: Rs 300
# Transaction failed — balance unchanged at Rs 300
# Program continues after the wallet block.


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SUMMARY")
print("═" * 50)
print("""
Covered in this file:
  - Why context managers exist: guaranteed cleanup, even on error
  - `with EXPR as VAR:` calls __enter__ then guarantees __exit__ runs
  - __enter__(self) sets up the resource and returns the 'as' value
  - __exit__(self, exc_type, exc_value, traceback) tears down the resource
  - Returning True from __exit__ suppresses the exception; False lets it propagate
  - Multiple context managers can be chained in a single `with` statement

Coming up next (Part 2 of Day 19):
  - The contextlib module
  - The @contextmanager decorator — writing context managers with generators
  - contextlib.suppress, contextlib.ExitStack, and other handy utilities
""")

# ── Cleanup: remove the demo files created in Section 1 & 6 ──
import os
for _file in ("mumbai_sales_report.txt", "mumbai_sales_report_copy.txt"):
    if os.path.exists(_file):
        os.remove(_file)
