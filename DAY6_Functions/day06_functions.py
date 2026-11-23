"""
══════════════════════════════════════════════════════════════════
 PYTHON IN 30 DAYS  |  DAY 6  |  FUNCTIONS AND SCOPE
══════════════════════════════════════════════════════════════════

Topic       : def, parameters, return, defaults, keyword arguments,
              multiple return values, scope (local / global), design
Project     : PaisaTracker v0 "Calculator" is COMPLETE today
Builds on   : Day 2 (variables), Day 3 (if / elif / else),
              Day 4 (lists, dicts), Day 5 (for and while loops)
How to run  : python day06_functions.py   (macOS / Linux: python3)

This file follows the same story, syntax, examples, concepts and
PaisaTracker order as the three Day 6 notebooks. It never uses the
real input(): typed answers come from a list called simulated_replies.
Set USE_REAL_INPUT = True near the end to type your own answers.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: A story
# ══════════════════════════════════════════════════════════════
#
# ── Priya fixes a bug... in only one place ──
# Priya's PaisaTracker is growing. Her menu works, but her code has a problem. The same four lines that add up all the expenses are copied in three places: the report, the menu option "Show total", and the budget check.
#
# Yesterday she found a mistake in the total calculation. She fixed it in the report. She forgot the other two. Now the report says one amount and the menu says another!
#
# "There must be a way to write this once and use it everywhere," Priya says.
#
# Her teacher smiles and shows her the chai stall again.
#
#   A customer does not explain how to make chai every time. He just says "one cutting chai".
#   The chai-wala already knows the recipe. The customer gives a small instruction (how many cups), the chai-wala follows the recipe, and hands back the finished cup.
#
# A function is exactly that: a recipe with a name. You write the steps once. Then you ask for it by name, as many times as you like.
#
# ── Where else do we see this? ──
# - The UPI "Pay" button: same steps every time, different amount and receiver each time.
# - A dabbawala route in Mumbai: the same process every day, a new tiffin each day.
# - A mixer grinder: you put things in, press the button, and get something out.


# ── Priya's problem, in code ──
# Same four lines, copied three times:

expenses = [
    {"name": "chai", "amount": 20},
    {"name": "groceries", "amount": 640},
    {"name": "metro", "amount": 30},
]

# place 1: the report
total = 0
for expense in expenses:
    total += expense["amount"]
print("Report total:", total)

# place 2: the menu option "Show total"
total = 0
for expense in expenses:
    total += expense["amount"]
print("Menu total:", total)

# place 3: the budget check
total = 0
for expense in expenses:
    total += expense["amount"]
if total > 500:
    print("Budget check: over 500!")
# Output:
#   Report total: 690
#   Menu total: 690
#   Budget check: over 500!


# ── The same program with a function ──
# Write the recipe once, then call it by name:

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

print("Report total:", calculate_total(expenses))
print("Menu total:", calculate_total(expenses))
if calculate_total(expenses) > 500:
    print("Budget check: over 500!")
# Output:
#   Report total: 690
#   Menu total: 690
#   Budget check: over 500!


# What we gained
# | Problem before | With a function |
# |----------------|-----------------|
# | Same code copied 3 times | Written once |
# | A bug must be fixed in 3 places | Fixed in one place |
# | Hard to read | `calculate_total(expenses)` says what it does |
# | Hard to test | Test it on its own |


# ══════════════════════════════════════════════════════════════
# PART 2: The syntax
# ══════════════════════════════════════════════════════════════
#
# def function_name(parameters):
#     # lines of the function (indented by 4 spaces)
#     return result
#
# ── The parts of a function ──
# | Part | What it is | Example |
# |------|------------|---------|
# | `def` | the keyword that says "I am defining a function" | `def` |
# | name | what the job is called (lowercase with underscores) | `calculate_total` |
# | `( )` and parameters | the inputs the function needs (can be empty) | `(expenses)` |
# | `:` | the colon ends the first line | `:` |
# | body | the indented lines that do the work | `total = 0 ...` |
# | `return` | sends the answer back (optional) | `return total` |
#
# ── Two different steps: DEFINE and CALL ──
# | Step | Like in the chai stall | What happens |
# |------|------------------------|--------------|
# | Define (`def ...`) | Writing the recipe on a card | Nothing runs yet. Python just remembers the recipe |
# | Call (`name(...)`) | Ordering "one cutting chai" | The steps run now |
#
# ── What happens when you call a function ──
#   Your code                          The function
#   ---------                          ------------
#   result = add_numbers(5, 3)  --->   a = 5, b = 3        (arguments go in)
#                                      answer = a + b
#   result is now 8             <---   return answer       (the value comes back)
#   (your code carries on)
#
# ── Three small rules ──
# 1. Define before you call. Python reads from top to bottom.
# 2. Always use parentheses to call: `say_hello()`, not `say_hello`.
# 3. Give functions verb names that say the job: `calculate_total`, `show_menu`, `is_valid_amount`.


# ══════════════════════════════════════════════════════════════
# PART 3: Simple examples
# ══════════════════════════════════════════════════════════════
#
# ── Example 1: A function with no inputs ──
# Defining prints nothing. Only the calls make it run.

def say_hello():
    print("Namaste from PaisaTracker!")

print("Before calling")
say_hello()
say_hello()
print("After calling")
# Output:
#   Before calling
#   Namaste from PaisaTracker!
#   Namaste from PaisaTracker!
#   After calling


# Try it: call `say_hello()` three more times. Then remove the parentheses from one call (`say_hello`) and see that nothing prints.


# ── Example 2: A function with one input (a parameter) ──

def greet(name):
    print(f"Hello, {name}!")

greet("Priya")
greet("Arjun")
# Output:
#   Hello, Priya!
#   Hello, Arjun!


# `name` is the parameter (the empty box in the recipe). `"Priya"` is the argument (the real value we put in the box). One function, many different results.


# ── Example 3: A function that gives something back (`return`) ──

def add_numbers(a, b):
    answer = a + b
    return answer

result = add_numbers(5, 3)
print(result)
print(add_numbers(10, 20) + 1)
# Output:
#   8
#   31


# Follow the call `add_numbers(5, 3)`:
#
# | Step | What happens |
# |------|--------------|
# | 1 | Python sees the call and jumps into the function |
# | 2 | `a` becomes 5 and `b` becomes 3 |
# | 3 | `answer = 5 + 3` makes 8 |
# | 4 | `return answer` sends 8 back to where the call was |
# | 5 | `result = 8` |


# ── Example 4: A function called in a loop ──

def square(number):
    return number * number

for n in range(1, 5):
    print(n, "squared is", square(n))
# Output:
#   1 squared is 1
#   2 squared is 4
#   3 squared is 9
#   4 squared is 16


# ── Your first exercises ──


# ── Your turn 1: Greet the user ──
#
# Write a function `greet_user(name)` that prints `Namaste, ` followed by the name and `!`.
# Call it for "Arjun" and then for "Riya".
#
# Expected output
# Namaste, Arjun!
# Namaste, Riya!

# YOUR CODE HERE


# Show solution (try first!)
#
# def greet_user(name):
#     print(f"Namaste, {name}!")
#
# greet_user("Arjun")
# greet_user("Riya")
#


# ── Your turn 2: Rectangle area ──
#
# Write a function `rectangle_area(length, width)` that RETURNS the area.
# Print the area of a 5 by 3 and a 10 by 4 rectangle.
#
# Expected output
# 15
# 40

# YOUR CODE HERE


# Show solution (try first!)
#
# def rectangle_area(length, width):
#     return length * width
#
# print(rectangle_area(5, 3))
# print(rectangle_area(10, 4))
#


# ══════════════════════════════════════════════════════════════
# PART 4: One concept at a time
# ══════════════════════════════════════════════════════════════
#
# 1. A function with no parameters
# 2. Parameters and arguments (order matters)
# 3. `return` vs `print`
# 4. `return` ends the function (early return and `None`)
# 5. Default parameter values
# 6. Keyword arguments
# 7. Returning more than one value
# 8. Functions that call other functions
# 9. Local scope: the private room
# 10. Global variables and constants
# 11. Lists and dicts can be changed by a function
# 12. Docstrings and good function design
# 13. Testing a function


# ══════════════════════════════════════════════════════════════
# ── Concept 1: A function with no parameters ──
# Idea: a function does not need inputs. It is useful for a job you repeat the same way every time, like printing a line between sections.

def print_line():
    print("-" * 30)

print("PAISATRACKER REPORT")
print_line()
print("chai - ₹20")
print_line()
# Output:
#   PAISATRACKER REPORT
#   ------------------------------
#   chai - ₹20
#   ------------------------------


# What to notice: we wrote `print("-" * 30)` once and used it twice. Change the 30 in the function and every line changes.


# ══════════════════════════════════════════════════════════════
# ── Concept 2: Parameters and arguments ──
# Idea:
# - A parameter is the placeholder name in the `def` line (`name`, `amount`).
# - An argument is the real value you give in the call (`"chai"`, `20`).
# - Arguments go in by position: the first argument goes to the first parameter, and so on.

def show_expense(name, amount):
    print(f"{name} costs ₹{amount}")

show_expense("chai", 20)
show_expense("movie", 450)
show_expense(450, "movie")      # wrong order! Python does not notice
# Output:
#   chai costs ₹20
#   movie costs ₹450
#   450 costs ₹movie


# What to notice: the last call gave silly output but no error. The order of arguments matters.


# ── Your turn 2: Chai bill ──
#
# Write `show_bill(cups, price)` that prints the bill like `3 cups x ₹20 = ₹60`.
# Call it with (3, 20) and then (5, 15).
#
# Expected output
# 3 cups x ₹20 = ₹60
# 5 cups x ₹15 = ₹75

# YOUR CODE HERE


# Show solution (try first!)
#
# def show_bill(cups, price):
#     print(f"{cups} cups x ₹{price} = ₹{cups * price}")
#
# show_bill(3, 20)
# show_bill(5, 15)
#


# ══════════════════════════════════════════════════════════════
# ── Concept 3: `return` vs `print` ──
# Idea: this confuses every beginner.
# - `print` only shows something on the screen. The value is lost.
# - `return` hands the value back so you can store it or use it in more maths.

def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)       # shows 5, but x gets nothing useful
y = add_return(2, 3)      # shows nothing, but y gets 5
print("x is", x)
print("y is", y)
print("y doubled:", y * 2)
# print(x * 2)            # would crash: None cannot be multiplied
# Output:
#   5
#   x is None
#   y is 5
#   y doubled: 10


# What to notice: the function with only `print` gave back `None` (Python's word for "nothing"). If you want to use the answer later, `return` it.


# ── Your turn 3: Price with GST ──
#
# Write `add_gst(amount)` that RETURNS the amount plus 18% GST.
# Print `add_gst(100)` and `add_gst(250)`.
#
# Expected output
# 118.0
# 295.0

# YOUR CODE HERE


# Show solution (try first!)
#
# def add_gst(amount):
#     return amount + amount * 18 / 100
#
# print(add_gst(100))
# print(add_gst(250))
#


# ══════════════════════════════════════════════════════════════
# ── Concept 4: `return` ends the function ──
# Idea: the moment Python reaches `return`, the function stops and sends the value back. Lines after it never run. This lets us handle special cases first (an early return).

def biggest(amounts):
    if len(amounts) == 0:
        return None            # nothing to look at: leave immediately
    largest = amounts[0]
    for amount in amounts:
        if amount > largest:
            largest = amount
    return largest

print(biggest([120, 45, 300]))
print(biggest([]))
# Output:
#   300
#   None


# What to notice: an empty list is handled safely instead of crashing on `amounts[0]`. A function with no `return` also gives back `None`.


# ══════════════════════════════════════════════════════════════
# ── Concept 5: Default parameter values ──
# Idea: give a parameter a default with `=`. If the caller does not provide it, the default is used. Parameters with defaults must come after the ones without.

def add_gst(amount, rate=18):
    return amount + amount * rate / 100

print(add_gst(250))          # uses the default rate 18
print(add_gst(250, 5))       # overrides it with 5
# Output:
#   295.0
#   262.5


# ── Your turn 5: A default category ──
#
# Write `make_expense(name, amount, category="misc")` that RETURNS a dict with the three keys.
# Print `make_expense("chai", 20)` and `make_expense("metro", 30, "travel")`.
#
# Expected output
# {'name': 'chai', 'amount': 20, 'category': 'misc'}
# {'name': 'metro', 'amount': 30, 'category': 'travel'}

# YOUR CODE HERE


# Show solution (try first!)
#
# def make_expense(name, amount, category="misc"):
#     return {"name": name, "amount": amount, "category": category}
#
# print(make_expense("chai", 20))
# print(make_expense("metro", 30, "travel"))
#


# ══════════════════════════════════════════════════════════════
# ── Concept 6: Keyword arguments ──
# Idea: in the call, you can write the parameter name (`amount=85`). Then the order no longer matters, and the call reads like a sentence.

def make_expense(name, amount, category="misc"):
    return {"name": name, "amount": amount, "category": category}

print(make_expense(amount=85, name="auto-rickshaw", category="travel"))
print(make_expense("chai", 20, category="food"))
# Output:
#   {'name': 'auto-rickshaw', 'amount': 85, 'category': 'travel'}
#   {'name': 'chai', 'amount': 20, 'category': 'food'}


# What to notice: mixing is fine. Put the normal (positional) arguments first, and keyword arguments after.


# ══════════════════════════════════════════════════════════════
# ── Concept 7: Returning more than one value ──
# Idea: `return a, b` sends back two values at once (Python packs them in a tuple, Day 4). The caller can unpack them into two variables.

def min_and_max(amounts):
    smallest = amounts[0]
    largest = amounts[0]
    for amount in amounts:
        if amount < smallest:
            smallest = amount
        if amount > largest:
            largest = amount
    return smallest, largest

low, high = min_and_max([120, 45, 300, 80])
print(f"Smallest ₹{low}, largest ₹{high}")
print(min_and_max([120, 45, 300, 80]))        # the raw result is a tuple
# Output:
#   Smallest ₹45, largest ₹300
#   (45, 300)


# ── Your turn 7: Total and count ──
#
# Write `total_and_count(amounts)` that returns BOTH the total and how many amounts there are.
# Print: `Total ₹795 from 5 expenses`.
#
# Expected output
# Total ₹795 from 5 expenses

amounts = [120, 45, 300, 80, 250]

# YOUR CODE HERE


# Show solution (try first!)
#
# def total_and_count(amounts):
#     total = 0
#     count = 0
#     for amount in amounts:
#         total += amount
#         count += 1
#     return total, count
#
# total, count = total_and_count(amounts)
# print(f"Total ₹{total} from {count} expenses")
#


# ══════════════════════════════════════════════════════════════
# ── Concept 8: Functions that call other functions ──
# Idea: small functions are building blocks. A bigger function can call smaller ones. Each function has one job.

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def average_expense(expenses):
    if len(expenses) == 0:
        return 0
    return round(calculate_total(expenses) / len(expenses), 2)     # uses calculate_total

def print_summary(expenses):
    print("Count  :", len(expenses))
    print("Total  :", calculate_total(expenses))
    print("Average:", average_expense(expenses))

my_expenses = [{"amount": 120}, {"amount": 45}, {"amount": 300}]
print_summary(my_expenses)
# Output:
#   Count  : 3
#   Total  : 465
#   Average: 155.0


# ── Your turn 8: Over budget? ──
#
# Write `is_over_budget(expenses, budget)` that RETURNS True when the total is above the budget. Use the given `calculate_total`.
# Print the result for budgets 500 and 1000.
#
# Expected output
# True
# False

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

expenses = [{"amount": 120}, {"amount": 45}, {"amount": 300}, {"amount": 80}, {"amount": 250}]

# YOUR CODE HERE


# Show solution (try first!)
#
# def is_over_budget(expenses, budget):
#     return calculate_total(expenses) > budget
#
# print(is_over_budget(expenses, 500))
# print(is_over_budget(expenses, 1000))
#


# ══════════════════════════════════════════════════════════════
# ── Concept 9: Local scope (the private room) ──
# Idea: scope means where a variable can be seen. A variable created inside a function is local: it lives in the function's private room and disappears when the function ends. Nobody outside can see it.

def make_message(name):
    message = f"Welcome, {name}!"     # message is LOCAL to this function
    return message

print(make_message("Priya"))
# print(message)    # <- NameError: 'message' only existed inside the function
# Output:
#   Welcome, Priya!


# What to notice: to get something out of the private room, return it. That is why `return` exists.


# ══════════════════════════════════════════════════════════════
# ── Concept 10: Global variables and constants ──
# Idea: a variable created outside every function is global.
# - A function can read a global variable. This is fine for constants (values that never change, written in CAPITALS), like `LIMIT = 500`.
# - If a function assigns to a name, Python makes a new local variable, even if a global has the same name.

LIMIT = 500                           # a global constant

def is_above_limit(amount):
    return amount > LIMIT             # reading a global: fine

print(is_above_limit(640), is_above_limit(20))
# Output:
#   True False

counter = 0

def try_to_change():
    counter = 99                      # creates a NEW local variable!
    print("inside :", counter)

try_to_change()
print("outside:", counter)            # the global is untouched
# Output:
#   inside : 99
#   outside: 0


# There is a `global` keyword that lets a function change a global variable:

def really_change():
    global counter
    counter = 99

really_change()
print("after global:", counter)
# Output:
#   after global: 99


# Advice: avoid `global` for changing values. It makes code hard to follow and hard to test. Prefer parameters in, `return` out.


# Check your understanding: A function says `total = 0` and then adds to it. Is the `total` outside the function changed?
#
# No. Assigning inside a function creates a local `total`. The outside `total` is a different variable. To get the answer out, `return` it.
#


# ══════════════════════════════════════════════════════════════
# ── Concept 11: Lists and dicts can be changed by a function ──
# Idea: when you pass a list or dict, the function works on the original, not a copy. So `append` inside a function changes the list outside too. Numbers and text behave differently: reassigning them inside only changes the local copy.

def add_item(items, item):
    items.append(item)                # changes the ORIGINAL list

def reset_number(number):
    number = 0                        # only changes the local copy

shopping = ["atta", "dal"]
add_item(shopping, "rice")
print(shopping)

amount = 50
reset_number(amount)
print(amount)
# Output:
#   ['atta', 'dal', 'rice']
#   50


# ── Your turn 11: Add an expense ──
#
# Write `add_expense(expenses, name, amount)` that appends a dict with `name` and `amount` to the list. It needs no `return`.
# Call it twice, then print how many expenses there are and the last one.
#
# Expected output
# 2
# {'name': 'metro', 'amount': 30}

expenses = []

# YOUR CODE HERE


# Show solution (try first!)
#
# def add_expense(expenses, name, amount):
#     expenses.append({"name": name, "amount": amount})
#
# add_expense(expenses, "chai", 20)
# add_expense(expenses, "metro", 30)
# print(len(expenses))
# print(expenses[-1])
#


# ══════════════════════════════════════════════════════════════
# ── Concept 12: Docstrings and good function design ──
# Idea: a docstring is a short description in triple quotes as the first line inside the function. It explains what the function does.
#
# A good function:
# - has one job
# - has a verb name that says the job (`calculate_total`, `show_menu`, `is_valid_amount`)
# - is short (a screen or less)
# - uses parameters and return instead of globals
# - returns answers instead of printing them, when someone may need the answer later

def calculate_total(expenses):
    """Return the sum of the amount of every expense."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

