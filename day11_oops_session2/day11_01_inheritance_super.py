"""
Day 11 — Object-Oriented Programming II
File 1 of 3: Inheritance & super()

What this file covers:
    - What inheritance is and why it matters
    - Creating a child class that extends a parent class
    - Overriding methods in a child class
    - Using super() to call the parent class's methods
    - Multi-level inheritance (grandparent -> parent -> child)

Prerequisites:
    - Day 10: Classes, objects, __init__, self, instance variables, instance methods

How to run:
    python day11_01_inheritance_super.py
"""

# ════════════════════════════════════════════════════════════
# SECTION 1: Why Inheritance?
# ════════════════════════════════════════════════════════════
# On Day 10 we built standalone classes. In real programs, many classes
# share common behaviour. Instead of copy-pasting code, we let a "child"
# class inherit attributes and methods from a "parent" class.
#
# Syntax:
#     class Child(Parent):
#         ...
#
# This means: "Child IS-A Parent, plus some extra stuff."

print("=" * 50)
print("SECTION 1: A Basic Parent Class")
print("=" * 50)


class Employee:
    """A generic employee at a company in Mumbai."""

    def __init__(self, name, employee_id, monthly_salary):
        self.name = name
        self.employee_id = employee_id
        self.monthly_salary = monthly_salary

    def describe(self):
        return f"{self.name} (ID: {self.employee_id}) earns Rs.{self.monthly_salary}/month"

    def annual_salary(self):
        return self.monthly_salary * 12


# Using the parent class on its own works exactly like Day 10.
generic_employee = Employee("Arjun Mehta", "EMP101", 45000)
print(generic_employee.describe())
# Output: Arjun Mehta (ID: EMP101) earns Rs.45000/month


# ── Concept: Creating a Child Class ──
# A Manager IS-A Employee, but also manages a team. Instead of rewriting
# name/employee_id/monthly_salary handling, Manager inherits from Employee.

print("-" * 50)
print("SECTION 2: Inheriting From Employee")
print("-" * 50)


class Manager(Employee):
    """A Manager is an Employee who also leads a team."""

    def __init__(self, name, employee_id, monthly_salary, team_size):
        # super().__init__() calls the PARENT's __init__ to set up the
        # shared attributes (name, employee_id, monthly_salary).
        super().__init__(name, employee_id, monthly_salary)
        # Now we add attributes that are specific to Manager.
        self.team_size = team_size

    def describe(self):
        # We OVERRIDE describe() to add extra detail, but we reuse the
        # parent's version with super() instead of repeating its logic.
        base_description = super().describe()
        return f"{base_description}, leading a team of {self.team_size}"


priya_manager = Manager("Priya Sharma", "MGR201", 90000, team_size=8)
print(priya_manager.describe())
# Output: Priya Sharma (ID: MGR201) earns Rs.90000/month, leading a team of 8
print(priya_manager.annual_salary())
# Output: 1080000 (inherited method, works without redefinition)


# ── Concept: Why super() Instead of Hardcoding ──
# If Employee.__init__ ever changes (e.g. adds a "department" field),
# every child class using super() automatically picks up the change.
# Hardcoding `self.name = name` again in Manager would duplicate logic
# and risk going out of sync with the parent.


# ════════════════════════════════════════════════════════════
# SECTION 3: Multi-Level Inheritance
# ════════════════════════════════════════════════════════════
# A child class can itself become a parent for another class.
# Employee -> Manager -> SeniorManager

print("-" * 50)
print("SECTION 3: Multi-Level Inheritance")
print("-" * 50)


class SeniorManager(Manager):
    """A SeniorManager is a Manager who also oversees other managers."""

    def __init__(self, name, employee_id, monthly_salary, team_size, managers_supervised):
        super().__init__(name, employee_id, monthly_salary, team_size)
        self.managers_supervised = managers_supervised

    def describe(self):
        base_description = super().describe()
        return f"{base_description}, supervising {self.managers_supervised} managers"


