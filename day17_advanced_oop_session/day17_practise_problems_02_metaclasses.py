"""
Day 17 — Advanced OOP — Practice Problem Set
File 2 of 4: Section C (Metaclasses)

Difficulty legend:
    🟢 Warm-up   — should feel comfortable
    🟡 Core      — the day's main concept, applied directly
    🔴 Challenge — combines multiple ideas or edge cases

Section index (this file):
    C — Metaclasses (4 problems)

How to run:
    python day17_practise_problems_02_metaclasses.py
"""


# ════════════════════════════════════════════════════════
# SECTION C — Metaclasses
# ════════════════════════════════════════════════════════

# ── C1. 🟢 Warm-up — type() of a class ──
# Define a plain class `Ticket` (no special metaclass). Print
# type(Ticket) and type(Ticket()).
#
# Expected output:
# <class 'type'>
# <class '__main__.Ticket'>

# YOUR CODE HERE


# SOLUTION:
# class Ticket:
#     pass
#
#
# print(type(Ticket))
# print(type(Ticket()))

print("-" * 50)


# ── C2. 🟢 Warm-up — Creating a class with type() directly ──
# Use type("Vendor", (object,), {"city": "Delhi"}) to dynamically
# build a class called Vendor. Create an instance and print
# instance.city.
#
# Expected output:
# Delhi

# YOUR CODE HERE


# SOLUTION:
# Vendor = type("Vendor", (object,), {"city": "Delhi"})
# vendor_instance = Vendor()
# print(vendor_instance.city)

print("-" * 50)


# ── C3. 🟡 Core — Singleton metaclass ──
# Write a metaclass `SingletonMeta` (as shown in the concept file)
# and apply it to a class `Logger` that stores a list `entries = []`
# in __init__. Create logger1 = Logger() and logger2 = Logger(),
# append "Order placed" to logger1.entries, then print
# logger2.entries and (logger1 is logger2).
#
# Expected output:
# ['Order placed']
# True

# YOUR CODE HERE


# SOLUTION:
# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class Logger(metaclass=SingletonMeta):
#     def __init__(self):
#         self.entries = []
#
#
# logger1 = Logger()
# logger2 = Logger()
# logger1.entries.append("Order placed")
# print(logger2.entries)
# print(logger1 is logger2)

print("-" * 50)


# ── C4. 🔴 Challenge — Auto-registering plugin metaclass ──
# Build a metaclass `HandlerMeta` that maintains a class-level dict
# `registry = {}` on the metaclass itself, and registers every
# subclass (but NOT the base class) using the class's __name__ as
# the key. Create a base class `PaymentHandler(metaclass=HandlerMeta)`
# and two subclasses `UPIHandler` and `CardHandler` (empty bodies
# with `pass` are fine). Print sorted(list(HandlerMeta.registry.keys())).
#
# Expected output:
# ['CardHandler', 'UPIHandler']

# YOUR CODE HERE


# SOLUTION:
# class HandlerMeta(type):
#     registry = {}
#
#     def __new__(mcs, name, bases, namespace):
#         new_class = super().__new__(mcs, name, bases, namespace)
#         if bases:
#             mcs.registry[name] = new_class
#         return new_class
#
#
# class PaymentHandler(metaclass=HandlerMeta):
#     pass
#
#
# class UPIHandler(PaymentHandler):
#     pass
#
#
# class CardHandler(PaymentHandler):
#     pass
#
#
# print(sorted(list(HandlerMeta.registry.keys())))

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   C — Metaclasses (4 problems)
#
# Difficulty breakdown: 2x 🟢 Warm-up, 1x 🟡 Core, 1x 🔴 Challenge
#
# Next file: day17_practise_problems_03_protocol_classes.py
# (Section D — Protocol Classes)
