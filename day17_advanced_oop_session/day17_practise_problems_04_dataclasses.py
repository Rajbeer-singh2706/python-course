"""
Day 17 — Advanced OOP — Practice Problem Set
File 4 of 4: Section E (dataclasses) + Section F (Mixed Challenges)

Difficulty legend:
    🟢 Warm-up   — should feel comfortable
    🟡 Core      — the day's main concept, applied directly
    🔴 Challenge — combines multiple ideas or edge cases

Section index (this file):
    E — @dataclass Decorator (4 problems)
    F — Mixed Challenges combining ABC + Protocol + dataclass +
        prior-day concepts (2 problems)

How to run:
    python day17_practise_problems_04_dataclasses.py
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# ════════════════════════════════════════════════════════
# SECTION E — @dataclass Decorator
# ════════════════════════════════════════════════════════

# ── E1. 🟢 Warm-up — Basic dataclass ──
# Create a @dataclass `Book` with fields `title: str` and
# `price: float`. Create Book("Python Basics", 399.0) and print it.
#
# Expected output:
# Book(title='Python Basics', price=399.0)

# YOUR CODE HERE


# SOLUTION:
# @dataclass
# class Book:
#     title: str
#     price: float
#
#
# print(Book("Python Basics", 399.0))

print("-" * 50)


# ── E2. 🟡 Core — default_factory for mutable defaults ──
# Create a @dataclass `ShoppingCart` with fields `owner: str` and
# `items: list = field(default_factory=list)`. Create two separate
# carts, add "Rice" to the first cart's items only, and print both
# carts' items lists to prove they don't share state.
#
# Expected output:
# ['Rice']
# []

# YOUR CODE HERE


# SOLUTION:
# @dataclass
# class ShoppingCart:
#     owner: str
#     items: list = field(default_factory=list)
#
#
# cart1 = ShoppingCart("Priya")
# cart2 = ShoppingCart("Arjun")
# cart1.items.append("Rice")
# print(cart1.items)
# print(cart2.items)

print("-" * 50)


# ── E3. 🟡 Core — frozen dataclass ──
# Create a frozen @dataclass `PinCode` with a single field
# `code: str`. Try to reassign pincode.code after creation inside a
# try/except block, printing "Cannot modify PinCode" if it fails.
#
# Expected output:
# Cannot modify PinCode

# YOUR CODE HERE


# SOLUTION:
# from dataclasses import FrozenInstanceError
#
#
# @dataclass(frozen=True)
# class PinCode:
#     code: str
#
#
# pincode = PinCode("411001")
# try:
#     pincode.code = "411002"
# except FrozenInstanceError:
#     print("Cannot modify PinCode")

print("-" * 50)


# ── E4. 🔴 Challenge — __post_init__ validation + order=True ──
# Create a dataclass `ExamScore` with `order=True`, fields
# `marks: int` and `student: str = field(compare=False)`.
# Add __post_init__ that raises ValueError if marks is not between
# 0 and 100. Create two valid ExamScore instances and print the
# `student` name of whichever has the higher marks using max().
#
# Expected output:
# Arjun Mehta

# YOUR CODE HERE


# SOLUTION:
# @dataclass(order=True)
# class ExamScore:
#     marks: int
#     student: str = field(compare=False)
#
#     def __post_init__(self):
#         if not (0 <= self.marks <= 100):
#             raise ValueError("marks must be between 0 and 100")
#
#
# score1 = ExamScore(marks=78, student="Priya Sharma")
# score2 = ExamScore(marks=91, student="Arjun Mehta")
# print(max(score1, score2).student)

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION F — Mixed Challenges (Day 17 + Prior Days)
# ════════════════════════════════════════════════════════

# ── F1. 🔴 Challenge — ABC + dataclass together ──
# Create an ABC `Notification` with abstract method
# `render(self) -> str`. Create a @dataclass subclass `SMSAlert`
# (must combine @dataclass with ABC inheritance) with fields
# `phone: str` and `message: str`, implementing render() as
# f"SMS to {self.phone}: {self.message}". Instantiate it with
# phone="9876543210", message="Your order has shipped" and print
# both the dataclass repr AND render().
#
# Expected output:
# SMSAlert(phone='9876543210', message='Your order has shipped')
# SMS to 9876543210: Your order has shipped

# YOUR CODE HERE


# SOLUTION:
# class Notification(ABC):
#     @abstractmethod
#     def render(self) -> str:
#         pass
#
#
# @dataclass
# class SMSAlert(Notification):
#     phone: str
#     message: str
#
#     def render(self) -> str:
#         return f"SMS to {self.phone}: {self.message}"
#
#
# alert = SMSAlert(phone="9876543210", message="Your order has shipped")
# print(alert)
# print(alert.render())

print("-" * 50)


# ── F2. 🔴 Challenge — Protocol + list comprehension (Day 6) + sorted() (Day 15) ──
# Define a runtime_checkable Protocol `HasWeight` with attribute
# `weight_kg: float`. Create a @dataclass `Parcel` with fields
# `tracking_id: str` and `weight_kg: float`. Given a list of three
# Parcel instances:
#   Parcel("PCL1", 2.5), Parcel("PCL2", 0.8), Parcel("PCL3", 5.1)
# use a list comprehension + sorted(key=...) (Day 15 concept) to
# print the tracking_id values ordered from LIGHTEST to HEAVIEST.
#
# Expected output:
# ['PCL2', 'PCL1', 'PCL3']

# YOUR CODE HERE


# SOLUTION:
# @runtime_checkable
# class HasWeight(Protocol):
#     weight_kg: float
#
#
# @dataclass
# class Parcel:
#     tracking_id: str
#     weight_kg: float
#
#
# parcels = [Parcel("PCL1", 2.5), Parcel("PCL2", 0.8), Parcel("PCL3", 5.1)]
# lightest_to_heaviest = [p.tracking_id for p in sorted(parcels, key=lambda p: p.weight_kg)]
# print(lightest_to_heaviest)

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   E — @dataclass Decorator (4 problems)
#   F — Mixed Challenges: ABC + Protocol + dataclass +
#       prior-day concepts (2 problems)
#
# Difficulty breakdown: 1x 🟢 Warm-up, 3x 🟡 Core, 2x 🔴 Challenge
#
# ════════════════════════════════════════════════════════
# DAY 17 PROBLEM SET — FULL SUMMARY (all 4 files)
# ════════════════════════════════════════════════════════
#   File 1 — Section A (Prior Review, 2) + Section B (ABC, 4)       = 6
#   File 2 — Section C (Metaclasses, 4)                             = 4
#   File 3 — Section D (Protocol Classes, 4)                        = 4
#   File 4 — Section E (dataclasses, 4) + Section F (Mixed, 2)      = 6
#   TOTAL                                                           = 20
#
# Next up: Day 18 — Type Hints & Static Analysis
