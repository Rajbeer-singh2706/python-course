"""
Day 3 — Practice Problems (Part 2 of 2)
Topic: match statement + Mixed Challenges (Day 2 + Day 3 combined)

Cumulative scope: Day 2 (variables, types, casting) + Day 3 (if/elif/else,
comparison & logical operators, nesting, match statement)

Difficulty legend:
    🟢 Warm-up   — direct application of one concept
    🟡 Core      — combines 2+ ideas, requires some thought
    🔴 Challenge — multi-step reasoning, edge cases

Section index:
    B (cont.) — match Statement
    E — Mixed Challenges (Day 2 + Day 3 end-to-end)

How to run:
    python day03_practise_problems_02_match_mixed.py
    (Requires Python 3.10 or newer)
"""

# ════════════════════════════════════════════════════════
# SECTION — match Statement
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION: match Statement")
print("=" * 50)

# --- Problem 1 ---
# 🟢 Warm-up
# Use match to print the weekday name for day_num = 5.
#   1 Monday, 2 Tuesday, 3 Wednesday, 4 Thursday, 5 Friday, 6 Saturday, 7 Sunday
#   anything else -> "Invalid day"
# Expected output: Friday

day_num = 5

# YOUR CODE HERE


# SOLUTION:
# match day_num:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")

print("-" * 50)

# --- Problem 2 ---
# 🟢 Warm-up
# Use match to print a vehicle's wheel category for vehicle_type = "auto".
#   "bike" | "scooter"  -> "Two-wheeler"
#   "auto" | "car"       -> "Four-wheeler-ish"  (note: just match literally as required)
#   "truck" | "bus"      -> "Heavy vehicle"
#   anything else         -> "Unknown vehicle"
# Expected output: Four-wheeler-ish

vehicle_type = "auto"

# YOUR CODE HERE


# SOLUTION:
# match vehicle_type:
#     case "bike" | "scooter":
#         print("Two-wheeler")
#     case "auto" | "car":
#         print("Four-wheeler-ish")
#     case "truck" | "bus":
#         print("Heavy vehicle")
#     case _:
#         print("Unknown vehicle")

print("-" * 50)

# --- Problem 3 ---
# 🟡 Core
# Use match with a guard clause to categorize an exam score (0-100):
#   score >= 90        -> "Distinction"
#   score >= 60         -> "First Class"
#   score >= 35         -> "Pass"
#   else                -> "Fail"
# Use: score = 91
# Expected output: Distinction

score = 91

# YOUR CODE HERE


# SOLUTION:
# match score:
#     case s if s >= 90:
#         print("Distinction")
#     case s if s >= 60:
#         print("First Class")
#     case s if s >= 35:
#         print("Pass")
#     case _:
#         print("Fail")

print("-" * 50)

# --- Problem 4 ---
# 🟡 Core
# Use match to route a UPI app transaction status to a message:
#   "success"  -> "Payment successful"
#   "pending"  -> "Payment pending, please wait"
#   "failed"   -> "Payment failed, try again"
#   anything else -> "Unknown status"
# Use: txn_status = "pending"
# Expected output: Payment pending, please wait

txn_status = "pending"

# YOUR CODE HERE


# SOLUTION:
# match txn_status:
#     case "success":
#         print("Payment successful")
#     case "pending":
#         print("Payment pending, please wait")
#     case "failed":
#         print("Payment failed, try again")
#     case _:
#         print("Unknown status")

print("-" * 50)

# --- Problem 5 ---
# 🔴 Challenge
# Use match with guard clauses to set a delivery ETA message based on
# city_tier (1, 2, or 3) AND is_express (bool):
#   city_tier == 1 and is_express  -> "Delivery in 1 day"
#   city_tier == 1                  -> "Delivery in 2 days"
#   city_tier == 2 and is_express  -> "Delivery in 2 days"
#   city_tier == 2                  -> "Delivery in 4 days"
#   city_tier == 3                  -> "Delivery in 6 days"
#   anything else                   -> "Delivery unavailable"
# Use: city_tier = 2, is_express = True
# Expected output: Delivery in 2 days

city_tier = 2
is_express = True

# YOUR CODE HERE


# SOLUTION:
# match city_tier:
#     case 1 if is_express:
#         print("Delivery in 1 day")
#     case 1:
#         print("Delivery in 2 days")
#     case 2 if is_express:
#         print("Delivery in 2 days")
#     case 2:
#         print("Delivery in 4 days")
#     case 3:
#         print("Delivery in 6 days")
#     case _:
#         print("Delivery unavailable")


