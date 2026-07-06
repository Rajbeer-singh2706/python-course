"""
Day 17 — Advanced OOP
File 4 of 4: The @dataclass Decorator

What this file covers:
    - The boilerplate problem with regular classes for simple data
    - `@dataclass` — auto-generated __init__, __repr__, __eq__
    - Default values and `field(default_factory=...)`
    - `frozen=True` for immutable dataclasses
    - `order=True` for automatic comparison operators
    - `__post_init__` for validation after construction

Prerequisites:
    - day17_01_abstract_base_classes.py
    - Day 10-11 (OOP I & II)

How to run:
    python day17_04_dataclasses.py
"""

from dataclasses import dataclass, field, FrozenInstanceError


# ════════════════════════════════════════════════════════
# SECTION 1: The Boilerplate Problem
# ════════════════════════════════════════════════════════
#
# Consider a simple "Passenger" record for an IRCTC booking system.
# Writing it the OLD way (Day 10 style) means manually writing
# __init__, __repr__, and __eq__ — a lot of repetitive code just
# to hold a few pieces of data.

class PassengerOldStyle:
    def __init__(self, name, age, seat):
        self.name = name
        self.age = age
        self.seat = seat

    def __repr__(self):
        return f"PassengerOldStyle(name={self.name!r}, age={self.age!r}, seat={self.seat!r})"

    def __eq__(self, other):
        if not isinstance(other, PassengerOldStyle):
            return NotImplemented
        return (self.name, self.age, self.seat) == (other.name, other.age, other.seat)


p1 = PassengerOldStyle("Arjun Mehta", 29, "B2-45")
print(p1)
# Output:
# PassengerOldStyle(name='Arjun Mehta', age=29, seat='B2-45')

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: The Same Class with @dataclass
# ════════════════════════════════════════════════════════
#
# @dataclass auto-generates __init__, __repr__, and __eq__ for you,
# based purely on the class-level type-annotated attributes.

@dataclass
class Passenger:
    name: str
    age: int
    seat: str


p2 = Passenger("Arjun Mehta", 29, "B2-45")
print(p2)
# Output:
# Passenger(name='Arjun Mehta', age=29, seat='B2-45')

p3 = Passenger("Arjun Mehta", 29, "B2-45")
print(f"p2 == p3 -> {p2 == p3}")
# Output:
# p2 == p3 -> True

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 3: Default Values and default_factory
# ════════════════════════════════════════════════════════
#
# Simple defaults work like normal function defaults. But MUTABLE
# defaults (lists, dicts) need `field(default_factory=...)` — using
# a plain mutable default is a classic Python bug (shared state
# across all instances) and @dataclass forbids it outright.

@dataclass
class TrainTicket:
    passenger_name: str
    train_number: str = "12951"          # simple default
    coach: str = "AC2"                    # simple default
    co_passengers: list = field(default_factory=list)  # mutable default


ticket_a = TrainTicket("Priya Sharma")
ticket_a.co_passengers.append("Meera Iyer")

ticket_b = TrainTicket("Sanjay Verma")

print(f"ticket_a co-passengers: {ticket_a.co_passengers}")
print(f"ticket_b co-passengers: {ticket_b.co_passengers}")
# Output:
# ticket_a co-passengers: ['Meera Iyer']
# ticket_b co-passengers: []
# (Each instance gets its OWN list — no shared state!)

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 4: frozen=True — Immutable Dataclasses
# ════════════════════════════════════════════════════════

@dataclass(frozen=True)
class GSTInvoiceLine:
    item_name: str
    price: float
    gst_percent: float = 18.0


line = GSTInvoiceLine("Wireless Mouse", 799.0)
print(line)

try:
    line.price = 999.0  # not allowed — frozen!
except FrozenInstanceError as error:
    print(f"Cannot modify frozen dataclass -> {error}")
# Output:
# GSTInvoiceLine(item_name='Wireless Mouse', price=799.0, gst_percent=18.0)
# Cannot modify frozen dataclass -> cannot assign to field 'price'

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 5: order=True — Automatic Comparison Operators
# ════════════════════════════════════════════════════════

@dataclass(order=True)
class Order:
    priority: int
    order_id: str = field(compare=False)  # excluded from comparisons


