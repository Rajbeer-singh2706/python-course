"""
Day 14 — Decorators & Closures — Practice Problem Set (File 1 of 2)

Cumulative scope: Days 1-14 (all prior concepts may appear in Section A)

Difficulty legend:
    🟢 Warm-up   — direct application of a single concept
    🟡 Core      — combines 2+ ideas, requires a bit more thought
    🔴 Challenge — multi-step, closer to a real mini-project

Section index (this file):
    Section A — Prior Days Review               (3 problems)
    Section B — First-Class Functions            (4 problems)
    Section C — Closures & Free Variables         (4 problems)

(Section D, E, and Mixed Challenges continue in
 day14_practise_problems_02_decorators_builtin.py)

How to run:
    python day14_practise_problems_01_first_class_closures.py
"""


# ════════════════════════════════════════════════════════════════
# SECTION A — Prior Days Review
# ════════════════════════════════════════════════════════════════

# ── Problem A1 🟢 Warm-up ──
# Given a list of iterator-produced squares (Day 13), use a generator
# expression to build a list of only the EVEN squares from 1 to 10.
#
# Expected output: [4, 16, 36, 64, 100]

# YOUR CODE HERE
even_squares = None

print("Problem A1:")
# SOLUTION:
even_squares = [n * n for n in range(1, 11) if (n * n) % 2 == 0]
print(even_squares)
print("-" * 50)


# ── Problem A2 🟢 Warm-up ──
# Using a custom exception (Day 9), write a function `check_age(age)`
# that raises a ValueError with message "Age cannot be negative" if
# age < 0, otherwise returns f"Age {age} is valid".
#
# Expected output:
#   Age 25 is valid
#   Caught: Age cannot be negative

# YOUR CODE HERE
def check_age(age):
    pass


print("Problem A2:")
# SOLUTION:
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age {age} is valid"


print(check_age(25))
try:
    check_age(-5)
except ValueError as error:
    print(f"Caught: {error}")
print("-" * 50)


# ── Problem A3 🟡 Core ──
# Using OOP (Day 10/11), define a class `Vehicle` with __init__(self, brand)
# and a __str__ method returning f"Vehicle: {brand}". Create an instance
# for brand "Tata" and print it directly (print(obj) should use __str__).
#
# Expected output: Vehicle: Tata

# YOUR CODE HERE
class Vehicle:
    pass


print("Problem A3:")
# SOLUTION:
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Vehicle: {self.brand}"


print(Vehicle("Tata"))
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION B — First-Class Functions
# ════════════════════════════════════════════════════════════════

# ── Problem B1 🟢 Warm-up ──
# Assign the built-in function `len` to a variable called `measure`.
# Use it to print the length of the string "Bengaluru".
#
# Expected output: 9

# YOUR CODE HERE
measure = None

print("Problem B1:")
# SOLUTION:
measure = len
print(measure("Bengaluru"))
print("-" * 50)


# ── Problem B2 🟢 Warm-up ──
# Create a list called `math_ops` containing the built-in functions
# `abs`, `round`, and a lambda-free custom function `square(x)` that
# returns x * x. Call each on the value -4 and print the results in a
# list (use a list comprehension).
#
# Expected output: [4, -4, 16]
# (Note: round(-4) == -4, that's expected here)

# YOUR CODE HERE
def square(x):
    return x * x


print("Problem B2:")
# SOLUTION:
math_ops = [abs, round, square]
print([op(-4) for op in math_ops])
print("-" * 50)


# ── Problem B3 🟡 Core ──
# Write a higher-order function `apply_twice(func, value)` that calls
# `func` on `value` twice in a row (i.e. func(func(value))) and returns
# the result. Test it with a function that adds 100kg-worth-of-rupees
# style tax: `add_gst(price) -> price * 1.05`.
#
# Expected output: 1102.5

# YOUR CODE HERE
def apply_twice(func, value):
    pass


def add_gst(price):
    return price * 1.05


print("Problem B3:")
# SOLUTION:
def apply_twice(func, value):
    return func(func(value))


print(apply_twice(add_gst, 1000))
print("-" * 50)


