"""
Day 19 · Practice Problems — Part 2: @contextmanager Decorator, contextlib
Utilities & Mixed Challenges

Cumulative scope: builds on Part 1 (with statement + class-based context
managers) and adds generator-based context managers + contextlib helpers,
then combines everything with concepts from Days 1-18.

Difficulty legend:
    🟢 Warm-up   — quick recall / direct application
    🟡 Core      — combines a few ideas, needs some thought
    🔴 Challenge — multi-step, closer to a real-world mini-project

Section index (this file):
    Section D — @contextmanager Decorator     (4 problems)
    Section E — contextlib Utilities          (4 problems)
    Section F — Mixed Challenges              (3 problems)

How to run:
    python day19_practise_problems_02_contextlib.py
"""

import contextlib
import os

# ════════════════════════════════════════════════════════════════
# SECTION D — @contextmanager Decorator
# ════════════════════════════════════════════════════════════════

print("═" * 50)
print("SECTION D: @contextmanager Decorator")
print("═" * 50)

# ── Problem D1 🟢 ──
# Write a generator-based context manager `namaste()` using
# @contextlib.contextmanager that prints "Namaste!" before yielding
# nothing useful (just yield None), and prints "Alvida!" after.
# (This should behave identically to Problem C1 from file 1.)

# YOUR CODE HERE


# SOLUTION:
# @contextlib.contextmanager
# def namaste():
#     print("Namaste!")
#     yield
#     print("Alvida!")
#
# with namaste():
#     print("(inside the block)")
# Expected output:
# Namaste!
# (inside the block)
# Alvida!

print("-" * 50)

# ── Problem D2 🟡 ──
# Write `pune_branch_counter()` — a generator-based context manager that
# yields a dict {"count": 0}. Inside the `with` block, the caller
# increments count. After the block (in a finally), print
# "Final visitor count for Pune branch: <count>".

# YOUR CODE HERE


# SOLUTION:
# @contextlib.contextmanager
# def pune_branch_counter():
#     data = {"count": 0}
#     try:
#         yield data
#     finally:
#         print(f"Final visitor count for Pune branch: {data['count']}")
#
# with pune_branch_counter() as counter:
#     counter["count"] += 1
#     counter["count"] += 1
#     counter["count"] += 1
# Expected output: Final visitor count for Pune branch: 3

print("-" * 50)

# ── Problem D3 🟡 ──
# Write `safe_division(numerator, denominator)` as a generator-based
# context manager. It should yield the division result if the denominator
# is not zero. If ZeroDivisionError occurs (i.e. denominator is 0), catch
# it inside the generator, print "Cannot divide by zero — returning None
# instead", and yield None instead of raising. Hint: you need to compute
# the result BEFORE the yield, inside a try/except.

# YOUR CODE HERE


# SOLUTION:
# @contextlib.contextmanager
# def safe_division(numerator, denominator):
#     try:
#         result = numerator / denominator
#     except ZeroDivisionError:
#         print("Cannot divide by zero — returning None instead")
#         result = None
#     yield result
#
# with safe_division(100, 0) as result:
#     print(f"Result: {result}")
# with safe_division(100, 5) as result:
#     print(f"Result: {result}")
# Expected output:
# Cannot divide by zero — returning None instead
# Result: None
# Result: 20.0

print("-" * 50)

# ── Problem D4 🔴 ──
# Write `rollback_on_error(label)` as a generator-based context manager
# that maintains a module-level list `applied_changes`. Before yield,
# append f"{label}: started" to applied_changes. Wrap the yield in
# try/except Exception — if an exception occurs, append
# f"{label}: rolled back" and re-raise; in the else clause (no exception),
# append f"{label}: committed". Test it twice: once where the block
# succeeds, once where it raises a ValueError (catch it outside).
# Print `applied_changes` at the end.

# YOUR CODE HERE


# SOLUTION:
# applied_changes = []
#
# @contextlib.contextmanager
# def rollback_on_error(label):
#     applied_changes.append(f"{label}: started")
#     try:
#         yield
#     except Exception:
#         applied_changes.append(f"{label}: rolled back")
#         raise
#     else:
#         applied_changes.append(f"{label}: committed")
#
# with rollback_on_error("add_address"):
#     pass  # succeeds
#
# try:
#     with rollback_on_error("update_payment"):
#         raise ValueError("Card expired")
# except ValueError:
#     pass
#
# print(applied_changes)
# Expected output:
# ['add_address: started', 'add_address: committed', 'update_payment: started', 'update_payment: rolled back']

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION E — contextlib Utilities
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SECTION E: contextlib Utilities")
print("═" * 50)

