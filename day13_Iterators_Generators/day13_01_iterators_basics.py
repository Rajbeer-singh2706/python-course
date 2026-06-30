"""
Day 13 — Iterators & Generators
File 1 of 4: Iterators Basics (__iter__ / __next__)

Covers:
    - What "iterable" and "iterator" actually mean
    - Building a custom iterator class from scratch
    - The StopIteration exception
    - Manually driving an iterator with iter() / next()

Prerequisites:
    - Day 10: Classes, __init__, self
    - Day 11: Inheritance & dunder methods

How to run:
    python day13_01_iterators_basics.py
"""

# ════════════════════════════════════════════════════════════════════════
# SECTION A — What is an Iterable vs an Iterator?
# ════════════════════════════════════════════════════════════════════════
# An ITERABLE is anything you can loop over (lists, tuples, strings, dicts).
# An ITERATOR is the object that actually produces values, one at a time,
# via next(). Every iterator is also an iterable (it has __iter__ that
# returns itself), but most iterables (like a plain list) are NOT iterators
# themselves — calling iter() on them PRODUCES a fresh iterator.

numbers = [10, 20, 30]          # numbers is ITERABLE
iterator = iter(numbers)        # iter() gives us an ITERATOR
print(type(numbers))            # Output: <class 'list'>
print(type(iterator))           # Output: <class 'list_iterator'>

print(next(iterator))           # Output: 10
print(next(iterator))           # Output: 20
print(next(iterator))           # Output: 30
# print(next(iterator))         # Would raise StopIteration — list exhausted

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION B — Building a Custom Iterator Class
# ════════════════════════════════════════════════════════════════════════
# To make a class iterable, give it __iter__.
# To make something an iterator, give it __iter__ (returning self) AND
# __next__ (producing the next value, raising StopIteration when done).

class DeliveryRoute:
    """An iterable: represents a sequence of delivery stops across Mumbai."""

    def __init__(self, stops):
        self.stops = stops

    def __iter__(self):
        # Each time someone loops over a DeliveryRoute, hand them a
        # BRAND NEW RouteIterator so the route can be iterated multiple times.
        return RouteIterator(self.stops)


class RouteIterator:
    """The actual iterator: tracks position and produces the next stop."""

    def __init__(self, stops):
        self.stops = stops
        self.index = 0

    def __iter__(self):
        return self  # an iterator's __iter__ just returns itself

    def __next__(self):
        if self.index >= len(self.stops):
            raise StopIteration
        stop = self.stops[self.index]
        self.index += 1
        return stop


route = DeliveryRoute(["Andheri", "Bandra", "Worli", "Colaba"])

print("First pass:")
for stop in route:
    print(f"  -> {stop}")

print("Second pass (works again — __iter__ gives a fresh iterator):")
for stop in route:
    print(f"  -> {stop}")
# Output:
# First pass:
#   -> Andheri
#   -> Bandra
#   -> Worli
#   -> Colaba
# Second pass (works again — __iter__ gives a fresh iterator):
#   -> Andheri
#   -> Bandra
#   -> Worli
#   -> Colaba

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION C — Driving an Iterator Manually
# ════════════════════════════════════════════════════════════════════════
# A for loop is really just sugar for repeatedly calling next() inside a
# try/except StopIteration block. Let's prove it.

manual_iter = iter(route)
while True:
    try:
        stop = next(manual_iter)
        print(f"Visiting: {stop}")
    except StopIteration:
        print("Route complete — no more stops.")
        break
# Output:
# Visiting: Andheri
# Visiting: Bandra
# Visiting: Worli
# Visiting: Colaba
# Route complete — no more stops.

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION D — Guided Examples
# ════════════════════════════════════════════════════════════════════════

# Example 1: Counting down from a number (countdown timer for Riya's quiz app)
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("Example 1 — Quiz countdown for Riya's app:")
for tick in Countdown(3):
    print(f"  {tick}...")
print("  Go!")
print("-" * 50)


# Example 2: Iterating over a custom "Cart" of products with prices in rupees
class ShoppingCart:
    def __init__(self, items):
        self.items = items  # list of (name, price) tuples

    def __iter__(self):
        return CartIterator(self.items)


class CartIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item


cart = ShoppingCart([("Notebook", 60), ("Pen Set", 120), ("Backpack", 1450)])
print("Example 2 — Arjun's shopping cart:")
total = 0
for name, price in cart:
    print(f"  {name}: ₹{price}")
    total += price
print(f"  Total: ₹{total}")
# Output:
#   Notebook: ₹60
#   Pen Set: ₹120
#   Backpack: ₹1450
#   Total: ₹1630
print("-" * 50)


# Example 3: An iterator that skips invalid (negative) values
class ValidAmountsIterator:
    """Skips negative numbers — useful for cleaning messy transaction data."""

    def __init__(self, amounts):
        self.amounts = amounts
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.amounts):
            value = self.amounts[self.index]
            self.index += 1
            if value >= 0:
                return value
        raise StopIteration


print("Example 3 — Sanjay's cleaned transaction amounts:")
raw_amounts = [500, -20, 750, -5, 300]
for amt in ValidAmountsIterator(raw_amounts):
    print(f"  Valid amount: ₹{amt}")
# Output:
#   Valid amount: ₹500
#   Valid amount: ₹750
#   Valid amount: ₹300
print("-" * 50)


# Example 4: Manually exhausting an iterator and catching StopIteration safely
print("Example 4 — Manually checking when a route iterator is exhausted:")
short_route = DeliveryRoute(["Colaba", "Worli"])
it = iter(short_route)
results = []
while True:
    try:
        results.append(next(it))
    except StopIteration:
        break
print(f"  Collected stops: {results}")
# Output:
#   Collected stops: ['Colaba', 'Worli']

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════════════
# Build a class `EvenNumbers` that is an iterator producing even numbers
# from 0 up to (but not including) a given limit.
#
# Example:
#   for n in EvenNumbers(10):
#       print(n)
#   Expected output: 0 2 4 6 8

# YOUR CODE HERE


# SOLUTION:
# class EvenNumbers:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.limit:
#             raise StopIteration
#         value = self.current
#         self.current += 2
#         return value
#
# for n in EvenNumbers(10):
#     print(n)


# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
# - An iterable can be looped over; an iterator is the object that actually
#   produces values via __next__.
# - Custom iterators need __iter__ (returns self) and __next__ (returns the
#   next value or raises StopIteration).
# - for loops are syntactic sugar over iter() + repeated next() calls inside
#   a try/except StopIteration block.
#
# Next up (File 2 of 4): Generator functions — the same protocol, with far
# less boilerplate, using the `yield` keyword.

if __name__ == "__main__":
    print("Day 13, File 1 — Iterators Basics: all demonstrations ran successfully.")
