"""
Day 17 — Advanced OOP — Practice Problem Set
File 1 of 4: Section A (Prior Days Review) + Section B (Abstract Base Classes)

Day 17 topic: Advanced OOP — Abstract Base Classes, Metaclasses,
Protocol classes, and @dataclass.

Cumulative scope: Days 1-17 (functions, data structures, OOP I & II,
iterators/generators, decorators, concurrency, and now advanced OOP).

Difficulty legend:
    🟢 Warm-up   — should feel comfortable
    🟡 Core      — the day's main concept, applied directly
    🔴 Challenge — combines multiple ideas or edge cases

Section index (this file):
    A — Prior Days Review (2 problems)
    B — Abstract Base Classes (4 problems)

How to run:
    python day17_practise_problems_01_abstract_base_classes.py
"""

from abc import ABC, abstractmethod


# ════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════

# ── A1. 🟢 Warm-up — Decorators (Day 14) ──
# Write a decorator `announce` that prints "Starting..." before
# calling the wrapped function and "Done!" after it returns.
# Apply it to a function `book_ticket(name)` that prints
# f"Ticket booked for {name}" and call it with "Priya Sharma".
#
# Expected output:
# Starting...
# Ticket booked for Priya Sharma
# Done!

# YOUR CODE HERE


# SOLUTION:
# def announce(func):
#     def wrapper(*args, **kwargs):
#         print("Starting...")
#         result = func(*args, **kwargs)
#         print("Done!")
#         return result
#     return wrapper
#
#
# @announce
# def book_ticket(name):
#     print(f"Ticket booked for {name}")
#
#
# book_ticket("Priya Sharma")

print("-" * 50)


# ── A2. 🟢 Warm-up — Generators (Day 13) ──
# Write a generator function `even_numbers(limit)` that yields even
# numbers from 2 up to (and including) `limit`. Use it to print
# all even numbers up to 10, space-separated on one line.
#
# Expected output:
# 2 4 6 8 10

# YOUR CODE HERE


# SOLUTION:
# def even_numbers(limit):
#     for n in range(2, limit + 1, 2):
#         yield n
#
#
# print(*even_numbers(10))

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION B — Abstract Base Classes
# ════════════════════════════════════════════════════════

# ── B1. 🟢 Warm-up — Basic ABC ──
# Create an abstract base class `Shape` with an abstract method
# `area(self)`. Try instantiating `Shape()` directly inside a
# try/except TypeError block and print "Shape cannot be instantiated"
# if it fails.
#
# Expected output:
# Shape cannot be instantiated

# YOUR CODE HERE


# SOLUTION:
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# try:
#     Shape()
# except TypeError:
#     print("Shape cannot be instantiated")

print("-" * 50)


# ── B2. 🟢 Warm-up — Implementing an ABC ──
# Using the `Shape` ABC above (redefine it here), create a subclass
# `Circle` that takes `radius` and implements area() as
# 3.14 * radius ** 2. Create Circle(radius=5) and print its area.
#
# Expected output:
# 78.5

# YOUR CODE HERE


# SOLUTION:
# class ShapeB2(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Circle(ShapeB2):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# print(Circle(radius=5).area())

print("-" * 50)


# ── B3. 🟡 Core — ABC with a concrete (shared) method ──
# Create an ABC `Employee` with:
#   - abstract method `calculate_salary(self)`
#   - a concrete method `describe(self)` returning
#     f"{self.name} works in {self.department}"
# Create a subclass `Manager(name, department, base, bonus)` where
# calculate_salary() returns base + bonus.
# Instantiate Manager("Meera Iyer", "Sales", 60000, 15000) and
# print describe() then calculate_salary().
#
# Expected output:
# Meera Iyer works in Sales
# 75000

# YOUR CODE HERE


# SOLUTION:
# class EmployeeB4(ABC):
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department
#
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
#     def describe(self):
#         return f"{self.name} works in {self.department}"
#
#
# class Manager(EmployeeB4):
#     def __init__(self, name, department, base, bonus):
#         super().__init__(name, department)
#         self.base = base
#         self.bonus = bonus
#
#     def calculate_salary(self):
#         return self.base + self.bonus
#
#
# manager = Manager("Meera Iyer", "Sales", 60000, 15000)
# print(manager.describe())
# print(manager.calculate_salary())

print("-" * 50)


# ── B4. 🔴 Challenge — ABC + isinstance() polymorphism ──
# Create an ABC `Discount` with abstract method `apply(self, price)`.
# Create subclasses:
#   - `FlatDiscount(amount)` -> apply(price) returns price - amount
#   - `PercentDiscount(percent)` -> apply(price) returns
#     price * (1 - percent / 100)
# Given a list of (Discount instance, price) pairs:
#   [(FlatDiscount(100), 1000), (PercentDiscount(20), 1000)]
# print the discounted price for each, and also print whether each
# discount object isinstance() of Discount.
#
# Expected output:
# 900 True
# 800.0 True

# YOUR CODE HERE


# SOLUTION:
# class Discount(ABC):
#     @abstractmethod
#     def apply(self, price):
#         pass
#
#
# class FlatDiscount(Discount):
#     def __init__(self, amount):
#         self.amount = amount
#
#     def apply(self, price):
#         return price - self.amount
#
#
# class PercentDiscount(Discount):
#     def __init__(self, percent):
#         self.percent = percent
#
#     def apply(self, price):
#         return price * (1 - self.percent / 100)
#
#
# pairs = [(FlatDiscount(100), 1000), (PercentDiscount(20), 1000)]
# for discount_obj, price in pairs:
#     print(discount_obj.apply(price), isinstance(discount_obj, Discount))

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   A — Prior Days Review: decorators, generators (2 problems)
#   B — Abstract Base Classes (4 problems)
#
# Difficulty breakdown: 4x 🟢 Warm-up, 1x 🟡 Core, 1x 🔴 Challenge
#
# Next file: day17_practise_problems_02_metaclasses.py
# (Section C — Metaclasses)
