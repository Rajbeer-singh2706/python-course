"""
Day 5 — Functions & Scope
File 3 of 3: Scope and the LEGB Rule

Covers:
    - Local scope
    - Enclosing scope
    - Global scope
    - Built-in scope
    - The LEGB lookup order
    - The `global` keyword

Prerequisites:
    - Day 5, File 1: Function Basics
    - Day 5, File 2: *args and **kwargs

How to run:
    python day05_03_scope_legb.py
"""

# ════════════════════════════════════════════════════════
# SECTION A — Local Scope
# ════════════════════════════════════════════════════════
#
# A variable created INSIDE a function only exists inside that function.
# This is called "local scope." It cannot be accessed from outside.

# ── Concept: Local Variables ──


def calculate_bonus(salary):
    bonus = salary * 0.10  # 'bonus' is local to this function
    return bonus


print(f"Bonus: Rs. {calculate_bonus(50000)}")
# Output: Bonus: Rs. 5000.0

# Trying to access 'bonus' here would raise a NameError, because
# 'bonus' only exists inside calculate_bonus().
# print(bonus)  # This line would cause: NameError: name 'bonus' is not defined

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION B — Global Scope
# ════════════════════════════════════════════════════════
#
# A variable created OUTSIDE any function, at the top level of the file,
# is in "global scope." It can be READ from inside any function.

# ── Concept: Reading a Global Variable ──

college_name = "Mumbai Institute of Technology"  # global variable


def print_college():
    # We can READ the global variable without any special keyword
    print(f"Welcome to {college_name}")


print_college()
# Output: Welcome to Mumbai Institute of Technology

print("-" * 50)

# ── Concept: Modifying a Global Variable Needs `global` ──

total_registrations = 0  # global variable


def register_student_wrong():
    # This creates a NEW local variable called total_registrations,
    # it does NOT modify the global one!
    total_registrations = total_registrations + 1
    return total_registrations


# Uncommenting the line below would raise:
# UnboundLocalError: local variable 'total_registrations' referenced before assignment
# register_student_wrong()


def register_student_correct():
    global total_registrations  # tells Python: use the global variable
    total_registrations = total_registrations + 1


register_student_correct()
register_student_correct()
register_student_correct()
print(f"Total registrations: {total_registrations}")
# Output: Total registrations: 3

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION C — Enclosing Scope (Nested Functions)
# ════════════════════════════════════════════════════════
#
# When a function is defined inside another function, the inner
# function can read variables from the outer (enclosing) function.
# This is the "E" in LEGB.

# ── Concept: Enclosing Scope ──


def outer_batch_manager():
    batch_name = "Python Batch A"  # enclosing variable

    def announce():
        # 'batch_name' is not local to announce(), but it's found
        # in the enclosing scope of outer_batch_manager()
        print(f"Announcing for: {batch_name}")

    announce()


outer_batch_manager()
# Output: Announcing for: Python Batch A

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION D — Built-in Scope
# ════════════════════════════════════════════════════════
#
# Python has a set of built-in names always available, like
# print, len, sum, range, etc. These live in the "built-in" scope —
# the last place Python looks when resolving a name.

# ── Concept: Built-in Names ──

numbers_list = [10, 20, 30, 40]
print(f"len() is a built-in function: {len(numbers_list)}")
print(f"sum() is a built-in function: {sum(numbers_list)}")
# Output:
# len() is a built-in function: 4
# sum() is a built-in function: 100

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION E — The LEGB Rule (Putting It Together)
# ════════════════════════════════════════════════════════
#
# When Python looks up a name, it searches in this order:
#   L — Local        (inside the current function)
#   E — Enclosing     (inside any outer function)
#   G — Global        (top-level of the file/module)
#   B — Built-in      (Python's built-in names)
#
# Python stops at the FIRST place it finds the name.

# ── Concept: LEGB in Action ──

city = "Mumbai"  # Global


def travel_planner():
    city = "Delhi"  # Local (shadows the global 'city')

    def inner_trip():
        city = "Pune"  # Local to inner_trip (shadows both above)
        print(f"Inside inner_trip: {city}")  # finds Local -> Pune

    inner_trip()
    print(f"Inside travel_planner: {city}")  # finds Local -> Delhi


travel_planner()
print(f"At global level: {city}")  # finds Global -> Mumbai
# Output:
# Inside inner_trip: Pune
# Inside travel_planner: Delhi
# At global level: Mumbai

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION F — Guided Examples
# ════════════════════════════════════════════════════════

# Example 1: Global counter for a Mumbai grocery delivery app
print("Example 1: Order Counter")

orders_placed = 0


def place_order(item):
    global orders_placed
    orders_placed += 1
    print(f"Order #{orders_placed} placed for {item}")


place_order("Rice - 5kg")
place_order("Milk - 2L")
print("-" * 50)

# Example 2: Enclosing scope with a discount calculator
print("Example 2: Store Discount Calculator")


def store_manager(store_name):
    discount_rate = 0.15  # enclosing variable

    def final_price(price):
        return price - (price * discount_rate)

    return final_price


calculate_discounted_price = store_manager("Mumbai Mart")
print(f"Final price: Rs. {calculate_discounted_price(2000)}")
print("-" * 50)

# Example 3: Local variables don't leak between function calls
print("Example 3: Independent Local Variables")


def process_ticket(ticket_id):
    status = "Processed"  # local, fresh each call
    print(f"Ticket {ticket_id}: {status}")


process_ticket(101)
process_ticket(102)
print("-" * 50)

# Example 4: Mixing global read and built-in functions
print("Example 4: Batch Statistics")

batch_scores = [88, 92, 76, 95, 60]


def batch_summary():
    # Reads the global 'batch_scores', uses built-in sum() and len()
    average = sum(batch_scores) / len(batch_scores)
    print(f"Batch average: {round(average, 2)}")
    print(f"Highest score (built-in max): {max(batch_scores)}")


batch_summary()
print("-" * 50)


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Write the following:
#   1. A global variable `wallet_balance = 1000`
#   2. A function `spend_money(amount)` that uses the `global` keyword
#      to subtract `amount` from `wallet_balance`
#   3. A function `check_balance()` that prints the current
#      `wallet_balance` (no need for `global` here since it's read-only)
#
# Call spend_money() a couple of times with different amounts, then
# call check_balance() to confirm the balance updated correctly.
#
# Expected output (example):
#   Spent Rs. 200. Remaining will be shown below.
#   Spent Rs. 150. Remaining will be shown below.
#   Current wallet balance: Rs. 650

# YOUR CODE HERE


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# In this file, you learned:
#   - Local scope — variables that live only inside a function
#   - Global scope — variables at the top level, readable everywhere,
#     but requiring the `global` keyword to modify from inside a function
#   - Enclosing scope — variables from an outer function visible to
#     a nested inner function
#   - Built-in scope — Python's always-available names (print, len, etc.)
#   - The LEGB rule — the order Python searches: Local, Enclosing,
#     Global, Built-in
#
# This wraps up Day 5! Next up: Day 6 — Data Structures
# (lists, tuples, dictionaries, sets, and comprehensions).
