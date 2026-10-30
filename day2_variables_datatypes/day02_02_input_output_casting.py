"""
Day 02 — Variables & Data Types (Part 2: Input, Output & Type Casting)
=========================================================================

What this file covers:
    - input() and print() — getting data in, sending data out
    - print() formatting options (sep, end, f-strings)
    - Type casting with int(), float(), str()

Prerequisites:
    - Day 01: Python environment set up
    - Day 02 Part 1: Core data types (int, float, str, bool) and type()

How to run:
    $ python day02_02_input_output_casting.py
"""

# ════════════════════════════════════════════════════════════════
# SECTION 1: input() — Reading from the User
# ════════════════════════════════════════════════════════════════
# input() always pauses a program and waits for the user to type
# something, then ENTER. Importantly: input() ALWAYS returns a str,
# even if the user types a number.

# ── Simulated input ──
user_city = input("Enter your city: ")
user_age_text = input("Enter your age: ")

print("City entered:", user_city)
print("Age entered (as text):", user_age_text)
print(type(user_age_text))   # <class 'str'>  <-- always a string!

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 2: print() — Formatting Output
# ════════════════════════════════════════════════════════════════

# ── Multiple values, custom separator ──
print("Mumbai", "Delhi", "Pune", sep=" | ")
# Output: Mumbai | Delhi | Pune

# ── Custom line ending ──
print("Loading", end="...")
print("done!")
# Output: Loading...done!

# ── f-strings (preferred modern formatting) ──
name = "Arjun"
balance = 2500.75
print(f"{name}'s wallet balance is Rs. {balance}")
# Output: Arjun's wallet balance is Rs. 2500.75

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# SECTION 3: Type Casting — Converting Between Types
# ════════════════════════════════════════════════════════════════
# Since input() always gives a str, you must CAST it to int/float
# before doing math with it.

age_text = "23"             # str, e.g. from input()
age_number = int(age_text)  # cast str -> int
print(age_number + 1)       # 24  (math now works!)

price_text = "149.99"
price_number = float(price_text)  # cast str -> float
print(price_number * 2)           # 299.98

# Casting the other direction: number -> str (useful for concatenation)
score = 95
message = "Your score is " + str(score)
print(message)  # Your score is 95

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════════

# Example 1: Simulated age-based greeting prep (no real input() used)
raw_age = "30"  # simulating input("Enter age: ")
age = int(raw_age)
print(f"In 5 years, you will be {age + 5} years old.")

print("-" * 50)

# Example 2: Auto-rickshaw fare calculator using casted input
raw_distance_km = "6.5"  # simulating input("Distance in km: ")
distance_km = float(raw_distance_km)
fare = 30 + (distance_km * 17)  # base fare + per-km rate
print(f"Estimated auto fare for {distance_km} km: Rs. {fare:.2f}")

print("-" * 50)

# Example 3: Combining str and numbers safely with f-strings
buyer_name = "Sanjay Verma"
items_bought = 4
total_amount = 1380.0
print(f"{buyer_name} bought {items_bought} items for a total of Rs. {total_amount}")

print("-" * 50)

# Example 4: Round-trip casting (str -> int -> str)
ticket_number_text = "1042"
ticket_number = int(ticket_number_text)
ticket_number += 1  # next ticket
next_ticket_text = str(ticket_number)
print("Next ticket number:", next_ticket_text)

print("-" * 50)

# ════════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════════
# Simulate two inputs:
#   raw_items = "5"      (number of items bought)
#   raw_price = "99.50"  (price per item)
# Cast them to the right types, calculate the total cost,
# and print: "Total: Rs. <total>" using an f-string.
#
# Expected output:
#   Total: Rs. 497.5

# YOUR CODE HERE


# SOLUTION:
# raw_items = "5"
# raw_price = "99.50"
# items = int(raw_items)
# price = float(raw_price)
# total = items * price
# print(f"Total: Rs. {total}")

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
# Covered today (Part 2):
#   - input() always returns a string
#   - print() formatting: sep, end, and f-strings
#   - Type casting with int(), float(), str() to convert between types
#
# Next session (Day 3): Control Flow — if/elif/else, comparison and
# logical operators, nested conditions, and the match statement.

if __name__ == "__main__":
    pass