riya_senior = SeniorManager(
    "Riya Kapoor", "SRMGR301", 150000, team_size=20, managers_supervised=4
)
print(riya_senior.describe())
# Output: Riya Kapoor (ID: SRMGR301) earns Rs.150000/month, leading a team
#         of 20, supervising 4 managers

# Notice how describe() chains all the way up: SeniorManager calls Manager's
# describe(), which calls Employee's describe(). Each level adds its own bit.


# ════════════════════════════════════════════════════════════
# SECTION 4: isinstance() and Class Hierarchies
# ════════════════════════════════════════════════════════════

print("-" * 50)
print("SECTION 4: Checking Relationships With isinstance()")
print("-" * 50)

print(isinstance(riya_senior, SeniorManager))  # Output: True
print(isinstance(riya_senior, Manager))        # Output: True (inherited relationship)
print(isinstance(riya_senior, Employee))       # Output: True (grandparent relationship)
print(isinstance(generic_employee, Manager))   # Output: False (not a Manager)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════

print("-" * 50)
print("GUIDED EXAMPLE 1: Vehicle -> Car")
print("-" * 50)


class Vehicle:
    def __init__(self, brand, max_speed_kmph):
        self.brand = brand
        self.max_speed_kmph = max_speed_kmph

    def info(self):
        return f"{self.brand} vehicle, top speed {self.max_speed_kmph} km/h"


class Car(Vehicle):
    def __init__(self, brand, max_speed_kmph, num_doors):
        super().__init__(brand, max_speed_kmph)
        self.num_doors = num_doors

    def info(self):
        return f"{super().info()}, {self.num_doors} doors"


tata_car = Car("Tata Nexon", 165, 5)
print(tata_car.info())
# Output: Tata Nexon vehicle, top speed 165 km/h, 5 doors


print("-" * 50)
print("GUIDED EXAMPLE 2: BankAccount -> SavingsAccount")
print("-" * 50)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = super().deposit(interest)
        return self.balance


arjun_savings = SavingsAccount("Arjun", 10000, 0.05)
print(arjun_savings.apply_interest())
# Output: 10500.0


print("-" * 50)
print("GUIDED EXAMPLE 3: Shape -> Rectangle -> Square")
print("-" * 50)


class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is a {self.name}"


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side):
        # A Square is a Rectangle where length == width.
        super().__init__(side, side)
        self.name = "Square"  # override the inherited name


delhi_square = Square(4)
print(delhi_square.describe())  # Output: This is a Square
print(delhi_square.area())      # Output: 16


print("-" * 50)
print("GUIDED EXAMPLE 4: Student -> ScholarshipStudent")
print("-" * 50)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        status = "Pass" if self.marks >= 35 else "Fail"
        return f"{self.name}: {self.marks} marks ({status})"


class ScholarshipStudent(Student):
    def __init__(self, name, marks, scholarship_amount):
        super().__init__(name, marks)
        self.scholarship_amount = scholarship_amount

    def result(self):
        base_result = super().result()
        return f"{base_result}, Scholarship: Rs.{self.scholarship_amount}"


riya_student = ScholarshipStudent("Riya", 88, 20000)
print(riya_student.result())
# Output: Riya: 88 marks (Pass), Scholarship: Rs.20000


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Create a class `Animal` with attributes `name` and `sound`, and a method
# `make_sound()` that returns f"{self.name} says {self.sound}".
#
# Then create a class `Dog(Animal)` whose __init__ takes only `name`
# (always set sound to "Woof") and calls super().__init__() correctly.
#
# Expected output when you create Dog("Tommy") and call make_sound():
#   "Tommy says Woof"

# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file we covered:
#   - Why inheritance avoids duplicate code (Employee -> Manager -> SeniorManager)
#   - How super().__init__() reuses the parent constructor
#   - How super().method_name() reuses and extends parent methods
#   - Multi-level inheritance chains
#   - isinstance() for checking class relationships
#
# Next file (day11_02_polymorphism_encapsulation.py) covers:
#   - Polymorphism: same method name, different behaviour per class
#   - Encapsulation: name mangling and the @property decorator

if __name__ == "__main__":
    print("-" * 50)
    print("Day 11, File 1 complete: Inheritance & super()")
