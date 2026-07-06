"""
Day 14 — Decorators & Closures
File 1 of 3: First-Class Functions & Closures

What this file covers:
    - Functions as first-class objects (assign, store, pass, return)
    - Higher-order functions (functions that take/return other functions)
    - Closures — inner functions that remember free variables
    - The `nonlocal` keyword for mutating captured variables

Prerequisites:
    - Day 5 (Functions & Scope), Day 6 (Data Structures), Day 13 (Iterators & Generators)

How to run:
    python day14_01_first_class_and_closures.py
"""


# ════════════════════════════════════════════════════════════════
# SECTION 1 — Functions Are First-Class Objects
# ════════════════════════════════════════════════════════════════
#
# In Python, a function is just another object — the same way an int,
# a string, or a list is an object. That means we can:
#   1. Assign a function to a variable
#   2. Store functions inside a list or dictionary
#   3. Pass a function as an argument to another function
#   4. Return a function from another function
#
# This single idea is the foundation for decorators later in this file.

# ── Assigning a function to a variable ──

def greet_customer(name):
    """Return a friendly Swiggy order-confirmation greeting."""
    return f"Namaste, {name}! Your Swiggy order is confirmed."


# Notice: no parentheses here. We are referencing the function object
# itself, not calling it.
send_greeting = greet_customer

print(send_greeting("Priya"))
# Output: Namaste, Priya! Your Swiggy order is confirmed.

print(send_greeting is greet_customer)
# Output: True  (same function object, just two names for it)

print("-" * 50)

# ── Storing functions in a list ──

def to_upper(text):
    return text.upper()


def to_title(text):
    return text.title()


text_transformers = [to_upper, to_title, str.lower]

sample = "arjun mehta"
for transformer in text_transformers:
    print(transformer(sample))
# Output: ARJUN MEHTA
# Output: Arjun Mehta
# Output: arjun mehta

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 2 — Higher-Order Functions
# ════════════════════════════════════════════════════════════════
#
# A higher-order function either:
#   (a) accepts another function as an argument, or
#   (b) returns a function as its result (or both).
#
# This lets us plug in different behaviour without rewriting the
# surrounding logic — very useful for pricing rules, sorting keys,
# and (later today) decorators.

# ── Example: passing a function as an argument ──

def apply_discount(price, strategy):
    """strategy is a function that decides how much discount to apply."""
    return strategy(price)


def festival_discount(price):
    return price * 0.80  # 20% off for festival sale


def loyalty_discount(price):
    return price * 0.90  # 10% off for loyal customers


def no_discount(price):
    return price


order_total = 1000
print(f"Festival price: Rs.{apply_discount(order_total, festival_discount)}")
print(f"Loyalty price: Rs.{apply_discount(order_total, loyalty_discount)}")
print(f"Regular price: Rs.{apply_discount(order_total, no_discount)}")
# Output: Festival price: Rs.800.0
# Output: Loyalty price: Rs.900.0
# Output: Regular price: Rs.1000

print("-" * 50)

# ── Example: returning a function from a function ──

def make_multiplier(factor):
    """Returns a NEW function that multiplies its input by `factor`."""

    def multiplier(number):
        return number * factor

    return multiplier  # returning the function object itself, not calling it


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(50))   # Output: 100
print(triple(50))   # Output: 150

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# SECTION 3 — Closures & Free Variables
# ════════════════════════════════════════════════════════════════
#
# A closure happens when an inner function "remembers" a variable
# from its enclosing (outer) function's scope, even after the outer
# function has already finished running. That remembered variable is
# called a FREE VARIABLE.
#
# Think of it as the inner function carrying a small backpack of
# values from "home" (the outer function) wherever it goes.

# ── A basic closure ──

def make_greeting_closure(city):
    """`city` becomes a free variable captured by `greeting`."""

    def greeting(name):
        return f"Hello {name}, welcome to our {city} store!"

    return greeting


mumbai_greeting = make_greeting_closure("Mumbai")
pune_greeting = make_greeting_closure("Pune")

print(mumbai_greeting("Riya"))
print(pune_greeting("Sanjay"))
# Output: Hello Riya, welcome to our Mumbai store!
# Output: Hello Sanjay, welcome to our Pune store!

print("-" * 50)

# ── Closures with mutable state: nonlocal ──
#
# If the inner function only READS the outer variable, no special
# keyword is needed. But if it needs to MODIFY (rebind) that variable,
# Python requires the `nonlocal` keyword — otherwise Python assumes
# you are creating a brand-new local variable inside the inner function.

def make_delivery_tracker(city):
    """Each call creates an independent closure with its own counter."""
    orders_delivered = 0

    def track(order_id):
        nonlocal orders_delivered       # without this: UnboundLocalError
        orders_delivered += 1
        return f"{city}: order {order_id} delivered (#{orders_delivered} today)"

    return track


mumbai_tracker = make_delivery_tracker("Mumbai")
delhi_tracker = make_delivery_tracker("Delhi")

