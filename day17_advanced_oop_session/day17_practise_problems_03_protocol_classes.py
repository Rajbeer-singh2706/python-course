"""
Day 17 — Advanced OOP — Practice Problem Set
File 3 of 4: Section D (Protocol Classes)

Difficulty legend:
    🟢 Warm-up   — should feel comfortable
    🟡 Core      — the day's main concept, applied directly
    🔴 Challenge — combines multiple ideas or edge cases

Section index (this file):
    D — Protocol Classes (4 problems)

How to run:
    python day17_practise_problems_03_protocol_classes.py
"""

from typing import Protocol, runtime_checkable


# ════════════════════════════════════════════════════════
# SECTION D — Protocol Classes
# ════════════════════════════════════════════════════════

# ── D1. 🟢 Warm-up — A basic Protocol ──
# Define a Protocol `HasArea` with a method `area(self) -> float`.
# Create a class `Square` (no inheritance from HasArea) with a
# `side` attribute and an `area()` method returning side ** 2.
# Write a function `print_area(shape: HasArea)` that prints
# f"Area: {shape.area()}" and call it with Square with side=4.
#
# Expected output:
# Area: 16

# YOUR CODE HERE


# SOLUTION:
# class HasArea(Protocol):
#     def area(self) -> float:
#         ...
#
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self) -> float:
#         return self.side ** 2
#
#
# def print_area(shape: HasArea) -> None:
#     print(f"Area: {shape.area()}")
#
#
# print_area(Square(side=4))

print("-" * 50)


# ── D2. 🟢 Warm-up — runtime_checkable isinstance ──
# Define a runtime_checkable Protocol `Closeable` with a method
# `close(self) -> None`. Create a class `FileHandle` with a
# `close()` method (just `pass` inside), and a class `PlainObject`
# with no close() method at all. Print isinstance() results for
# both against Closeable.
#
# Expected output:
# True
# False

# YOUR CODE HERE


# SOLUTION:
# @runtime_checkable
# class Closeable(Protocol):
#     def close(self) -> None:
#         ...
#
#
# class FileHandle:
#     def close(self) -> None:
#         pass
#
#
# class PlainObject:
#     pass
#
#
# print(isinstance(FileHandle(), Closeable))
# print(isinstance(PlainObject(), Closeable))

print("-" * 50)


# ── D3. 🟡 Core — Protocol with an attribute requirement ──
# Define a Protocol `HasCity` with a plain attribute `city: str`
# (no methods). Create two unrelated classes `Warehouse` and
# `Store`, both with a `city` attribute set in __init__. Write a
# function `same_city(a: HasCity, b: HasCity) -> bool` that returns
# a.city == b.city. Test with Warehouse("Pune") and Store("Pune").
#
# Expected output:
# True

# YOUR CODE HERE


# SOLUTION:
# class HasCity(Protocol):
#     city: str
#
#
# class Warehouse:
#     def __init__(self, city):
#         self.city = city
#
#
# class Store:
#     def __init__(self, city):
#         self.city = city
#
#
# def same_city(a: HasCity, b: HasCity) -> bool:
#     return a.city == b.city
#
#
# print(same_city(Warehouse("Pune"), Store("Pune")))

print("-" * 50)


# ── D4. 🔴 Challenge — Protocol vs ABC comparison in one script ──
# Create BOTH:
#   1. An ABC `Vehicle` (from abc import ABC, abstractmethod) with
#      abstract method `move(self) -> str`, and a subclass
#      `Scooter(Vehicle)` implementing move() -> "Scooter zooms off"
#   2. A runtime_checkable Protocol `Movable` with method
#      `move(self) -> str`
# Show that `Scooter` satisfies BOTH: print isinstance(scooter, Vehicle)
# and isinstance(scooter, Movable) — even though Scooter never
# explicitly inherited from Movable.
#
# Expected output:
# True
# True

# YOUR CODE HERE


# SOLUTION:
# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self) -> str:
#         pass
#
#
# class Scooter(Vehicle):
#     def move(self) -> str:
#         return "Scooter zooms off"
#
#
# @runtime_checkable
# class Movable(Protocol):
#     def move(self) -> str:
#         ...
#
#
# scooter = Scooter()
# print(isinstance(scooter, Vehicle))
# print(isinstance(scooter, Movable))

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   D — Protocol Classes (4 problems)
#
# Difficulty breakdown: 2x 🟢 Warm-up, 1x 🟡 Core, 1x 🔴 Challenge
#
# Next file: day17_practise_problems_04_dataclasses.py
# (Section E — dataclasses, plus Mixed Challenges covering the
# whole of Day 17)
