"""
Day 3 — Control Flow (Part 2 of 2)
Topic: The match statement (Python 3.10+)

What this file covers:
    - Basic match / case syntax
    - Matching literal values
    - The wildcard pattern (_)
    - Combining multiple values in one case (the | operator)
    - Guard clauses with `if` inside a case

Prerequisites:
    - Day 2: Variables & Data Types
    - day03_01_conditionals_operators.py (if / elif / else, comparison & logical operators)

How to run:
    python day03_02_match_statement.py
    (Requires Python 3.10 or newer)
"""

# ════════════════════════════════════════════════════════
# SECTION 1: Why match? (vs. if/elif chains)
# ════════════════════════════════════════════════════════
#
# `match` is Python's structural pattern matching statement,
# introduced in Python 3.10. It's often a cleaner alternative to
# long if/elif/elif/else chains when you're comparing ONE variable
# against many possible values.

# ── Concept: Basic match/case ──
day_number = 3

match day_number:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case _:                      # _ is the wildcard — matches anything else
        day_name = "Unknown day"

print(f"Day {day_number} is {day_name}")   # Output: Day 3 is Wednesday

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 2: Combining values with |  (the "or" pattern)
# ════════════════════════════════════════════════════════

# ── Concept: Matching multiple values in one case ──
month = "July"

match month:
    case "December" | "January" | "February":
        season = "Winter"
    case "March" | "April" | "May":
        season = "Summer"
    case "June" | "July" | "August" | "September":
        season = "Monsoon"
    case _:
        season = "Post-Monsoon"

print(f"{month} falls in the {season} season in India.")
# Output: July falls in the Monsoon season in India.

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION 3: Guard clauses — adding conditions to a case
# ════════════════════════════════════════════════════════
#
# A guard clause lets you attach an extra `if` condition to a
# case, so it only matches when BOTH the pattern AND the condition
# are true.

# ── Concept: case with a guard ──
order_amount = 1800

match order_amount:
    case amount if amount >= 2000:
        delivery_charge = 0
    case amount if amount >= 1000:
        delivery_charge = 20
    case _:
        delivery_charge = 40

print(f"Order: Rs.{order_amount} -> Delivery charge: Rs.{delivery_charge}")
# Output: Order: Rs.1800 -> Delivery charge: Rs.20


# ════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════

print("=" * 50)
print("GUIDED EXAMPLE 1: Swiggy order status messages")
print("=" * 50)

order_status = "out_for_delivery"

match order_status:
    case "placed":
        message = "Arjun's order has been placed."
    case "preparing":
        message = "The restaurant is preparing Arjun's food."
    case "out_for_delivery":
        message = "Arjun's order is on the way!"
    case "delivered":
        message = "Order delivered. Enjoy your meal, Arjun!"
    case _:
        message = "Unknown order status."

print(message)
# Output: Arjun's order is on the way!

print("=" * 50)
print("GUIDED EXAMPLE 2: Indian metro city fare zone (with guard clauses)")
print("=" * 50)

city_name = "Delhi"
distance_km = 14

match city_name:
    case "Mumbai" | "Delhi" if distance_km > 10:
        fare_zone = "Zone 3 (Long distance)"
    case "Mumbai" | "Delhi":
        fare_zone = "Zone 1/2 (Short distance)"
    case _:
        fare_zone = "Not a metro city"

print(f"{city_name}, {distance_km} km -> {fare_zone}")
# Output: Delhi, 14 km -> Zone 3 (Long distance)

print("=" * 50)
print("GUIDED EXAMPLE 3: Exam grade lookup using match")
print("=" * 50)

percentage = 67

match percentage:
    case p if p >= 90:
        grade = "A+"
    case p if p >= 75:
        grade = "A"
    case p if p >= 60:
        grade = "B"
    case p if p >= 40:
        grade = "C"
    case _:
        grade = "Fail"

print(f"Riya scored {percentage}% -> Grade {grade}")
# Output: Riya scored 67% -> Grade B

print("=" * 50)
print("GUIDED EXAMPLE 4: Payment method routing")
print("=" * 50)

payment_method = "upi"

match payment_method:
    case "upi" | "netbanking":
        processing_fee = 0
    case "credit_card":
        processing_fee = 25
    case "cod":
        processing_fee = 40
    case _:
        processing_fee = 50

print(f"Payment via {payment_method} -> Processing fee: Rs.{processing_fee}")
# Output: Payment via upi -> Processing fee: Rs.0


# ════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════
#
# Sanjay is booking an IRCTC train ticket. Using `match`, set
# `berth_preference_msg` based on `berth_code`:
#   "LB" or "UB"          -> "Lower/Upper berth confirmed"
#   "SL"                  -> "Side Lower berth confirmed"
#   "RAC"                 -> "RAC — partial confirmation"
#   anything else          -> "Waitlisted"
#
# Use: berth_code = "SL"
# Expected output: "Side Lower berth confirmed"

berth_code = "SL"

# YOUR CODE HERE


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Covered in this file:
#   1. Basic match / case syntax
#   2. The wildcard pattern (_)
#   3. Combining values with | inside a case
#   4. Guard clauses (case ... if ...)
#
# Coming up next (Day 4): Loops — for, while, range(), break/continue/pass