# ── Problem E1 🟢 ──
# Given a dict `user = {"name": "Sanjay Verma"}`, use contextlib.suppress
# to safely try reading user["email"] into a variable `email`, defaulting
# to None beforehand. Print the final value of `email`.

# YOUR CODE HERE


# SOLUTION:
# user = {"name": "Sanjay Verma"}
# email = None
# with contextlib.suppress(KeyError):
#     email = user["email"]
# print(f"Email: {email}")
# Expected output: Email: None

print("-" * 50)

# ── Problem E2 🟡 ──
# You have a list of 4 filenames to create and read:
# ["e2_a.txt", "e2_b.txt", "e2_c.txt", "e2_d.txt"]. First write "data" to
# each. Then use contextlib.ExitStack() to open ALL of them at once for
# reading, and print the total number of files opened via
# `len(stack_list)` (build the list using stack.enter_context in a loop
# or list comprehension). Clean up (remove) the files afterward.

# YOUR CODE HERE


# SOLUTION:
# names = ["e2_a.txt", "e2_b.txt", "e2_c.txt", "e2_d.txt"]
# for name in names:
#     with open(name, "w") as f:
#         f.write("data")
#
# with contextlib.ExitStack() as stack:
#     handles = [stack.enter_context(open(name)) for name in names]
#     print(f"Total files opened: {len(handles)}")
#
# for name in names:
#     os.remove(name)
# Expected output: Total files opened: 4

print("-" * 50)

# ── Problem E3 🟡 ──
# Write a function `noisy_report()` that prints 3 lines about a fictional
# Ola cab ride summary. Use contextlib.redirect_stdout with an io.StringIO
# to capture its output instead of printing it to the terminal. Then
# print only the number of captured lines and the last captured line.

# YOUR CODE HERE


# SOLUTION:
# import io
#
# def noisy_report():
#     print("Ola ride #7788 summary")
#     print("Driver: Ramesh Kumar")
#     print("Fare: Rs 245")
#
# buffer = io.StringIO()
# with contextlib.redirect_stdout(buffer):
#     noisy_report()
#
# lines = buffer.getvalue().splitlines()
# print(f"Captured {len(lines)} lines")
# print(f"Last line: {lines[-1]}")
# Expected output:
# Captured 3 lines
# Last line: Fare: Rs 245

print("-" * 50)

# ── Problem E4 🔴 ──
# Write a function `send_notification(user_name, use_logging=False)` that
# picks between `open("e4_log.txt", "a")` and `contextlib.nullcontext()`
# depending on `use_logging`. Inside the `with` block, if the log file
# context is real (not None), write a line to it; always print
# f"Notified {user_name}". Call it twice: once with use_logging=False,
# once with use_logging=True for a different user. After both calls,
# check (and print) whether "e4_log.txt" exists, then clean it up if so.

# YOUR CODE HERE


# SOLUTION:
# def send_notification(user_name, use_logging=False):
#     ctx = open("e4_log.txt", "a") if use_logging else contextlib.nullcontext()
#     with ctx as log_file:
#         if log_file:
#             log_file.write(f"Notified {user_name}\n")
#         print(f"Notified {user_name}")
#
# send_notification("Riya Deshmukh", use_logging=False)
# send_notification("Arjun Mehta", use_logging=True)
#
# log_exists = os.path.exists("e4_log.txt")
# print(f"Log file created: {log_exists}")
# if log_exists:
#     os.remove("e4_log.txt")
# Expected output:
# Notified Riya Deshmukh
# Notified Arjun Mehta
# Log file created: True

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION F — Mixed Challenges (Day 19 + All Prior Days)
# ════════════════════════════════════════════════════════════════

print()
print("═" * 50)
print("SECTION F: Mixed Challenges")
print("═" * 50)

# ── Problem F1 🔴 ──
# (Day 19 + Day 9 + Day 11) Build a class-based context manager
# `RetryableTask` that accepts `task_name` and `max_attempts`. It has a
# method `attempt(succeeds)` that raises a custom exception
# `TaskFailedError` if succeeds is False. On __exit__, if a
# TaskFailedError propagated, print f"{task_name} failed permanently
# after all attempts" and suppress it; otherwise print
# f"{task_name} completed successfully". (For this problem, just call
# attempt() once per `with` block — retry looping across multiple `with`
# blocks is not required.) Demonstrate with task_name="Sync Inventory",
# calling attempt(False).

