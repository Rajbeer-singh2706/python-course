"""
Day 6 — Data Structures
File 1 of 4: Lists — creation, mutation, methods, and slicing

What this file covers:
    - Creating lists and understanding what makes them useful
    - Indexing and mutating list items
    - Common list methods: append, extend, insert, remove, pop, sort, reverse
    - Slicing syntax: list[start:stop:step]
    - Copying lists correctly (reference vs. real copy)

Prerequisites:
    - Day 5: Functions & Scope
    - Comfort with variables, loops, and basic conditionals (Days 2-4)

How to run:
    python3 day06_01_lists.py
"""


# ════════════════════════════════════════════════════════════
# SECTION A — Creating and Understanding Lists
# ════════════════════════════════════════════════════════════
# A list is an ORDERED, MUTABLE (changeable) collection of items.
# Unlike a single variable, a list can hold many values, and the
# order in which you put them in is remembered.
#
# Think of Priya's weekly grocery list: rice, dal, milk, vegetables.
# The order matters (rice first, milk last), and she can add or
# cross off items as the week goes on -- exactly like a Python list.

print("═" * 50)
print("SECTION A: Creating Lists")
print("═" * 50)

grocery_list = ["rice", "dal", "milk", "vegetables"]
print("Priya's grocery list:", grocery_list)
print("Type:", type(grocery_list))
# Output:
# Priya's grocery list: ['rice', 'dal', 'milk', 'vegetables']
# Type: <class 'list'>

# Lists can hold mixed types, though in practice we usually keep
# one type per list for clarity.
mixed_list = ["Arjun", 21, True, 5.5]
print("Mixed list:", mixed_list)
# Output: Mixed list: ['Arjun', 21, True, 5.5]

print("-" * 50)


# ── Indexing ──
# Just like strings, list items are accessed with square brackets
# and zero-based indices. Negative indices count from the end.
print("First item:", grocery_list[0])       # rice
print("Last item:", grocery_list[-1])        # vegetables
print("Second item:", grocery_list[1])       # dal
# Output:
# First item: rice
# Last item: vegetables
# Second item: dal

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION B — Mutating Lists
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION B: Mutating Lists")
print("═" * 50)

# ── Changing an item by index ──
grocery_list[0] = "basmati rice"
print("After renaming item 0:", grocery_list)
# Output: After renaming item 0: ['basmati rice', 'dal', 'milk', 'vegetables']

# ── append() vs extend() ──
# append() adds ONE item to the end.
# extend() merges the items of ANOTHER iterable into the list.
grocery_list.append("sugar")
print("After append('sugar'):", grocery_list)
# Output: After append('sugar'): ['basmati rice', 'dal', 'milk', 'vegetables', 'sugar']

grocery_list.extend(["tea", "salt"])
print("After extend(['tea', 'salt']):", grocery_list)
# Output: After extend(['tea', 'salt']): [..., 'sugar', 'tea', 'salt']

# Common mistake: grocery_list.append(["tea", "salt"]) would add ONE
# nested list item, not two separate items. Try to avoid this bug.

print("-" * 50)

# ── remove(), pop(), insert() ──
grocery_list.remove("milk")          # removes by VALUE
print("After remove('milk'):", grocery_list)

popped_item = grocery_list.pop()     # removes and RETURNS the last item
print("Popped item:", popped_item)
print("List after pop():", grocery_list)

grocery_list.insert(1, "ghee")       # insert 'ghee' at index 1
print("After insert(1, 'ghee'):", grocery_list)
# Output:
# After remove('milk'): ['basmati rice', 'dal', 'vegetables', 'sugar', 'tea', 'salt']
# Popped item: salt
# List after pop(): ['basmati rice', 'dal', 'vegetables', 'sugar', 'tea']
# After insert(1, 'ghee'): ['basmati rice', 'ghee', 'dal', 'vegetables', 'sugar', 'tea']

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION C — Sorting, Reversing, and Useful Methods
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION C: Sorting & Useful Methods")
print("═" * 50)

prices_in_rupees = [450, 120, 899, 60, 310]
print("Original prices:", prices_in_rupees)

prices_in_rupees.sort()
print("Sorted ascending:", prices_in_rupees)

prices_in_rupees.sort(reverse=True)
print("Sorted descending:", prices_in_rupees)

prices_in_rupees.reverse()
print("Reversed:", prices_in_rupees)

print("Length:", len(prices_in_rupees))
print("Is 899 in the list?", 899 in prices_in_rupees)
print("Index of 310:", prices_in_rupees.index(310))
# Output:
# Original prices: [450, 120, 899, 60, 310]
# Sorted ascending: [60, 120, 310, 450, 899]
# Sorted descending: [899, 450, 310, 120, 60]
# Reversed: [60, 120, 310, 450, 899]
# Length: 5
# Is 899 in the list? True
# Index of 310: 2

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION D — Slicing Syntax
# ════════════════════════════════════════════════════════════
# Slicing uses list[start:stop:step] to extract a sub-list.
# IMPORTANT: 'stop' is EXCLUSIVE -- Python stops BEFORE that index.
print("═" * 50)
print("SECTION D: Slicing")
print("═" * 50)

