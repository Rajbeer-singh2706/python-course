"""
Day 14 — Decorators & Closures — Practice Problem Set (File 2 of 2)

Cumulative scope: Days 1-14 (mixed challenges combine current + prior days)

Difficulty legend:
    🟢 Warm-up   — direct application of a single concept
    🟡 Core      — combines 2+ ideas, requires a bit more thought
    🔴 Challenge — multi-step, closer to a real mini-project

Section index (this file):
    Section D — Decorators From Scratch          (3 problems)
    Section E — Built-in Decorators               (3 problems)
    Section F — Mixed Challenges                  (3 problems)

(Section A, B, and C are in
 day14_practise_problems_01_first_class_closures.py)

How to run:
    python day14_practise_problems_02_decorators_builtin.py
"""

import functools


# ════════════════════════════════════════════════════════════════
# SECTION D — Decorators From Scratch
# ════════════════════════════════════════════════════════════════

# ── Problem D1 🟢 Warm-up ──
# Write a decorator `add_exclamation` that appends "!" to whatever
# string a decorated function returns. Apply it to `get_slogan()`
# which returns "Flipkart Big Billion Days".
#
# Expected output: Flipkart Big Billion Days!

# YOUR CODE HERE
def add_exclamation(func):
    pass


print("Problem D1:")
# SOLUTION:
def add_exclamation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"

    return wrapper


@add_exclamation
def get_slogan():
    return "Flipkart Big Billion Days"


print(get_slogan())
print("-" * 50)


# ── Problem D2 🟢 Warm-up ──
# Write a decorator `print_divider` that prints a line of 30 dashes
# BEFORE calling the decorated function, then returns its result
# unchanged. Apply it to `show_menu()` which returns "Today: Dal, Rice, Roti".
#
# Expected output:
#   ------------------------------
#   Today: Dal, Rice, Roti

# YOUR CODE HERE
def print_divider(func):
    pass


print("Problem D2:")
# SOLUTION:
def print_divider(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 30)
        return func(*args, **kwargs)

    return wrapper


@print_divider
def show_menu():
    return "Today: Dal, Rice, Roti"


print(show_menu())
print("-" * 50)


# ── Problem D3 🟡 Core ──
# Write a decorator `require_non_empty` that checks the FIRST positional
# argument passed to the decorated function; if it's an empty string,
# raise ValueError("Input cannot be empty"), otherwise call the function
# normally. Apply it to `greet(name)` which returns f"Hello, {name}!".
#
# Expected output:
#   Hello, Meera!
#   Caught: Input cannot be empty

# YOUR CODE HERE
def require_non_empty(func):
    pass


