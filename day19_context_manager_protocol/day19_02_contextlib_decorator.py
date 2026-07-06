"""
Day 19 · Context Managers — Part 2: `contextlib` & the `@contextmanager` Decorator

What this file covers:
    - Writing context managers with generator functions using
      `@contextlib.contextmanager` (no classes needed)
    - `contextlib.suppress()` — a shortcut for ignoring specific exceptions
    - `contextlib.ExitStack()` — managing a dynamic number of context managers
    - `contextlib.redirect_stdout()` — redirecting printed output
    - `contextlib.nullcontext()` — a "do nothing" context manager

Prerequisites:
    - Day 13 (generators, `yield`)
    - Day 14 (decorators)
    - day19_01_context_manager_protocol.py (the with protocol, __enter__/__exit__)

How to run:
    python day19_02_contextlib_decorator.py
"""

import contextlib

# ════════════════════════════════════════════════════════════════
# SECTION 1 — @contextmanager: Generator-Based Context Managers
# ════════════════════════════════════════════════════════════════

# ── Why use a decorator instead of a class? ──
# Writing a whole class with __init__/__enter__/__exit__ is a lot of
# boilerplate for something simple. `@contextlib.contextmanager` lets you
# write a context manager as a single generator function:
#
#   - Code BEFORE `yield`  → runs on __enter__
#   - The yielded value    → becomes the 'as' variable
#   - Code AFTER `yield`   → runs on __exit__ (wrap in try/finally for safety)

print("═" * 50)
print("SECTION 1: @contextmanager Basics")
print("═" * 50)


@contextlib.contextmanager
def announcer():
    print("Entering the block...")
    yield "hello from inside"
    print("Exiting the block...")


with announcer() as message:
    print(f"Received: {message}")
# Output:
# Entering the block...
# Received: hello from inside
# Exiting the block...


# ════════════════════════════════════════════════════════════════
# SECTION 2 — Handling Exceptions with try/finally
# ════════════════════════════════════════════════════════════════

# ── Always wrap cleanup in try/finally ──
# If the code inside the `with` block raises an exception, it is raised
# right at the `yield` statement inside your generator. Wrap it in
# try/finally to guarantee cleanup still happens.

print()
print("═" * 50)
print("SECTION 2: Exceptions with @contextmanager")
print("═" * 50)


@contextlib.contextmanager
def db_session(customer_name):
    print(f"Opening DB session for {customer_name}...")
    try:
        yield {"customer": customer_name, "committed": False}
    except Exception as e:
        print(f"Error detected ({type(e).__name__}: {e}) — rolling back!")
        raise  # re-raise so the caller still sees the error
    else:
        print("No errors — committing transaction.")
    finally:
        print("Session closed.")


try:
    with db_session("Meera Iyer") as session:
        raise ValueError("Card declined")
except ValueError as e:
    print(f"Caught outside the block: {e}")
# Output:
# Opening DB session for Meera Iyer...
# Error detected (ValueError: Card declined) — rolling back!
# Session closed.
# Caught outside the block: Card declined


# ════════════════════════════════════════════════════════════════
# SECTION 3 — contextlib.suppress()
# ════════════════════════════════════════════════════════════════

# ── A clean shortcut for "ignore this specific exception" ──
# Instead of writing try/except/pass, contextlib.suppress(*exceptions)
# does it as a context manager — much more readable.

print()
print("═" * 50)
print("SECTION 3: contextlib.suppress()")
print("═" * 50)

user_settings = {"theme": "dark", "language": "en"}

# The old way:
try:
    notification_pref = user_settings["notifications"]
except KeyError:
    notification_pref = None

# The contextlib way — cleaner when you just want to ignore the error:
notification_pref = None
with contextlib.suppress(KeyError):
    notification_pref = user_settings["notifications"]

print(f"Notification preference: {notification_pref}")
# Output: Notification preference: None

with contextlib.suppress(FileNotFoundError):
    with open("nonexistent_bigbasket_invoice.txt") as f:
        f.read()

print("Program kept running even though the file did not exist.")
# Output: Program kept running even though the file did not exist.


# ════════════════════════════════════════════════════════════════
# SECTION 4 — contextlib.ExitStack()
# ════════════════════════════════════════════════════════════════

# ── Managing a variable/dynamic number of context managers ──
# Sometimes you don't know in advance how many resources you'll need
# to open (e.g. a list of files). ExitStack lets you push context
# managers onto a stack, and they all get closed automatically —
# in reverse order — when the `with` block ends.

print()
print("═" * 50)
print("SECTION 4: contextlib.ExitStack()")
print("═" * 50)

branch_files = ["pune_branch.txt", "chennai_branch.txt", "delhi_branch.txt"]

# Create the demo files first
for name in branch_files:
    with open(name, "w") as f:
        f.write(f"Sales data for {name.split('_')[0].title()} branch\n")

with contextlib.ExitStack() as stack:
    opened_files = [stack.enter_context(open(name)) for name in branch_files]
    for f in opened_files:
        print(f"  Read: {f.read().strip()}")
print("All branch files closed automatically via ExitStack.")
# Output:
#   Read: Sales data for Pune branch
#   Read: Sales data for Chennai branch
#   Read: Sales data for Delhi branch
# All branch files closed automatically via ExitStack.

# cleanup demo files
import os
for name in branch_files:
    os.remove(name)


# ════════════════════════════════════════════════════════════════
# SECTION 5 — contextlib.redirect_stdout()
# ════════════════════════════════════════════════════════════════