localities = ["Andheri", "Bandra", "Colaba", "Dadar", "Worli"]
print("All localities:", localities)
print("localities[1:3]:", localities[1:3])       # ['Bandra', 'Colaba']
print("localities[:2]:", localities[:2])         # ['Andheri', 'Bandra']
print("localities[-2:]:", localities[-2:])       # ['Dadar', 'Worli']
print("localities[::-1]:", localities[::-1])     # reversed copy
print("localities[::2]:", localities[::2])       # every second item
# Output:
# All localities: ['Andheri', 'Bandra', 'Colaba', 'Dadar', 'Worli']
# localities[1:3]: ['Bandra', 'Colaba']
# localities[:2]: ['Andheri', 'Bandra']
# localities[-2:]: ['Dadar', 'Worli']
# localities[::-1]: ['Worli', 'Dadar', 'Colaba', 'Bandra', 'Andheri']
# localities[::2]: ['Andheri', 'Colaba', 'Worli']

print("-" * 50)

# Slicing works on strings the same way.
city = "Mumbai"
print("city[1:4]:", city[1:4])   # 'umb'
# Output: city[1:4]: umb

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION E — Copying Lists Correctly
# ════════════════════════════════════════════════════════════
# b = a only copies the REFERENCE -- both names point to the same
# list in memory. Changing one changes the other!
print("═" * 50)
print("SECTION E: Copying Lists")
print("═" * 50)

original = ["Priya", "Arjun"]
reference_copy = original          # NOT a real copy
reference_copy.append("Riya")
print("original after mutating reference_copy:", original)
# Output: original after mutating reference_copy: ['Priya', 'Arjun', 'Riya']
# Notice 'original' changed too -- this is the reference-copy trap!

real_copy = original.copy()        # or original[:]
real_copy.append("Sanjay")
print("original after mutating real_copy:", original)
print("real_copy:", real_copy)
# Output:
# original after mutating real_copy: ['Priya', 'Arjun', 'Riya']
# real_copy: ['Priya', 'Arjun', 'Riya', 'Sanjay']

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1: Building a shopping cart total
cart_items = ["notebook", "pen", "eraser"]
cart_prices = [60, 10, 5]
total = sum(cart_prices)
print(f"Example 1 -- Cart items: {cart_items}, Total: Rs.{total}")
# Output: Example 1 -- Cart items: ['notebook', 'pen', 'eraser'], Total: Rs.75

# Example 2: Filtering a list of exam scores above a cutoff
exam_scores = [45, 78, 92, 34, 88, 61]
passing_scores = []
for score in exam_scores:
    if score >= 50:
        passing_scores.append(score)
print(f"Example 2 -- Passing scores (>=50): {passing_scores}")
# Output: Example 2 -- Passing scores (>=50): [78, 92, 88, 61]

# Example 3: Reversing a guest list for a Delhi wedding
guest_list = ["Sanjay Verma", "Riya Deshmukh", "Arjun", "Priya"]
print(f"Example 3 -- Guests in reverse order: {guest_list[::-1]}")
# Output: Example 3 -- Guests in reverse order: ['Priya', 'Arjun', 'Riya Deshmukh', 'Sanjay Verma']

# Example 4: Splitting a delivery route into first-half / second-half stops
delivery_stops = ["Andheri", "Bandra", "Dadar", "Worli", "Colaba", "Fort"]
midpoint = len(delivery_stops) // 2
first_half = delivery_stops[:midpoint]
second_half = delivery_stops[midpoint:]
print(f"Example 4 -- First half: {first_half}, Second half: {second_half}")
# Output: Example 4 -- First half: ['Andheri', 'Bandra', 'Dadar'], Second half: ['Worli', 'Colaba', 'Fort']

print("-" * 50)


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Task: Given the list of monthly expenses (in rupees) below, write
# code that:
#   1. Adds a new expense of 750 for "mobile recharge" info (just the number)
#   2. Removes the expense equal to 200
#   3. Prints the three highest expenses using slicing on a sorted copy
#
# Expected output (order of prints may vary slightly):
#   Updated expenses: [1200, 3400, 200(removed), 750, ...]
#   Top 3 expenses: [<three largest numbers>]

monthly_expenses = [1200, 3400, 200, 900, 1500]

# YOUR CODE HERE


# SOLUTION:
# monthly_expenses.append(750)
# monthly_expenses.remove(200)
# top_three = sorted(monthly_expenses, reverse=True)[:3]
# print("Updated expenses:", monthly_expenses)
# print("Top 3 expenses:", top_three)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file we covered:
#   - Creating and indexing lists
#   - Mutating lists: append, extend, insert, remove, pop
#   - Sorting and reversing lists
#   - Slicing syntax: list[start:stop:step] (stop is exclusive!)
#   - Reference copies vs. real copies (.copy() or [:])
#
# Next up: day06_02_tuples.py -- immutable, ordered collections and
# how packing/unpacking works.