print(calculate_total.__doc__)
# Output:
#   Return the sum of the amount of every expense.


# ══════════════════════════════════════════════════════════════
# ── Concept 13: Testing a function ──
# Idea: before trusting a function, call it with inputs where you already know the answer.

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

if calculate_total([{"amount": 10}, {"amount": 20}]) == 30:
    print("Test 1 passed")
else:
    print("Test 1 FAILED")

if calculate_total([]) == 0:
    print("Test 2 passed (empty list)")
else:
    print("Test 2 FAILED")
# Output:
#   Test 1 passed
#   Test 2 passed (empty list)


# What to notice: always test the edge case (an empty list). Real bugs love edge cases. On Day 20 we meet `pytest`, which does this automatically.


# ── Recap of Part 4 ──
# | Concept | Remember |
# |---------|----------|
# | No parameters | `def name():`, good for repeated jobs |
# | Parameters / arguments | placeholder in `def`, real value in the call; order matters |
# | `return` vs `print` | `return` gives the value back; `print` only shows it |
# | Early return / `None` | `return` stops the function; no return gives `None` |
# | Defaults | `rate=18`, defaults come last |
# | Keyword arguments | `amount=85`, order no longer matters |
# | Multiple returns | `return a, b` then `x, y = function()` |
# | Functions calling functions | small building blocks, one job each |
# | Local scope | variables inside a function stay inside |
# | Global | read freely; avoid changing with `global` |
# | Lists / dicts | the function changes the original |
# | Docstring | first line inside the function |
# | Testing | call with known answers, include edge cases |


