"""
Day 13 — Iterators & Generators
Practice Problem Set — File 1 of 4

Section Index:
    Section A — Prior Days Review (Days 10-12: OOP, modules)
    Section B — Iterator Basics (__iter__ / __next__)

Difficulty Legend:
    🟢 Warm-up   🟡 Core   🔴 Challenge

How to run:
    python day13_practise_problems_01_review_iterators.py
"""

# ════════════════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════════════════════

# Problem A1  🟢 Warm-up
# Create a class `Student` (Day 10 review) with __init__ taking `name` and
# `marks` (a list of ints). Add a method `average()` that returns the mean
# of marks. Create a Student named "Priya" with marks [78, 85, 92] and
# print her average.

# YOUR CODE HERE


# SOLUTION:
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def average(self):
#         return sum(self.marks) / len(self.marks)
#
# priya = Student("Priya", [78, 85, 92])
# print(f"{priya.name}'s average: {priya.average():.2f}")
# # Output: Priya's average: 85.00

print("-" * 50)

# Problem A2  🟡 Core
# Create a class `Vehicle` with a class variable `wheels = 4` and an
# instance variable `owner`. Create a subclass `Bike` (Day 11 review) that
# overrides `wheels = 2`. Create one Vehicle owned by "Arjun" and one Bike
# owned by "Sanjay Verma", and print each owner with their wheel count.

# YOUR CODE HERE


# SOLUTION:
# class Vehicle:
#     wheels = 4
#     def __init__(self, owner):
#         self.owner = owner
#
# class Bike(Vehicle):
#     wheels = 2
#
# car = Vehicle("Arjun")
# bike = Bike("Sanjay Verma")
# print(f"{car.owner}: {car.wheels} wheels")
# print(f"{bike.owner}: {bike.wheels} wheels")
# # Output:
# # Arjun: 4 wheels
# # Sanjay Verma: 2 wheels

print("-" * 50)

# Problem A3  🟡 Core
# Using the `math` module (Day 12 review), write code that computes and
# prints the ceiling and floor of 17.3.

# YOUR CODE HERE


# SOLUTION:
# import math
# value = 17.3
# print(f"Ceiling: {math.ceil(value)}")
# print(f"Floor: {math.floor(value)}")
# # Output:
# # Ceiling: 18
# # Floor: 17

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION B — Iterator Basics (__iter__ / __next__)
# ════════════════════════════════════════════════════════════════════════

# Problem B1  🟢 Warm-up
# Use Python's built-in iter() and next() to manually print the first 3
# values from the list [10, 20, 30, 40, 50] without using a for loop.

# YOUR CODE HERE


# SOLUTION:
# numbers = [10, 20, 30, 40, 50]
# it = iter(numbers)
# print(next(it))
# print(next(it))
# print(next(it))
# # Output:
# # 10
# # 20
# # 30

print("-" * 50)

# Problem B2  🟡 Core
# Write a class `Countdown` that is its own iterator (has both __iter__
# returning self, and __next__). It should start at a given number and
# count down to 1 (inclusive), then raise StopIteration.

# YOUR CODE HERE


# SOLUTION:
# class Countdown:
#     def __init__(self, start):
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < 1:
#             raise StopIteration
#         value = self.current
#         self.current -= 1
#         return value
#
# for n in Countdown(5):
#     print(n)
# # Output: 5 4 3 2 1

print("-" * 50)

# Problem B3  🟡 Core
# Write a class `MumbaiTrainStops` that is an iterable (has __iter__
# returning a fresh iterator each time) wrapping a list of station names.
# Demonstrate it can be looped over twice successfully.

# YOUR CODE HERE


# SOLUTION:
# class StationIterator:
#     def __init__(self, stations):
#         self.stations = stations
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.stations):
#             raise StopIteration
#         station = self.stations[self.index]
#         self.index += 1
#         return station
#
# class MumbaiTrainStops:
#     def __init__(self, stations):
#         self.stations = stations
#
#     def __iter__(self):
#         return StationIterator(self.stations)
#
# line = MumbaiTrainStops(["Churchgate", "Dadar", "Borivali"])
# print("Pass 1:", list(line))
# print("Pass 2:", list(line))
# # Output:
# # Pass 1: ['Churchgate', 'Dadar', 'Borivali']
# # Pass 2: ['Churchgate', 'Dadar', 'Borivali']

print("-" * 50)

# Problem B4  🔴 Challenge
# Write an iterator class `PrimeIterator` that, given a limit, produces all
# prime numbers up to (and including) that limit, one at a time.
# Hint: write a helper function `is_prime(n)`.

# YOUR CODE HERE


# SOLUTION:
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# class PrimeIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#         while self.current <= self.limit:
#             if is_prime(self.current):
#                 return self.current
#             self.current += 1
#         raise StopIteration
#
# print(list(PrimeIterator(20)))
# # Output: [2, 3, 5, 7, 11, 13, 17, 19]

print("-" * 50)

# Problem B5  🔴 Challenge
# Write a class `BoundedCart` that acts as an iterator over a list of
# (item, price) tuples, but raises StopIteration early (stops yielding)
# the moment the running total would exceed a given budget — even if more
# items remain in the cart.

# YOUR CODE HERE


# SOLUTION:
# class BoundedCart:
#     def __init__(self, items, budget):
#         self.items = items
#         self.budget = budget
#         self.index = 0
#         self.total = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.items):
#             raise StopIteration
#         name, price = self.items[self.index]
#         if self.total + price > self.budget:
#             raise StopIteration
#         self.total += price
#         self.index += 1
#         return name, price
#
# cart_items = [("Notebook", 60), ("Pen Set", 120), ("Backpack", 1450), ("Eraser", 10)]
# for item, price in BoundedCart(cart_items, budget=200):
#     print(f"{item}: Rs.{price}")
# # Output:
# # Notebook: Rs.60
# # Pen Set: Rs.120

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
# Section A: 3 problems — OOP, inheritance, and module review (Days 10-12)
# Section B: 5 problems — building custom iterators with __iter__/__next__
# Difficulty breakdown: 2x Warm-up, 4x Core, 2x Challenge
#
# Continue to File 2 of 4 for Section C — Generator Functions (yield).

if __name__ == "__main__":
    print("Day 13 Practice Set, File 1 — Review & Iterator Basics: file loaded successfully.")
