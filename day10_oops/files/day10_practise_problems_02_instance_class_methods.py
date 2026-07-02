"""
Day 10 — Practice Problems (File 2 of 2)
Topic: OOP I — Instance vs Class Variables, Instance Methods, Mixed Challenges

Cumulative scope: Days 1-10 (all prior topics plus today's full OOP I content:
classes, objects, __init__, self, instance vs class variables, instance methods)

Difficulty legend:
    🟢 Warm-up   — quick, direct application
    🟡 Core      — combines a few ideas
    🔴 Challenge — requires extra thought / multiple steps

Section index (this file):
    C — Instance vs Class Variables (5 problems)
    D — Instance Methods in Depth (4 problems)
    E — Mixed Challenges (3 problems)

(Section A and B are in day10_practise_problems_01_classes_basics.py)

How to run:
    python day10_practise_problems_02_instance_class_methods.py
"""

# ════════════════════════════════════════════════════════
# SECTION C — Instance vs Class Variables
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION C: Instance vs Class Variables")
print("=" * 50)

# ── Problem C1 🟢 Warm-up ──
# Define a class `School` with a class variable `board = "CBSE"`. Create two
# objects (no __init__ needed) and print `.board` on both through the
# instances, then print it through the class itself (School.board).

# YOUR CODE HERE


# SOLUTION:
# class School:
#     board = "CBSE"
#
# s1 = School()
# s2 = School()
# print(s1.board)
# print(s2.board)
# print(School.board)

print("-" * 50)


# ── Problem C2 🟢 Warm-up ──
# Define a class `Restaurant` with a class variable `gst_percent = 5`.
# __init__ accepts `name`. Create an object for "Saravana Bhavan" and print
# f"{name} charges {gst_percent}% GST" using the object's attributes.

# YOUR CODE HERE


# SOLUTION:
# class Restaurant:
#     gst_percent = 5
#
#     def __init__(self, name):
#         self.name = name
#
# r = Restaurant("Saravana Bhavan")
# print(f"{r.name} charges {r.gst_percent}% GST")

print("-" * 50)


# ── Problem C3 🟡 Core ──
# Define a class `Counter` with a class variable `total = 0`. __init__
# should increment Counter.total by 1 every time a new object is created
# (no other parameters needed). Create 5 Counter objects in a loop and then
# print Counter.total. It should print 5.

# YOUR CODE HERE


# SOLUTION:
# class Counter:
#     total = 0
#
#     def __init__(self):
#         Counter.total += 1
#
# for _ in range(5):
#     Counter()
# print(Counter.total)

print("-" * 50)


# ── Problem C4 🟡 Core ──
# Define a class `Employee` with a class variable `default_bonus = 5000`.
# __init__ accepts `name`. Create two employees "Priya" and "Arjun".
# Override `bonus` (set from `default_bonus`) as an INSTANCE variable only
# for Priya, giving her 8000. Then print each employee's bonus by reading
# self.default_bonus for Arjun (since he has no override) and self.bonus
# for Priya. Confirm that changing Employee.default_bonus afterwards to
# 6000 does NOT affect Priya's overridden bonus but DOES affect what Arjun
# would see via default_bonus.

# YOUR CODE HERE


# SOLUTION:
# class Employee:
#     default_bonus = 5000
#
#     def __init__(self, name):
#         self.name = name
#
# priya = Employee("Priya")
# arjun = Employee("Arjun")
# priya.bonus = 8000  # instance-level override
#
# print(f"Priya's bonus: {priya.bonus}")
# print(f"Arjun's bonus (uses class default): {arjun.default_bonus}")
#
# Employee.default_bonus = 6000
# print(f"After change -> Priya's bonus: {priya.bonus}")
# print(f"After change -> Arjun's bonus: {arjun.default_bonus}")

print("-" * 50)


# ── Problem C5 🔴 Challenge ──
# Define a class `Library` with a class variable `books_available = 100`.
# Add an instance method `issue_book(self)` that decreases
# Library.books_available by 1 (use the class name, not self, to modify it)
# and prints the remaining count — UNLESS books_available is already 0, in
# which case it prints "No books left!".
# Create two Library objects (they share the same pool) and call
# issue_book() 3 times total across both objects, confirming the shared
# count drops correctly regardless of which object calls it.

# YOUR CODE HERE


# SOLUTION:
# class Library:
#     books_available = 100
#
#     def issue_book(self):
#         if Library.books_available > 0:
#             Library.books_available -= 1
#             print(f"Book issued. Remaining: {Library.books_available}")
#         else:
#             print("No books left!")
#
# branch1 = Library()
# branch2 = Library()
# branch1.issue_book()
# branch2.issue_book()
# branch1.issue_book()

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION D — Instance Methods in Depth
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION D: Instance Methods in Depth")
print("=" * 50)