# ══════════════════════════════════════════════════════════════
# PART 5: The PaisaTracker codebase
# ══════════════════════════════════════════════════════════════
#
# On Day 5 we built a menu that works, but it is one long block of code. Today we give every job a name. We build the functions in three stages:
#
# | Stage | What it adds |
# |-------|--------------|
# | 1 | Calculation functions: total, category totals, biggest expense |
# | 2 | Action functions: validate an amount, add an expense, show expenses |
# | 3 | Menu functions: show the menu and run it. v0 is complete! |
#
# Every function follows the good-design rules: one job, a verb name, parameters in, return out.


# ── Stage 1: Calculation functions ──
# These functions only work with data and return an answer. They never print and never ask anything. That makes them easy to test and reuse.

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def category_totals(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]
    return totals

def biggest_expense(expenses):
    if len(expenses) == 0:
        return None
    biggest = expenses[0]
    for expense in expenses:
        if expense["amount"] > biggest["amount"]:
            biggest = expense
    return biggest


# Test each one with data where we know the answer:

sample = [
    {"name": "chai", "amount": 20, "category": "food"},
    {"name": "auto-rickshaw", "amount": 85, "category": "travel"},
    {"name": "groceries", "amount": 640, "category": "food"},
]

print("Total       :", calculate_total(sample))
print("By category :", category_totals(sample))
print("Biggest     :", biggest_expense(sample))
print("Empty total :", calculate_total([]))
print("Empty biggest:", biggest_expense([]))
# Output:
#   Total       : 745
#   By category : {'food': 660, 'travel': 85}
#   Biggest     : {'name': 'groceries', 'amount': 640, 'category': 'food'}
#   Empty total : 0
#   Empty biggest: None


