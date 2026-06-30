"""
Day 11 — Object-Oriented Programming II
Practice Problems — File 1 of 3: Prior Days Review + Inheritance

Cumulative scope: Days 1-11 (Setup through OOP II - Inheritance)

Difficulty legend:
    🟢 Warm-up   — straightforward, single-concept
    🟡 Core      — typical exam/interview level
    🔴 Challenge — combines multiple ideas or edge cases

Section index in this file:
    Section A — Prior Days Review (Days 1-10)
    Section B — Inheritance & super()

How to run:
    python day11_practise_problems_01_inheritance.py
"""

# ════════════════════════════════════════════════════════════
# SECTION A: Prior Days Review
# ════════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION A: Prior Days Review")
print("=" * 50)

# ── Problem A1 ──
# 🟢 Warm-up
# Write a function `is_even(n)` that returns True if n is even, else False.
# (Reviews Day 3: control flow)

n_value = 18  # simulating input()

# YOUR CODE HERE


def is_even_solution(n):
    return n % 2 == 0


# SOLUTION:
# print(is_even_solution(n_value))
# Expected output: True

print("-" * 50)

# ── Problem A2 ──
# 🟢 Warm-up
# Given a dictionary of student marks, use a dict comprehension to create
# a new dictionary containing only students who scored 75 or above.
# (Reviews Day 6: data structures + comprehensions)

marks_dict = {"Arjun": 82, "Priya": 67, "Riya": 91, "Karan": 40}  # simulating input()

# YOUR CODE HERE


def filter_passing_solution(marks):
    return {name: score for name, score in marks.items() if score >= 75}


# SOLUTION:
# print(filter_passing_solution(marks_dict))
# Expected output: {'Arjun': 82, 'Riya': 91}

print("-" * 50)

# ── Problem A3 ──
# 🟡 Core
# Write a function `safe_divide(a, b)` that returns a / b, but catches
# ZeroDivisionError and returns the string "Cannot divide by zero" instead.
# (Reviews Day 9: error handling)

a_value, b_value = 50, 0  # simulating input()

# YOUR CODE HERE


