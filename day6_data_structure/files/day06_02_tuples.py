"""
Day 6 — Data Structures
File 2 of 4: Tuples — immutability, packing, and unpacking

What this file covers:
    - Creating tuples and how they differ from lists
    - Why immutability matters and what it protects against
    - Packing and unpacking values
    - Common real-world use cases for tuples

Prerequisites:
    - day06_01_lists.py (lists, indexing, slicing)

How to run:
    python3 day06_02_tuples.py
"""


# ════════════════════════════════════════════════════════════
# SECTION A — Creating Tuples
# ════════════════════════════════════════════════════════════
# A tuple looks like a list but uses round brackets, and once
# created its contents CANNOT change. Use a tuple whenever a value
# should stay fixed -- like GPS coordinates or a date of birth.

print("═" * 50)
print("SECTION A: Creating Tuples")
print("═" * 50)

mumbai_coordinates = (19.0760, 72.8777)
print("Mumbai coordinates:", mumbai_coordinates)
print("Type:", type(mumbai_coordinates))
# Output:
# Mumbai coordinates: (19.076, 72.8777)
# Type: <class 'tuple'>

# A single-item tuple needs a trailing comma, otherwise Python
# treats the parentheses as just grouping (not a tuple).
single_item = ("Delhi",)
not_a_tuple = ("Delhi")
print("single_item type:", type(single_item))     # tuple
print("not_a_tuple type:", type(not_a_tuple))      # str
# Output:
# single_item type: <class 'tuple'>
# not_a_tuple type: <class 'str'>

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION B — Immutability
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION B: Immutability")
print("═" * 50)

# Indexing and slicing work exactly like lists (read-only access).
print("Latitude:", mumbai_coordinates[0])
print("Both values:", mumbai_coordinates[:])
# Output:
# Latitude: 19.076
# Both values: (19.076, 72.8777)

# Trying to modify a tuple raises a TypeError.
try:
    mumbai_coordinates[0] = 20.0
except TypeError as error:
    print("Error caught:", error)
# Output: Error caught: 'tuple' object does not support item assignment

print("-" * 50)


# ════════════════════════════════════════════════════════════
# SECTION C — Packing and Unpacking
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("SECTION C: Packing & Unpacking")
print("═" * 50)

# Packing: combining several values into one tuple.
student_record = ("Arjun", 21, "Delhi")
print("Packed tuple:", student_record)

# Unpacking: splitting a tuple back into separate variables.
name, age, city = student_record
print(f"Unpacked -- name: {name}, age: {age}, city: {city}")
# Output:
# Packed tuple: ('Arjun', 21, 'Delhi')
# Unpacked -- name: Arjun, age: 21, city: Delhi

print("-" * 50)

# The star operator (*) can capture "the rest" during unpacking.
exam_scores_tuple = (91, 88, 76, 65, 59, 40)
highest, *middle, lowest = exam_scores_tuple
print("Highest:", highest)
print("Middle scores:", middle)
print("Lowest:", lowest)
# Output:
# Highest: 91
# Middle scores: [88, 76, 65, 59]
# Lowest: 40

print("-" * 50)

# Swapping two variables -- a very common tuple-packing trick.
price_today, price_yesterday = 450, 480
price_today, price_yesterday = price_yesterday, price_today
print(f"After swap -- today: {price_today}, yesterday: {price_yesterday}")
# Output: After swap -- today: 480, yesterday: 450

print("-" * 50)


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════
print("═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# Example 1: Returning multiple values from a function using a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)

daily_temps = [28, 31, 27, 33, 29]
lowest_temp, highest_temp = get_min_max(daily_temps)
print(f"Example 1 -- Lowest: {lowest_temp}C, Highest: {highest_temp}C")
# Output: Example 1 -- Lowest: 27C, Highest: 33C

# Example 2: Storing a fixed set of RGB-like values for a UI theme
navy_theme_color = (30, 58, 95)  # (R, G, B)
print(f"Example 2 -- Navy theme RGB: {navy_theme_color}")
# Output: Example 2 -- Navy theme RGB: (30, 58, 95)

# Example 3: A list of tuples representing (city, population in lakhs)
city_population = [("Mumbai", 200), ("Delhi", 190), ("Bengaluru", 130)]
for city_name, population in city_population:
    print(f"Example 3 -- {city_name}: {population} lakhs")
# Output:
# Example 3 -- Mumbai: 200 lakhs
# Example 3 -- Delhi: 190 lakhs
# Example 3 -- Bengaluru: 130 lakhs

# Example 4: Using a tuple as a dictionary key (lists cannot do this!)
distance_lookup = {("Mumbai", "Pune"): 150, ("Delhi", "Agra"): 230}
print(f"Example 4 -- Mumbai to Pune: {distance_lookup[('Mumbai', 'Pune')]} km")
# Output: Example 4 -- Mumbai to Pune: 150 km

print("-" * 50)


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Task: Given the tuple below representing a train journey
# (train_name, source, destination, duration_hours), unpack it into
# four separate variables and print a formatted sentence describing
# the journey.
#
# Expected output:
#   Rajdhani Express travels from Mumbai to Delhi in 16 hours.

train_journey = ("Rajdhani Express", "Mumbai", "Delhi", 16)

# YOUR CODE HERE


# SOLUTION:
# train_name, source, destination, duration_hours = train_journey
# print(f"{train_name} travels from {source} to {destination} in {duration_hours} hours.")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# In this file we covered:
#   - Creating tuples and the single-item trailing-comma rule
#   - Why tuples are immutable and the TypeError it raises
#   - Packing values into a tuple and unpacking with * for "the rest"
#   - Real use cases: fixed records, function returns, dict keys
#
# Next up: day06_03_dictionaries.py -- key-value pairs and how to
# look up data safely.