# ── Stage 2: Action functions ──
# These do the visible work: check the input, add to the list, and show the list. We also bring back the limit warning from Day 3. `LIMIT` is a global constant that functions only read.

LIMIT = 500

def is_valid_amount(text):
    return text.isdigit() and int(text) > 0

def add_expense(expenses, name, amount, category):
    expenses.append({"name": name, "amount": amount, "category": category})
    print(f"Added: {name} - ₹{amount} ({category})")
    if amount > LIMIT:
        print(f"  Warning: ₹{amount} is above your limit of ₹{LIMIT}")

def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    number = 1
    for expense in expenses:
        print(f"{number}. {expense['name']} - ₹{expense['amount']} ({expense['category']})")
        number += 1

test_list = []
print(is_valid_amount("250"), is_valid_amount("abc"), is_valid_amount("0"))
add_expense(test_list, "chai", 20, "food")
add_expense(test_list, "groceries", 640, "food")
show_expenses(test_list)
show_expenses([])
# Output:
#   True False False
#   Added: chai - ₹20 (food)
#   Added: groceries - ₹640 (food)
#     Warning: ₹640 is above your limit of ₹500
#   1. chai - ₹20 (food)
#   2. groceries - ₹640 (food)
#   No expenses yet.


# What to notice: `add_expense` changes the list that we passed in (Concept 11), so it does not need a `return`. `show_expenses` uses an early return for an empty list (Concept 4).
#
# ── Stage 3: Menu functions (v0 complete) ──
# `ask()` is a small helper. With `USE_REAL_INPUT = False` it plays back the answers in `simulated_replies`, like the `typed` list on Day 5. Set it to `True` to type your own answers.