def safe_divide_solution(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


# SOLUTION:
# print(safe_divide_solution(a_value, b_value))
# Expected output: Cannot divide by zero

print("-" * 50)

# ── Problem A4 ──
# 🟡 Core
# Create a class `Book` (Day 10 style — no inheritance yet) with `title`
# and `author`, and an instance method `summary()` returning
# f"{title} by {author}".
# (Reviews Day 10: classes & objects)

# YOUR CODE HERE


class BookReviewSolution:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def summary(self):
        return f"{self.title} by {self.author}"


# SOLUTION:
# review_book = BookReviewSolution("Ikigai", "Hector Garcia")
# print(review_book.summary())
# Expected output: Ikigai by Hector Garcia


# ════════════════════════════════════════════════════════════
# SECTION B: Inheritance & super()
# ════════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION B: Inheritance & super()")
print("=" * 50)

# ── Problem B1 ──
# 🟢 Warm-up
# Create a parent class `Animal` with attribute `name` and method
# `speak()` returning f"{self.name} makes a sound". Create a child class
# `Cat(Animal)` that does NOT override anything.

# YOUR CODE HERE


class AnimalSolutionB1:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class CatSolutionB1(AnimalSolutionB1):
    pass


# SOLUTION:
# whiskers = CatSolutionB1("Whiskers")
# print(whiskers.speak())
# Expected output: Whiskers makes a sound

print("-" * 50)

# ── Problem B2 ──
# 🟢 Warm-up
# Create a class `Vehicle` with `__init__(self, brand)`. Create a child
# class `Bike(Vehicle)` whose `__init__` accepts `brand` and `cc`
# (engine size), calling `super().__init__(brand)` for the shared part.

brand_input, cc_input = "Royal Enfield", 350  # simulating input()

# YOUR CODE HERE


class VehicleSolutionB2:
    def __init__(self, brand):
        self.brand = brand


class BikeSolutionB2(VehicleSolutionB2):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc


# SOLUTION:
# my_bike = BikeSolutionB2(brand_input, cc_input)
# print(my_bike.brand, my_bike.cc)
# Expected output: Royal Enfield 350

print("-" * 50)

# ── Problem B3 ──
# 🟡 Core
# Create a class `Person` with `__init__(self, name, age)` and a method
# `intro()` returning f"I am {name}, {age} years old". Create a child
# class `Teacher(Person)` that adds `subject` and OVERRIDES `intro()` to
# return the parent's intro() plus f", I teach {subject}".

name_input, age_input, subject_input = "Meera", 34, "Mathematics"  # simulating input()

# YOUR CODE HERE


class PersonSolutionB3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return f"I am {self.name}, {self.age} years old"


class TeacherSolutionB3(PersonSolutionB3):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def intro(self):
        return f"{super().intro()}, I teach {self.subject}"


# SOLUTION:
# meera_teacher = TeacherSolutionB3(name_input, age_input, subject_input)
# print(meera_teacher.intro())
# Expected output: I am Meera, 34 years old, I teach Mathematics

print("-" * 50)

# ── Problem B4 ──
# 🟡 Core
# Create three-level inheritance: `Shape` (attribute `color`) ->
# `Polygon(Shape)` (adds `num_sides`) -> `Pentagon(Polygon)` (sets
# `num_sides` to 5 automatically, only takes `color` as input).
# Add a method `describe()` on Shape returning
# f"A {self.color} shape with {self.num_sides} sides" and call it on
# a Pentagon instance.

color_input = "blue"  # simulating input()

# YOUR CODE HERE


class ShapeSolutionB4:
    def __init__(self, color, num_sides):
        self.color = color
        self.num_sides = num_sides

    def describe(self):
        return f"A {self.color} shape with {self.num_sides} sides"


class PolygonSolutionB4(ShapeSolutionB4):
    def __init__(self, color, num_sides):
        super().__init__(color, num_sides)


class PentagonSolutionB4(PolygonSolutionB4):
    def __init__(self, color):
        super().__init__(color, num_sides=5)


# SOLUTION:
# blue_pentagon = PentagonSolutionB4(color_input)
# print(blue_pentagon.describe())
# Expected output: A blue shape with 5 sides

print("-" * 50)

# ── Problem B5 ──
# 🔴 Challenge
# Create a class `Employee` with `__init__(self, name, base_salary)` and
# method `total_pay()` returning `base_salary`. Create `Manager(Employee)`
# that adds `bonus` and overrides `total_pay()` to return
# `super().total_pay() + bonus`. Create `Director(Manager)` that adds
# `stock_units` (each worth Rs.100) and overrides `total_pay()` to return
# `super().total_pay() + stock_units * 100`.
# Verify the final amount for a Director with base_salary=80000,
# bonus=20000, stock_units=50.

base_salary_input, bonus_input, stock_units_input = 80000, 20000, 50  # simulating input()

# YOUR CODE HERE


class EmployeeSolutionB5:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_pay(self):
        return self.base_salary


class ManagerSolutionB5(EmployeeSolutionB5):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def total_pay(self):
        return super().total_pay() + self.bonus


class DirectorSolutionB5(ManagerSolutionB5):
    def __init__(self, name, base_salary, bonus, stock_units):
        super().__init__(name, base_salary, bonus)
        self.stock_units = stock_units

    def total_pay(self):
        return super().total_pay() + self.stock_units * 100


# SOLUTION:
# sample_director = DirectorSolutionB5("Vikram", base_salary_input, bonus_input, stock_units_input)
# print(sample_director.total_pay())
# Expected output: 105000


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections in this file: A (Prior Days Review), B (Inheritance & super())
# Difficulty breakdown: 4 Warm-up, 4 Core, 1 Challenge = 9 problems
#
# Next file (day11_practise_problems_02_encapsulation_polymorphism.py)
# covers: Polymorphism & Encapsulation problems (Section C)

if __name__ == "__main__":
    print("-" * 50)
    print("Day 11 Practice Problems, File 1 complete")
