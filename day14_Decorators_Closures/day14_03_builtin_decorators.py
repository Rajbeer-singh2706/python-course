"""
Day 14 — Decorators & Closures
File 3 of 3: Built-in Decorators — @staticmethod, @classmethod, @property

What this file covers:
    - @staticmethod — utility methods that don't need self or cls
    - @classmethod — methods that receive the class itself (cls),
      commonly used for alternate constructors
    - @property — turning a method into a read-like-an-attribute value
    - @<property_name>.setter — allowing controlled attribute writes
    - Combining all three inside one realistic class

Prerequisites:
    - Day 10 (OOP I), Day 11 (OOP II)
    - day14_02_decorators_from_scratch.py (decorator fundamentals)

How to run:
    python day14_03_builtin_decorators.py
"""


# ════════════════════════════════════════════════════════════════
# SECTION 1 — @staticmethod
# ════════════════════════════════════════════════════════════════
#
# A static method behaves like a plain function that happens to live
# inside a class's namespace for organisational purposes. It does NOT
# receive `self` or `cls` automatically — use it for utility/helper
# logic that is related to the class but doesn't need instance or
# class data.

class IRCTCTicket:
    """Represents a single train ticket booking."""

    def __init__(self, passenger, fare):
        self.passenger = passenger
        self._fare = fare  # underscore = "private by convention"

    @staticmethod
    def is_valid_pnr(pnr):
        """Utility check — doesn't need self or cls at all."""
        return len(pnr) == 10 and pnr.isdigit()


print(IRCTCTicket.is_valid_pnr("2451236789"))   # Output: True
print(IRCTCTicket.is_valid_pnr("ABC123"))       # Output: False

# Static methods can also be called on an instance (same result):
sample_ticket = IRCTCTicket("Sanjay Verma", 850)
print(sample_ticket.is_valid_pnr("1234567890"))  # Output: True

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2 — @classmethod
# ════════════════════════════════════════════════════════════════
#
# A class method receives `cls` (the class itself) as its first
# argument instead of `self`. The most common use is an ALTERNATE
# CONSTRUCTOR — a different way to build an instance of the class.

class SwiggyOrder:
    """Represents a food order placed on Swiggy."""

    GST_RATE = 0.05  # class variable — shared across all instances

    def __init__(self, customer, base_price):
        self.customer = customer
        self.base_price = base_price

    @classmethod
    def from_combo_deal(cls, customer, combo_name):
        """Alternate constructor: build an order from a fixed combo menu."""
        combo_prices = {
            "student_thali": 149,
            "family_pack": 599,
            "biryani_special": 249,
        }
        price = combo_prices.get(combo_name, 199)  # default price if unknown
        return cls(customer, price)  # cls(...) instead of SwiggyOrder(...)

    def total_with_gst(self):
        return round(self.base_price * (1 + self.GST_RATE), 2)


regular_order = SwiggyOrder("Priya", 400)
combo_order = SwiggyOrder.from_combo_deal("Arjun", "biryani_special")

print(f"{regular_order.customer} pays Rs.{regular_order.total_with_gst()}")
print(f"{combo_order.customer} pays Rs.{combo_order.total_with_gst()}")
# Output: Priya pays Rs.420.0
# Output: Arjun pays Rs.261.45

print("-" * 50)

# ── Why cls(...) instead of ClassName(...)? Subclass safety ──

class SwiggyPremiumOrder(SwiggyOrder):
    """A subclass that adds free delivery — GST rate stays the same."""
    GST_RATE = 0.05

    def total_with_gst(self):
        base_total = super().total_with_gst()
        return base_total  # premium members get free delivery (no add-on fee)


premium_combo = SwiggyPremiumOrder.from_combo_deal("Meera", "family_pack")
print(type(premium_combo).__name__)   # Output: SwiggyPremiumOrder
# Because from_combo_deal used cls(...), calling it on the SUBCLASS
# correctly returns a SwiggyPremiumOrder, not a plain SwiggyOrder.

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3 — @property
# ════════════════════════════════════════════════════════════════
#
# @property turns a method into something that is READ like a plain
# attribute — no parentheses at the call site. This is useful for
# computed values that should always stay in sync with the object's
# real data (like a GST-inclusive fare computed from a base fare).

class IRCTCTicketWithFare(IRCTCTicket):
    """Extends IRCTCTicket with a computed, GST-inclusive fare."""

    @property
    def fare_with_gst(self):
        """Read-only computed attribute: base fare + 5% GST."""
        return round(self._fare * 1.05, 2)


ticket = IRCTCTicketWithFare("Riya Deshmukh", 850)
print(ticket.fare_with_gst)      # Output: 892.5   <- no parentheses!

print("-" * 50)

# ── @property with a matching setter, for controlled writes ──
#
# By default, a @property is read-only. Adding a matching
# @<name>.setter lets you write to it too, WHILE still validating
# the incoming value — something a plain public attribute can't do.

