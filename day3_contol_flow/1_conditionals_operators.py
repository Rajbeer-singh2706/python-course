"""
Day 3 — Control Flow (Part 1 of 2)
Topic: if / elif / else, comparison operators, logical operators, nested conditions

What this file covers:
    - Making decisions in code using if / elif / else
    - Comparison operators: == != > < >= <=
    - Logical operators: and / or / not
    - Nested conditionals

Prerequisites:
    - Day 2: Variables & Data Types (int, float, str, bool, input/print, type casting)

How to run:
    python 1_conditionals_operators.py
"""

# ════════════════════════════════════════════════════════
# SECTION 1: Comparison Operators
# ════════════════════════════════════════════════════════
#
# Comparison operators compare two values and always produce a
# boolean result: True or False.
#
#   ==   equal to
#   !=   not equal to
#   >    greater than
#   <    less than
#   >=   greater than or equal to
#   <=   less than or equal to

# ── Comparing Numbers ──
wallet_balance = 1500
item_price = 1200

print(wallet_balance > item_price)   # Output: True  (1500 > 1200)
print(wallet_balance == item_price)  # Output: False (not equal)
print(wallet_balance != item_price)  # Output: True  (they ARE different)

print("-" * 50)

# ── Comparing Strings ──
# Strings are compared character by character, alphabetically
city_a = "Mumbai"
city_b = "Delhi"

print(city_a == city_b)   # Output: False
print(city_a > city_b)    # Output: True  ('M' comes after 'D' alphabetically)

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: if / elif / else
# ════════════════════════════════════════════════════════
#
# An `if` statement runs a block of code ONLY when its condition
# is True. `elif` (else-if) checks another condition if the first
# was False. `else` catches everything else.

# ── Concept: Single if ──
auto_fare = 85
if auto_fare > 50:
    print("This is a long auto ride.")   # Output: This is a long auto ride.

print("-" * 50)

# ── Concept: if / else ──
temperature_mumbai = 34
if temperature_mumbai > 30:
    print("Carry water, it's hot today.")   # Output: Carry water, it's hot today.
else:
    print("Pleasant weather today.")

print("-" * 50)

# ── Concept: if / elif / else (multiple branches) ──
marks = 78

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print(f"Marks: {marks} -> Grade: {grade}")   # Output: Marks: 78 -> Grade: A


# ════════════════════════════════════════════════════════
# SECTION 3: Logical Operators
# ════════════════════════════════════════════════════════
#
# Logical operators combine multiple boolean conditions:
#   and   -> True only if BOTH sides are True
#   or    -> True if AT LEAST ONE side is True
#   not   -> flips True to False and vice versa

age = 22
has_id_card = True

# ── Concept: and ──
if age >= 18 and has_id_card:
    print("Arjun can enter the concert.")   # Output: Arjun can enter the concert.

print("-" * 50)

# ── Concept: or ──
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("Riya can sleep in today.")   # Output: Riya can sleep in today.

print("-" * 50)

# ── Concept: not ──
is_raining = False
if not is_raining:
    print("Sanjay can go for his evening walk.")   # Output: Sanjay can go for his evening walk.


# ════════════════════════════════════════════════════════
# SECTION 4: Nested Conditions
# ════════════════════════════════════════════════════════
#
# An if statement can contain another if statement inside it.
# This lets us check conditions in stages, layer by layer.

account_balance = 5000
is_premium_member = True

if account_balance > 1000:
    print("Balance check passed.")
    if is_premium_member:
        print("Priya gets free same-day delivery.")   # Output: Priya gets free same-day delivery.
    else:
        print("Standard delivery applies.")
else:
    print("Balance too low for checkout.")


# ════════════════════════════════════════════════════════
# GUIDED EXAMPLES — Indian e-commerce / daily-life contexts
# ════════════════════════════════════════════════════════

print("=" * 50)
print("GUIDED EXAMPLE 1: Metro ticket pricing (Delhi Metro)")
print("=" * 50)

distance_km = 18

if distance_km <= 2:
    fare = 10
elif distance_km <= 5:
    fare = 20
elif distance_km <= 12:
    fare = 30
elif distance_km <= 21:
    fare = 40
else:
    fare = 50

print(f"Distance: {distance_km} km -> Fare: Rs.{fare}")
# Output: Distance: 18 km -> Fare: Rs.40

print("=" * 50)
print("GUIDED EXAMPLE 2: Flipkart Big Billion Days discount eligibility")
print("=" * 50)

cart_value = 2200
is_flipkart_plus_member = True

if cart_value >= 2000 and is_flipkart_plus_member:
    print("Arjun gets free delivery + 10% extra discount.")
elif cart_value >= 2000:
    print("Arjun gets free delivery only.")
else:
    print("No special offers apply to this order.")
# Output: Arjun gets free delivery + 10% extra discount.

print("=" * 50)
print("GUIDED EXAMPLE 3: Mumbai local train pass eligibility (nested)")
print("=" * 50)

age_years = 16
is_student = True

if age_years < 18:
    if is_student:
        print("Riya Deshmukh is eligible for a concession pass.")
    else:
        print("Riya Deshmukh needs a regular child ticket.")
else:
    print("Adult fare applies.")
# Output: Riya Deshmukh is eligible for a concession pass.

print("=" * 50)
print("GUIDED EXAMPLE 4: Weather-based outfit suggestion (Bengaluru vs Mumbai)")
print("=" * 50)

city = "Mumbai"
humidity_percent = 85
temperature_c = 33

if city == "Mumbai" and humidity_percent > 70 and temperature_c > 30:
    print("Sanjay Verma should wear light cotton clothes today.")
else:
    print("Regular clothing is fine today.")
# Output: Sanjay Verma should wear light cotton clothes today.


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Priya is shopping on Myntra. Write a program that decides her
# discount based on these rules:
#   - If cart_value >= 3000 AND she has a coupon -> 25% discount
#   - elif cart_value >= 3000 (no coupon)         -> 15% discount
#   - elif cart_value >= 1000                      -> 5% discount
#   - else                                          -> no discount
#
# Use: cart_value = 3500, has_coupon = True
# Expected output: "Discount: 25%"

cart_value = 3500
has_coupon = True

# YOUR CODE HERE


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Covered in this file:
#   1. Comparison operators (== != > < >= <=)
#   2. if / elif / else branching
#   3. Logical operators (and / or / not)
#   4. Nested conditionals
#
# Coming up next in day03_02_match_statement.py:
#   - Python's match statement (structural pattern matching, 3.10+)
