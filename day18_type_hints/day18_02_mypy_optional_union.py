"""
Day 18 — Type Hints & Static Analysis
File 2 of 3: Static Checking with mypy, plus Optional & Union Types

Covers:
    - Installing and running mypy from the command line
    - Reading a mypy error report
    - Optional[X] for values that might be None
    - Union[X, Y] (and the modern X | Y syntax) for values that could be
      one of several types
    - Narrowing Optional/Union values safely with `if` checks

Prerequisites:
    - Day 18, file 1 (Type Hints Basics)

How to run:
    python day18_02_mypy_optional_union.py
"""

from typing import Optional, Union

# ════════════════════════════════════════════════════════════
# SECTION 1: Running mypy From the Command Line
# ════════════════════════════════════════════════════════════
# mypy is a SEPARATE program from the Python interpreter. It reads your
# .py files WITHOUT running them, and cross-checks every hint you wrote.
#
# Install it once per project:
#     pip install mypy --break-system-packages
#
# Then run it against a file (or a whole folder):
#     python -m mypy day18_02_mypy_optional_union.py
#
# mypy prints one line per problem, in the format:
#     filename.py:LINE: error: <description>  [error-code]
#
# For example, if a script named bad_example.py contained:
#
#     def add_gst(amount: float) -> float:
#         return amount * 1.18
#
#     add_gst("1000")   # passing a str where float is expected
#
# running `python -m mypy bad_example.py` would report something like:
#
#     bad_example.py:4: error: Argument 1 to "add_gst" has incompatible
#     type "str"; expected "float"  [arg-type]
#     Found 1 error in 1 file (checked 1 source file)
#
# mypy never runs add_gst() — it only reads the *signature* and the
# *call site* and compares the two. That's the whole idea of "static"
# analysis: catching mismatches before the program ever executes.

print("=" * 50)
print("SECTION 1: mypy runs from the terminal, not inside this script")
print("=" * 50)
print("Command:  python -m mypy day18_02_mypy_optional_union.py")
print("(see the module docstring above for how to read its output)")


# ════════════════════════════════════════════════════════════
# SECTION 2: Optional — a Value That Might Be None
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 2: Optional[X]")
print("=" * 50)
# Optional[X] literally means "X, or None". It is shorthand for
# Union[X, None]. Use it whenever a variable, parameter, or return value
# is allowed to be missing.


def find_pnr_status(pnr: str, known_pnrs: dict[str, str]) -> Optional[str]:
    """Look up an IRCTC PNR's status. Returns None if the PNR is unknown."""
    return known_pnrs.get(pnr)


pnr_database: dict[str, str] = {
    "4567891234": "CONFIRMED",
    "9988776655": "WAITLISTED",
}

print(find_pnr_status("4567891234", pnr_database))
# Output: CONFIRMED
print(find_pnr_status("0000000000", pnr_database))
# Output: None


# ── Narrowing an Optional value before using it ──
# You cannot safely call string methods on "maybe None" without checking
# first — mypy will refuse to let you, and Python itself would crash
# with AttributeError if the value really is None.
def describe_status(status: Optional[str]) -> str:
    if status is None:
        return "No record found for this PNR."
    # Inside this branch, mypy now KNOWS status is str, not Optional[str].
    # This is called "narrowing".
    return f"Status: {status.title()}"


print(describe_status(find_pnr_status("9988776655", pnr_database)))
# Output: Status: Waitlisted
print(describe_status(find_pnr_status("1111111111", pnr_database)))
# Output: No record found for this PNR.


# ════════════════════════════════════════════════════════════
# SECTION 3: Union — a Value That Could Be Several Types
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 3: Union[X, Y]")
print("=" * 50)
# Union[X, Y] means "either X or Y". Common example: a function that
# accepts a discount as either a flat rupee amount (int) or a
# percentage (float).


def apply_discount(price: float, discount: Union[int, float]) -> float:
    """
    Apply a discount to a price.
    If `discount` is an int, treat it as a flat rupee amount.
    If `discount` is a float, treat it as a percentage.
    """
    if isinstance(discount, int):
        return price - discount
    return price - (price * discount / 100)


print(apply_discount(1000.0, 150))
# Output: 850.0
print(apply_discount(1000.0, 15.0))
# Output: 850.0


# ── Modern syntax (Python 3.10+): X | Y instead of Union[X, Y] ──
# This reads more naturally and needs no import from `typing`.
def format_order_id(order_id: int | str) -> str:
    """Accept an order ID as either an int or a str, always return str."""
    return f"ORD-{order_id}"


