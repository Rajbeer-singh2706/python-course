"""
Day 13 — Iterators & Generators
File 2 of 4: Generator Functions (yield)

Covers:
    - The `yield` keyword and how generator functions work
    - Generator state being paused/resumed between calls
    - StopIteration being raised automatically when a generator finishes
    - Why generators are memory-efficient (lazy evaluation)

Prerequisites:
    - Day 13, File 1: Iterators Basics

How to run:
    python day13_02_generators_yield.py
"""

# ════════════════════════════════════════════════════════════════════════
# SECTION A — Your First Generator Function
# ════════════════════════════════════════════════════════════════════════
# Any function containing `yield` automatically becomes a generator
# function. Calling it does NOT run the function body — it returns a
# generator object. Code only runs when next() is called (or the
# generator is iterated over).

def delivery_route_gen(stops):
    """Generator version of the iterator from File 1 — far less code."""
    for stop in stops:
        yield stop


route = delivery_route_gen(["Andheri", "Bandra", "Worli"])
print(type(route))            # Output: <class 'generator'>
print(next(route))            # Output: Andheri
print(next(route))            # Output: Bandra
print(next(route))            # Output: Worli
# next(route) here would raise StopIteration — generator is exhausted

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION B — Generators Pause and Resume (Keep State!)
# ════════════════════════════════════════════════════════════════════════
# Each yield pauses execution exactly where it is, remembering all local
# variables. The next call to next() resumes right after that yield.

def order_tracker():
    print("  [generator] Starting order tracking...")
    total = 0
    for amount in [250, 400, 999]:
        total += amount
        print(f"  [generator] About to yield, running total so far: ₹{total}")
        yield total
    print("  [generator] No more orders, tracker finished.")


print("Driving order_tracker() step by step:")
tracker = order_tracker()
print("Calling next() #1:")
print("  ->", next(tracker))
print("Calling next() #2:")
print("  ->", next(tracker))
print("Calling next() #3:")
print("  ->", next(tracker))
# Output (interleaved prints show the pause/resume behaviour):
#   [generator] Starting order tracking...
#   [generator] About to yield, running total so far: ₹250
#   -> 250
#   [generator] About to yield, running total so far: ₹650
#   -> 650
#   [generator] About to yield, running total so far: ₹1649
#   -> 1649

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION C — Filtering Lazily with a Generator
# ════════════════════════════════════════════════════════════════════════

def order_amounts_above(orders, threshold):
    """Lazily yields only order amounts above a threshold (in rupees)."""
    for order in orders:
        if order > threshold:
            yield order


orders = [250, 720, 150, 980, 60, 1500]
print("High-value orders (above ₹500):")
for amt in order_amounts_above(orders, 500):
    print(f"  ₹{amt}")
# Output:
#   ₹720
#   ₹980
#   ₹1500

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION D — Guided Examples
# ════════════════════════════════════════════════════════════════════════

# Example 1: An infinite generator (must be consumed carefully, e.g. with a limit)
def auto_invoice_numbers(prefix="INV"):
    """Infinite generator producing invoice numbers — pairs well with a limit."""
    n = 1
    while True:
        yield f"{prefix}-{n:04d}"
        n += 1


print("Example 1 — First 5 auto-generated invoice numbers:")
invoice_gen = auto_invoice_numbers()
for _ in range(5):
    print(f"  {next(invoice_gen)}")
# Output:
#   INV-0001
#   INV-0002
#   INV-0003
#   INV-0004
#   INV-0005
print("-" * 50)


# Example 2: Generator that converts a list of names to greetings, lazily
def greeting_generator(names, city="Mumbai"):
    for name in names:
        yield f"Namaste {name}, welcome to our {city} store!"


print("Example 2 — Greeting customers one at a time:")
customers = ["Priya", "Arjun", "Riya Deshmukh"]
for greeting in greeting_generator(customers):
    print(f"  {greeting}")
print("-" * 50)


# Example 3: Generator with `return` to stop early (return inside a generator
# raises StopIteration immediately, optionally carrying a value)
def first_three_under_budget(prices, budget):
    """Yields prices under budget, stopping completely once 3 are found."""
    count = 0
    for price in prices:
        if price <= budget:
            yield price
            count += 1
            if count == 3:
                return  # stops the generator early


print("Example 3 — First 3 items Sanjay can afford under ₹1000:")
catalog_prices = [1200, 800, 450, 1500, 999, 300, 50]
for p in first_three_under_budget(catalog_prices, 1000):
    print(f"  ₹{p}")
# Output:
#   ₹800
#   ₹450
#   ₹999
print("-" * 50)


# Example 4: Using `yield` to build a simple running-average generator
def running_average():
    """Send-free simple version: yields the running average of values seen
    so far each time it's advanced (paired with a feeder list)."""
    total = 0
    count = 0
    values = [100, 200, 300, 400]
    for v in values:
        total += v
        count += 1
        yield total / count


print("Example 4 — Running average of Riya's daily sales (₹):")
for avg in running_average():
    print(f"  Running average: ₹{avg:.2f}")
# Output:
#   Running average: ₹100.00
#   Running average: ₹150.00
#   Running average: ₹200.00
#   Running average: ₹250.00

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════════════
# Write a generator function `squares_up_to(n)` that yields the squares of
# numbers from 1 up to and including n.
#
# Example:
#   for sq in squares_up_to(5):
#       print(sq)
#   Expected output: 1 4 9 16 25

# YOUR CODE HERE


# SOLUTION:
# def squares_up_to(n):
#     for i in range(1, n + 1):
#         yield i * i
#
# for sq in squares_up_to(5):
#     print(sq)


# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
# - `yield` turns an ordinary function into a generator function.
# - Calling a generator function returns a generator object immediately —
#   no code runs until next() is called or it's iterated over.
# - Each yield pauses execution, preserving local state, until the next
#   next() call resumes it.
# - A generator can run forever (infinite generator) as long as you only
#   ever pull a finite number of values from it.
# - `return` inside a generator stops it early (raises StopIteration).
#
# Next up (File 3 of 4): Generator expressions — the compact one-line
# cousin of generator functions.

if __name__ == "__main__":
    print("Day 13, File 2 — Generators (yield): all demonstrations ran successfully.")
