"""
Day 4 — Practice Problems: Loops
=================================

Cumulative scope : Variables & Data Types (Day 2), Control Flow (Day 3),
                    Loops (Day 4)
Difficulty legend : 🟢 Warm-up   🟡 Core   🔴 Challenge

Section index
-------------
  A. Prior Days Review        (variables, data types, control flow)
  B. for loops & range()
  C. while loops
  D. break / continue / pass / loop-else
  E. Mixed Challenges

Run with: python day04_practise_problems.py
Every problem has a prompt, a starter "YOUR CODE HERE" block, and a
commented-out SOLUTION block beneath it. Uncomment a SOLUTION block to
check your work.
"""

print("═" * 50)
print("SECTION A: Prior Days Review")
print("═" * 50)

# ── Problem A1 ── 🟢 Warm-up
# Priya's age is stored below. Print whether she is a "minor" or
# "adult" (18+) using an if/else statement (Day 3 concept).
priya_age = 20

# YOUR CODE HERE

# SOLUTION:
# if priya_age >= 18:
#     print("Priya is an adult.")
# else:
#     print("Priya is a minor.")

print("-" * 50)

# ── Problem A2 ── 🟢 Warm-up
# Convert the string price below into a float, then print it
# formatted as "Rs <price>" with 2 decimal places (Day 2 concept).
price_str = "349.5"

# YOUR CODE HERE

# SOLUTION:
# price_float = float(price_str)
# print(f"Rs {price_float:.2f}")

print("-" * 50)

# ── Problem A3 ── 🟡 Core
# Given the temperature below, print "Hot" if above 35, "Pleasant" if
# between 20 and 35 (inclusive), otherwise print "Cold". Use elif.
delhi_temp = 38

# YOUR CODE HERE

# SOLUTION:
# if delhi_temp > 35:
#     print("Hot")
# elif 20 <= delhi_temp <= 35:
#     print("Pleasant")
# else:
#     print("Cold")


print("\n" + "═" * 50)
print("SECTION B: for loops & range()")
print("═" * 50)

# ── Problem B1 ── 🟢 Warm-up
# Print numbers 1 through 10 (inclusive) using a for loop with range().

# YOUR CODE HERE

# SOLUTION:
# for n in range(1, 11):
#     print(n, end=" ")
# print()

print("-" * 50)

# ── Problem B2 ── 🟢 Warm-up
# Loop through the list of Mumbai railway stations below and print
# each one prefixed with "Station: ".
stations = ["Churchgate", "Dadar", "Andheri", "Borivali"]

# YOUR CODE HERE

# SOLUTION:
# for station in stations:
#     print(f"Station: {station}")

print("-" * 50)

# ── Problem B3 ── 🟡 Core
# Print all even numbers from 2 to 20 (inclusive) using range() with
# a step argument (no `if` check needed).

# YOUR CODE HERE

# SOLUTION:
# for n in range(2, 21, 2):
#     print(n, end=" ")
# print()

print("-" * 50)

# ── Problem B4 ── 🟡 Core
# Arjun's weekly expenses (rupees) are below. Use a for loop to
# calculate and print the total.
weekly_expenses = [450, 1200, 300, 800, 600, 150, 900]

# YOUR CODE HERE

# SOLUTION:
# total = 0
# for expense in weekly_expenses:
#     total += expense
# print(f"Total weekly expense: Rs {total}")

print("-" * 50)

# ── Problem B5 ── 🔴 Challenge
# Print a multiplication table for the number 7, from 7x1 to 7x10,
# formatted as "7 x 1 = 7", "7 x 2 = 14", etc.

# YOUR CODE HERE

# SOLUTION:
# number = 7
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


print("\n" + "═" * 50)
print("SECTION C: while loops")
print("═" * 50)

# ── Problem C1 ── 🟢 Warm-up
# Use a while loop to print numbers from 5 down to 1.

# YOUR CODE HERE

# SOLUTION:
# n = 5
# while n >= 1:
#     print(n, end=" ")
#     n -= 1
# print()

print("-" * 50)

# ── Problem C2 ── 🟡 Core
# Riya has Rs 2000 in savings and adds Rs 250 every month. Use a while
# loop to print her balance each month until it reaches or exceeds
# Rs 3000. Also print how many months it took.
balance = 2000
monthly_savings = 250

# YOUR CODE HERE

# SOLUTION:
# months = 0
# while balance < 3000:
#     balance += monthly_savings
#     months += 1
#     print(f"Month {months}: Rs {balance}")
# print(f"Reached target in {months} months.")

print("-" * 50)

# ── Problem C3 ── 🟡 Core
# Use a while loop to find the first power of 2 that exceeds 1000,
# printing each power of 2 along the way (1, 2, 4, 8, ...).

# YOUR CODE HERE

# SOLUTION:
# power = 1
# while power <= 1000:
#     print(power, end=" ")
#     power *= 2
# print(f"\nFirst power of 2 exceeding 1000: {power}")

print("-" * 50)

# ── Problem C4 ── 🔴 Challenge
# Simulate a countdown for a Mumbai local train departure. Starting at
# 10 seconds, count down to 0 using a while loop, printing "T-minus X"
# for each second, and print "Departed!" once the countdown reaches 0.

# YOUR CODE HERE

# SOLUTION:
# seconds = 10
# while seconds >= 0:
#     print(f"T-minus {seconds}")
#     seconds -= 1
# print("Departed!")


print("\n" + "═" * 50)
print("SECTION D: break / continue / pass / loop-else")
print("═" * 50)