print(mumbai_tracker("SW1001"))
print(mumbai_tracker("SW1002"))
print(delhi_tracker("SW2001"))
print(mumbai_tracker("SW1003"))
# Output: Mumbai: order SW1001 delivered (#1 today)
# Output: Mumbai: order SW1002 delivered (#2 today)
# Output: Delhi: order SW2001 delivered (#1 today)
# Output: Mumbai: order SW1003 delivered (#3 today)
#
# Notice mumbai_tracker and delhi_tracker keep completely separate
# counts — each call to make_delivery_tracker() creates a fresh closure.

print("-" * 50)

# ── Inspecting a closure's captured variables ──

print(mumbai_tracker.__closure__[0].cell_contents)
# Output: Mumbai
print([cell.cell_contents for cell in mumbai_tracker.__closure__])
# Output: ['Mumbai', 3]   (city, orders_delivered — order may vary)

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES — 4 progressively complex worked examples
# ════════════════════════════════════════════════════════════════

# --- Example 1: a function that returns a function based on a condition ---

def get_shipping_calculator(is_prime_member):
    """Returns the correct shipping-fee calculator function."""

    def free_shipping(order_total):
        return 0

    def standard_shipping(order_total):
        return 40 if order_total < 500 else 0

    return free_shipping if is_prime_member else standard_shipping


calc_for_priya = get_shipping_calculator(is_prime_member=True)
calc_for_arjun = get_shipping_calculator(is_prime_member=False)

print(f"Priya's shipping fee: Rs.{calc_for_priya(300)}")
print(f"Arjun's shipping fee: Rs.{calc_for_arjun(300)}")
# Output: Priya's shipping fee: Rs.0
# Output: Arjun's shipping fee: Rs.40

print("-" * 50)

# --- Example 2: closures for a running average (Meera's expense tracker) ---

def make_expense_averager():
    """Closure that tracks a running average of expenses in rupees."""
    total = 0
    count = 0

    def add_expense(amount):
        nonlocal total, count
        total += amount
        count += 1
        return round(total / count, 2)

    return add_expense


meera_average = make_expense_averager()
print(meera_average(500))    # Output: 500.0
print(meera_average(300))    # Output: 400.0
print(meera_average(700))    # Output: 500.0

print("-" * 50)

# --- Example 3: using a function as a dictionary value (dispatch table) ---

def handle_credit_card(amount):
    return f"Charged Rs.{amount} to credit card"


def handle_upi(amount):
    return f"Paid Rs.{amount} via UPI (Paytm)"


def handle_cod(amount):
    return f"Cash on delivery: collect Rs.{amount}"


payment_dispatch = {
    "card": handle_credit_card,
    "upi": handle_upi,
    "cod": handle_cod,
}

selected_method = "upi"  # simulating a user's selection
print(payment_dispatch[selected_method](1250))
# Output: Paid Rs.1250 via UPI (Paytm)

print("-" * 50)

# --- Example 4: a closure-based simple event counter for IRCTC bookings ---

def make_booking_counter():
    """Returns two functions sharing the same closure state."""
    bookings = []

    def add_booking(pnr):
        bookings.append(pnr)
        return f"Booking {pnr} recorded"

    def total_bookings():
        return len(bookings)

    return add_booking, total_bookings


record_booking, get_total = make_booking_counter()

print(record_booking("PNR1001"))
print(record_booking("PNR1002"))
print(f"Total bookings so far: {get_total()}")
# Output: Booking PNR1001 recorded
# Output: Booking PNR1002 recorded
# Output: Total bookings so far: 2

print("-" * 50)


# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
#
# Write a closure factory `make_bank_account(starting_balance)` that
# returns two inner functions: `deposit(amount)` and `withdraw(amount)`.
# - deposit should add to the balance and return the new balance
# - withdraw should subtract from the balance (never going negative —
#   if the withdrawal would go negative, return "Insufficient funds"
#   instead) and otherwise return the new balance
#
# Expected output when run against the test calls below:
#   500
#   remaining balance after using: 300
#   Insufficient funds

# YOUR CODE HERE
def make_bank_account(starting_balance):
    balance = starting_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance

    return deposit, withdraw


# Test calls (do not modify):
deposit, withdraw = make_bank_account(200)
print(deposit(300))          # Expected: 500
result = withdraw(200)
print(f"remaining balance after using: {result}")   # Expected: remaining balance after using: 300
print(withdraw(10000))       # Expected: Insufficient funds


# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
#
# In this file you learned:
#   - Functions are first-class objects: assign, store, pass, return them
#   - Higher-order functions accept and/or return other functions
#   - Closures let an inner function remember free variables from its
#     enclosing scope, even after that scope has finished executing
#   - `nonlocal` is required when the inner function needs to MODIFY
#     (not just read) a captured variable
#
# Next file: day14_02_decorators_from_scratch.py
# We combine first-class functions + closures to build our own
# decorators using the @ syntax, and learn why functools.wraps matters.

if __name__ == "__main__":
    print("\nDay 14, File 1 complete — first-class functions & closures.")
