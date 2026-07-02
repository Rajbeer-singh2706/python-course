"""
Day 6 — Data Structures
File 3 of 4: Dictionaries — key-value pairs and methods

What this file covers:
    - Creating dictionaries and understanding key-value pairs
    - Adding, updating, and removing entries
    - Safe lookups with .get()
    - Iterating with .keys(), .values(), .items()

Prerequisites:
    - day06_01_lists.py, day06_02_tuples.py

How to run:
    python3 day06_03_dictionaries.py
"""


# ════════════════════════════════════════════════════════════
# SECTION A — Creating Dictionaries
# ════════════════════════════════════════════════════════════
# A dictionary is like a phonebook: you look up a NAME (the key)
# to find a NUMBER (the value). Keys must be unique; values can
# repeat.

print("═" * 50)
print("SECTION A: Creating Dictionaries")
print("═" * 50)

student_marks = {"Riya": 88, "Sanjay": 74, "Priya": 91}
print("Student marks:", student_marks)
print("Type:", type(student_marks))
# Output:
# Student marks: {'Riya': 88, 'Sanjay': 74, 'Priya': 91}
# Type: <class 'dict'>

# Looking up a value by key
print("Riya's marks:", student_marks["Riya"])
# Output: Riya's marks: 88

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION B — Adding, Updating, and Removing Entries
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION B: Adding, Updating, Removing")
print("═" * 50)

student_marks["Arjun"] = 67          # add a new key
print("After adding Arjun:", student_marks)

student_marks["Sanjay"] = 79         # update an existing key
print("After updating Sanjay:", student_marks)

del student_marks["Priya"]           # remove a key entirely
print("After deleting Priya:", student_marks)
# Output:
# After adding Arjun: {'Riya': 88, 'Sanjay': 74, 'Priya': 91, 'Arjun': 67}
# After updating Sanjay: {'Riya': 88, 'Sanjay': 79, 'Priya': 91, 'Arjun': 67}
# After deleting Priya: {'Riya': 88, 'Sanjay': 79, 'Arjun': 67}

print("-" * 50)

# .pop() removes a key AND returns its value
removed_value = student_marks.pop("Arjun")
print("Popped value:", removed_value)
print("Dictionary after pop:", student_marks)
# Output:
# Popped value: 67
# Dictionary after pop: {'Riya': 88, 'Sanjay': 79}

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION C — Safe Lookups with .get()
# ════════════════════════════════════════════════════════════
# Accessing a missing key with [] raises a KeyError.
# .get(key, default) returns a fallback value instead of crashing.
print("═" * 50)
print("SECTION C: Safe Lookups")
print("═" * 50)

try:
    print(student_marks["Vikram"])
except KeyError as error:
    print("Error caught:", error)
# Output: Error caught: 'Vikram'

print("Safe lookup with .get():", student_marks.get("Vikram", 0))
print("Safe lookup for existing key:", student_marks.get("Riya", 0))
# Output:
# Safe lookup with .get(): 0
# Safe lookup for existing key: 88

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION D — Iterating Over Dictionaries
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION D: Iterating")
print("═" * 50)

print("Keys:", list(student_marks.keys()))
print("Values:", list(student_marks.values()))
print("Items:", list(student_marks.items()))
# Output:
# Keys: ['Riya', 'Sanjay']
# Values: [88, 79]
# Items: [('Riya', 88), ('Sanjay', 79)]

print("-" * 50)

for name, marks in student_marks.items():
    print(f"{name} scored {marks} marks")
# Output:
# Riya scored 88 marks
# Sanjay scored 79 marks

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1: A price list in rupees for a Mumbai tea stall
tea_stall_prices = {"tea": 15, "coffee": 25, "samosa": 20, "vada pav": 18}
print(f"Example 1 -- Price of samosa: Rs.{tea_stall_prices['samosa']}")
# Output: Example 1 -- Price of samosa: Rs.20

# Example 2: Counting word frequency in a sentence
sentence = "mumbai is a busy city and mumbai never sleeps"
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print("Example 2 -- Word counts:", word_counts)
# Output: Example 2 -- Word counts: {'mumbai': 2, 'is': 1, 'a': 1, 'busy': 1,
#         'city': 1, 'and': 1, 'never': 1, 'sleeps': 1}

# Example 3: Nested dictionary for student profiles
student_profiles = {
    "Riya Deshmukh": {"age": 20, "city": "Mumbai", "marks": 88},
    "Sanjay Verma": {"age": 22, "city": "Delhi", "marks": 79},
}
print(f"Example 3 -- Riya's city: {student_profiles['Riya Deshmukh']['city']}")
# Output: Example 3 -- Riya's city: Mumbai

# Example 4: Merging two dictionaries with the update() method
weekday_prices = {"tea": 15, "coffee": 25}
weekend_prices = {"coffee": 30, "cold coffee": 40}
weekday_prices.update(weekend_prices)
print(f"Example 4 -- Merged prices: {weekday_prices}")
# Output: Example 4 -- Merged prices: {'tea': 15, 'coffee': 30, 'cold coffee': 40}

print("-" * 50)


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Task: Given the dictionary of monthly rent (in rupees) for
# roommates below, write code that:
#   1. Adds a new roommate "Arjun" with rent 8000
#   2. Safely looks up the rent for "Kavita" (not present) using
#      .get() with a default of 0
#   3. Prints the total rent collected using sum(dict.values())
#
# Expected output:
#   Kavita's rent (default 0): 0
#   Total rent collected: <sum including Arjun>

roommate_rent = {"Priya": 9000, "Sanjay": 8500, "Riya": 9500}

# YOUR CODE HERE


# SOLUTION:
# roommate_rent["Arjun"] = 8000
# kavita_rent = roommate_rent.get("Kavita", 0)
# print("Kavita's rent (default 0):", kavita_rent)
# print("Total rent collected:", sum(roommate_rent.values()))


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file we covered:
#   - Creating dictionaries and looking up values by key
#   - Adding, updating, and removing entries (including .pop())
#   - Safe lookups with .get(key, default) to avoid KeyError
#   - Iterating with .keys(), .values(), .items()
#   - Nested dictionaries and merging with .update()
#
# Next up: day06_04_sets_comprehensions.py -- unique collections
# and compact ways to build lists/dicts/sets.