# ════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges (Day 2 + Day 3, end-to-end)
# ════════════════════════════════════════════════════════

print("=" * 50)
print("SECTION E: Mixed Challenges")
print("=" * 50)

# --- Problem E1 ---
# 🔴 Challenge
# Priya enters her cart total as a string (from a form). Convert it to a
# float, then use if/elif/else to apply BigBasket's delivery rule:
#   total >= 600  -> "Free delivery"
#   total >= 300   -> "Delivery charge: Rs.25"
#   else            -> "Delivery charge: Rs.40"
# Use: cart_total_str = "450.50"
# Expected output: Delivery charge: Rs.25

cart_total_str = "450.50"

# YOUR CODE HERE


# SOLUTION:
# cart_total = float(cart_total_str)
# if cart_total >= 600:
#     print("Free delivery")
# elif cart_total >= 300:
#     print("Delivery charge: Rs.25")
# else:
#     print("Delivery charge: Rs.40")

print("-" * 50)

# --- Problem E2 ---
# 🔴 Challenge
# Arjun's BMI category checker. Compute BMI = weight_kg / (height_m ** 2),
# then use match with guard clauses to print the category:
#   bmi < 18.5          -> "Underweight"
#   18.5 <= bmi < 25     -> "Normal"
#   25 <= bmi < 30        -> "Overweight"
#   bmi >= 30             -> "Obese"
# Use: weight_kg = 72, height_m = 1.75
# Expected output: Normal (BMI ~23.5)

weight_kg = 72
height_m = 1.75

# YOUR CODE HERE


# SOLUTION:
# bmi = weight_kg / (height_m ** 2)
# match bmi:
#     case b if b < 18.5:
#         print("Underweight")
#     case b if b < 25:
#         print("Normal")
#     case b if b < 30:
#         print("Overweight")
#     case _:
#         print("Obese")

print("-" * 50)

# --- Problem E3 ---
# 🔴 Challenge
# Sanjay applies for an e-commerce "Super Coin" reward tier. Combine
# logical operators AND a match-based tier lookup:
#   Step 1: is_eligible = (orders_this_year >= 10) and (total_spent_rs >= 5000)
#   Step 2: if is_eligible, use match on total_spent_rs to assign a tier:
#       total_spent_rs >= 20000  -> "Gold"
#       total_spent_rs >= 10000   -> "Silver"
#       else                       -> "Bronze"
#     if NOT eligible -> print "Not eligible for rewards"
# Use: orders_this_year = 12, total_spent_rs = 15500
# Expected output: Silver

orders_this_year = 12
total_spent_rs = 15500

# YOUR CODE HERE


# SOLUTION:
# is_eligible = (orders_this_year >= 10) and (total_spent_rs >= 5000)
# if is_eligible:
#     match total_spent_rs:
#         case s if s >= 20000:
#             print("Gold")
#         case s if s >= 10000:
#             print("Silver")
#         case _:
#             print("Bronze")
# else:
#     print("Not eligible for rewards")

print("-" * 50)

# --- Problem E4 ---
# 🔴 Challenge
# Riya Deshmukh wants to know if she should carry an umbrella when
# heading out in Mumbai. Build the full decision using nested
# conditionals + logical operators (NOT match, for variety):
#   - input values come in as strings (simulate form input) and must be
#     cast to the right types first
#   - if rain_chance_percent >= 60 OR (is_monsoon_season and rain_chance_percent >= 30):
#       -> "Carry an umbrella"
#     else:
#       -> "Umbrella not needed"
# Use: rain_chance_str = "40", is_monsoon_season = True
# Expected output: Carry an umbrella

rain_chance_str = "40"
is_monsoon_season = True

# YOUR CODE HERE


# SOLUTION:
# rain_chance_percent = int(rain_chance_str)
# if rain_chance_percent >= 60 or (is_monsoon_season and rain_chance_percent >= 30):
#     print("Carry an umbrella")
# else:
#     print("Umbrella not needed")


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   match Statement (5 problems)
#   E — Mixed Challenges (4 problems)
#
# Combined with day03_practise_problems_01_conditionals.py:
#   Total problems across both files: 25
#   Difficulty breakdown: 7 Warm-up | 9 Core | 9 Challenge
#
# Next: Day 4 practice problems — Loops (for, while, range, break/continue/pass)