# ── Capturing printed output ──
# Handy for testing, or for capturing output from a function that
# only knows how to print() (e.g. a legacy report generator).

print()
print("═" * 50)
print("SECTION 5: contextlib.redirect_stdout()")
print("═" * 50)

import io


def generate_invoice_report():
    print("Invoice #4521 — Arjun Mehta — Rs 2,150")
    print("Invoice #4522 — Riya Deshmukh — Rs 980")


captured_output = io.StringIO()
with contextlib.redirect_stdout(captured_output):
    generate_invoice_report()

report_text = captured_output.getvalue()
print(f"Captured {len(report_text.splitlines())} lines of report output.")
print("First line captured:", report_text.splitlines()[0])
# Output:
# Captured 2 lines of report output.
# First line captured: Invoice #4521 — Arjun Mehta — Rs 2,150


# ════════════════════════════════════════════════════════════════
# SECTION 6 — contextlib.nullcontext()
# ════════════════════════════════════════════════════════════════

# ── A "do nothing" context manager ──
# Useful when a context manager is optional — you can pick between
# a real one and nullcontext() without branching your `with` code.

print()
print("═" * 50)
print("SECTION 6: contextlib.nullcontext()")
print("═" * 50)


def process_order(order_id, verbose_logging=False):
    log_context = open("order_log.txt", "w") if verbose_logging else contextlib.nullcontext()
    with log_context as log_file:
        if log_file:
            log_file.write(f"Processing order {order_id}\n")
        print(f"Order {order_id} processed (verbose_logging={verbose_logging})")


process_order(101, verbose_logging=False)
process_order(102, verbose_logging=True)
# Output:
# Order 101 processed (verbose_logging=False)
# Order 102 processed (verbose_logging=True)

if os.path.exists("order_log.txt"):
    os.remove("order_log.txt")


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian Context
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1: A generator-based context manager for an IRCTC seat lock
@contextlib.contextmanager
def seat_lock(train_name, seat_number):
    print(f"Locking seat {seat_number} on {train_name}...")
    try:
        yield f"{train_name}-{seat_number}"
    finally:
        print(f"Releasing lock on seat {seat_number} on {train_name}.")


with seat_lock("Shatabdi Express", "B4-22") as seat_id:
    print(f"  Confirming booking for seat: {seat_id}")
# Output:
# Locking seat B4-22 on Shatabdi Express...
#   Confirming booking for seat: Shatabdi Express-B4-22
# Releasing lock on seat B4-22 on Shatabdi Express.

print()

# Example 2: Suppressing a specific error while parsing Razorpay-style webhook data
webhook_payloads = [
    {"amount": 500, "status": "paid"},
    {"status": "failed"},  # missing "amount" key
    {"amount": 1200, "status": "paid"},
]

total_collected = 0
for payload in webhook_payloads:
    with contextlib.suppress(KeyError):
        total_collected += payload["amount"]

print(f"Total collected (skipping malformed payloads): Rs {total_collected}")
# Output: Total collected (skipping malformed payloads): Rs 1700

print()

# Example 3: ExitStack to open a dynamic number of category files for BigBasket
categories = ["fruits", "dairy", "snacks"]
for cat in categories:
    with open(f"bigbasket_{cat}.txt", "w") as f:
        f.write(f"Category: {cat.title()}\n")

with contextlib.ExitStack() as stack:
    handles = {cat: stack.enter_context(open(f"bigbasket_{cat}.txt")) for cat in categories}
    for cat, handle in handles.items():
        print(f"  {cat}: {handle.read().strip()}")
print("All BigBasket category files closed.")
# Output:
#   fruits: Category: Fruits
#   dairy: Category: Dairy
#   snacks: Category: Snacks
# All BigBasket category files closed.

for cat in categories:
    os.remove(f"bigbasket_{cat}.txt")


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("MINI-CHALLENGE")
print("═" * 50)

# Using @contextlib.contextmanager, write a generator-based context
# manager called `zomato_order(restaurant_name)` that:
#   1. Prints "Order started at <restaurant_name>" before the yield
#   2. Yields a list (this will be the 'as' variable, used to collect items)
#   3. After the block finishes (in a finally), prints
#      "Order finalized: <comma-separated items> — <count> item(s)"
#      using the list that was yielded and filled in by the caller

# YOUR CODE HERE


# ── Commented Solution ──
# @contextlib.contextmanager
# def zomato_order(restaurant_name):
#     print(f"Order started at {restaurant_name}")
#     items = []
#     try:
#         yield items
#     finally:
#         print(f"Order finalized: {', '.join(items)} — {len(items)} item(s)")
#
# with zomato_order("Punjabi Tadka") as order_items:
#     order_items.append("Dal Makhani")
#     order_items.append("Jeera Rice")
#
# Expected output:
# Order started at Punjabi Tadka
# Order finalized: Dal Makhani, Jeera Rice — 2 item(s)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SUMMARY")
print("═" * 50)
print("""
Covered in this file:
  - @contextlib.contextmanager turns a generator function into a context manager
    (code before yield = __enter__, code after yield = __exit__)
  - Wrap the yield in try/finally to guarantee cleanup runs even on error
  - contextlib.suppress(*exceptions) — a clean one-liner to ignore specific errors
  - contextlib.ExitStack() — manage a dynamic/unknown number of context managers
  - contextlib.redirect_stdout() — capture printed output into a stream
  - contextlib.nullcontext() — a placeholder "do nothing" context manager

Coming up next (Day 20):
  - Testing with unittest and pytest
  - Fixtures, mocking, and coverage reports
""")
