"""
Day 5 — Functions & Scope — Practice Problems
File 3 of 3: Scope & LEGB + Mixed Challenges

Difficulty legend:
    🟢 Warm-up   — straightforward, single concept
    🟡 Core      — combines a couple of ideas
    🔴 Challenge — requires more careful thinking

Section index (this file):
    Section D — Scope & the LEGB Rule
    Section E — Mixed Challenges (combines Day 5 + earlier days)

How to run:
    python day05_practise_problems_03_scope_mixed.py
"""

# ════════════════════════════════════════════════════════
# SECTION D — Scope & the LEGB Rule
# ════════════════════════════════════════════════════════

# --------------------------------------------------------
# Problem D1  🟢 Warm-up
# --------------------------------------------------------
# There is a global variable `shop_name = "Delhi Electronics"`.
# Write a function `print_shop_name()` that prints the global
# variable (no need to modify it, just read it).

shop_name = "Delhi Electronics"

# YOUR CODE HERE


# SOLUTION:
# def print_shop_name():
#     print(shop_name)
#
# print_shop_name()  # Output: Delhi Electronics

print("-" * 50)

# --------------------------------------------------------
# Problem D2  🟡 Core
# --------------------------------------------------------
# There is a global variable `stock_count = 50`.
# Write a function `sell_item(quantity)` that uses the `global`
# keyword to reduce `stock_count` by `quantity`.
# Call it twice — once with 5, once with 10 — then print the
# final `stock_count`.

stock_count = 50

# YOUR CODE HERE


# SOLUTION:
# def sell_item(quantity):
#     global stock_count
#     stock_count -= quantity
#
# sell_item(5)
# sell_item(10)
# print(stock_count)  # Output: 35

print("-" * 50)

# --------------------------------------------------------
# Problem D3  🟡 Core
# --------------------------------------------------------
# Write a function `outer_trip_planner()` that:
#   - Defines a local variable `mode = "Flight"`
#   - Defines a nested function `inner_details()` that reads and
#     prints `mode` from the enclosing scope
#   - Calls `inner_details()` from inside `outer_trip_planner()`
# Call `outer_trip_planner()` to test it.

# YOUR CODE HERE


# SOLUTION:
# def outer_trip_planner():
#     mode = "Flight"
#
#     def inner_details():
#         print(f"Travel mode: {mode}")
#
#     inner_details()
#
# outer_trip_planner()  # Output: Travel mode: Flight

print("-" * 50)

# --------------------------------------------------------
# Problem D4  🔴 Challenge
# --------------------------------------------------------
# Predict the output BEFORE running, then write code to verify it.
# Given:
#
#   value = "Global"
#
#   def outer():
#       value = "Enclosing"
#
#       def inner():
#           value = "Local"
#           print(value)
#
#       inner()
#       print(value)
#
#   outer()
#   print(value)
#
# Write out the three print statements' results as comments, then
# actually run the code below to check yourself.

# YOUR CODE HERE (write your prediction as a comment, then the code)


# SOLUTION:
# # Prediction: Local, Enclosing, Global
# value = "Global"
#
# def outer():
#     value = "Enclosing"
#
#     def inner():
#         value = "Local"
#         print(value)
#
#     inner()
#     print(value)
#
# outer()
# print(value)
# # Output:
# # Local
# # Enclosing
# # Global

print("-" * 50)


# ════════════════════════════════════════════════════════
# SECTION E — Mixed Challenges
# ════════════════════════════════════════════════════════

# --------------------------------------------------------
# Problem E1  🔴 Challenge
# --------------------------------------------------------
# Write a function `bus_ticket_price(age, *stops, is_student=False, **extra)`
# that:
#   - Charges a base fare of Rs. 20 per stop (use len(stops))
#   - Applies a 50% discount to the total if age < 12
#   - Applies a 20% discount to the total if is_student is True
#     (only one discount applies — prefer the age discount if both apply)
#   - Adds any extra charges from `extra` (e.g. luggage_fee=10) to the
#     final total after discounts
#   - Returns the final price
#
# Test with a 10-year-old riding 3 stops, and a student aged 20 riding
# 5 stops with a luggage_fee=15.

