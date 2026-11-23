"""
══════════════════════════════════════════════════════════════
 PYTHON IN 30 DAYS  |  DAY 6  |  PRACTICE PROBLEMS: FUNCTIONS
══════════════════════════════════════════════════════════════

Day   : 6 (Functions and scope)    Part : 1-part day
Scope : def, parameters, return, defaults, keyword arguments, multiple
        return values, scope, helper functions. Reviews Days 3-5.
        Ends with PaisaTracker-style problems.
How to run : python day06_practise_problems.py   (needs no input)

Difficulty legend:  🟢 Warm-up   🟡 Core   🔴 Challenge

Section index:
  Section A: Review of earlier days (Days 3-5) (3 problems)
  Section B: Function basics: def, call, parameters, return (5 problems)
  Section C: Defaults, keyword arguments and multiple return values (4 problems)
  Section D: Scope, helper functions and changing lists (4 problems)
  Section E: Mixed challenges with PaisaTracker (4 problems)

How to use this file:
  1. Read the prompt and the expected output.
  2. Write your code where it says # YOUR CODE HERE.
  3. Run the file and compare with the expected output.
  4. Stuck? Peek at the commented # SOLUTION block. Try first!
  5. Never use the real input() here. Use the lists provided.
"""


# ══════════════════════════════════════════════════════════════
# SECTION A: Review of earlier days (Days 3-5)
# ══════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────
# Problem A1  [🟢 Warm-up]  Marks label (Day 3)
# ──────────────────────────────────────────────────────────────
# Print the result label for the marks: 75 or more is "distinction", 60 or more is "first class",
# 40 or more is "pass", otherwise "fail".
#
# Expected output:
#   72 marks: first class

print("Problem A1")
marks = 72
# YOUR CODE HERE

# SOLUTION:
# if marks >= 75:
#     label = "distinction"
# elif marks >= 60:
#     label = "first class"
# elif marks >= 40:
#     label = "pass"
# else:
#     label = "fail"
# print(f"{marks} marks: {label}")
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem A2  [🟡 Core]  Big expenses (Day 4)
# ──────────────────────────────────────────────────────────────
# Use a list comprehension to build a list of the NAMES of expenses above 100,
# then print it and the sum of all the amounts.
#
# Expected output:
#   ['groceries', 'movie']
#   1110

print("Problem A2")
expenses = [
    {"name": "chai", "amount": 20},
    {"name": "groceries", "amount": 640},
    {"name": "movie", "amount": 450},
]
# YOUR CODE HERE

# SOLUTION:
# big = [e["name"] for e in expenses if e["amount"] > 100]
# print(big)
# print(sum(e["amount"] for e in expenses))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem A3  [🟡 Core]  Savings months (Day 5)
# ──────────────────────────────────────────────────────────────
# Priya saves ₹700 a month. Use a while loop to find how many months she needs to reach ₹5000.
#
# Expected output:
#   8 months, saved ₹5600

print("Problem A3")
saved = 0
months = 0
# YOUR CODE HERE

# SOLUTION:
# while saved < 5000:
#     saved += 700
#     months += 1
# print(f"{months} months, saved ₹{saved}")
print("-" * 50)

# ══════════════════════════════════════════════════════════════
# SECTION B: Function basics: def, call, parameters, return
# ══════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────
# Problem B1  [🟢 Warm-up]  Say hello
# ──────────────────────────────────────────────────────────────
# Write a function `say_hello()` with no parameters that prints Namaste from PaisaTracker!
# Call it three times.
#
# Expected output:
#   Namaste from PaisaTracker!
#   Namaste from PaisaTracker!
#   Namaste from PaisaTracker!

print("Problem B1")
# YOUR CODE HERE

# SOLUTION:
# def say_hello():
#     print("Namaste from PaisaTracker!")
#
# say_hello()
# say_hello()
# say_hello()
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem B2  [🟢 Warm-up]  Greet by name
# ──────────────────────────────────────────────────────────────
# Write `greet(name)` that prints Hello, <name>! Call it for Priya and Arjun.
#
# Expected output:
#   Hello, Priya!
#   Hello, Arjun!