print("Problem D3:")
# SOLUTION:
def require_non_empty(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args and args[0] == "":
            raise ValueError("Input cannot be empty")
        return func(*args, **kwargs)

    return wrapper


@require_non_empty
def greet(name):
    return f"Hello, {name}!"


print(greet("Meera"))
try:
    greet("")
except ValueError as error:
    print(f"Caught: {error}")
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION E — Built-in Decorators
# ════════════════════════════════════════════════════════════════

# ── Problem E1 🟢 Warm-up ──
# Define class `TemperatureConverter` with a @staticmethod
# `celsius_to_fahrenheit(celsius)` returning celsius * 9/5 + 32.
# Call it directly on the class with 30.
#
# Expected output: 86.0

# YOUR CODE HERE
class TemperatureConverter:
    pass


print("Problem E1:")
# SOLUTION:
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32


print(TemperatureConverter.celsius_to_fahrenheit(30))
print("-" * 50)


# ── Problem E2 🟢 Warm-up ──
# Define class `Movie` with __init__(self, title, rating) and a
# @property `is_hit` returning True if rating >= 7.0, else False.
# Create a Movie("RRR", 8.8) and print its is_hit property.
#
# Expected output: True

# YOUR CODE HERE
class Movie:
    pass


print("Problem E2:")
# SOLUTION:
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    @property
    def is_hit(self):
        return self.rating >= 7.0


print(Movie("RRR", 8.8).is_hit)
print("-" * 50)


# ── Problem E3 🟡 Core ──
# Define class `Employee` with __init__(self, name, monthly_salary) and
# a @classmethod `from_annual(cls, name, annual_salary)` that converts
# annual salary to monthly (annual / 12, rounded to 2 decimals) and
# builds the instance via cls(...). Create an employee via
# from_annual("Sanjay", 960000) and print monthly_salary.
#
# Expected output: 80000.0

# YOUR CODE HERE
class Employee:
    pass


print("Problem E3:")
# SOLUTION:
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    @classmethod
    def from_annual(cls, name, annual_salary):
        return cls(name, round(annual_salary / 12, 2))


emp = Employee.from_annual("Sanjay", 960000)
print(emp.monthly_salary)
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION F — Mixed Challenges (current + prior days combined)
# ════════════════════════════════════════════════════════════════

# ── Problem F1 🔴 Challenge ──
# Combine closures + decorators: write a decorator FACTORY
# `max_calls(limit)` that only allows a function to be called `limit`
# times; on further calls, it returns the string "Call limit reached"
# instead of running the function (use a closure counter with
# `nonlocal`). Apply @max_calls(2) to `send_otp(mobile)` which returns
# f"OTP sent to {mobile}". Call it three times with "9876543210".
#
# Expected output:
#   OTP sent to 9876543210
#   OTP sent to 9876543210
#   Call limit reached

# YOUR CODE HERE
def max_calls(limit):
    pass


print("Problem F1:")
# SOLUTION:
def max_calls(limit):
    def decorator(func):
        calls_made = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls_made
            if calls_made >= limit:
                return "Call limit reached"
            calls_made += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


@max_calls(2)
def send_otp(mobile):
    return f"OTP sent to {mobile}"


print(send_otp("9876543210"))
print(send_otp("9876543210"))
print(send_otp("9876543210"))
print("-" * 50)


# ── Problem F2 🔴 Challenge ──
# Combine OOP (Day 10/11) + built-in decorators: define a class
# `Course` with __init__(self, title, total_seats, seats_filled=0), a
# @property `seats_available` (total_seats - seats_filled), a
# @property `is_full` (True if seats_available == 0), and a
# @classmethod `fully_booked(cls, title, total_seats)` that builds a
# Course with seats_filled == total_seats. Test with a course of 30
# seats, 30 filled, printing seats_available and is_full.
#
# Expected output:
#   0
#   True

# YOUR CODE HERE
class Course:
    pass


print("Problem F2:")
# SOLUTION:
class Course:
    def __init__(self, title, total_seats, seats_filled=0):
        self.title = title
        self.total_seats = total_seats
        self.seats_filled = seats_filled

    @property
    def seats_available(self):
        return self.total_seats - self.seats_filled

    @property
    def is_full(self):
        return self.seats_available == 0

    @classmethod
    def fully_booked(cls, title, total_seats):
        return cls(title, total_seats, seats_filled=total_seats)


python_course = Course.fully_booked("30-Day Python Course", 30)
print(python_course.seats_available)
print(python_course.is_full)
print("-" * 50)


# ── Problem F3 🔴 Challenge ──
# End-to-end: write a decorator `log_to_list(log)` — a decorator
# FACTORY that takes an existing list `log` and, each time the
# decorated function is called, appends
# f"{func.__name__} called with {args}" to that list, then returns the
# function's normal result (use functools.wraps). Apply it to a
# function `book_ticket(passenger, seat)` that returns
# f"{passenger} booked seat {seat}". Call it once with ("Priya", "A1"),
# then print the log list.
#
# Expected output:
#   Priya booked seat A1
#   ["book_ticket called with ('Priya', 'A1')"]

# YOUR CODE HERE
def log_to_list(log):
    pass


print("Problem F3:")
# SOLUTION:
def log_to_list(log):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log.append(f"{func.__name__} called with {args}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


booking_log = []


@log_to_list(booking_log)
def book_ticket(passenger, seat):
    return f"{passenger} booked seat {seat}"


print(book_ticket("Priya", "A1"))
print(booking_log)
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# Sections completed in this file:
#   D — Decorators From Scratch     (3 problems)
#   E — Built-in Decorators         (3 problems)
#   F — Mixed Challenges            (3 problems)
#
# Difficulty breakdown: 4x 🟢 Warm-up, 2x 🟡 Core, 3x 🔴 Challenge
#
# Combined with File 1 (Section A-C): 20 problems total for Day 14
#   🟢 Warm-up: 10   🟡 Core: 7   🔴 Challenge: 3   (20 total)
#
# Next: Day 15 practice problems will build on first-class functions
# with map(), filter(), reduce(), lambda, zip(), enumerate(), and
# sorted(key=...).

if __name__ == "__main__":
    print("\nPractice file 2 of 2 complete. Day 14 practice set finished!")