USE_REAL_INPUT = False
simulated_replies = [
    "1", "chai", "20", "food",
    "1", "auto-rickshaw", "85", "travel",
    "1", "groceries", "abc", "640", "food",     # 'abc' is rejected, then 640 is accepted
    "2", "3", "4", "9", "5",
]

def ask(prompt):
    if USE_REAL_INPUT:
        return input(prompt)
    reply = simulated_replies.pop(0)
    print(f"{prompt}{reply}")
    return reply

def show_menu():
    print()
    print("1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit")

def read_amount():
    amount_text = ask("Amount: ")
    while not is_valid_amount(amount_text):
        print("  Invalid amount. Please type a positive whole number.")
        amount_text = ask("Amount: ")
    return int(amount_text)

def run_menu(expenses):
    running = True
    while running:
        show_menu()
        choice = ask("Choose: ")
        if choice == "1":
            name = ask("Expense name: ")
            amount = read_amount()
            category = ask("Category: ")
            add_expense(expenses, name, amount, category)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print(f"Total spent: ₹{calculate_total(expenses)}")
        elif choice == "4":
            for category, amount in category_totals(expenses).items():
                print(f"  {category}: ₹{amount}")
        elif choice == "5":
            running = False
            print("Goodbye! (Your data is lost for now. On Day 8 we save it to a file.)")
        else:
            print("Invalid choice. Please type 1 to 5.")


