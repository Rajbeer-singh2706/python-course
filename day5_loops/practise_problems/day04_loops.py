"""
Day 4 — Loops
=============

Topic       : for loop, while loop, range(), break / continue / pass, else on loops
Prereqs     : Day 2 (Variables & Data Types), Day 3 (Control Flow)
Run with    : python day04_loops.py

What this file covers
----------------------
1. The for loop and iterating over sequences
2. range() and its three forms
3. The while loop
4. break, continue, and pass
5. The else clause on loops (a Python-specific feature)
6. Four guided examples using Mumbai/Delhi shopping & travel scenarios
7. A mini-challenge at the end

Read this file top to bottom like a tutorial — every section is runnable
on its own when you run the whole file with `python day04_loops.py`.
"""

# ════════════════════════════════════════════════════════════
# SECTION 1 — The for loop
# ════════════════════════════════════════════════════════════
# A `for` loop walks through items in a sequence (string, list, tuple, etc.)
# one at a time, running the indented block for each item.

print("═" * 50)
print("SECTION 1: The for loop")
print("═" * 50)

# ── Looping over a list ──
cities = ["Mumbai", "Delhi", "Pune", "Jaipur"]

for city in cities:
    print(f"Visiting: {city}")
# Output:
# Visiting: Mumbai
# Visiting: Delhi
# Visiting: Pune
# Visiting: Jaipur

print("-" * 50)

# ── Looping over a string ──
# Strings are sequences too, so you can loop character by character.
name = "Arjun"
for letter in name:
    print(letter, end=" ")
print()  # newline after the loop
# Output: A r j u n


# ════════════════════════════════════════════════════════════
# SECTION 2 — range()
# ════════════════════════════════════════════════════════════
# range() generates a sequence of numbers. It has three forms:
#   range(stop)              -> 0, 1, 2, ..., stop-1
#   range(start, stop)       -> start, start+1, ..., stop-1
#   range(start, stop, step) -> start, start+step, start+2*step, ...

print("\n" + "═" * 50)
print("SECTION 2: range()")
print("═" * 50)

# ── range(stop) ──
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()
# Output: 0 1 2 3 4