# ── Problem B4 🟡 Core ──
# Write a function `build_pricing_menu()` that returns a dictionary
# mapping city names ("Mumbai", "Delhi", "Bengaluru") to functions that
# each return that city's delivery fee (Mumbai: 30, Delhi: 25,
# Bengaluru: 35). Use the dictionary to print Bengaluru's fee.
#
# Expected output: 35

# YOUR CODE HERE
def build_pricing_menu():
    pass


print("Problem B4:")
# SOLUTION:
def build_pricing_menu():
    def mumbai_fee():
        return 30

    def delhi_fee():
        return 25

    def bengaluru_fee():
        return 35

    return {"Mumbai": mumbai_fee, "Delhi": delhi_fee, "Bengaluru": bengaluru_fee}


menu = build_pricing_menu()
print(menu["Bengaluru"]())
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION C — Closures & Free Variables
# ════════════════════════════════════════════════════════════════

# ── Problem C1 🟢 Warm-up ──
# Write a closure factory `make_power_function(exponent)` that returns
# a function `power(base)` computing base ** exponent. Create a
# `square_fn` (exponent=2) and print square_fn(9).
#
# Expected output: 81

# YOUR CODE HERE
def make_power_function(exponent):
    pass


print("Problem C1:")
# SOLUTION:
def make_power_function(exponent):
    def power(base):
        return base ** exponent

    return power


square_fn = make_power_function(2)
print(square_fn(9))
print("-" * 50)


# ── Problem C2 🟢 Warm-up ──
# Write a closure factory `make_greeting(language)` returning a function
# that greets a name in the given language ("hindi" -> "Namaste, {name}!",
# any other value -> "Hello, {name}!"). Test with language="hindi",
# name="Arjun".
#
# Expected output: Namaste, Arjun!

# YOUR CODE HERE
def make_greeting(language):
    pass


print("Problem C2:")
# SOLUTION:
def make_greeting(language):
    def greeting(name):
        if language == "hindi":
            return f"Namaste, {name}!"
        return f"Hello, {name}!"

    return greeting


hindi_greeting = make_greeting("hindi")
print(hindi_greeting("Arjun"))
print("-" * 50)


# ── Problem C3 🟡 Core ──
# Write a closure-based counter `make_countdown(start)` that returns a
# function `tick()`. Each call to tick() should return the next number
# counting DOWN from `start`, using `nonlocal`. Call tick() three times
# on a countdown starting at 5.
#
# Expected output:
#   5
#   4
#   3

# YOUR CODE HERE
def make_countdown(start):
    pass


print("Problem C3:")
# SOLUTION:
def make_countdown(start):
    current = start

    def tick():
        nonlocal current
        value = current
        current -= 1
        return value

    return tick


countdown = make_countdown(5)
print(countdown())
print(countdown())
print(countdown())
print("-" * 50)


# ── Problem C4 🟡 Core ──
# Write `make_cart_total()` returning a closure `add_item(price)` that
# accumulates a running total (starting at 0) using `nonlocal`, and
# returns the new running total each time it's called. Add items priced
# 199, 349, and 120 (Flipkart-style cart) and print the total after
# each addition.
#
# Expected output:
#   199
#   548
#   668

# YOUR CODE HERE
def make_cart_total():
    pass


print("Problem C4:")
# SOLUTION:
def make_cart_total():
    total = 0

    def add_item(price):
        nonlocal total
        total += price
        return total

    return add_item


add_item = make_cart_total()
print(add_item(199))
print(add_item(349))
print(add_item(120))
print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# Sections completed in this file:
#   A — Prior Days Review           (3 problems)
#   B — First-Class Functions       (4 problems)
#   C — Closures & Free Variables   (4 problems)
#
# Difficulty breakdown: 6x 🟢 Warm-up, 5x 🟡 Core, 0x 🔴 Challenge
#
# Continue with:
#   day14_practise_problems_02_decorators_builtin.py
#   (Section D — Decorators From Scratch, Section E — Built-in
#   Decorators, Section F — Mixed Challenges)

if __name__ == "__main__":
    print("\nPractice file 1 of 2 complete.")
