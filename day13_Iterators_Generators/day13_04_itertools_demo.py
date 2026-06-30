"""
Day 13 — Iterators & Generators
File 4 of 4: The itertools Module

Covers:
    - itertools.chain — joining multiple iterables into one stream
    - itertools.islice — lazily slicing an iterator (even infinite ones)
    - itertools.product — Cartesian product of iterables
    - itertools.cycle — repeating an iterable indefinitely

Prerequisites:
    - Day 13, Files 1–3: Iterators, generators, generator expressions

How to run:
    python day13_04_itertools_demo.py
"""

from itertools import chain, islice, product, cycle, count

# ════════════════════════════════════════════════════════════════════════
# SECTION A — itertools.chain
# ════════════════════════════════════════════════════════════════════════
# chain() joins several iterables end-to-end into a single continuous
# iterator, without copying any of them into a new list first.

mumbai_stops = ["Andheri", "Bandra"]
delhi_stops = ["Saket", "Dwarka"]

all_stops = list(chain(mumbai_stops, delhi_stops))
print(f"All delivery stops (Mumbai + Delhi): {all_stops}")
# Output: All delivery stops (Mumbai + Delhi): ['Andheri', 'Bandra', 'Saket', 'Dwarka']

# chain also works lazily — you don't have to convert to a list immediately
for stop in chain(mumbai_stops, delhi_stops):
    print(f"  Visiting: {stop}")
# Output:
#   Visiting: Andheri
#   Visiting: Bandra
#   Visiting: Saket
#   Visiting: Dwarka

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION B — itertools.islice
# ════════════════════════════════════════════════════════════════════════
# islice() takes a "slice" of an iterator lazily — crucial when the
# iterator is infinite, since list[:5] would never finish on one.

def all_orders():
    """An infinite generator producing order numbers."""
    n = 1
    while True:
        yield n * 111
        n += 1


first_five = list(islice(all_orders(), 5))
print(f"First 5 order numbers: {first_five}")
# Output: First 5 order numbers: [111, 222, 333, 444, 555]

# islice also supports start, stop, step like regular slicing
every_other_of_first_ten = list(islice(all_orders(), 0, 10, 2))
print(f"Every other of first 10: {every_other_of_first_ten}")
# Output: Every other of first 10: [111, 333, 555, 777, 999]

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION C — itertools.product
# ════════════════════════════════════════════════════════════════════════
# product() generates the Cartesian product of iterables — equivalent to
# nested for loops, but lazy and far more readable.

sizes = ["S", "M", "L"]
colors = ["Red", "Blue"]

print("All size/colour combinations for a T-shirt order:")
for combo in product(sizes, colors):
    print(f"  {combo}")
# Output:
#   ('S', 'Red')
#   ('S', 'Blue')
#   ('M', 'Red')
#   ('M', 'Blue')
#   ('L', 'Red')
#   ('L', 'Blue')

# repeat= lets you find the product of an iterable with itself
print("All 2-digit PIN combos using digits 0-2:")
pins = list(product(range(3), repeat=2))
print(f"  {pins}")
# Output:
#   [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# SECTION D — itertools.cycle (and count, for comparison)
# ════════════════════════════════════════════════════════════════════════
# cycle() repeats an iterable FOREVER. Always pair it with islice() or a
# manual break/counter, or your program will hang.

delivery_riders = cycle(["Riya", "Sanjay", "Arjun"])
assigned = list(islice(delivery_riders, 7))
print(f"Riders assigned to 7 consecutive deliveries: {assigned}")
# Output: Riders assigned to 7 consecutive deliveries:
# ['Riya', 'Sanjay', 'Arjun', 'Riya', 'Sanjay', 'Arjun', 'Riya']

# count() is itertools' infinite counter — also needs islice or a break
invoice_numbers = list(islice(count(start=1001, step=1), 4))
print(f"First 4 invoice numbers starting at 1001: {invoice_numbers}")
# Output: First 4 invoice numbers starting at 1001: [1001, 1002, 1003, 1004]

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════════════

# Example 1: Combining two product catalogs (Mumbai warehouse + Delhi warehouse)
mumbai_catalog = ["Notebook", "Pen Set"]
delhi_catalog = ["Backpack", "Water Bottle"]
print("Example 1 — Combined catalog from both warehouses:")
for product_name in chain(mumbai_catalog, delhi_catalog):
    print(f"  {product_name}")
print("-" * 50)


# Example 2: Paging through a large lazy result set with islice
def search_results():
    """Pretend this streams thousands of product matches lazily."""
    n = 1
    while n <= 1000:
        yield f"Product-{n}"
        n += 1


print("Example 2 — Showing results 11-15 (page 3, 5 per page):")
page_3 = list(islice(search_results(), 10, 15))
print(f"  {page_3}")
# Output:
#   ['Product-11', 'Product-12', 'Product-13', 'Product-14', 'Product-15']
print("-" * 50)


# Example 3: Generating all table/seat combos for a restaurant booking system
tables = ["T1", "T2"]
times = ["7:00 PM", "8:30 PM"]
print("Example 3 — All table/time slot combinations:")
for table, time in product(tables, times):
    print(f"  {table} at {time}")
print("-" * 50)


# Example 4: Round-robin assigning support tickets to agents using cycle
agents = cycle(["Meera", "Kabir", "Priya"])
tickets = ["TICKET-1", "TICKET-2", "TICKET-3", "TICKET-4", "TICKET-5"]
print("Example 4 — Round-robin ticket assignment:")
for ticket in tickets:
    agent = next(agents)
    print(f"  {ticket} -> {agent}")
# Output:
#   TICKET-1 -> Meera
#   TICKET-2 -> Kabir
#   TICKET-3 -> Priya
#   TICKET-4 -> Meera
#   TICKET-5 -> Kabir

print("-" * 50)

# ════════════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════════════
# Using itertools, build a list of the first 6 values produced by cycling
# through ["North", "South", "East", "West"] (zone names for a Delhi
# delivery fleet).
#
# Expected output:
# ['North', 'South', 'East', 'West', 'North', 'South']

# YOUR CODE HERE


# SOLUTION:
# zones = cycle(["North", "South", "East", "West"])
# first_six = list(islice(zones, 6))
# print(first_six)


# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
# - chain() joins multiple iterables into a single continuous stream.
# - islice() lazily slices an iterator — essential for infinite iterators.
# - product() generates Cartesian products, replacing nested for loops.
# - cycle() (and count()) repeat/produce values forever — always pair with
#   islice() or another stopping condition.
#
# This completes Day 13's concept files. Next session — Day 14: Decorators
# & Closures — builds directly on the "functions as objects" mental model
# we've been reinforcing with generators today.

if __name__ == "__main__":
    print("Day 13, File 4 — itertools: all demonstrations ran successfully.")
