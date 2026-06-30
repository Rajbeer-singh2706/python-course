"""
Day 12 — Modules & Packages (Part 2 of 3)
==========================================

Topic   : The `__main__` guard
Covers  : Why `if __name__ == "__main__":` exists, how Python sets the
          `__name__` variable, importable vs runnable scripts
Prereqs : Day 5 (functions), Day 12 Part 1 (imports & packages)
Run with: python day12_02_main_guard.py

THE PROBLEM IT SOLVES
Every Python file has a hidden built-in variable called `__name__`.
- When you RUN a file directly (python myfile.py), Python sets
  `__name__` to the string "__main__".
- When you IMPORT a file into another file (import myfile), Python sets
  `__name__` to the file's own module name (e.g. "myfile") instead.

This lets a single .py file behave differently depending on whether it
is being run as the main program or being reused as a library of
functions/classes by another file — which is exactly how real Python
projects (including our Day 26-30 capstone) are structured.
"""

# ════════════════════════════════════════════════════════════════
# SECTION 1: WHAT IS `__name__`?
# ════════════════════════════════════════════════════════════════

# ── Concept: __name__ is automatically set by Python ──
print("── Inspecting __name__ ──")
print(f"The value of __name__ in this file right now is: {__name__!r}")
# Output (when run directly): The value of __name__ in this file right now is: '__main__'

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: WHY "JUST RUNNING CODE AT THE TOP LEVEL" CAUSES PROBLEMS
# ════════════════════════════════════════════════════════════════

# ── Concept: Demo functions that simulate a billing module ──
# Imagine this file is `billing.py`, used by a bigger Mumbai retail app.


def calculate_gst(amount, rate=0.18):
    """Return the GST (tax) amount for a given bill amount."""
    return round(amount * rate, 2)


def generate_invoice(customer_name, amount):
    """Build and return a simple invoice summary string."""
    gst = calculate_gst(amount)
    total = round(amount + gst, 2)
    return (
        f"Invoice for {customer_name}: "
        f"Subtotal Rs.{amount:.2f} + GST Rs.{gst:.2f} = Total Rs.{total:.2f}"
    )


# ── Concept: Code WITHOUT a guard runs every time the file is imported ──
# If we wrote `print(generate_invoice("Test", 100))` right here with no
# guard, then EVERY OTHER FILE that does `import day12_02_main_guard`
# would immediately print that test invoice too — even though they only
# wanted to borrow the `calculate_gst` function. That is almost always
# unwanted side-effect behaviour in a real project.

print("── Functions defined, but no test code has run automatically ──")
print("(If this were imported elsewhere, only the functions would load)")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: THE GUARD ITSELF
# ════════════════════════════════════════════════════════════════

# ── Concept: if __name__ == "__main__": ──
# Code placed inside this block ONLY runs when the file is executed
# directly with `python filename.py`. It is skipped entirely when the
# file is imported as a module by something else.
#
#   if __name__ == "__main__":
#       # "demo" or "test" code goes here
#       print(generate_invoice("Riya", 500))
#
# This is why almost every well-structured .py file in this course
# (and in professional codebases) ends with this exact pattern.

print("── The guard pattern (see bottom of this file for the real one) ──")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════

print("── Guided Example 1: A reusable temperature converter function ──")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


mumbai_temp_c = 34
print(f"{mumbai_temp_c}°C is {celsius_to_fahrenheit(mumbai_temp_c):.1f}°F")
# Output: 34°C is 93.2°F

print("-" * 50)

print("── Guided Example 2: A function library for a shop ──")


def apply_discount(price, percent):
    return round(price - (price * percent / 100), 2)


item_price = 1200
discount_percent = 15
print(f"Original: Rs.{item_price}, after {discount_percent}% off: Rs.{apply_discount(item_price, discount_percent)}")
# Output: Original: Rs.1200, after 15% off: Rs.1020.0

print("-" * 50)

print("── Guided Example 3: Demonstrating module-style organisation ──")


class Invoice:
    """A small class that would normally live in its own module."""

    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

    def total_with_gst(self):
        return round(self.amount * 1.18, 2)


sample_invoice = Invoice("Arjun Mehta", 2500)
print(f"{sample_invoice.customer}'s total with GST: Rs.{sample_invoice.total_with_gst()}")
# Output: Arjun Mehta's total with GST: Rs.2950.0

print("-" * 50)

print("── Guided Example 4: Why guards matter when 'importing' is simulated ──")


def simulate_import_behaviour():
    """
    Pretend this function represents another file doing:
        import day12_02_main_guard as billing
    Notice it can call our functions WITHOUT triggering any demo code,
    because all demo/test prints in this file live inside the guard.
    """
    return generate_invoice("Simulated Import Caller", 750)


print(simulate_import_behaviour())

print("-" * 50)

print("── Guided Example 5: Multiple entry-point style checks ──")
modes = ["__main__", "billing_utils", "__main__"]
for mode in modes:
    if mode == "__main__":
        print(f"Mode '{mode}' -> file was run directly, demo code WOULD execute")
    else:
        print(f"Mode '{mode}' -> file was imported, demo code is SKIPPED")

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# 1. Write a function `is_high_value_order(amount)` that returns True if
#    amount > 5000, else False.
# 2. Do NOT call it at the top level of the file.
# 3. Only call and print its result inside the `if __name__ == "__main__":`
#    block at the bottom of this file, using amount = 6200.
#
# Expected output (only when this file is run directly):
#    Is 6200 a high-value order? True


# YOUR CODE HERE
def is_high_value_order(amount):
    return amount > 5000


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Covered in this file:
#   - `__name__` is set to "__main__" only when a file is run directly
#   - Code outside the guard runs on BOTH run and import (usually bad
#     for demo/test code)
#   - The `if __name__ == "__main__":` pattern keeps reusable functions
#     and classes separate from "try it out" code
#
# Next up in Part 3: exploring the standard library — os, sys, math,
# datetime, and pathlib — five modules you will use in almost every
# Python project from here on, including our Day 26-30 capstone.

if __name__ == "__main__":
    print("\n── Inside the __main__ guard now ──")
    print(generate_invoice("Riya Deshmukh", 500))
    test_amount = 6200
    print(f"Is {test_amount} a high-value order? {is_high_value_order(test_amount)}")
    print("\nDay 12, Part 2 (__main__ guard) complete!")
