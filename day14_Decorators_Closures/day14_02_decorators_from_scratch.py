"""
Day 14 — Decorators & Closures
File 2 of 3: Writing a Decorator From Scratch

What this file covers:
    - What a decorator actually is (a function returning a function)
    - The @ syntax as sugar for `func = decorator(func)`
    - Building decorators that accept *args, **kwargs
    - Why functools.wraps matters (preserving __name__ / __doc__)
    - Decorators that accept their own arguments (decorator factories)
    - Stacking multiple decorators

Prerequisites:
    - day14_01_first_class_and_closures.py (functions as objects, closures)

How to run:
    python day14_02_decorators_from_scratch.py
"""

import functools
import time


# ════════════════════════════════════════════════════════════════
# SECTION 1 — What Is a Decorator?
# ════════════════════════════════════════════════════════════════
#
# A decorator is simply a function that:
#   1. Takes another function as input
#   2. Defines a new "wrapper" function that adds some behaviour
#   3. Returns that wrapper function
#
# The @decorator_name syntax placed above a function definition is
# just a shortcut. These two blocks of code do exactly the same thing:
#
#   @my_decorator                further down the file, both are
#   def say_hi(): ...            identical to:
#
#                                 def say_hi(): ...
#                                 say_hi = my_decorator(say_hi)

# ── The "desugared" version first, so the @ syntax doesn't feel like magic ──

def shout(func):
    """A tiny decorator: uppercases whatever string `func` returns."""

    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def say_hi():
    return "namaste"


say_hi = shout(say_hi)   # manual decoration — no @ syntax yet
print(say_hi())
# Output: NAMASTE

print("-" * 50)

# ── The same thing, using @ syntax ──

@shout
def say_bye():
    return "alvida"


print(say_bye())
# Output: ALVIDA

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2 — Handling Arguments With *args, **kwargs
# ════════════════════════════════════════════════════════════════
#
# The `shout` decorator above only works on functions that take NO
# arguments. Real functions usually take arguments, so the wrapper
# needs to accept and forward *args and **kwargs.

def log_call(func):
    """Logs the function name, arguments, and return value."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@log_call
def place_order(item, city="Mumbai"):
    return f"Order for {item} placed in {city}"


place_order("Biryani", city="Bengaluru")
# Output: Calling place_order with args=('Biryani',), kwargs={'city': 'Bengaluru'}
# Output: place_order returned: Order for Biryani placed in Bengaluru

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3 — Why functools.wraps Matters
# ════════════════════════════════════════════════════════════════
#
# Without functools.wraps, the decorated function "loses its identity" —
# introspection tools (help(), __name__, __doc__) report the WRAPPER's
# metadata instead of the original function's. This breaks debugging,
# documentation generators, and testing tools.

def broken_decorator(func):
    """A decorator WITHOUT functools.wraps -- shows the problem."""

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@broken_decorator
def calculate_gst(amount):
    """Calculate 18% GST on the given amount."""
    return round(amount * 0.18, 2)


print(calculate_gst.__name__)   # Output: wrapper   <-- WRONG!
print(calculate_gst.__doc__)    # Output: None       <-- WRONG!

print("-" * 50)


def fixed_decorator(func):
    """A decorator WITH functools.wraps -- identity is preserved."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@fixed_decorator
def calculate_cgst(amount):
    """Calculate 9% CGST on the given amount."""
    return round(amount * 0.09, 2)


print(calculate_cgst.__name__)   # Output: calculate_cgst   <-- correct!
print(calculate_cgst.__doc__)    # Output: Calculate 9% CGST on the given amount.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — 5 progressively complex worked examples
# ════════════════════════════════════════════════════════════════

# --- Example 1: a timing decorator ---