# YOUR CODE HERE


# SOLUTION:
# class TaskFailedError(Exception):
#     pass
#
# class RetryableTask:
#     def __init__(self, task_name, max_attempts=3):
#         self.task_name = task_name
#         self.max_attempts = max_attempts
#
#     def __enter__(self):
#         return self
#
#     def attempt(self, succeeds):
#         if not succeeds:
#             raise TaskFailedError(f"{self.task_name} did not succeed")
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is TaskFailedError:
#             print(f"{self.task_name} failed permanently after all attempts")
#             return True
#         print(f"{self.task_name} completed successfully")
#         return False
#
# with RetryableTask("Sync Inventory") as task:
#     task.attempt(False)
# Expected output: Sync Inventory failed permanently after all attempts

print("-" * 50)

# ── Problem F2 🔴 ──
# (Day 19 + Day 13 + Day 6) Write a generator-based context manager
# `batch_processor(items, batch_size)` that yields successive batches
# (lists) of `items` of size `batch_size` ONE AT A TIME is not possible
# with a single yield — instead, have it yield the full list of batches
# (a list of lists) computed using a list comprehension, then in a
# finally block print f"Processed {len(items)} items in {<number of
# batches>} batches". Test with items = list(range(1, 11)) and
# batch_size = 3.

# YOUR CODE HERE


# SOLUTION:
# @contextlib.contextmanager
# def batch_processor(items, batch_size):
#     batches = [items[i:i + batch_size] for i in range(0, len(items), batch_size)]
#     try:
#         yield batches
#     finally:
#         print(f"Processed {len(items)} items in {len(batches)} batches")
#
# with batch_processor(list(range(1, 11)), batch_size=3) as batches:
#     for b in batches:
#         print(f"  Batch: {b}")
# Expected output:
#   Batch: [1, 2, 3]
#   Batch: [4, 5, 6]
#   Batch: [7, 8, 9]
#   Batch: [10]
# Processed 10 items in 4 batches

print("-" * 50)

# ── Problem F3 🔴 ──
# (Day 19 + Day 8 + Day 12) Build a context manager (class-based OR
# @contextmanager, your choice) called `csv_export_session(filename)`
# that, on enter, opens the file for writing and returns the file handle;
# on exit, always writes a footer line "# export complete" to the file
# (even if an exception occurred) before closing, then re-raises any
# exception. Use it to write 2 rows of a fictional Flipkart order export
# ("OrderID,Customer,Amount" header + one data row), forcing no error,
# then read the file back and print all its lines.

# YOUR CODE HERE


# SOLUTION:
# @contextlib.contextmanager
# def csv_export_session(filename):
#     f = open(filename, "w")
#     try:
#         yield f
#     finally:
#         f.write("# export complete\n")
#         f.close()
#
# with csv_export_session("f3_export.csv") as f:
#     f.write("OrderID,Customer,Amount\n")
#     f.write("1001,Meera Iyer,1899\n")
#
# with open("f3_export.csv") as f:
#     for line in f:
#         print(line.rstrip())
# os.remove("f3_export.csv")
# Expected output:
# OrderID,Customer,Amount
# 1001,Meera Iyer,1899
# # export complete

print("-" * 50)

print()
print("═" * 50)
print("END OF DAY 19 PRACTICE PROBLEMS")
print("═" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Sections in this file:
#   D. @contextmanager Decorator — 4 problems (yield-based enter/exit, state, error handling)
#   E. contextlib Utilities      — 4 problems (suppress, ExitStack, redirect_stdout, nullcontext)
#   F. Mixed Challenges          — 3 problems (combining Day 19 with Days 6, 8, 9, 11, 12, 13)
#
# Combined with file 1 (day19_practise_problems_01_context_manager_protocol.py):
#   Total problems this day: 24 (13 in file 1 + 11 in file 2)
#   Difficulty breakdown: 7 🟢 Warm-up, 9 🟡 Core, 8 🔴 Challenge
#
# Preview of Day 20: Testing with unittest & pytest — fixtures, mocking,
# and coverage reports build directly on today's context manager skills,
# since pytest fixtures are themselves a form of context manager!
