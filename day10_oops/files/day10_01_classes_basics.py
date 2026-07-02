"""
Day 10 — Object-Oriented Programming I
File 1 of 2: Classes, Objects, __init__, and self

Covers:
    - What a class is and why we use them
    - Creating objects (instances) from a class
    - The __init__ constructor method
    - The `self` keyword and what it really means

Prerequisites:
    - Day 5 (Functions & Scope)
    - Day 6 (Data Structures — especially dictionaries)
    - Day 9 (Error Handling)

How to run:
    python day10_01_classes_basics.py
"""

# ════════════════════════════════════════════════════════
# SECTION 1: WHY CLASSES? FROM DICTIONARIES TO OBJECTS
# ════════════════════════════════════════════════════════

# ── The Problem ──
# Until now, if we wanted to represent a "student" or a "task", we probably
# used a dictionary:
#
#     student = {"name": "Priya", "marks": 88}
#
# This works, but it has no built-in *behaviour*. If we want to calculate
# a grade, we need a separate function, and nothing stops someone from
# writing student["nmae"] = 90 (a typo that silently creates a new key).
#
# A CLASS lets us bundle DATA (attributes) and BEHAVIOUR (methods) into a
# single, reusable blueprint. Each object we create from that blueprint is
# called an INSTANCE.

print("=" * 50)
print("SECTION 1: Why classes?")
print("=" * 50)

# The old dictionary way (for comparison only):
student_dict = {"name": "Priya", "marks": 88}
print(f"Dictionary version: {student_dict['name']} scored {student_dict['marks']}")
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: DEFINING YOUR FIRST CLASS
# ════════════════════════════════════════════════════════

# ── Concept: The `class` keyword ──
# A class is defined using the `class` keyword, followed by the class name
# (convention: CapitalCase, e.g. Student, TaskManager) and a colon.
# By convention, class names use PascalCase while variables use snake_case.

class Student:
    """A simple class representing a student in Mumbai."""
    pass  # 'pass' means "do nothing" — placeholder for an empty class body


# Creating an object (instance) from the class is called INSTANTIATION.
# We call the class name like a function:
priya = Student()
print(f"priya is an object of type: {type(priya)}")
print(f"priya is an instance: {isinstance(priya, Student)}")
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 3: THE __init__ CONSTRUCTOR
# ════════════════════════════════════════════════════════

# ── Concept: __init__ ──
# An empty class isn't very useful. We want every Student object to start
# with some data already filled in — a name, a city, marks, etc.
#
# Python calls a special method named __init__ automatically every time a
# new object is created. This is called the CONSTRUCTOR. We use it to set
# up (initialise) the object's starting attributes.
#
# The double underscores on either side (__init__) mark it as a "dunder"
# (double underscore) method — Python's way of giving special meaning to
# certain method names. We'll see more dunder methods on Day 11.

class Student:
    """A student enrolled in the Python course, with a name and city."""

    def __init__(self, name, city, marks):
        # Anything assigned to self.xxx here becomes an ATTRIBUTE of the
        # object — data that "belongs" to this specific instance.
        self.name = name
        self.city = city
        self.marks = marks
        print(f"New Student object created for {self.name}")


# Now when we create an object, Python automatically calls __init__ for us,
# passing in the values we provide:
arjun = Student("Arjun", "Delhi", 76)
riya = Student("Riya Deshmukh", "Mumbai", 91)

print(f"{arjun.name} lives in {arjun.city} and scored {arjun.marks}")
print(f"{riya.name} lives in {riya.city} and scored {riya.marks}")
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 4: UNDERSTANDING `self`
# ════════════════════════════════════════════════════════

# ── Concept: What is `self`, really? ──
# `self` is simply a reference to THE SPECIFIC OBJECT the method is being
# called on. It is the first parameter of every instance method (including
# __init__), but Python fills it in automatically — you never pass it
# yourself.
#
#   arjun = Student("Arjun", "Delhi", 76)
#
# is roughly equivalent, under the hood, to Python doing:
#
#   arjun = Student.__new__(Student)          # create a blank object
#   Student.__init__(arjun, "Arjun", "Delhi", 76)   # self = arjun
#
# So inside __init__, `self.name = name` really means:
# "on THIS particular object, set its name attribute to the given value".
#
# `self` can technically be named anything, but EVERY Python programmer
# uses `self` by convention — never deviate from this.

class Task:
    """A single task in a Mumbai grocery delivery app."""

    def __init__(self, description, assigned_to):
        self.description = description
        self.assigned_to = assigned_to
        self.is_complete = False  # every new task starts incomplete

    def mark_complete(self):
        # `self` here refers to whichever Task object called this method.
        self.is_complete = True
        print(f"Task '{self.description}' marked complete by {self.assigned_to}")


