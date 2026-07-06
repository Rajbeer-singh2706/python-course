"""
Day 18 — Type Hints & Static Analysis
File 1 of 3: Type Hints Basics

Covers:
    - Why type hints exist and what problem they solve
    - Annotating variables
    - Annotating function parameters and return values
    - Type hints are NOT enforced at runtime (Python stays dynamic)
    - Built-in generic collection hints: list[...], dict[...], tuple[...], set[...]

Prerequisites:
    - Day 5 (Functions & Scope)
    - Day 6 (Data Structures)
    - Day 17 (Advanced OOP — dataclasses, ABCs)

How to run:
    python day18_01_type_hints_basics.py
"""

# ════════════════════════════════════════════════════════════
# SECTION 1: Why Type Hints?
# ════════════════════════════════════════════════════════════
# Python is dynamically typed — a variable can hold any type, and nothing
# stops you from mixing types by accident. In a small script that's fine.
# In a 5,000-line billing system for Flipkart, it becomes a bug factory.
#
# Type hints let you WRITE DOWN your intent — "this parameter should be a
# str", "this function returns an int" — so that:
#   1. Editors (VS Code + Pylance) can autocomplete and flag mistakes
#      as you type, before you ever run the code.
#   2. A separate tool called `mypy` can scan your whole project and
#      catch type mismatches without running a single line.
#   3. Other developers reading your code understand it faster.
#
# IMPORTANT: type hints are just annotations. Python itself never checks
# them while running your program — that job belongs to editors and
# static analysis tools like mypy. We'll prove that below.

print("=" * 50)
print("SECTION 1: Why Type Hints?")
print("=" * 50)

# A function with NO type hints — works, but the reader has to guess
def calculate_gst_no_hints(amount, rate):  # type: ignore[no-untyped-def]
    return amount * (rate / 100)

print(calculate_gst_no_hints(1000, 18))  # type: ignore[no-untyped-call]
# Output: 180.0

# The same function WITH type hints — intent is crystal clear
def calculate_gst(amount: float, rate: float) -> float:
    """Calculate GST amount given a base amount and a GST rate percentage."""
    return amount * (rate / 100)

print(calculate_gst(1000, 18))
# Output: 180.0


# ════════════════════════════════════════════════════════════
# SECTION 2: Annotating Variables
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 2: Annotating Variables")
print("=" * 50)

# ── Basic variable annotations ──
# Syntax: variable_name: Type = value
student_name: str = "Priya Sharma"
age: int = 21
cgpa: float = 8.7
is_enrolled: bool = True

print(student_name, age, cgpa, is_enrolled)
# Output: Priya Sharma 21 8.7 True

# ── Annotating without an initial value ──
# Useful when you declare a variable but assign it later (e.g. inside a
# conditional branch). This is purely informational for editors/mypy.
monthly_fee: float
monthly_fee = 4500.0
print(monthly_fee)
# Output: 4500.0

# ── Type hints do NOT stop you from breaking your own promise ──
# Python will happily let this run, even though it "lies" about the type.
# mypy, however, WOULD flag this line as an error if you ran it as a
# static check (we'll do that in the next file).
# (the ignore comment below silences mypy on this one intentional line)
age = "twenty-one"  # type: ignore[assignment]
print(f"age is now: {age!r} (Python did not stop us!)")
# Output: age is now: 'twenty-one' (Python did not stop us!)

# Reset it back so the rest of the file behaves sensibly
age = 21


# ════════════════════════════════════════════════════════════
# SECTION 3: Annotating Function Parameters & Return Values
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 3: Function Parameters & Return Values")
print("=" * 50)


# ── A function with multiple typed parameters ──
def format_invoice(customer: str, city: str, amount: float) -> str:
    """Return a human-readable invoice line for a Swiggy order."""
    return f"{customer} ({city}) — Rs. {amount:,.2f}"


print(format_invoice("Arjun Mehta", "Bengaluru", 749.50))
# Output: Arjun Mehta (Bengaluru) — Rs. 749.50


# ── A function that returns nothing explicit — use -> None ──
def print_receipt(order_id: int, total: float) -> None:
    """Print a receipt. Returns nothing, so the hint is -> None."""
    print(f"Order #{order_id} | Total: Rs. {total:,.2f}")


print_receipt(10245, 1299.0)
# Output: Order #10245 | Total: Rs. 1,299.00


# ── Default arguments keep their hints too ──
def apply_discount(price: float, discount_percent: float = 10.0) -> float:
    """Apply a percentage discount to a price. Default discount is 10%."""
    return price - (price * discount_percent / 100)


print(apply_discount(2000.0))
# Output: 1800.0
print(apply_discount(2000.0, 25.0))
# Output: 1500.0


# ════════════════════════════════════════════════════════════
# SECTION 4: Built-in Generic Collection Hints
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("SECTION 4: Collection Type Hints")
print("=" * 50)
# Since Python 3.9, the built-in collection types themselves support
# subscripting for hints — no need to import anything from `typing`
# for these common cases: list[X], dict[K, V], tuple[X, ...], set[X]

# ── list[str]: a list containing only strings ──
riders: list[str] = ["Riya Deshmukh", "Sanjay Verma", "Meera Iyer"]
print(riders)
# Output: ['Riya Deshmukh', 'Sanjay Verma', 'Meera Iyer']