print("Problem B2")
# YOUR CODE HERE

# SOLUTION:
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Priya")
# greet("Arjun")
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem B3  [🟢 Warm-up]  Rupee text
# ──────────────────────────────────────────────────────────────
# Write `rupees(amount)` that RETURNS text like ₹250. Print rupees(250).
#
# Expected output:
#   ₹250

print("Problem B3")
# YOUR CODE HERE

# SOLUTION:
# def rupees(amount):
#     return f"₹{amount}"
#
# print(rupees(250))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem B4  [🟡 Core]  Total of prices
# ──────────────────────────────────────────────────────────────
# Write `calculate_total(prices)` that RETURNS the total using a for loop (do not use sum()).
# Test it on [20, 85, 640] and on an empty list.
#
# Expected output:
#   745
#   0

print("Problem B4")
# YOUR CODE HERE

# SOLUTION:
# def calculate_total(prices):
#     total = 0
#     for price in prices:
#         total += price
#     return total
#
# print(calculate_total([20, 85, 640]))
# print(calculate_total([]))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem B5  [🟡 Core]  Valid amount?
# ──────────────────────────────────────────────────────────────
# Write `is_valid_amount(text)` that RETURNS True only if the text is made of digits and is above zero.
# Test it on "250", "abc" and "0".
#
# Expected output:
#   True
#   False
#   False

print("Problem B5")
# YOUR CODE HERE

# SOLUTION:
# def is_valid_amount(text):
#     return text.isdigit() and int(text) > 0
#
# print(is_valid_amount("250"))
# print(is_valid_amount("abc"))
# print(is_valid_amount("0"))
print("-" * 50)

# ══════════════════════════════════════════════════════════════
# SECTION C: Defaults, keyword arguments and multiple return values
# ══════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────
# Problem C1  [🟡 Core]  GST with a default
# ──────────────────────────────────────────────────────────────
# Write `add_gst(amount, rate=18)` that RETURNS the amount plus GST.
# Print add_gst(250) and add_gst(250, 5).
#
# Expected output:
#   295.0
#   262.5

print("Problem C1")
# YOUR CODE HERE

# SOLUTION:
# def add_gst(amount, rate=18):
#     return amount + amount * rate / 100
#
# print(add_gst(250))
# print(add_gst(250, 5))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem C2  [🟡 Core]  Keyword arguments
# ──────────────────────────────────────────────────────────────
# Write `make_expense(name, amount, category="misc")` that RETURNS a dict.
# Call it with keyword arguments in a different order, and once without a category.
#
# Expected output:
#   {'name': 'auto-rickshaw', 'amount': 85, 'category': 'travel'}
#   {'name': 'chai', 'amount': 20, 'category': 'misc'}

print("Problem C2")
# YOUR CODE HERE

# SOLUTION:
# def make_expense(name, amount, category="misc"):
#     return {"name": name, "amount": amount, "category": category}
#
# print(make_expense(amount=85, name="auto-rickshaw", category="travel"))
# print(make_expense("chai", 20))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem C3  [🟡 Core]  Smallest and largest
# ──────────────────────────────────────────────────────────────
# Write `min_and_max(amounts)` that returns BOTH the smallest and the largest (use a loop).
# Unpack the result and print: Smallest ₹45, largest ₹300
#
# Expected output:
#   Smallest ₹45, largest ₹300

print("Problem C3")
# YOUR CODE HERE

# SOLUTION:
# def min_and_max(amounts):
#     smallest = amounts[0]
#     largest = amounts[0]
#     for amount in amounts:
#         if amount < smallest:
#             smallest = amount
#         if amount > largest:
#             largest = amount
#     return smallest, largest
#
# low, high = min_and_max([120, 45, 300, 80])
# print(f"Smallest ₹{low}, largest ₹{high}")
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem C4  [🔴 Challenge]  Safe average
# ──────────────────────────────────────────────────────────────
# Write `average_amount(amounts)` that RETURNS the average rounded to 2 decimals,
# or 0 for an empty list. Test both cases.
#
# Expected output:
#   159.0
#   0

