"""
Day 6 — Data Structures
File 4 of 4: Sets & Comprehensions

What this file covers:
    - Creating sets and understanding uniqueness
    - Set operations: union, intersection, difference
    - List comprehensions
    - Dict comprehensions
    - Set comprehensions

Prerequisites:
    - day06_01_lists.py, day06_02_tuples.py, day06_03_dictionaries.py

How to run:
    python3 day06_04_sets_comprehensions.py
"""


# ════════════════════════════════════════════════════════════
# SECTION A — Creating Sets
# ════════════════════════════════════════════════════════════
# A set stores UNIQUE items only, with NO guaranteed order.
# Adding a duplicate simply has no effect.

print("═" * 50)
print("SECTION A: Creating Sets")
print("═" * 50)

mumbai_visitors = {"Priya", "Arjun", "Priya", "Riya"}
print("Mumbai visitors (duplicates removed):", mumbai_visitors)
print("Type:", type(mumbai_visitors))
# Output:
# Mumbai visitors (duplicates removed): {'Priya', 'Arjun', 'Riya'}
# Type: <class 'set'>

# Converting a list to a set is a quick way to de-duplicate.
repeated_cities = ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi"]
unique_cities = set(repeated_cities)
print("Unique cities:", unique_cities)
# Output: Unique cities: {'Mumbai', 'Delhi', 'Pune'}

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION B — Set Operations
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION B: Set Operations")
print("═" * 50)

delhi_visitors = {"Riya", "Sanjay"}

print("Union (| ):", mumbai_visitors | delhi_visitors)
print("Intersection (&):", mumbai_visitors & delhi_visitors)
print("Difference (-):", mumbai_visitors - delhi_visitors)
print("Symmetric difference (^):", mumbai_visitors ^ delhi_visitors)
# Output:
# Union (| ): {'Priya', 'Arjun', 'Riya', 'Sanjay'}
# Intersection (&): {'Riya'}
# Difference (-): {'Priya', 'Arjun'}
# Symmetric difference (^): {'Priya', 'Arjun', 'Sanjay'}

print("-" * 50)

# Adding, removing, and membership testing
mumbai_visitors.add("Kavita")
mumbai_visitors.discard("Arjun")     # no error even if item is absent
print("Updated set:", mumbai_visitors)
print("Is 'Priya' in the set?", "Priya" in mumbai_visitors)
# Output:
# Updated set: {'Priya', 'Riya', 'Kavita'}   (order may vary)
# Is 'Priya' in the set? True

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION C — List Comprehensions
# ════════════════════════════════════════════════════════════
# A comprehension is a compact way to build a new collection from
# an existing iterable, optionally filtering with an `if` clause.
print("═" * 50)
print("SECTION C: List Comprehensions")
print("═" * 50)

# The long way, with a regular loop:
squares_loop = []
for n in range(1, 6):
    squares_loop.append(n ** 2)
print("Squares (loop):", squares_loop)

# The comprehension way -- same result, one line:
squares = [n ** 2 for n in range(1, 6)]
print("Squares (comprehension):", squares)
# Output:
# Squares (loop): [1, 4, 9, 16, 25]
# Squares (comprehension): [1, 4, 9, 16, 25]

print("-" * 50)

# Comprehensions can filter with an `if` clause.
prices_in_rupees = [120, 560, 45, 899, 300, 610]
expensive_items = [price for price in prices_in_rupees if price > 500]
print("Prices above Rs.500:", expensive_items)
# Output: Prices above Rs.500: [560, 899, 610]

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION D — Dict and Set Comprehensions
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION D: Dict & Set Comprehensions")
print("═" * 50)

price_in_rupees = {"tea": 15, "coffee": 25, "samosa": 20}
doubled_prices = {item: price * 2 for item, price in price_in_rupees.items()}
print("Doubled prices:", doubled_prices)
# Output: Doubled prices: {'tea': 30, 'coffee': 50, 'samosa': 40}

print("-" * 50)

even_set = {n for n in range(10) if n % 2 == 0}
print("Even numbers set:", even_set)
# Output: Even numbers set: {0, 2, 4, 6, 8}

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1: Finding common subjects between two students using sets
priya_subjects = {"Math", "Physics", "Chemistry"}
arjun_subjects = {"Physics", "Biology", "Math"}
common_subjects = priya_subjects & arjun_subjects
print(f"Example 1 -- Common subjects: {common_subjects}")
# Output: Example 1 -- Common subjects: {'Physics', 'Math'}

# Example 2: List comprehension to convert Celsius to Fahrenheit
celsius_temps = [25, 30, 22, 35]
fahrenheit_temps = [(c * 9 / 5) + 32 for c in celsius_temps]
print(f"Example 2 -- Fahrenheit temps: {fahrenheit_temps}")
# Output: Example 2 -- Fahrenheit temps: [77.0, 86.0, 71.6, 95.0]

# Example 3: Dict comprehension to build a name-length lookup
names = ["Priya", "Arjun", "Riya Deshmukh", "Sanjay Verma"]
name_lengths = {name: len(name) for name in names}
print(f"Example 3 -- Name lengths: {name_lengths}")
# Output: Example 3 -- Name lengths: {'Priya': 5, 'Arjun': 5,
#         'Riya Deshmukh': 13, 'Sanjay Verma': 12}

# Example 4: Set comprehension to find unique first letters of cities
cities = ["Mumbai", "Delhi", "Manali", "Dehradun", "Pune"]
unique_first_letters = {city[0] for city in cities}
print(f"Example 4 -- Unique first letters: {unique_first_letters}")
# Output: Example 4 -- Unique first letters: {'M', 'D', 'P'}

print("-" * 50)


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Task: Given the list of exam scores below, write a single list
# comprehension that produces a list of "Pass"/"Fail" strings
# (Pass if score >= 40, else Fail).
#
# Expected output:
#   Results: ['Pass', 'Fail', 'Pass', 'Pass', 'Fail']

exam_scores = [55, 32, 78, 40, 25]

# YOUR CODE HERE


# SOLUTION:
# results = ["Pass" if score >= 40 else "Fail" for score in exam_scores]
# print("Results:", results)


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file we covered:
#   - Creating sets and why duplicates disappear automatically
#   - Set operations: union (|), intersection (&), difference (-)
#   - List comprehensions, with optional `if` filtering
#   - Dict comprehensions and set comprehensions
#
# This wraps up Day 6 -- Data Structures. Next up: Day 7 covers
# Strings & String Methods, including f-strings and the re module.