# Now the whole program is just three lines. Run it:

print("Welcome to PaisaTracker v0")
my_expenses = []
run_menu(my_expenses)
# Output:
#   Welcome to PaisaTracker v0
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 1
#   Expense name: chai
#   Amount: 20
#   Category: food
#   Added: chai - ₹20 (food)
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 1
#   Expense name: auto-rickshaw
#   Amount: 85
#   Category: travel
#   Added: auto-rickshaw - ₹85 (travel)
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 1
#   Expense name: groceries
#   Amount: abc
#     Invalid amount. Please type a positive whole number.
#   Amount: 640
#   Category: food
#   Added: groceries - ₹640 (food)
#     Warning: ₹640 is above your limit of ₹500
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 2
#   1. chai - ₹20 (food)
#   2. auto-rickshaw - ₹85 (travel)
#   3. groceries - ₹640 (food)
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 3
#   Total spent: ₹745
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 4
#     food: ₹660
#     travel: ₹85
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 9
#   Invalid choice. Please type 1 to 5.
#
#   1) Add expense   2) View expenses   3) Show total   4) Category totals   5) Exit
#   Choose: 5
#   Goodbye! (Your data is lost for now. On Day 8 we save it to a file.)


# ── Before and after ──
# | | Day 5 (one long block) | Day 6 (functions) |
# |---|------------------------|-------------------|
# | Total calculation | copied in several places | `calculate_total()` once |
# | Amount validation | a `while` loop inside the menu | `read_amount()` |
# | The menu | one very long `while` block | `show_menu()` and `run_menu()` |
# | Fixing a bug | change many places | change one function |
# | Testing | only by running everything | test each function alone |
#
# ── Read it line by line ──
# | Part of the code | Concept used |
# |------------------|--------------|
# | `def calculate_total(expenses):` ... `return total` | parameters and `return` (Concepts 2, 3) |
# | `biggest_expense([])` gives `None` | early return (Concept 4) |
# | `LIMIT = 500` used inside `add_expense` | global constant (Concept 10) |
# | `add_expense(expenses, ...)` changes the list | lists are changed in place (Concept 11) |
# | `read_amount()` calls `ask()` and `is_valid_amount()` | functions calling functions (Concept 8) |
# | `return int(amount_text)` | gets the value out of the private room (Concept 9) |
# | `run_menu(my_expenses)` | the menu loop from Day 5, now in a function |
#
# ── Use it for real ──
# Set `USE_REAL_INPUT = True` in the cell above and run the three-line cell again. In Jupyter a text box appears for each question. In a terminal, save the code as `paisatracker.py` and run it:
#
# | OS | Command |
# |----|---------|
# | Windows | `python paisatracker.py` |
# | macOS / Linux | `python3 paisatracker.py` |
# | uv | `uv run paisatracker.py` |
#
# ── Make it yours: two challenges ──