class BankAccount:
    """A simple account with a validated, property-protected balance."""

    def __init__(self, owner, starting_balance=0):
        self.owner = owner
        self._balance = starting_balance  # "private" backing field

    @property
    def balance(self):
        """Getter — read the current balance like a normal attribute."""
        return self._balance

    @balance.setter
    def balance(self, new_value):
        """Setter — validates before allowing a write to `balance`."""
        if new_value < 0:
            raise ValueError("Balance cannot be set to a negative value")
        self._balance = new_value


account = BankAccount("Sanjay Verma", starting_balance=1000)
print(account.balance)     # Output: 1000   (calls the getter)

account.balance = 1500     # calls the setter
print(account.balance)     # Output: 1500

try:
    account.balance = -200  # setter rejects this
except ValueError as error:
    print(f"Rejected: {error}")
# Output: Rejected: Balance cannot be set to a negative value

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — 4 progressively complex worked examples
# ════════════════════════════════════════════════════════════════

# --- Example 1: combining all three decorators in one class ---

class FlipkartProduct:
    """Demonstrates @staticmethod, @classmethod, and @property together."""

    PLATFORM_FEE = 20  # class variable

    def __init__(self, name, price, discount_percent=0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    @staticmethod
    def is_valid_discount(percent):
        """Utility check — no self/cls needed."""
        return 0 <= percent <= 90

    @classmethod
    def from_flash_sale(cls, name, price):
        """Alternate constructor: flash sale items always get 30% off."""
        return cls(name, price, discount_percent=30)

    @property
    def final_price(self):
        """Computed, read-only final price after discount + platform fee."""
        discounted = self.price * (1 - self.discount_percent / 100)
        return round(discounted + self.PLATFORM_FEE, 2)


print(FlipkartProduct.is_valid_discount(30))    # Output: True
print(FlipkartProduct.is_valid_discount(150))   # Output: False

flash_item = FlipkartProduct.from_flash_sale("Wireless Mouse", 999)
print(f"{flash_item.name}: Rs.{flash_item.final_price}")
# Output: Wireless Mouse: Rs.719.3

print("-" * 50)

# --- Example 2: @property for a derived / formatted display value ---

class StudentProfile:
    """Uses @property to expose a formatted display name."""

    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name} ({self.city})"


student = StudentProfile("Riya", "Deshmukh", "Pune")
print(student.display_name)
# Output: Riya Deshmukh (Pune)

print("-" * 50)

# --- Example 3: @classmethod tracking class-level state ---

class RegisteredStudent:
    """Uses a classmethod + class variable to count all instances."""
    total_registered = 0

    def __init__(self, name):
        self.name = name
        RegisteredStudent.total_registered += 1

    @classmethod
    def get_total_registered(cls):
        return cls.total_registered


RegisteredStudent("Priya")
RegisteredStudent("Arjun")
RegisteredStudent("Meera")
print(RegisteredStudent.get_total_registered())
# Output: 3

print("-" * 50)

# --- Example 4: static method used as a reusable validator across a module ---

class PaytmTransaction:
    """Uses a staticmethod validator shared by multiple methods."""

    def __init__(self, amount, upi_id):
        if not self.is_valid_upi(upi_id):
            raise ValueError(f"Invalid UPI ID: {upi_id}")
        self.amount = amount
        self.upi_id = upi_id

    @staticmethod
    def is_valid_upi(upi_id):
        return "@" in upi_id and len(upi_id.split("@")) == 2


txn = PaytmTransaction(500, "priya.sharma@okhdfcbank")
print(f"Transaction of Rs.{txn.amount} to {txn.upi_id} created")
# Output: Transaction of Rs.500 to priya.sharma@okhdfcbank created

try:
    PaytmTransaction(500, "not-a-valid-id")
except ValueError as error:
    print(f"Blocked: {error}")
# Output: Blocked: Invalid UPI ID: not-a-valid-id

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
#
# Complete the `Rectangle` class below so that:
#   - `area` is a read-only @property (width * height)
#   - `is_square` is a read-only @property (True if width == height)
#   - `from_square(side)` is a @classmethod alternate constructor
#     that builds a Rectangle with width == height == side
#
# Expected output:
#   24
#   False
#   25
#   True

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # YOUR CODE HERE
    @property
    def area(self):
        return self.width * self.height

    @property
    def is_square(self):
        return self.width == self.height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)


rect = Rectangle(4, 6)
print(rect.area)         # Expected: 24
print(rect.is_square)    # Expected: False

square = Rectangle.from_square(5)
print(square.area)       # Expected: 25
print(square.is_square)  # Expected: True


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - @staticmethod: a utility function living inside a class; no
#     self or cls
#   - @classmethod: receives cls, most often used for alternate
#     constructors that must respect subclassing (cls(...) not
#     ClassName(...))
#   - @property: makes a method readable like a plain attribute;
#     pair with @<name>.setter for validated writes
#
# This wraps up Day 14 — Decorators & Closures.
# Next: Day 15 — Functional Programming (map, filter, reduce, lambda,
# zip, enumerate, sorted with key=) — which builds directly on the
# first-class-function foundation from File 1.

if __name__ == "__main__":
    print("\nDay 14, File 3 complete — built-in decorators.")