def timer(func):
    """Reports how long a function took to run, in milliseconds."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} took {elapsed_ms:.3f} ms")
        return result

    return wrapper


@timer
def sum_of_squares(n):
    return sum(i * i for i in range(n))


total = sum_of_squares(10000)
print(f"Result: {total}")
# Output: sum_of_squares took <some small number> ms
# Output: Result: 333283335000

print("-" * 50)

# --- Example 2: a retry-count decorator (no actual failure simulated) ---

def count_calls(func):
    """Tracks how many times a function has been called, using a closure."""
    call_count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"{func.__name__} has been called {call_count} time(s)")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def check_pnr_status(pnr):
    return f"PNR {pnr}: CONFIRMED"


check_pnr_status("2451236789")
check_pnr_status("2451236790")
# Output: check_pnr_status has been called 1 time(s)
# Output: check_pnr_status has been called 2 time(s)

print("-" * 50)

# --- Example 3: a decorator FACTORY (a decorator that takes arguments) ---
#
# To let a decorator accept its own arguments (like a repeat count),
# we need one MORE layer of nesting: a function that returns a decorator.

def repeat(times):
    """Decorator factory: repeats the decorated function `times` times."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


@repeat(times=3)
def draw_lucky_number():
    import random
    random.seed(42)  # fixed seed for reproducible output in this demo
    return random.randint(1, 100)


# Note: because we reseed inside the function, all 3 calls give the
# same number here — this keeps the expected output deterministic.
print(draw_lucky_number())
# Output: [82, 82, 82]

print("-" * 50)

# --- Example 4: a validation decorator for Flipkart-style pricing ---

def validate_positive(func):
    """Raises ValueError if any positional argument is negative."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"{func.__name__} received a negative value: {value}")
        return func(*args, **kwargs)

    return wrapper


@validate_positive
def apply_flipkart_cashback(price, cashback_percent):
    return round(price - (price * cashback_percent / 100), 2)


print(apply_flipkart_cashback(2000, 10))
# Output: 1800.0

try:
    apply_flipkart_cashback(-500, 10)
except ValueError as error:
    print(f"Blocked: {error}")
# Output: Blocked: apply_flipkart_cashback received a negative value: -500

print("-" * 50)

# --- Example 5: stacking multiple decorators ---
#
# Decorators apply bottom-up: the one closest to the function runs
# first (innermost), then each decorator above wraps the previous result.

@timer
@log_call
def get_order_summary(order_id):
    return f"Order {order_id}: 2 items, Rs.450 total"


get_order_summary("SW3005")
# Output: Calling get_order_summary with args=('SW3005',), kwargs={}
# Output: get_order_summary returned: Order SW3005: 2 items, Rs.450 total
# Output: get_order_summary took <some small number> ms
# (this only reports the correct name because log_call uses functools.wraps)
#
# Reading order: @log_call wraps get_order_summary first (innermost),
# then @timer wraps the already-logged version (outermost).

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
#
# Write a decorator `uppercase_result` that converts a function's
# string return value to uppercase. Use functools.wraps. Then apply
# it to `city_welcome_message` below.
#
# Expected output:
#   WELCOME TO PUNE!

# YOUR CODE HERE
def uppercase_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_result
def city_welcome_message(city):
    return f"welcome to {city}!"


print(city_welcome_message("Pune"))   # Expected: WELCOME TO PUNE!


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - A decorator is a function that takes a function and returns a
#     wrapped version of it; @ syntax is sugar for func = decorator(func)
#   - Wrapper functions should accept *args, **kwargs to stay generic
#   - functools.wraps(func) preserves __name__ and __doc__ on the wrapper
#   - Decorator factories (a function returning a decorator) let you
#     pass arguments to the decorator itself, e.g. @repeat(times=3)
#   - Stacked decorators apply bottom-up (closest to the function first)
#
# Next file: day14_03_builtin_decorators.py
# We look at Python's built-in @staticmethod, @classmethod, and
# @property decorators used inside classes.

if __name__ == "__main__":
    print("\nDay 14, File 2 complete — decorators from scratch.")