# ── Your turn P1: Expenses in one category ──
#
# Write `expenses_in_category(expenses, category)` that RETURNS a list with only the expenses of that category.
# Print how many food expenses there are and their names.
#
# Expected output
# 2 food expenses
# chai
# groceries

expenses = [
    {"name": "chai", "amount": 20, "category": "food"},
    {"name": "auto-rickshaw", "amount": 85, "category": "travel"},
    {"name": "groceries", "amount": 640, "category": "food"},
    {"name": "metro", "amount": 30, "category": "travel"},
]

# YOUR CODE HERE


# Show solution (try first!)
#
# def expenses_in_category(expenses, category):
#     matches = []
#     for expense in expenses:
#         if expense["category"] == category:
#             matches.append(expense)
#     return matches
#
# food = expenses_in_category(expenses, "food")
# print(len(food), "food expenses")
# for expense in food:
#     print(expense["name"])
#


# ── Your turn P2: Category report ──
#
# Write `show_category_report(expenses)` that PRINTS each category and its total, one per line, like `food: ₹660`. Use the given `category_totals`.
#
# Expected output
# food: ₹660
# travel: ₹85

def category_totals(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]
    return totals

expenses = [
    {"name": "chai", "amount": 20, "category": "food"},
    {"name": "auto-rickshaw", "amount": 85, "category": "travel"},
    {"name": "groceries", "amount": 640, "category": "food"},
]

