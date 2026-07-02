"""
Day 5 — Functions & Scope
File 1 of 3: Function Basics

Covers:
    - Defining functions with `def`
    - Parameters and arguments
    - Return values
    - Default arguments

Prerequisites:
    - Day 2: Variables & Data Types
    - Day 3: Control Flow
    - Day 4: Loops

How to run:
    python day05_01_functions_basics.py
"""

# ════════════════════════════════════════════════════════
# SECTION A — Defining Functions with `def`
# ════════════════════════════════════════════════════════
#
# A function is a reusable block of code that performs a specific task.
# Instead of copy-pasting the same logic everywhere, we wrap it in a
# function and simply "call" it whenever we need it.
#
# Syntax:
#     def function_name():
#         # code block
#
# Every line inside the function must be indented (4 spaces).
# Calling the function is done using function_name().

# ── Concept: A Simple Function ──


def greet_student():
    print("Namaste! Welcome to Day 5 of the Python course.")


# Calling the function actually runs the code inside it
greet_student()
# Output: Namaste! Welcome to Day 5 of the Python course.

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION B — Parameters and Arguments
# ════════════════════════════════════════════════════════
#
# Parameters are placeholders listed in the function definition.
# Arguments are the actual values you pass in when calling the function.
#
#     def function_name(parameter1, parameter2):
#         # use parameter1, parameter2 here
#
#     function_name(argument1, argument2)

# ── Concept: Function with One Parameter ──


def greet_by_name(student_name):
    print(f"Namaste, {student_name}! Ready to learn functions today?")


greet_by_name("Priya")
# Output: Namaste, Priya! Ready to learn functions today?

greet_by_name("Arjun")
# Output: Namaste, Arjun! Ready to learn functions today?

print("-" * 50)

# ── Concept: Function with Multiple Parameters ──


def show_marks(student_name, subject, marks):
    print(f"{student_name} scored {marks} marks in {subject}.")


show_marks("Riya Deshmukh", "Mathematics", 92)
# Output: Riya Deshmukh scored 92 marks in Mathematics.

print("-" * 50)

# ── Concept: Keyword Arguments ──
# Arguments can be passed by keyword, in any order, using parameter=value.

show_marks(subject="Science", student_name="Sanjay Verma", marks=88)
# Output: Sanjay Verma scored 88 marks in Science.

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION C — Return Values
# ════════════════════════════════════════════════════════
#
# A function can send a result back to the caller using `return`.
# Without `return`, a function returns None by default.
# `return` also immediately exits the function.

# ── Concept: Returning a Value ──


def calculate_total(price, quantity):
    total = price * quantity
    return total


bill_amount = calculate_total(250, 3)
print(f"Total bill: Rs. {bill_amount}")
# Output: Total bill: Rs. 750

print("-" * 50)

# ── Concept: A Function with No Return ──


def log_purchase(item_name):
    print(f"Purchase logged: {item_name}")
    # no return statement here


result = log_purchase("Notebook")
print(f"Return value: {result}")
# Output:
# Purchase logged: Notebook
# Return value: None

print("-" * 50)

# ── Concept: Returning Multiple Values ──
# Python lets a function return more than one value, packed as a tuple.


def get_min_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = get_min_max([45, 78, 12, 90, 33])
print(f"Lowest: {lowest}, Highest: {highest}")
# Output: Lowest: 12, Highest: 90

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION D — Default Arguments
# ════════════════════════════════════════════════════════
#
# A parameter can have a default value, used when the caller doesn't
# supply that argument. Default parameters must come AFTER non-default
# ones in the function signature.

# ── Concept: Function with a Default Argument ──


def apply_discount(price, discount_percent=10):
    discounted_price = price - (price * discount_percent / 100)
    return discounted_price


# Using the default discount (10%)
print(f"Price after default discount: Rs. {apply_discount(1000)}")
# Output: Price after default discount: Rs. 900.0

# Overriding the default discount
print(f"Price after custom discount: Rs. {apply_discount(1000, 25)}")
# Output: Price after custom discount: Rs. 750.0

print("-" * 50)

# ── Concept: Multiple Default Arguments ──


def book_ticket(destination, travel_class="Sleeper", passengers=1):
    print(f"Booking {passengers} ticket(s) to {destination} in {travel_class} class.")


book_ticket("Mumbai")
# Output: Booking 1 ticket(s) to Mumbai in Sleeper class.

book_ticket("Delhi", "AC 3 Tier", 4)
# Output: Booking 4 ticket(s) to Delhi in AC 3 Tier class.

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION E — Guided Examples
# ════════════════════════════════════════════════════════

# Example 1: Simple greeting generator for Mumbai students
print("Example 1: Batch Greeting")


def welcome_batch(names):
    for name in names:
        print(f"Welcome to the batch, {name}!")


welcome_batch(["Priya", "Arjun", "Riya"])
print("-" * 50)

# Example 2: Grocery bill calculator (Mumbai delivery context)
print("Example 2: Grocery Bill Calculator")


def calculate_grocery_bill(item_prices, delivery_fee=30):
    subtotal = sum(item_prices)
    grand_total = subtotal + delivery_fee
    return grand_total


order_total = calculate_grocery_bill([120, 85, 45, 60])
print(f"Grand total for the Mumbai grocery order: Rs. {order_total}")
print("-" * 50)

# Example 3: Attendance percentage calculator
print("Example 3: Attendance Percentage")


def attendance_percentage(days_present, total_days):
    if total_days == 0:
        return 0
    return round((days_present / total_days) * 100, 2)


print(f"Arjun's attendance: {attendance_percentage(85, 90)}%")
print("-" * 50)

# Example 4: Auto-rickshaw fare estimator with a default base fare
print("Example 4: Auto Fare Estimator")


def estimate_fare(distance_km, base_fare=30, rate_per_km=12):
    return base_fare + (distance_km * rate_per_km)


print(f"Fare for 5 km trip in Delhi: Rs. {estimate_fare(5)}")
print(f"Fare for 5 km trip (higher base fare): Rs. {estimate_fare(5, base_fare=50)}")
print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Write a function called `movie_ticket_price` that:
#   1. Takes parameters: age, and day_type (default value "weekday")
#   2. If age is under 12, the ticket is Rs. 100
#   3. Otherwise, if day_type is "weekend", the ticket is Rs. 250
#   4. Otherwise (weekday, age 12+), the ticket is Rs. 180
#   5. Returns the ticket price
#
# Test it with a few different students and print the results.
#
# Expected output (example):
#   Riya (age 10, weekday): Rs. 100
#   Arjun (age 20, weekend): Rs. 250
#   Priya (age 25, weekday): Rs. 180

# YOUR CODE HERE


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# In this file, you learned:
#   - How to define and call functions with `def`
#   - How to pass parameters and arguments (positional & keyword)
#   - How to return values from a function (including multiple values)
#   - How to set default argument values
#
# Next up (File 2 of 3): *args and **kwargs — handling a variable
# number of arguments in your functions.