# ── range(start, stop) ──
print("range(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print()
# Output: 2 3 4 5 6

# ── range(start, stop, step) ──
print("range(10, 0, -2):")
for i in range(10, 0, -2):
    print(i, end=" ")
print()
# Output: 10 8 6 4 2

print("-" * 50)

# ── Using range() with rupee amounts ──
print("Monthly savings target (in rupees), increasing by 500 each month:")
for month in range(1, 6):
    target = 1000 + (month - 1) * 500
    print(f"Month {month}: Rs {target}")


# ════════════════════════════════════════════════════════════
# SECTION 3 — The while loop
# ════════════════════════════════════════════════════════════
# A `while` loop keeps running as long as its condition stays True.
# You are responsible for changing something inside the loop so it
# eventually becomes False — otherwise you get an infinite loop!

print("\n" + "═" * 50)
print("SECTION 3: The while loop")
print("═" * 50)

# ── Basic while loop ──
count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1  # without this line, the loop would never end
# Output: Count is 1 ... Count is 5

print("-" * 50)

# ── while loop simulating a wallet balance countdown ──
wallet_balance = 250  # rupees
item_price = 60

while wallet_balance >= item_price:
    wallet_balance -= item_price
    print(f"Bought one item. Remaining balance: Rs {wallet_balance}")
print(f"Not enough money left to buy another item (Rs {wallet_balance} remaining).")


# ════════════════════════════════════════════════════════════
# SECTION 4 — break, continue, and pass
# ════════════════════════════════════════════════════════════
# break    -> exits the loop immediately
# continue -> skips the rest of this iteration, moves to the next one
# pass     -> does nothing; a placeholder so the code is syntactically valid

print("\n" + "═" * 50)
print("SECTION 4: break, continue, pass")
print("═" * 50)

# ── break: stop searching once found ──
delivery_cities = ["Pune", "Nagpur", "Mumbai", "Indore"]
target = "Mumbai"

for c in delivery_cities:
    if c == target:
        print(f"Found {target}! Stopping search.")
        break
    print(f"Checked {c}, not a match.")

print("-" * 50)

# ── continue: skip items that don't meet a condition ──
print("Even numbers only, from 1 to 10:")
for n in range(1, 11):
    if n % 2 != 0:
        continue  # skip odd numbers
    print(n, end=" ")
print()
# Output: 2 4 6 8 10

print("-" * 50)

# ── pass: placeholder while planning code structure ──
for n in range(1, 6):
    if n == 3:
        pass  # TODO: handle the special case for 3 later
    else:
        print(f"Processing item {n}")


# ════════════════════════════════════════════════════════════
# SECTION 5 — else clause on loops
# ════════════════════════════════════════════════════════════
# A loop's `else` block runs ONLY IF the loop completes WITHOUT hitting
# a `break`. This is a Python-specific feature most other languages
# don't have, and it's handy for "search and report" patterns.

print("\n" + "═" * 50)
print("SECTION 5: else clause on loops")
print("═" * 50)

# ── for...else: search that completes normally ──
stock = ["Rice", "Dal", "Atta", "Sugar"]
needed = "Oil"

for item in stock:
    if item == needed:
        print(f"{needed} is in stock!")
        break
else:
    # Runs because the loop finished without finding "Oil"
    print(f"{needed} is NOT in stock — add to shopping list.")

print("-" * 50)

# ── while...else ──
attempts = 0
max_attempts = 3
correct_pin = "4321"
entered_pin = "0000"  # simulating a wrong guess every time (no real input())

while attempts < max_attempts:
    attempts += 1
    if entered_pin == correct_pin:
        print("PIN accepted!")
        break
    print(f"Attempt {attempts}: incorrect PIN.")
else:
    print("Maximum attempts reached. Card blocked.")


# ════════════════════════════════════════════════════════════
# GUIDED EXAMPLES
# ════════════════════════════════════════════════════════════

print("\n" + "═" * 50)
print("GUIDED EXAMPLES")
print("═" * 50)

# ── Example 1: Auto-rickshaw fare meter simulation ──
print("\nExample 1: Auto-rickshaw fare meter (Mumbai)")
base_fare = 26       # rupees for first 1.5 km
per_km_rate = 17      # rupees per additional km
total_km = 8

fare = base_fare
for km in range(1, total_km):
    fare += per_km_rate
    print(f"  After {km + 1} km: Rs {fare}")
print(f"Final fare for {total_km} km: Rs {fare}")

print("-" * 50)

# ── Example 2: Sum and average of cricket scores ──
print("\nExample 2: Riya's cricket scores this season")
scores = [45, 67, 12, 89, 34, 56]
total_runs = 0

for score in scores:
    total_runs += score

average = total_runs / len(scores)
print(f"  Scores: {scores}")
print(f"  Total runs: {total_runs}")
print(f"  Average: {average:.2f}")

print("-" * 50)

# ── Example 3: Validating a list of pincodes with continue ──
print("\nExample 3: Filtering valid Mumbai pincodes (must start with '400')")
pincodes = ["400001", "110001", "400072", "560001", "400099"]
valid_pincodes = []

for pin in pincodes:
    if not pin.startswith("400"):
        continue
    valid_pincodes.append(pin)

print(f"  All pincodes checked: {pincodes}")
print(f"  Valid Mumbai pincodes: {valid_pincodes}")

print("-" * 50)

# ── Example 4: ATM withdrawal simulation using while + break ──
print("\nExample 4: ATM withdrawal simulation")
account_balance = 5000
withdrawal_requests = [1000, 2000, 1500, 3000]  # simulating sequential requests

i = 0
while i < len(withdrawal_requests):
    request = withdrawal_requests[i]
    if request > account_balance:
        print(f"  Request of Rs {request} declined — insufficient balance (Rs {account_balance}).")
        break
    account_balance -= request
    print(f"  Withdrew Rs {request}. Remaining balance: Rs {account_balance}")
    i += 1


# ════════════════════════════════════════════════════════════
# MINI-CHALLENGE
# ════════════════════════════════════════════════════════════
# Sanjay Verma runs a small kirana store in Delhi. He has a list of
# daily sales (in rupees) for the past 10 days. Write code that:
#   1. Loops through the sales list
#   2. Skips any day with sales of 0 (store was closed) using `continue`
#   3. Stops counting immediately (using `break`) if any day's sales
#      exceed Rs 10,000 (flag for review — unusually high, possibly an error)
#   4. Prints the running total of valid sales days processed before
#      the loop stopped
#
# Expected output (for the sample data below) should show each valid
# day's sales, skip day 4 (closed), and stop at day 8 with a "flagged
# for review" message before printing the running total.

daily_sales = [4500, 6200, 0, 3100, 7800, 5400, 12500, 4900, 6100]

# YOUR CODE HERE
# running_total = 0
# for day_index, sales in enumerate(daily_sales, start=1):
#     ...

# SOLUTION:
# running_total = 0
# for day_index, sales in enumerate(daily_sales, start=1):
#     if sales == 0:
#         print(f"Day {day_index}: store closed, skipping.")
#         continue
#     if sales > 10000:
#         print(f"Day {day_index}: Rs {sales} flagged for review — stopping count.")
#         break
#     running_total += sales
#     print(f"Day {day_index}: Rs {sales} (running total: Rs {running_total})")
# print(f"\nFinal running total before stop: Rs {running_total}")


# ════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════
# Today you learned:
#   - for loops iterate over sequences (lists, strings, range(), etc.)
#   - range(start, stop, step) generates number sequences for counting
#   - while loops repeat based on a condition, not a fixed sequence
#   - break exits a loop early; continue skips to the next iteration
#   - pass is a no-op placeholder for incomplete code
#   - else on a loop runs only if the loop was NOT broken out of
#
# Next session (Day 5): Functions & Scope — defining reusable blocks
# of code with def, parameters, return values, *args/**kwargs, and
# the LEGB scope rule.

if __name__ == "__main__":
    print("\nDay 4 concept file ran successfully — no errors!")