# YOUR CODE HERE


# Show solution (try first!)
#
# def show_category_report(expenses):
#     for category, amount in category_totals(expenses).items():
#         print(f"{category}: ₹{amount}")
#
# show_category_report(expenses)
#


# ══════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════
#
# ── You learned ──
# - [ ] A function is a recipe with a name: write once, use many times
# - [ ] `def name(parameters):` defines, `name(arguments)` calls
# - [ ] `return` hands a value back; `print` only shows it; no `return` gives `None`
# - [ ] Defaults (`rate=18`) and keyword arguments (`amount=85`)
# - [ ] `return a, b` sends back two values
# - [ ] Scope: variables inside a function are local; read global constants, avoid changing globals
# - [ ] Lists and dicts passed to a function are changed in place
# - [ ] Good functions have one job and a verb name
#
# ── PaisaTracker v0 is COMPLETE ──
# Your tracker now has: expenses as a list of dicts, a for-loop report, a menu loop, and clean functions for totals, validation, adding, showing and running the menu. The data lives in memory only.
#
# ── Coming next: Day 7, Strings and string methods (Part 1 of 2) ──
# Our output is plain. Tomorrow we make it look professional with neat table formatting and f-string tricks. This starts v1 "Saves data", which also learns to save and load expenses on Day 8.