print(format_order_id(10245))
# Output: ORD-10245
print(format_order_id("SW-778"))
# Output: ORD-SW-778


# ── Modern syntax also applies to Optional: X | None ──
def welcome_message(name: str | None) -> str:
    if name is None:
        return "Welcome, Guest!"
    return f"Welcome, {name}!"


print(welcome_message("Sanjay Verma"))
# Output: Welcome, Sanjay Verma!
print(welcome_message(None))
# Output: Welcome, Guest!


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Progressive, Indian-context
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("GUIDED EXAMPLES")
print("=" * 50)


# Example 1: Optional return from a search function
def find_rider(name: str, riders: list[str]) -> Optional[str]:
    for rider in riders:
        if rider.lower() == name.lower():
            return rider
    return None


rider_list = ["Riya Deshmukh", "Meera Iyer"]
print(find_rider("meera iyer", rider_list))
# Output: Meera Iyer
print(find_rider("Arjun Mehta", rider_list))
# Output: None


# Example 2: A dataclass-style record with an Optional field
class Order:
    """An order that may or may not yet have an assigned rider."""

    def __init__(self, order_id: int, rider: Optional[str] = None) -> None:
        self.order_id: int = order_id
        self.rider: Optional[str] = rider

    def status(self) -> str:
        if self.rider is None:
            return f"Order #{self.order_id}: awaiting rider assignment"
        return f"Order #{self.order_id}: assigned to {self.rider}"


order_a = Order(20001)
order_b = Order(20002, rider="Sanjay Verma")
print(order_a.status())
# Output: Order #20001: awaiting rider assignment
print(order_b.status())
# Output: Order #20002: assigned to Sanjay Verma


# Example 3: Union input, normalised output
def normalise_pincode(pincode: Union[int, str]) -> str:
    """Pincodes may arrive as int (from a form) or str (from a CSV)."""
    return str(pincode).zfill(6)


print(normalise_pincode(411001))
# Output: 411001
print(normalise_pincode("5600"))
# Output: 005600


# Example 4: Combining Optional with a collection type
def latest_order_id(order_ids: list[int]) -> Optional[int]:
    """Return the highest order ID, or None if the list is empty."""
    if not order_ids:
        return None
    return max(order_ids)


print(latest_order_id([10245, 10312, 10098]))
# Output: 10312
print(latest_order_id([]))
# Output: None


# Example 5: A function using the modern `|` syntax for both Union and Optional
def parse_rating(raw: str | int | None) -> float | None:
    """
    Parse a Zomato rating that may arrive as a string ('4.5'), an int (4),
    or be missing entirely (None).
    """
    if raw is None:
        return None
    return float(raw)


print(parse_rating("4.5"))
# Output: 4.5
print(parse_rating(4))
# Output: 4.0
print(parse_rating(None))
# Output: None


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Write a fully type-hinted function `safe_average` that takes a
# list[float] | None and returns Optional[float]:
#   - If the input is None OR an empty list, return None.
#   - Otherwise return the average, rounded to 2 decimal places.
#
# Expected output:
#   safe_average([80.0, 90.0, 70.0]) -> 80.0
#   safe_average([])                 -> None
#   safe_average(None)               -> None

print("\n" + "=" * 50)
print("MINI-CHALLENGE")
print("=" * 50)

# YOUR CODE HERE
def safe_average(values: list[float] | None) -> float | None:
    if not values:
        return None
    return round(sum(values) / len(values), 2)


print(safe_average([80.0, 90.0, 70.0]))
# Output: 80.0
print(safe_average([]))
# Output: None
print(safe_average(None))
# Output: None

# ── SOLUTION (reference) ──
# def safe_average(values: list[float] | None) -> float | None:
#     if not values:
#         return None
#     return round(sum(values) / len(values), 2)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Covered today (file 2 of 3):
#   - mypy is a separate command-line tool that statically checks hints
#     without running your code: python -m mypy <file>
#   - Optional[X] means "X or None" — always narrow with an `is None`
#     check before using the value
#   - Union[X, Y] means "X or Y" — narrow with isinstance() checks
#   - Modern syntax: X | Y replaces Union[X, Y], and X | None replaces
#     Optional[X], available from Python 3.10 onward
#
# Next file (3 of 3): TypeVar and Generics — writing functions and
# classes that work with ANY type while still being fully type-checked.

if __name__ == "__main__":
    pass