task1 = Task("Deliver groceries to Bandra", "Sanjay Verma")
task2 = Task("Restock vegetables at Andheri store", "Priya")

# `self` inside mark_complete() refers to task1 when we call task1.mark_complete()
task1.mark_complete()
# ... and refers to task2 when we call task2.mark_complete()
task2.mark_complete()

print(f"Task 1 complete? {task1.is_complete}")
print(f"Task 2 complete? {task2.is_complete}")
print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 5: GUIDED EXAMPLES (Indian context)
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION 5: Guided Examples")
print("=" * 50)

# ── Example 1: A simple BankAccount class ──
class BankAccount:
    """A basic savings account at a Mumbai branch."""

    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Balance is only Rs.{self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. New balance: Rs.{self.balance}")


sanjay_account = BankAccount("Sanjay Verma", 5000)
sanjay_account.deposit(1500)
sanjay_account.withdraw(2000)
sanjay_account.withdraw(10000)  # should fail — insufficient funds
print("-" * 50)


# ── Example 2: A Movie class for a Delhi multiplex booking system ──
class Movie:
    """A movie showing at a Delhi multiplex."""

    def __init__(self, title, language, ticket_price):
        self.title = title
        self.language = language
        self.ticket_price = ticket_price
        self.seats_booked = 0

    def book_seats(self, count):
        self.seats_booked += count
        total = count * self.ticket_price
        print(f"Booked {count} seat(s) for '{self.title}'. Total: Rs.{total}")


movie = Movie("3 Idiots (Re-release)", "Hindi", 250)
movie.book_seats(4)
print(f"Total seats booked so far: {movie.seats_booked}")
print("-" * 50)


# ── Example 3: A Recipe class using default-like behaviour via __init__ ──
class Recipe:
    """A recipe card for a home cook in Pune."""

    def __init__(self, name, ingredients, servings=2):
        self.name = name
        self.ingredients = ingredients  # expects a list
        self.servings = servings

    def describe(self):
        ingredient_list = ", ".join(self.ingredients)
        print(f"{self.name} (serves {self.servings}): {ingredient_list}")


poha = Recipe("Kanda Poha", ["poha", "onion", "mustard seeds", "turmeric"])
poha.describe()

biryani = Recipe("Hyderabadi Biryani", ["rice", "chicken", "spices", "yogurt"], servings=6)
biryani.describe()
print("-" * 50)


# ── Example 4: A LibraryBook class showing multiple attributes at once ──
class LibraryBook:
    """A book in a school library in Chennai."""

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self, student_name):
        if self.available:
            self.available = False
            print(f"'{self.title}' borrowed by {student_name}")
        else:
            print(f"Sorry, '{self.title}' is already checked out")


book = LibraryBook("Wings of Fire", "A.P.J. Abdul Kalam", "978-8173711466")
book.borrow("Riya Deshmukh")
book.borrow("Arjun")  # should fail — already checked out
print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════

# Create a class called `AutoRickshaw` that represents a Mumbai auto-rickshaw
# ride booking.
#
# Requirements:
#   1. __init__ should accept: driver_name, vehicle_number, and set a
#      starting fare of 0.
#   2. Add a method `add_distance_fare(self, km)` that adds (km * 15) rupees
#      to the fare (Rs. 15 per km) and prints the updated fare.
#   3. Create an object for driver "Ramesh" with vehicle number "MH-01-AB-1234"
#      and call add_distance_fare(5), then add_distance_fare(3).
#
# Expected output (approx):
#   Fare after 5 km: Rs.75
#   Fare after 3 km: Rs.120

# YOUR CODE HERE


# SOLUTION:
# class AutoRickshaw:
#     def __init__(self, driver_name, vehicle_number):
#         self.driver_name = driver_name
#         self.vehicle_number = vehicle_number
#         self.fare = 0
#
#     def add_distance_fare(self, km):
#         self.fare += km * 15
#         print(f"Fare after {km} km: Rs.{self.fare}")
#
# ride = AutoRickshaw("Ramesh", "MH-01-AB-1234")
# ride.add_distance_fare(5)
# ride.add_distance_fare(3)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
# In this file, we covered:
#   - Why classes exist (bundling data + behaviour, unlike plain dicts)
#   - Defining a class with the `class` keyword
#   - Creating objects (instantiation)
#   - The __init__ constructor and how it auto-runs on object creation
#   - What `self` actually refers to under the hood
#
# Next up (day10_02_instance_class_variables.py):
#   - Instance variables vs. class variables
#   - Instance methods in more depth