order1 = Order(priority=2, order_id="SWG-101")
order2 = Order(priority=1, order_id="SWG-102")

print(f"order1 < order2 -> {order1 < order2}")
print(f"sorted priorities: {[o.priority for o in sorted([order1, order2])]}")
# Output:
# order1 < order2 -> False
# sorted priorities: [1, 2]

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 6: __post_init__ — Validation After Construction
# ════════════════════════════════════════════════════════

@dataclass
class BankTransfer:
    sender: str
    receiver: str
    amount: float

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Transfer amount must be positive")


transfer = BankTransfer("Riya Deshmukh", "Sanjay Verma", 5000.0)
print(transfer)

try:
    bad_transfer = BankTransfer("Riya Deshmukh", "Sanjay Verma", -100.0)
except ValueError as error:
    print(f"Transfer rejected -> {error}")
# Output:
# BankTransfer(sender='Riya Deshmukh', receiver='Sanjay Verma', amount=5000.0)
# Transfer rejected -> Transfer amount must be positive

print("-" * 50)


# ════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════

# ── Example 1: A dataclass with a computed property ──
@dataclass
class Product:
    name: str
    price: float
    quantity: int

    @property
    def subtotal(self) -> float:
        return self.price * self.quantity


product = Product("Notebook", 45.0, 3)
print(f"{product.name} subtotal: Rs. {product.subtotal}")
# Output:
# Notebook subtotal: Rs. 135.0

print("-" * 50)


# ── Example 2: Nesting dataclasses ──
@dataclass
class Address:
    city: str
    pincode: str


@dataclass
class Customer:
    name: str
    address: Address


customer = Customer("Meera Iyer", Address("Chennai", "600001"))
print(customer)
print(f"City: {customer.address.city}")
# Output:
# Customer(name='Meera Iyer', address=Address(city='Chennai', pincode='600001'))
# City: Chennai

print("-" * 50)


# ── Example 3: Converting a dataclass to a dict ──
from dataclasses import asdict

order_dict = asdict(Order(priority=3, order_id="SWG-205"))
print(order_dict)
# Output:
# {'priority': 3, 'order_id': 'SWG-205'}

print("-" * 50)


# ── Example 4: field with repr=False to hide sensitive data ──
@dataclass
class UserAccount:
    username: str
    password: str = field(repr=False)


account = UserAccount("arjun_m", "supersecret123")
print(account)
# Output:
# UserAccount(username='arjun_m')

print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Create a frozen, order-able dataclass `Coupon` with fields:
#   - code: str
#   - discount_percent: float
#   - min_order_value: float = 0.0
#
# Add a __post_init__ that raises a ValueError if discount_percent
# is not between 0 and 100.
#
# Create two Coupon instances and print whichever one has the
# HIGHER discount_percent using max().
#
# Expected output:
# Coupon(discount_percent=50.0, code='FESTIVE50', min_order_value=500.0)

# YOUR CODE HERE


# SOLUTION:
# @dataclass(frozen=True, order=True)
# class Coupon:
#     discount_percent: float
#     code: str = field(compare=False)
#     min_order_value: float = field(default=0.0, compare=False)
#
#     def __post_init__(self):
#         if not (0 <= self.discount_percent <= 100):
#             raise ValueError("discount_percent must be between 0 and 100")
#
#
# coupon1 = Coupon(discount_percent=10.0, code="SAVE10", min_order_value=200.0)
# coupon2 = Coupon(discount_percent=50.0, code="FESTIVE50", min_order_value=500.0)
# print(max(coupon1, coupon2))


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# In this file you learned:
#   - @dataclass eliminates __init__/__repr__/__eq__ boilerplate
#   - field(default_factory=...) safely handles mutable defaults
#   - frozen=True makes instances immutable
#   - order=True auto-generates comparison operators
#   - __post_init__ runs validation right after construction
#   - asdict() converts a dataclass instance into a plain dict
#
# This wraps up Day 17 — Advanced OOP! You've now covered
# abstract base classes, metaclasses, protocols, and dataclasses —
# the four pillars of professional-level Python class design.
# Next up: Day 18 — Type Hints & Static Analysis.
