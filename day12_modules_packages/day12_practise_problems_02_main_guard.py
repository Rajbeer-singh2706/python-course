"""
Day 12 — Practice Problems (File 2 of 3)
==========================================

Topic         : The `__main__` guard
Cumulative    : Builds on File 1 (imports)
Difficulty    : 🟢 Warm-up | 🟡 Core | 🔴 Challenge
Section Index :
    C — The __main__ Guard

Run with: python day12_practise_problems_02_main_guard.py
All input() calls are simulated using pre-assigned variables.
"""

print("=" * 60)
print("SECTION C — THE __main__ GUARD")
print("=" * 60)

# ── Problem C1 — 🟢 Warm-up ──
# Print the value of `__name__` in this file. What string do you expect
# to see since this file is being run directly?

# YOUR CODE HERE


# SOLUTION:
# print(__name__)  # Expected: __main__

print("-" * 50)

# ── Problem C2 — 🟢 Warm-up ──
# Write a function `greet(name)` that returns f"Namaste, {name}!".
# Do NOT call it at the top level — only call and print it for
# name = "Kabir" inside an `if __name__ == "__main__":` block.

# YOUR CODE HERE


# SOLUTION:
# def greet(name):
#     return f"Namaste, {name}!"
#
# if __name__ == "__main__":
#     print(greet("Kabir"))  # Expected: Namaste, Kabir!

print("-" * 50)

# ── Problem C3 — 🟡 Core ──
# Write a function `square(n)` that returns n*n. Then write THREE
# separate test calls for n = 2, n = 5, n = 9, but make sure all three
# test prints only happen inside one `if __name__ == "__main__":` block
# (not three separate ones).

# YOUR CODE HERE


# SOLUTION:
# def square(n):
#     return n * n
#
# if __name__ == "__main__":
#     for value in (2, 5, 9):
#         print(f"{value} squared is {square(value)}")
#     # Expected:
#     # 2 squared is 4
#     # 5 squared is 25
#     # 9 squared is 81

print("-" * 50)

# ── Problem C4 — 🟡 Core ──
# A function `convert_inr_to_usd(amount, rate=83.0)` should return the
# USD equivalent of an INR amount. Define the function at the top
# level, but ONLY print a demo conversion of 5000 INR inside the guard.

# YOUR CODE HERE


# SOLUTION:
# def convert_inr_to_usd(amount, rate=83.0):
#     return round(amount / rate, 2)
#
# if __name__ == "__main__":
#     print(convert_inr_to_usd(5000))  # Expected: 60.24

print("-" * 50)

# ── Problem C5 — 🔴 Challenge ──
# Explain in a comment (2-3 lines) what would go wrong if the line
# `process_all_orders()` (a slow function that hits a database) were
# placed at the TOP LEVEL of a file called `orders.py`, and another
# file did `import orders` just to reuse one small helper function
# from it.

# YOUR CODE HERE


# SOLUTION:
# # Because there is no __main__ guard, `process_all_orders()` would run
# # immediately and automatically the moment `import orders` executes,
# # even though the importing file only wanted one helper function.
# # This could slow down or break the importing program unexpectedly,
# # and is a common real-world bug caused by missing the guard.

print("-" * 50)

# ── Problem C6 — 🔴 Challenge ──
# Write a function `run_diagnostics()` that returns a dictionary:
# {"status": "ok", "module": __name__}. Call it ONLY inside the guard
# and print the result.

# YOUR CODE HERE


# SOLUTION:
# def run_diagnostics():
#     return {"status": "ok", "module": __name__}
#
# if __name__ == "__main__":
#     print(run_diagnostics())  # Expected: {'status': 'ok', 'module': '__main__'}

print("-" * 50)

print("=" * 60)
print("Section C: 6 problems")
print("Next file: day12_practise_problems_03_stdlib_modules.py (includes Mixed Challenges)")
print("=" * 60)

if __name__ == "__main__":
    print("\nDay 12 Practice — File 2 (__main__ Guard) complete!")