print("Problem C4")
# YOUR CODE HERE

# SOLUTION:
# def average_amount(amounts):
#     if len(amounts) == 0:
#         return 0
#     return round(sum(amounts) / len(amounts), 2)
#
# print(average_amount([120, 45, 300, 80, 250]))
# print(average_amount([]))
print("-" * 50)

# ══════════════════════════════════════════════════════════════
# SECTION D: Scope, helper functions and changing lists
# ══════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────
# Problem D1  [🟡 Core]  Do not touch the global
# ──────────────────────────────────────────────────────────────
# Write `increase_budget(budget, extra)` that RETURNS the new budget WITHOUT changing the global `budget`.
# Print the global budget and the new budget.
#
# Expected output:
#   5000
#   6500

print("Problem D1")
budget = 5000
# YOUR CODE HERE

# SOLUTION:
# def increase_budget(budget, extra):
#     budget = budget + extra
#     return budget
#
# new_budget = increase_budget(budget, 1500)
# print(budget)
# print(new_budget)
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem D2  [🟡 Core]  Limit constant
# ──────────────────────────────────────────────────────────────
# Use the global constant LIMIT inside `is_above_limit(amount)` that RETURNS True or False.
# Test it on 640 and 20.
#
# Expected output:
#   True
#   False

print("Problem D2")
LIMIT = 500
# YOUR CODE HERE

# SOLUTION:
# def is_above_limit(amount):
#     return amount > LIMIT
#
# print(is_above_limit(640))
# print(is_above_limit(20))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem D3  [🟡 Core]  Change a list in place
# ──────────────────────────────────────────────────────────────
# Write `add_item(items, item)` that appends to the list it receives (no return).
# Call it twice and print the list.
#
# Expected output:
#   ['atta', 'dal', 'rice']

print("Problem D3")
shopping = ["atta"]
# YOUR CODE HERE

# SOLUTION:
# def add_item(items, item):
#     items.append(item)
#
# add_item(shopping, "dal")
# add_item(shopping, "rice")
# print(shopping)
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem D4  [🔴 Challenge]  Report with helper functions
# ──────────────────────────────────────────────────────────────
# Write `expense_line(expense)` that RETURNS text like `chai - ₹20 (food)`, and `show_report(expenses)` that
# prints each line (using expense_line) and then the total (using calculate_total).
#
# Expected output:
#   chai - ₹20 (food)
#   metro - ₹30 (travel)
#   Total: ₹50

print("Problem D4")
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

expenses = [
    {"name": "chai", "amount": 20, "category": "food"},
    {"name": "metro", "amount": 30, "category": "travel"},
]
# YOUR CODE HERE

# SOLUTION:
# def expense_line(expense):
#     return f"{expense['name']} - ₹{expense['amount']} ({expense['category']})"
#
# def show_report(expenses):
#     for expense in expenses:
#         print(expense_line(expense))
#     print(f"Total: ₹{calculate_total(expenses)}")
#
# show_report(expenses)
print("-" * 50)

# ══════════════════════════════════════════════════════════════
# SECTION E: Mixed challenges with PaisaTracker
# ══════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────
# Problem E1  [🟡 Core]  PaisaTracker: category totals
# ──────────────────────────────────────────────────────────────
# Write `category_totals(expenses)` that RETURNS a dict of totals per category. Print the result.
#
# Expected output:
#   {'food': 660, 'travel': 85}

print("Problem E1")
expenses = [
    {"name": "chai", "amount": 20, "category": "food"},
    {"name": "auto-rickshaw", "amount": 85, "category": "travel"},
    {"name": "groceries", "amount": 640, "category": "food"},
]
# YOUR CODE HERE