# YOUR CODE HERE


# SOLUTION:
# def bus_ticket_price(age, *stops, is_student=False, **extra):
#     base_total = len(stops) * 20
#     if age < 12:
#         base_total *= 0.5
#     elif is_student:
#         base_total *= 0.8
#     extra_charges = sum(extra.values())
#     return base_total + extra_charges
#
# print(bus_ticket_price(10, "Stop1", "Stop2", "Stop3"))
# # Output: 30.0
#
# print(bus_ticket_price(20, "Stop1", "Stop2", "Stop3", "Stop4", "Stop5",
#                         is_student=True, luggage_fee=15))
# # Output: 95.0

print("-" * 50)

# --------------------------------------------------------
# Problem E2  🔴 Challenge
# --------------------------------------------------------
# Write a function `batch_report(batch_name, *scores)` that:
#   - Uses a global variable `total_batches_processed` (starts at 0)
#     and increments it by 1 using the `global` keyword each time
#     the function is called
#   - Returns a tuple of (average_score, highest_score, lowest_score)
#     using the *scores passed in (assume at least one score is given)
#   - Prints the batch name and the returned tuple
#
# Call it for two different batches with different score lists, then
# print `total_batches_processed` at the end.

total_batches_processed = 0

# YOUR CODE HERE


# SOLUTION:
# def batch_report(batch_name, *scores):
#     global total_batches_processed
#     total_batches_processed += 1
#     average_score = sum(scores) / len(scores)
#     highest_score = max(scores)
#     lowest_score = min(scores)
#     result = (average_score, highest_score, lowest_score)
#     print(f"{batch_name}: {result}")
#     return result
#
# batch_report("Batch A", 80, 90, 70)
# batch_report("Batch B", 60, 75, 95, 88)
# print(f"Total batches processed: {total_batches_processed}")
# # Output:
# # Batch A: (80.0, 90, 70)
# # Batch B: (79.5, 95, 60)
# # Total batches processed: 2

print("-" * 50)

# --------------------------------------------------------
# Problem E3  🔴 Challenge
# --------------------------------------------------------
# Write a function `mumbai_delivery_slip(customer_name, *items, **meta)`
# that combines everything from Day 5:
#   - Uses a default keyword argument `discount_percent=0` inside meta
#     handling (i.e. read it with meta.get("discount_percent", 0))
#   - Calculates a subtotal assuming each item in *items costs a flat
#     Rs. 50 (i.e. subtotal = 50 * number_of_items)
#   - Applies the discount percentage to the subtotal
#   - Returns the final amount, rounded to 2 decimal places
#
# Test it with:
#   mumbai_delivery_slip("Riya Deshmukh", "Rice", "Dal", "Oil", "Sugar",
#                         discount_percent=10, area="Mumbai")

# YOUR CODE HERE


# SOLUTION:
# def mumbai_delivery_slip(customer_name, *items, **meta):
#     discount_percent = meta.get("discount_percent", 0)
#     subtotal = 50 * len(items)
#     final_amount = subtotal - (subtotal * discount_percent / 100)
#     return round(final_amount, 2)
#
# print(mumbai_delivery_slip("Riya Deshmukh", "Rice", "Dal", "Oil", "Sugar",
#                             discount_percent=10, area="Mumbai"))
# # Output: 180.0

print("-" * 50)


# ════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════
#
# Sections in this file:
#   D. Scope & LEGB Rule       — 4 problems
#   E. Mixed Challenges        — 3 problems
#
# Difficulty breakdown: 1x 🟢 Warm-up, 2x 🟡 Core, 4x 🔴 Challenge
#
# ── Full Day 5 Practice Set Overview ──
#   File 1: Prior Days Review + Function Basics  (8 problems)
#   File 2: *args and **kwargs                    (5 problems)
#   File 3: Scope & LEGB + Mixed Challenges        (7 problems)
#   TOTAL: 20 problems
#
# Next up: Day 6 — Data Structures (lists, tuples, dicts, sets,
# comprehensions, and slicing).