# ── Problem D1 ── 🟢 Warm-up
# Loop through the numbers 1 to 20. Stop the loop completely (break)
# as soon as you find a number divisible by 13.

# YOUR CODE HERE

# SOLUTION:
# for n in range(1, 21):
#     if n % 13 == 0:
#         print(f"Found: {n}")
#         break

print("-" * 50)

# ── Problem D2 ── 🟡 Core
# Loop through the list of order amounts below. Use `continue` to skip
# any order under Rs 100 (too small to process), and print the rest
# prefixed with "Processing order: Rs ".
order_amounts = [50, 250, 80, 600, 30, 1200]

# YOUR CODE HERE

# SOLUTION:
# for amount in order_amounts:
#     if amount < 100:
#         continue
#     print(f"Processing order: Rs {amount}")

print("-" * 50)

# ── Problem D3 ── 🟡 Core
# The list below contains employee IDs. Search for the ID "EMP104".
# Use for...else: if found, print "Employee found" and break; if the
# loop completes without finding it, print "Employee not found".
employee_ids = ["EMP101", "EMP102", "EMP103", "EMP105"]
search_id = "EMP104"

# YOUR CODE HERE

# SOLUTION:
# for emp_id in employee_ids:
#     if emp_id == search_id:
#         print("Employee found")
#         break
# else:
#     print("Employee not found")

print("-" * 50)

# ── Problem D4 ── 🔴 Challenge
# Loop through numbers 1 to 30. Use `pass` for multiples of 5 (do
# nothing — placeholder for future logic), use `continue` to skip
# multiples of 3 (but not 5), and print all other numbers.

# YOUR CODE HERE

# SOLUTION:
# for n in range(1, 31):
#     if n % 5 == 0:
#         pass  # placeholder: multiples of 5 handled elsewhere later
#     elif n % 3 == 0:
#         continue
#     else:
#         print(n, end=" ")
# print()


print("\n" + "═" * 50)
print("SECTION E: Mixed Challenges")
print("═" * 50)

# ── Problem E1 ── 🔴 Challenge
# Sanjay Verma's kirana store tracks daily customer counts for a week.
# Using a for loop, calculate the total and average customers per day.
# Then, using a second loop with break, find and print the first day
# (1-indexed) where customer count exceeded 100.
daily_customers = [85, 92, 110, 78, 95, 120, 88]

# YOUR CODE HERE

# SOLUTION:
# total = 0
# for count in daily_customers:
#     total += count
# average = total / len(daily_customers)
# print(f"Total customers: {total}, Average: {average:.2f}")
#
# for day_index, count in enumerate(daily_customers, start=1):
#     if count > 100:
#         print(f"Day {day_index} was the first to exceed 100 customers ({count}).")
#         break

print("-" * 50)

# ── Problem E2 ── 🔴 Challenge
# A vending machine in Delhi accepts coins until the total reaches or
# exceeds Rs 20 (price of a snack). Coins are inserted one at a time
# from the list below. Use a while loop to add coins, print the
# running total, and stop (break) once Rs 20 or more is reached.
# If all coins are inserted and Rs 20 is still not reached, use the
# while...else clause to print "Insufficient funds — transaction
# cancelled."
coins_inserted = [5, 2, 5, 1, 2]  # rupees, simulating coin insertions

# YOUR CODE HERE

# SOLUTION:
# total_inserted = 0
# i = 0
# while i < len(coins_inserted):
#     total_inserted += coins_inserted[i]
#     print(f"Inserted Rs {coins_inserted[i]}, total so far: Rs {total_inserted}")
#     if total_inserted >= 20:
#         print("Snack dispensed!")
#         break
#     i += 1
# else:
#     print("Insufficient funds — transaction cancelled.")

print("-" * 50)

# ── Problem E3 ── 🔴 Challenge
# Combine everything: loop through the list of (name, marks) tuples
# below. Skip any student with marks below 0 (data entry error, use
# continue). Stop processing entirely if a mark above 100 is found
# (invalid data, use break, and print which student caused it).
# Otherwise, classify each valid student as "Pass" (marks >= 40) or
# "Fail", and keep a running count of passes.
student_marks = [
    ("Priya", 78),
    ("Arjun", -5),
    ("Riya Deshmukh", 39),
    ("Sanjay Verma", 105),
    ("Kavita", 92),
]

# YOUR CODE HERE

# SOLUTION:
# pass_count = 0
# for student_name, marks in student_marks:
#     if marks < 0:
#         print(f"{student_name}: invalid negative marks, skipping.")
#         continue
#     if marks > 100:
#         print(f"{student_name}: marks {marks} exceed 100 — invalid data, stopping.")
#         break
#     result = "Pass" if marks >= 40 else "Fail"
#     if result == "Pass":
#         pass_count += 1
#     print(f"{student_name}: {marks} -> {result}")
# print(f"Total passes counted before stop: {pass_count}")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Sections covered:
#   A. Prior Days Review        — 3 problems
#   B. for loops & range()      — 5 problems
#   C. while loops               — 4 problems
#   D. break/continue/pass/else  — 4 problems
#   E. Mixed Challenges          — 3 problems
#   Total: 19 problems
#
# Difficulty breakdown: 🟢 Warm-up x5  🟡 Core x9  🔴 Challenge x5
#
# Next problem set (Day 5): Functions & Scope — defining functions,
# parameters, return values, *args/**kwargs, and the LEGB scope rule.

if __name__ == "__main__":
    print("\nDay 4 practice problems file ran successfully — no errors!")