# SOLUTION:
# def category_totals(expenses):
#     totals = {}
#     for expense in expenses:
#         category = expense["category"]
#         if category in totals:
#             totals[category] += expense["amount"]
#         else:
#             totals[category] = expense["amount"]
#     return totals
#
# print(category_totals(expenses))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem E2  [🔴 Challenge]  PaisaTracker: filter by category
# ──────────────────────────────────────────────────────────────
# Write `expenses_in_category(expenses, category)` that RETURNS only the matching expenses.
# Print how many travel expenses there are and the total of their amounts.
#
# Expected output:
#   2 travel expenses, total ₹115

print("Problem E2")
expenses = [
    {"name": "chai", "amount": 20, "category": "food"},
    {"name": "auto-rickshaw", "amount": 85, "category": "travel"},
    {"name": "groceries", "amount": 640, "category": "food"},
    {"name": "metro", "amount": 30, "category": "travel"},
]
# YOUR CODE HERE

# SOLUTION:
# def expenses_in_category(expenses, category):
#     matches = []
#     for expense in expenses:
#         if expense["category"] == category:
#             matches.append(expense)
#     return matches
#
# travel = expenses_in_category(expenses, "travel")
# total = 0
# for expense in travel:
#     total += expense["amount"]
# print(f"{len(travel)} travel expenses, total ₹{total}")
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem E3  [🔴 Challenge]  PaisaTracker: biggest expense
# ──────────────────────────────────────────────────────────────
# Write `biggest_expense(expenses)` that RETURNS the expense with the largest amount,
# or None for an empty list. Test both cases.
#
# Expected output:
#   {'name': 'groceries', 'amount': 640}
#   None

print("Problem E3")
expenses = [
    {"name": "chai", "amount": 20},
    {"name": "groceries", "amount": 640},
    {"name": "metro", "amount": 30},
]
# YOUR CODE HERE

# SOLUTION:
# def biggest_expense(expenses):
#     if len(expenses) == 0:
#         return None
#     biggest = expenses[0]
#     for expense in expenses:
#         if expense["amount"] > biggest["amount"]:
#             biggest = expense
#     return biggest
#
# print(biggest_expense(expenses))
# print(biggest_expense([]))
print("-" * 50)

# ──────────────────────────────────────────────────────────────
# Problem E4  [🔴 Challenge]  PaisaTracker: mini menu with functions
# ──────────────────────────────────────────────────────────────
# Write `add_expense(expenses, name, amount)` and `calculate_total(expenses)`, then run a menu loop on the
# simulated answers. 1 = add (asks name and amount), 2 = show total, 3 = exit.
#
# Expected output:
#   Added chai - ₹20
#   Added metro - ₹30
#   Total: ₹50
#   Goodbye!

print("Problem E4")
typed = ["1", "chai", "20", "1", "metro", "30", "2", "3"]
expenses = []
# YOUR CODE HERE

# SOLUTION:
# def add_expense(expenses, name, amount):
#     expenses.append({"name": name, "amount": amount})
#
# def calculate_total(expenses):
#     total = 0
#     for expense in expenses:
#         total += expense["amount"]
#     return total
#
# running = True
# while running:
#     choice = typed.pop(0)
#     if choice == "1":
#         name = typed.pop(0)
#         amount = int(typed.pop(0))
#         add_expense(expenses, name, amount)
#         print(f"Added {name} - ₹{amount}")
#     elif choice == "2":
#         print(f"Total: ₹{calculate_total(expenses)}")
#     elif choice == "3":
#         running = False
#         print("Goodbye!")
print("-" * 50)

# ══════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════
# Total problems : 20
#   Section A: 3 problems - Review of earlier days (Days 3-5)
#   Section B: 5 problems - Function basics: def, call, parameters, return
#   Section C: 4 problems - Defaults, keyword arguments and multiple return values
#   Section D: 4 problems - Scope, helper functions and changing lists
#   Section E: 4 problems - Mixed challenges with PaisaTracker
# Difficulty     : 🟢 Warm-up 4  |  🟡 Core 11  |  🔴 Challenge 5
#
# Next problem set (Day 7 Part 1: Strings and formatting):
#   You will format PaisaTracker output as a neat table using f-strings and string methods.
print("Day 6 practice set ready. Happy coding!")
