"""
Day 17 — Advanced OOP
File 3 of 4: Protocol Classes (Structural Subtyping)

What this file covers:
    - "Duck typing" and why Python cares about behavior, not ancestry
    - `typing.Protocol` — defining a shape without forcing inheritance
    - The difference between ABC (nominal typing) and
      Protocol (structural typing)
    - `@runtime_checkable` for isinstance() checks against a Protocol
    - When to prefer Protocol over ABC

Prerequisites:
    - day17_01_abstract_base_classes.py (same day, file 1)
    - Day 18 will cover type hints in more depth — this file uses
      just enough typing syntax to demonstrate Protocol

How to run:
    python day17_03_protocol_classes.py
"""

from typing import Protocol, runtime_checkable


# ════════════════════════════════════════════════════════
# SECTION 1: The Problem — ABC Forces Inheritance
# ════════════════════════════════════════════════════════
#
# With ABCs (file 1), a class MUST explicitly inherit from the
# abstract base to be recognized as "one of its kind". But what if
# you have classes from different, unrelated parts of your codebase
# that all happen to support the same method — without wanting to
# share a common ancestor? That's where Protocol comes in.
#
# Protocol uses STRUCTURAL typing ("if it walks like a duck and
# quacks like a duck, it's a duck") instead of NOMINAL typing
# ("it's a duck only if it inherits from Duck").


# ── Concept: Defining a Protocol ──
class Invoiceable(Protocol):
    """Any object with a total() method returning a float qualifies —
    no inheritance required."""

    def total(self) -> float:
        ...


# ── Concept: Classes that satisfy the Protocol WITHOUT inheriting it ──
class SwiggyOrder:
    def __init__(self, food_cost, delivery_fee):
        self.food_cost = food_cost
        self.delivery_fee = delivery_fee

    def total(self) -> float:
        return self.food_cost + self.delivery_fee


class FlipkartCart:
    def __init__(self, items_price, gst):
        self.items_price = items_price
        self.gst = gst

    def total(self) -> float:
        return self.items_price + self.gst


def print_invoice(item: Invoiceable) -> None:
    """Type-checkers (e.g. mypy) accept ANY object with total() here,
    even though neither SwiggyOrder nor FlipkartCart inherits Invoiceable."""
    print(f"Invoice total: Rs. {item.total()}")


order = SwiggyOrder(food_cost=450, delivery_fee=40)
cart = FlipkartCart(items_price=2999, gst=150)

print_invoice(order)
print_invoice(cart)
# Output:
# Invoice total: Rs. 490
# Invoice total: Rs. 3149

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: @runtime_checkable — isinstance() with Protocols
# ════════════════════════════════════════════════════════
#
# By default, Protocols only help STATIC type checkers like mypy.
# To use them with `isinstance()` at runtime, mark them
# `@runtime_checkable`.

@runtime_checkable
class Trackable(Protocol):
    def track(self) -> str:
        ...


class IRCTCShipment:
    def track(self) -> str:
        return "Train PNR confirmed, seat allotted"


class LooseObject:
    """Has no track() method at all."""
    pass


shipment = IRCTCShipment()
loose = LooseObject()

print(f"shipment satisfies Trackable? {isinstance(shipment, Trackable)}")
print(f"loose satisfies Trackable?    {isinstance(loose, Trackable)}")
# Output:
# shipment satisfies Trackable? True
# loose satisfies Trackable?    False

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 3: Protocol vs ABC — Side by Side
# ════════════════════════════════════════════════════════
#
#   ABC (nominal typing)              Protocol (structural typing)
#   -----------------------------     -----------------------------
#   Subclass MUST inherit             No inheritance needed at all
#   Good for a shared library of      Good for "any object that
#   related, cooperating classes      happens to have this shape"
#   Enforced at OBJECT CREATION       Enforced by type checkers
#   time (TypeError if incomplete)    (and optionally isinstance())

print("See comment block above for the ABC vs Protocol comparison table")
print("-" * 50)


# ════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════

# ── Example 1: A "Discountable" Protocol used across unrelated classes ──
@runtime_checkable
class Discountable(Protocol):
    def apply_discount(self, percent: float) -> float:
        ...


class Laptop:
    def __init__(self, price):
        self.price = price

    def apply_discount(self, percent: float) -> float:
        return self.price * (1 - percent / 100)


class TrainTicket:
    def __init__(self, fare):
        self.fare = fare

    def apply_discount(self, percent: float) -> float:
        return self.fare * (1 - percent / 100)


items = [Laptop(60000), TrainTicket(1200)]
for thing in items:
    discounted = thing.apply_discount(10)
    print(f"{type(thing).__name__} after 10% discount: Rs. {discounted}")
# Output:
# Laptop after 10% discount: Rs. 54000.0
# TrainTicket after 10% discount: Rs. 1080.0

print("-" * 50)


# ── Example 2: Protocol with multiple required methods ──
class Playable(Protocol):
    def play(self) -> str:
        ...

    def pause(self) -> str:
        ...


class MusicTrack:
    def play(self) -> str:
        return "Playing song"

    def pause(self) -> str:
        return "Song paused"


def control_media(media: Playable) -> None:
    print(media.play())
    print(media.pause())


control_media(MusicTrack())
# Output:
# Playing song
# Song paused

print("-" * 50)


# ── Example 3: A function accepting "anything with a name attribute" ──
class HasName(Protocol):
    name: str


class Passenger:
    def __init__(self, name):
        self.name = name


class Driver:
    def __init__(self, name):
        self.name = name


def greet(entity: HasName) -> str:
    return f"Namaste, {entity.name}!"


print(greet(Passenger("Riya Deshmukh")))
print(greet(Driver("Sanjay Verma")))
# Output:
# Namaste, Riya Deshmukh!
# Namaste, Sanjay Verma!

print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Define a runtime_checkable Protocol called `Refundable` with one
# method: refund(self) -> str
#
# Create two UNRELATED classes (no shared base class) that both
# implement refund():
#   - `MetroCardTopUp` -> refund() returns "Rs. 200 refunded to metro card"
#   - `MovieTicket`     -> refund() returns "Rs. 350 refunded to wallet"
#
# Loop over instances of both and print isinstance(x, Refundable)
# followed by x.refund() for each.
#
# Expected output:
# True
# Rs. 200 refunded to metro card
# True
# Rs. 350 refunded to wallet

# YOUR CODE HERE


# SOLUTION:
# @runtime_checkable
# class Refundable(Protocol):
#     def refund(self) -> str:
#         ...
#
#
# class MetroCardTopUp:
#     def refund(self) -> str:
#         return "Rs. 200 refunded to metro card"
#
#
# class MovieTicket:
#     def refund(self) -> str:
#         return "Rs. 350 refunded to wallet"
#
#
# for refundable_item in [MetroCardTopUp(), MovieTicket()]:
#     print(isinstance(refundable_item, Refundable))
#     print(refundable_item.refund())


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Protocol enables structural typing — no inheritance required
#   - @runtime_checkable allows isinstance() checks against a Protocol
#   - ABC = nominal typing (must inherit); Protocol = structural
#     typing (must just have the right shape)
#   - Protocols can require methods, multiple methods, or attributes
#
# Next up: day17_04_dataclasses.py — the @dataclass decorator for
# clean, boilerplate-free data-holding classes!
