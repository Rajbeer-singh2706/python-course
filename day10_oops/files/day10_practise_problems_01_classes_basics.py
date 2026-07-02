"""
Day 10 — Practice Problems (File 1 of 2)
Topic: OOP I — Classes, Objects, __init__, self

Cumulative scope: Days 1-10 (Setup, Variables, Control Flow, Loops,
Functions & Scope, Data Structures, Strings, File I/O, Error Handling,
and today's Classes/Objects/__init__/self)

Difficulty legend:
    🟢 Warm-up   — quick, direct application
    🟡 Core      — combines a few ideas
    🔴 Challenge — requires extra thought / multiple steps

Section index (this file):
    A — Prior Days Review (2 problems)
    B — Classes & Objects, __init__, self (6 problems)

(Section C, D, and Mixed Challenges continue in
 day10_practise_problems_02_instance_class_methods.py)

How to run:
    python day10_practise_problems_01_classes_basics.py
"""

# ════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION A: Prior Days Review")
print("=" * 50)

# ── Problem A1 🟢 Warm-up ──
# Using a dictionary (Day 6), store the name and marks of a student named
# "Arjun" with marks 82. Print a sentence using an f-string (Day 7):
# "Arjun scored 82 marks"

# YOUR CODE HERE


# SOLUTION:
# student = {"name": "Arjun", "marks": 82}
# print(f"{student['name']} scored {student['marks']} marks")

print("-" * 50)


# ── Problem A2 🟡 Core ──
# Write a function (Day 5) called `average_marks` that accepts a list of
# integers and returns their average using try/except (Day 9) to handle
# an empty list gracefully (return 0 if the list is empty).
# Test it with [88, 76, 91, 65] and with an empty list [].

# YOUR CODE HERE


# SOLUTION:
# def average_marks(marks_list):
#     try:
#         return sum(marks_list) / len(marks_list)
#     except ZeroDivisionError:
#         return 0
#
# print(average_marks([88, 76, 91, 65]))
# print(average_marks([]))

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION B — Classes & Objects, __init__, self
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION B: Classes & Objects, __init__, self")
print("=" * 50)

# ── Problem B1 🟢 Warm-up ──
# Define an empty class called `Car` (use `pass` in the body).
# Create one object called `my_car` from it, then print its type using
# type(my_car).

# YOUR CODE HERE


# SOLUTION:
# class Car:
#     pass
#
# my_car = Car()
# print(type(my_car))

print("-" * 50)


# ── Problem B2 🟢 Warm-up ──
# Define a class `Fruit` with an __init__ that accepts `name` and `price`
# and stores them as self.name and self.price. Create an object for
# "Mango" priced at 120 rupees, then print:
# "Mango costs Rs.120"

# YOUR CODE HERE


# SOLUTION:
# class Fruit:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# mango = Fruit("Mango", 120)
# print(f"{mango.name} costs Rs.{mango.price}")

print("-" * 50)


# ── Problem B3 🟡 Core ──
# Define a class `Contact` for a phone contacts app. __init__ should accept
# `name` and `phone_number`. Add a method `display(self)` that prints:
# "Name: <name>, Phone: <phone_number>"
# Create two contacts: "Sanjay Verma" / "9876543210" and
# "Meera" / "9123456780". Call display() on both.

# YOUR CODE HERE


# SOLUTION:
# class Contact:
#     def __init__(self, name, phone_number):
#         self.name = name
#         self.phone_number = phone_number
#
#     def display(self):
#         print(f"Name: {self.name}, Phone: {self.phone_number}")
#
# c1 = Contact("Sanjay Verma", "9876543210")
# c2 = Contact("Meera", "9123456780")
# c1.display()
# c2.display()

print("-" * 50)


# ── Problem B4 🟡 Core ──
# Define a class `Wallet` representing a Paytm-style digital wallet.
# __init__ accepts `owner_name` and starts `balance` at 0.
# Add a method `add_money(self, amount)` that increases the balance and
# prints "Added Rs.<amount>. Balance: Rs.<balance>".
# Add a method `pay(self, amount)` that, if there is enough balance,
# deducts it and prints "Paid Rs.<amount>. Balance: Rs.<balance>",
# otherwise prints "Insufficient balance!".
# Create a wallet for "Riya Deshmukh", add 500, then try to pay 300, then
# try to pay 400 (should fail).

# YOUR CODE HERE


# SOLUTION:
# class Wallet:
#     def __init__(self, owner_name):
#         self.owner_name = owner_name
#         self.balance = 0
#
#     def add_money(self, amount):
#         self.balance += amount
#         print(f"Added Rs.{amount}. Balance: Rs.{self.balance}")
#
#     def pay(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print(f"Paid Rs.{amount}. Balance: Rs.{self.balance}")
#
# wallet = Wallet("Riya Deshmukh")
# wallet.add_money(500)
# wallet.pay(300)
# wallet.pay(400)

print("-" * 50)


# ── Problem B5 🟡 Core ──
# Define a class `Movie` with __init__ accepting `title`, `rating` (out of
# 10), and `language`. Add a method `is_recommended(self)` that returns
# True if rating >= 7, else False. Create three Movie objects of your
# choice (Indian films) and print which ones are recommended using a loop
# over a list of the three objects.

# YOUR CODE HERE


# SOLUTION:
# class Movie:
#     def __init__(self, title, rating, language):
#         self.title = title
#         self.rating = rating
#         self.language = language
#
#     def is_recommended(self):
#         return self.rating >= 7
#
# movies = [
#     Movie("Dangal", 8.4, "Hindi"),
#     Movie("Baahubali", 8.0, "Telugu"),
#     Movie("Random Flop", 4.5, "Hindi"),
# ]
# for m in movies:
#     status = "Recommended" if m.is_recommended() else "Not recommended"
#     print(f"{m.title} ({m.language}): {status}")

print("-" * 50)


# ── Problem B6 🔴 Challenge ──
# Define a class `RailwayTicket` for booking on IRCTC. __init__ should
# accept `passenger_name`, `source`, `destination`, and `fare`. Add a
# method `apply_senior_discount(self)` that reduces fare by 40% (multiply
# by 0.6) and prints the new fare, ONLY if fare is currently above 500 —
# otherwise print "No discount applicable".
# Test with a ticket that has fare=800 (should discount) and one with
# fare=300 (should not).

# YOUR CODE HERE


# SOLUTION:
# class RailwayTicket:
#     def __init__(self, passenger_name, source, destination, fare):
#         self.passenger_name = passenger_name
#         self.source = source
#         self.destination = destination
#         self.fare = fare
#
#     def apply_senior_discount(self):
#         if self.fare > 500:
#             self.fare = self.fare * 0.6
#             print(f"Discount applied. New fare: Rs.{self.fare:.2f}")
#         else:
#             print("No discount applicable")
#
# t1 = RailwayTicket("Arjun", "Mumbai", "Pune", 800)
# t1.apply_senior_discount()
#
# t2 = RailwayTicket("Priya", "Delhi", "Agra", 300)
# t2.apply_senior_discount()

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
# Sections in this file:
#   A — Prior Days Review           (2 problems)
#   B — Classes, __init__, self     (6 problems)
#
# Difficulty breakdown: 3 Warm-up, 4 Core, 1 Challenge
#
# Continue with day10_practise_problems_02_instance_class_methods.py for:
#   C — Instance vs Class Variables
#   D — Instance Methods in Depth
#   E — Mixed Challenges