# ── dict[str, float]: a dict mapping city names to average delivery fees ──
delivery_fees: dict[str, float] = {
    "Mumbai": 35.0,
    "Pune": 25.0,
    "Chennai": 30.0,
}
print(delivery_fees)
# Output: {'Mumbai': 35.0, 'Pune': 25.0, 'Chennai': 30.0}

# ── tuple[int, str, float]: a FIXED-length tuple where each slot has its
# own type — this is different from list, which is one type repeated ──
order_record: tuple[int, str, float] = (10246, "Chennai", 899.0)
print(order_record)
# Output: (10246, 'Chennai', 899.0)

# ── tuple[int, ...]: a VARIABLE-length tuple of all-the-same type
# (the literal `...` here means "zero or more of the previous type") ──
otp_digits: tuple[int, ...] = (4, 8, 1, 5, 9, 2)
print(otp_digits)
# Output: (4, 8, 1, 5, 9, 2)

# ── set[str]: a set of unique strings ──
visited_cities: set[str] = {"Delhi", "Mumbai", "Pune"}
print(sorted(visited_cities))
# Output: ['Delhi', 'Mumbai', 'Pune']

# ── Nesting: a dict of city -> list of rider names ──
riders_by_city: dict[str, list[str]] = {
    "Mumbai": ["Priya Sharma", "Arjun Mehta"],
    "Pune": ["Riya Deshmukh"],
}
print(riders_by_city)
# Output: {'Mumbai': ['Priya Sharma', 'Arjun Mehta'], 'Pune': ['Riya Deshmukh']}


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Progressive, Indian-context
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 50)
print("GUIDED EXAMPLES")
print("=" * 50)


# Example 1: Simple typed function
def full_name(first: str, last: str) -> str:
    return f"{first} {last}"


print(full_name("Meera", "Iyer"))
# Output: Meera Iyer


# Example 2: Typed function with a collection parameter
def total_spend(amounts: list[float]) -> float:
    return sum(amounts)


zomato_orders = [349.0, 599.0, 220.5]
print(total_spend(zomato_orders))
# Output: 1168.5


# Example 3: Typed function returning a collection
def top_spenders(spend_by_name: dict[str, float], threshold: float) -> list[str]:
    return [name for name, spend in spend_by_name.items() if spend > threshold]


spend_data: dict[str, float] = {
    "Sanjay Verma": 5200.0,
    "Riya Deshmukh": 1800.0,
    "Arjun Mehta": 6100.0,
}
print(top_spenders(spend_data, 3000.0))
# Output: ['Sanjay Verma', 'Arjun Mehta']


# Example 4: Typed function with a tuple return (multiple values)
def split_invoice(total: float, gst_rate: float) -> tuple[float, float]:
    """Return (base_amount, gst_amount) split out of a GST-inclusive total."""
    base = total / (1 + gst_rate / 100)
    gst = total - base
    return base, gst


base_amount, gst_amount = split_invoice(1180.0, 18.0)
print(f"Base: Rs. {base_amount:.2f}, GST: Rs. {gst_amount:.2f}")
# Output: Base: Rs. 1000.00, GST: Rs. 180.00


# Example 5: A small class using typed attributes and methods together
class Passenger:
    """A simple IRCTC passenger record with typed attributes."""

    def __init__(self, name: str, age: int, pnr: str) -> None:
        self.name: str = name
        self.age: int = age
        self.pnr: str = pnr

    def summary(self) -> str:
        return f"{self.name} (age {self.age}) — PNR {self.pnr}"


passenger = Passenger("Priya Sharma", 29, "4567891234")
print(passenger.summary())
# Output: Priya Sharma (age 29) — PNR 4567891234


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Write a fully type-hinted function `average_rating` that takes a
# list[float] of star ratings (e.g. from Zomato reviews) and returns
# the average as a float, rounded to 2 decimal places.
#
# Expected output for ratings = [4.5, 3.0, 5.0, 4.0]:
#   4.12  (Python's round() uses banker's rounding + float representation,
#          so 4.125 rounds down to 4.12 here, not up to 4.13)

print("\n" + "=" * 50)
print("MINI-CHALLENGE")
print("=" * 50)

# YOUR CODE HERE
ratings: list[float] = [4.5, 3.0, 5.0, 4.0]


def average_rating(values: list[float]) -> float:
    return round(sum(values) / len(values), 2)


print(average_rating(ratings))
# Output: 4.12

# ── SOLUTION (reference) ──
# def average_rating(values: list[float]) -> float:
#     return round(sum(values) / len(values), 2)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Covered today (file 1 of 3):
#   - Why type hints exist: editor support, static checking, readability
#   - Annotating variables: name: Type = value
#   - Annotating function parameters and return values, including -> None
#   - Type hints are NOT enforced at runtime — Python still runs "wrong" code
#   - Built-in generic collection hints: list[X], dict[K, V], tuple[...],
#     set[X], and nesting them together
#
# Next file (2 of 3): mypy static checking in practice, plus Optional
# and Union types for values that might be None or one of several types.

if __name__ == "__main__":
    pass
