"""
Day 5 — Functions & Scope
File 2 of 3: *args and **kwargs

Covers:
    - *args — variable number of positional arguments
    - **kwargs — variable number of keyword arguments
    - Combining regular parameters with *args and **kwargs

Prerequisites:
    - Day 5, File 1: Function Basics (def, parameters, return, defaults)

How to run:
    python day05_02_args_kwargs.py
"""

# ════════════════════════════════════════════════════════
# SECTION A — *args (Variable Positional Arguments)
# ════════════════════════════════════════════════════════
#
# Sometimes we don't know in advance how many arguments will be passed
# to a function. `*args` collects any number of positional arguments
# into a tuple.
#
#     def function_name(*args):
#         # args is a tuple of all the values passed in

# ── Concept: Basic *args ──


def total_marks(*marks):
    print(f"Marks received: {marks}")
    print(f"Type of args: {type(marks)}")
    return sum(marks)


result = total_marks(85, 90, 78)
print(f"Total: {result}")
# Output:
# Marks received: (85, 90, 78)
# Type of args: <class 'tuple'>
# Total: 253

print("-" * 50)

# ── Concept: *args with Zero or Many Arguments ──


def announce_students(*names):
    if not names:
        print("No students to announce.")
        return
    for name in names:
        print(f"- {name}")


announce_students()
# Output: No students to announce.

announce_students("Priya", "Arjun", "Riya Deshmukh")
# Output:
# - Priya
# - Arjun
# - Riya Deshmukh

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION B — **kwargs (Variable Keyword Arguments)
# ════════════════════════════════════════════════════════
#
# `**kwargs` collects any number of keyword arguments into a dictionary.
#
#     def function_name(**kwargs):
#         # kwargs is a dict of all the key=value pairs passed in

# ── Concept: Basic **kwargs ──


def student_profile(**details):
    print(f"Details received: {details}")
    print(f"Type of kwargs: {type(details)}")
    for key, value in details.items():
        print(f"  {key}: {value}")


student_profile(name="Sanjay Verma", city="Mumbai", age=21)
# Output:
# Details received: {'name': 'Sanjay Verma', 'city': 'Mumbai', 'age': 21}
# Type of kwargs: <class 'dict'>
#   name: Sanjay Verma
#   city: Mumbai
#   age: 21

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION C — Combining Regular Params, *args, and **kwargs
# ════════════════════════════════════════════════════════
#
# The correct order in a function signature is:
#     def function_name(positional, *args, default=value, **kwargs):
#
# Regular positional parameters come first, then *args,
# then any default keyword parameters, then **kwargs.

# ── Concept: Combining Everything ──


def create_invoice(customer_name, *item_prices, discount=0, **extra_info):
    subtotal = sum(item_prices)
    final_total = subtotal - discount
    print(f"Invoice for: {customer_name}")
    print(f"Items total: Rs. {subtotal}")
    print(f"Discount applied: Rs. {discount}")
    print(f"Final total: Rs. {final_total}")
    for key, value in extra_info.items():
        print(f"{key.title()}: {value}")


create_invoice("Priya", 500, 300, 150, discount=50, city="Mumbai", payment="UPI")
# Output:
# Invoice for: Priya
# Items total: Rs. 950
# Discount applied: Rs. 50
# Final total: Rs. 900
# City: Mumbai
# Payment: UPI

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION D — Guided Examples
# ════════════════════════════════════════════════════════

# Example 1: Sum any number of expense amounts
print("Example 1: Flexible Expense Summer")


def total_expenses(*amounts):
    return sum(amounts)


print(f"Total: Rs. {total_expenses(120, 340, 75, 900, 60)}")
print("-" * 50)

# Example 2: Building a student report card with **kwargs
print("Example 2: Report Card Builder")


def report_card(student_name, **subject_marks):
    print(f"Report Card for {student_name}:")
    for subject, marks in subject_marks.items():
        print(f"  {subject}: {marks}")
    average = sum(subject_marks.values()) / len(subject_marks)
    print(f"  Average: {round(average, 2)}")


report_card("Arjun", Maths=88, Science=92, English=79)
print("-" * 50)

# Example 3: Combining *args and **kwargs for a Mumbai food order
print("Example 3: Food Order Summary")


def food_order(customer_name, *dishes, **order_info):
    print(f"Order for {customer_name}: {', '.join(dishes)}")
    for key, value in order_info.items():
        print(f"  {key}: {value}")


food_order("Riya Deshmukh", "Vada Pav", "Pav Bhaji", area="Mumbai", payment_mode="Cash")
print("-" * 50)

# Example 4: Forwarding arguments to another function
print("Example 4: Forwarding Arguments")


def log_call(*args, **kwargs):
    print(f"Called with args={args}, kwargs={kwargs}")


def register_student(name, age, **kwargs):
    log_call(name, age, **kwargs)
    print(f"Registered {name}, age {age}")


register_student("Sanjay Verma", 22, city="Delhi", course="Python")
print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Write a function called `travel_summary` that:
#   1. Takes a traveller_name as the first parameter
#   2. Accepts any number of city names using *args
#   3. Accepts any number of extra details using **kwargs
#      (e.g. mode="Train", budget=5000)
#   4. Prints a summary like:
#        Traveller: Arjun
#        Cities: Mumbai, Delhi, Pune
#        mode: Train
#        budget: 5000
#
# Test it by calling it with at least 3 cities and 2 keyword details.

# YOUR CODE HERE


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# In this file, you learned:
#   - How *args collects extra positional arguments into a tuple
#   - How **kwargs collects extra keyword arguments into a dict
#   - How to combine regular parameters, *args, defaults, and **kwargs
#     in the correct order
#
# Next up (File 3 of 3): Scope and the LEGB rule — where Python
# looks for variable names.
