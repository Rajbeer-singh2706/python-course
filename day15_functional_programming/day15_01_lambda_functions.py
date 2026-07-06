"""
Day 15 — Functional Programming
File 1 of 3: Lambda Expressions

Covers:
    - What a lambda is and how it differs from a regular def function
    - Single and multi-argument lambdas
    - Where lambdas are typically used (as arguments to other functions)
    - When to prefer def over lambda

Prerequisites:
    - Day 5 (Functions & Scope) — parameters, arguments, return values
    - Day 6 (Data Structures) — lists, dictionaries

How to run:
    python day15_01_lambda_functions.py
"""

# ══════════════════════════════════════════════════════════════
# SECTION 1 — What Is a Lambda?
# ══════════════════════════════════════════════════════════════
# A lambda is a small, anonymous (unnamed) function written in a single
# expression. It's Python's shorthand for a function that:
#   1. Does one simple thing
#   2. Doesn't need a name because it's only used once or twice
#   3. Fits comfortably on one line
#
# Syntax:  lambda arguments: expression
#
# The expression is automatically returned — there is no "return" keyword.

print("═" * 50)
print("SECTION 1: What Is a Lambda?")
print("═" * 50)

# ── A regular function ──
def square(x):
    return x * x

# ── The exact same behaviour as a lambda ──
square_lambda = lambda x: x * x

print(square(5))          # Output: 25
print(square_lambda(5))   # Output: 25

# Both are callable the same way, but the lambda has no name of its own
# (we only gave it one — square_lambda — by assigning it to a variable).
print(type(square_lambda))   # Output: <class 'function'>


# ══════════════════════════════════════════════════════════════
# SECTION 2 — Lambdas With Multiple Arguments
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION 2: Lambdas With Multiple Arguments")
print("═" * 50)

# ── Two arguments ──
# Priya wants to calculate the final price of a Flipkart item including GST.
calculate_price = lambda base, gst_percent: base + (base * gst_percent / 100)

print(calculate_price(1000, 18))   # Output: 1180.0
print(calculate_price(500, 5))     # Output: 525.0

# ── Three arguments ──
# A simple weighted average of three exam scores.
weighted_average = lambda a, b, c: round((a * 0.3) + (b * 0.3) + (c * 0.4), 2)

print(weighted_average(80, 90, 70))   # Output: 79.0

# ── Lambda with a default argument ──
apply_discount = lambda price, discount=10: price - (price * discount / 100)

print(apply_discount(1000))       # Output: 900.0
print(apply_discount(1000, 25))   # Output: 750.0


# ══════════════════════════════════════════════════════════════
# SECTION 3 — Why Lambdas Exist: Passing Functions as Arguments
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION 3: Why Lambdas Exist")
print("═" * 50)

# Lambdas are most useful when a function needs another function as an
# argument, and writing a full def just for that one use feels wasteful.
# sorted() is the classic example — it accepts a "key" function that tells
# it what to compare.

students = [
    {"name": "Arjun", "marks": 76},
    {"name": "Priya", "marks": 88},
    {"name": "Meera", "marks": 92},
]

# Without lambda, you'd need a separate named function just for this one sort:
def get_marks(student):
    return student["marks"]

sorted_by_def = sorted(students, key=get_marks)

# With lambda, the same logic lives inline, right where it's used:
sorted_by_lambda = sorted(students, key=lambda s: s["marks"])

print([s["name"] for s in sorted_by_def])      # Output: ['Arjun', 'Priya', 'Meera']
print([s["name"] for s in sorted_by_lambda])    # Output: ['Arjun', 'Priya', 'Meera']

print("-" * 50)


# ══════════════════════════════════════════════════════════════
# SECTION 4 — When to Use lambda vs def
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("SECTION 4: When to Use lambda vs def")
print("═" * 50)

# RULE OF THUMB:
#   - Use lambda for a short, one-off expression passed directly into
#     another function (map, filter, sorted, etc.)
#   - Use def when the logic needs a name, multiple lines, a docstring,
#     or will be reused in several places.

# Good use of lambda — quick, inline, disposable:
prices = [249, 499, 129]
with_gst = list(map(lambda p: round(p * 1.05, 2), prices))
print(with_gst)   # Output: [261.45, 523.95, 135.45]

# Poor use of lambda — this deserves a real function with a name:
# BAD:
# validate = lambda order: order["amount"] > 0 and order["status"] == "confirmed" \
#     and order["items"] and order["customer"] is not None
# GOOD:
def is_valid_order(order):
    """A valid order has a positive amount, is confirmed, has items, and a customer."""
    return (
        order["amount"] > 0
        and order["status"] == "confirmed"
        and order["items"]
        and order["customer"] is not None
    )


# ══════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ══════════════════════════════════════════════════════════════
print()
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1 — Sanjay converts Celsius to Fahrenheit for a weather app.
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
print(f"Example 1: {celsius_to_fahrenheit(30)}")   # Output: Example 1: 86.0
print("-" * 50)

# Example 2 — Meera checks if a Paytm transaction ID is valid (10 digits).
is_valid_txn_id = lambda txn_id: len(str(txn_id)) == 10
print(f"Example 2: {is_valid_txn_id(9876543210)}")   # Output: Example 2: True
print("-" * 50)

# Example 3 — Riya builds a simple ranking label from a score.
grade_label = lambda score: "A" if score >= 90 else ("B" if score >= 75 else "C")
print(f"Example 3: {grade_label(82)}")   # Output: Example 3: B
print("-" * 50)

# Example 4 — Arjun combines first and last name into a display name.
full_name = lambda first, last: f"{first} {last}".title()
print(f"Example 4: {full_name('arjun', 'mehta')}")   # Output: Example 4: Arjun Mehta
print("-" * 50)

# Example 5 — Sorting a list of Swiggy restaurants by rating (highest first).
restaurants = [
    {"name": "Punjabi Tadka", "rating": 4.2},
    {"name": "South Spice", "rating": 4.7},
    {"name": "Bengal Bites", "rating": 4.4},
]
top_rated = sorted(restaurants, key=lambda r: r["rating"], reverse=True)
print(f"Example 5: {[r['name'] for r in top_rated]}")
# Output: Example 5: ['South Spice', 'Bengal Bites', 'Punjabi Tadka']
print("-" * 50)


# ══════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ══════════════════════════════════════════════════════════════
# Write a lambda called "is_metro_city" that takes a city name and returns
# True if it's one of: "Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata".
#
# Expected output:
#   True
#   False

# YOUR CODE HERE
is_metro_city = None   # replace with your lambda

# ── Solution (uncomment to check your work) ──
# is_metro_city = lambda city: city in ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata"]
# print(is_metro_city("Mumbai"))    # Output: True
# print(is_metro_city("Nashik"))    # Output: False


# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
# In this file you learned:
#   - lambda creates a small anonymous function in one expression
#   - lambdas can take zero, one, or multiple arguments (and even defaults)
#   - lambdas shine as inline arguments to functions like sorted(), map(), filter()
#   - use def instead of lambda once logic needs a name, multiple lines, or reuse
#
# Next file: day15_02_map_filter_reduce.py
#   → Using lambda together with map(), filter(), and functools.reduce()
#     to transform, select, and combine data functionally.