# ── Problem D1 🟢 Warm-up ──
# Define a class `Rectangle` with __init__ accepting `length` and `width`.
# Add an instance method `area(self)` that returns length * width.
# Create a rectangle 5 x 3 and print its area.

# YOUR CODE HERE


# SOLUTION:
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# r = Rectangle(5, 3)
# print(r.area())

print("-" * 50)


# ── Problem D2 🟡 Core ──
# Define a class `SavingsGoal` for someone saving up for a trip to Goa.
# __init__ accepts `target_amount` and starts `saved_amount` at 0.
# Add a method `add_savings(self, amount)` that increases saved_amount and
# prints progress as a percentage (rounded to 1 decimal), e.g.
# "Progress: 40.0% (Rs.4000/Rs.10000)"
# Create a goal of 10000 and add savings of 3000, then 1000.

# YOUR CODE HERE


# SOLUTION:
# class SavingsGoal:
#     def __init__(self, target_amount):
#         self.target_amount = target_amount
#         self.saved_amount = 0
#
#     def add_savings(self, amount):
#         self.saved_amount += amount
#         percent = (self.saved_amount / self.target_amount) * 100
#         print(f"Progress: {percent:.1f}% (Rs.{self.saved_amount}/Rs.{self.target_amount})")
#
# goal = SavingsGoal(10000)
# goal.add_savings(3000)
# goal.add_savings(1000)

print("-" * 50)


# ── Problem D3 🟡 Core ──
# Define a class `Playlist` for a music app. __init__ starts with an empty
# list `songs`. Add methods:
#   - add_song(self, song_name) -> appends to songs, prints confirmation
#   - remove_song(self, song_name) -> removes if present, else prints
#     "Song not found: <song_name>"
#   - show_playlist(self) -> prints numbered list of songs
# Add "Kesariya", "Tum Hi Ho", and "Zinda" to a playlist, remove "Tum Hi Ho",
# then show the playlist.

# YOUR CODE HERE


# SOLUTION:
# class Playlist:
#     def __init__(self):
#         self.songs = []
#
#     def add_song(self, song_name):
#         self.songs.append(song_name)
#         print(f"Added: {song_name}")
#
#     def remove_song(self, song_name):
#         if song_name in self.songs:
#             self.songs.remove(song_name)
#             print(f"Removed: {song_name}")
#         else:
#             print(f"Song not found: {song_name}")
#
#     def show_playlist(self):
#         for i, song in enumerate(self.songs, start=1):
#             print(f"{i}. {song}")
#
# playlist = Playlist()
# playlist.add_song("Kesariya")
# playlist.add_song("Tum Hi Ho")
# playlist.add_song("Zinda")
# playlist.remove_song("Tum Hi Ho")
# playlist.show_playlist()

print("-" * 50)


# ── Problem D4 🔴 Challenge ──
# Define a class `ElectricityBill` for a household in Pune. __init__
# accepts `units_consumed`. Add a method `calculate_bill(self)` that
# returns the total bill using slab-based pricing:
#   - First 100 units: Rs.3 per unit
#   - Next 100 units (101-200): Rs.5 per unit
#   - Any units above 200: Rs.8 per unit
# Test with units_consumed = 250 and print the result.
# (Hint: 100*3 + 100*5 + 50*8 = 1200)

# YOUR CODE HERE


# SOLUTION:
# class ElectricityBill:
#     def __init__(self, units_consumed):
#         self.units_consumed = units_consumed
#
#     def calculate_bill(self):
#         units = self.units_consumed
#         total = 0
#         if units > 200:
#             total += (units - 200) * 8
#             units = 200
#         if units > 100:
#             total += (units - 100) * 5
#             units = 100
#         total += units * 3
#         return total
#
# bill = ElectricityBill(250)
# print(f"Total bill: Rs.{bill.calculate_bill()}")

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION E: Mixed Challenges")
print("=" * 50)

# ── Problem E1 🔴 Challenge ──
# Define a class `Warehouse` combining class + instance variables:
#   - Class variable `total_stock_value = 0` (shared across all items)
#   - __init__ accepts `item_name` and `quantity` and `unit_price`
#   - On creation, add (quantity * unit_price) to Warehouse.total_stock_value
#   - Add a method `sell(self, count)` that reduces self.quantity by count
#     (if enough stock; else print "Not enough stock"), and also reduces
#     Warehouse.total_stock_value by (count * self.unit_price)
# Create two warehouse items and sell some units from each, then print
# Warehouse.total_stock_value at the end.

# YOUR CODE HERE


# SOLUTION:
# class Warehouse:
#     total_stock_value = 0
#
#     def __init__(self, item_name, quantity, unit_price):
#         self.item_name = item_name
#         self.quantity = quantity
#         self.unit_price = unit_price
#         Warehouse.total_stock_value += quantity * unit_price
#
#     def sell(self, count):
#         if count > self.quantity:
#             print("Not enough stock")
#         else:
#             self.quantity -= count
#             Warehouse.total_stock_value -= count * self.unit_price
#             print(f"Sold {count} unit(s) of {self.item_name}")
#
# item1 = Warehouse("Basmati Rice (25kg bag)", 50, 1200)
# item2 = Warehouse("Sunflower Oil (1L)", 100, 150)
# item1.sell(10)
# item2.sell(20)
# print(f"Total stock value remaining: Rs.{Warehouse.total_stock_value}")

print("-" * 50)


# ── Problem E2 🔴 Challenge ──
# Define a class `QuizGame` that combines earlier-day concepts (loops,
# dictionaries) with today's OOP concepts:
#   - __init__ accepts `player_name` and starts `score` at 0
#   - Class variable `questions` = a dictionary of 3 general-knowledge
#     questions about India mapped to their answers, e.g.
#     {"Capital of India?": "Delhi", "National sport?": "Hockey",
#      "Longest river?": "Ganga"}
#   - Add a method `play(self, answers_given)` that accepts a dictionary of
#     the player's answers, loops through QuizGame.questions, and adds 1 to
#     self.score for every correct match. Print the final score out of 3.
# Test with a player who gets 2 out of 3 correct.

# YOUR CODE HERE


# SOLUTION:
# class QuizGame:
#     questions = {
#         "Capital of India?": "Delhi",
#         "National sport?": "Hockey",
#         "Longest river?": "Ganga",
#     }
#
#     def __init__(self, player_name):
#         self.player_name = player_name
#         self.score = 0
#
#     def play(self, answers_given):
#         for question, correct_answer in QuizGame.questions.items():
#             if answers_given.get(question) == correct_answer:
#                 self.score += 1
#         print(f"{self.player_name} scored {self.score}/{len(QuizGame.questions)}")
#
# player_answers = {
#     "Capital of India?": "Delhi",
#     "National sport?": "Cricket",  # wrong on purpose
#     "Longest river?": "Ganga",
# }
# game = QuizGame("Sanjay Verma")
# game.play(player_answers)

print("-" * 50)


# ── Problem E3 🔴 Challenge ──
# Design a class `HospitalQueue` for a Bengaluru clinic's token system that
# uses BOTH a class variable and file-writing-style logic (Day 8 style,
# but simulated with a list here instead of an actual file):
#   - Class variable `next_token = 1` (shared, auto-incrementing)
#   - __init__ accepts `patient_name`, assigns self.token = HospitalQueue.next_token,
#     then increments HospitalQueue.next_token by 1
#   - Add a method `call_patient(self)` that prints:
#     "Token #<token>: Please proceed, <patient_name>"
# Register three patients ("Priya", "Meera", "Arjun") in that order and
# call each one, confirming tokens are assigned 1, 2, 3 automatically.

# YOUR CODE HERE


# SOLUTION:
# class HospitalQueue:
#     next_token = 1
#
#     def __init__(self, patient_name):
#         self.patient_name = patient_name
#         self.token = HospitalQueue.next_token
#         HospitalQueue.next_token += 1
#
#     def call_patient(self):
#         print(f"Token #{self.token}: Please proceed, {self.patient_name}")
#
# p1 = HospitalQueue("Priya")
# p2 = HospitalQueue("Meera")
# p3 = HospitalQueue("Arjun")
# p1.call_patient()
# p2.call_patient()
# p3.call_patient()

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
# Sections in this file:
#   C — Instance vs Class Variables   (5 problems)
#   D — Instance Methods in Depth     (4 problems)
#   E — Mixed Challenges              (3 problems)
#
# Difficulty breakdown (this file): 3 Warm-up, 4 Core, 5 Challenge
#
# Combined with file 1 (day10_practise_problems_01_classes_basics.py):
#   Total problems across both files: 20
#   Total difficulty breakdown: 6 Warm-up, 8 Core, 6 Challenge
#
# Next up: Day 11 practice problems will build on today's OOP foundation
# with inheritance, polymorphism, encapsulation, and dunder methods.
